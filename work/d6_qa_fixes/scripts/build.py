"""D6 QA-fix build: placements, final art, QA (B's metrics), before/after renders, contact sheets, results.csv.
NON-LIVE. Read-only on Printify (variant sizes were read once via printify-get-blueprint-variants; physical sizes are
from those variant titles). No uploads/writes. Run: python3 -I build.py <scratchpad_dir_with_sr_outputs>
QA math is copied verbatim from winstar-recovery/qa/qa_placements.py (bbox, inside fraction, src/print px ratio)
and qa_repaired_art.py (transparency, border, checker), applied PER VARIANT with that variant's placement."""
import csv, glob, hashlib, json, os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage as nd
Image.MAX_IMAGE_PIXELS = None
W = '/home/user/crowned-co-data/work'; O = W + '/d6_qa_fixes'; BR = '/home/user/winstar4u/my-projects/winstar-recovery'
SP = sys.argv[1]; TF = W + '/d6_new_art/text_fix'
os.makedirs(O + '/art', exist_ok=True); os.makedirs(O + '/placements', exist_ok=True); os.makedirs(O + '/before_after', exist_ok=True)
try: FONT = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 15); FONTB = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 17)
except Exception: FONT = FONTB = ImageFont.load_default()

# physical width in inches per variant (from Printify variant titles, blueprint-variants read 2026-11-20)
PHYS = {'41653': 71, '112701': 58, '112702': 58, '113861': 10, '113862': 22, '244223': 12, '244224': 18, '244225': 16, '244226': 18, '244227': 20, '244228': 24}
VTITLE = {'147745': 'King', '147746': 'Queen', '147747': 'Twin', '147748': 'Twin XL', '41653': '71x74 in', '112701': '58x58 in', '112702': '58x102 in',
          '113861': '10x10 in', '113862': '22x22 in', '244224': '12x18 in lumbar', '244226': '18x18 in', '244227': '20x20 in', '244228': '24x24 in',
          '70900': 'White 12M', '70904': 'White 18M', '71073': 'Blue 3-6M', '71089': 'Blue NB', '72006': '2 in', '72007': '3 in', '72008': '4 in', '72009': '5 in', '72010': '6 in'}
BLANK = {'71073': (150, 190, 228), '71089': (150, 190, 228)}  # baby blue; everything else white

def pj(pid):
    d = glob.glob(f'{W}/d6_batch*/{pid}')[0]; return d, json.load(open(d + '/placement.json'))
def sha1(f): return hashlib.sha1(open(f, 'rb').read()).hexdigest()

# ---- B's QA functions (verbatim logic) ----
def bbox(im):
    a = np.array(im.convert('RGBA'))
    if a[..., 3].min() < 250: m = a[..., 3] > 16; mode = 'alpha'
    else:
        c = a[0, 0, :3].astype(int); m = np.abs(a[..., :3].astype(int) - c).sum(2) > 40; mode = 'opaque_bg'
    ys, xs = np.where(m); h, w = m.shape
    return (xs.min() / w, ys.min() / h, (xs.max() + 1) / w, (ys.max() + 1) / h), mode
def geom(bb, iw, ih, pr, W_, H_):
    bx0, by0, bx1, by1 = bb
    aw = pr['scale'] * W_; ah = aw * ih / iw; cx = pr['x'] * W_; cy = pr['y'] * H_
    x0 = cx - aw / 2 + bx0 * aw; x1 = cx - aw / 2 + bx1 * aw; y0 = cy - ah / 2 + by0 * ah; y1 = cy - ah / 2 + by1 * ah
    ix = max(0, min(x1, W_) - max(x0, 0)); iy = max(0, min(y1, H_) - max(y0, 0))
    return ix * iy / ((x1 - x0) * (y1 - y0)), iw / aw
def checker(a):
    op = a[..., 3] > 200; g = a[..., :3].astype(int)
    light = (g.min(2) > 185) & (np.ptp(g, 2) < 12) & op
    if light.sum() < 2000: return 0.0
    d = np.abs(g[:, 16:, 0] - g[:, :-16, 0]); m = light[:, 16:] & light[:, :-16] & (d > 20) & (d < 70)
    return m.mean() * 100
def art_metrics(im):
    a = np.array(im.convert('RGBA')); al = a[..., 3]; transp = (al < 10).mean() * 100
    b = np.concatenate([al[0], al[-1], al[:, 0], al[:, -1]]); border = (b > 128).mean() * 100
    return transp, border, checker(a)

# ---- placement helpers ----
def recentre(bb, iw, ih, pr, W_, H_, s_new):
    """keep the content centre where it was under placement pr, change scale to s_new"""
    bx0, by0, bx1, by1 = bb; aw = pr['scale'] * W_; ah = aw * ih / iw
    ccx = pr['x'] * W_ - aw / 2 + (bx0 + bx1) / 2 * aw; ccy = pr['y'] * H_ - ah / 2 + (by0 + by1) / 2 * ah
    aw2 = s_new * W_; ah2 = aw2 * ih / iw
    x = (ccx - aw2 * ((bx0 + bx1) / 2 - 0.5)) / W_; y = (ccy - ah2 * ((by0 + by1) / 2 - 0.5)) / H_
    return {'x': round(x, 4), 'y': round(y, 4), 'scale': round(s_new, 4), 'angle': 0}
def fit_centre(bb, iw, ih, W_, H_, margin=0.02):
    bx0, by0, bx1, by1 = bb
    s = min((1 - 2 * margin) / (bx1 - bx0), (1 - 2 * margin) * H_ / ((by1 - by0) * W_ * ih / iw))
    return recentre(bb, iw, ih, {'x': 0.5 - ((bx0 + bx1) / 2 - 0.5) * s, 'y': 0.5 - ((by0 + by1) / 2 - 0.5) * s * W_ * ih / iw / H_, 'scale': s}, W_, H_, s)

def qa(art_file, per_var, ph, dec, repaired, native_px=None):
    """per_var: {vid: placement}. Returns dict with B-style metrics."""
    im = Image.open(art_file); iw, ih = im.size; bb, mode = bbox(im)
    rows = {}; worst_in = 1.0; min_ratio = 9; worst_v = None
    for vid, (W_, H_) in ph.items():
        f, r = geom(bb, iw, ih, per_var[vid], W_, H_)
        nat = (native_px / iw * r) if native_px else r
        ppi = (W_ / PHYS[vid]) if vid in PHYS else None
        rows[vid] = dict(inside=round(f, 4), ratio=round(r, 3), nominal_dpi=round(r * 300), native_ratio=round(nat, 3), native_nominal_dpi=round(nat * 300),
                         physical_dpi=(round(r * ppi) if ppi else None), placeholder_ppi=(round(ppi) if ppi else None))
        worst_in = min(worst_in, f)
        if r < min_ratio: min_ratio = r; worst_v = vid
    issues = []
    if worst_in < 0.999: issues.append(f'GEOMETRY: only {worst_in:.1%} of content inside placeholder')
    if min_ratio < 0.33: issues.append(f'RESOLUTION: src/print px ratio {min_ratio:.2f} (<0.33)')
    elif min_ratio < 0.5: issues.append(f'RESOLUTION-WARN: src/print px ratio {min_ratio:.2f} (<0.5)')
    if mode == 'opaque_bg':
        c = np.array(im.convert('RGB'))[0, 0]
        if not (c.min() > 235 and 'sublimation' in dec): issues.append(f'TRANSPARENCY-WARN: opaque background rgb{tuple(int(v) for v in c)} on {dec}; blank is white')
    transp, border, chk = art_metrics(im)
    if repaired:
        if transp < 1 and dec in ('dtf', 'dtg', 'embroidery', 'direct-to-fabric'): issues.append('opaque art (no transparency) on garment/fabric decoration')
        if chk > 0.5: issues.append(f'possible checkerboard residue score {chk:.2f}')
        if border > 5: issues.append(f'art touches canvas edge ({border:.0f}% of border opaque) [WARN]')
    hard = [x for x in issues if not ('WARN' in x.split(':')[0] or x.endswith('[WARN]'))]
    b_verdict = 'FAIL' if hard else ('WARN' if issues else 'PASS')
    return dict(px=(iw, ih), bbox=[round(v, 4) for v in bb], mode=mode, per_variant=rows, inside_min=worst_in, ratio_min=min_ratio, worst_variant=worst_v,
                transparent_pct=round(transp, 1), border_opaque_pct=round(border, 1), checker=round(chk, 2), issues=issues, b_verdict=b_verdict)

# ---- rendering ----
def place_on(canvas_px, art, pr, W_, H_, blank, max_side):
    s = max_side / max(W_, H_); cw, ch = int(W_ * s), int(H_ * s)
    cv = Image.new('RGBA', (cw, ch), blank + (255,))
    aw = pr['scale'] * W_ * s; ah = aw * art.height / art.width
    if aw > 2 and ah > 2:
        a = art.copy(); a.thumbnail((max(1, int(aw * 2)), max(1, int(ah * 2))), Image.LANCZOS); a = a.resize((max(1, int(round(aw))), max(1, int(round(ah)))), Image.LANCZOS)
        tmp = Image.new('RGBA', (cw, ch), (0, 0, 0, 0)); tmp.paste(a, (int(round(pr['x'] * cw - aw / 2)), int(round(pr['y'] * ch - ah / 2))), a)
        cv = Image.alpha_composite(cv, tmp)
    return cv.convert('RGB')
def detail(art, pr, W_, H_, fx, fy, win=360, blank=(255, 255, 255)):
    """what the printer gets: a win x win window of PRINT pixels around art point (fx,fy) (normalised art coords)"""
    iw, ih = art.size; aw = pr['scale'] * W_; ratio = iw / aw
    cx, cy = fx * iw, fy * ih; half = win / 2 * ratio
    box = (int(cx - half), int(cy - half), int(cx + half), int(cy + half))
    c = art.crop(box).resize((win, win), Image.BICUBIC)
    bg = Image.new('RGBA', (win, win), blank + (255,)); bg.alpha_composite(c.convert('RGBA')); return bg.convert('RGB')
def detail_point(art):
    a = art.convert('RGBA'); a.thumbnail((400, 400)); g = np.asarray(a.convert('L')).astype(float); al = np.asarray(a)[..., 3] > 30
    e = np.abs(nd.sobel(g, 0)) + np.abs(nd.sobel(g, 1)); e[~al] = 0; e = nd.uniform_filter(e, 40)
    y, x = np.unravel_index(np.argmax(e), e.shape); return x / e.shape[1], y / e.shape[0]
def panel(img, lines, w):
    img = img.copy(); img.thumbnail((w, 10000)); P = Image.new('RGB', (w, img.height + 22 * len(lines) + 8), (40, 40, 44))
    P.paste(img, ((w - img.width) // 2, 0)); d = ImageDraw.Draw(P)
    for i, t in enumerate(lines): d.text((6, img.height + 4 + 22 * i), t, fill=(255, 255, 255) if i else (255, 220, 120), font=FONT if i else FONTB)
    return P
def compose(title, row1, row2, out):
    Wd = 1600; n = len(row1); pw = (Wd - 10 * (n + 1)) // n
    P1 = [panel(i, l, pw) for i, l in row1]; h1 = max(p.height for p in P1)
    n2 = len(row2); pw2 = min(380, (Wd - 10 * (n2 + 1)) // max(n2, 1)); P2 = [panel(i, l, pw2) for i, l in row2]; h2 = max([p.height for p in P2] + [0])
    S = Image.new('RGB', (Wd, 40 + h1 + 20 + h2 + 10), (25, 25, 28)); d = ImageDraw.Draw(S); d.text((10, 10), title, fill='white', font=FONTB)
    for i, p in enumerate(P1): S.paste(p, (10 + i * (pw + 10), 40))
    for i, p in enumerate(P2): S.paste(p, (10 + i * (pw2 + 10), 40 + h1 + 20))
    S.save(out, optimize=True); return S

# ---- configuration ----
def tfile(pid): return glob.glob(f'{W}/d6_batch*/{pid}/original.png')[0]
HH_T = tfile('6ac713f042c818a1ad096025')  # transparent cut of nostalgic-happy-holidays-tree (same pixels, mean diff 1.9/255)
HOLES = O + '/art/6ac7149db8146913210038d0_treeup_holes_filled.png'
SRC = {'raccoon': tfile('6ac711cfb32a96bbe40d0c95'), 'openbar': tfile('6ac71200b32a96bbe40d0ca9'), 'tree': tfile('6ac7110850fc6704d30bf925'), 'tree_t': HH_T,
       'skeleton': tfile('6ac7109b35a66ab7dc0b0eea'), 'martini': tfile('6ac7127ab8146913210037cc'), 'candy': TF + '/5fa6bcd6cdbb68aaf4c51c41f42b629bf054ff5e.png',
       'receipt': TF + '/2ddd38528249f1711e9d8812f76490075b8b5392.png', 'treeup': TF + '/f193d6d08b1ad932eb905ac8d3c3c0b6119a8e76.png', 'treeup_t': HOLES,
       'truck': TF + '/9253995681aa7f28db34a5c459a7883d1325add2.png',
       'party': BR + '/regenerated/6ac71204f0a0ce97bc0c9211_upscaled2x.png', 'santa': BR + '/regenerated/6ac711a4b8d5d3e719013158_upscaled2x.png'}
NATIVE_W = {'party': 2048, 'santa': 1702}  # B's files are 2x Lanczos of these native widths
B_FAIL = {}  # repaired-art FAIL file per product (B's qa/repaired_art_qa.csv)
for r in csv.DictReader(open(BR + '/qa/repaired_art_qa.csv')):
    B_FAIL[r['product_id']] = (W + '/' + r['file'].split('crowned-co-data/work/')[1], r)
B_PL = {r['product_id']: r for r in csv.DictReader(open(BR + '/qa/placement_qa_224.csv'))}

ITEMS = [  # pid, item, route, art key/file, issue
    ('6ac71302336f835866011570', 1, 'pillow', None, 'placement FAIL: ~88% content inside lumbar 244224 with shared placement'),
    ('6ac71305fa3cae10170efb32', 1, 'pillow', None, 'placement FAIL: ~88% content inside lumbar 244224 with shared placement'),
    ('6ac71309fa3cae10170efb40', 1, 'pillow', None, 'placement FAIL: ~89% content inside lumbar 244224 with shared placement'),
    ('6ac711cfb32a96bbe40d0c95', 1, 'upscale', 'raccoon', 'placement FAIL: low resolution (ratio 0.12)'),
    ('6ac71200b32a96bbe40d0ca9', 1, 'upscale', 'openbar', 'placement FAIL: low resolution (ratio 0.12)'),
    ('6ac713526356cae0df02e40e', 1, 'motif', HH_T, 'placement FAIL: low resolution (ratio 0.33-)'),
    ('6ac7110850fc6704d30bf925', 1, 'upscale', 'tree', 'placement FAIL: low resolution (ratio 0.29)'),
    ('6ac71308d9b782898109a98a', 1, 'upscale', 'tree_t', 'placement FAIL: low resolution (ratio 0.24)'),
    ('6ac7109b35a66ab7dc0b0eea', 1, 'upscale', 'skeleton', 'placement FAIL: low resolution (ratio 0.28)'),
    ('6ac7127ab8146913210037cc', 1, 'upscale', 'martini', 'placement FAIL: low resolution (ratio 0.18)'),
    ('6ac712d76027ad007d0e7df9', 1, 'upscale', 'skeleton', 'placement FAIL: low resolution (ratio 0.23)'),
    ('6ac7149db8146913210038d0', 2, 'holes', HOLES, 'repaired-art FAIL: speckled see-through holes in TREE UP letters'),
    ('6ac7134483f1a0e50d071df7', 2, 'motif', TF + '/5fa6bcd6cdbb68aaf4c51c41f42b629bf054ff5e.png', 'repaired-art FAIL: LOW-RES ratio 0.32'),
    ('6ac710f0fa3cae10170efa36', 2, 'upscale', 'candy', 'repaired-art FAIL: LOW-RES ratio 0.29'),
    ('6ac712fa42c818a1ad095f97', 2, 'upscale', 'candy', 'repaired-art FAIL: LOW-RES ratio 0.23'),
    ('6ac713e2c077332834034e13', 2, 'motif', TF + '/c0a403dd613bb626349cea50fc11231ffc2ea0ff.png', 'repaired-art FAIL: opaque white bg on fabric + LOW-RES ratio 0.32'),
    ('6ac7115a6356cae0df02e2e9', 2, 'upscale', 'receipt', 'repaired-art FAIL: LOW-RES ratio 0.29'),
    ('6ac711c0a005c19c550d8971', 2, 'upscale', 'treeup_t', 'repaired-art FAIL: opaque white bg on fabric + LOW-RES ratio 0.16'),
    ('6ac71179b814691321003745', 2, 'upscale', 'treeup', 'repaired-art FAIL: LOW-RES ratio 0.29'),
    ('6ac711357be9df884b032d51', 2, 'upscale', 'truck', 'repaired-art FAIL: LOW-RES ratio 0.29'),
    ('6ac7232d73283b982509a1c3', 2, 'sticker', HOLES, 'repaired-art FAIL: checker score 0.65 + opaque square (die-cut would be a square)'),
    ('6ac71204f0a0ce97bc0c9211', 3, 'duvet', 'party', 'B REWORK: ~102 dpi after 2x upscale'),
    ('6ac711a4b8d5d3e719013158', 3, 'duvet', 'santa', 'B REWORK: ~102 dpi after 2x upscale'),
]
TARGET_MOTIF = 0.52; TARGET_UP = 0.75

def native_min_ratio(pid, f):
    d, j = pj(pid); im = Image.open(f); iw = im.size[0]; pr = j.get('proposed') or j['current']
    return min(iw / (pr['scale'] * w) for w, h in j['placeholders'].values())

# final SR art per key: downscale 4x SR output to the factor needed for ratio >= TARGET_UP on its products (cap 4x)
need = {}
for pid, item, route, key, _ in ITEMS:
    if route in ('upscale',): need[key] = max(need.get(key, 0), TARGET_UP / native_min_ratio(pid, SRC[key]))
need['party'] = need['santa'] = 4.0
FINAL = {}
for key, f in need.items():
    src = Image.open(SRC[key]); nw = NATIVE_W.get(key, src.size[0]); fac = min(4.0, f)
    out = f'{O}/art/{key}_realesrgan-anime6B_x{fac:.2f}.png'
    if not os.path.exists(out):
        sr = Image.open(f'{SP}/sr/{key}.png'); tw = round(nw * fac)
        if abs(tw - sr.size[0]) > 4: sr = sr.resize((tw, round(sr.size[1] * tw / sr.size[0])), Image.LANCZOS)
        sr.save(out, optimize=True)
    FINAL[key] = (out, fac, nw)
    print('final art', key, Image.open(out).size, f'{os.path.getsize(out) / 1e6:.1f} MB')

results = []; sheet_tiles = []
def write_json(name, d): json.dump(d, open(f'{O}/placements/{name}.json', 'w'), indent=1)
def groups(per_var):
    g = {}
    for v, p in per_var.items(): g.setdefault(json.dumps(p, sort_keys=True), []).append(int(v))
    return [{'variant_ids': sorted(vs), 'placement': json.loads(k)} for k, vs in g.items()]

for pid, item, route, key, issue in ITEMS:
    d, j = pj(pid); ph = j['placeholders']; dec = (j.get('decoration_method') or '').lower(); prop = j.get('proposed') or j['current']
    blank = lambda v: BLANK.get(v, (255, 255, 255))
    options = []  # (label, art_file, per_var, method, native_px)
    if route == 'pillow':
        art = d + '/original.png'; im = Image.open(art); iw, ih = im.size; bb, _ = bbox(im); pv = {}
        for v, (W_, H_) in ph.items():
            p = (j.get('proposed_per_variant_group') or {}).get(v)
            f, r = geom(bb, iw, ih, p, W_, H_) if p else (0, 0)
            if not p or f < 0.999 or r < 0.5:
                p = fit_centre(bb, iw, ih, W_, H_); s_max = iw / (0.5 * W_)
                if p['scale'] > s_max: p = recentre(bb, iw, ih, p, W_, H_, s_max)
            pv[v] = {k: p[k] for k in ('x', 'y', 'scale', 'angle')}
        options.append(('per-variant placements', art, pv, 'original art unchanged; print_areas split per variant (lumbar 244224 gets its own scale)', None))
    elif route == 'motif':
        art = key; im = Image.open(art); iw, ih = im.size; bb, _ = bbox(im)
        wmax = max(w for w, h in ph.values()); s = iw / (TARGET_MOTIF * wmax)
        pv = {v: recentre(bb, iw, ih, prop, W_, H_, s) for v, (W_, H_) in ph.items()}
        options.append(('smaller centred motif', art, pv, f'native art, scale {prop["scale"]:.3f}->{s:.3f} ({s / prop["scale"]:.0%} linear) so the largest variant prints at >=150 dpi nominal', None))
    elif route in ('holes', 'sticker'):
        pv = {v: dict(prop) for v in ph}
        options.append(('hole-filled art' if route == 'holes' else 'transparent die-cut art', key, pv,
                        'TREE UP letter holes filled from the letter fill (letter-mask restricted), outline defringed' if route == 'holes' else
                        'same corrected PATIENCE design as a transparent cut (hole-filled file) so the die-cut follows the art, not a square', None))
    elif route == 'upscale':
        art, fac, nw = FINAL[key]; im = Image.open(art); iw, ih = im.size; bb, _ = bbox(im)
        pv = {}; wmax = max(w for w, h in ph.values())
        s = prop['scale']
        if iw / (s * wmax) < 0.5: s = iw / (TARGET_MOTIF * wmax)
        for v, (W_, H_) in ph.items(): pv[v] = dict(prop) if s == prop['scale'] else recentre(bb, iw, ih, prop, W_, H_, s)
        options.append((f'Real-ESRGAN x{fac:.2f} upscale', art, pv, f'local AI upscale (Real-ESRGAN anime6B, CPU) x{fac:.2f}' + ('' if s == prop['scale'] else f'; scale {prop["scale"]:.3f}->{s:.3f} to clear 150 dpi'), nw))
    elif route == 'duvet':
        bfile = SRC[key]; bim = Image.open(bfile); iw, ih = bim.size; bb, _ = bbox(bim); wmax = max(w for w, h in ph.values())
        sA = iw / (TARGET_MOTIF * wmax)
        options.append(('OPTION A smaller motif (B file)', bfile, {v: recentre(bb, iw, ih, prop, W_, H_, sA) for v, (W_, H_) in ph.items()},
                        f"B's 2x file as-is, scale {prop['scale']:.3f}->{sA:.3f} ({sA / prop['scale']:.0%} linear)", NATIVE_W[key]))
        art, fac, nw = FINAL[key]; im = Image.open(art); iw2, ih2 = im.size; bb2, _ = bbox(im)
        options.append(('OPTION B Real-ESRGAN x4', art, {v: recentre(bb2, iw2, ih2, prop, W_, H_, prop['scale']) for v, (W_, H_) in ph.items()},
                        'native 2048 (B file /2) -> Real-ESRGAN anime6B x4, original proposed scale kept', nw))
    # BEFORE (B FAIL / REWORK)
    if route == 'duvet': before_file = SRC[key]
    elif pid in B_FAIL: before_file = B_FAIL[pid][0]
    else: before_file = d + '/original.png'
    bq = qa(before_file, {v: prop for v in ph}, ph, dec, item >= 2)
    bimg = Image.open(before_file).convert('RGBA')
    b_render = BR + f'/qa/placement_renders/{pid}.png'
    row1 = []; row2 = []
    largest = max(ph, key=lambda v: ph[v][0] * ph[v][1])
    if item == 1 and os.path.exists(b_render):
        row1.append((Image.open(b_render).convert('RGB'), ['BEFORE: B FAIL render', f"B: {B_PL[pid]['issues'][:60]}"]))
    else:
        bv = bq['worst_variant']
        row1.append((place_on(None, bimg, prop, *ph[bv], blank(bv), 600), [f"BEFORE: {'B REWORK' if route == 'duvet' else 'B FAIL'} file on {VTITLE.get(bv, bv)}",
                     f"{os.path.basename(before_file)[:22]}  ratio {bq['ratio_min']:.2f} = {bq['ratio_min'] * 300:.0f} dpi nominal"]))
    fx, fy = detail_point(Image.open(options[-1][1]))
    bv = bq['worst_variant']
    row2.append((detail(bimg, prop, *ph[bv], fx, fy, blank=blank(bv)), ['BEFORE print px 1:1', f"{bq['ratio_min'] * 300:.0f} dpi nom."]))
    for oi, (label, art, pv, method, native_px) in enumerate(options):
        q = qa(art, pv, ph, dec, item >= 2, native_px=None)
        upscaled = route in ('upscale', 'duvet')
        nat = (native_px / Image.open(art).size[0] * q['ratio_min']) if native_px else q['ratio_min']
        geo_ok = q['inside_min'] >= 0.999; res_ok = q['ratio_min'] >= 0.5; hard_b = q['b_verdict'] == 'FAIL'
        if not geo_ok or hard_b and res_ok: status = 'FAIL'
        elif not res_ok: status = 'NEEDS_HIGHRES_SOURCE'
        elif upscaled or q['b_verdict'] == 'WARN': status = 'WARN'
        else: status = 'PASS'
        aim = Image.open(art).convert('RGBA'); wv = q['worst_variant']
        geo_worst = min(q['per_variant'], key=lambda v: q['per_variant'][v]['inside'])
        show = [largest] + ([wv] if wv != largest else []) + ([geo_worst] if geo_worst not in (largest, wv) else [])
        if route == 'pillow': show = [largest, '244224'] if largest != '244224' else ['244224']
        if route == 'holes': show = [largest, '71073']
        if route == 'duvet': show = [largest] if oi == 0 else [largest, '147747']
        for v in show:
            pvq = q['per_variant'][v]
            row1.append((place_on(None, aim, pv[v], *ph[v], blank(v), 600), [f"AFTER {label[:30]} - {VTITLE.get(v, v)}" + (' (worst)' if v == wv else ''),
                         f"s={pv[v]['scale']:.3f} inside {pvq['inside']:.1%}  {pvq['nominal_dpi']} dpi nom." + (f" / {pvq['physical_dpi']} phys" if pvq['physical_dpi'] else '')]))
        row2.append((detail(aim, pv[wv], *ph[wv], fx, fy, blank=blank(wv)), [f'AFTER{" A" if route == "duvet" and oi == 0 else (" B" if route == "duvet" else "")} print px 1:1', f"{q['ratio_min'] * 300:.0f} dpi nom." + (f' (native {nat * 300:.0f})' if upscaled else '')]))
        if route == 'holes':  # 1:1 zoom on the repaired letters, on the blue blank
            for nm, im_ in (('BEFORE', bimg), ('AFTER', aim)):
                c = im_.crop((300, 120, 1100, 520)); bg = Image.new('RGBA', c.size, BLANK['71073'] + (255,)); bg.alpha_composite(c)
                row2.append((bg.convert('RGB').crop((0, 0, 380, 380)), [f'{nm} letters 1:1 (art px)', 'on Blue blank']))
        suffix = '' if route != 'duvet' else ('_optionA' if oi == 0 else '_optionB')
        rel = os.path.relpath(art, W)
        write_json(pid + suffix, dict(product_id=pid, shop_id=j['shop_id'], title=j['title'], blueprint_id=j['blueprint_id'], print_provider_id=j['print_provider_id'],
            position=j['position'], decoration_method=dec, issue=issue, option=label, method=method,
            art=dict(file='work/' + rel, px=list(Image.open(art).size), sha1=sha1(art), native_source_width_px=native_px, upscaled=upscaled),
            print_areas=groups(pv), per_variant_qa=q['per_variant'], content_bbox_norm=q['bbox'], qa_status=status, b_script_verdict=q['b_verdict'], issues=q['issues'],
            before=dict(file=os.path.relpath(before_file, '/home/user'), placement=prop, ratio_min=round(bq['ratio_min'], 3), inside_min=round(bq['inside_min'], 4)),
            live_change_made=False, note='NON-LIVE staging file. Nothing uploaded. Applying it needs an image upload + product update = owner-approved write.'))
        notes = [method, f"B-script verdict {q['b_verdict']}"] + q['issues']
        if upscaled: notes.append(f"native-pixel equivalent {nat * 300:.0f} dpi nominal (upscale adds no true detail)")
        phys = [f"{VTITLE.get(v, v)} {x['physical_dpi']} phys dpi @ {x['placeholder_ppi']} ppi placeholder" for v, x in q['per_variant'].items() if x['physical_dpi'] and v == wv]
        if phys: notes.append('physical: ' + phys[0])
        if route == 'duvet' and oi == 0:
            sN = NATIVE_W[key] / (0.5 * max(w for w, h in ph.values()))
            notes.append(f'a motif at native >=150 dpi would need scale {sN:.3f} (~{sN * 104:.0f} in wide on King)')
        results.append(dict(product_id=pid, issue=issue, fix_applied=label + ': ' + method, file='work/' + rel,
            effective_dpi_largest_variant=round(q['ratio_min'] * 300), content_inside_min=f"{q['inside_min']:.4f}", qa_status=status, notes=' | '.join(notes)))
        sheet_tiles.append((pid, label, status, row1[0][0], row1[-1][0], round(q['ratio_min'] * 300)))
    compose(f"{pid}  {j['title'][:70]}  - {issue}", row1, row2, f'{O}/before_after/{pid}.png')
    print(pid, route, [(r['qa_status'], r['effective_dpi_largest_variant'], r['content_inside_min']) for r in results if r['product_id'] == pid])

k = list(results[0].keys())
with open(O + '/results.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, k); w.writeheader(); w.writerows(results)
# contact sheets: 3 x 4 tiles, each tile = BEFORE | AFTER
TW, TH = 530, 330
for n in range(0, len(sheet_tiles), 12):
    S = Image.new('RGB', (TW * 3 + 20, TH * 4 + 20), (25, 25, 28)); dr = ImageDraw.Draw(S)
    for i, (pid, label, st, b, a, dpi) in enumerate(sheet_tiles[n:n + 12]):
        x0, y0 = 10 + (i % 3) * TW, 10 + (i // 3) * TH
        for k_, im in enumerate((b, a)):
            t = im.copy(); t.thumbnail((255, 270)); S.paste(t, (x0 + k_ * 262 + (255 - t.width) // 2, y0 + (270 - t.height) // 2))
        col = {'PASS': (90, 220, 90), 'WARN': (240, 200, 60)}.get(st, (240, 80, 80))
        dr.text((x0, y0 + 274), f'{pid}  {st}  {dpi} dpi', fill=col, font=FONTB); dr.text((x0, y0 + 296), label[:60], fill='white', font=FONT)
    S.save(f'{O}/contact_sheet_{n // 12 + 1}.png', optimize=True)
from collections import Counter
print(Counter(r['qa_status'] for r in results))
