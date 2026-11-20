"""Task C: per-product wording before/after previews for the 49-product wording packet
(winstar-recovery/wording/WORDING_APPROVAL_PACKET.md). LOCAL ONLY. Left = current live print file with its current
placement; right = proposed corrected art with that product's (staged) placement. W2 also gets the WELCOME alternative.
Art/placement source per product, in priority order:
  1. d6_final_rework/placements/<pid>.json (this session: SR upscales, Jingle/wreath/engraving fits)
  2. d6_qa_fixes/placements/<pid>.json (prior QA-fix staging: upscales, smaller motif, hole-filled)
  3. d6_new_art/text_fix/<sha1>.png with the batch 'proposed' placement (same aspect) or a content-box fit.
Run: python3 -I build_c.py"""
import csv, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from frlib import *

G = {  # group: (pids, before, after)
 'W1': (['6ac7125707e4149a0f001074'], 'Hanging sign: (blank, no text)', 'Hanging sign: WELCOME / EST. NORTH POLE'),
 'W2': ('6ac7134483f1a0e50d071df7 6ac713cd2d1baaa3fd0058b2 6ac711a0b8d5d3e719013155 6ac71159ed135347800f9acc 6ac710f0fa3cae10170efa36 6ac712fa42c818a1ad095f97 6ac713e2b814691321003889 6ac712f80ed8f1657605f2f1 6ac71340b814691321003853 6ac714e26f976358160c4915 6ac71811d0a23214d80b2aec 6ac7127aa5ade89b5c080fc0'.split(),
        'Street-sign plaque: (blank, no text)', 'Street-sign plaque: CANDY CANE LANE'),
 'W3': (['6ac714eba5ade89b5c0810e2'], 'Bottom ribbon: (blank, no text)', 'Bottom ribbon: POUR ANOTHER'),
 'W4': ('6ac7147e83f1a0e50d071e7a 6ac713e2c077332834034e13 6ac711ff6f976358160c4763 6ac7115a6356cae0df02e2e9 6ac713d7ed135347800f9c25 6ac71559c077332834034f19'.split(),
        'Receipt: ITEM - PRICE / QUANTITY - PRICE / TOTAL - PRICE, red total $99,999.99',
        'Receipt: ITEM - ALL THE GIFTS / QUANTITY - UNLIMITED / TOTAL - PRICELESS, red total PAID IN COOKIES'),
 'W5': ('6ac711d86f976358160c4749 6ac711357be9df884b032d51 6ac7151a7be9df884b032edd'.split(), 'Bottom ribbon: (blank, no text)', 'Bottom ribbon: BRINGING HOME THE TREE'),
 'W6': ('6ac71082fa3cae10170ef9de 6ac714f835cf3f6ec802eba3 6ac7108d50fc6704d30bf8a2 6ac71126336f83586601148e'.split(),
        'Bottom ribbon: (blank, no text)', 'Bottom ribbon: TO THE LIQUOR STORE (new art, incl. small ROAD TRIP plate)'),
 'W7': (['6ac71013e2a15b12600266ae'], 'No headline (wreath + 2026 tag only)', 'Arched headline: MERRY CHRISTMAS (new art)'),
 'W9': (['6ac711e2a005c19c550d8980'], 'KEEP CHRIST / IN CHRISTMAS / FOR UNTO US A CHILD IS BORN / Luke 2:11 - Glory to God in the Highest - Isaiah 9:6',
        'KEEP CHRIST / IN CHRISTMAS / FOR UNTO US A CHILD IS BORN (scripture-reference line removed; 1-bit engraving redraw)'),
 'G1': (['6ac337dd95514001380fd619'], 'JOLLY, TIRED, AND, AND CAFFEINATED', 'JOLLY, TIRED, AND CAFFEINATED'),
 'G2': ('6ac7020567e0e81ed20ffda7 6ac7113d42c818a1ad095ed6 6ac7113afb1d11d19e036f60 6ac7118407e4149a0f001011 6ac6ff9c2a2224fe7d0775a1 6ac700f42a2224fe7d077640 6ac717f3aa7a21cb900b506c 6ac702723a88d2f780057c9b 6ac7155542c818a1ad0960c7 6ac702fb1e2eac4da206fc65'.split(),
        'MY ELF MADE / MADE ME DO IT', 'MY ELF / MADE ME DO IT'),
 'G3': ('6ac7149db8146913210038d0 6ac71401fb1d11d19e0370ee 6ac7121fa005c19c550d899e 6ac711c0a005c19c550d8971 6ac71443a005c19c550d8a93 6ac71179b814691321003745 6ac713f542c818a1ad09602a 6ac7126007e4149a0f001079 6ac7232d73283b982509a1c3'.split(),
        'Meter: P-A-T-I-T-A-N-E-C-E', 'Meter: P-A-T-I-E-N-C-E'),
}
assert sum(len(v[0]) for v in G.values()) == 49
TFR = {r['product_id']: r for r in csv.DictReader(open(W + '/d6_new_art/text_fix/results.csv'))}
WEL = json.load(open(O + '/art/welcome_meta.json'))
OUTD = O + '/wording_previews'; os.makedirs(OUTD, exist_ok=True)

def staged(pid):
    """(art, per_var placement, native_w, source)"""
    d, j, _ = pj(pid); ph = j['placeholders']
    for src in (f'{O}/placements/{pid}.json', f'{W}/d6_qa_fixes/placements/{pid}.json'):
        if os.path.exists(src):
            s = json.load(open(src)); art = '/home/user/' + s['art']['file'] if not s['art']['file'].startswith('work/') else W + '/' + s['art']['file'][5:]
            if not os.path.exists(art): art = '/home/user/crowned-co-data/' + s['art']['file']
            pv = {str(v): g['placement'] for g in s['print_areas'] for v in g['variant_ids']}
            nw = s['art'].get('native_source_width_px') if s['art'].get('upscaled') else None
            return art, pv, nw, os.path.relpath(src, W)
    art = W + '/d6_new_art/text_fix/' + TFR[pid]['sha1'] + '.png'
    o = Image.open(d + '/original.png'); a = Image.open(art)
    if abs(o.width / o.height - a.width / a.height) < 0.01: pv = proposed(j); how = 'batch proposed placement'
    else: pv = match_box(d + '/original.png', proposed(j), art, ph); how = 'content-box fit to proposed'
    return art, pv, None, 'text_fix + ' + how

def welcome_art(art):
    b = os.path.basename(art)
    for k, v in WEL.items():
        if b.startswith(k) or b == k: return O + '/' + v['file'] if not v['file'].startswith('/') else v['file']
    return None

rows = []; tiles = {}; GZ = {}
SRCMAP = json.load(open(W + '/d6_new_art/text_fix/work/src_map.json'))
for grp_, (pids_, _, _) in G.items():   # group close-up box from the first same-size source/fix pair
    for p_ in pids_:
        if p_ in TFR and grp_ not in ('W6', 'W7', 'W9') and grp_ not in GZ:
            tf_ = W + '/d6_new_art/text_fix/' + TFR[p_]['sha1'] + '.png'; sp_ = SRCMAP.get(TFR[p_]['sha1'], [None, None])[1]
            if sp_ and Image.open(sp_).size == Image.open(tf_).size:
                b_ = diff_box(sp_, tf_)
                if b_: GZ[grp_] = b_
for grp, (pids, before, after) in G.items():
    for pid in pids:
        d, j, _ = pj(pid); ph = j['placeholders']; L = largest(ph); blank = blank_for(j)
        art, pv, nw, srcnote = staged(pid)
        q = qa(pid, art, pv, nw); bq = qa(pid, d + '/original.png', current(j))
        st = 'PASS' if (q['inside_min'] >= 0.999 and q['dpi_largest'] >= 150 and not (q['upscaled'] and q['native_dpi_largest'] < 150)) else \
             ('WARN' if q['inside_min'] >= 0.999 and q['dpi_largest'] >= 150 else 'REWORK')
        variants = [('PROPOSED', after, art, pv, nw, q, st)]
        if grp == 'W2':
            wa = welcome_art(art)
            if wa:
                if Image.open(wa).size == Image.open(art).size: wpv = pv
                else: wpv = match_box(art, pv, wa, ph)
                wq = qa(pid, wa, wpv, nw)
                wst = 'PASS' if (wq['inside_min'] >= 0.999 and wq['dpi_largest'] >= 150 and not (wq['upscaled'] and wq['native_dpi_largest'] < 150)) else ('WARN' if wq['dpi_largest'] >= 150 else 'REWORK')
                variants.append(('ALTERNATIVE (QA-recommended)', 'Street-sign plaque: WELCOME', wa, wpv, nw, wq, wst))
        Bimg = Image.open(d + '/original.png').convert('RGBA')
        cols = [(place_on(Bimg, j['current'], *ph[L], blank), ['BEFORE: live print file, current placement',
                 f"original.png {Bimg.width}x{Bimg.height}  s={j['current']['scale']}  | {bq['dpi_largest']} dpi eff. | inside {bq['inside_min']:.1%}",
                 f'wording: {before}'[:95], (f'  {before[95:190]}' if len(before) > 95 else '')])]
        zrow = []
        for lab, txt, a_, pv_, nw_, q_, st_ in variants:
            A = Image.open(a_).convert('RGBA'); p = pv_[L]
            cols.append((place_on(A, p, *ph[L], blank), [f'AFTER {lab} [{st_}]', f"{os.path.basename(a_)[:40]} {A.width}x{A.height}",
                         f"x={p['x']} y={p['y']} s={p['scale']} | {q_['dpi_largest']} dpi eff." + (f" / {q_['native_dpi_largest']} native" if q_['upscaled'] else '') + f" | inside {q_['inside_min']:.2%}",
                         f'wording: {txt}'[:95], (f'  {txt[95:190]}' if len(txt) > 95 else '')]))
        # text close-up: changed region (same-aspect art) else centre crop
        zb = None
        if pid in TFR and grp not in ('W6', 'W7', 'W9'):
            tf = W + '/d6_new_art/text_fix/' + TFR[pid]['sha1'] + '.png'; sp = SRCMAP.get(TFR[pid]['sha1'], [None, None])[1]
            if sp and Image.open(sp).size == Image.open(tf).size: zb = diff_box(sp, tf)
            if zb: GZ.setdefault(grp, zb)
            else: zb = GZ.get(grp)
        if zb and grp in ('W1', 'W2', 'W3', 'W4', 'W5', 'G1', 'G2', 'G3'):
            zrow.append((crop_on(Bimg, zb, blank), ['BEFORE text close-up']))
            for lab, txt, a_, *_ in variants: zrow.append((crop_on(Image.open(a_).convert('RGBA'), zb, blank), [f'AFTER {lab.split()[0]} text close-up']))
        out = f'{OUTD}/{grp}_{pid}.png'
        compose([f'{pid}  |  shop {SHOP}  |  group {grp}  |  wording proposal (NOT applied; owner decision)', j['title'][:115],
                 f'BEFORE wording: {before}'[:160], f'AFTER wording:  {after}'[:160] + ('   | ALT: WELCOME' if len(variants) > 1 else '')],
                cols, out, zrow=zrow)
        tiles.setdefault(grp, []).append((pid, cols, [v[6] for v in variants]))
        for lab, txt, a_, pv_, nw_, q_, st_ in variants:
            rows.append(dict(product_id=pid, shop_id=SHOP, group=grp if lab == 'PROPOSED' else grp + '-ALT', before_text=before, after_text=txt,
                             art_file=os.path.relpath(a_, '/home/user'), placement_source=srcnote if lab == 'PROPOSED' else 'WELCOME variant, same placement',
                             preview_png=f'work/d6_final_rework/wording_previews/{grp}_{pid}.png', largest_variant=L,
                             dpi=q_['dpi_largest'], native_dpi=q_['native_dpi_largest'], dpi_min_all_variants=q_['dpi_min'], inside_pct=round(q_['inside_min'] * 100, 2),
                             status=st_, wording_status='PENDING OWNER APPROVAL'))
        print(grp, pid, [(r['status'], r['dpi'], r['inside_pct']) for r in rows if r['product_id'] == pid])

with open(O + '/wording_previews.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, list(rows[0].keys())); w.writeheader(); w.writerows(rows)
# contact sheet per group: each tile = BEFORE | AFTER (| ALT)
for grp, ts in tiles.items():
    ncol = 2 if grp == 'W2' else 3; TWd = 780 if grp == 'W2' else 520; TH = 300
    nrow = (len(ts) + ncol - 1) // ncol
    S = Image.new('RGB', (TWd * ncol + 20, TH * nrow + 60), (25, 25, 28)); dr = ImageDraw.Draw(S)
    dr.text((10, 10), f'{grp}: {G[grp][1][:70]}  ->  {G[grp][2][:70]}' + ('  (3rd image = WELCOME alt)' if grp == 'W2' else ''), fill='white', font=FONTB)
    for i, (pid, cols, sts) in enumerate(ts):
        x0, y0 = 10 + (i % ncol) * TWd, 50 + (i // ncol) * TH; k = len(cols); cw = (TWd - 10) // k
        for c_, (im, _) in enumerate(cols):
            t = im.copy(); t.thumbnail((cw - 6, 240)); S.paste(t, (x0 + c_ * cw + (cw - t.width) // 2, y0 + (240 - t.height) // 2))
        col = (90, 220, 90) if all(s == 'PASS' for s in sts) else (240, 200, 60)
        dr.text((x0, y0 + 246), f"{pid}  {'/'.join(sts)}", fill=col, font=FONTB)
    S.save(f'{O}/contact_sheets/wording_{grp}.png', optimize=True)
from collections import Counter
print(Counter((r['group'][:2], r['status']) for r in rows), len(rows))
