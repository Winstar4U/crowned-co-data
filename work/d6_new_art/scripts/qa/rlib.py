import glob, numpy as np
from PIL import Image
from scipy import ndimage as ndi
Image.MAX_IMAGE_PIXELS = None
FIX = '/home/user/crowned-co-data/work/d6_new_art/fixed/'
def orig(pid):
    return np.asarray(Image.open(glob.glob(f'/home/user/crowned-co-data/work/d6_batch*/{pid}/original.png')[0]).convert('RGBA')).astype(np.float32)
def v1(sha):
    return np.asarray(Image.open([p for p in glob.glob(FIX + sha + '*.png') if '_v2' not in p][0]).convert('RGBA')).astype(np.float32)
def save(a, path):
    Image.fromarray(np.clip(a + 0.5, 0, 255).astype(np.uint8), 'RGBA').save(path)
def cand_white(a, t=228, c=28):
    rgb = a[..., :3]; mn, mx = rgb.min(-1), rgb.max(-1)
    return (mn >= t) & (mx - mn <= c)
def comp_on(a, col):
    bg = np.zeros(a.shape[:2] + (3,), np.float32); bg[:] = col
    al = a[..., 3:4] / 255.0
    return a[..., :3] * al + bg * (1 - al)
def view(arrs, path, col=(17, 17, 17), box=None, size=1400):
    ims = []
    for a in arrs:
        if box: y0, y1, x0, x1 = box; a = a[y0:y1, x0:x1]
        ims.append(comp_on(a, col))
    im = Image.fromarray(np.hstack(ims).astype(np.uint8)); im.thumbnail((size, size)); im.save(path)
def unmix_ring(a, cleared, ring_px=2, soft=60.0):
    rgb, al = a[..., :3], a[..., 3]
    dist = ndi.distance_transform_edt(~cleared)
    ring = (~cleared) & (dist <= ring_px)
    mn = rgb.min(-1)
    est = np.where(ring, np.clip((255.0 - mn) / soft, 0, 1), 1.0)
    un = np.clip((rgb - (1 - est[..., None]) * 255.0) / np.maximum(est, 1e-3)[..., None], 0, 255)
    out = a.copy()
    out[..., :3] = np.where(ring[..., None], un, rgb)
    out[..., 3] = al * est
    out[..., 3][cleared] = 0
    return out
def white_key(a, soft=60.0, floor=0.2):
    rgb = a[..., :3]; mn = rgb.min(-1)
    al = np.clip((255.0 - mn) / soft, 0, 1) * (a[..., 3] / 255.0)
    un = np.clip((rgb - (1 - al[..., None]) * 255.0) / np.maximum(al, 1e-3)[..., None], 0, 255)
    al = np.where(al < floor, 0, al)
    out = np.dstack([un, al * 255.0]); return out
def lum(c):
    c = c / 255.0; c = np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * c[..., 0] + 0.7152 * c[..., 1] + 0.0722 * c[..., 2]
def stroke(a, r, color, mask=None):
    al = a[..., 3]
    m = (al >= 128) if mask is None else mask
    d = ndi.distance_transform_edt(~m)
    s = np.clip(r + 0.5 - d, 0, 1)
    fa = al / 255.0
    oa = fa + s * (1 - fa)
    rgb = (a[..., :3] * fa[..., None] + np.array(color, np.float32) * (s * (1 - fa))[..., None]) / np.maximum(oa, 1e-6)[..., None]
    return np.dstack([rgb, oa * 255.0])
def dark_components(a, bg=(17, 17, 17), frac=0.6, minarea=40):
    op = a[..., 3] > 128
    L = lum(a[..., :3]); Lb = lum(np.array(bg, np.float32)[None])[0]
    cr = (np.maximum(L, Lb) + 0.05) / (np.minimum(L, Lb) + 0.05)
    low = (cr < 2.5) & op
    lab, n = ndi.label(op, structure=np.ones((3, 3)))
    if not n: return np.zeros_like(op)
    idx = np.arange(1, n + 1); area = ndi.sum(np.ones_like(lab), lab, idx); ls = ndi.sum(low, lab, idx)
    return np.isin(lab, idx[(ls >= frac * area) & (area >= minarea)])
