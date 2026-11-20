"""Before/after images (<=1600px wide) for FIXED rows + contact sheets. Usage: python3 -I before_after.py"""
import os, sys, json, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw, ImageFont
from scipy import ndimage
import overlay as O, qa_after as Q, csv
Image.MAX_IMAGE_PIXELS = None
OUT = Q.OUT; os.makedirs(OUT + '/before_after', exist_ok=True)
F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 15); FB = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 17)
qa = {r['product_id']: r for r in csv.DictReader(open(OUT + '/qa_after.csv'))}
qa0 = {r['product_id']: r for r in csv.DictReader(open('/home/user/winstar4u/my-projects/winstar-recovery/qa/placement_qa_224.csv'))}
def on(im, c=(255, 255, 255)):
    b = Image.new('RGBA', im.size, c + (255,)); b.alpha_composite(im.convert('RGBA')); return b.convert('RGB')
def fit(im, w, h):
    im = im.copy(); im.thumbnail((w, h), Image.LANCZOS); c = Image.new('RGB', (w, h), (110, 110, 115)); c.paste(im, ((w - im.width) // 2, (h - im.height) // 2)); return c
def zoom_box(orig):  # densest-edge window, 22% of width, in normalized coords
    a = np.asarray(orig.convert('RGBA')).astype(float); g = np.asarray(on(orig).convert('L')).astype(float)
    e = np.hypot(ndimage.sobel(g, 0), ndimage.sobel(g, 1)) * (a[..., 3] > 16)
    s = max(8, int(orig.width * 0.22)); ii = ndimage.uniform_filter(e, s)
    y, x = np.unravel_index(ii.argmax(), ii.shape)
    return (max(0, x - s // 2) / orig.width, max(0, y - s // 2) / orig.height, s / orig.width, s / orig.height)
for pid, (b, art, kind) in Q.FIX.items():
    d = f'{Q.S.W}/d6_batch{b}/{pid}'; j = json.load(open(d + '/placement.json'))
    vid = max(j['placeholders'], key=lambda v: j['placeholders'][v][0] * j['placeholders'][v][1])  # largest = worst dpi
    PW, PH = j['placeholders'][vid]; pr = (j.get('proposed_per_variant_group') or {}).get(vid, j['proposed'])
    orig = Image.open(d + '/original.png'); new = Image.open(art)
    W = 1600; cv = Image.new('RGB', (W, 700), (45, 45, 50)); dr = ImageDraw.Draw(cv)
    title = f'{pid}  shop {j["shop_id"]}  batch {b}  bp {j["blueprint_id"]}  v{vid} {PW}x{PH}  ' + j['title'][:70]
    dr.text((12, 8), title, font=FB, fill='white')
    if kind == 'upscale':
        ren = O.render(pid, b, vid, pr, art, size=470)
        cv.paste(fit(ren, 500, 600), (10, 40))
        bx = zoom_box(orig); aw = pr['scale'] * PW; tw = int(round(bx[2] * aw)); th = int(round(bx[3] * aw * orig.height / orig.width))
        def crop(im):
            c = im.crop((round(bx[0] * im.width), round(bx[1] * im.height), round((bx[0] + bx[2]) * im.width), round((bx[1] + bx[3]) * im.height)))
            c = on(c).resize((tw, th), Image.LANCZOS)   # resampled to PRINT pixels, as the printer does
            return c.resize((520, round(520 * th / tw)), Image.NEAREST)
        cb, ca = crop(orig), crop(new)
        cv.paste(cb, (530, 70)); cv.paste(ca, (1070, 70))
        r0 = qa0[pid]['src_print_px_ratio_min']; r1 = qa[pid]['src_print_px_ratio_min']
        dr.text((530, 44), f'BEFORE  original {orig.width}x{orig.height}  src/print {r0}  (zoom, print px)', font=F, fill=(255, 150, 150))
        dr.text((1070, 44), f'AFTER  x4 upscale {new.width}x{new.height}  src/print {r1}', font=F, fill=(150, 255, 150))
        dr.text((530, 600), f'QA before: {qa0[pid]["qa_status"]} {qa0[pid]["issues"][:60]}', font=F, fill='white')
        dr.text((530, 622), f'QA after: {qa[pid]["qa_status"]}  inside {qa[pid]["content_inside_min"]}  raw-SVG shape {qa[pid]["shape_inside_min"]}  placement unchanged', font=F, fill='white')
        dr.text((530, 644), 'Local Real-ESRGAN x4 (no new detail; edges/text re-drawn crisp). Not uploaded, not live.', font=F, fill=(220, 220, 160))
    else:
        rb = O.render(pid, b, vid, pr, None, size=520); ra = O.render(pid, b, vid, pr, art, size=520)
        cv.paste(fit(rb, 560, 610), (10, 40)); cv.paste(fit(ra, 560, 610), (580, 40))
        dr.text((20, 652), 'BEFORE: original art (red = any content outside raw SVG safe shape)', font=F, fill=(255, 150, 150))
        dr.text((590, 652), f'AFTER: specks removed, QA {qa[pid]["qa_status"]}, shape {qa[pid]["shape_inside_min"]}', font=F, fill=(150, 255, 150))
        ao = np.asarray(orig.convert('RGBA'))[..., 3]; an = np.asarray(new.convert('RGBA'))[..., 3]
        rem = (ao > 16) & (an == 0); nrem = ndimage.label(rem, np.ones((3, 3)))[1]
        def spk(im, m):  # removed specks dilated 8px, red, on grey
            c = np.array(on(im, (200, 200, 200))); c[ndimage.binary_dilation(m, iterations=8)] = (230, 0, 0) if m.any() else 0; return Image.fromarray(c)
        left = (an > 16) & ndimage.binary_dilation(rem, iterations=2)
        sb, sa = spk(orig, rem), spk(new, left); nb_, na_ = nrem, int(left.sum())
        sb.thumbnail((440, 290)); sa.thumbnail((440, 290))
        cv.paste(sb, (1150, 64)); cv.paste(sa, (1150, 380))
        dr.text((1150, 42), f'before: {nb_} grey specks to remove (red, enlarged 8px)', font=F, fill='white')
        dr.text((1150, 358), f'after: {na_} speck px remain (design untouched)', font=F, fill='white')
    cv.save(f'{OUT}/before_after/{pid}.png', optimize=True)
    print(pid, 'ok')
# contact sheets: 2 columns x 3 rows, each tile 790x346
pids = list(Q.FIX)
for n in range(0, len(pids), 6):
    sh = Image.new('RGB', (1600, 1080), (30, 30, 34))
    for i, pid in enumerate(pids[n:n + 6]):
        t = Image.open(f'{OUT}/before_after/{pid}.png'); t.thumbnail((790, 346), Image.LANCZOS)
        sh.paste(t, (5 + (i % 2) * 798, 5 + (i // 2) * 358))
    sh.save(f'{OUT}/contact_sheet_{n // 6 + 1}.png', optimize=True); print('sheet', n // 6 + 1)
