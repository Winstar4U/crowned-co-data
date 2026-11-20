"""Remove detached specks (bg-removal leftovers) from a transparent PNG: connected components of alpha>16 that are
smaller than MAXPX and lie >= MINDIST px from every design component (>1% of the largest) get alpha 0. Usage: python3 -I despeck.py <in> <out>"""
import sys, numpy as np
from PIL import Image
from scipy import ndimage
MAXPX, MINDIST = 100, 20
a = np.array(Image.open(sys.argv[1]).convert('RGBA')); al = a[..., 3]
lab, n = ndimage.label(al > 16, structure=np.ones((3, 3))); sz = np.bincount(lab.ravel()); sz[0] = 0; main = sz.argmax()
keep_ids = np.nonzero(sz > 0.01 * sz.max())[0]  # design components (figure, every letter, i-dots...)
dist = ndimage.distance_transform_edt(~np.isin(lab, keep_ids))
rm = np.zeros(al.shape, bool); k = 0
for i in range(1, n + 1):
    if i in keep_ids or sz[i] >= MAXPX: continue
    m = lab == i
    if dist[m].min() >= MINDIST: rm |= m; k += 1
# also clear faint (alpha 1..16) pixels in the same far zone
rm |= (al > 0) & (al <= 16) & (dist >= MINDIST)
a[rm, 3] = 0
Image.fromarray(a, 'RGBA').save(sys.argv[2], compress_level=6)
print(sys.argv[2], 'removed components', k, 'pixels', int(rm.sum()), 'of', n - 1, 'non-main components')
