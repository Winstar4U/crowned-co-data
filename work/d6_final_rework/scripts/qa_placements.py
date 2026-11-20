"""Independent QA of the 224 READY_FOR_REVIEW placement proposals.
Recomputes content bbox from original.png and checks proposed placement against every
enabled placeholder; renders an after-preview per product. Read-only; no Printify writes."""
import csv,json,glob,re,hashlib,sys
import numpy as np
from PIL import Image,ImageDraw
Image.MAX_IMAGE_PIXELS=None
W='/home/user/winstar4u/crowned-co-data/work'
OUT='/home/user/my-projects/winstar-recovery/qa'
IP=re.compile(r'\b(?:grinch|disney|texaco|coca|pepsi|marvel|star wars|nfl|nba|harley|jack daniel|hallmark|peanuts|snoopy|rudolph|frosty|charlie brown|elf on the shelf|buddy the elf|home alone|griswold|national lampoon|budweiser|coors|starbucks)\b',re.I)
rows=[]
for i in range(1,11):
    for r in csv.DictReader(l for l in open(f'{W}/d6_batch{i}/batch{i}_results.csv') if not l.startswith('#')):
        if r['status']=='READY_FOR_REVIEW': r['batch']=i; rows.append(r)
def bbox(im):
    a=np.array(im.convert('RGBA'))
    if a[...,3].min()<250: m=a[...,3]>16; mode='alpha'
    else:
        c=a[0,0,:3].astype(int); m=np.abs(a[...,:3].astype(int)-c).sum(2)>40; mode='opaque_bg'
    ys,xs=np.where(m); h,w=m.shape
    return (xs.min()/w,ys.min()/h,(xs.max()+1)/w,(ys.max()+1)/h),mode
res=[]
for r in rows:
    p=r['product_id']; d=f"{W}/d6_batch{r['batch']}/{p}"
    j=json.load(open(d+'/placement.json')); im=Image.open(d+'/original.png')
    iw,ih=im.size; (bx0,by0,bx1,by1),mode=bbox(im)
    pr=j['proposed']; issues=[]; worst_in=1.0; min_ratio=9
    if j['product_id']!=p: issues.append('MAPPING: placement.json product_id mismatch')
    if list(j['image_px'])!=[iw,ih]: issues.append(f'MAPPING: image_px {j["image_px"]} != file {iw}x{ih}')
    if j.get('shop_id')!=r['shop_id']: issues.append('MAPPING: shop mismatch')
    for vid,(W_,H_) in j['placeholders'].items():
        aw=pr['scale']*W_; ah=aw*ih/iw; cx=pr['x']*W_; cy=pr['y']*H_
        x0=cx-aw/2+bx0*aw; x1=cx-aw/2+bx1*aw; y0=cy-ah/2+by0*ah; y1=cy-ah/2+by1*ah
        ix=max(0,min(x1,W_)-max(x0,0)); iy=max(0,min(y1,H_)-max(y0,0))
        frac=ix*iy/((x1-x0)*(y1-y0)); worst_in=min(worst_in,frac)
        min_ratio=min(min_ratio,iw/aw)
    sa=set(j.get('safe_area_source',{}).values())
    if worst_in<0.999: issues.append(f'GEOMETRY: only {worst_in:.1%} of content inside placeholder')
    if min_ratio<0.33: issues.append(f'RESOLUTION: src/print px ratio {min_ratio:.2f} (<0.33)')
    elif min_ratio<0.5: issues.append(f'RESOLUTION-WARN: src/print px ratio {min_ratio:.2f} (<0.5)')
    tr=j.get('transparency',r.get('transparency_ok',''))
    if mode=='opaque_bg':
        c=np.array(im.convert('RGB'))[0,0]
        white=c.min()>235
        dec=(j.get('decoration_method') or '').lower()
        if white and ('sublimation' in dec or 'uv' in dec or dec in ('','sublimation')):
            pass  # white bg on white-substrate sublimation product prints invisibly
        else:
            issues.append(f'TRANSPARENCY-WARN: opaque background rgb{tuple(int(v) for v in c)} on {dec or "unknown"} product; verify blank colour')
    if IP.search(r['title']+' '+j.get('image_name','')): issues.append('IP: trademark keyword in title/filename: '+IP.search(r['title']+' '+j.get('image_name','')).group(0))
    if sa-{'rect'}: shape_note='non-rect safe area ('+','.join(sorted(sa-{'rect'}))+'): rect bounds verified independently; shape fit taken from prior verify_inside_safe_frac=%s'%min(j.get('verify_inside_safe_frac',{1:0}).values())
    else: shape_note=''
    hard=[x for x in issues if not x.split(':')[0].endswith('WARN')]
    status='FAIL' if hard else ('WARN' if issues or shape_note else 'PASS')
    # render after-preview on first placeholder
    vid,(W_,H_)=next(iter(j['placeholders'].items())); s=360/max(W_,H_)
    cv=Image.new('RGB',(int(W_*s)+40,int(H_*s)+60),(120,120,125)); dr=ImageDraw.Draw(cv)
    dr.rectangle([20,20,20+W_*s,20+H_*s],fill=(238,238,238))
    aw=pr['scale']*W_*s; ah=aw*ih/iw
    if aw>2 and ah>2:
        a=im.convert('RGBA').resize((max(1,int(aw)),max(1,int(ah))))
        cv.paste(a,(int(20+pr['x']*W_*s-aw/2),int(20+pr['y']*H_*s-ah/2)),a)
    dr.rectangle([20,20,20+W_*s,20+H_*s],outline=(255,0,0))
    dr.text((4,cv.height-36),f'{p} {status}',fill='white'); dr.text((4,cv.height-20),r['title'][:58],fill='white')
    fn=f'{OUT}/placement_renders/{p}.png'; cv.save(fn)
    res.append(dict(product_id=p,shop_id=r['shop_id'],batch=r['batch'],title=r['title'],blueprint=r['blueprint_id'],
        decoration=j.get('decoration_method'),current=r['current_xyscale'],proposed=r['proposed_xyscale'],
        content_inside_min=f'{worst_in:.4f}',src_print_px_ratio_min=f'{min_ratio:.2f}',bg_mode=mode,
        prior_verify=r['verify_pass'],qa_status=status,issues=' | '.join(issues),shape_note=shape_note,
        defect_before=j.get('defect_note',''),prior_before_after=f'crowned-co-data/work/d6_batch{r["batch"]}/{p}/before_after.png',
        independent_after_render=f'winstar-recovery/qa/placement_renders/{p}.png'))
k=list(res[0].keys())
with open(f'{OUT}/placement_qa_224.csv','w',newline='') as f:
    w=csv.DictWriter(f,k); w.writeheader(); w.writerows(res)
from collections import Counter
print(len(res),Counter(x['qa_status'] for x in res))
for x in res:
    if x['qa_status']!='PASS': print(x['product_id'],x['qa_status'],x['issues'][:150],'||',x['shape_note'][:90])
