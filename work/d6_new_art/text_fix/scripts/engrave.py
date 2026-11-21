"""Full-colour -> 1-colour laser-engraving line art (black ink on transparent).
Pipeline (per source), working at 600 dpi of the actual print size on the tumbler:
  1. composite on white, luminance; bilateral smoothing (kills gradients/noise, keeps edges)
  2. ink = (L < Otsu threshold)  OR  colour-boundary edges (Canny on Lab, dilated to the min line weight)
  3. enforce min line weight 0.5 mm: morphological opening with a 0.5 mm disk (strokes thinner than
     that are dropped), fill pinholes < 0.3 mm, drop specks < 0.5 mm^2
  4. output = black ink, alpha = ink (anti-aliased by 2x supersample), sized at 600 dpi
Metrics recorded for honesty: ink lost by the line-weight opening, ink coverage, OCR of the text."""
import sys; sys.path.insert(0, "/home/user/crowned-co-data/work/d6_new_art/text_fix/scripts")
from common import *
import cv2

MM = 600 / 25.4          # px per mm at 600 dpi

def disk(r):
    r = max(1, int(round(r)))
    y, x = np.ogrid[-r:r + 1, -r:r + 1]
    return (x * x + y * y) <= r * r

def engrave(a, print_w_in, invert_bg_dark=False):
    Wt = int(round(print_w_in * 600))
    im = on_bg(a, (255, 255, 255))
    h = int(round(im.height * Wt / im.width))
    im = im.resize((Wt, h), Image.LANCZOS)
    rgb = np.asarray(im)
    sm = cv2.bilateralFilter(rgb, 9, 40, 7)
    L = cv2.cvtColor(sm, cv2.COLOR_RGB2LAB)
    l = L[..., 0]
    alpha_src = np.asarray(Image.fromarray(np.clip(a[..., 3], 0, 255).astype(np.uint8)).resize((Wt, h), Image.LANCZOS)) > 128
    # threshold on the design pixels only
    vals = l[alpha_src & (rgb.min(-1) < 245)]
    t, _ = cv2.threshold(vals.reshape(-1, 1).astype(np.uint8), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    dark = l < t
    ed = cv2.Canny(cv2.GaussianBlur(L, (0, 0), 1.2), 40, 90) > 0
    ed = ndi.binary_dilation(ed, structure=disk(0.3 * MM))
    ink = (dark | ed) & alpha_src
    before = ink.sum()
    ink = ndi.binary_opening(ink, structure=disk(0.25 * MM))       # 0.5 mm min stroke
    lost = 1 - ink.sum() / max(before, 1)
    holes = ~ink
    hl, hn = ndi.label(holes); hs = ndi.sum(holes, hl, range(1, hn + 1))
    ink |= np.isin(hl, np.nonzero(hs < (0.3 * MM) ** 2 * 3.14)[0] + 1)
    il, inn = ndi.label(ink); isz = ndi.sum(ink, il, range(1, inn + 1))
    ink &= ~np.isin(il, np.nonzero(isz < 0.5 * MM * MM)[0] + 1)
    # anti-alias: slight blur of the binary mask
    alpha = cv2.GaussianBlur(ink.astype(np.float32), (0, 0), 0.6) * 255
    out = np.zeros((h, Wt, 4), np.float32); out[..., 3] = alpha
    return out, {'print_w_in': print_w_in, 'out_px': [Wt, h], 'otsu_L': float(t),
                 'ink_lost_to_min_weight': round(float(lost), 3), 'ink_coverage': round(float(ink.mean()), 3)}
