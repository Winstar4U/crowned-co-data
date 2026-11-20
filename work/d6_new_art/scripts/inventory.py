import csv, hashlib, json, os, re, sys
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

W = '/home/user/crowned-co-data/work'
OUT = W + '/d6_new_art'
LOCAL = {'white_box', 'checkerboard', 'low_contrast'}


def classify(n):
    u = n
    if re.search(r'BLANK \(no text\)|blank street-sign|EMPTY green ribbon|EMPTY', u):
        return 'blank_text'
    if 'ENGRAVING' in u:
        return 'engraving'
    if 'duplicated-word' in u:
        return 'garbled_text'
    if '400x400' in u:
        return 'low_res'
    if re.search(r'checkerboard', u, re.I):
        return 'checkerboard'
    if re.search(r'low[- ]contrast', u, re.I):
        return 'low_contrast'
    if 'opaque WHITE background' in u:
        return 'white_box'
    return 'other'


def sha1(p):
    h = hashlib.sha1()
    with open(p, 'rb') as f:
        for c in iter(lambda: f.read(1 << 20), b''):
            h.update(c)
    return h.hexdigest()


rows = []
for i in range(1, 11):
    f = f'{W}/d6_batch{i}/batch{i}_results.csv'
    for r in csv.DictReader(l for l in open(f) if not l.startswith('#')):
        if r['status'] != 'NEEDS_NEW_ART':
            continue
        pid = r['product_id']
        cat = r.get('new_art_category') or classify(r['notes'])
        pdir = f'{W}/d6_batch{i}/{pid}'
        orig = f'{pdir}/original.png'
        pl = json.load(open(f'{pdir}/placement.json'))
        if os.path.exists(orig):
            s = sha1(orig)
            im = Image.open(orig)
            dims = f'{im.width}x{im.height}'
            mode = im.mode
        else:
            s, dims, mode = 'MISSING', '', ''
        route = 'LOCAL' if cat in LOCAL else 'GENERATE'
        rows.append(dict(batch=i, product_id=pid, title=r['title'], blueprint=r['blueprint_id'],
                         category=cat, sha1=s, fix_route=route, src_px=dims, src_mode=mode,
                         image_name=pl.get('image_name', ''), decoration=pl.get('decoration_method', ''),
                         source_file=orig, notes=r['notes'][:400]))

os.makedirs(OUT, exist_ok=True)
with open(OUT + '/inventory.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)
print(len(rows), 'rows')
