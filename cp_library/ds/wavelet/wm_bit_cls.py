import cp_library.__header__
import cp_library.ds.__header__
from cp_library.ds.tree.bit.bit_cls import BIT
import cp_library.ds.wavelet.__header__
from cp_library.ds.wavelet.wm_weighted_cls import WMStatic, WMWeighted

class WMBIT(WMWeighted):
    class Level(WMStatic.Level):
        def build(L,W:list[int]):super().build();L.W=BIT(W[:])
        def sum(L,l:int,r:int):return L.W.sum_range(l,r)
    def _build_base(wm,W):wm.W=BIT(W[:])
    def _sum_range(wm,l,r):return wm.W.sum_range(l,r)
    def add(wm,i:int,w:int):
        wm.W.add(i,w)
        for L in wm.down:L.W.add(i:=L.pos(L[i],i),w)