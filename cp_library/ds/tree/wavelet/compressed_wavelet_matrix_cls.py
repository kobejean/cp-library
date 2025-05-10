import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.tree.__header__
import cp_library.ds.tree.wavelet.__header__
from cp_library.ds.tree.wavelet.wavelet_matrix_cls import WaveletMatrix

class CompressedWaveletMatrix(WaveletMatrix):
    def __init__(W,A):
        A,W.V = icoord_compress(A)
        super().__init__(A, len(W.V)-1)

    def _lval(W, x: int):
        l,r=-1,len(W.V)
        while 1<r-l:
            if W.V[m:=(l+r)>>1]<=x:l=m
            else:r=m
        return l
    def _rval(W, x: int):
        i = W._lval(x)
        return x if W.V and x == W.V[i] else i+1
    def _val(W, x: int): return x if W.V and x == W.V[x := W._lval(x)] else -1
    def __contains__(W,x:int):return W.V and W.V[W._lval(x)] == x
    def kth(W,k:int,l:int,r:int):return W.V[super().kth(l,r,k)]
    def select(W,x:int,k:int,l:int=0,r:int=-1):return super().select(x,k,l,r)if~(x:=W._val(x))else-1
    def rank_range(W,x:int,l:int,r:int):return super().rank_range(x,l,r)if~(x:=W._val(x))else 0
    def count(W,x:int,l:int,r:int):return super().count(W._val(x),l,r)
    def count_below(W,hi:int,l:int,r:int):return super().count_below(W._rval(hi),l,r)
    def count_between(W,lo:int,hi:int,l:int,r:int):return super().count_between(W._rval(lo),W._rval(hi),l,r)
    def prev_val(W,hi:int,l:int,r:int):return super().prev_val(W._rval(hi),l,r)
    def next_val(W,lo:int,l:int,r:int):return super().next_val(W._rval(lo),l,r)

from cp_library.alg.iter.cmpr.icoord_compress_fn import icoord_compress
