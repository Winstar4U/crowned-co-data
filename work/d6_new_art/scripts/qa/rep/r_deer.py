import sys; sys.path.insert(0, sys.argv[1])
from rlib import *
for pid, sha in [('6ac70202a085d659d502276f', '46f859ccce'), ('6ac717e1ac4a665555019d40', '78de4579ec')]:
    full = [p for p in glob.glob(FIX + sha + '*.png') if '_v2' not in p][0].split('/')[-1][:-4]
    f = v1(sha)
    m = cand_white(f, 225, 30) & (f[..., 3] > 200)
    lab, n = ndi.label(m); idx = np.arange(1, n + 1); a = ndi.sum(np.ones_like(lab), lab, idx)
    com = ndi.center_of_mass(m, lab, idx)
    rm = []
    kept = []
    for i, c, ar in zip(idx, com, a):
        if ar < 60: continue
        cy, cx = c
        if 780 <= cx <= 1100 and 1000 <= cy <= 1200: kept.append((int(ar), int(cx), int(cy))); continue  # eye whites + nose highlight
        rm.append(i)
    pocket = np.isin(lab, rm)
    pocket = ndi.binary_dilation(pocket, iterations=1, mask=cand_white(f, 215, 40))
    cleared = pocket | (f[..., 3] < 8)
    out = unmix_ring(f, cleared, ring_px=2)
    out[..., 3][f[..., 3] < 8] = 0
    print(sha, 'removed comps', len(rm), 'px', int(pocket.sum()), 'kept', kept)
    save(out, FIX + full + '_v2.png')
view([v1('46f859ccce'), out], sys.argv[1] + '/rdeer.png', size=1400)
