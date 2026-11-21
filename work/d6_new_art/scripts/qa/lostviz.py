import sys,os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import vlib as V, numpy as np
from PIL import Image
o=V.load(sys.argv[1]); f=V.load(sys.argv[2]); cat=sys.argv[3]
m=V.qa_metrics(o,f,cat); lost=m['lost_mask']
col=tuple(int(c) for c in sys.argv[5].split(',')) if len(sys.argv)>5 else (17,17,17)
bg=np.zeros_like(f); bg[...,:3]=col; bg[...,3]=255
a=f[...,3:4]/255; img=f[...,:3]*a+bg[...,:3]*(1-a)
img[lost]=[255,0,255]
im=Image.fromarray(img.astype(np.uint8)); im.thumbnail((1000,1000)); im.save(sys.argv[4])
ys,xs=np.nonzero(lost); print(m['loss_pct'], len(ys), (xs.min(),ys.min(),xs.max(),ys.max()) if len(ys) else '')
