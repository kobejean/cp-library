import cp_library.__header__
from cp_library.alg.iter.cmpr.coord_compress_fn import coord_compress
import cp_library.ds.__header__
import cp_library.ds.wavelet.__header__
from cp_library.ds.wavelet.wm_compressed_cls import WMCompressed
from cp_library.ds.wavelet.wm_monoid_cls import WMMonoid

class WMMonoidCompressed(WMMonoid, WMCompressed):
    def __init__(wm,op,e,A:list[int],W:list[int]):A,wm.Y=coord_compress(A);WMMonoid.__init__(wm,op,e,A,W,len(wm.Y)-1)
    def prod_at(wm,y,l,r):return super().prod_at(y,l,r)if~(y:=wm._yidx(y))else 0
    def prod_below(wm,u,l,r):return super().prod_below(wm._didx(u),l,r)
    def prod_between(wm,d,u,l,r):return super().prod_between(wm._didx(d),wm._didx(u),l,r)
    def prod_corner(wm,r,u):return super().prod_corner(r,wm._didx(u))
    def prod_rect(wm,l,d,r,u):return super().prod_rect(l,wm._didx(d),r,wm._didx(u))