"""MY ELF MADE / MADE ME DO IT -> MY ELF / MADE ME DO IT.
Removes the line-1 'MADE' (and the ornaments between ELF and MADE), then rotates the
'MY ELF' group along line 1's own arc so it is centred over line 2. Line-2 outlines
that were shared with the removed glyphs are rebuilt at the measured outline width.
Original glyph pixels are re-used (no re-typesetting). Run: python3 -I fix_elf.py"""
import sys; sys.path.insert(0, "/home/user/crowned-co-data/work/d6_new_art/text_fix/scripts")
from common import *
import math

sha_w, p_w = src('d7531299c7')      # white-bg RGB (identical pixels to 111997c641)
sha_t, p_t = src('f9fe64d6e0')      # transparent cut, pixel-aligned
a = load_rgba(p_w)
rgb = a[..., :3].copy()
H, W = rgb.shape[:2]
r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
mn = rgb.min(-1)

# exterior background (same gated flood as phase 2)
_, _ = P.fix_white_box(a)
ext = P.bgmask_cache['bg'].copy()
opaque = ~ext

red = (r > 180) & (g < 110) & (b < 110)
lab, n = ndi.label(red)
objs = ndi.find_objects(lab)
sz = ndi.sum(red, lab, range(1, n + 1))
L1 = {}
for i in range(n):
    sl = objs[i]
    if sz[i] > 5000 and sl[0].start < 200:
        cx = (sl[1].start + sl[1].stop) / 2
        L1[i + 1] = cx
ids = sorted(L1, key=lambda k: L1[k])
assert len(ids) == 9, ids
MY_ELF = ids[:5]; MADE = ids[5:]

def hull(idl):
    m = np.isin(lab, idl)
    m = ndi.binary_closing(m, iterations=6)
    m = ndi.binary_fill_holes(m)
    return m

h_me = hull(MY_ELF)
h_md = hull(MADE)
dark = opaque & (rgb.max(-1) < 135)
near1 = ndi.binary_dilation(h_me | h_md, iterations=5)
_wf = opaque & (mn > 215) & ~near1
_wl, _wn = ndi.label(_wf)
_ws = ndi.sum(_wf, _wl, range(1, _wn + 1))
_wc = ndi.center_of_mass(_wf, _wl, range(1, _wn + 1))
_keepw = [i + 1 for i in range(_wn) if _ws[i] > 1500 and _wc[i][0] > 400]
other_fill = ndi.binary_opening(opaque & ~dark & ~near1 & ~_wf, iterations=3) | np.isin(_wl, _keepw)
# owner map by nearest fill
owner_lab = np.zeros((H, W), np.int8)
owner_lab[other_fill] = 3
owner_lab[h_me] = 1
owner_lab[h_md] = 2
_, (iy, ix) = ndi.distance_transform_edt(owner_lab == 0, return_indices=True)
owner = owner_lab[iy, ix]

# outline width: distance-to-exterior measured on the red hull boundary of MY ELF
d_me = ndi.distance_transform_edt(~h_me)
d_ext = ndi.distance_transform_edt(~ext)
edge = h_me & ~ndi.binary_erosion(h_me)
t_out = float(np.median(d_ext[edge]))
print('outline width ~', round(t_out, 1))
R = int(math.ceil(2.2 * t_out))

d_md = ndi.distance_transform_edt(~h_md)
band = np.zeros((H, W), bool); band[:720] = True
rem = band & opaque & (owner == 2) & (d_md <= R)
grp = band & opaque & (owner == 1) & (d_me <= R)
grp_move = band & opaque & (owner == 1) & (d_me <= t_out + 2.5)   # letter + its own outline only

# small ornament components
olab, on = ndi.label(opaque)
osz = ndi.sum(opaque, olab, range(1, on + 1))
oobj = ndi.find_objects(olab)
big = set((np.argsort(-osz)[:1] + 1).tolist())
orn_rm, orn_grp = [], []
for i in range(on):
    if (i + 1) in big or osz[i] > 6000:
        continue
    sl = oobj[i]
    cy, cx = (sl[0].start + sl[0].stop) / 2, (sl[1].start + sl[1].stop) / 2
    if cy < 330 and 1095 <= cx <= 1160:
        orn_rm.append(i + 1)           # dots / star between ELF and MADE
    elif cy < 330 and 670 <= cx <= 745:
        orn_grp.append(i + 1)          # dot / snowflake between MY and ELF
    elif cy < 330 and 1160 < cx < 1730 and h_md[int(cy), int(cx)]:
        orn_rm.append(i + 1)
    elif 260 < cy < 300 and 1200 <= cx <= 1250:
        orn_rm.append(i + 1)           # red dot hanging under MADE's 'M'
print('ornaments removed', len(orn_rm), 'moved', len(orn_grp))
rem |= np.isin(olab, orn_rm)
grp |= np.isin(olab, orn_grp)
grp_move |= np.isin(olab, orn_grp)
# include anti-aliased fringe (1px) around both masks, limited to non-owned-by-line2
fr = ndi.binary_dilation(rem, iterations=2) & ~opaque
rem |= fr
fr = ndi.binary_dilation(grp, iterations=2) & ~opaque
grp |= fr
grp_move |= ndi.binary_dilation(grp_move, iterations=2) & ~opaque

# arc centre from baselines of the 9 letters
pts = []
for k in ids:
    ys, xs = np.nonzero(lab == k)
    pts.append((xs.mean(), ys.max()))
Pm = np.array(pts)
A = np.c_[2 * Pm[:, 0], 2 * Pm[:, 1], np.ones(len(Pm))]
cx0, cy0, c0 = np.linalg.lstsq(A, (Pm ** 2).sum(1), rcond=None)[0]
print('arc centre', round(cx0), round(cy0))

# target centre = centre of line 2 (opaque text 380..700, owner==3, dark or fill) bbox
gy, gx = np.nonzero(grp)
g_cx = (gx.min() + gx.max()) / 2
l2 = opaque & (owner == 3) & (np.arange(H)[:, None] > 330) & (np.arange(H)[:, None] < 640)
l2x = np.nonzero(l2.any(0))[0]
# restrict to the main text span (ignore far side swooshes)
tgt = (np.percentile(np.nonzero(l2)[1], 1) + np.percentile(np.nonzero(l2)[1], 99)) / 2
print('group centre', g_cx, 'target', tgt)
ang_g = math.atan2(g_cx - cx0, cy0 - 250)
ang_t = math.atan2(tgt - cx0, cy0 - 250)
theta = math.degrees(ang_t - ang_g)
print('rotate (deg, clockwise +)', round(theta, 2))

canvas = rgb.copy()
canvas[rem | grp] = 255.0
# rebuild line-2 outline where it was shared
wf = opaque & (mn > 215)
gf = opaque & (g > 150) & (r < 130) & (b < 120)
cand2 = (wf | gf) & (np.arange(H)[:, None] > 200) & ~near1
l2l, l2n = ndi.label(cand2)
l2s = ndi.sum(cand2, l2l, range(1, l2n + 1))
l2c = ndi.center_of_mass(cand2, l2l, range(1, l2n + 1))
fill2 = np.isin(l2l, [i + 1 for i in range(l2n) if 1500 < l2s[i] < 30000 and 330 < l2c[i][0] < 520])
d2 = ndi.distance_transform_edt(~fill2)
outline_col = np.median(rgb[dark & (owner == 3) & band], axis=0)
edge2 = fill2 & ~ndi.binary_erosion(fill2)
t2 = float(np.median(d_ext[edge2 & ~ndi.binary_dilation(rem | grp, iterations=25)]))
print('line-2 outline width (fill edge -> exterior)', t2)
cov = np.clip(t2 - 0.5 - d2, 0, 1)          # anti-aliased outline coverage
rebuild = (rem | grp) & (cov > 0) & ~fill2
cw_ = cov[rebuild][:, None]
canvas[rebuild] = cw_ * outline_col + (1 - cw_) * canvas[rebuild]
print('rebuilt outline px', int(rebuild.sum()))
# seam clean-up: near the removed/moved glyphs, nothing may sit outside line-2's outline radius
small_orn = [i + 1 for i in range(on) if (i + 1) not in big and osz[i] <= 6000 and (i + 1) not in orn_rm and (i + 1) not in orn_grp]
orn_keep = np.isin(olab, small_orn)
zone = ndi.binary_dilation(rem | grp, iterations=12)
seam = zone & (d2 > t2 + 0.5) & ~fill2 & ~orn_keep & opaque & ~(rem | grp)
canvas[seam] = 255.0
print('seam px cleared', int(seam.sum()))

layer = np.where(grp_move[..., None], rgb, 255.0).astype(np.uint8)
L = Image.fromarray(layer, 'RGB')
M = Image.fromarray((grp_move * 255).astype(np.uint8), 'L')
# PIL rotate: positive = counter-clockwise, so use -theta
Lr = np.asarray(L.rotate(-theta, resample=Image.BICUBIC, center=(cx0, cy0), fillcolor=(255, 255, 255))).astype(np.float32)
Mr = np.asarray(M.rotate(-theta, resample=Image.BICUBIC, center=(cx0, cy0), fillcolor=0)).astype(np.float32) / 255.0
# collision check against what remains
remain = (canvas.min(-1) < 200)
coll = (Mr > 0.5) & remain & ~(np.isin(owner, [1]))
print('collision px', int(coll.sum()))
canvas = Mr[..., None] * Lr + (1 - Mr[..., None]) * canvas
out = np.dstack([canvas, np.full((H, W), 255.0, np.float32)])
fixed, info = P.fix_white_box(out)
bg1 = P.bgmask_cache['bg']
# enclosed white gaps created/moved by the edit (between letters) -> background too
foot = ndi.binary_dilation(rem | grp | (Mr > 0.02), iterations=20)
cw = (canvas.min(-1) >= 228) & ~bg1
cl, cn = ndi.label(cw)
cs = ndi.sum(cw, cl, range(1, cn + 1))
hit = np.unique(cl[foot & cw]); hit = hit[hit > 0]
keep_fill = np.unique(cl[fill2 & cw]); keep_fill = keep_fill[keep_fill > 0]
gaps = np.isin(cl, np.setdiff1d(hit, keep_fill))
# letter counters / slivers in the text band (white = background in the design)
co = cl[:720]
small = np.nonzero(cs < 3000)[0] + 1
counters = np.zeros_like(cw); counters[:720] = np.isin(co, small)
# leftover outline fragments from the old glyph positions
op = ~(bg1 | gaps | counters)
fl, fn = ndi.label(op)
fs = ndi.sum(op, fl, range(1, fn + 1))
oldfoot = (rem | grp) & (Mr < 0.02)
frag_ids = [i + 1 for i in range(fn) if fs[i] < 4000]
specks = np.isin(fl, [i + 1 for i in range(fn) if fs[i] < 80]) & foot
frag = np.isin(fl, frag_ids) & ~np.isin(olab, list(range(1, on + 1)) and np.zeros(1)) 
fh = np.unique(fl[oldfoot & np.isin(fl, frag_ids)]); fh = fh[fh > 0]
frag = np.isin(fl, fh) | specks
canvas[frag] = 255.0
out = np.dstack([canvas, np.full((H, W), 255.0, np.float32)])
bg2 = bg1 | gaps | counters | frag | (seam & (Mr < 0.02))
fixed = P.edge_ring_unmix(out, bg2, ring_px=2)
info['fragments_cleared_px'] = int(frag.sum())
info['counters_cleared_px'] = int(counters.sum())
info['edit_gap_px_cleared'] = int(gaps.sum())
print(info)
np.save(WK + '/elf_dbg.npy', np.stack([rem, grp, rebuild, Mr > 0.5]))
Image.fromarray(Lr.astype(np.uint8)).save(WK + '/elf_Lr.png')
save_rgba(fixed, WK + '/elf_fixed.png')
json.dump({'theta_deg': theta, 'outline_px': t_out, 'collision_px': int(coll.sum()),
           'arc_centre': [cx0, cy0], 'rebuilt_outline_px': int(rebuild.sum()), **info},
          open(WK + '/elf_meta.json', 'w'), indent=1)
