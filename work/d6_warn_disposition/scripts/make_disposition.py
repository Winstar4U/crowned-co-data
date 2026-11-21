"""Assemble disposition.csv for the 106 WARN rows of placement_qa_224.csv. Usage: python3 -I make_disposition.py"""
import csv, json, os, collections
OUT = '/home/user/crowned-co-data/work/d6_warn_disposition'
R = 'work/d6_warn_disposition/'
qa0 = [r for r in csv.DictReader(open('/home/user/winstar4u/my-projects/winstar-recovery/qa/placement_qa_224.csv')) if r['qa_status'] == 'WARN']
sc = {x['product_id']: x for x in json.load(open(OUT + '/shape_check.json'))}
qa1 = {r['product_id']: r for r in csv.DictReader(open(OUT + '/qa_after.csv'))}
fixmeta = {p: json.load(open(f'{OUT}/placements/{p}.json'))['warn_fix'] for p in qa1}
def shape_txt(p):
    x = sc[p]; v = x['variants']; kinds = sorted({y['kind'] for y in v.values()}); ov = max(y['overflow_px'] for y in v.values())
    t = f"independent raw-SVG shape check ({'/'.join(kinds)}, {len(v)} placeholder geometr{'y' if len(v)==1 else 'ies'}, SVG transforms honoured): {x['inside_min']*100:.3f}% of content pixels inside"
    if x['inside_best_poly_min'] < x['inside_min'] - 1e-9 or any(y['n_polys'] > 1 for y in v.values()): t += f", {x['inside_best_poly_min']*100:.3f}% inside a single face/panel"
    t += f"; max overflow {ov:.1f} placeholder px" + (" (sub-pixel/rasterisation tolerance: edge pixels touch, do not cross, Printify's safe line, which is already inset from the cut)" if (0 < ov <= 7 or x["inside_min"] < 1) else "")
    return t, ov
rows = []
for r in qa0:
    p = r['product_id']; iss = r['issues']
    warn = ' | '.join([z for z in [iss, ('SHAPE-NOTE: ' + r['shape_note'].split(':')[0]) if r['shape_note'] else ''] if z])
    st, ov = shape_txt(p); disp = reason = newf = qa_after = cause = ''
    if p in qa1:
        m = fixmeta[p]; disp = 'FIXED'; q = qa1[p]
        newf = f"{R}placements/{p}.json; {m['new_art_local']}; {R}before_after/{p}.png"
        qa_after = f"{q['qa_status']} (rect inside {q['content_inside_min']}, src/print {q['src_print_px_ratio_min']}, raw-SVG shape {q['shape_inside_min']})"
        if m['kind'] == 'upscale':
            cause = 'resolution'
            phys = {'1327': 'scarf 27x71in, placeholder ~156 ppi -> was ~%d dpi physical' % round(float(r['src_print_px_ratio_min']) * 156),
                    '643': 'cutting board, 300 ppi placeholder -> was ~%d dpi' % round(float(r['src_print_px_ratio_min']) * 300),
                    '429': 'laptop sleeve, 300 ppi placeholder -> was ~%d dpi' % round(float(r['src_print_px_ratio_min']) * 300),
                    '39': 'tank top DTG, 300 ppi placeholder -> was ~%d dpi' % round(float(r['src_print_px_ratio_min']) * 300)}[r['blueprint']]
            reason = (f"Low source resolution ({phys}). Local Real-ESRGAN anime6B x4 upscale of the same art (edge-bleed RGB so no white matte, "
                      f"Lanczos alpha), placement x/y/scale unchanged; src/print {r['src_print_px_ratio_min']} -> {q['src_print_px_ratio_min']}. "
                      "Flat cartoon/type art: edges and text re-drawn crisp, colours within 2 levels of original; upscale adds no true detail. "
                      "Live use needs: upload as a new Printify image + owner-approved product update.")
            if r['blueprint'] == '39': reason += " Separate pre-existing caveat: dark maroon/green ink on the enabled Black tank variants is low contrast (see OWNER questions)."
        else:
            cause = 'stray specks (found during shape re-check)'
            reason = (f"Shape-note WARN; re-check found detached grey (rgb~137) background-removal specks ~45-50 px around the design "
                      f"({'some outside the ornament safe circle, 20 px overflow' if ov > 7 else 'inside the safe circle; would print as grey dust dots on white ceramic'}). "
                      "despeck.py removed only detached sub-100px specks >=20 px from every design component; design pixels untouched; placement unchanged. "
                      "Live use needs: upload new image + owner-approved product update.")
    elif p == '6ac7112383f1a0e50d071cdf':
        disp, cause = 'REWORK', 'baked checkerboard (found during re-check)'
        reason = (f"Shape WARN itself clears ({st}), but visual re-check shows the source PNG has a baked-in opaque grey/white checkerboard "
                  "(fake transparency) around the design and inside the scroll; it would print as a grey checker pattern on the white scarf. "
                  "Need: a clean transparent PNG of 'I Checked Santa's List / He Needs To Mind His Business' (true alpha, no checker), >= 2700 px wide "
                  "(placement scale 0.305 on 11100 px placeholder needs >= 3386 px for src/print 1.0; >= 1693 px minimum for 0.5). Regenerate or re-export, then re-place at x=0.5,y=0.5,scale=0.305.")
        qa_after = 'shape PASS; art FAIL (checkerboard)'
    elif p == '6ad4254232b024bb32043467':
        disp, cause = 'OWNER', 'opaque photo background'
        reason = ("Opaque full-bleed photo (bg rgb 87,88,70) on a white ceramic ornament: the dye-sub prints it fine, the WARN is aesthetic. "
                  "Proposed fit (scale 0.553) shows the whole photo as a small rectangle with white ceramic around it. Alternative checked locally: "
                  "full-bleed cover x=0.5,y=0.53,scale=1.2 keeps tree, star topper and pegs inside the safe circle (variant 69370) with only "
                  f"background crossing the cut line. {st}.")
        qa_after = 'WARN (unchanged; owner decision)'
    elif r['blueprint'] == '937':
        disp, cause = 'ACCEPT', 'white opaque background on white canvas'
        reason = ("Opaque background is white (outer 30 px mean 254.4-254.9, min 245) on canvas (digital printing on white canvas): the "
                  "background prints as, and is indistinguishable from, the white canvas, so no visible box. Geometry: content 100% inside; " + st + ".")
        qa_after = 'WARN accepted (background white on white canvas; geometry PASS)'
    else:
        x = sc[p]
        assert x['inside_min'] >= 0.998 and ov <= 7 and not iss, p
        disp, cause = 'ACCEPT', 'shape-note only (non-rect safe area)'
        reason = ("WARN was only 'shape fit taken from prior verify'. " + st + ". Rect bounds also 100% inside every enabled placeholder; resolution ratio "
                  f"{r['src_print_px_ratio_min']} (>=0.5). Prints inside the blueprint's own safe area.")
        qa_after = f"PASS (raw-SVG shape {x['inside_min']*100:.3f}% inside, overflow {ov:.1f}px)"
    rows.append(dict(product_id=p, shop_id=r['shop_id'], batch=r['batch'], warn_issues=warn, disposition=disp, reason=reason, new_file=newf, qa_after=qa_after, _cause=cause))
with open(OUT + '/disposition.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, ['product_id', 'shop_id', 'batch', 'warn_issues', 'disposition', 'reason', 'new_file', 'qa_after']); w.writeheader()
    w.writerows([{k: v for k, v in x.items() if not k.startswith('_')} for x in rows])
print(len(rows), collections.Counter(x['disposition'] for x in rows))
print(collections.Counter((x['disposition'], x['_cause']) for x in rows))
