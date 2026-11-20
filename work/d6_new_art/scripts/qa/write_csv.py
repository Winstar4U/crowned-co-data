import json, csv
A = json.load(open('qa_a.json')); B = json.load(open('qa_b.json'))
OUT = '/home/user/crowned-co-data/work/d6_new_art/qa_results.csv'
# visual verdicts (from verify sheets + 1:1 crops reviewed by eye)
VIS = {
 '83869020': ('QA_FAIL', 'bright light-source core at top centre was removed as background: ragged see-through hole/spikes cut into the golden ray panel down to the trumpet (shows blank colour on black backpack); needs gated flood that protects the ray panel or regenerated art'),
 '53299362': ('QA_FAIL', "text not acceptable: dark outline wraps the faded/broken lower half of 'HAPPY' in the grey script and turns the fragments into blobs - 'HAPPY' reads garbled; needs regenerated art"),
 '643045f5@dark': ('QA_WARN', 'baked checker patch under the CHRISTMAS arch (behind the light garland) is now a see-through hole with leftover cream fragments - looks blotchy on the BLACK blank (fine on white sublimation blanks)'),
 '661174a2': ('QA_WARN', 'art touches canvas bottom/side edge in source so the added cream outline is cut flat there (14% border opaque); legible otherwise - pad canvas before outlining'),
 '9e3db274': ('QA_WARN', "headline touches top canvas edge so the outline is cut flat at the top (6% border opaque); legible otherwise"),
 'd9c3157b': ('QA_WARN', "'CHRISTMAS' touches top canvas edge so the outline is cut flat at the top (12% border opaque); legible otherwise"),
 '350d4292': ('QA_WARN', 'art touches left/right canvas edges so the outline is cut flat at the sides (10% border opaque); legible otherwise'),
 'e69e8b51': ('QA_WARN', 'minor: outline clipped where the C and the bottom scroll touch the canvas edge (5% border opaque)'),
 '3243882c': ('QA_WARN', "minor residue: halftone-dot fragments left of 'HA' remain as a small white speck cluster visible on black"),
 'a0e42e17': ('QA_WARN', 'contrast: brown/olive art on mid-gray apron - 74% of opaque px under 2:1 vs gray; reads muted (fine on lighter/darker aprons)'),
 '873af255': ('QA_WARN', 'design-pixel loss 1.61% (>1%) = cream checker backing remnants cleared from behind the scroll text and checker-tile edges; core loss 0%, text intact'),
}
NOTE_OK = {
 'low_contrast': 'outline/stroke fix; text unchanged; legible on blank',
 'white_box': 'bg removed cleanly; text unchanged',
 'checkerboard': 'checker removed; text unchanged',
}
B_VIS = {
 '96e7dc4c': ('QA_PASS', "v2: white fills of 'EX' (and letter bodies on that line) restored from the original inside the letter outlines; no holes; text unchanged"),
 'd118595b': ('QA_WARN', 'v2: punched-out papers/mug/calendar/to-do rebuilt as solid off-white (246,243,236) behind the original ink; enclosed checker strip right of CANCELED cleared. Loss 1.74% (>1%) = tiny distress-texture specks inside letters that were already cleared in v1 (print as dark distress dots, core loss 0%); paper shading is flat reconstruction - owner eyeball'),
 '46f859cc': ('QA_PASS', 'v2: enclosed white background pockets (hoof/muzzle, antler gaps etc., 27 regions) removed with 2px unmix feather; eye whites and nose highlight kept'),
 '78de4579': ('QA_PASS', 'v2: same file content as 46f859cc v2 (identical source art) - pockets removed, eye whites kept'),
 '570a81cd': ('QA_PASS', 'v2 built from clean FIXED3 873af255 (1702x2048, pom-pom intact) + uniform 14px cream backing under the scroll text so it reads on dark blanks; hat unchanged; text unchanged'),
 'a897d056': ('QA_PASS', 'v2: all near-white keyed out (wreath centre and letter counters now transparent) + uniform 12px cream outline so dark green/red reads on black; text unchanged (outline is a style addition)'),
 'b0b97665': ('QA_PASS', 'v2: lost receipt paper rebuilt as solid off-white behind the receipt print (31 regions, 231k px); receipt ink preserved; text unchanged'),
 '1702519f': ('QA_WARN', 'v2: soft white-key (glow -> semi-transparent) + enclosed star highlight restored; stable/figures/text intact. Loss 5.13% at alpha<128 is the soft glow (only 0.02% fully removed); the white glow behind the star/rays cannot reproduce on black, so the star prints without its glow and with a slightly dark rim'),
}
def dpi_status(d):
    return 'QA_FAIL' if d < 100 else ('QA_WARN' if d < 150 else 'QA_PASS')
rank = {'QA_PASS': 0, 'QA_WARN': 1, 'QA_FAIL': 2}
rows = []
for part, D in (('A', A), ('B', B)):
    for pid, o in D.items():
        s8 = o['sha'][:8]
        st, notes = 'QA_PASS', []
        if part == 'A':
            dark = any(n.startswith(('black',)) for n in o['blanks'])
            key = s8 + '@dark' if (s8 == '643045f5' and dark) else s8
            if key in VIS:
                st, n = VIS[key]; notes.append(n)
            else:
                notes.append(NOTE_OK[o['cat']])
        else:
            st, n = B_VIS[s8]; notes.append(n)
        ds = dpi_status(o['dpi'])
        if ds != 'QA_PASS':
            notes.append(f"print size: {o['dpi']:.0f} dpi on largest variant {o['dpi_var'][0]} ({o['dpi_var'][1]}x{o['dpi_var'][2]} px placeholder, scale {o['dpi_var'][3]})" + (' < 100 dpi' if ds == 'QA_FAIL' else ' (100-150 dpi)'))
            if rank[ds] > rank[st]: st = ds
        if o['loss_pct'] >= 1.0 and st == 'QA_PASS':
            st = 'QA_WARN'; notes.append(f"loss {o['loss_pct']}%")
        chk = 'none' if o['tile_E'] < 0.002 and o['speck_frac'] < 0.001 else 'trace'
        if s8 == '3243882c': chk = 'minor specks'
        if s8 == '643045f5': chk = 'enclosed patch remnants'
        chk += f" (tileE {o['tile_E']} vs orig {o['tile_E_orig']}; isolated specks {o['speck_n']}, {o['speck_frac']*100:.3f}% area)"
        cn = '; '.join(f"{k}: {v*100:.0f}% px <2:1" for k, v in o['lowc'].items())
        rows.append(dict(product_id=pid, sha1=o['sha'], file_used=o['file'], category=o['cat'], qa_status=st,
                         dpi_largest_variant=round(o['dpi']), design_pixel_loss_pct=o['loss_pct'], checker_residue=chk,
                         contrast_note=cn, notes=('PART ' + part + ' | ') + ' | '.join(notes) + f" | edge opaque {o['edge_opaque']*100:.1f}%, core loss {o['core_loss_pct']}% | render verify/{pid}.png"))
with open(OUT, 'w', newline='') as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
import collections
for part, D in (('A', A), ('B', B)):
    c = collections.Counter(r['qa_status'] for r in rows if r['product_id'] in D); print(part, len(D), dict(c))
    for r in rows:
        if r['product_id'] in D and r['qa_status'] != 'QA_PASS':
            print(' ', r['qa_status'], r['product_id'], r['sha1'][:8], r['dpi_largest_variant'], r['notes'][:150])
