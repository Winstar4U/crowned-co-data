import sys; sys.path.insert(0, sys.argv[1])
from rlib import *
pid, sha = '6ac7178307e4149a0f001490', '96e7dc4c99a99947a9e5f11344f0ee8492e4a88b'
o = orig(pid); f = v1(sha)
cw = cand_white(o)
y0, y1, x0, x1 = 440, 770, 840, 1220
band = np.zeros(cw.shape, bool); band[y0:y1, x0:x1] = True
dark = (o[..., :3].max(-1) < 120) & band          # letter outlines
closed = ndi.binary_closing(dark, iterations=6)
holes = ndi.binary_fill_holes(closed) & ~closed
region = ndi.binary_dilation(holes, iterations=3) & band
region = ndi.binary_fill_holes(region | (ndi.binary_fill_holes(closed) & band))  # whole letter bodies
region &= ndi.binary_fill_holes(ndi.binary_dilation(closed, iterations=1))
print('region px', int(region.sum()), 'changed', int((region & (np.abs(f - o).max(-1) > 2)).sum()))
out = f.copy(); out[region] = o[region]; out[..., 3][region] = 255
save(out, FIX + sha + '_v2.png')
view([o, f, out], sys.argv[1] + '/r96.png', box=(430, 780, 820, 1240), size=1300)
