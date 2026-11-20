"""Fill speckled see-through holes inside the cream 'TREE UP' letters of 6ac7149db8146913210038d0.
The DTG file (text_fix/d402b87a...) is pixel-aligned with the opaque master of the same design
(text_fix/7d9d6870..., mean abs diff 0.2/255 on shared opaque pixels). Letter mask = master pixels of the
letter's own cream fill in the headline band, morphologically closed (3x3, 2 iter) and hole-filled, but
never on master white background (keeps R/P counters transparent) and never on the black outline.
Inside that mask the hole pixels get the letter's own fill colour from the master and alpha 255.
Nothing outside the TREE UP letters changes; wording untouched."""
import sys,numpy as np
from PIL import Image
from scipy import ndimage as nd
src,master,out,dbg,band_h=sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],int(sys.argv[5])
a=np.array(Image.open(src).convert('RGBA')).astype(np.float32);m=np.array(Image.open(master).convert('RGB')).astype(np.float32)
H,W=a.shape[:2];band=np.zeros((H,W),bool);band[:band_h]=True
R,G,B=m[...,0],m[...,1],m[...,2]
mcream=(R>225)&(G>215)&(R-B>12)&(R-B<60)&band
mwhite=(m.min(2)>244)&(np.ptp(m,2)<8)
mblack=m.max(2)<90
letter=nd.binary_fill_holes(nd.binary_closing(mcream,np.ones((3,3)),iterations=2))&band&~mwhite&~nd.binary_dilation(mblack,iterations=1)
letter|=mcream
# the period dot is a white-filled glyph enclosed by the outline in the master (same colour as master bg);
# add the enclosed master-white component that contains the dot centre (1662,450) to the letter mask
encw=nd.binary_fill_holes(mblack|~mwhite)&mwhite&band
lab,_=nd.label(encw);pid=lab[450,1662]
if pid: letter|=lab==pid
need=letter&((a[...,3]<250)|(np.abs(a[...,:3]-m).max(2)>18))
# 1-2px pinholes between the cream fill and the black outline: master there is outline/fill blend (not white bg)
need|=nd.binary_dilation(letter,iterations=3)&(a[...,3]<250)&~mwhite&(m.max(2)<235)&band
# the master's thin near-white liner just inside the outline (<=2px from the cream fill) was keyed out with the bg
need|=nd.binary_dilation(letter,iterations=2)&(a[...,3]<250)&band
o=a.copy();o[...,:3][need]=m[need];o[...,3][need]=255
# defringe: light-grey white-matte pixels on the OUTER edge of the black outline (outside letters, next to
# transparency) are un-mixed against white -> outline black with alpha = darkness (no white halo on dark garments)
tr=o[...,3]<10
lg=band&~letter&(o[...,3]>200)&(o[...,:3].min(2)>110)&(np.ptp(o[...,:3],2)<20)&nd.binary_dilation(tr,iterations=2)&nd.binary_dilation(mblack,iterations=3)
lum=o[...,:3][lg].mean(1);o[...,3][lg]=np.clip(255-lum,0,255)*255/235;o[...,:3][lg]=(25,22,20)
print('defringed px',int(lg.sum()))
Image.fromarray(o.clip(0,255).astype(np.uint8),'RGBA').save(out)
d=np.zeros((H,W,3),np.uint8);d[a[...,3]>200]=(90,90,90);d[letter]=(200,200,120);d[need]=(255,0,0)
Image.fromarray(d[:band_h]).save(dbg)
hole_before=(letter&(a[...,3]<250)).sum();hole_after=(letter&(o[...,3]<250)).sum()
print('letter-mask px',int(letter.sum()),'see-through px in letters before',int(hole_before),'after',int(hole_after),'px changed',int(need.sum()))
