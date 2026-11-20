"""Santa's List scarf 6ac7112383f1a0e50d071cdf: remove the baked-in grey/white checkerboard (fake transparency).
LOCAL ONLY. Input: work/d6_batch1/6ac7112383f1a0e50d071cdf/original.png (2048x2048 RGBA, binary alpha).
Steps
 1. Fit the checker grid (tile size + phase) on the exterior RGB, where the fake-transparency tiles survive under alpha=0.
    The two tile colours are measured there (light ~253, grey ~231).
 2. Exterior clean-up: flood-fill from the canvas border through (transparent | light low-saturation) pixels, i.e. the
    two tile colours; every opaque tile pixel reached is cleared. Design pixels are protected by the dark outline.
    Then opaque islands < 1500 px that are not connected to the main design are cleared (stray tile fragments).
 3. Interior tile regions: inside the parchment the checker is baked into the colour (alternate tiles darker).
    For pixels of the parchment (light, warm, opaque, not ink), the per-parity local mean is measured with a
    large masked Gaussian and the grey-parity tiles are gain-corrected to the light-parity level (per channel),
    which flattens the tile pattern while keeping the parchment texture and all ink.
 4. Enclosed transparent holes (punched-out whites from an earlier bad removal: snowflakes, cane stripes, letter
    grunge) smaller than 0.5% of the canvas are filled opaque white; larger enclosed areas stay transparent.
Outputs: corrected art PNG + metrics json."""
import json, sys
import numpy as np
from PIL import Image
from scipy import ndimage as nd

SRC = '/home/user/crowned-co-data/work/d6_batch1/6ac7112383f1a0e50d071cdf/original.png'
OUT = sys.argv[1]; MET = sys.argv[2]
a = np.asarray(Image.open(SRC).convert('RGBA')).astype(np.float32)
rgb = a[..., :3].copy(); al = a[..., 3].copy(); H, W = al.shape
g = rgb.mean(2); sat = rgb.max(2) - rgb.min(2)

# ---- 1. grid fit on exterior (alpha==0) pixels ----
T = al < 10
ext_rgb = T & (sat < 12) & (g > 215)
def parity(t, x0, y0):
    xs = np.floor((np.arange(W) - x0) / t).astype(int); ys = np.floor((np.arange(H) - y0) / t).astype(int)
    return ((ys[:, None] + xs[None, :]) % 2).astype(bool)
sub = (slice(0, H, 2), slice(0, W, 2))
dark_ext = (g < 242)
# separable phase search: column profile of dark fraction over exterior, row profile likewise
# 2-D grid search: tile size near 2048/90 (90 tiles across), phase near 0; scored on exterior tile pixels
ys_, xs_ = np.nonzero(ext_rgb); rs = np.random.default_rng(0).choice(len(xs_), min(40000, len(xs_)), replace=False)
xs_, ys_ = xs_[rs].astype(np.float64), ys_[rs].astype(np.float64); dk = dark_ext[ys_.astype(int), xs_.astype(int)]
best = (0, None)
for t_ in np.arange(22.55, 22.95, 0.005):
    for px_ in np.arange(-4, 4.01, 0.5):
        for py_ in np.arange(-4, 4.01, 0.5):
            pp = ((np.floor((xs_ - px_) / t_) + np.floor((ys_ - py_) / t_)) % 2).astype(bool)
            sc = max((pp == dk).mean(), (pp != dk).mean())
            if sc > best[0]: best = (sc, (t_, px_, py_))
agree, (t, phx, phy) = best
P = parity(t, phx, phy)
if ((P == dark_ext) & ext_rgb).sum() < ((P != dark_ext) & ext_rgb).sum(): P = ~P
light_c = np.median(rgb[ext_rgb & ~P], 0); grey_c = np.median(rgb[ext_rgb & P], 0)

# ---- 2. exterior flood ----
tile_like = (sat < 16) & (g > 212)
passable = T | tile_like
lab, n = nd.label(passable)
border = np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]])); border = border[border > 0]
ext = np.isin(lab, border)
cleared_flood = ext & ~T
al[ext] = 0
# stray opaque islands
op = al > 127
lab2, n2 = nd.label(op)
sizes = nd.sum(op, lab2, range(1, n2 + 1))
main = 1 + int(np.argmax(sizes))
small = np.isin(lab2, [i + 1 for i, s in enumerate(sizes) if s < 1500 and i + 1 != main])
# only islands lying in the exterior (outside the filled design silhouette)
sil = nd.binary_fill_holes(lab2 == main)
small &= ~sil
cleared_islands = small.copy(); al[small] = 0

# ---- 3. parchment tile flattening ----
op = al > 127
r, gg, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
parch = op & (g > 150) & (r > gg) & (gg > b) & (r - b > 18) & (r - b < 90) & sil
parch = nd.binary_erosion(parch, iterations=2)
# also the light low-sat checker tiles that sit inside the scroll (opaque white/grey inside silhouette)
inner_tile = op & tile_like & sil & ~nd.binary_dilation(~sil, iterations=3)
# The baked tiles inside the scroll are hand-drawn (irregular, ~22-25 px), so the global grid only seeds the exterior;
# inside, the tile classes are segmented locally: ink-free parchment luminance -> 7px median (keeps tile steps) ->
# minus a sigma-30 trend -> sign = light/grey tile class, cleaned with a 3px open/close.
gl = np.where(parch, g, 0); den = nd.gaussian_filter(parch.astype(np.float32), 3)
_, (iy, ix) = nd.distance_transform_edt(~parch, return_indices=True); gfill = g[iy, ix]   # ink -> nearest parchment value
med = nd.median_filter(gfill, 7)
trend = nd.gaussian_filter(np.where(parch, med, 0), 30) / np.maximum(nd.gaussian_filter(parch.astype(np.float32), 30), 1e-3)
resid = med - trend
Pin = resid < 0                                    # grey-tile class
Pin = nd.binary_opening(Pin, iterations=3); Pin = nd.binary_closing(Pin, iterations=3)
S = 16.0
for ch in range(3):
    c = rgb[..., ch]
    mL = parch & ~Pin; mG = parch & Pin
    numL = nd.gaussian_filter(np.where(mL, c, 0), S); denL = nd.gaussian_filter(mL.astype(np.float32), S)
    numG = nd.gaussian_filter(np.where(mG, c, 0), S); denG = nd.gaussian_filter(mG.astype(np.float32), S)
    ok = (denL > 0.08) & (denG > 0.08)
    gain = np.where(ok, (numL / np.maximum(denL, 1e-6)) / np.maximum(numG / np.maximum(denG, 1e-6), 1), 1.0)
    gain = np.clip(gain, 1.0, 1.15)
    # apply to grey-class parchment AND the ink-free halo around it (soft 1px feather at class edges)
    tgt = Pin & nd.binary_dilation(parch, iterations=1) & (al > 127) & (g > 120) & ok
    c2 = c.copy(); c2[tgt] = np.clip(c[tgt] * gain[tgt], 0, 255); rgb[..., ch] = c2
fixed_px = int((parch & Pin).sum())
# inner light/grey tile pixels inside the scroll: map grey tiles to the light tile colour
it = inner_tile & P
rgb[it] = np.clip(rgb[it] * (light_c / np.maximum(grey_c, 1)), 0, 255)

# ---- 4. enclosed holes ----
T2 = al < 10
lab3, n3 = nd.label(T2)
bl = np.unique(np.concatenate([lab3[0], lab3[-1], lab3[:, 0], lab3[:, -1]]))
hs = nd.sum(T2, lab3, range(1, n3 + 1))
fill_ids = [i + 1 for i, s in enumerate(hs) if (i + 1) not in bl and s < 0.005 * H * W]
holes = np.isin(lab3, fill_ids)
rgb[holes] = 254; al[holes] = 255
big_enclosed = int(sum(s for i, s in enumerate(hs) if (i + 1) not in bl and s >= 0.005 * H * W))

out = np.dstack([rgb, al]); out[al < 10, :3] = 0  # clean matte under transparent pixels
Image.fromarray(np.clip(out + 0.5, 0, 255).astype(np.uint8), 'RGBA').save(OUT, optimize=True)
met = dict(src=SRC, out=OUT, px=[W, H], tile_px=round(float(t), 3), phase=[float(phx), float(phy)], grid_agreement=round(float(agree), 4),
           tile_light_rgb=[int(v) for v in light_c], tile_grey_rgb=[int(v) for v in grey_c],
           exterior_tile_px_cleared=int(cleared_flood.sum()), stray_island_px_cleared=int(cleared_islands.sum()),
           parchment_grey_tile_px_gain_corrected=fixed_px, inner_tile_px_recoloured=int(it.sum()),
           enclosed_holes_filled=len(fill_ids), enclosed_hole_px_filled=int(holes.sum()), big_enclosed_transparent_px_kept=big_enclosed,
           transparent_frac_before=round(float(T.mean()), 4), transparent_frac_after=round(float((al < 10).mean()), 4))
json.dump(met, open(MET, 'w'), indent=1); print(met)

# ---- residual tile contrast (same class map, before vs after) ----
def tile_contrast(rgb_):
    g_ = rgb_.mean(2); m_ = parch
    return float(g_[m_ & ~Pin].mean() - g_[m_ & Pin].mean())
before_tc = tile_contrast(a[..., :3]); after_tc = tile_contrast(rgb)
met.update(parchment_tile_contrast_before=round(before_tc, 2), parchment_tile_contrast_after=round(after_tc, 2),
           parchment_tile_contrast_reduction=round(1 - after_tc / before_tc, 3))
json.dump(met, open(MET, 'w'), indent=1); print('tile contrast', before_tc, after_tc)
