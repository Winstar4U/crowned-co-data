"""W2 alternative wording: street-sign plaque reads WELCOME (matching W1) instead of CANDY CANE LANE.
LOCAL ONLY. Same method/font/colours/plaque centre as d6_new_art/text_fix/scripts/fix_candy.py (Bebas Neue Bold,
cream + dark-green drop shadow); only the word changes. Built on the three blank-plaque source files:
  5fa6bcd6cd (opaque master), 5d22f4d4a7 (transparent cut, same geometry), 1170ae6c3a (crop, offset -196,-38).
Also writes WELCOME versions of the Real-ESRGAN upscaled candy files: the plaque box is replaced by the Lanczos-scaled
BLANK plaque from the native source and WELCOME is rendered directly at the upscaled resolution (vector text, no SR).
Usage: python3 make_welcome.py <out_dir> [sr_file:factor:native_key ...]"""
import sys, json
sys.path.insert(0, '/home/user/crowned-co-data/work/d6_new_art/text_fix/scripts')
from textlib import *   # noqa: F401,F403  (render_text, paste_layer, warp_affine_layer, composite_full, src, load_rgba, save_rgba)

OUT = sys.argv[1]
CREAM = (243, 234, 203); DARK = (12, 44, 31)
CX, CY = 1027, 714            # plaque centre measured in fix_candy.py
BOX_W, CAP_MAX = 344, 44      # plaque text box width; inner plaque height ~60 px between the dot rows
TEXT = 'WELCOME'

def fit_text(text, key, box_w, cap_max, **kw):
    cap = cap_max
    while True:
        L = render_text(text, key, cap, **kw)
        if L.shape[1] <= box_w or cap < 10: return L, cap
        cap -= 1

def welcome_layer(H, W, k=1.0):
    L, cap = fit_text(TEXT, 'bebas', int(BOX_W * k), int(round(CAP_MAX * k)), fill=CREAM, shadow=(2.5 * k, 2.5 * k, DARK), tracking=0.14)
    lay = np.zeros((H, W, 4), np.float32)
    x0 = int(round(CX * k - L.shape[1] / 2)); y0 = int(round(CY * k - L.shape[0] / 2))
    return paste_layer(lay, L, x0, y0), cap

meta = {}
sha_m, pm = src('5fa6bcd6cd'); M = load_rgba(pm); H, W = M.shape[:2]
lay, cap = welcome_layer(H, W)
outs = {sha_m: composite_full(M, lay)}
sha_t, pt = src('5d22f4d4a7'); outs[sha_t] = composite_full(load_rgba(pt), lay)
sha_s, ps = src('1170ae6c3a'); S = load_rgba(ps)
outs[sha_s] = composite_full(S, warp_affine_layer(lay, np.array([[1, 0, -196.019], [0, 1, -38.179]]), (S.shape[1], S.shape[0])))
for k_, v in outs.items():
    p = f'{OUT}/welcome_{k_[:10]}.png'; save_rgba(v, p); meta[k_[:10]] = dict(file=p, cap_px=cap, text=TEXT, font='Bebas Neue Bold')

# upscaled variants
BX = (CX - BOX_W // 2 - 14, CY - 34, CX + BOX_W // 2 + 14, CY + 34)   # plaque text box (native px) incl. shadow margin
for spec in sys.argv[2:]:
    f, fac, key = spec.split(':'); fac = float(fac)
    U = load_rgba(f); Hu, Wu = U.shape[:2]
    _, pn = src(key); N = load_rgba(pn)
    # blank plaque patch from the native blank source, scaled by fac
    patch = Image.fromarray(np.clip(N[BX[1]:BX[3], BX[0]:BX[2]] + 0.5, 0, 255).astype(np.uint8), 'RGBA')
    x0u, y0u = int(round(BX[0] * fac)), int(round(BX[1] * fac)); x1u, y1u = int(round(BX[2] * fac)), int(round(BX[3] * fac))
    patch = np.asarray(patch.resize((x1u - x0u, y1u - y0u), Image.LANCZOS)).astype(np.float32)
    U2 = U.copy(); U2[y0u:y1u, x0u:x1u] = patch
    layu, capu = welcome_layer(Hu, Wu, fac)
    R = composite_full(U2, layu)
    p = f'{OUT}/welcome_' + os.path.basename(f); save_rgba(R, p)
    meta[os.path.basename(f)] = dict(file=p, cap_px=capu, text=TEXT, factor=fac, base=f)
json.dump(meta, open(OUT + '/welcome_meta.json', 'w'), indent=1); print(json.dumps(meta, indent=1))
