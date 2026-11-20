"""Re-run the independent QA checks (same rules as winstar-recovery/qa/qa_placements.py: rect geometry vs every
enabled placeholder, src/print px ratio, opaque-background check, mapping) plus the raw-SVG shape check
(shape_check.py) on the corrected art/placement of FIXED rows. Writes placements/<pid>.json and qa_after.csv.
Usage: python3 -I qa_after.py"""
import csv, json, os, sys, copy, hashlib
import numpy as np
from PIL import Image
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shape_check as S
Image.MAX_IMAGE_PIXELS = None
OUT = '/home/user/crowned-co-data/work/d6_warn_disposition'
A = OUT + '/art/'
FIX = {  # pid: (batch, new art, fix description)
 '6ac71229b8146913210037a6': (1, A + 'avoiding-carolers-gnome_x4.png', 'upscale'),
 '6ac7110e07e4149a0f000fcd': (1, A + 'avoiding-carolers-gnome_x4.png', 'upscale'),
 '6ac7111557527ce5fd0196c3': (1, A + 'avoiding-carolers-raccoon_x4.png', 'upscale'),
 '6ac710117be9df884b032c6c': (2, A + 'openbar_fixed_x4.png', 'upscale'),
 '6ac7114a35a66ab7dc0b0f63': (2, A + 'openbar_fixed_x4.png', 'upscale'),
 '6ac711516f976358160c470e': (2, A + 'christmas-stress-tinsel-done_x4.png', 'upscale'),
 '6ac71176ed135347800f9ae0': (3, A + 'elegantly-wasted-martini_x4.png', 'upscale'),
 '6ac710ff7be9df884b032d2f': (4, A + 'naughty-list-skeleton-v2_x4.png', 'upscale'),
 '6ac711f1b32a96bbe40d0ca2': (4, A + 'prosecco-ho-ho-ho_x4.png', 'upscale'),
 '6ac7164faa7a21cb900b4f01': (4, A + 'prosecco-ho-ho-ho_x4.png', 'upscale'),
 '6ac7126c57527ce5fd01976a': (10, A + 'naughty-list-skeleton_x4.png', 'upscale'),
 '6ac8f919149425f38d04bedd': (2, A + '6ac8f919149425f38d04bedd_despeck.png', 'despeck'),
}
def bbox(im):  # identical rule to qa_placements.py
    a = np.array(im.convert('RGBA'))
    if a[..., 3].min() < 250: m = a[..., 3] > 16; mode = 'alpha'
    else:
        c = a[0, 0, :3].astype(int); m = np.abs(a[..., :3].astype(int) - c).sum(2) > 40; mode = 'opaque_bg'
    ys, xs = np.where(m); h, w = m.shape
    return (xs.min() / w, ys.min() / h, (xs.max() + 1) / w, (ys.max() + 1) / h), mode
def qa(pid, batch, art):
    d = f'{S.W}/d6_batch{batch}/{pid}'; j = json.load(open(d + '/placement.json'))
    im = Image.open(art); iw, ih = im.size; (bx0, by0, bx1, by1), mode = bbox(im)
    issues = []; worst = 1.0; ratio = 9
    for vid, (W_, H_) in j['placeholders'].items():
        pr = (j.get('proposed_per_variant_group') or {}).get(vid, j['proposed'])
        aw = pr['scale'] * W_; ah = aw * ih / iw; cx = pr['x'] * W_; cy = pr['y'] * H_
        x0 = cx - aw / 2 + bx0 * aw; x1 = cx - aw / 2 + bx1 * aw; y0 = cy - ah / 2 + by0 * ah; y1 = cy - ah / 2 + by1 * ah
        ix = max(0, min(x1, W_) - max(x0, 0)); iy = max(0, min(y1, H_) - max(y0, 0))
        worst = min(worst, ix * iy / ((x1 - x0) * (y1 - y0))); ratio = min(ratio, iw / aw)
    if worst < 0.999: issues.append(f'GEOMETRY: only {worst:.1%} inside placeholder')
    if ratio < 0.33: issues.append(f'RESOLUTION: ratio {ratio:.2f}')
    elif ratio < 0.5: issues.append(f'RESOLUTION-WARN: ratio {ratio:.2f}')
    if mode == 'opaque_bg': issues.append('TRANSPARENCY-WARN: opaque background')
    o = Image.open(d + '/original.png')
    if abs(iw / ih - o.size[0] / o.size[1]) > 1e-3: issues.append('ASPECT changed vs original')
    sc = S.check(pid, batch, art=art)
    if sc['inside_min'] < 0.9995: issues.append(f'SHAPE: {sc["inside_min"]:.4%} inside raw SVG safe shape')
    elif sc['overflow_cells_max'] > 4: issues.append(f'SHAPE: max overflow {sc["overflow_cells_max"]:.1f} raster cells')
    hard = [x for x in issues if not x.split(':')[0].endswith('WARN')]
    st = 'FAIL' if hard else ('WARN' if issues else 'PASS')
    return dict(product_id=pid, content_inside_min=f'{worst:.4f}', src_print_px_ratio_min=f'{ratio:.2f}', bg_mode=mode,
                shape_inside_min=f'{sc["inside_min"]:.5f}', shape_overflow_cells=f'{sc["overflow_cells_max"]:.2f}',
                qa_status=st, issues=' | '.join(issues)), j, (iw, ih)
if __name__ == '__main__':
    os.makedirs(OUT + '/placements', exist_ok=True); rows = []
    for pid, (b, art, kind) in FIX.items():
        r, j, px = qa(pid, b, art); rows.append(r); print(r)
        n = copy.deepcopy(j)
        n['warn_fix'] = dict(kind=kind, source_original=f'work/d6_batch{b}/{pid}/original.png',
            new_art_local=os.path.relpath(art, '/home/user/crowned-co-data'), new_art_sha256=hashlib.sha256(open(art, 'rb').read()).hexdigest(),
            new_art_px=list(px), old_image_px=j['image_px'], placement_changed=False,
            note=('Real-ESRGAN anime6B x4 local upscale (edge-bleed RGB, Lanczos alpha); upscale adds no true detail: native-pixel '
                  'resolution unchanged' if kind == 'upscale' else 'removed %s detached grey bg-removal specks ~50px outside the figure' % 180),
            requires='upload new art as a NEW Printify image + owner-approved product update (not done; local only)',
            qa_after=r['qa_status'])
        n['image_px'] = list(px); n['image_name_proposed'] = os.path.basename(art); n['live_change_made'] = False
        json.dump(n, open(f'{OUT}/placements/{pid}.json', 'w'), indent=1)
    with open(OUT + '/qa_after.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, list(rows[0])); w.writeheader(); w.writerows(rows)
