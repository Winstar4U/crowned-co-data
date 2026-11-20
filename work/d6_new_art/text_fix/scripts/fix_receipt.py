"""Santa's Favorite Customer receipt: replace 'PRICE' x3 and '$99,999.99' placeholders.
Erase with cv2.inpaint on paper (masks = glyph ink dilated), typeset in Montserrat (the
receipt's own face: geometric sans, Bold labels / ExtraBold red total), right-aligned to the
original PRICE column edge, total centred on the original total's centre."""
import sys; sys.path.insert(0, "/home/user/crowned-co-data/work/d6_new_art/text_fix/scripts")
from textlib import *

sha, p = src('2ddd385282')
a = load_rgba(p); H, W = a.shape[:2]
rgb = a[..., :3]
INK = (38, 29, 21); RED = (200, 41, 45)
VALUES = [('ALL THE GIFTS', 1381), ('UNLIMITED', 1446), ('PRICELESS', 1510)]   # row tops of PRICE
TOTAL = 'PAID IN COOKIES'
RIGHT = 1388

# masks
dk = rgb.max(-1) < 150
m = np.zeros((H, W), bool)
for _, y in VALUES:
    m[y - 8:y + 30, 1280:1400] = True
m &= ndi.binary_dilation(dk, iterations=3)
rd = (rgb[..., 0] - rgb[..., 1] > 22)
mt = np.zeros((H, W), bool); mt[1578:1660, 925:1300] = True
mt &= ndi.binary_dilation(rd, iterations=6)
mask = ndi.binary_dilation(m | mt, iterations=2)
u8 = np.clip(rgb, 0, 255).astype(np.uint8)
inp = cv2.inpaint(u8, mask.astype(np.uint8) * 255, 7, cv2.INPAINT_TELEA).astype(np.float32)
out = a.copy(); out[..., :3] = np.where(mask[..., None], inp, rgb)

# measure original cap heights: 'PRICE' rows ~29px tall (1377..1406); total digits ~51px
cap_lab = 21.0
for txt, y in VALUES:
    L = render_text(txt, 'mont_b', cap_lab, fill=INK, tracking=0.04)
    # align cap top to row top, right edge to RIGHT
    out = paste_layer(out, L, RIGHT - L.shape[1] + 1, y - 1)
Lt = render_text(TOTAL, 'mont_xb', 37.0, fill=RED, tracking=0.03)
cx = (946 + 1276) / 2.0; cyt = 1617.0
out = paste_layer(out, Lt, int(round(cx - Lt.shape[1] / 2)), int(round(cyt - Lt.shape[0] / 2)))
save_rgba(out, WK + '/receipt_fixed.png')
json.dump({'values': VALUES, 'total': TOTAL, 'inpaint_px': int(mask.sum())}, open(WK + '/receipt_meta.json', 'w'))
