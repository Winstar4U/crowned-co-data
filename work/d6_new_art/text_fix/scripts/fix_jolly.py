"""JOLLY, TIRED, AND, AND CAFFEINATED -> JOLLY, TIRED, AND CAFFEINATED.
Deletes the comma + second 'AND' (separate opaque components) and the stray dark specks
of the old cut-out halo next to it. The first 'AND' already sits on the design's centre axis."""
import sys; sys.path.insert(0, "/home/user/crowned-co-data/work/d6_new_art/text_fix/scripts")
from common import *
sha, p = src('6ef24aa6af')
a = load_rgba(p); op = a[..., 3] > 128
l, n = ndi.label(op, structure=np.ones((3, 3)))
s = ndi.sum(op, l, range(1, n + 1)); o = ndi.find_objects(l)
def comp_at(y0, y1, x0, x1, minsz):
    return [i + 1 for i in range(n) if s[i] >= minsz and o[i][0].start >= y0 and o[i][0].stop <= y1 and o[i][1].start >= x0 and o[i][1].stop <= x1]
rm = comp_at(1000, 1080, 1240, 1295, 1000) + comp_at(790, 1050, 1295, 1775, 50000)   # comma, AND2
specks = [i + 1 for i in range(n) if s[i] < 80 and 760 < (o[i][0].start + o[i][0].stop) / 2 < 1100 and (o[i][1].start + o[i][1].stop) / 2 > 1280]
print('removed comps', rm, 'specks', len(specks))
assert len(rm) == 2
m = np.isin(l, rm + specks)
m = ndi.binary_dilation(m, iterations=2) & ~np.isin(l, [i + 1 for i in range(n) if (i + 1) not in rm + specks])
out = a.copy(); out[m] = 0
save_rgba(out, WK + '/jolly_fixed.png')
