"""Restore the original's low-frequency colour after Real-ESRGAN (model drifts hue a few levels).
out_rgb = SR + gauss(Lanczos4x(orig) - SR, sigma); alpha from SR. Usage: python3 -I color_fix.py <orig> <sr_raw> <out>"""
import sys, numpy as np
from PIL import Image
from scipy import ndimage
Image.MAX_IMAGE_PIXELS = None
o = Image.open(sys.argv[1]).convert('RGBA'); s = Image.open(sys.argv[2]).convert('RGBA')
oa = np.asarray(o).astype(np.float32); solid = oa[..., 3] > 127
_, (iy, ix) = ndimage.distance_transform_edt(~solid, return_indices=True)
ob = oa.copy(); ob[..., :3] = oa[..., :3][iy, ix]  # edge-bleed so the matte does not leak in
up = np.asarray(Image.fromarray(ob.clip(0, 255).astype(np.uint8)).resize(s.size, Image.LANCZOS)).astype(np.float32)
sa = np.asarray(s).astype(np.float32)
out = sa.copy()
for c in range(3):
    out[..., c] = sa[..., c] + ndimage.gaussian_filter(up[..., c] - sa[..., c], 10)
out = out.clip(0, 255).astype(np.uint8)
Image.fromarray(out, 'RGBA').save(sys.argv[3], compress_level=6)
d = np.abs(np.asarray(Image.fromarray(out).resize(o.size, Image.BOX)).astype(float)[..., :3] - oa[..., :3])[(oa[..., 3] > 250)]
print(sys.argv[3], s.size, 'mean |diff| vs original after colour fix', d.mean(0).round(2))
