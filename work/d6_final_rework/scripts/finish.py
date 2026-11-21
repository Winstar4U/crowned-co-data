"""Task A+B+D wrap-up: results.csv (every not-yet-PASS item and its outcome), generation_jobs.csv (NOT run),
before/after contact sheets. LOCAL ONLY. Run after build_b.py and build_c.py."""
import csv, glob, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from frlib import *

res = json.load(open(O + '/results_b.json'))
for r in res: r['source_of_item'] = 'this session (d6_final_rework)'
# OWNER decision item (no artwork defect to repair)
dsp = {r['product_id']: r for r in csv.DictReader(open(W + '/d6_warn_disposition/disposition.csv'))}
o = dsp['6ad4254232b024bb32043467']
res.append(dict(product_id=o['product_id'], shop_id=o['shop_id'], title=pj(o['product_id'])[1]['title'], issue='OWNER: ' + o['warn_issues'],
                fix='none (owner choice): proposed fit s=0.553 vs full-bleed cover x=0.5,y=0.53,s=1.2 (both checked 100% inside safe circle in d6_warn_disposition)',
                art_file='crowned-co-data/' + os.path.relpath(pj(o['product_id'])[0], '/home/user/crowned-co-data') + '/original.png', placement_json='', before_after_png='work/d6_warn_disposition/before_after/',
                largest_variant='', effective_dpi_largest='', native_dpi_largest='', dpi_min_all_variants='', inside_safe_pct=100.0, status='BLOCKED',
                reason='owner decision: opaque full-bleed photo on white ceramic ornament (aesthetic choice, prints fine either way)', source_of_item='d6_warn_disposition OWNER'))
# carried-forward upscale WARNs from d6_qa_fixes (no new work; native resolution can only come from regeneration)
qa_jobs = []
for x in csv.DictReader(open(W + '/d6_qa_fixes/results.csv')):
    if x['qa_status'] != 'WARN' or 'winstar-recovery' in x['file']: continue
    pid = x['product_id']; pjf = glob.glob(f"{W}/d6_qa_fixes/placements/{pid}*.json"); pjf = [p for p in pjf if 'optionA' not in p][0]
    s = json.load(open(pjf)); d, j, _ = pj(pid); ph = j['placeholders']; L = largest(ph)
    pv = {str(v): g['placement'] for g in s['print_areas'] for v in g['variant_ids']}
    nat = s['art']['native_source_width_px']; nd_ = round(300 * nat / (pv[L]['scale'] * ph[L][0]))
    res.append(dict(product_id=pid, shop_id=j['shop_id'], title=j['title'], issue=x['issue'], fix=x['fix_applied'], art_file='crowned-co-data/' + x['file'],
                    placement_json='work/d6_qa_fixes/placements/' + os.path.basename(pjf), before_after_png=f'work/d6_qa_fixes/before_after/{pid}.png',
                    largest_variant=L, effective_dpi_largest=x['effective_dpi_largest_variant'], native_dpi_largest=nd_, dpi_min_all_variants='',
                    inside_safe_pct=round(float(x['content_inside_min']) * 100, 2), status='WARN',
                    reason=f'carried forward: Real-ESRGAN upscale, native {nd_} dpi; only a native high-res regeneration clears it (optional job)', source_of_item='d6_qa_fixes WARN (no new work)'))
    qa_jobs.append((pid, j, L, ph, pv, nat, s['art']['file'], x['file']))

keys = ['product_id', 'shop_id', 'status', 'reason', 'issue', 'fix', 'art_file', 'placement_json', 'before_after_png', 'largest_variant',
        'effective_dpi_largest', 'native_dpi_largest', 'dpi_min_all_variants', 'inside_safe_pct', 'source_of_item', 'title']
with open(O + '/results.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, keys, extrasaction='ignore'); w.writeheader(); w.writerows(res)

# generation_jobs.csv - NOT RUN. required = none; optional native-resolution re-renders for every upscaled WARN
jobs = []
def job(pids, src, req_w, ref_h_ratio, why, prio, prompt_extra=''):
    jobs.append(dict(priority=prio, product_ids=' '.join(pids), source_file=src, required_px_w=req_w, required_px_h=round(req_w * ref_h_ratio),
                     ideal_px_w=round(req_w * 1.5), prompt=('Faithful high-resolution re-render of the attached artwork: identical composition, wording, spelling, '
                     'colours and layout; crisp clean edges; true transparent background (no checkerboard, no white box); PNG. ' + prompt_extra).strip(), why=why, status='NOT RUN (paid; needs owner approval)'))
seen = {}
for pid, j, L, ph, pv, nat, fa, xf in qa_jobs:
    key = fa
    req = round(0.5 * pv[L]['scale'] * ph[L][0])
    seen.setdefault(os.path.basename(fa).split('_realesrgan')[0], []).append((pid, req, fa))
for k, lst in seen.items():
    req = max(r for _, r, _ in lst); fa = lst[0][2]; im = Image.open(W + '/' + fa[5:] if fa.startswith('work/') else '/home/user/crowned-co-data/' + fa)
    job([p for p, _, _ in lst], 'crowned-co-data/' + fa + '  (upscaled stand-in; reference the native file named in its placement JSON)', req, im.height / im.width,
        f'native resolution for >=150 dpi at the staged placement (currently Real-ESRGAN upscale, WARN)', 'OPTIONAL')
for r in json.load(open(O + '/results_b.json')):
    if r['status'] == 'WARN' and 'upscaled' in r['reason']:
        s = json.load(open(O + '/placements/' + r['product_id'] + '.json')); d, j, _ = pj(r['product_id']); ph = j['placeholders']; L = largest(ph)
        pv = {str(v): g['placement'] for g in s['print_areas'] for v in g['variant_ids']}; req = round(0.5 * pv[L]['scale'] * ph[L][0])
        import build_b_items as BI
        job([r['product_id']], 'crowned-co-data/work/d6_new_art/' + BI.SRITEMS[r['product_id']][1].split('/d6_new_art/')[1], req,
            s['art']['px'][1] / s['art']['px'][0], 'native resolution for >=150 dpi (currently Real-ESRGAN upscale, WARN)', 'OPTIONAL')
    if r['product_id'] == '6ac71082fa3cae10170ef9de':
        s = json.load(open(O + '/placements/' + r['product_id'] + '.json')); d, j, _ = pj(r['product_id']); ph = j['placeholders']; L = largest(ph)
        job(['6ac71082fa3cae10170ef9de'], 'winstar-recovery/regenerated/JINGLE_SHARED_regen.png', round(0.5 * ph[L][0] * s['print_areas'][0]['placement']['scale']), 1360 / 2048,
            'shower curtain needs native >=150 dpi; only if W6 wording is approved and the upscale is not accepted', 'CONDITIONAL (W6 approved)')
with open(O + '/generation_jobs.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, list(jobs[0].keys())); w.writeheader(); w.writerows(jobs)

# contact sheets of this session's before/after (3 x 3 per sheet)
items = [r for r in json.load(open(O + '/results_b.json'))]
TW, TH = 530, 330
for n in range(0, len(items), 9):
    S = Image.new('RGB', (TW * 3 + 20, TH * 3 + 20), (25, 25, 28)); dr = ImageDraw.Draw(S)
    for i, r in enumerate(items[n:n + 9]):
        x0, y0 = 10 + (i % 3) * TW, 10 + (i // 3) * TH
        ba = Image.open(O + '/before_after/' + r['product_id'] + '.png'); th_ = 26 * 4 + 12
        top = ba.crop((0, th_, ba.width, min(ba.height, th_ + 380))); top.thumbnail((TW - 10, 262)); S.paste(top, (x0, y0))
        col = {'PASS': (90, 220, 90), 'WARN': (240, 200, 60), 'BLOCKED': (120, 170, 255)}.get(r['status'], (240, 80, 80))
        dr.text((x0, y0 + 268), f"{r['product_id']}  {r['status']}  {r['effective_dpi_largest']} dpi (native {r['native_dpi_largest']})", fill=col, font=FONTB)
        dr.text((x0, y0 + 292), f"inside {r['inside_safe_pct']}%  {r['title'][:55]}", fill='white', font=FONTS)
    S.save(f'{O}/contact_sheets/before_after_{n // 9 + 1}.png', optimize=True)
from collections import Counter
print(Counter(r['status'] for r in res), len(res), 'jobs', len(jobs))
