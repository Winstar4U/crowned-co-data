"""Build the Phase 6 live-application batches from existing local evidence only.
No Printify calls, no writes anywhere except reports/phase6/.
Run from the repo root: python3 reports/phase6/build_phase6.py
"""
import csv, glob, json, os, collections

OUT = 'reports/phase6'
master = list(csv.DictReader(open('reports/master_register/master_defects.csv')))
sales = {r['product_id']: r for r in csv.DictReader(open('reports/Winstar_Sales_Readiness_Register.csv'))}
warn = {r['product_id']: r for r in csv.DictReader(open('work/d6_warn_disposition/disposition.csv'))}
qafix = collections.defaultdict(list)
for r in csv.DictReader(open('work/d6_qa_fixes/results.csv')):
    qafix[r['product_id']].append(r)

# placement.json per product (batch evidence holds the CURRENT live values = rollback)
pj = {}
for f in glob.glob('work/d6_batch*/*/placement.json'):
    pj[os.path.basename(os.path.dirname(f))] = f

# products with any open owner/technical/not-verified row cannot go in a ready batch
blocked = collections.defaultdict(list)
for r in master:
    if r['final_status'] != 'VERIFIED READY FOR APPROVAL':
        blocked[r['product_id']].append(f"{r['defect_type']}: {r['final_status']}")
# apply the warn-disposition outcomes that post-date the register
for pid, w in warn.items():
    if w['disposition'] == 'REWORK':
        blocked[pid].append('artwork: REWORK REQUIRED (baked-in checkerboard, warn disposition)')
    elif w['disposition'] == 'OWNER':
        blocked[pid].append('artwork: BLOCKED — OWNER DECISION (warn disposition)')

ready = collections.OrderedDict()
for r in master:
    if r['final_status'] != 'VERIFIED READY FOR APPROVAL':
        continue
    pid = r['product_id']
    ready.setdefault(pid, {'shop_id': r['shop_id'], 'shop': r['shop_name'], 'title': r['title'],
                           'defects': [], 'actions': [], 'evidence': []})
    d = ready[pid]
    d['defects'].append(r['defect_type'])
    d['actions'].append(r['live_action_needed'])
    d['evidence'].append(r['evidence_path_or_ref'])

rows, held = [], []
for pid, d in ready.items():
    s = sales.get(pid, {})
    link = s.get('channel_link', '')
    holiday = s.get('holiday', '')
    rb = ''
    if pid in pj:
        p = json.load(open(pj[pid]))
        c = p.get('current', {})
        rb = (f"re-upsert print_areas position={p.get('position')} image_id={p.get('image_id')} "
              f"x={c.get('x')} y={c.get('y')} scale={c.get('scale')} angle={c.get('angle')} "
              f"(values captured {p.get('updated_at')})")
    else:
        rb = 'restore prior print_areas from a get-product snapshot taken immediately before the write'
    change = ' | '.join(sorted(set(a for a in d['actions'] if a and a != 'none')))
    if pid in warn and warn[pid]['disposition'] == 'FIXED':
        change += f" | warn-fix: upload {warn[pid]['new_file'].split(';')[1].strip()} then apply {warn[pid]['new_file'].split(';')[0].strip()}"
    if not link and 'printify-publish-product' in change:
        # Publishing an unlinked product would CREATE a listing: that is a separate publication decision.
        import re
        change = re.sub(r';?\s*then printify-publish-product[^|]*', '', change).strip()
        change += ' | NO publish step: no channel link recorded (publishing would create a new listing = separate owner decision; external:null does not prove unpublished)'
    upscale = any('realesrgan' in a.lower() or '_x4' in a.lower() for a in d['actions']) or \
        (pid in warn and warn[pid]['disposition'] == 'FIXED' and '_x4' in warn[pid]['new_file'])
    risk = []
    if link:
        risk.append('LIVE LISTING: Printify update re-syncs to the channel; mockups regenerate')
    if any(x in ('artwork', 'resolution') for x in d['defects']):
        risk.append('art swap: new upload replaces the live print file')
    if upscale:
        risk.append('AI-upscaled file (no new detail)')
    rec = {'product_id': pid, 'shop_id': d['shop_id'], 'shop': d['shop'], 'title': d['title'][:90],
           'holiday': holiday, 'channel_link': link, 'defects': '+'.join(sorted(set(d['defects']))),
           'exact_change': change or 'placement update per placement.json proposed values',
           'evidence': ' ; '.join(sorted(set(d['evidence'])))[:300],
           'risk': '; '.join(risk) or 'unlinked draft-side product: low customer exposure',
           'rollback': rb}
    if pid in blocked:
        rec['held_reason'] = ' ; '.join(blocked[pid])
        held.append(rec)
    else:
        rows.append(rec)

# PROFIT FIRST ordering: linked first, then holiday, then shop
rows.sort(key=lambda r: (r['channel_link'] == '', r['holiday'] not in ('Y', 'yes', 'True', '1', 'holiday'), r['shop_id']))
for i, r in enumerate(rows):
    r['batch'] = f"LA-{i // 40 + 1:02d}"

fields = ['batch', 'product_id', 'shop_id', 'shop', 'title', 'holiday', 'channel_link', 'defects',
          'exact_change', 'risk', 'rollback', 'evidence']
with open(f'{OUT}/live_application_batches.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)
with open(f'{OUT}/held_from_live_batches.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=fields[1:] + ['held_reason'], extrasaction='ignore'); w.writeheader(); w.writerows(held)

summ = collections.OrderedDict()
for r in rows:
    b = summ.setdefault(r['batch'], collections.Counter())
    b['products'] += 1
    b['linked'] += bool(r['channel_link'])
    b[r['shop']] += 1
    b['art_swap'] += 'art swap' in r['risk']
    b['upscaled'] += 'AI-upscaled' in r['risk']
json.dump({'ready_products': len(rows), 'held_products': len(held), 'batches': summ},
          open(f'{OUT}/batch_summary.json', 'w'), indent=1)
print(len(rows), 'ready;', len(held), 'held')
for k, v in summ.items():
    print(k, dict(v))
