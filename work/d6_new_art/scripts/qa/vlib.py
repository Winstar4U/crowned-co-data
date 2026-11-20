"""Independent QA for D6 local art fixes. Local files only; run with python3 -I."""
import json, os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage as ndi
Image.MAX_IMAGE_PIXELS = None
OUT = '/home/user/crowned-co-data/work/d6_new_art'
VER = OUT + '/verify'
os.makedirs(VER, exist_ok=True)
EIGHT = np.ones((3, 3), bool)
BLACK, WHITE = (17, 17, 17), (249, 249, 249)
BLANKS = {
 '5546': [('gray apron', (128, 128, 128))], '10823': [('black backpack', BLACK)], '1698': [('black hat', BLACK)],
 '713': [('black apron', BLACK)], '2005': [('black hoodie', BLACK)], '66': [('black fleece', BLACK)],
 '9': [('black tee', BLACK)], '1436': [('black crew', BLACK)], '10796': [('black shorts', BLACK)],
 '77': [('black hoodie', BLACK)], '568': [('blue onesie', (46, 84, 160))],
 '468': [('white sublim.', WHITE)], '2662': [('white duvet', WHITE)], '582': [('white mousepad', WHITE)],
 '5353': [('white pillow', WHITE)], '1646': [('white napkin', WHITE)], '643': [('white board', WHITE)],
 '430': [('white pin', WHITE)], '1245': [('clear glass/white', (240, 240, 240))],
}


def blanks_for(bp, pl):
    b = list(BLANKS.get(str(bp), [('black', BLACK)]))
    if (('contrast_vs_white' in pl) or ('white hoodie' in ' '.join(pl.get('notes', [])).lower())) and not any(c == WHITE for _, c in b):
        b.append(('white variant', WHITE))
    return b


def load(p):
    return np.asarray(Image.open(p).convert('RGBA')).astype(np.float32)


def lum(c):
    c = c / 255.0
    c = np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * c[..., 0] + 0.7152 * c[..., 1] + 0.0722 * c[..., 2]


def contrast_low_frac(a, col, thr=2.0):
    op = a[..., 3] > 128
    if not op.any():
        return 1.0
    L = lum(a[..., :3][op]); Lb = lum(np.array(col, np.float32)[None])[0]
    hi, lo = np.maximum(L, Lb), np.minimum(L, Lb)
    return float(((hi + 0.05) / (lo + 0.05) < thr).mean())


def design_mask(o, cat):
    rgb, al = o[..., :3], o[..., 3]
    mn, mx = rgb.min(-1), rgb.max(-1)
    if cat == 'white_box':
        return (al > 128) & ~((mn >= 228) & (mx - mn <= 28))
    if cat == 'checkerboard':
        return (al > 128) & ~((mn >= 112) & (mx - mn <= 16))
    return al > 128


def tile_energy(a):
    """alternating-tile energy: max over tile size t of the fraction of canvas px p where
    p, p+(0,t), p+(t,0), p+(t,t) are opaque neutral-light, horizontal and vertical steps
    flip tone (6..90) and the diagonal returns to the same tone (<5)."""
    rgb = a[..., :3]; mn, mx = rgb.min(-1), rgb.max(-1)
    M = (a[..., 3] > 200) & (mn >= 112) & (mx - mn <= 16)
    N = M.size
    if M.sum() < 0.0005 * N:
        return 0.0, 0
    L = rgb.mean(-1)
    best, bt = 0.0, 0
    for t in range(3, 41):
        m = M[:-t, :-t] & M[t:, :-t] & M[:-t, t:] & M[t:, t:]
        if not m.any():
            continue
        p = L[:-t, :-t]
        h = np.abs(p - L[:-t, t:]); v = np.abs(p - L[t:, :-t]); d = np.abs(p - L[t:, t:])
        c = m & (h >= 6) & (h <= 90) & (v >= 6) & (v <= 90) & (d < 5)
        e = float(c.sum()) / N
        if e > best:
            best, bt = e, t
    return best, bt


def specks(a):
    """isolated small components (area < 0.02% canvas) farther than 1.5% of min dim
    from any larger component; returns (count, area frac, neutral-light count)."""
    H, W = a.shape[:2]; N = H * W
    op = a[..., 3] > 128
    lab, n = ndi.label(op, structure=EIGHT)
    if n == 0:
        return 0, 0.0, 0
    idx = np.arange(1, n + 1)
    area = ndi.sum(np.ones_like(lab), lab, idx)
    big = np.isin(lab, idx[area >= 0.0002 * N])
    if not big.any():
        return 0, 0.0, 0
    dist = ndi.distance_transform_edt(~big)
    md = ndi.minimum(dist, lab, idx)
    small = (area < 0.0002 * N) & (md > 0.015 * min(H, W))
    rgb = a[..., :3]; mn, mx = rgb.min(-1), rgb.max(-1)
    nl = (mn >= 112) & (mx - mn <= 16)
    nlc = ndi.sum(nl & op, lab, idx)
    return int(small.sum()), float(area[small].sum() / N), int((small & (nlc >= 0.5 * area)).sum())


def edge_opaque(a):
    al = a[..., 3]; H, W = al.shape
    b = max(2, int(0.01 * min(H, W)))
    border = np.concatenate([al[:b].ravel(), al[-b:].ravel(), al[:, :b].ravel(), al[:, -b:].ravel()])
    return float((border > 128).mean())


def eff_dpi(W, pl):
    """effective dpi = 300 * image_px_width / (placeholder_px_width * scale) on the
    largest enabled variant placeholder (Printify scale is relative to print-area width)."""
    ph = pl.get('placeholders') or {}
    groups = pl.get('proposed_per_variant_group') or {}
    base = pl.get('proposed') or pl.get('current') or {}
    worst = None
    for vid, (pw, phh) in ph.items():
        sc = base.get('scale', 1.0) or 1.0
        for g, gv in (groups.items() if isinstance(groups, dict) else []):
            if isinstance(gv, dict) and vid in str(gv.get('variants', gv.get('variant_ids', ''))):
                sc = (gv.get('proposed') or gv).get('scale', sc)
        d = 300.0 * W / (pw * sc)
        if worst is None or d < worst[0]:
            worst = (d, vid, pw, phh, sc)
    return worst


def white_holes_vs_orig(o, f):
    """fraction of original near-white opaque px enclosed inside the design (not edge
    connected) that became transparent - info only."""
    return None


def qa_metrics(orig, fixed, cat):
    if orig.shape[:2] != fixed.shape[:2]:
        im = Image.fromarray(np.clip(orig, 0, 255).astype(np.uint8), 'RGBA').resize((fixed.shape[1], fixed.shape[0]), Image.LANCZOS)
        orig = np.asarray(im).astype(np.float32)
    dm = design_mask(orig, cat)
    lost = dm & (fixed[..., 3] < 128)
    loss = float(lost.sum() / max(dm.sum(), 1))
    core = ndi.binary_erosion(dm, iterations=2)
    core_loss = float((lost & core).sum() / max(core.sum(), 1))
    keep = dm & (fixed[..., 3] >= 250) & (orig[..., 3] >= 250)
    rgbd = float(np.abs(fixed[..., :3][keep] - orig[..., :3][keep]).mean()) if keep.any() else 0.0
    te, tt = tile_energy(fixed)
    te0, tt0 = tile_energy(orig)
    sc, sf, snl = specks(fixed)
    return dict(design_px=int(dm.sum()), loss_pct=round(100 * loss, 3), core_loss_pct=round(100 * core_loss, 3), lost_mask=lost, kept_rgb_mae=round(rgbd, 2),
                tile_E=round(te, 5), tile_t=tt, tile_E_orig=round(te0, 5), speck_n=sc, speck_frac=round(sf, 5), speck_nl=snl,
                edge_opaque=round(edge_opaque(fixed), 4), transparent_frac=round(float((fixed[..., 3] < 8).mean()), 4))


FONT = ImageFont.load_default()


def comp(a, col, size):
    im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8), 'RGBA')
    im = im.copy(); im.thumbnail((size, size), Image.LANCZOS)
    bg = Image.new('RGBA', (size, size), col + (255,))
    bg.alpha_composite(im, ((size - im.width) // 2, (size - im.height) // 2))
    return bg.convert('RGB')


def zoom_box(fixed, lost):
    """1:1 crop centred on the worst area: lost design px if any, else most neutral-light opaque px, else centre."""
    H, W = fixed.shape[:2]; S = min(360, H, W)
    rgb = fixed[..., :3]; mn, mx = rgb.min(-1), rgb.max(-1)
    w = lost.astype(np.float32) * 4 + ((fixed[..., 3] > 128) & (mn >= 112) & (mx - mn <= 16)).astype(np.float32)
    w = ndi.uniform_filter(w, size=S // 2)
    if w.max() <= 0:
        cy, cx = H // 2, W // 2
    else:
        cy, cx = np.unravel_index(np.argmax(w), w.shape)
    y0 = int(np.clip(cy - S // 2, 0, H - S)); x0 = int(np.clip(cx - S // 2, 0, W - S))
    return y0, x0, S


def render(pid, label, orig, fixed, blanks, lost, status_line):
    T = 380
    rows = []
    y0, x0, S = zoom_box(fixed, lost)
    for name, col in blanks:
        crop = fixed[y0:y0 + S, x0:x0 + S]
        rows.append((name, comp(orig, col, T), comp(fixed, col, T), comp(crop, col, T)))
    # loss overlay row (magenta = lost design px) on first blank
    sheet = Image.new('RGB', (3 * T + 40, 48 + len(rows) * (T + 22) + 4), (255, 255, 255))
    d = ImageDraw.Draw(sheet)
    d.text((8, 4), label, fill=(0, 0, 0), font=FONT)
    d.text((8, 20), status_line, fill=(0, 0, 160), font=FONT)
    y = 36
    for name, b, a, z in rows:
        d.text((8, y), f'BEFORE on {name}', fill=(160, 0, 0), font=FONT)
        d.text((T + 20, y), f'AFTER on {name}', fill=(0, 110, 0), font=FONT)
        d.text((2 * T + 32, y), f'AFTER 1:1 crop @({x0},{y0}) {S}px', fill=(0, 110, 0), font=FONT)
        y += 14
        sheet.paste(b, (8, y)); sheet.paste(a, (T + 20, y)); sheet.paste(z, (2 * T + 32, y))
        y += T + 8
    sheet.save(f'{VER}/{pid}.png')
    return f'{VER}/{pid}.png'


def contact_sheets(paths, prefix='verify_sheet_', per=6, start=1, width=1200):
    out = []
    for k in range(0, len(paths), per):
        ims = [Image.open(p) for p in paths[k:k + per]]
        ims = [im.resize((width // 2, int(im.height * (width // 2) / im.width)), Image.LANCZOS) for im in ims]
        rows = [ims[i:i + 2] for i in range(0, len(ims), 2)]
        H = sum(max(i.height for i in r) for r in rows)
        sh = Image.new('RGB', (width, H), (255, 255, 255))
        y = 0
        for r in rows:
            for j, im in enumerate(r):
                sh.paste(im, (j * (width // 2), y))
            y += max(i.height for i in r)
        p = f'{VER}/{prefix}{start + k // per}.png'
        sh.save(p); out.append(p)
    return out
