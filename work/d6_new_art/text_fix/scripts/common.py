import sys, os, json, csv
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from scipy import ndimage as ndi
sys.path.insert(0, '/home/user/crowned-co-data/work/d6_new_art/scripts')
import process as P  # our own phase-2 helpers (fix_white_box, gated_flood)
Image.MAX_IMAGE_PIXELS = None
TF = '/home/user/crowned-co-data/work/d6_new_art/text_fix'
WK = TF + '/work'
SRC = json.load(open(WK + '/src_map.json'))
TABLE = json.load(open(WK + '/table.json'))

def src(prefix):
    k = [s for s in SRC if s.startswith(prefix)][0]
    return k, SRC[k][1]

def load_rgba(p):
    return np.asarray(Image.open(p).convert('RGBA')).astype(np.float32)

def save_rgba(a, p):
    Image.fromarray(np.clip(a + 0.5, 0, 255).astype(np.uint8), 'RGBA').save(p)

def on_bg(a, color, crop=None, maxside=None):
    im = Image.fromarray(np.clip(a + 0.5, 0, 255).astype(np.uint8), 'RGBA')
    if crop: im = im.crop(crop)
    bg = Image.new('RGBA', im.size, tuple(color) + (255,)); bg.alpha_composite(im)
    bg = bg.convert('RGB')
    if maxside: bg.thumbnail((maxside, maxside), Image.LANCZOS)
    return bg

def font(name, size):
    paths = {
        'bebas': '/usr/share/fonts/truetype/bebas-neue/BebasNeue-Regular.ttf',
        'spartan_black': None,
    }
    return ImageFont.truetype(name, size)
