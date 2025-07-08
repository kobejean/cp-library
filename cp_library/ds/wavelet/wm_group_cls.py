import cp_library.__header__
import cp_library.ds.__header__
from cp_library.ds.list.presum_cls import Presum
import cp_library.ds.wavelet.__header__
from cp_library.ds.wavelet.wm_monoid_cls import WMStatic, WMMonoid

class WMGroup(WMMonoid):
    class Level(WMStatic.Level):
        def build(L, op, e, diff, W):super().build();L.W=Presum(W,op,e,diff)
        def prod(L,l:int,r:int):return L.W.range_sum(l,r)
    def __init__(wm,op,e,diff,A,W,Amax=None):wm._build(op,e,diff,A,W,[0]*len(A),[0]*len(A),max(A,default=0)if Amax is None else Amax)
    def _build(wm,op,e,diff,A,W,nA,nW,Amax):wm.diff=diff;super()._build(op, e, A, W, nA, nW, Amax)
    def _build_base(wm,W):wm.W=Presum(W,wm.op,wm.e,wm.diff)
    def _build_level(wm,L,W):L.build(wm.op,wm.e,wm.diff,W)
    def _prod_range(wm,l,r):return wm.W.range_sum(l,r)