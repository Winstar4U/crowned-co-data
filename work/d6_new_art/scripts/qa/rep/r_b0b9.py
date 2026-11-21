import sys; sys.path.insert(0, sys.argv[1])
from rlib import *
from holes import holes
sha = 'b0b9766582'
full = [p for p in glob.glob(FIX + sha + '*.png') if '_v2' not in p][0].split('/')[-1][:-4]
f = v1(sha)
PAPER = np.array([246, 243, 236], np.float32)
lab, sel, info = holes(f, minarea=20)
fm = np.zeros(lab.shape, bool); nb = 0; ns = 0
for i, (ar, cx, cy) in zip(sel, info):
    if cy < 900: continue        # text block gaps above the pile stay transparent (background)
    m = lab == i
    if ar >= 1500:
        fm |= m; nb += 1
    else:
        ys, xs = np.nonzero(m)
        sl = (slice(max(ys.min() - 4, 0), ys.max() + 5), slice(max(xs.min() - 4, 0), xs.max() + 5))
        c = m[sl]; ring = ndi.binary_dilation(c, iterations=3) & ~c
        rr = f[sl][ring]
        if (rr[:, 3] > 128).mean() >= 0.95:
            fm |= m; ns += 1
pf = ndi.binary_dilation(fm, iterations=2) & (f[..., 3] < 250)
out = f.copy()
al = out[..., 3:4] / 255.0
out[..., :3] = np.where(pf[..., None], out[..., :3] * al + PAPER * (1 - al), out[..., :3]); out[..., 3] = np.where(pf, 255.0, out[..., 3])
print('receipt holes filled big', nb, 'small', ns, 'px', int(pf.sum()))
save(out, FIX + full + '_v2.png')
view([f, out], sys.argv[1] + '/rb0v2.png', size=1500)
view([f, out], sys.argv[1] + '/rb0v2z.png', box=(1300, 1800, 300, 1300), size=1500)
