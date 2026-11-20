import json,sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import vlib as V, numpy as np
from scipy import ndimage as ndi
def flatwhite(f):
    rgb=f[...,:3]; mn,mx=rgb.min(-1),rgb.max(-1)
    m=(mn>=238)&(mx-mn<=12)&(f[...,3]>200)
    lab,n=ndi.label(m)
    if not n: return 0,0.0,[]
    idx=np.arange(1,n+1); area=ndi.sum(np.ones_like(lab),lab,idx)
    N=m.size; sel=area>=0.0002*N
    com=ndi.center_of_mass(m,lab,idx[sel])
    big=sorted(zip(area[sel],com),reverse=True)[:6]
    return int(sel.sum()), round(float(area[sel].sum()/N),4), [(int(a),int(c[1]),int(c[0])) for a,c in big]
if __name__=='__main__':
    q=json.load(open('qa_a.json')); seen={}
    for pid,o in q.items():
        if o['sha'] in seen: continue
        f=V.load(o['file']); r=flatwhite(f); seen[o['sha']]=r
        print(o['sha'][:8],o['cat'][:6],r)
    json.dump(seen,open('enclosed_a.json','w'))
