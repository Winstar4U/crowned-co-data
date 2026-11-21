"""Local Real-ESRGAN 4x super-resolution (RRDBNet, weights from xinntao/Real-ESRGAN GitHub releases).
Usage: python -I sr.py <in.png> <out.png> <weights.pth> [nblock=6] [final_long_side=0]
RGB via model; alpha via Lanczos 4x (binary 0/255 masks: + Gaussian 1.8px de-stair and 2x edge contrast).
RGB is super-resolved as composited on WHITE (every target blank here is white); not for dark blanks."""
import sys,math,time
import numpy as np, torch, torch.nn as nn, torch.nn.functional as F
from PIL import Image
from scipy import ndimage
Image.MAX_IMAGE_PIXELS=None
class RDB(nn.Module):
    def __init__(s,nf=64,gc=32):
        super().__init__()
        s.conv1=nn.Conv2d(nf,gc,3,1,1);s.conv2=nn.Conv2d(nf+gc,gc,3,1,1);s.conv3=nn.Conv2d(nf+2*gc,gc,3,1,1)
        s.conv4=nn.Conv2d(nf+3*gc,gc,3,1,1);s.conv5=nn.Conv2d(nf+4*gc,nf,3,1,1);s.l=nn.LeakyReLU(0.2,True)
    def forward(s,x):
        x1=s.l(s.conv1(x));x2=s.l(s.conv2(torch.cat((x,x1),1)));x3=s.l(s.conv3(torch.cat((x,x1,x2),1)))
        x4=s.l(s.conv4(torch.cat((x,x1,x2,x3),1)));x5=s.conv5(torch.cat((x,x1,x2,x3,x4),1));return x5*0.2+x
class RRDB(nn.Module):
    def __init__(s,nf=64,gc=32):
        super().__init__();s.rdb1=RDB(nf,gc);s.rdb2=RDB(nf,gc);s.rdb3=RDB(nf,gc)
    def forward(s,x): return s.rdb3(s.rdb2(s.rdb1(x)))*0.2+x
class RRDBNet(nn.Module):
    def __init__(s,nb=23,nf=64,gc=32):
        super().__init__()
        s.conv_first=nn.Conv2d(3,nf,3,1,1);s.body=nn.Sequential(*[RRDB(nf,gc) for _ in range(nb)]);s.conv_body=nn.Conv2d(nf,nf,3,1,1)
        s.conv_up1=nn.Conv2d(nf,nf,3,1,1);s.conv_up2=nn.Conv2d(nf,nf,3,1,1);s.conv_hr=nn.Conv2d(nf,nf,3,1,1);s.conv_last=nn.Conv2d(nf,3,3,1,1);s.l=nn.LeakyReLU(0.2,True)
    def forward(s,x):
        f=s.conv_first(x);f=f+s.conv_body(s.body(f))
        f=s.l(s.conv_up1(F.interpolate(f,scale_factor=2,mode='nearest')));f=s.l(s.conv_up2(F.interpolate(f,scale_factor=2,mode='nearest')))
        return s.conv_last(s.l(s.conv_hr(f)))
def load(w,nb):
    m=RRDBNet(nb);sd=torch.load(w,map_location='cpu',weights_only=True);sd=sd.get('params_ema',sd.get('params',sd))
    m.load_state_dict(sd,strict=True);m.eval();return m
@torch.no_grad()
def run(m,img,tile=320,pad=32):
    h,w,_=img.shape;out=np.zeros((h*4,w*4,3),np.float32);x=torch.from_numpy(img.transpose(2,0,1)).float()[None]
    for y0 in range(0,h,tile):
        for x0 in range(0,w,tile):
            y1=min(y0+tile,h);x1=min(x0+tile,w);ya=max(0,y0-pad);xa=max(0,x0-pad);yb=min(h,y1+pad);xb=min(w,x1+pad)
            o=m(x[:,:,ya:yb,xa:xb]).clamp(0,1)[0].numpy().transpose(1,2,0)
            out[y0*4:y1*4,x0*4:x1*4]=o[(y0-ya)*4:(y0-ya)*4+(y1-y0)*4,(x0-xa)*4:(x0-xa)*4+(x1-x0)*4]
    return out
def main():
    inp,outp,w=sys.argv[1:4];nb=int(sys.argv[4]) if len(sys.argv)>4 else 6;final=int(sys.argv[5]) if len(sys.argv)>5 else 0
    pre=float(sys.argv[6]) if len(sys.argv)>6 else 1.0
    torch.set_num_threads(4);t=time.time();m=load(w,nb)
    full=Image.open(inp).convert('RGBA')
    if pre!=1.0: full=full.resize((round(full.width*pre),round(full.height*pre)),Image.BOX)  # e.g. undo a prior 2x Lanczos
    fa=np.asarray(full);FW,FH=full.size
    # crop to content (+24px) to save CPU; area outside is plain background
    if fa[...,3].min()<250: cm=fa[...,3]>8
    else:
        c=fa[0,0,:3].astype(int);cm=np.abs(fa[...,:3].astype(int)-c).sum(2)>12
    ys,xs=np.where(cm);x0=max(0,xs.min()-24);y0=max(0,ys.min()-24);x1=min(FW,xs.max()+25);y1=min(FH,ys.max()+25)
    im=full.crop((x0,y0,x1,y1));a=np.asarray(im).astype(np.float32)/255;rgb=a[...,:3].copy();al=a[...,3]
    has_a=al.min()<0.99
    binary=np.unique((al*255).round()).size<=4
    if has_a:
        # all target blanks are white: super-resolve the art as it appears composited on white (old bg matte in
        # transparent pixels discarded); alpha is upscaled separately below
        rgb=rgb*al[...,None]+(1.0-al[...,None])
    o=run(m,rgb)
    if has_a:
        # alpha: Lanczos 4x + mild edge contrast (k=2.2); the model on alpha-as-grey produced a two-step grey rim
        L=np.asarray(Image.fromarray((al*255).round().astype(np.uint8)).resize((al.shape[1]*4,al.shape[0]*4),Image.LANCZOS)).astype(np.float32)/255
        if binary: L=ndimage.gaussian_filter(L,1.8);oa=np.clip((L-0.5)*2.0+0.5,0,1)   # de-stair the 0/255 source mask
        else: oa=np.clip(L,0,1)
    else: oa=np.ones(o.shape[:2],np.float32)
    res=np.dstack([o,oa]);res=(res*255+0.5).clip(0,255).astype(np.uint8);C=Image.fromarray(res,'RGBA')
    R=full.resize((FW*4,FH*4),Image.LANCZOS) if not has_a else Image.new('RGBA',(FW*4,FH*4),(0,0,0,0))
    R.paste(C,(x0*4,y0*4))
    if final and max(R.size)!=final:
        s=final/max(R.size);R=R.resize((round(R.width*s),round(R.height*s)),Image.LANCZOS)
    if not has_a: R=R.convert('RGB')
    R.save(outp,optimize=False,compress_level=6);print(inp,'->',outp,R.size,'%.0fs'%(time.time()-t))
if __name__=='__main__':main()
