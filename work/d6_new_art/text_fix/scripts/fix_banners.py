"""Blank ribbon banners: typeset the title phrase, flag-warped to the banner's own centreline.
truck tree (9253995681 master, d499f625bb identical geometry), Ho Ho (d5007b7352),
Jingle (33bfc50a57 master; 2989efb65a identical; 876f6be331 crop offset)."""
import sys; sys.path.insert(0, "/home/user/crowned-co-data/work/d6_new_art/text_fix/scripts")
from textlib import *
meta = {}

def fit(text, key, wmax, cap, **kw):
    while True:
        L = render_text(text, key, cap, **kw)
        if L.shape[1] <= wmax or cap < 8:
            return L, cap
        cap -= 0.5

def banner(a, box, cond, text, key, span, cap, fill, shadow=None, stroke=0, stroke_fill=(0, 0, 0), tracking=0.04, dy=0.0, deg=4):
    f, xs, cs, hs, m = banner_centreline(a, box, cond, deg=deg)
    L, c = fit(text, key, span[1] - span[0], cap, fill=fill, shadow=shadow, stroke=stroke, stroke_fill=stroke_fill, tracking=tracking)
    x_left = int(round((span[0] + span[1]) / 2 - L.shape[1] / 2))
    wp, x0, y0 = flag_warp(L, lambda x: f(x) + dy, x_left)
    lay = np.zeros(a.shape, np.float32)
    lay = paste_layer(lay, wp, x0, y0)
    return lay, {'text': text, 'font': key, 'cap_px': c, 'x': [x_left, x_left + L.shape[1]],
                 'min_banner_h': int(hs[(xs >= span[0]) & (xs <= span[1])].min())}

green = lambda r: (r[..., 1] > r[..., 0] + 12) & (r[..., 1] > 70)
outs = {}
# ---- truck tree ----
sha, p = src('9253995681'); a = load_rgba(p)
lay, meta['truck'] = banner(a, (560, 1580, 1520, 1840), green, 'BRINGING HOME THE TREE', 'slab',
                            (650, 1420), 50, fill=(250, 236, 204), shadow=(2.5, 2.5, (120, 34, 30)), tracking=0.04, dy=4)
outs[sha] = composite_full(a, lay)
sha2, p2 = src('d499f625bb'); b = load_rgba(p2); assert b.shape == a.shape
outs[sha2] = composite_full(b, lay)
# ---- Ho Ho Pour Another ----
sha, p = src('d5007b7352'); a = load_rgba(p)
gr2 = lambda r: (r[..., 1] > r[..., 0] + 25) & (r[..., 1] > 90)
L_in = None
lay, meta['hoho'] = banner(a, (400, 1540, 1200, 1790), gr2, 'POUR ANOTHER', 'mont_blk',
                           (490, 1110), 60, fill=(216, 45, 34), stroke=3.5, stroke_fill=(231, 181, 104),
                           shadow=(3, 3, (33, 6, 2)), tracking=0.03, dy=2)
outs[sha] = composite_full(a, lay)
# ---- Jingle All the Way (to the liquor store) ----
sha, p = src('33bfc50a57'); a = load_rgba(p)
rgb = a[..., :3]
gmed = np.median(rgb[1190:1200, 1215:1230].reshape(-1, 3), axis=0)
X0, X1, Y0, Y1 = 805, 1245, 1149, 1222
box = np.zeros(a.shape[:2], bool); box[Y0:Y1, X0:X1] = True
ng = box & (np.abs(rgb - gmed).sum(-1) > 60)
lab, n = ndi.label(ng); sz = ndi.sum(ng, lab, range(1, n + 1))
big = np.isin(lab, [i + 1 for i in range(n) if sz[i] > 150])  # holly, dashes, small snowflakes (dots are < 150 px)
gr3 = lambda r: (r[..., 1] > r[..., 0] + 20) & (r[..., 1] > 70)
_f, _xs, _cs, _hs, inner = banner_centreline(a, (700, 1100, 1350, 1300), gr3, deg=2)
interior = np.zeros(a.shape[:2], bool); interior[1100:1300, 700:1350] = ndi.binary_erosion(inner, iterations=5)
mk = ndi.binary_dilation(big, iterations=3) & box & interior
u8 = np.clip(rgb, 0, 255).astype(np.uint8)
inp = cv2.inpaint(u8, mk.astype(np.uint8) * 255, 9, cv2.INPAINT_TELEA).astype(np.float32)
a2 = a.copy(); a2[..., :3] = np.where(mk[..., None], inp, rgb)
lay, meta['jingle'] = banner(a, (780, 1110, 1270, 1290), gr3, 'TO THE LIQUOR STORE', 'slab',
                             (812, 1238), 34, fill=(246, 222, 160), shadow=(2, 2, (20, 45, 25)), tracking=0.03, dy=0, deg=2)
meta['jingle']['removed'] = 'centre holly sprig, 2 gold dashes, 2 small inner snowflakes (inpainted)'
meta['jingle']['inpaint_px'] = int(mk.sum())
outs[sha] = composite_full(a2, lay)
np.save(WK + '/jingle_layer.npy', lay)
np.save(WK + '/jingle_mask.npy', mk)
json.dump(meta, open(WK + '/banner_meta.json', 'w'), indent=1)
for k, v in outs.items():
    save_rgba(v, WK + f'/banner_{k[:10]}.png')
print(meta)
