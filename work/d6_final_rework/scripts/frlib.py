"""Shared helpers for d6_final_rework (LOCAL ONLY; no network, no Printify writes).
Placement math (as in d6_qa_fixes/scripts/build.py and winstar-recovery/qa/qa_placements.py):
  x,y = centre of the image as a fraction of the placeholder; scale = image width / placeholder width;
  src/print px ratio = image_px_w / (placeholder_px_w * scale); effective dpi = 300 * ratio.
Geometry: rectangle-inside fraction of the content bbox + raw-SVG safe-shape check (shape_check.py, copied from
d6_warn_disposition) of every content pixel."""
import glob, hashlib, json, os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage as nd
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shape_check as SC
Image.MAX_IMAGE_PIXELS = None
W = '/home/user/crowned-co-data/work'; O = W + '/d6_final_rework'; BR = '/home/user/winstar4u/my-projects/winstar-recovery'
SHOP = '26418699'
try:
    FONT = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 15)
    FONTB = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 18)
    FONTS = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 13)
except Exception: FONT = FONTB = FONTS = ImageFont.load_default()

def pj(pid):
    d = glob.glob(f'{W}/d6_batch*/{pid}')[0]
    return d, json.load(open(d + '/placement.json')), d.split('d6_batch')[1].split('/')[0]
def sha1(f): return hashlib.sha1(open(f, 'rb').read()).hexdigest()
def proposed(j):
    g = j.get('proposed_per_variant_group') or {}
    return {v: dict(g.get(v, j.get('proposed') or j['current'])) for v in j['placeholders']}
def current(j): return {v: dict(j['current']) for v in j['placeholders']}
def largest(ph): return max(ph, key=lambda v: ph[v][0] * ph[v][1])

def bbox(im):
    a = np.array(im.convert('RGBA'))
    if a[..., 3].min() < 250: m = a[..., 3] > 16
    else:
        c = a[0, 0, :3].astype(int); m = np.abs(a[..., :3].astype(int) - c).sum(2) > 40
    ys, xs = np.where(m); h, w = m.shape
    return (xs.min() / w, ys.min() / h, (xs.max() + 1) / w, (ys.max() + 1) / h)
def content_box_ph(bb, iw, ih, pr, W_, H_):
    aw = pr['scale'] * W_; ah = aw * ih / iw; x0 = pr['x'] * W_ - aw / 2; y0 = pr['y'] * H_ - ah / 2
    return (x0 + bb[0] * aw, y0 + bb[1] * ah, x0 + bb[2] * aw, y0 + bb[3] * ah)
def rect_inside(bb, iw, ih, pr, W_, H_):
    x0, y0, x1, y1 = content_box_ph(bb, iw, ih, pr, W_, H_)
    ix = max(0, min(x1, W_) - max(x0, 0)); iy = max(0, min(y1, H_) - max(y0, 0))
    return ix * iy / ((x1 - x0) * (y1 - y0))

def match_box(ref_art, ref_pl, new_art, ph):
    """Place new_art so its content bbox fits (contain, centred) in the placeholder box occupied by ref_art's content
    under ref_pl. Returns {vid: placement}."""
    ri = Image.open(ref_art); rb = bbox(ri); ni = Image.open(new_art); nb = bbox(ni); nw, nh = ni.size
    out = {}
    for v, (W_, H_) in ph.items():
        X0, Y0, X1, Y1 = content_box_ph(rb, *ri.size, ref_pl[v], W_, H_)
        cw = (nb[2] - nb[0]); chn = (nb[3] - nb[1]) * nh / nw   # content size in units of art width
        aw = min((X1 - X0) / cw, (Y1 - Y0) / chn); ah = aw * nh / nw
        cx = (X0 + X1) / 2 - ((nb[0] + nb[2]) / 2 - 0.5) * aw; cy = (Y0 + Y1) / 2 - ((nb[1] + nb[3]) / 2 - 0.5) * ah
        out[v] = {'x': round(cx / W_, 4), 'y': round(cy / H_, 4), 'scale': round(aw / W_, 4), 'angle': 0}
    return out

def qa(pid, art, per_var, native_w=None):
    """per-variant: rect inside, safe-shape inside (raw SVG), ratio, effective dpi, native dpi."""
    d, j, batch = pj(pid); ph = j['placeholders']; im = Image.open(art); iw, ih = im.size; bb = bbox(im)
    try:
        sc = SC.check(pid, batch, per_var, art); shp = {v: sc['variants'][v] for v in ph}
    except Exception as e:
        shp = {v: dict(kind=f'rect (shape check error {e!r})'[:80], inside_union=None) for v in ph}
    rows = {}
    for v, (W_, H_) in ph.items():
        pr = per_var[v]; r = iw / (pr['scale'] * W_); nat = (native_w / iw * r) if native_w else r
        rows[v] = dict(placeholder=[W_, H_], placement=pr, rect_inside=round(rect_inside(bb, iw, ih, pr, W_, H_), 4),
                       shape_inside=(round(shp[v]['inside_union'], 4) if shp[v].get('inside_union') is not None else None),
                       safe_area=shp[v].get('kind'), ratio=round(r, 3), effective_dpi=round(300 * r), native_dpi=round(300 * nat))
    L = largest(ph)
    ins = [x['shape_inside'] if x['shape_inside'] is not None else x['rect_inside'] for x in rows.values()]
    return dict(art=art, px=[iw, ih], bbox=[round(x, 4) for x in bb], per_variant=rows, largest_variant=L,
                dpi_largest=rows[L]['effective_dpi'], native_dpi_largest=rows[L]['native_dpi'],
                dpi_min=min(x['effective_dpi'] for x in rows.values()), native_dpi_min=min(x['native_dpi'] for x in rows.values()),
                inside_min=min(ins), upscaled=bool(native_w and native_w != iw))

# ---------------- rendering ----------------
def blank_for(j):
    t = j['title'].lower(); dec = (j.get('decoration_method') or '').lower()
    if 'engrav' in dec: return (200, 200, 205)
    if 'backpack' in t: return (25, 25, 28)
    return (255, 255, 255)
def place_on(art, pr, W_, H_, blank, max_side=620):
    s = max_side / max(W_, H_); cw, ch = max(2, int(W_ * s)), max(2, int(H_ * s))
    cv = Image.new('RGBA', (cw, ch), blank + (255,))
    aw = pr['scale'] * W_ * s; ah = aw * art.height / art.width
    if aw > 2 and ah > 2:
        a = art.copy(); a.thumbnail((max(1, int(aw * 2)), max(1, int(ah * 2))), Image.LANCZOS)
        a = a.resize((max(1, int(round(aw))), max(1, int(round(ah)))), Image.LANCZOS)
        tmp = Image.new('RGBA', (cw, ch), (0, 0, 0, 0)); tmp.paste(a, (int(round(pr['x'] * cw - aw / 2)), int(round(pr['y'] * ch - ah / 2))), a)
        cv = Image.alpha_composite(cv, tmp)
    out = cv.convert('RGB'); dr = ImageDraw.Draw(out); dr.rectangle((0, 0, cw - 1, ch - 1), outline=(255, 80, 80))
    return out
def crop_on(art, box_norm, blank, out_w=420):
    iw, ih = art.size; b = (int(box_norm[0] * iw), int(box_norm[1] * ih), int(box_norm[2] * iw), int(box_norm[3] * ih))
    c = art.crop(b); bg = Image.new('RGBA', c.size, blank + (255,)); bg.alpha_composite(c.convert('RGBA'))
    bg = bg.convert('RGB'); s = out_w / bg.width; return bg.resize((out_w, max(1, int(bg.height * s))), Image.LANCZOS)
def panel(img, lines, w, head=(255, 220, 120)):
    img = img.copy(); img.thumbnail((w, 10000)); P = Image.new('RGB', (w, img.height + 20 * len(lines) + 10), (40, 40, 44))
    P.paste(img, ((w - img.width) // 2, 0)); d = ImageDraw.Draw(P)
    for i, t in enumerate(lines): d.text((6, img.height + 5 + 20 * i), t, fill=head if i == 0 else (235, 235, 235), font=FONTB if i == 0 else FONTS)
    return P
def compose(title_lines, cols, out, width=1600, zrow=None):
    n = len(cols); pw = (width - 10 * (n + 1)) // n
    P = [panel(i, l, pw) for i, l in cols]; h = max(p.height for p in P)
    Z = [panel(i, l, pw) for i, l in (zrow or [])]; hz = max([p.height for p in Z] + [0])
    th = 26 * len(title_lines) + 12
    S = Image.new('RGB', (width, th + h + (hz + 10 if Z else 0) + 10), (25, 25, 28)); d = ImageDraw.Draw(S)
    for i, t in enumerate(title_lines): d.text((10, 8 + 26 * i), t, fill='white' if i else (120, 200, 255), font=FONTB if i == 0 else FONT)
    for i, p in enumerate(P): S.paste(p, (10 + i * (pw + 10), th))
    for i, p in enumerate(Z): S.paste(p, (10 + i * (pw + 10), th + h + 10))
    S.save(out, optimize=True); return S
def diff_box(a_file, b_file, pad=0.04):
    """normalised bbox of the changed region between two same-aspect arts (compared at 600 px wide)."""
    A = Image.open(a_file).convert('RGBA'); B = Image.open(b_file).convert('RGBA')
    if abs(A.width / A.height - B.width / B.height) > 0.01: return None
    w = 600; h = int(600 * A.height / A.width)
    def flat(im):
        bg = Image.new('RGBA', im.size, (255, 255, 255, 255)); bg.alpha_composite(im); return np.asarray(bg.convert('RGB').resize((w, h), Image.BOX)).astype(int)
    D = np.abs(flat(A) - flat(B)).sum(2) > 60
    D = nd.binary_opening(D, iterations=1)
    if D.sum() < 30: return None
    lab, n = nd.label(nd.binary_dilation(D, iterations=6)); s = nd.sum(D, lab, range(1, n + 1)); k = 1 + int(np.argmax(s))
    ys, xs = np.where(lab == k)
    x0, x1, y0, y1 = xs.min() / w - pad, (xs.max() + 1) / w + pad, ys.min() / h - pad, (ys.max() + 1) / h + pad
    return (max(0, x0), max(0, y0), min(1, x1), min(1, y1))
def write_json(path, d): json.dump(d, open(path, 'w'), indent=1)
def groups(per_var):
    g = {}
    for v, p in per_var.items(): g.setdefault(json.dumps(p, sort_keys=True), []).append(int(v))
    return [{'variant_ids': sorted(vs), 'placement': json.loads(k)} for k, vs in g.items()]
