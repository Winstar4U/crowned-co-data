"""400px thumbnail sources -> rebuild from the full-res (2048px) master of the SAME design found
elsewhere in the D6 originals (signature search, corr >= 0.996). The master is re-framed with the
similarity transform estimated master->thumbnail (ORB + RANSAC), so the printed framing matches the
current placement; resolution goes up ~5x. Transparent thumbnails get a transparent output
(phase-2 gated white-flood when the master has a white background)."""
import sys; sys.path.insert(0, "/home/user/crowned-co-data/work/d6_new_art/text_fix/scripts")
from common import *
import cv2

MAP = {  # low-res sha prefix -> master file (raw) and note
    'bc19514d3a': '/home/user/crowned-co-data/work/d6_batch10/6ac71653f2868c4f0a02171a/original.png',
    'b46be3ec39': '/home/user/crowned-co-data/work/d6_batch9/6ac7101a050d0f25a7091893/original.png',
    '5312ae6d6c': '/home/user/crowned-co-data/work/d6_batch6/6ac6fe9c7a961335020e18a9/original.png',
    '277d653404': '/home/user/crowned-co-data/work/d6_batch9/6ac712c0b32a96bbe40d0cf2/original.png',
    '50f323a7a6': '/home/user/crowned-co-data/work/d6_batch4/6ac701e535cf3f6ec802e201/original.png',
    'd402b87a81': WK + '/patience_fixed_rgb.png',      # patience master, already text-fixed
    'c0a403dd61': WK + '/receipt_fixed.png',           # receipt master, already text-fixed
}

def gray(a):
    al = a[..., 3:4] / 255.0
    return np.clip(a[..., :3] * al + 255 * (1 - al), 0, 255).mean(-1).astype(np.uint8)

def est(master, small):
    """similarity master->small via ORB on master downscaled to ~small size"""
    k = small.shape[1] / master.shape[1]
    mg = cv2.resize(gray(master), None, fx=k * 2, fy=k * 2, interpolation=cv2.INTER_AREA)
    sg = cv2.resize(gray(small), None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    orb = cv2.ORB_create(5000, edgeThreshold=15, patchSize=15)
    k1, d1 = orb.detectAndCompute(mg, None); k2, d2 = orb.detectAndCompute(sg, None)
    m = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True).match(d1, d2)
    p1 = np.float32([k1[x.queryIdx].pt for x in m]); p2 = np.float32([k2[x.trainIdx].pt for x in m])
    M, inl = cv2.estimateAffinePartial2D(p1, p2, ransacReprojThreshold=1.5)
    # compose: master px -> mg (x 2k) -> sg -> small (/2)
    S1 = np.array([[2 * k, 0, 0], [0, 2 * k, 0], [0, 0, 1]]); S2 = np.array([[0.5, 0, 0], [0, 0.5, 0], [0, 0, 1]])
    Mf = S2 @ np.vstack([M, [0, 0, 1]]) @ S1
    return Mf[:2], int(inl.sum()), len(m)

meta = {}
for pre, mpath in MAP.items():
    sha, sp = src(pre)
    small = load_rgba(sp); master = load_rgba(mpath)
    transparent_small = (small[..., 3] < 250).mean() > 0.02
    M, ni, nm = est(master, small)
    s = float(np.sqrt(abs(np.linalg.det(M[:, :2]))))
    # output canvas: thumbnail framing at master resolution
    up = 1.0 / s
    Wo, Ho = int(round(small.shape[1] * up)), int(round(small.shape[0] * up))
    A = M * up                        # master -> output (pure ~translation at scale ~1)
    if transparent_small and (master[..., 3] > 250).all():
        P.fix_white_box(master); bg = P.bgmask_cache['bg']
        master = P.edge_ring_unmix(master, bg, ring_px=2)
    pm = master.copy(); pm[..., :3] *= pm[..., 3:4] / 255.0
    out = cv2.warpAffine(pm, A, (Wo, Ho), flags=cv2.INTER_LANCZOS4, borderValue=(255, 255, 255, 255) if not transparent_small else 0)
    out = np.clip(out, 0, 255); al = out[..., 3:4]
    out[..., :3] = np.where(al > 0, out[..., :3] * 255.0 / np.maximum(al, 1e-6), 0)
    # thumbnail-guided background cleanup: regions opaque here but transparent in the thumbnail
    # (enclosed white counters, white haze) are cleared when they are low-saturation light pixels.
    cleared = 0
    if transparent_small:
        T = cv2.resize(small[..., 3], (Wo, Ho), interpolation=cv2.INTER_CUBIC)
        rgbm = out[..., :3]; sat = rgbm.max(-1) - rgbm.min(-1)
        cand = (out[..., 3] > 40) & (T < 60) & (rgbm.min(-1) > 232) & (sat < 18)
        lab, n = ndi.label(cand)
        if n:
            sz = ndi.sum(cand, lab, range(1, n + 1))
            keep = np.nonzero(sz >= 30)[0] + 1
            clr = np.isin(lab, keep)
            # only where the thumbnail is clearly transparent across the component's core
            clr = ndi.binary_dilation(clr, iterations=1) & (T < 90)
        else:
            clr = np.zeros(T.shape, bool)
        # anything where the live thumbnail is fully transparent stays transparent (haze/smudges)
        haze = (out[..., 3] > 0) & (cv2.GaussianBlur(T, (0, 0), 2.0) < 12)
        clr = clr | haze
        if True:
            cleared = int(clr.sum())
            out = P.edge_ring_unmix(out, clr | (out[..., 3] < 1), ring_px=1)
    # verification: downscale output to thumbnail size and compare on opaque pixels
    back = cv2.resize(out, (small.shape[1], small.shape[0]), interpolation=cv2.INTER_AREA)
    op = (small[..., 3] > 200) & (back[..., 3] > 200)
    diff = float(np.abs(back[..., :3] - small[..., :3])[op].mean())
    aiou = float(((small[..., 3] > 128) & (back[..., 3] > 128)).sum() / max(((small[..., 3] > 128) | (back[..., 3] > 128)).sum(), 1))
    save_rgba(out, WK + f'/lowres_{pre}.png')
    meta[sha] = {'master': mpath, 'scale_master_to_thumb': round(s, 5), 'orb_inliers': ni, 'out_px': [Wo, Ho],
                 'transparent': bool(transparent_small), 'thumb_guided_cleared_px': cleared, 'thumb_diff_mean': round(diff, 2), 'alpha_iou': round(aiou, 4)}
    print(pre, meta[sha])
json.dump(meta, open(WK + '/lowres_meta.json', 'w'), indent=1)
