#!/usr/bin/env python3
"""Build the reconciled master defect register from existing evidence only (read-only on sources)."""
import csv, glob, os, re, collections as C

D = '/home/user/crowned-co-data/'
R = '/home/user/winstar4u/my-projects/winstar-recovery/'
OUT = D + 'reports/master_register/'
os.makedirs(OUT, exist_ok=True)

SHOPS = {'26418699': 'Shopify Winstar4U', '26603005': 'Etsy WinstarDesigns', '28059412': 'eBay Winstardeals4U',
         '28122957': 'TikTok My TikTok Shop', '29451844': 'Amazon Winstar4U'}
VR, RW, BO, BT, NV = ('VERIFIED READY FOR APPROVAL', 'REWORK REQUIRED', 'BLOCKED — OWNER DECISION',
                      'BLOCKED — TECHNICAL', 'NOT VERIFIED')

def rd(p):
    with open(p, newline='') as f:
        return list(csv.DictReader([l for l in f if not l.startswith('#')]))

sr = {r['product_id']: r for r in rd(D + 'reports/Winstar_Sales_Readiness_Register.csv')}
queue = {r['product_id']: r for r in rd(D + 'work/artwork_redesign_batches.csv')}
batch = {}
for f in sorted(glob.glob(D + 'work/d6_batch*/batch*_results.csv')):
    for r in rd(f):
        r['_file'] = f.replace(D, '')
        batch[r['product_id']] = r
ev = {r['product_id']: r for r in rd(R + 'registers/ALL_D6_389_evidence_register.csv')}
pqa = {r['product_id']: r for r in rd(R + 'qa/placement_qa_224.csv')}
raq = {r['product_id']: r for r in rd(R + 'qa/repaired_art_qa.csv')}
regen = {r['product_id']: r for r in rd(R + 'regenerated/regeneration_register_24.csv')}
qf_path = D + 'work/d6_qa_fixes/results.csv'
qfix = C.defaultdict(list)
if os.path.exists(qf_path):
    for r in rd(qf_path):
        qfix[r['product_id']].append(r)

# wording packet: group -> (after text)
wording = {}
for line in open(R + 'wording/WORDING_APPROVAL_PACKET.md'):
    m = re.match(r'\|\s*([GW]\d+)\s*\|([^|]*)\|([^|]*)\|([^|]*)\|([^|]*)\|', line)
    if m:
        g = m.group(1)
        wording[g] = ((m.group(4).strip(), m.group(5).strip(), m.group(3).strip()) if g in ('W1','W2','W3','W4','W5','W6','W7')
                      else (m.group(3).strip(), m.group(4).strip(), m.group(2).strip()[:60]))

rows = []
def add(sid, pid, dtype, desc, evid, owner, status, nxt, live, source):
    title = (sr.get(pid) or queue.get(pid) or ev.get(pid) or {}).get('title', '')
    rows.append(dict(shop_id=sid, shop_name=SHOPS[sid], product_id=pid, title=title, defect_type=dtype,
                     description=desc, evidence_path_or_ref=evid, owner=owner, final_status=status,
                     next_action=nxt, live_action_needed=live, source=source))

def pub(sid, pid):
    return f'then printify-publish-product shop {sid} product {pid} to resync the channel listing'

def art_swap(sid, pid, f):
    return (f'printify-upload-image ({f}); printify-upsert-product shop {sid} product {pid}: replace print_areas image id '
            f'(keep approved x/y/scale); ' + pub(sid, pid))

ART_CAT = {'white_box': 'artwork', 'checkerboard': 'artwork', 'low_contrast': 'artwork', 'garbled_text': 'artwork',
           'blank_text': 'artwork', 'engraving': 'artwork', 'low_res': 'resolution', 'other': 'artwork'}

# ---------------- D6 389 queue ----------------
for pid, q in queue.items():
    sid = q['shop_id']; e = ev[pid]; b = batch.get(pid, {})
    ws, qa, wg = e['workstream'], e['qa_outcome'], e['wording_group']
    ba = e['before_preview']; after = e['after_preview']
    hist = f"D6 batch {q['batch']} cause={q['defect_cause']}: {q['defect_note'][:160]}"
    fixes = qfix.get(pid, [])
    fx_status = {r['qa_status'] for r in fixes}
    fx_ev = (f"work/d6_qa_fixes/results.csv; work/d6_qa_fixes/before_after/{pid}.png") if fixes else ''
    src = 'D6 queue + winstar-recovery c74849e'
    if ws.startswith('BLOCKED'):
        iss = e['issues']
        if 'duplicate listing' in iss or pid == '69b0212c4fead7b1ce06b69e':
            add(sid, pid, 'duplicate_listing', 'Leftover "Copy of" duplicate of 69af94a507af56435a07b7ce (same art, same blueprint); not an art defect. '
                'Also LOW IP note: MagSafe(R) named in description.', f"{ba}; {b.get('_file','')}", 'Owner', BO,
                'Owner picks: retire the copy or retitle it', f'printify-unpublish-product shop {sid} product {pid} (or delete), or upsert title without "Copy of"', src)
        elif 'Cannot reproduce' in iss or 'not reproducible' in iss:
            add(sid, pid, 'placement', f'{hist}. D6 re-check could NOT reproduce the defect: live placement already inside safe area; '
                'zoomed live mockup shows text fully visible. Likely false positive in the historical register.',
                f"{ba}; {b.get('_file','')}", 'Owner', NV, 'Owner confirms closing as false positive (no write); then reclassify sales bucket', 'none', src)
        else:
            bp = q.get('title', '')
            m = re.search(r'only provider (\d+) ?([A-Za-z]*)', iss)
            alt = f'provider {m.group(1)} {m.group(2)}'.strip() if m else 'another provider'
            add(sid, pid, 'availability_discontinued', 'Print provider 99 no longer makes this blueprint (get-blueprint-variants -> 404 '
                f'provider mismatch); product cannot be fulfilled as configured. Underlying art defect: {q["defect_note"][:120]}',
                f"{ba}; {b.get('_file','')}", 'Owner', BO,
                f'Owner decides: recreate on {alt} (new product, loses listing history) or unpublish',
                f'printify-unpublish-product shop {sid} product {pid}; or create replacement product on {alt} (upsert-product + publish) then unpublish {pid}', src)
        continue

    if ws == 'PLACEMENT ONLY':
        p = pqa[pid]
        pos = b.get('position', 'front')
        live = (f"printify-upsert-product shop {sid} product {pid}: print_areas {pos} image x/y/scale -> {p['proposed']} "
                f"(was {p['current']}); " + pub(sid, pid))
        if qa == 'FAIL':
            if 'GEOMETRY' in p['issues']:
                fx = fixes[0] if fixes else None
                if fx and fx['qa_status'] == 'PASS':
                    add(sid, pid, 'placement', f"{hist}. Recovery QA FAIL (~88% inside lumbar variant 244224). Superseded by d6_qa_fixes: "
                        f"per-variant print_areas (lumbar gets own scale), content_inside_min {fx['content_inside_min']}, dpi {fx['effective_dpi_largest_variant']}; PASS.",
                        f"{fx_ev}; {after}", 'Owner', VR, 'Owner go-live approval (product-specific)',
                        f'printify-upsert-product shop {sid} product {pid}: split print_areas per variant (lumbar 244224 own scale) per d6_qa_fixes; ' + pub(sid, pid),
                        'winstar-recovery placement_qa_224 + d6_qa_fixes (newer)')
                else:
                    add(sid, pid, 'placement', f'{hist}. Recovery QA FAIL geometry; fix in progress (d6_qa_fixes absent/partial).', after, 'Claude', RW,
                        'Finish per-variant placement fix and re-QA', live, 'winstar-recovery placement_qa_224')
            else:  # resolution FAIL
                ratio = p['src_print_px_ratio_min']
                fx = fixes[0] if fixes else None
                if not fx:
                    add(sid, pid, 'resolution', f'{hist}. Recovery QA FAIL: src/print px ratio {ratio} (<0.33). Fix in progress (d6_qa_fixes absent).',
                        after, 'Claude', RW, 'Finish resolution fix and re-QA', live, 'winstar-recovery placement_qa_224')
                elif fx['qa_status'] == 'PASS':
                    add(sid, pid, 'resolution', f"{hist}. Recovery QA FAIL ratio {ratio}; superseded by d6_qa_fixes: {fx['fix_applied'][:120]}; "
                        f"{fx['effective_dpi_largest_variant']} dpi largest variant; PASS.", f'{fx_ev}; {after}', 'Owner', VR,
                        'Owner go-live approval (product-specific)', f"printify-upsert-product shop {sid} product {pid}: scale per d6_qa_fixes ({fx['fix_applied'][:60]}); " + pub(sid, pid),
                        'winstar-recovery placement_qa_224 + d6_qa_fixes (newer)')
                else:
                    nat = re.search(r'native-pixel equivalent (\d+) dpi', fx['notes'])
                    add(sid, pid, 'resolution', f"{hist}. Recovery QA FAIL ratio {ratio}. d6_qa_fixes applied AI upscale ({fx['fix_applied'][:70]}): "
                        f"{fx['effective_dpi_largest_variant']} dpi nominal but native-equivalent only {nat.group(1) if nat else '?'} dpi (no new detail); WARN.",
                        f'{fx_ev}; {after}', 'Owner', BO, 'Owner chooses: accept AI upscale / shrink motif / regenerate at 4k',
                        f"printify-upload-image ({fx['file']}); printify-upsert-product shop {sid} product {pid} with approved file/scale; " + pub(sid, pid),
                        'winstar-recovery placement_qa_224 + d6_qa_fixes (newer)')
            continue
        warn = ''
        if 'RESOLUTION-WARN' in p['issues']:
            warn = f" WARN: marginal resolution, src/print px ratio {p['src_print_px_ratio_min']} (<0.5) - show owner at approval."
        if 'non-rect' in p['shape_note'] and qa == 'WARN':
            warn += ' WARN: non-rectangular safe area; rect bounds independently verified, shape fit inherited from prior verify (confirm on Printify mockup).'
        add(sid, pid, 'placement', f"{hist}. Corrected placement {p['proposed']}; independent QA {qa}, content_inside_min {p['content_inside_min']}.{warn}",
            f"{ba}; {after}; winstar-recovery/qa/placement_qa_224.csv", 'Owner', VR, 'Owner go-live approval (product-specific)', live,
            'D6 queue + winstar-recovery placement_qa_224')
        if 'TRANSPARENCY-WARN' in p['issues']:
            add(sid, pid, 'artwork', f"Opaque background on {p['decoration']} product ({p['issues'][:90]}); prints as a box unless the blank is the same colour.",
                f"{after}; winstar-recovery/qa/placement_qa_224.csv", 'Claude', NV,
                f'Read-only check of enabled blank colours (printify-get-products-9eb shop {sid} product {pid})', 'none (if blank colour matches); else art swap', 'winstar-recovery placement_qa_224')
        dup = sr.get(pid, {}).get('flags', '')
        if 'DUPLICATE_LISTING' in dup:
            add(sid, pid, 'duplicate_listing', f"Sales register flags DUPLICATE_LISTING ({sr[pid]['flags']}); register note: {sr[pid]['reason'][:130]}", 'Winstar_Sales_Readiness_Register.csv flags; Quality Register §8f/§8g/§8k/§8p',
                'Owner', BO, 'Owner picks which listing to keep (or confirms size-variant pair is intentional)', f'printify-unpublish-product shop {sid} for the redundant member', 'Sales Readiness Register')
        continue

    # repaired art / regenerated
    ra = raq.get(pid); rg = regen.get(pid)
    cat = (ra or {}).get('category') or q['defect_cause']
    dtype = ART_CAT.get(cat, 'artwork')
    f = e['fix_file']
    issues = e['issues']
    if wg:
        before, after_txt, why = wording.get(wg, ('', '', ''))
        fxn = ''
        if fixes:
            fxn = ' d6_qa_fixes: ' + '; '.join(f"{x['qa_status']} {x['fix_applied'][:60]}" for x in fixes)
        add(sid, pid, 'wording', f"{hist}. Repaired art ({ws}, QA {qa}) uses NEW/CHANGED wording group {wg} ({why[:50]}): {before[:70]} -> {after_txt[:90]}.{fxn}",
            f"winstar-recovery/wording/WORDING_APPROVAL_PACKET.md ({wg}); {f}; {ba}", 'Owner', BO,
            f'Owner approves or edits wording {wg}; then go-live approval', art_swap(sid, pid, f), 'winstar-recovery wording packet + repaired_art_qa/regeneration_register')
        res_fix = [x for x in fixes if x['qa_status'] != 'PASS']
        if res_fix or (qa == 'FAIL' and not fixes):
            if not fixes:
                add(sid, pid, 'resolution' if 'LOW-RES' in issues else 'artwork', f'Repaired-art QA FAIL: {issues[:150]}. Fix in progress (d6_qa_fixes absent).',
                    f, 'Claude', RW, 'Finish fix and re-QA', art_swap(sid, pid, f), 'winstar-recovery repaired_art_qa')
            else:
                x = res_fix[0]
                add(sid, pid, 'resolution', f"Repaired-art QA FAIL ({issues[:90]}). d6_qa_fixes applied {x['fix_applied'][:70]}; {x['notes'][-80:]}; WARN.",
                    fx_ev, 'Owner', BO, 'Owner chooses: accept AI upscale / shrink motif / regenerate at 4k', art_swap(sid, pid, x['file']),
                    'winstar-recovery repaired_art_qa + d6_qa_fixes (newer)')
        continue
    if rg and rg['result'] == 'REWORK':
        opts = '; '.join(f"{x['fix_applied'][:55]} -> {x['effective_dpi_largest_variant']} dpi" for x in fixes) or 'fix in progress (d6_qa_fixes absent)'
        add(sid, pid, 'resolution', f'{hist}. Duvet art at 51 dpi; 2x upscale ~102 dpi (REWORK). d6_qa_fixes options: {opts}. Native detail still below 150 dpi.',
            f"{fx_ev}; winstar-recovery/regenerated/regeneration_register_24.csv", 'Owner', BO if fixes else RW,
            'Owner chooses option A (smaller motif) / B (AI x4 upscale) / regenerate at 4k', art_swap(sid, pid, fixes[0]['file'] if fixes else f),
            'winstar-recovery regeneration_register_24 + d6_qa_fixes (newer)')
        continue
    if qa == 'FAIL':
        x = fixes[0] if fixes else None
        if not x:
            add(sid, pid, dtype, f'{hist}. Repaired-art QA FAIL: {issues[:150]}. Fix in progress.', f, 'Claude', RW, 'Finish fix and re-QA', art_swap(sid, pid, f), 'winstar-recovery repaired_art_qa')
        elif x['qa_status'] == 'PASS':
            add(sid, pid, dtype, f"{hist}. Repaired-art QA FAIL ({issues[:80]}) superseded by d6_qa_fixes PASS: {x['fix_applied'][:90]}.",
                f'{fx_ev}', 'Owner', VR, 'Owner go-live approval (product-specific)', art_swap(sid, pid, x['file']), 'winstar-recovery repaired_art_qa + d6_qa_fixes (newer)')
        else:
            add(sid, pid, 'resolution', f"{hist}. Repaired-art QA FAIL ({issues[:80]}); d6_qa_fixes WARN: {x['fix_applied'][:70]}.",
                fx_ev, 'Owner', BO, 'Owner chooses: accept AI upscale / shrink motif / regenerate', art_swap(sid, pid, x['file']), 'winstar-recovery repaired_art_qa + d6_qa_fixes (newer)')
        continue
    warn = ''
    if qa in ('WARN', 'PASS-WARN'):
        warn = f' WARN: {issues[:140]}'
    sup = ''
    if ra and ra.get('superseded'):
        sup = f" Earlier local fix FAILED and is superseded by {rg['file'] if rg else 'regenerated file'}."
    add(sid, pid, dtype, f"{hist}. Fixed via {ws}; independent QA {qa}.{sup}{warn}", f"{f}; {ba}; {after}", 'Owner', VR,
        'Owner go-live approval (product-specific)', art_swap(sid, pid, f), 'D6 queue + winstar-recovery ' + ('regeneration_register_24' if rg else 'repaired_art_qa'))
    dup = sr.get(pid, {}).get('flags', '')
    if 'DUPLICATE_LISTING' in dup:
        add(sid, pid, 'duplicate_listing', f"Sales register flags DUPLICATE_LISTING ({sr[pid]['flags']}); register note: {sr[pid]['reason'][:130]}", 'Winstar_Sales_Readiness_Register.csv flags; Quality Register §8f/§8g/§8k/§8p',
            'Owner', BO, 'Owner picks which listing to keep (or confirms intentional)', f'printify-unpublish-product shop {sid} for the redundant member', 'Sales Readiness Register')

# wording/repaired-art duplicate flags for wording rows (D6 products with dup flags handled above only in non-wording branches)
have = {(r['product_id'], r['defect_type']) for r in rows}
for pid in queue:
    fl = sr.get(pid, {}).get('flags', '')
    if 'DUPLICATE_LISTING' in fl and (pid, 'duplicate_listing') not in have and pid != '69b0212c4fead7b1ce06b69e':
        add(queue[pid]['shop_id'], pid, 'duplicate_listing', f"Sales register flags DUPLICATE_LISTING ({sr[pid]['flags']}); register note: {sr[pid]['reason'][:130]}", 'Winstar_Sales_Readiness_Register.csv flags; Quality Register §8f/§8g/§8k/§8p',
            'Owner', BO, 'Owner picks which listing to keep (or confirms size-variant pair is intentional)', f"printify-unpublish-product shop {queue[pid]['shop_id']} for the redundant member", 'Sales Readiness Register')

# ---------------- non-D6 items from the Sales Readiness Register ----------------
for pid, r in sr.items():
    if pid in queue:
        continue
    sid, fl, b = r['shop_id'], r['flags'], r['bucket']
    if 'PRICE_LOSS' in fl:
        add(sid, pid, 'profitability', 'Wall Tapestry flat $30.99 on all 8 sizes; 68x80 loses $5.06, 88x104 loses $16.63 per sale before shipping '
            '(art already fixed live). Margin also depends on D2 (who pays shipping).',
            'reports/Winstar_Tapestry_Pricing_Correction_Table.csv; reports/Winstar_Tapestry_Duffel_Profitability_Evidence.md; Owner Decision D1/D2',
            'Owner', BO, 'Owner answers D1 (A/B/C) and D2', f'printify-set-product-prices shop {sid} product {pid}: 8 variants per correction table option A or B (or disable 68x80 and 88x104 variants), then re-read to verify', 'Sales Readiness Register + Decision Register D1')
    if 'PLATFORM_BLOCKED' in fl:
        add(sid, pid, 'artwork', 'Live listing still prints a grey checkerboard background. Owner approved the swap and corrected art is staged, but Printify '
            'rejects the update (48 retired variant IDs on the product).', 'reports/Printify_Support_Packet_Checkerboard_Legacy_Variants.md; Decision Register D4; Quality Register line 119',
            'Owner', BT, 'Owner submits the Printify support ticket (D4a); if no answer by 2026-11-24 choose D4(d) unpublish',
            f'printify-upsert-product shop {sid} product {pid}: swap to staged corrected image (blocked by platform until support clears retired variants); or printify-unpublish-product', 'Sales Readiness Register + Decision Register D4')
    if b == 'UNKNOWN' and r['reason'].startswith('Artwork fixed; Printify record has no sales-channel link'):
        add(sid, pid, 'marketplace_sync', 'Duffel bag: artwork fixed, ~45% margin, but Printify has no Shopify link, so it may not be buyable.',
            'Decision Register D3; Sales Readiness Register', 'Owner', BO, 'Owner answers D3 (check Shopify admin first, option a)',
            f'printify-publish-product shop {sid} product {pid} (only if absent from Shopify admin)', 'Sales Readiness Register + Decision Register D3')
    if b == 'HOLD':
        add(sid, pid, 'IP', 'TEXACO (Chevron-registered) trademark artwork on live Matte Canvas. Owner kept it on 2026-11-18; D7 optional revisit open. '
            'Replacement art (2 Higgsfield variants) NOT inspected: image host blocked; star emblem needs trademark screen.',
            'Quality Register Item 2 (line 1253); Decision Register D7; work/d7_texaco_replacement/README.md', 'Owner', BO,
            'Owner answers D7 (keep / unpublish); replacement art must be downloaded and trademark-screened before use',
            f'printify-unpublish-product shop {sid} product {pid}; or printify-upload-image + upsert-product with screened replacement art + publish', 'Sales Readiness Register + Decision Register D7')
    if 'DUPLICATE_LISTING' in fl:
        gap = ' Neither member confirmed live (no channel link) - also part of the D5 verification gap.' if b == 'UNKNOWN' else ''
        pillow = ' Same art/blueprint, different declared pillow size - may be an intentional size split (YELLOW in register).' if 'Pillow' in r['title'] else ''
        add(sid, pid, 'duplicate_listing', f'True duplicate listing (same artwork + blueprint as another listing in this shop).{pillow}{gap}',
            'Winstar_Sales_Readiness_Register.csv flags; Quality Register §5a (eBay), §8d/§8e (Etsy), §8f/§8k (Shopify)', 'Owner', BO,
            'Owner picks which member of the pair/cluster to keep' + (' (after D5 export)' if sid in ('28059412',) else ''),
            f'printify-unpublish-product shop {sid} product {pid} if it is the redundant member', 'Sales Readiness Register + Quality Register')

# Amazon duplicate pairs NOT covered by the owner's "keep all 7" decision (pairs #1, #9, #10, #11 in §8a)
AMZ = [('#1', '6ae41f6ae88b7e964c0e7380', '6ae414e0e88b7e964c0e72ed', 'neither live'),
       ('#9', '6ae41f72e88b7e964c0e738a', '6ae414eaf755b251850ceb05', 'live status unclear'),
       ('#10', '6ae41f68e88b7e964c0e737e', '6adea7d6853b5615b805ead5', 'only 6adea7d6 live (ASIN B0HPN22XVP)'),
       ('#11', '6ae414e0e88b7e964c0e72ee', '6ae41f6ce88b7e964c0e7383', 'only 6ae414e0...72ee live (ASIN B0HPSD8268)')]
for n, a, b2, st in AMZ:
    for pid, other in ((a, b2), (b2, a)):
        add('29451844', pid, 'duplicate_listing', f'Amazon true-duplicate pair {n} with {other} ({st}). Not covered by owner decision D-3F2G504W3Y, which kept only the 7 both-live pairs.',
            'Quality Register §8a pair table (line 2261-2280); Sales Readiness Register', 'Owner', BO,
            'After D5 Seller Central export, owner picks which record to keep', f'printify-unpublish-product shop 29451844 product {pid} if redundant (or delete unlinked draft record)', 'Quality Register §8a')

# ---------------- write CSV (dedupe on key) ----------------
seen = {}
for r in rows:
    k = (r['shop_id'], r['product_id'], r['defect_type'])
    if k in seen:
        seen[k]['description'] += ' | ALSO: ' + r['description']
        continue
    seen[k] = r
rows = list(seen.values())
cols = ['shop_id', 'shop_name', 'product_id', 'title', 'defect_type', 'description', 'evidence_path_or_ref', 'owner',
        'final_status', 'next_action', 'live_action_needed', 'source']
rows.sort(key=lambda r: (list(SHOPS).index(r['shop_id']), r['final_status'], r['defect_type'], r['product_id']))
with open(OUT + 'master_defects.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)

# ---------------- stats ----------------
print('rows', len(rows), 'unique products', len({(r['shop_id'], r['product_id']) for r in rows}))
print(C.Counter(r['final_status'] for r in rows))
print(C.Counter(r['defect_type'] for r in rows))
for sid in SHOPS:
    rs = [r for r in rows if r['shop_id'] == sid]
    print(sid, len(rs), len({r['product_id'] for r in rs}), dict(C.Counter(r['final_status'] for r in rs)))
    # product-level worst status
import json
json.dump({'qfix_products': len(qfix), 'qfix_rows': sum(len(v) for v in qfix.values())}, open('/tmp/claude-0/-home-user-crowned-co-data/c0034cf5-75d5-55a9-aa8f-5993db7544c2/scratchpad/stats.json', 'w'))
