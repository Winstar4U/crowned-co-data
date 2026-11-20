"""Patience meter: 'P A T I T A N E C E' -> 'P A T I E N C E'.
Keeps original P,A,T (red band). Erases the yellow-band letters + the stray I on the divider
(cv2.inpaint, band-local), then re-places the ORIGINAL E,N,C,E glyphs plus an I built from the
original I's stem, at the original 54px pitch, centred in the yellow band. No font substitution."""
import sys; sys.path.insert(0, "/home/user/crowned-co-data/work/d6_new_art/text_fix/scripts")
from common import *
import cv2

sha, p = src('f193d6d08b')
im = np.asarray(Image.open(p).convert('RGB')).astype(np.float32)
H, W = im.shape[:2]
X0, X1 = 1615, 1685          # meter interior columns (outline at ~1595 / ~1700)
DIV0, DIV1 = 1076, 1080      # red/yellow divider rows
YEL0, YEL1 = 1081, 1426      # yellow interior rows (divider to teal at 1427)
letters = {  # (y0, y1) of original glyphs, x span ~1634..1661
    'P': (894, 934), 'A': (948, 988), 'T': (1002, 1041), 'I': (1056, 1094), 'T2': (1107, 1147),
    'A2': (1161, 1201), 'N': (1216, 1256), 'E': (1270, 1310), 'C': (1324, 1364), 'E2': (1377, 1417)}
GX0, GX1 = 1628, 1668

def glyph(y0, y1, bgc):
    """extract glyph as (ink rgb, alpha) from original over its band colour"""
    patch = im[y0 - 3:y1 + 3, GX0:GX1]
    L = patch.mean(-1); Lb = bgc.mean(); ink = np.array([22., 18., 16.])
    al = np.clip((Lb - L) / (Lb - ink.mean()), 0, 1)
    return al

yel = np.median(im[YEL0 + 5:YEL1 - 5, 1620:1630].reshape(-1, 3), axis=0)
red = np.median(im[1045:1070, 1620:1630].reshape(-1, 3), axis=0)
ink = np.median(im[1290:1300, 1640:1646].reshape(-1, 3), axis=0)
print('yellow', yel, 'red', red, 'ink', ink)

glyphs = {k: glyph(*letters[k], yel) for k in ['N', 'E', 'C', 'E2']}
# I: stem slice from the part of the original I above the divider, stretched to 40 rows (+ AA ends)
Ia = glyph(*letters['I'], red)          # 44 rows incl padding
stem = Ia[3 + 5:3 + 15].mean(0)          # rows 1061..1070 averaged profile
I = np.zeros_like(glyphs['N']); I[3:3 + 40] = stem[None, :]
top = Ia[3, :] / max(Ia[3:3 + 5].max(), 1e-3)      # keep original end anti-aliasing
I[3] = stem * np.clip(Ia[3].max() / max(stem.max(), 1e-3), 0, 1)
glyphs['I'] = I

# erase all letters: row-wise linear interpolation across the glyph column (bands are flat
# horizontally; divider rows interpolate black->black so the divider stays intact)
out = im.copy()
R0, R1 = 885, 1424
xl, xr = GX0 - 3, GX1 + 3
for yy in range(R0, R1 + 1):
    cl = np.median(im[yy, xl - 3:xl], axis=0); cr = np.median(im[yy, xr:xr + 3], axis=0)
    t = np.linspace(0, 1, xr - xl)[:, None]
    out[yy, xl:xr] = (1 - t) * cl + t * cr
# re-place the 8 original glyphs P A T I E N C E at a uniform pitch, clear of the divider
glyphs.update({k: glyph(*letters[k], red) for k in ['P', 'A', 'T']})
pitch, gh = 68, 40
t0 = 892
seq = ['P', 'A', 'T', 'I', 'E', 'N', 'C', 'E2']
tops = [t0 + i * pitch for i in range(8)]
for k, top in zip(seq, tops):
    al = glyphs[k]
    y = top - 3
    h = al.shape[0]
    assert not (top <= DIV1 + 4 and top + gh >= DIV0 - 4), (k, top)
    reg = out[y:y + h, GX0:GX1]
    out[y:y + h, GX0:GX1] = al[..., None] * ink + (1 - al[..., None]) * reg
print('tops', tops)
m = np.zeros((H, W), bool); m[R0:R1 + 1, xl:xr] = True
t0 = tops[3]
a = np.dstack([out, np.full((H, W), 255.0, np.float32)])
save_rgba(a, WK + '/patience_fixed_rgb.png')
json.dump({'tops': tops, 'pitch': pitch,
           'inpaint_px': int(m.sum())}, open(WK + '/patience_meta.json', 'w'))
