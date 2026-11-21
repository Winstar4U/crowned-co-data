import csv,json,glob,os,re,collections
W='/home/user/crowned-co-data/work'
inv={r['product_id']:r for r in csv.DictReader(open(W+'/d6_new_art/inventory.csv'))}
res={r['product_id']:r for r in csv.DictReader(open(W+'/d6_new_art/results.csv'))}
br={}
for f in glob.glob(W+'/d6_batch*/batch*_results.csv'):
    rows=[l for l in open(f) if not l.startswith('#')]
    for r in csv.DictReader(rows): br[r['product_id']]=r
cw=re.compile(r'\b(black|white|navy|gr[ae]y|heather|red|blue|green|pink|natural|cream|beige|brown|khaki|maroon|charcoal|clear|tan|ivory|sand|olive|purple|orange|yellow|mint|iron)\b[^|;,.]{0,25}',re.I)
out={}
for pid,r in res.items():
    if r['fix_status'] not in('FIXED_LOCAL','FAILED_LOCAL'):continue
    i=inv[pid]; pl=json.load(open(os.path.join(os.path.dirname(i['source_file']),'placement.json')))
    txt=' | '.join([i['notes'],str(pl.get('defect_note','')),' '.join(pl.get('notes',[])),br.get(pid,{}).get('notes',''),i['title']])
    cks=[k for k in pl if k.startswith('contrast_vs')]
    out[pid]=dict(status=r['fix_status'],sha=r['sha1'],cat=r['category'],bp=i['blueprint'],deco=i['decoration'],src=i['source_file'],
        ph=pl.get('placeholders'),prop=pl.get('proposed'),cur=pl.get('current'),ppvg=pl.get('proposed_per_variant_group'),
        cks={k:pl[k] for k in cks},colors=sorted(set(m.group(0).strip().lower()[:30] for m in cw.finditer(txt))))
json.dump(out,open('gather.json','w'),indent=1)
for pid,o in out.items():
    print(pid,o['status'][:5],o['sha'][:8],o['cat'][:6],o['bp'],o['deco'],list(o['cks'].keys()),o['colors'][:8], 'ppvg' if o['ppvg'] else '')
