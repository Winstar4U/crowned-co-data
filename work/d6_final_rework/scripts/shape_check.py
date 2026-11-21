"""Independent shape-fit check for D6 placement WARN rows (read-only, local).
For every enabled placeholder: rasterize the blueprint's own SVG safe shape (raw, no extra margin), map every
content pixel (QA content mask: alpha>16, or |rgb-corner|>40 for opaque art; max-pooled so no pixel is lost)
through the proposed placement, and report % inside the shape, % inside the best single sub-polygon, and the
minimum clearance (in placeholder px) from content to the shape edge. Usage: python3 -I shape_check.py <qa.csv> <out.json>"""
import csv, json, math, os, re, sys
import numpy as np
from PIL import Image, ImageDraw
from scipy import ndimage
Image.MAX_IMAGE_PIXELS = None
W = '/home/user/crowned-co-data/work'
NUM = r"-?\d*\.?\d+(?:e-?\d+)?"
B1_SVG = {69370: "69049eb1a4e7ea51b50fcc72", 74403: "69049ec89e9751aadf0e2bff", 147746: "68e9049b60083c38900efad2",
          147745: "69774192bd641e3540096f92", 147747: "6979cc1691e7e99fd60cd7b2", 147748: "6979cc293a08be45a200a782",
          130091: "68bea94d8f0bc1a7bd0b1282"}

def attr(t, n):
    m = re.search(r'\b%s="([^"]*)"' % re.escape(n), t); return m.group(1) if m else None

def path_polys(d):
    from svg.path import parse_path, Move
    if not re.fullmatch(r"[0-9A-Za-z.,\-\s]+", d or ""): return []
    polys, cur = [], []
    for seg in parse_path(d):
        if isinstance(seg, Move):
            if len(cur) > 2: polys.append(cur)
            cur = [(seg.end.real, seg.end.imag)]; continue
        n = 2 if seg.__class__.__name__ in ("Line", "Close") else 32
        for i in range(1, n + 1):
            p = seg.point(i / n); cur.append((p.real, p.imag))
    if len(cur) > 2: polys.append(cur)
    return polys

def shape(fp):
    s = open(fp, encoding="utf-8", errors="replace").read()
    bg = re.search(r'<rect id="color_background"[^>]*>', s)
    if not bg: return None
    t = bg.group(0); bx, by = float(attr(t, "x") or 0), float(attr(t, "y") or 0)
    bw, bh = float(attr(t, "width")), float(attr(t, "height"))
    polys, kind = [], 'rect'
    for m in re.finditer(r'<(rect|circle|polygon|path) id="(safew|safe|safe area|Safe area|Safe Area)"[^>]*>', s):
        tag, el = m.group(1), m.group(0); kind = 'printify_safe_area'
        if tag == 'rect':
            x, y, w, h = [float(attr(el, k) or 0) for k in ('x', 'y', 'width', 'height')]
            pp = [[(x, y), (x + w, y), (x + w, y + h), (x, y + h)]]
        elif tag == 'circle':
            cx, cy, r = [float(attr(el, k)) for k in ('cx', 'cy', 'r')]
            pp = [[(cx + r * math.cos(a), cy + r * math.sin(a)) for a in np.linspace(0, 2 * math.pi, 360)]]
        elif tag == 'polygon':
            v = [float(z) for z in re.findall(NUM, attr(el, 'points'))]; pp = [list(zip(v[0::2], v[1::2]))]
        else: pp = path_polys(attr(el, 'd'))
        tf = attr(el, 'transform') or ''
        for op, args in reversed(re.findall(r'(translate|rotate|matrix)\(([^)]*)\)', tf)):  # rightmost first
            a = [float(z) for z in re.findall(NUM, args)]
            if op == 'translate': f = lambda X, Y, a=a: (X + a[0], Y + (a[1] if len(a) > 1 else 0))
            elif op == 'rotate':
                t = math.radians(a[0]); c0, s0 = (a[1], a[2]) if len(a) == 3 else (0, 0)
                f = lambda X, Y, t=t, c0=c0, s0=s0: (c0 + (X - c0) * math.cos(t) - (Y - s0) * math.sin(t), s0 + (X - c0) * math.sin(t) + (Y - s0) * math.cos(t))
            else: f = lambda X, Y, a=a: (a[0] * X + a[2] * Y + a[4], a[1] * X + a[3] * Y + a[5])
            pp = [[f(X, Y) for X, Y in q] for q in pp]
        for q in pp:
            key = tuple(round(c, 1) for pt in q[:4] for c in pt)
            if key not in [tuple(round(c, 1) for pt in z[:4] for c in pt) for z in polys]: polys.append(q)
    if polys: pass
    else:
        m = re.search(r'<g id="outlines">\s*<g id="front">\s*<path d="([^"]+)"', s)
        if m: polys = path_polys(m.group(1)); kind = 'printify_print_outline'
    return dict(kind=kind if polys else 'rect', polys=[[((x - bx) / bw, (y - by) / bh) for x, y in p] for p in polys])

def raster(polys, mw, mh):
    m = Image.new('L', (mw, mh), 0); d = ImageDraw.Draw(m)
    for p in polys: d.polygon([(u * mw, v * mh) for u, v in p], fill=255)
    return np.array(m) > 127

def content_mask(im, cap=1000):
    a = np.array(im.convert('RGBA'))
    if a[..., 3].min() < 250: m = a[..., 3] > 16
    else:
        c = a[0, 0, :3].astype(int); m = np.abs(a[..., :3].astype(int) - c).sum(2) > 40
    h, w = m.shape; f = max(1, math.ceil(max(h, w) / cap))
    if f > 1:  # max-pool: any content pixel in the block counts
        H, Wd = math.ceil(h / f) * f, math.ceil(w / f) * f
        p = np.zeros((H, Wd), bool); p[:h, :w] = m; m = p.reshape(H // f, f, Wd // f, f).any((1, 3))
    return m

def check(pid, batch, pl_override=None, art=None):
    d = f'{W}/d6_batch{batch}/{pid}'; j = json.load(open(d + '/placement.json'))
    prods = {json.loads(l)['product_id']: json.loads(l) for l in open(f'{W}/d6_batch{batch}/products.jsonl')}
    p = prods[pid]; bp = j['blueprint_id']
    views = json.load(open(f'{W}/d6_batch1/_svg/views.json')) if str(batch) == '1' else {}
    im = Image.open(art or d + '/original.png'); iw, ih = im.size
    cm = content_mask(im); ch, cw = cm.shape
    ys, xs = np.nonzero(cm); u_img = (xs + 0.5) / cw; v_img = (ys + 0.5) / ch
    # include pixel extents (corners of each content cell) for conservativeness
    du, dv = 0.5 / cw, 0.5 / ch
    per = {}
    for vid, (PW, PH) in j['placeholders'].items():
        if pl_override: pr = pl_override.get(vid, pl_override.get('_all'))
        else: pr = (j.get('proposed_per_variant_group') or {}).get(vid, j['proposed'])
        if str(batch) == '1': sid = B1_SVG.get(int(vid)) or (views.get(str(bp)) or [None])[0]
        else: sid = (p.get('svgs') or {}).get(vid) or p.get('svg')
        fp = f'{W}/d6_batch{batch}/_svg/{sid}.svg'
        sh = shape(fp) if sid and os.path.exists(fp) else None
        k = 1600 / max(PW, PH); mw, mh = max(8, round(PW * k)), max(8, round(PH * k))
        polys = (sh or {}).get('polys') or [[(0, 0), (1, 0), (1, 1), (0, 1)]]
        uni = raster(polys, mw, mh)
        aw = pr['scale'] * PW; ah = aw * ih / iw
        res = {}
        for name, msk in [('union', uni)] + [(f'poly{i}', raster([q], mw, mh)) for i, q in enumerate(polys)] if len(polys) > 1 else [('union', uni)]:
            ok = np.ones(len(xs), bool)
            for sx in (-du, du):
                for sy in (-dv, dv):
                    X = (pr['x'] * PW - aw / 2 + (u_img + sx) * aw) / PW; Y = (pr['y'] * PH - ah / 2 + (v_img + sy) * ah) / PH
                    iu = np.floor(X * mw).astype(int); iv = np.floor(Y * mh).astype(int)
                    inb = (iu >= 0) & (iu < mw) & (iv >= 0) & (iv < mh)
                    o = np.zeros(len(xs), bool); o[inb] = msk[iv[inb], iu[inb]]; ok &= o
            res[name] = float(ok.mean())
        # clearance: distance transform of the union shape, sampled at content pixels (centres)
        dt = ndimage.distance_transform_edt(uni) / k  # placeholder px
        X = (pr['x'] * PW - aw / 2 + u_img * aw) / PW; Y = (pr['y'] * PH - ah / 2 + v_img * ah) / PH
        iu = np.clip(np.floor(X * mw).astype(int), 0, mw - 1); iv = np.clip(np.floor(Y * mh).astype(int), 0, mh - 1)
        clear = float(dt[iv, iu].min()) if len(xs) else 0.0
        dto = ndimage.distance_transform_edt(~uni) / k  # distance OUTSIDE the shape, placeholder px
        Xo = (pr['x'] * PW - aw / 2 + u_img * aw) / PW; Yo = (pr['y'] * PH - ah / 2 + v_img * ah) / PH
        offc = (Xo < 0) | (Xo >= 1) | (Yo < 0) | (Yo >= 1)
        over = float(dto[iv, iu].max()) if len(xs) else 0.0
        if offc.any(): over = max(over, float(max(0, -Xo.min(), Xo.max() - 1) * PW), float(max(0, -Yo.min(), Yo.max() - 1) * PH))
        cell = max(PW, PH) / 1600
        per[vid] = dict(svg=sid, kind=(sh or {}).get('kind', 'rect(no svg)'), n_polys=len(polys), W=PW, H=PH,
                        placement=pr, inside_union=res['union'],
                        inside_best_poly=max(v for k_, v in res.items() if k_.startswith('poly')) if len(polys) > 1 else res['union'],
                        clearance_px=round(clear, 1), overflow_px=round(over, 1), raster_cell_px=round(cell, 2), clearance_frac_short=round(clear / min(PW, PH), 4),
                        src_print_ratio=round(iw / aw, 3))
    return dict(product_id=pid, batch=batch, blueprint=bp, variants=per,
                inside_min=min(v['inside_union'] for v in per.values()),
                inside_best_poly_min=min(v['inside_best_poly'] for v in per.values()),
                clearance_frac_min=min(v['clearance_frac_short'] for v in per.values()),
                overflow_cells_max=max(v['overflow_px'] / v['raster_cell_px'] for v in per.values()),
                ratio_min=min(v['src_print_ratio'] for v in per.values()))

if __name__ == '__main__':
    rows = [r for r in csv.DictReader(open(sys.argv[1])) if r['qa_status'] == 'WARN']
    out = []
    for r in rows:
        try: out.append(check(r['product_id'], r['batch']))
        except Exception as e: out.append(dict(product_id=r['product_id'], batch=r['batch'], error=repr(e)))
        x = out[-1]; print(x['product_id'], x.get('blueprint'), x.get('inside_min'), x.get('inside_best_poly_min'), x.get('clearance_frac_min'), x.get('overflow_cells_max'), x.get('error', ''))
    json.dump(out, open(sys.argv[2], 'w'), indent=1)
