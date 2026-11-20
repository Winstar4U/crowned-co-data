import csv, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import vlib as V
import numpy as np
g = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gather.json')))
res = list(csv.DictReader(open(V.OUT + '/results.csv')))
inv = {r['product_id']: r for r in csv.DictReader(open(V.OUT + '/inventory.csv'))}
rows = [r for r in res if r['fix_status'] == 'FIXED_LOCAL']
cache = {}
out = {}
for r in rows:
    pid, sha = r['product_id'], r['sha1']
    i = inv[pid]
    pl = json.load(open(os.path.join(os.path.dirname(i['source_file']), 'placement.json')))
    if sha not in cache:
        o = V.load(i['source_file']); f = V.load(r['output_file'])
        m = V.qa_metrics(o, f, r['category'])
        cache[sha] = (o, f, m)
    o, f, m = cache[sha]
    blanks = V.blanks_for(i['blueprint'], pl)
    dpi = V.eff_dpi(f.shape[1], pl)
    cl = {n: round(V.contrast_low_frac(f, c), 3) for n, c in blanks}
    cl0 = {n: round(V.contrast_low_frac(o, c), 3) for n, c in blanks}
    line = (f"dpi {dpi[0]:.0f} (var {dpi[1]} {dpi[2]}x{dpi[3]} sc {dpi[4]}) | loss {m['loss_pct']}% core {m['core_loss_pct']}% | tileE {m['tile_E']} (orig {m['tile_E_orig']}) | "
            f"specks {m['speck_n']}/{m['speck_frac']} nl{m['speck_nl']} | edge {m['edge_opaque']} | lowC {cl}")
    V.render(pid, f"{pid} bp{i['blueprint']} {r['category']} sha1 {sha[:10]} {f.shape[1]}x{f.shape[0]} file fixed/{os.path.basename(r['output_file'])}", o, f, blanks, m['lost_mask'], line)
    mm = {k: v for k, v in m.items() if k != 'lost_mask'}
    out[pid] = dict(sha=sha, file=r['output_file'], cat=r['category'], bp=i['blueprint'], dpi=round(dpi[0], 1), dpi_var=dpi[1:],
                    lowc=cl, lowc_orig=cl0, blanks=[n for n, _ in blanks], **mm)
    print(pid, sha[:8], line, flush=True)
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'qa_a.json'), 'w'), indent=1)
