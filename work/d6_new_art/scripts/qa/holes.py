import sys; sys.path.insert(0, sys.argv[1])
from rlib import *
def holes(f, minarea=1500):
    T = f[..., 3] < 8
    lab, n = ndi.label(T)
    edge = np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))
    idx = np.arange(1, n + 1); a = ndi.sum(np.ones_like(lab), lab, idx)
    sel = idx[(a >= minarea) & ~np.isin(idx, edge)]
    com = ndi.center_of_mass(T, lab, sel)
    return lab, sel, [(int(a[i - 1]), int(c[1]), int(c[0])) for i, c in zip(sel, com)]
if __name__ == '__main__':
    for sha, nm in [('d118595bce', 'hd11.png'), ('b0b9766582', 'hb0.png')]:
        f = v1(sha); lab, sel, info = holes(f)
        print(sha, len(sel), sorted(info, reverse=True)[:30])
        g = f.copy(); g[np.isin(lab, sel)] = [255, 0, 255, 255]
        view([g], nm, size=1100)
