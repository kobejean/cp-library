import cp_library.__header__
import cp_library.ds.__header__
from cp_library.ds.tree.segtree_cls import SegTree
import cp_library.ds.wavelet.__header__
from cp_library.ds.wavelet.wm_monoid_cls import WMStatic, WMMonoid

class WMSegTree(WMMonoid):
    class Level(WMStatic.Level):
        def build(L, op, e, W):super().build();L.W=SegTree(op,e,W)
        def prod(L,l:int,r:int):return L.W.prod(l,r)
    def _build_base(wm,W):wm.W=SegTree(wm.op,wm.e,W)
    def _build_level(wm,L,W):L.build(wm.op,wm.e,W)
    def _prod_range(wm,l:int,r:int):return wm.W.prod(l,r)
    def set(wm,i:int,w:int):
        wm.W.set(i,w)
        for L in wm.down:L.W.set(i:=L.pos(L[i],i),w)
    def get(wm,i:int):return wm.W.get(i)