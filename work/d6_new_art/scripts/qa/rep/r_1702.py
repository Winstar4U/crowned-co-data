import sys; sys.path.insert(0, sys.argv[1])
from rlib import *
sha, pid = '1702519f0b', '6ac717ba64166f603b0c8935'
full = [p for p in glob.glob(FIX + sha + '*.png') if '_v2' not in p][0].split('/')[-1][:-4]
o = orig(pid)
out = white_key(o, soft=90.0, floor=0.10)
# small enclosed white highlights (star core, sparkles) inside gold: keep opaque from original
cw = cand_white(o, 226, 30)
lab, n = ndi.label(cw); idx = np.arange(1, n + 1); a = ndi.sum(np.ones_like(lab), lab, idx)
kept = 0
for i in idx[a < 400]:
    sl = ndi.find_objects(lab == i)[0] if False else None
objs = ndi.find_objects(lab)
for i, sl in enumerate(objs, start=1):
    if a[i - 1] >= 400 or a[i - 1] < 4: continue
    ys = slice(max(sl[0].start - 4, 0), sl[0].stop + 4); xs = slice(max(sl[1].start - 4, 0), sl[1].stop + 4)
    c = lab[ys, xs] == i
    ring = ndi.binary_dilation(c, iterations=3) & ~c
    if ring.any() and (out[ys, xs][..., 3][ring] > 200).mean() >= 0.9:
        sub = out[ys, xs]; sub[c] = o[ys, xs][c]; sub[..., 3][c] = 255; kept += 1
op = out[..., 3] > 16
l2, n2 = ndi.label(op, structure=np.ones((3, 3)))
a2 = ndi.sum(np.ones_like(l2), l2, np.arange(1, n2 + 1))
out[..., 3][np.isin(l2, np.arange(1, n2 + 1)[a2 < 12])] = 0
print('kept highlights', kept, 'transparent frac', round(float((out[..., 3] < 8).mean()), 4))
save(out, FIX + full + '_v2.png')
view([o, out], sys.argv[1] + '/r1702c.png', box=(380, 1000, 550, 1500), size=1500)
view([o, out], sys.argv[1] + '/r1702d.png', size=1500)
# pass 2: restore small fully-enclosed keyed-out highlights (star core, sparkle centres) from the original
T = out[..., 3] < 128
l3, n3 = ndi.label(T)
edge = np.unique(np.concatenate([l3[0], l3[-1], l3[:, 0], l3[:, -1]]))
idx = np.arange(1, n3 + 1); a3 = ndi.sum(np.ones_like(l3), l3, idx)
cand = idx[(a3 < 3000) & ~np.isin(idx, edge)]
objs3 = ndi.find_objects(l3)
rm = np.zeros(T.shape, bool); sel = []
for i in cand:
    sl = objs3[i - 1]
    ys = slice(max(sl[0].start - 4, 0), sl[0].stop + 4); xs = slice(max(sl[1].start - 4, 0), sl[1].stop + 4)
    c = l3[ys, xs] == i
    ring = ndi.binary_dilation(c, iterations=3) & ~c
    if (out[ys, xs][..., 3][ring] > 230).mean() >= 0.9:
        rm[ys, xs] |= c; sel.append(i)
out[rm] = o[rm]; out[..., 3][rm] = 255
print('restored enclosed highlights', len(sel), int(rm.sum()))
save(out, FIX + full + '_v2.png')
view([o, out], sys.argv[1] + '/r1702c.png', box=(380, 800, 800, 1300), size=1500)
