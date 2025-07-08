import cp_library.__header__
from cp_library.alg.iter.rank.rank_fn import rank
import cp_library.ds.__header__
import cp_library.ds.wavelet.__header__
from cp_library.ds.wavelet.wm_weighted_cls import WMWeighted
from cp_library.ds.wavelet.wm_compressed_cls import WMCompressed

class WMWeightedCompressed(WMWeighted, WMCompressed):
    def __init__(wm,A:list[int],W:list[int]):A,wm.Y=rank(A);super().__init__(A,W,len(wm.Y)-1)
    def sum_at(wm,y,l,r):return super().sum_at(y,l,r)if~(y:=wm._yidx(y))else 0
    def sum_below(wm,u,l,r):return super().sum_below(wm._didx(u),l,r)
    def sum_between(wm,d,u,l,r):return super().sum_between(wm._didx(d),wm._didx(u),l,r)
    def sum_corner(wm,r,u):return super().sum_corner(r,wm._didx(u))
    def sum_rect(wm,l,d,r,u):return super().sum_rect(l,wm._didx(d),r,wm._didx(u))