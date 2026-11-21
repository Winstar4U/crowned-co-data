import sys; sys.path.insert(0, sys.argv[1])
from rlib import *
sha = 'a897d05659'
full = [p for p in glob.glob(FIX + sha + '*.png') if '_v2' not in p][0].split('/')[-1][:-4]
s1 = np.asarray(Image.open(sys.argv[1] + '/rep/a897d056_stage1.png')).astype(np.float32)
dk = dark_components(s1, frac=0.5, minarea=30)
out = stroke(s1, 12.0, (250, 248, 240))
print('stroked comps px', int(dk.sum()))
save(out, FIX + full + '_v2.png')
view([s1, out], sys.argv[1] + '/r_a897b.png', size=1500)
view([s1, out], sys.argv[1] + '/r_a897c.png', box=(1700, 1950, 500, 1550), size=1500)
