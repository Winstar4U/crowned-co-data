import sys,json,glob; sys.path.insert(0,'.')
import vlib as V, numpy as np
from scipy import ndimage as ndi
def cutmetric(o,f):
    if o.shape[:2]!=f.shape[:2]: return None
    cleared=(f[...,3]<8)&(o[...,3]>128)
    op=(f[...,3]>128).astype(np.float32)
    dens=ndi.uniform_filter(op,81)
    cut=cleared&(dens>0.55)
    lab,n=ndi.label(cut)
    if not n: return 0.0,0,(0,0)
    a=ndi.sum(np.ones_like(lab),lab,np.arange(1,n+1)); k=int(np.argmax(a))+1
    c=ndi.center_of_mass(cut,lab,k)
    return round(float(cut.sum()/cut.size),5), int(a.max()), (int(c[1]),int(c[0]))
if __name__=='__main__':
    files=json.load(open(sys.argv[1])); seen=set(); res={}
    for pid,o in files.items():
        if o['sha'] in seen or o['cat']=='low_contrast': continue
        seen.add(o['sha'])
        org=V.load(glob.glob(f'/home/user/crowned-co-data/work/d6_batch*/{pid}/original.png')[0]); f=V.load(o['file'])
        r=cutmetric(org,f); res[o['sha']]=r; print(o['sha'][:8],o['cat'][:5],r,flush=True)
    json.dump(res,open(sys.argv[2],'w'))
