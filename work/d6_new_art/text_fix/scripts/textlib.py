"""Text rendering helpers: supersampled straight text, flag-warp to a banner centreline, compositing."""
import sys; sys.path.insert(0, "/home/user/crowned-co-data/work/d6_new_art/text_fix/scripts")
from common import *
import cv2

FONTS = {
    'bebas': '/usr/share/fonts/opentype/bebas-neue/BebasNeue-Bold.otf',
    'slab': '/usr/share/fonts/opentype/roboto/slab/RobotoSlab-Bold.otf',
    'mont_xb': '/usr/share/fonts/truetype/montserrat/Montserrat-ExtraBold.ttf',
    'mont_b': '/usr/share/fonts/truetype/montserrat/Montserrat-Bold.ttf',
    'mont_sb': '/usr/share/fonts/truetype/montserrat/Montserrat-SemiBold.ttf',
    'mont_blk': '/usr/share/fonts/truetype/montserrat/Montserrat-Black.ttf',
}

def _font(key, px):
    p = FONTS.get(key, key)
    if not os.path.exists(p):
        import glob
        c = glob.glob('/usr/share/fonts/**/' + os.path.basename(p), recursive=True)
        p = c[0]
    return ImageFont.truetype(p, px)

def cap_height_ratio(key):
    f = _font(key, 1000)
    b = f.getbbox('H')
    return (b[3] - b[1]) / 1000.0

def render_text(text, key, cap_h, fill, stroke=0, stroke_fill=(0, 0, 0), shadow=None, tracking=0.0, ss=4):
    """Return float32 RGBA (premultiplied=False) array of a single line; cap height = cap_h px.
    shadow = (dx, dy, (r,g,b)) in output px. tracking in em."""
    px = int(round(cap_h / cap_height_ratio(key) * ss))
    f = _font(key, px)
    sw = int(round(stroke * ss))
    # measure with tracking
    widths = [f.getlength(ch) for ch in text]
    tr = tracking * px
    total = sum(widths) + tr * (len(text) - 1)
    asc, desc = f.getmetrics()
    pad = sw + (int(abs(shadow[0]) * ss + abs(shadow[1]) * ss) if shadow else 0) + 4 * ss
    Wd, Hd = int(total + 2 * pad), int(asc + desc + 2 * pad)
    def draw_layer(color, offset=(0, 0), stroke_w=0, sfill=None):
        im = Image.new('RGBA', (Wd, Hd), (0, 0, 0, 0))
        d = ImageDraw.Draw(im)
        x = pad + offset[0]
        for ch, w in zip(text, widths):
            d.text((x, pad + offset[1]), ch, font=f, fill=tuple(color) + (255,), stroke_width=stroke_w,
                   stroke_fill=(tuple(sfill) + (255,)) if sfill is not None else None)
            x += w + tr
        return im
    base = Image.new('RGBA', (Wd, Hd), (0, 0, 0, 0))
    if shadow:
        base.alpha_composite(draw_layer(shadow[2], (int(shadow[0] * ss), int(shadow[1] * ss)), sw, shadow[2]))
    base.alpha_composite(draw_layer(fill, (0, 0), sw, stroke_fill if sw else None))
    # crop to ink
    bb = base.getbbox()
    base = base.crop((max(bb[0] - ss, 0), max(bb[1] - ss, 0), min(bb[2] + ss, Wd), min(bb[3] + ss, Hd)))
    # cap-top offset (for vertical centring on caps): find H top in same font
    out = base.resize((max(1, base.width // ss), max(1, base.height // ss)), Image.LANCZOS)
    return np.asarray(out).astype(np.float32)

def paste_layer(img, layer, x0, y0):
    """alpha-composite float RGBA layer onto float RGBA img at integer (x0,y0)."""
    h, w = layer.shape[:2]
    H, W = img.shape[:2]
    xa, ya = max(x0, 0), max(y0, 0); xb, yb = min(x0 + w, W), min(y0 + h, H)
    L = layer[ya - y0:yb - y0, xa - x0:xb - x0]
    R = img[ya:yb, xa:xb]
    la = L[..., 3:4] / 255.0; ra = R[..., 3:4] / 255.0
    oa = la + ra * (1 - la)
    rgb = (L[..., :3] * la + R[..., :3] * ra * (1 - la)) / np.maximum(oa, 1e-6)
    img[ya:yb, xa:xb] = np.dstack([rgb, oa[..., 0] * 255.0])
    return img

def flag_warp(layer, centre_fn, x_left):
    """Vertically shift each column of a straight text layer so its middle follows centre_fn(x)
    (absolute image x -> absolute y). Returns (warped_layer, x0, y0)."""
    h, w = layer.shape[:2]
    xs = np.arange(w) + x_left
    cy = np.array([centre_fn(x) for x in xs])
    top = cy - h / 2.0
    y0 = int(np.floor(top.min())) - 2
    H2 = int(np.ceil(top.max() - y0)) + h + 4
    mapx = np.tile(np.arange(w, dtype=np.float32)[None, :], (H2, 1))
    mapy = (np.arange(H2, dtype=np.float32)[:, None] + y0 - top[None, :]).astype(np.float32)
    # premultiply for clean resampling
    pm = layer.copy(); pm[..., :3] *= pm[..., 3:4] / 255.0
    wp = cv2.remap(pm, mapx, mapy, cv2.INTER_CUBIC, borderMode=cv2.BORDER_CONSTANT, borderValue=0)
    wp = np.clip(wp, 0, 255)
    a = wp[..., 3:4]
    wp[..., :3] = np.where(a > 0, wp[..., :3] * 255.0 / np.maximum(a, 1e-6), 0)
    return np.clip(wp, 0, 255), x_left, y0

def warp_affine_layer(layer_full, M, out_wh):
    """Map a full-size master-coords RGBA layer into a variant via 2x3 affine M (master->variant)."""
    pm = layer_full.copy(); pm[..., :3] *= pm[..., 3:4] / 255.0
    wp = cv2.warpAffine(pm, M.astype(np.float64), out_wh, flags=cv2.INTER_LANCZOS4, borderValue=0)
    wp = np.clip(wp, 0, 255); a = wp[..., 3:4]
    wp[..., :3] = np.where(a > 0, wp[..., :3] * 255.0 / np.maximum(a, 1e-6), 0)
    return np.clip(wp, 0, 255)

def composite_full(img, layer_full):
    return paste_layer(img.copy(), layer_full, 0, 0)

def banner_centreline(img, box, cond, deg=4, frac=0.5):
    """Fit centre line of the banner fill inside box (x0,y0,x1,y1). cond(rgb)->bool mask."""
    x0, y0, x1, y1 = box
    sub = img[y0:y1, x0:x1, :3]
    m = cond(sub) & (img[y0:y1, x0:x1, 3] > 128)
    m = ndi.binary_closing(m, iterations=4)
    l, n = ndi.label(m); s = ndi.sum(m, l, range(1, n + 1))
    m = l == (np.argmax(s) + 1)
    m = ndi.binary_fill_holes(m)
    xs, cs, hs = [], [], []
    for x in range(m.shape[1]):
        ys = np.nonzero(m[:, x])[0]
        if len(ys) > 10:
            xs.append(x + x0); cs.append(ys.min() + frac * (ys.max() - ys.min()) + y0); hs.append(ys.max() - ys.min())
    xs, cs, hs = map(np.array, (xs, cs, hs))
    p = np.polyfit(xs, cs, deg)
    return (lambda x: float(np.polyval(p, x))), xs, cs, hs, m
