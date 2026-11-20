"""Assemble outputs: text_fix/<sha1>.png, previews/<product_id>.png, contact sheets, results.csv."""
import sys; sys.path.insert(0, "/home/user/crowned-co-data/work/d6_new_art/text_fix/scripts")
from common import *
import csv, shutil

PRV = TF + '/previews'; os.makedirs(PRV, exist_ok=True)
def full(pre): return src(pre)[0]

ELF = 'MY ELF / MADE ME DO IT (line-1 duplicate MADE removed; MY ELF re-centred on its arc)'
PAT = 'Meter now reads P-A-T-I-E-N-C-E (original glyphs re-spaced; headline unchanged)'
REC = "Receipt: ITEM=ALL THE GIFTS / QUANTITY=UNLIMITED / TOTAL=PRICELESS; red total 'PAID IN COOKIES'"
fixed = {}   # sha -> (array, category, wording, note)
elf = load_rgba(WK + '/elf_fixed.png')
for pre in ['d7531299c7', '111997c641', 'f9fe64d6e0']:
    fixed[full(pre)] = (elf, 'garbled_text', ELF, 'transparent output (exterior white removed, letter fills/plate kept white); OCR fill-mask: "MY ELF / MADE ME Do jy" (stylised IT); same art as f9fe64d6e0 cut')
fixed[full('89941b397d')] = (elf[30:30 + 1312, 268:268 + 1515], 'garbled_text', ELF, 'exact crop (268,30) of the 2048x1365 master, verified RGB diff 0')
pat = load_rgba(WK + '/patience_fixed_rgb.png')
for pre in ['f193d6d08b', '7d9d687044']:
    fixed[full(pre)] = (pat, 'garbled_text', PAT, 'opaque like source (white-substrate products); OCR of meter column: "PATIENCE"')
fixed[full('6ef24aa6af')] = (load_rgba(WK + '/jolly_fixed.png'), 'garbled_text', 'JOLLY, TIRED, AND CAFFEINATED (", AND" deleted)',
                             'line 3 is now cup + AND (AND already on the centre axis) leaving open space at right of line 3; tesseract cannot read this ornate face - visual check only')
cm = json.load(open(WK + '/candy_meta.json'))
c5d = load_rgba(WK + '/candy_5d22f4d4a7.png')
fixed[full('5d22f4d4a7')] = (c5d, 'blank_text', 'Street-sign plaque: CANDY CANE LANE', 'Bebas Neue Bold cream + dark-green drop shadow, cap 38px')
fixed[full('5fa6bcd6cd')] = (c5d, 'blank_text', 'Street-sign plaque: CANDY CANE LANE', 'built on the pixel-identical transparent cut 5d22f4d4a7 so dtf backpack (black) gets no white box; cap 38px')
fixed[full('1170ae6c3a')] = (load_rgba(WK + '/candy_1170ae6c3a.png'), 'blank_text', 'Street-sign plaque: CANDY CANE LANE', 'same text layer, crop offset (-196,-38)')
fixed[full('3b2c254f1d')] = (load_rgba(WK + '/candy_3b2c254f1d.png'), 'blank_text', 'Hanging sign: WELCOME / EST. NORTH POLE', 'headline already reads CANDY CANE LANE, so the hanging sign got a welcome line instead of a repeat; Bebas Neue Bold')
bm = json.load(open(WK + '/banner_meta.json'))
for pre in ['9253995681', 'd499f625bb']:
    fixed[full(pre)] = (load_rgba(WK + f'/banner_{pre}.png'), 'blank_text', 'Ribbon: BRINGING HOME THE TREE', 'Roboto Slab Bold cream, dark-red shadow, flag-warped to ribbon centreline; cap 37.5px')
fixed[full('d5007b7352')] = (load_rgba(WK + '/banner_d5007b7352.png'), 'blank_text', 'Ribbon: POUR ANOTHER', 'Montserrat Black red + gold stroke (matches HO HO HO headline), flag-warped; cap 47px')
fixed[full('2ddd385282')] = (load_rgba(WK + '/receipt_fixed.png'), 'blank_text', REC, 'Montserrat Bold/ExtraBold (receipt face), placeholders inpainted; OCR: ITEM ALL THE GIFTS / QUANTITY UNLIMITED / TOTAL PRICELESS / PAID IN COOKIES')
lm = json.load(open(WK + '/lowres_meta.json'))
LRW = {'d402b87a81': PAT, 'c0a403dd61': REC}
for sha, m in lm.items():
    pre = sha[:10]
    cat = SRC[sha][0]
    fixed[sha] = (load_rgba(WK + f'/lowres_{pre}.png'), cat, LRW.get(pre, '(unchanged design)'),
                  f"400px thumbnail replaced by full-res master of the same design ({os.path.relpath(m['master'], '/home/user/crowned-co-data/work')}), framing matched (scale {m['scale_master_to_thumb']}), thumbnail-guided bg cleanup; downscale diff vs live thumb {m['thumb_diff_mean']}/255, alpha IoU {m['alpha_iou']}")

NEED = {
    'engraving': 'automatic 1-colour conversion tried (Otsu+edge, 0.5 mm min line) - result muddy/blobby, small text illegible; needs hand-made vector line art (evidence work/eng_try.png, eng_try2.png)',
    'other': None,
}
need_note = {
    full('d8da95fe58'): 'banner covered by skeleton limbs in the source composition - needs redraw',
    full('b7ad86de04'): 'title text absent from the file and intended title wording unknown - needs re-export with title',
    full('33bfc50a57'): 'Jingle ribbon: tried "TO THE LIQUOR STORE" after removing the centre holly - cap only 25px (~1.6-1.8 mm printed on mousepad/bottle), collides with the dotted border; not professional - regenerate with a larger blank banner (evidence work/jb_v.png)',
    full('2989efb65a'): 'same Jingle art as 33bfc50a57 - see that row',
    full('876f6be331'): 'same Jingle art as 33bfc50a57 (crop) - see that row',
}

# blank colours (from mockup_before.jpg review); default white substrate
BLANK = {'6ac7020567e0e81ed20ffda7': (20, 20, 20), '6ac7117d3925bc76b9037258': (20, 20, 20), '6ac71811d0a23214d80b2aec': (25, 25, 25),
         '6ac717f3aa7a21cb900b506c': (25, 25, 25), '6ac7118407e4149a0f001011': (170, 226, 212), '6ac6ff9c2a2224fe7d0775a1': (248, 248, 248)}
EXTRA_DARK = {'6ac6ff9c2a2224fe7d0775a1'}   # dark colours also enabled

def dpi(r, w):
    ph = r['ph'] or {}; sc = (r['prop'] or r['cur'] or {}).get('scale', 1.0)
    best = None
    for vid, (pw, phh) in ph.items():
        d = 300.0 * w / (sc * pw)
        if best is None or d < best[0]: best = (d, vid, pw)
    return best

font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 13)
rows = []; sheet_items = []
# nominal dpi = 300 * src_px / (scale * placeholder_px): Printify placeholder px treated as 300 dpi (same basis as the batch 'src px/print px' ratio)
written = set()
for r in TABLE:
    if r['route'] != 'GENERATE':
        continue
    sha = r['sha1']; pid = r['pid']
    orig = load_rgba(SRC[sha][1])
    if sha in fixed:
        arr, cat, wording, note = fixed[sha]
        outp = f'{TF}/{sha}.png'
        if sha not in written:
            save_rgba(arr, outp); written.add(sha)
        d = dpi(r, arr.shape[1]); d0 = dpi(r, orig.shape[1])
        status = 'FIXED_LOCAL'
        if d and d[0] < 150:
            note += f' | LOW-RES on largest variant {d[1]}: src/print px ratio {d[0]/300:.2f} (<0.5; source-resolution limit, not changed by this text fix)'
        rows.append(dict(product_id=pid, sha1=sha, category=r['cat'], fix_status=status, wording_used=wording,
                         dpi_largest_variant=f'{d[0]:.0f} nominal (variant {d[1]}, scale {(r["prop"] or r["cur"])["scale"]}, src/print px {d[0]/300:.2f}; before {d0[0]:.0f})' if d else '',
                         notes=note))
        # preview
        col = BLANK.get(pid, (248, 248, 248))
        S = 520
        aft = on_bg(arr, col, maxside=S)
        bef = on_bg(orig, col); bef = bef.resize((aft.width, aft.height) if abs(bef.width / bef.height - aft.width / aft.height) < 0.02 else (S, int(S * bef.height / bef.width)), Image.LANCZOS)
        panels = [('BEFORE', bef), ('AFTER', aft)]
        if pid in EXTRA_DARK:
            panels.append(('AFTER on black', on_bg(arr, (20, 20, 20), maxside=S)))
        sheet = Image.new('RGB', (len(panels) * (S + 20) + 20, S + 70), (255, 255, 255))
        dr = ImageDraw.Draw(sheet)
        dr.text((10, 6), f'{pid}  bp{r["bp"]}  {r["dec"]}  {r["cat"]}  sha1 {sha[:10]}  blank rgb{col}', fill=(0, 0, 0), font=font)
        dr.text((10, 24), wording[:150], fill=(0, 90, 0), font=font)
        for i, (lab, im) in enumerate(panels):
            x = 20 + i * (S + 20)
            dr.text((x, 46), lab, fill=(160, 0, 0) if lab == 'BEFORE' else (0, 110, 0), font=font)
            sheet.paste(im, (x + (S - im.width) // 2, 64 + (S - im.height) // 2))
        sheet.save(f'{PRV}/{pid}.png')
        sheet_items.append(f'{PRV}/{pid}.png')
    else:
        reason = need_note.get(sha) or NEED.get(r['cat']) or 'not attempted'
        d0 = dpi(r, orig.shape[1])
        rows.append(dict(product_id=pid, sha1=sha, category=r['cat'], fix_status='NEEDS_GENERATION', wording_used='',
                         dpi_largest_variant=f'{d0[0]:.0f} nominal (current art, src/print px {d0[0]/300:.2f})' if d0 else '', notes=reason))

with open(TF + '/results.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['product_id', 'sha1', 'category', 'fix_status', 'wording_used', 'dpi_largest_variant', 'notes'])
    w.writeheader(); w.writerows(rows)
# contact sheets (12 per sheet)
for k in range(0, len(sheet_items), 12):
    ims = [Image.open(p) for p in sheet_items[k:k + 12]]
    tw = 760
    th = [int(im.height * tw / im.width) for im in ims]
    cols = 3; rws = (len(ims) + cols - 1) // cols
    rh = max(th)
    cs = Image.new('RGB', (cols * (tw + 10) + 10, rws * (rh + 10) + 10), (200, 200, 200))
    for i, im in enumerate(ims):
        cs.paste(im.resize((tw, th[i]), Image.LANCZOS), (10 + (i % cols) * (tw + 10), 10 + (i // cols) * (rh + 10)))
    cs.save(f'{TF}/contact_sheet_{k // 12 + 1}.png')
from collections import Counter
print(Counter((r['category'], r['fix_status']) for r in rows), len(rows), 'files', len(written))
