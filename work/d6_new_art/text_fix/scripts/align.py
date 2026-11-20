import sys; sys.path.insert(0, "/home/user/crowned-co-data/work/d6_new_art/text_fix/scripts")
from common import *
import cv2
def gray_on_white(a):
    rgb = a[..., :3]; al = a[..., 3:4] / 255.0
    return (rgb * al + 255 * (1 - al)).mean(-1).astype(np.uint8)
def align(src_a, ref_a):
    """similarity transform mapping ref coords -> src coords"""
    g1, g2 = gray_on_white(src_a), gray_on_white(ref_a)
    orb = cv2.ORB_create(8000)
    k1, d1 = orb.detectAndCompute(g1, None); k2, d2 = orb.detectAndCompute(g2, None)
    m = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True).match(d2, d1)
    p2 = np.float32([k2[x.queryIdx].pt for x in m]); p1 = np.float32([k1[x.trainIdx].pt for x in m])
    M, inl = cv2.estimateAffinePartial2D(p2, p1, ransacReprojThreshold=2.0)
    return M, int(inl.sum()), len(m)
if __name__ == '__main__':
    a = load_rgba(src(sys.argv[1])[1]); b = load_rgba(src(sys.argv[2])[1])
    M, ni, nm = align(a, b); print(np.round(M, 4), ni, nm)
