"""Task A+B: every D6 artwork item still not at PASS/accepted -> local repair or exact blocker.
LOCAL ONLY: no Printify writes, no Higgsfield, no Bridge, no git. Run: python3 -I build_b.py <sr_dir>
Writes placements/<pid>.json, before_after/<pid>.png, results_b.json (consumed by finish.py)."""
import csv, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from frlib import *

SR = sys.argv[1]
REG = {r['product_id']: r for r in csv.DictReader(open(BR + '/regenerated/regeneration_register_24.csv'))}
ENGR = [p for p, r in REG.items() if r['file'].endswith('_engrave_final.png')]
JINGLE = ['6ac71082fa3cae10170ef9de', '6ac714f835cf3f6ec802eba3', '6ac7108d50fc6704d30bf8a2', '6ac71126336f83586601148e']
NF = W + '/d6_new_art/fixed/'; TF = W + '/d6_new_art/text_fix/'
SRITEMS = {  # pid: (sr key, native file, prior status source)
    '6ac713e635cf3f6ec802eb32': ('w713e6', NF + '873af255de3e870c6a62bf0902fea098bf709c47.png'),
    '6ac6fe9f0a223533b30703f2': ('w6fe9f', NF + 'a8556930c780ac13556f0ffa91467d32f4a0bed2.png'),
    '6ac6fe9c7a961335020e18a9': ('w6fe9c', NF + '6e444f4fc6ce3fc5fb144f255d759c245e0a9bd4.png'),
    '6ac71401fb1d11d19e0370ee': ('w71401', TF + 'f193d6d08b1ad932eb905ac8d3c3c0b6119a8e76.png'),
    '6ac7127aa5ade89b5c080fc0': ('w7127a', TF + '5fa6bcd6cdbb68aaf4c51c41f42b629bf054ff5e.png'),
}
TARGET_UP = 0.75   # src/print ratio after upscale (225 dpi), same target as d6_qa_fixes
os.makedirs(O + '/placements', exist_ok=True); os.makedirs(O + '/before_after', exist_ok=True); os.makedirs(O + '/art', exist_ok=True)

def status_of(q, blocked=None, warns=()):
    if blocked: return 'BLOCKED'
    if q['inside_min'] < 0.999: return 'REWORK'
    if q['dpi_largest'] < 150: return 'REWORK'
    if q['upscaled'] and q['native_dpi_largest'] < 150: return 'WARN'
    if warns: return 'WARN'
    return 'PASS'

def zoom_box(art):
    bb = bbox(Image.open(art)); cx, cy = (bb[0] + bb[2]) / 2, (bb[1] + bb[3]) / 2; w = (bb[2] - bb[0]) * 0.32; h = (bb[3] - bb[1]) * 0.32
    return (cx - w / 2, cy - h / 2, cx + w / 2, cy + h / 2)

results = []
def do(pid, art, per_var, issue, fix, native_w=None, blocked=None, warns=(), zoom=None, extra=None, before_art=None, label_after='AFTER'):
    d, j, batch = pj(pid); ph = j['placeholders']; L = largest(ph); blank = blank_for(j)
    q = qa(pid, art, per_var, native_w); st = status_of(q, blocked, warns)
    bfile = before_art or d + '/original.png'; bpl = per_var if before_art else current(j)
    bq = qa(pid, bfile, bpl)
    blabel = 'BEFORE (prior repaired art, native px, same placement)' if before_art else 'BEFORE (live print file, current placement)'
    reason = blocked or ('; '.join(warns) if warns else '')
    if st == 'REWORK' and not reason:
        reason = 'geometry: content outside safe area' if q['inside_min'] < 0.999 else f"{q['dpi_largest']} dpi < 150 on largest variant"
    if q['upscaled'] and st == 'WARN': reason = (reason + '; ' if reason else '') + f"upscaled: effective {q['dpi_largest']} dpi, native {q['native_dpi_largest']} dpi (upscale adds no true detail)"
    pjson = dict(product_id=pid, shop_id=j['shop_id'], title=j['title'], blueprint_id=j['blueprint_id'], print_provider_id=j['print_provider_id'],
                 position=j['position'], decoration_method=j.get('decoration_method'), issue=issue, fix=fix,
                 art=dict(file=os.path.relpath(art, '/home/user'), px=q['px'], sha1=sha1(art), native_source_width_px=native_w or q['px'][0], upscaled=q['upscaled']),
                 print_areas=groups(per_var), qa=q, status=st, reason=reason,
                 before=dict(file=os.path.relpath(bfile, '/home/user'), placement=bpl[largest(ph)], dpi_largest=bq['dpi_largest'], inside_min=bq['inside_min']),
                 live_change_made=False, note='NON-LIVE staging file. Nothing uploaded. Applying it needs an image upload + product update = owner-approved write.')
    if extra: pjson.update(extra)
    write_json(f'{O}/placements/{pid}.json', pjson)
    Bimg = Image.open(before_art or d + '/original.png').convert('RGBA'); Aimg = Image.open(art).convert('RGBA')
    pv = q['per_variant'][L]
    cols = [(place_on(Bimg, bpl[L], *ph[L], blank), [f'{blabel} - variant {L}',
             f"{os.path.basename(bfile)[:40]} {Bimg.width}x{Bimg.height}  s={bpl[L]['scale']}",
             f"{bq['dpi_largest']} dpi eff. | inside {bq['inside_min']:.1%}"]),
            (place_on(Aimg, per_var[L], *ph[L], blank), [f'{label_after} - variant {L}  [{st}]',
             f"{os.path.basename(art)[:44]} {Aimg.width}x{Aimg.height}",
             f"x={per_var[L]['x']} y={per_var[L]['y']} s={per_var[L]['scale']} | {pv['effective_dpi']} dpi eff. / {pv['native_dpi']} native | inside {q['inside_min']:.2%}"])]
    zb = zoom or zoom_box(art); zbb = zoom or zoom_box(before_art or d + '/original.png')
    zrow = [(crop_on(Bimg, zbb, blank), ['BEFORE detail (art px)']), (crop_on(Aimg, zb, blank), ['AFTER detail (art px)'])]
    compose([f"{pid}  |  shop {j['shop_id']}  |  {st}", j['title'][:110], f'Issue: {issue}'[:150], f'Fix: {fix}'[:150] + (f'  | Reason: {reason}'[:150] if reason else '')],
            cols, f'{O}/before_after/{pid}.png', zrow=zrow)
    results.append(dict(product_id=pid, shop_id=j['shop_id'], title=j['title'], issue=issue, fix=fix, art_file=os.path.relpath(art, '/home/user'),
                        placement_json=f'work/d6_final_rework/placements/{pid}.json', before_after_png=f'work/d6_final_rework/before_after/{pid}.png',
                        largest_variant=L, effective_dpi_largest=q['dpi_largest'], native_dpi_largest=q['native_dpi_largest'], dpi_min_all_variants=q['dpi_min'],
                        inside_safe_pct=round(q['inside_min'] * 100, 2), status=st, reason=reason))
    print(pid, st, q['dpi_largest'], q['native_dpi_largest'], q['inside_min'], reason[:80])

# 1. Santa's List scarf: checker removed locally
pid = '6ac7112383f1a0e50d071cdf'; d, j, _ = pj(pid)
art = O + '/art/6ac7112383f1a0e50d071cdf_checker_removed.png'; met = json.load(open(O + '/art/6ac7112383f1a0e50d071cdf_checker_metrics.json'))
do(pid, art, {v: {'x': 0.5, 'y': 0.5, 'scale': 0.305, 'angle': 0} for v in j['placeholders']},
   'REWORK: grey/white checkerboard baked into source PNG (exterior tile fragments + tile pattern inside the scroll); top line cropped at current scale 0.4',
   f"local checker removal: exterior tiles flood-cleared ({met['exterior_tile_px_cleared']} px) + {met['stray_island_px_cleared']} px stray fragments, "
   f"scroll tile pattern gain-flattened (tile contrast {met['parchment_tile_contrast_before']}->{met['parchment_tile_contrast_after']}, -{met['parchment_tile_contrast_reduction']:.0%}), "
   f"{met['enclosed_holes_filled']} punched-out white holes refilled white; re-placed x=0.5 y=0.5 s=0.305",
   zoom=(0.25, 0.45, 0.6, 0.72), extra=dict(checker_metrics=met))

# 2. two local-art FAILs -> second session's regenerated art (PASS in its register); placement re-fit here
for pid, fix in [('6ac717a24636838bd804f846', 'regenerated art (second session, Higgsfield job 4a4e057e): solid sunburst, no hole; fitted to the content box of the proposed placement'),
                 ('6ac7113450fc6704d30bf944', 'regenerated art (second session, Higgsfield job e8db5460): complete MERRY EVERYTHING. / HAPPY ALWAYS. letters; fitted to the content box of the proposed placement')]:
    d, j, _ = pj(pid); art = BR + '/regenerated/' + pid + '_regen.png'
    pv = match_box(d + '/original.png', proposed(j), art, j['placeholders'])
    do(pid, art, pv, 'local-art FAIL: ' + REG[pid]['defect'], fix)

# 3. skeleton scarf (regenerated, needed placement re-fit)
pid = '6ac7117346dd1e896e04e0c4'; d, j, _ = pj(pid); art = BR + '/regenerated/' + pid + '_regen.png'
do(pid, art, match_box(d + '/original.png', proposed(j), art, j['placeholders']), 'NEEDS_GENERATION: banner text covered by skeleton limbs',
   'regenerated art (second session, job 9903778d) EGGNOG RECOVERY IN PROGRESS banner clear; placement re-fitted to the proposed content box')

# 4. 14 engraving tumblers (regenerated 1-bit art) - placement + geometry
for pid in ENGR:
    d, j, _ = pj(pid); art = BR + '/' + REG[pid]['file'].split('winstar-recovery/')[1]
    pv = match_box(d + '/original.png', proposed(j), art, j['placeholders'])
    warns, blocked = [], None
    if pid == '6ac711e2a005c19c550d8980': blocked = 'owner wording decision W9 (scripture-reference line removed) pending'
    if pid == '6ac71152ed135347800f9ac9': warns = ['checklist text ~0.9 mm cap height on 3 in engrave area - confirm with provider proof']
    do(pid, art, pv, 'NEEDS_GENERATION: full-colour art on engraving product', 'regenerated 1-bit black-on-transparent engraving art (second session, job ' + REG[pid]['higgsfield_job'][:8] + '); fitted to the proposed content box',
       blocked=blocked, warns=warns)

# 5. five repaired-art resolution WARNs -> local Real-ESRGAN (anime6B) upscale, substrate-agnostic edge bleed
for pid, (key, nat) in SRITEMS.items():
    d, j, _ = pj(pid); pv = proposed(j); nw, nh = Image.open(nat).size
    rmin = min(nw / (pv[v]['scale'] * j['placeholders'][v][0]) for v in pv)
    fac = min(4.0, TARGET_UP / rmin); out = f'{O}/art/{pid}_realesrgan-anime6B_x{fac:.2f}.png'
    if not os.path.exists(out):
        if not os.path.exists(f'{SR}/{key}.png'): print('SR missing', pid); continue
        s = Image.open(f'{SR}/{key}.png'); s.resize((round(nw * fac), round(nh * fac)), Image.LANCZOS).save(out, optimize=True)
    do(pid, out, pv, f'repaired-art WARN: low resolution (src/print ratio {rmin:.2f} = {300 * rmin:.0f} dpi) on {nat.split("/")[-2]}/{os.path.basename(nat)[:10]}',
       f'local Real-ESRGAN anime6B x{fac:.2f} (edge-bleed, no white matte), placement unchanged', native_w=nw, before_art=nat, label_after='AFTER (upscaled)')

# 6. BLOCKED on wording: 4 Jingle + wreath (second session art with proposed wording); computed placement for C
for pid in JINGLE + ['6ac71013e2a15b12600266ae']:
    d, j, _ = pj(pid); art = BR + '/' + REG[pid]['file'].split('winstar-recovery/')[1]; native = None
    if pid in JINGLE and os.path.exists(f'{SR}/jingle.png'):
        pv0 = match_box(d + '/original.png', proposed(j), art, j['placeholders'])
        nw = Image.open(art).size[0]; rmin = min(nw / (pv0[v]['scale'] * j['placeholders'][v][0]) for v in pv0)
        if rmin < 0.5:
            fac = min(4.0, TARGET_UP / rmin); out = f'{O}/art/JINGLE_SHARED_realesrgan-anime6B_x{fac:.2f}.png'
            if not os.path.exists(out): Image.open(f'{SR}/jingle.png').resize((round(nw * fac), round(1360 * fac)), Image.LANCZOS).save(out, optimize=True)
            art, native = out, nw
    pv = match_box(d + '/original.png', proposed(j), art, j['placeholders'])
    grp = 'W7' if pid == '6ac71013e2a15b12600266ae' else 'W6'
    do(pid, art, pv, 'NEEDS_GENERATION: ' + REG[pid]['defect'], 'second-session art with PROPOSED wording; fitted to the proposed content box' + (' (Real-ESRGAN upscaled for this size)' if native else ''),
       native_w=native, blocked=f'owner wording decision {grp} pending (art exists; nothing to generate unless the wording is rejected)')

json.dump(results, open(O + '/results_b.json', 'w'), indent=1)
from collections import Counter; print(Counter(r['status'] for r in results))
