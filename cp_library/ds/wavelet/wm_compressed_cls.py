import cp_library.__header__
from cp_library.alg.divcon.bisect_left_fn import bisect_left
from cp_library.alg.iter.rank.rank_fn import rank
import cp_library.ds.__header__
import cp_library.ds.wavelet.__header__
from cp_library.ds.wavelet.wm_static_cls import WMStatic

class WMCompressed(WMStatic):
    def __init__(wm,A):A,wm.Y=rank(A);super().__init__(A,len(wm.Y)-1)
    def _didx(wm,y:int):return bisect_left(wm.Y,y,0,len(wm.Y))
    def _yidx(wm,y:int):return i if(i:=wm._didx(y))<len(wm.Y)and wm.Y[i]==y else-1
    def __contains__(wm,y:int):return(i:=wm._didx(y))<len(wm.Y)and wm.Y[i]==y
    def kth(wm,k,l,r):return wm.Y[super().kth(k,l,r)]
    def select(wm,y,k,l=0,r=-1):return super().select(y,k,l,r)if~(y:=wm._yidx(y))else-1
    def rank_range(wm,y,l,r):return super().rank_range(y,l,r)if~(y:=wm._yidx(y))else 0
    def count_at(wm,y,l,r):return super().count_at(y,l,r)if~(y:=wm._yidx(y))else 0
    def count_below(wm,u,l,r):return super().count_below(wm._didx(u),l,r)
    def count_between(wm,d,u,l,r):return super().count_between(wm._didx(d),wm._didx(u),l,r)
    def prev_val(wm,u,l,r):return super().prev_val(wm._didx(u),l,r)
    def next_val(wm,d,l,r):return super().next_val(wm._didx(d),l,r)