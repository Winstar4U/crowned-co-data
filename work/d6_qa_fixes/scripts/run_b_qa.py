"""Cross-check: run B's ORIGINAL qa/qa_placements.py source (only paths and the batch range patched) on every new
placement JSON. Each print-area group becomes its own synthetic 'batch' so B's single-'proposed' logic is applied
to exactly the variants that group covers. Usage: python3 -I run_b_qa.py <tmpdir>"""
import json, glob, os, sys, csv, re
T = sys.argv[1]; O = '/home/user/crowned-co-data/work/d6_qa_fixes'; BSRC = '/home/user/winstar4u/my-projects/winstar-recovery/qa/qa_placements.py'
os.makedirs(T + '/out/placement_renders', exist_ok=True); n = 0; index = []
for f in sorted(glob.glob(O + '/placements/*.json')):
    d = json.load(open(f)); art = '/home/user/crowned-co-data/' + d['art']['file']
    from PIL import Image
    iw, ih = Image.open(art).size
    for g in d['print_areas']:
        n += 1; bd = f'{T}/d6_batch{n}/{d["product_id"]}'; os.makedirs(bd, exist_ok=True)
        if os.path.lexists(bd + '/original.png'): os.remove(bd + '/original.png')
        os.symlink(art, bd + '/original.png')
        ph = {str(v): d['per_variant_qa'] and None for v in g['variant_ids']}
        src_ph = json.load(open(glob.glob(f'/home/user/crowned-co-data/work/d6_batch*/{d["product_id"]}/placement.json')[0]))['placeholders']
        json.dump(dict(product_id=d['product_id'], shop_id=d['shop_id'], image_px=[iw, ih], decoration_method=d['decoration_method'], proposed=g['placement'],
                       placeholders={str(v): src_ph[str(v)] for v in g['variant_ids']}, image_name=os.path.basename(art)), open(bd + '/placement.json', 'w'))
        with open(f'{T}/d6_batch{n}/batch{n}_results.csv', 'w', newline='') as fh:
            w = csv.DictWriter(fh, ['product_id', 'shop_id', 'title', 'blueprint_id', 'status', 'current_xyscale', 'proposed_xyscale', 'verify_pass', 'transparency_ok'])
            w.writeheader(); w.writerow(dict(product_id=d['product_id'], shop_id=d['shop_id'], title=d['title'], blueprint_id=d['blueprint_id'], status='READY_FOR_REVIEW',
                                             current_xyscale='', proposed_xyscale=json.dumps(g['placement']), verify_pass='', transparency_ok=''))
        index.append((n, os.path.basename(f), g['variant_ids']))
src = open(BSRC).read()
src = src.replace("W='/home/user/winstar4u/crowned-co-data/work'", f"W={T!r}").replace("OUT='/home/user/my-projects/winstar-recovery/qa'", f"OUT={T + '/out'!r}").replace('range(1,11)', f'range(1,{n + 1})')
assert f"W={T!r}" in src and 'range(1,11)' not in src
exec(compile(src, 'qa_placements.py(B, paths patched)', 'exec'), {'__name__': '__main__'})
res = list(csv.DictReader(open(T + '/out/placement_qa_224.csv')))
for (i, fn, vids), r in zip(index, res):
    print(f"{fn:42s} variants {','.join(map(str, vids)):32s} B:{r['qa_status']:4s} inside {r['content_inside_min']} ratio {r['src_print_px_ratio_min']} {r['issues'][:70]}")
