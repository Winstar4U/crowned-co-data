"""D6 phase 2: local mechanical fixes (white_box / checkerboard / low_contrast).
Reads inventory.csv, writes fixed/<sha1>.png, previews/<product_id>.png, metrics.json.
Local files only. Run with python3 -I."""
import csv, json, os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage as ndi

Image.MAX_IMAGE_PIXELS = None
OUT = '/home/user/crowned-co-data/work/d6_new_art'
FIX = OUT + '/fixed'
PRV = OUT + '/previews'
os.makedirs(FIX, exist_ok=True)
os.makedirs(PRV, exist_ok=True)
LOCAL = {'white_box', 'checkerboard', 'low_contrast'}
FOUR = ndi.generate_binary_structure(2, 1)


def load(p):
    return np.asarray(Image.open(p).convert('RGBA')).astype(np.float32)


def border_connected(mask):
    lab, n = ndi.label(mask, structure=FOUR)
    if n == 0:
        return np.zeros_like(mask)
    edge = np.unique(np.concatenate([lab[0], lab[-1], lab[:, 0], lab[:, -1]]))
    edge = edge[edge > 0]
    return np.isin(lab, edge)


def edge_ring_unmix(a, cleared, ring_px=2, soft=60.0):
    """Feather 1-2px: pixels within ring_px of the cleared bg get alpha from their
    distance to white, then colour is un-mixed from white to kill the halo."""
    rgb, al = a[..., :3], a[..., 3]
    dist = ndi.distance_transform_edt(~cleared)
    ring = (~cleared) & (dist <= ring_px)
    mn = rgb.min(-1)
    est = np.clip((255.0 - mn) / soft, 0.0, 1.0)
    alpha_ring = np.where(ring, est, 1.0)
    alpha_ring = np.maximum(alpha_ring, 0.0)
    safe = np.maximum(alpha_ring, 1e-3)[..., None]
    un = np.clip((rgb - (1 - alpha_ring[..., None]) * 255.0) / safe, 0, 255)
    rgb2 = np.where(ring[..., None], un, rgb)
    al2 = al * alpha_ring
    al2[cleared] = 0
    out = np.dstack([rgb2, al2])
    return out


def gated_flood(cand, k, N):
    """Border flood that cannot leak through gaps narrower than ~2k px.
    Small regions reachable only through narrow gaps (slivers between letters)
    are still cleared; large enclosed design areas are protected."""
    full = border_connected(cand)
    er = ndi.binary_erosion(cand, iterations=k, border_value=1)
    seed = border_connected(er)
    g = ndi.binary_dilation(seed, iterations=k + 1, mask=cand)
    diff = full & ~g
    lab, n = ndi.label(diff, structure=FOUR)
    protected = 0
    if n:
        idx = np.arange(1, n + 1)
        area = ndi.sum(np.ones_like(lab), lab, idx)
        small = idx[area < 0.0004 * N]
        g = g | np.isin(lab, small)
        protected = int(area[area >= 0.0004 * N].sum())
    return g, protected


def low_contrast_mask(a, bg=(17, 17, 17)):
    def lum(c):
        c = c / 255.0
        c = np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
        return 0.2126 * c[..., 0] + 0.7152 * c[..., 1] + 0.0722 * c[..., 2]
    L = lum(a[..., :3])
    Lb = lum(np.array(bg, np.float32)[None])[0]
    hi, lo = np.maximum(L, Lb), np.minimum(L, Lb)
    return ((hi + 0.05) / (lo + 0.05) < 2.5) & (a[..., 3] > 128)


def low_contrast_frac(a, bg=(17, 17, 17)):
    al = a[..., 3] > 128
    if al.sum() == 0:
        return 0.0
    def lum(c):
        c = c / 255.0
        c = np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
        return 0.2126 * c[..., 0] + 0.7152 * c[..., 1] + 0.0722 * c[..., 2]
    L = lum(a[..., :3][al])
    Lb = lum(np.array(bg, np.float32)[None])[0]
    hi, lo = np.maximum(L, Lb), np.minimum(L, Lb)
    return float(((hi + 0.05) / (lo + 0.05) < 2.5).mean())


bgmask_cache = {}


def fix_white_box(a):
    N = a.shape[0] * a.shape[1]
    rgb, al = a[..., :3], a[..., 3]
    mn, mx = rgb.min(-1), rgb.max(-1)
    cand = ((mn >= 228) & (mx - mn <= 28)) | (al < 8)
    bg, prot = gated_flood(cand, 3, N)
    bgmask_cache['bg'] = bg
    out = edge_ring_unmix(a, bg, ring_px=2)
    return out, {'cleared_frac': round(float(bg.mean()), 4), 'protected_enclosed_px': prot}


def neutral_light(a):
    rgb = a[..., :3]
    mn, mx = rgb.min(-1), rgb.max(-1)
    return (mn >= 112) & (mx - mn <= 16) & (a[..., 3] > 0)


def small_light_specks(a, N):
    """components of opaque pixels that are small and mostly neutral-light"""
    op = a[..., 3] > 16
    nl = neutral_light(a)
    lab, n = ndi.label(op, structure=FOUR)
    if n == 0:
        return np.zeros(op.shape, bool), 0
    idx = np.arange(1, n + 1)
    area = ndi.sum(np.ones_like(lab), lab, idx)
    nlc = ndi.sum(nl, lab, idx)
    lim = max(64, 0.0002 * N)
    bad = idx[((area < lim) & (nlc >= 0.5 * area)) | (area < 16)]
    return np.isin(lab, bad), len(bad)


def checker_energy(a):
    """Alternating-tile energy: fraction of the canvas covered by opaque,
    neutral-light pixels that sit in small/medium isolated components or in the
    edge-connected light region (i.e. look like baked checker tiles)."""
    N = a.shape[0] * a.shape[1]
    nl = neutral_light(a) & (a[..., 3] > 16)
    bgc = border_connected(nl | (a[..., 3] < 8)) & nl
    op = a[..., 3] > 16
    lab, n = ndi.label(op, structure=FOUR)
    iso = np.zeros(op.shape, bool)
    if n:
        idx = np.arange(1, n + 1)
        area = ndi.sum(np.ones_like(lab), lab, idx)
        nlc = ndi.sum(nl, lab, idx)
        bad = idx[(area < 0.002 * N) & (nlc >= 0.5 * area)]
        iso = np.isin(lab, bad)
    return float((bgc | iso).sum() / N)


def checker_tones(a):
    """detect the alternating light tones from the outer 5% frame"""
    H, W = a.shape[:2]
    b = max(4, int(0.05 * min(H, W)))
    frame = np.zeros((H, W), bool)
    frame[:b] = frame[-b:] = True
    frame[:, :b] = frame[:, -b:] = True
    nl = neutral_light(a) & frame
    v = a[..., :3].min(-1)[nl].astype(int)
    if v.size < 50:
        return []
    h = np.bincount(v, minlength=256).astype(float)
    hs = np.convolve(h, np.ones(5) / 5, mode='same')
    peaks = []
    for t in np.argsort(hs)[::-1]:
        if hs[t] < 0.04 * v.size / 5:
            break
        if all(abs(t - p) > 10 for p in peaks):
            peaks.append(int(t))
        if len(peaks) >= 4:
            break
    return sorted(peaks)


TONE_MODE = ('d118595bce',)  # visual check: broad mode ate interior whites/greys of this design


def fix_checker(a, tone_mode=False):
    N = a.shape[0] * a.shape[1]
    nl = neutral_light(a)
    tones = checker_tones(a)
    mnv = a[..., :3].min(-1)
    tone_m = np.zeros(nl.shape, bool)
    for t in tones:
        tone_m |= np.abs(mnv - t) <= 12
    cand = ((nl & tone_m) if tone_mode else nl) | (a[..., 3] < 8)
    bgm, prot = gated_flood(cand, 2, N)
    bg = bgm & (a[..., 3] >= 8)
    out = a.copy()
    out[..., 3][bg] = 0
    # enclosed checker patches: neutral-light components that are bimodal
    # (two light tones, each >=20%, together >=85% of the component)
    etones = []
    enc_cleared = 0
    anyt = nl & (out[..., 3] > 0)
    lab, n = ndi.label(ndi.binary_dilation(anyt, iterations=3), structure=np.ones((3, 3)))
    if n:
        objs = ndi.find_objects(lab)
        sel = np.zeros(anyt.shape, bool)
        for i, sl in enumerate(objs, start=1):
            comp = (lab[sl] == i) & anyt[sl]
            area = int(comp.sum())
            if area < 300:
                continue
            v = mnv[sl][comp].astype(int)
            h = np.convolve(np.bincount(v, minlength=256).astype(float), np.ones(5) / 5, mode='same')
            pk = []
            for t in np.argsort(h)[::-1]:
                if all(abs(t - q) > 22 for q in pk):
                    pk.append(int(t))
                if len(pk) == 2:
                    break
            if len(pk) < 2:
                continue
            sh = [float((np.abs(v - t) <= 8).mean()) for t in pk]
            if min(sh) >= 0.2 and sum(sh) >= 0.6:
                sel[sl] |= comp
                etones.append(sorted(pk))
        out[..., 3][sel] = 0
        enc_cleared = int(sel.sum())
        bg = bg | sel
    specks, nsp = small_light_specks(out, N)
    out[..., 3][specks] = 0
    cleared = bg | specks | (a[..., 3] < 8)
    out = edge_ring_unmix(out, cleared, ring_px=1, soft=80.0)
    return out, {'mode': 'tone' if tone_mode else 'broad', 'tones': tones, 'cleared_tile_px': int(bg.sum()), 'specks_removed': int(nsp), 'protected_enclosed_px': prot, 'enclosed_checker_tones': etones, 'enclosed_checker_px_cleared': enc_cleared}


def fix_low_contrast(a, r, color, only_dark_components=False):
    al = a[..., 3]
    m = al >= 128
    lab, n = ndi.label(m, structure=FOUR)
    if n:
        area = ndi.sum(np.ones_like(lab), lab, np.arange(1, n + 1))
        m = m & ~np.isin(lab, np.arange(1, n + 1)[area < 40])
        if only_dark_components:
            lc = low_contrast_mask(a) & m
            lcs = ndi.sum(lc, lab, np.arange(1, n + 1))
            keep = np.arange(1, n + 1)[(lcs >= 0.6 * area) & (area >= 40)]
            m = np.isin(lab, keep)
            if not m.any():
                return a, {'selective_components': 0}
    d = ndi.distance_transform_edt(~m)
    s_alpha = np.clip(r + 0.5 - d, 0, 1) * 255.0
    stroke = np.zeros_like(a)
    stroke[..., :3] = color
    stroke[..., 3] = s_alpha
    # composite original over stroke
    fa = al[..., None] / 255.0
    sa = s_alpha[..., None] / 255.0
    oa = fa + sa * (1 - fa)
    rgb = (a[..., :3] * fa + stroke[..., :3] * sa * (1 - fa)) / np.maximum(oa, 1e-6)
    out = np.dstack([rgb, oa[..., 0] * 255.0])
    ex = {'stroke_px_src': r, 'stroke_rgb': list(color)}
    if only_dark_components:
        ex['selective_components'] = int(len(keep))
    return out, ex


WB_STROKE_T = 0.30


def stroke_r(prods, W):
    # stroke radius: 10 px at print resolution, from placement scale
    rs = []
    for p in prods:
        pl = json.load(open(os.path.join(os.path.dirname(p['source_file']), 'placement.json')))
        sc = (pl.get('proposed') or pl.get('current') or {}).get('scale', 1.0) or 1.0
        phw = max(v[0] for v in pl['placeholders'].values()) if pl.get('placeholders') else W
        rs.append(10.0 * W / (phw * sc))
    return round(float(np.clip(max(rs), 3, 12)), 2)


def stats(a):
    al = a[..., 3]
    H, W = al.shape
    b = max(2, int(0.01 * min(H, W)))
    border = np.concatenate([al[:b].ravel(), al[-b:].ravel(), al[:, :b].ravel(), al[:, -b:].ravel()])
    return {'opaque_frac': round(float((al > 128).mean()), 4),
            'transparent_frac': round(float((al < 8).mean()), 4),
            'border_opaque_frac': round(float((border > 128).mean()), 4)}


def composite(a, color, size):
    im = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8), 'RGBA')
    im.thumbnail((size, size), Image.LANCZOS)
    bg = Image.new('RGBA', (size, size), color + (255,))
    bg.alpha_composite(im, ((size - im.width) // 2, (size - im.height) // 2))
    return bg.convert('RGB')


def main():
    rows = list(csv.DictReader(open(OUT + '/inventory.csv')))
    local = [r for r in rows if r['fix_route'] == 'LOCAL']
    by_sha = {}
    for r in local:
        by_sha.setdefault(r['sha1'], []).append(r)
    only = set(sys.argv[1:])
    mp = OUT + '/metrics.json'
    metrics = json.load(open(mp)) if (only and os.path.exists(mp)) else {}
    font = ImageFont.load_default()
    for sha, prods in by_sha.items():
        cat = prods[0]['category']
        if only and cat not in only:
            continue
        a = load(prods[0]['source_file'])
        H, W = a.shape[:2]
        info = {'category': cat, 'src_px': f'{W}x{H}', 'products': [p['product_id'] for p in prods]}
        before = stats(a)
        if cat == 'white_box':
            out, extra = fix_white_box(a)
            lcf = low_contrast_frac(out)
            extra['lowcontrast_vs_black_after_bg'] = round(lcf, 3)
            # trigger: dark components that vanish on the black blank after bg removal
            _, probe = fix_low_contrast(out, 1, (250, 248, 240), only_dark_components=True)
            extra['dark_components'] = probe.get('selective_components', 0)
            lcm = low_contrast_mask(out)
            opq = out[..., 3] > 128
            lab, n = ndi.label(opq, structure=FOUR)
            dark_area = 0
            if n:
                idx = np.arange(1, n + 1)
                area = ndi.sum(np.ones_like(lab), lab, idx)
                lcs = ndi.sum(lcm, lab, idx)
                dark_area = float(area[(lcs >= 0.6 * area) & (area >= 40)].sum() / max(opq.sum(), 1))
            extra['dark_component_area_frac'] = round(dark_area, 4)
            if dark_area >= 0.005:
                out, ex2 = fix_low_contrast(out, stroke_r(prods, W), (250, 248, 240))
                extra.update(ex2)
                extra['chained_light_stroke'] = True
            # enclosed flat whites left in place (letter counters etc.)
            rgbo = a[..., :3]
            flat_w = (rgbo.min(-1) >= 240) & ~bgmask_cache['bg']
            labw, nw = ndi.label(flat_w, structure=FOUR)
            if nw:
                aw = ndi.sum(np.ones_like(labw), labw, np.arange(1, nw + 1))
                extra['enclosed_white_regions'] = int((aw >= 0.0002 * W * H).sum())
                extra['enclosed_white_px'] = int(aw[aw >= 0.0002 * W * H].sum())
            c1, c2 = (17, 17, 17), (249, 249, 249)
            n1, n2 = 'black', 'white'
        elif cat == 'checkerboard':
            out, extra = fix_checker(a, tone_mode=sha.startswith(TONE_MODE))
            info['checker_energy_before'] = round(checker_energy(a), 5)
            info['checker_energy_after'] = round(checker_energy(out), 5)
            c1, c2 = (17, 17, 17), (249, 249, 249)
            n1, n2 = 'black', 'white'
        else:
            notes = ' '.join(p['notes'] for p in prods)
            light_blank = ('LIGHT blank' in notes) or ('LIGHT ink' in notes) or ('CLEAR glass' in notes) or ('clear glass' in notes.lower())
            r = stroke_r(prods, W)
            color = (24, 24, 24) if light_blank else (250, 248, 240)
            out, extra = fix_low_contrast(a, r, color)
            if light_blank:
                c1, c2, n1, n2 = (249, 249, 249), (17, 17, 17), 'white (problem blank)', 'black'
            else:
                c1, c2, n1, n2 = (17, 17, 17), (249, 249, 249), 'black (problem blank)', 'white'
            info['stroke'] = 'dark' if light_blank else 'light'
        after = stats(out)
        info.update(extra)
        info['lowcontrast_vs_black_final'] = round(low_contrast_frac(out), 3)
        info['before'] = before
        info['after'] = after
        outp = f'{FIX}/{sha}.png'
        Image.fromarray(np.clip(out + 0.5, 0, 255).astype(np.uint8), 'RGBA').save(outp, optimize=False)
        info['output_file'] = outp
        # previews per product
        S = 420
        p1 = composite(a, c1, S)
        p2 = composite(out, c1, S)
        p3 = composite(out, c2, S)
        for p in prods:
            sheet = Image.new('RGB', (3 * S + 40, S + 46), (255, 255, 255))
            d = ImageDraw.Draw(sheet)
            d.text((8, 4), f"{p['product_id']}  bp{p['blueprint']}  {cat}  sha1 {sha[:10]}  {p['src_px']}", fill=(0, 0, 0), font=font)
            d.text((8, 22), f"ORIGINAL on {n1}", fill=(160, 0, 0), font=font)
            d.text((S + 28, 22), f"FIXED on {n1}", fill=(0, 110, 0), font=font)
            d.text((2 * S + 48, 22), f"FIXED on {n2}", fill=(0, 110, 0), font=font)
            sheet.paste(p1, (8, 40)); sheet.paste(p2, (S + 28, 40)); sheet.paste(p3, (2 * S + 48, 40))
            sheet.save(f"{PRV}/{p['product_id']}.png")
        metrics[sha] = info
        print(sha[:10], cat, info.get('before'), info.get('after'), {k: v for k, v in info.items() if k.startswith(('checker', 'cleared', 'specks', 'stroke'))}, flush=True)
    json.dump(metrics, open(OUT + '/metrics.json', 'w'), indent=1)


if __name__ == '__main__':
    main()
