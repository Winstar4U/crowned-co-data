import sys; sys.path.insert(0, sys.argv[1])
from rlib import *
f = v1('873af255de')
full = [p for p in glob.glob(FIX + '873af255de*.png') if '_v2' not in p][0].split('/')[-1][:-4]
H, W = f.shape[:2]
op = f[..., 3] >= 128
# scroll/text band: opaque px below the hat cuff (hat cuff bottom ~ y 1150 at 2048 scale) - exclude hat by component
lab, n = ndi.label(op, structure=np.ones((3, 3)))
idx = np.arange(1, n + 1); area = ndi.sum(np.ones_like(lab), lab, idx)
hat = lab == idx[np.argmax(area)]
text = op & ~hat
cl = ndi.binary_closing(text, iterations=10)
out = stroke(f, 14.0, (250, 248, 240), mask=(cl | text) & ~hat)
print('text px', int(text.sum()))
save(out, FIX + '570a81cddb099127ba13496baf63b1934842e57d_v2.png')
view([f, out], sys.argv[1] + '/r570v2.png', size=1500)
view([out], sys.argv[1] + '/r570v2b.png', col=(46, 84, 160), size=900)
