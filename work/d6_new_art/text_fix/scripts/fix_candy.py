"""Candy Cane Lane: fill the blank green street-sign plaque.
master 5fa6bcd6cd (RGB) -> same layer onto 5d22f4d4a7 (identical geometry, transparent) and
1170ae6c3a (crop offset -196,-38). Separate design 3b2c254f1d (hanging sign) handled below."""
import sys; sys.path.insert(0, "/home/user/crowned-co-data/work/d6_new_art/text_fix/scripts")
from textlib import *

CREAM = (243, 234, 203); DARK = (12, 44, 31)
meta = {}

def fit_text(text, key, box_w, cap_max, **kw):
    cap = cap_max
    while True:
        L = render_text(text, key, cap, **kw)
        if L.shape[1] <= box_w or cap < 10:
            return L, cap
        cap -= 1

# ---- street-sign plaque family ----
sha_m, pm = src('5fa6bcd6cd')
M = load_rgba(pm); H, W = M.shape[:2]
text = 'CANDY CANE LANE'
L, cap = fit_text(text, 'bebas', 344, 54, fill=CREAM, shadow=(2.5, 2.5, DARK), tracking=0.06)
cx, cy = 1027, 714          # plaque centre between the snowflakes / dot rows (measured)
# vertical: centre the cap height (layer includes shadow)
x0 = int(round(cx - L.shape[1] / 2)); y0 = int(round(cy - L.shape[0] / 2))
layer = np.zeros((H, W, 4), np.float32)
layer = paste_layer(layer, L, x0, y0)
meta['plaque'] = {'text': text, 'font': 'Bebas Neue Bold', 'cap_px': cap, 'box': [x0, y0, x0 + L.shape[1], y0 + L.shape[0]]}
outs = {}
outs[sha_m] = composite_full(M, layer)
sha_t, pt = src('5d22f4d4a7'); T = load_rgba(pt)
assert T.shape == M.shape
outs[sha_t] = composite_full(T, layer)
sha_s, ps = src('1170ae6c3a'); S = load_rgba(ps)
A = np.array([[1, 0, -196.019], [0, 1, -38.179]])
outs[sha_s] = composite_full(S, warp_affine_layer(layer, A, (S.shape[1], S.shape[0])))

# ---- hanging-sign design (fanny pack) ----
sha_f, pf = src('3b2c254f1d'); F = load_rgba(pf)
HC = (250, 240, 207); HD = (8, 34, 20)
L1, c1 = fit_text('WELCOME', 'bebas', 470, 112, fill=HC, shadow=(4, 4, HD), tracking=0.08)
L2, c2 = fit_text('EST. NORTH POLE', 'bebas', 470, 34, fill=HC, shadow=(2, 2, HD), tracking=0.25)
gap = 26
tot = L1.shape[0] + gap + L2.shape[0]
cxh, cyh = 1510, 912
lay = np.zeros(F.shape, np.float32)
lay = paste_layer(lay, L1, int(cxh - L1.shape[1] / 2), int(cyh - tot / 2))
lay = paste_layer(lay, L2, int(cxh - L2.shape[1] / 2), int(cyh - tot / 2 + L1.shape[0] + gap))
outs[sha_f] = composite_full(F, lay)
meta['hanging'] = {'text': 'WELCOME / EST. NORTH POLE', 'font': 'Bebas Neue Bold', 'cap_px': [c1, c2]}
json.dump(meta, open(WK + '/candy_meta.json', 'w'), indent=1)
for k, v in outs.items():
    save_rgba(v, WK + f'/candy_{k[:10]}.png')
np.save(WK + '/candy_F.npy', np.zeros(1))
print(meta)
