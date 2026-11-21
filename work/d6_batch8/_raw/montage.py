import json,sys
from PIL import Image,ImageDraw
out=sys.argv[1]; ids=sys.argv[2].split(",") if len(sys.argv)>2 else None
seen={};order=[]
for l in open('products.jsonl'):
    p=json.loads(l); im=p['areas'][0]['images'][0]
    seen.setdefault(im['id'],[]).append(p['product_id'])
    if im['id'] not in order: order.append(im['id'])
info={}
for l in open('products.jsonl'):
    p=json.loads(l); im=p['areas'][0]['images'][0]; info[im['id']]=(im['name'],p['product_id'],im['width'],im['height'])
sel=[i for i in order if (ids is None or i in ids)]
T=640;tiles=[]
for iid in sel:
    name,pid,w,h=info[iid]
    a=Image.open(f'{pid}/original.png').convert('RGBA'); a.thumbnail((T,T))
    t=Image.new('RGB',(T,T+40),(120,60,140))
    t.paste(a,((T-a.width)//2,40+(T-a.height)//2),a)
    ImageDraw.Draw(t).rectangle([0,0,T,38],fill='black')
    ImageDraw.Draw(t).text((4,2),f"{name[:60]} {w}x{h}",fill='white')
    ImageDraw.Draw(t).text((4,20),",".join(x[-6:] for x in seen[iid]),fill='yellow')
    tiles.append(t)
cols=3;rows=(len(tiles)+cols-1)//cols
S=Image.new('RGB',(cols*(T+6),rows*(T+46)),'white')
for i,t in enumerate(tiles): S.paste(t,((i%cols)*(T+6),(i//cols)*(T+46)))
S.save(out); print(len(tiles))
