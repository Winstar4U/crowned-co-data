import csv, glob, os
from PIL import Image
OUT = '/home/user/crowned-co-data/work/d6_new_art'
rows = list(csv.DictReader(open(OUT + '/inventory.csv')))
order = {'white_box': 0, 'checkerboard': 1, 'low_contrast': 2}
local = sorted([r for r in rows if r['fix_route'] == 'LOCAL'], key=lambda r: (order[r['category']], r['sha1']))
for f in glob.glob(OUT + '/contact_sheet_*.png'):
    os.remove(f)
PER = 8
for k in range(0, len(local), PER):
    ims = [Image.open(f"{OUT}/previews/{r['product_id']}.png") for r in local[k:k + PER]]
    w, h = ims[0].size
    sw, sh = w // 2, h // 2
    sheet = Image.new('RGB', (2 * sw + 6, 4 * (sh + 4)), (90, 90, 90))
    for j, im in enumerate(ims):
        sheet.paste(im.resize((sw, sh), Image.LANCZOS), ((j % 2) * (sw + 6), (j // 2) * (sh + 4)))
    sheet.save(f"{OUT}/contact_sheet_{k // PER + 1}.png")
    print(k // PER + 1, [r['product_id'][-6:] + ':' + r['sha1'][:6] for r in local[k:k + PER]])
