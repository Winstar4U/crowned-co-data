import sys
from PIL import Image
Image.MAX_IMAGE_PIXELS=None
src,out,x0,y0,x1,y1,size=sys.argv[1],sys.argv[2],*map(int,sys.argv[3:8])
col=tuple(int(c) for c in (sys.argv[8] if len(sys.argv)>8 else '17,17,17').split(','))
im=Image.open(src).convert('RGBA').crop((x0,y0,x1,y1))
bg=Image.new('RGBA',im.size,col+(255,)); bg.alpha_composite(im)
bg=bg.convert('RGB'); bg.thumbnail((size,size),Image.LANCZOS); bg.save(out)
