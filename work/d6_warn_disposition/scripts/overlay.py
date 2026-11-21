"""Render a geometry overlay: safe shape (green), placeholder (grey), art, content outside the safe shape (red).
Usage: python3 -I overlay.py <pid> <batch> <vid> <out.png> [x y scale] [art_path]"""
import sys, json, numpy as np
sys.path.insert(0, '/home/user/crowned-co-data/work/d6_warn_disposition/scripts')
import shape_check as S
from PIL import Image, ImageDraw
def render(pid, batch, vid, pr=None, art=None, size=700, title=''):
    W = S.W; d = f'{W}/d6_batch{batch}/{pid}'; j = json.load(open(d + '/placement.json'))
    prods = {json.loads(l)['product_id']: json.loads(l) for l in open(f'{W}/d6_batch{batch}/products.jsonl')}
    p = prods[pid]; PW, PH = j['placeholders'][vid]
    pr = pr or (j.get('proposed_per_variant_group') or {}).get(vid, j['proposed'])
    if str(batch) == '1':
        views = json.load(open(f'{W}/d6_batch1/_svg/views.json')); sid = S.B1_SVG.get(int(vid)) or (views.get(str(j['blueprint_id'])) or [None])[0]
    else: sid = (p.get('svgs') or {}).get(vid) or p.get('svg')
    sh = S.shape(f'{W}/d6_batch{batch}/_svg/{sid}.svg')
    k = size / max(PW, PH); cw, ch = round(PW * k), round(PH * k)
    cv = Image.new('RGB', (cw + 40, ch + 70), (110, 110, 115)); dr = ImageDraw.Draw(cv)
    dr.rectangle([20, 20, 20 + cw, 20 + ch], fill=(250, 250, 250))
    im = Image.open(art or d + '/original.png').convert('RGBA'); iw, ih = im.size
    aw = pr['scale'] * PW * k; ah = aw * ih / iw; ox = 20 + pr['x'] * PW * k - aw / 2; oy = 20 + pr['y'] * PH * k - ah / 2
    a = im.resize((max(1, round(aw)), max(1, round(ah))), Image.LANCZOS); cv.paste(a, (round(ox), round(oy)), a)
    msk = S.raster(sh['polys'], cw, ch) if sh and sh['polys'] else np.ones((ch, cw), bool)
    cm = np.array(Image.fromarray(S.content_mask(im).astype(np.uint8) * 255).resize(a.size, Image.NEAREST)) > 0
    arr = np.array(cv); H_, W_ = cm.shape
    for yy in range(H_):
        Y = round(oy) + yy - 20
        if not (0 <= Y < ch): 
            xs = np.nonzero(cm[yy])[0]; X = round(ox) + xs; ok = (X >= 0) & (X < cv.width) & (round(oy) + yy >= 0) & (round(oy) + yy < cv.height)
            arr[round(oy) + yy, X[ok]] = (230, 0, 0) if ok.any() else arr[0, 0]; continue
        xs = np.nonzero(cm[yy])[0]; X = round(ox) + xs - 20
        out = (X < 0) | (X >= cw); inn = ~out
        bad = np.zeros(len(xs), bool); bad[inn] = ~msk[Y, X[inn]]; bad |= out
        Xc = X[bad] + 20; ok = (Xc >= 0) & (Xc < cv.width); arr[Y + 20, Xc[ok]] = (230, 0, 0)
    cv = Image.fromarray(arr); dr = ImageDraw.Draw(cv)
    for q in (sh or {}).get('polys', []): dr.line([(20 + u * cw, 20 + v * ch) for u, v in q] + [(20 + q[0][0] * cw, 20 + q[0][1] * ch)], fill=(0, 160, 60), width=2)
    dr.rectangle([20, 20, 20 + cw, 20 + ch], outline=(60, 60, 60))
    dr.text((6, ch + 28), f'{pid} v{vid} x={pr["x"]:.4f} y={pr["y"]:.4f} s={pr["scale"]:.3f}', fill='white')
    dr.text((6, ch + 46), title[:90], fill='white')
    return cv
if __name__ == '__main__':
    a = sys.argv; pr = dict(x=float(a[5]), y=float(a[6]), scale=float(a[7]), angle=0) if len(a) > 7 else None
    render(a[1], a[2], a[3], pr, a[8] if len(a) > 8 else None).save(a[4])
