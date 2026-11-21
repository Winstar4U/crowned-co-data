import sys; sys.path.insert(0, sys.argv[1])
from rlib import *
jobs = {'a897d056': '6ac717a6a4cff7da370fd145', '1702519f': '6ac717ba64166f603b0c8935'}
for sha, pid in jobs.items():
    full = [p for p in glob.glob(FIX + sha + '*.png') if '_v2' not in p][0].split('/')[-1][:-4]
    o = orig(pid)
    cw = cand_white(o, 226, 30)
    lab, n = ndi.label(cw); idx = np.arange(1, n + 1); a = ndi.sum(np.ones_like(lab), lab, idx)
    bg = np.isin(lab, idx[a >= 25])
    out = unmix_ring(o, bg, ring_px=2)
    # speck cleanup: tiny isolated opaque bits left in the cleared area
    op = out[..., 3] > 16
    l2, n2 = ndi.label(op, structure=np.ones((3, 3)))
    if n2:
        a2 = ndi.sum(np.ones_like(l2), l2, np.arange(1, n2 + 1))
        out[..., 3][np.isin(l2, np.arange(1, n2 + 1)[a2 < 12])] = 0
    dk = dark_components(out)
    print(sha, 'cleared', round(float(bg.mean()), 4), 'dark comp px', int(dk.sum()), 'frac of opaque', round(float(dk.sum() / max((out[..., 3] > 128).sum(), 1)), 4))
    save(out, f'{sys.argv[1]}/rep/{sha}_stage1.png')
    view([o, v1(sha), out], f'{sys.argv[1]}/r_{sha}.png', size=1500)
