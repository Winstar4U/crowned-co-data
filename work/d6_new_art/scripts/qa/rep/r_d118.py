import sys; sys.path.insert(0, sys.argv[1])
from rlib import *
from holes import holes
sha = 'd118595bce'
full = [p for p in glob.glob(FIX + sha + '*.png') if '_v2' not in p][0].split('/')[-1][:-4]
f = v1(sha)
lab, sel, info = holes(f)
BG_GAPS = [(715, 1053), (1438, 1073)]   # visually confirmed: enclosed background gaps (contain checker residue)
rgb = f[..., :3]; mn, mx = rgb.min(-1), rgb.max(-1)
nl = (mn >= 112) & (mx - mn <= 16) & (f[..., 3] > 0)
out = f.copy()
paper = np.zeros(lab.shape, bool); gap = np.zeros(lab.shape, bool)
for i, (ar, cx, cy) in zip(sel, info):
    m = lab == i
    if any(abs(cx - x) < 60 and abs(cy - y) < 60 for x, y in BG_GAPS):
        cand = nl | (f[..., 3] < 8)
        l2, _ = ndi.label(cand)
        ids = np.unique(l2[m]); ids = ids[ids > 0]
        reg = np.isin(l2, ids) & ndi.binary_dilation(m, iterations=60)
        gap |= reg
    else:
        paper |= m
# clear gaps (checker residue) with 1px feather
out[..., 3][gap] = 0
# paper fill: off-white behind the design, slightly grown under the anti-aliased edge
pf = ndi.binary_dilation(paper, iterations=2) & ~gap
PAPER = np.array([246, 243, 236], np.float32)
al = out[..., 3:4] / 255.0
fill = np.where(pf[..., None], out[..., :3] * al + PAPER * (1 - al), out[..., :3])
out[..., :3] = fill; out[..., 3] = np.where(pf, 255.0, out[..., 3])
print('paper px', int(pf.sum()), 'gap cleared px', int(gap.sum()))
save(out, FIX + full + '_v2.png')
view([f, out], sys.argv[1] + '/rd11v2.png', size=1500)
view([f, out], sys.argv[1] + '/rd11v2z.png', box=(950, 1500, 300, 1600), size=1500)
# pass 2: small punched-out whites in the wrapping-paper pile (enclosed, bordered by light fabric)
T = out[..., 3] < 8
l3, n3 = ndi.label(T)
edge = np.unique(np.concatenate([l3[0], l3[-1], l3[:, 0], l3[:, -1]]))
objs = ndi.find_objects(l3)
filled = 0; fm = np.zeros(T.shape, bool)
for i, sl in enumerate(objs, start=1):
    if i in edge or sl is None: continue
    ys = slice(max(sl[0].start - 4, 0), sl[0].stop + 4); xs = slice(max(sl[1].start - 4, 0), sl[1].stop + 4)
    c = l3[ys, xs] == i; ar = int(c.sum())
    if ar < 20 or ar >= 1500 or sl[0].start < 1000 or sl[0].stop > 1880: continue
    ring = ndi.binary_dilation(c, iterations=3) & ~c
    rr = out[ys, xs][ring]
    if (rr[:, 3] > 128).mean() < 0.95: continue
    pass
    fm[ys, xs] |= c; filled += 1
fm2 = ndi.binary_dilation(fm, iterations=1) & (out[..., 3] < 250)
al = out[..., 3:4] / 255.0
out[..., :3] = np.where(fm2[..., None], out[..., :3] * al + PAPER * (1 - al), out[..., :3]); out[..., 3] = np.where(fm2, 255.0, out[..., 3])
print('small holes filled', filled, int(fm2.sum()))
save(out, FIX + full + '_v2.png')
view([f, out], sys.argv[1] + '/rd11v2z.png', box=(950, 1500, 300, 1600), size=1500)
view([f, out], sys.argv[1] + '/rd11v2.png', size=1500)
