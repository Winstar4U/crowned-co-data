import json,glob,hashlib,csv,sys
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
rows=[]
for d in sorted(glob.glob('/home/user/crowned-co-data/work/d6_batch*/6ac*')):
    try: j=json.load(open(d+'/placement.json'))
    except Exception: continue
    f=d+'/original.png'
    try:
        b=open(f,'rb').read(); s=hashlib.sha1(b).hexdigest(); im=Image.open(f); px=im.size
    except Exception: s='';px=('','')
    rows.append(dict(pid=j['product_id'],dir=d,bp=j.get('blueprint_id'),image_id=j.get('image_id'),name=j.get('image_name'),w=px[0],h=px[1],sha1=s,title=j['title'][:60]))
w=csv.DictWriter(open(sys.argv[1],'w',newline=''),list(rows[0]));w.writeheader();w.writerows(rows)
print(len(rows))
