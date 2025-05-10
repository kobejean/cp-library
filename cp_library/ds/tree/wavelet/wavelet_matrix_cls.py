import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.tree.__header__
import cp_library.ds.tree.wavelet.__header__
from cp_library.ds.tree.wavelet.bit_array_cls import BitArray

class WaveletMatrix:
    def __init__(W,A, Amax: int = None):
        if Amax is None: Amax = max(A, default=0)
        W.N=N=len(A); W.H=Amax.bit_length()
        W.L,B=[BitArray(N, H) for H in range(W.H-1,-1,-1)],[0]*N
        W.U = W.L[::-1]
        for L in W.L:
            x,y,i=-1,N-1,N
            while i:y-=A[i:=i-1]>>L.H&1
            for i,k in enumerate(A):
                if k>>L.H&1:B[y:=y+1]=k;L.set1(i)
                else:B[x:=x+1]=k
            A,B=B,A;L.build()

    def kth(W, l: int, r: int, k: int):
        '''Returns the `k+1`-th value in sorted order of values in range `[l, r)`'''
        if k < 0: k += r-l
        s=0
        for L in W.L:
            l, r = l-(l1:=L.count1(l)), r-(r1:=L.count1(r))
            if k>=r-l:s|=1<<L.H;k-=r-l;l,r=L.T0+l1,L.T0+r1
        return s
    
    def select(W, x: int, k: int, l: int = 0, r: int = -1):
        '''Returns the index of the `k+1`-th occurance of `x` in range `[l, r)`'''
        if not (0 <= x < 1 << W.H): return -1
        if r == -1: r = W.N-1
        if k < 0: k += r - l
        for L in W.L: l, r = L.pos_pair(L[x], l, r)
        if not l <= (i:=l+k) < r: return -1
        for L in W.U:
            if x>>L.H&1:i=L.select1(i-L.T0)
            else:i=L.select0(i)
        return i

    def rank(W, x: int, r: int): return W.rank_range(0, r, x)
    def rank_range(W, x: int, l: int, r: int):
        if l >= r: return 0
        for L in W.L: l, r = L.pos_pair(L[x], l, r)
        return r-l
    
    def count(W, x: int, l: int, r: int):
        '''Count how many `x` values are in range `[l,r)` '''
        if l >= r: return 0
        return W._cnt(x+1, l, r)-W._cnt(x, l, r)
    
    def count_between(W, lo: int, hi: int, l: int, r: int):
        '''Count `i`'s in `[l,r)` such that `lo <= A[i] < hi` '''
        if l >= r or lo >= hi: return 0
        return W._cnt(hi, l, r)-W._cnt(lo, l, r)

    def count_below(W, hi: int, l: int, r: int):
        '''Count `i`'s in `[l,r)` such that `A[i] < hi` '''
        return W._cnt(hi, l, r)

    def _cnt(W, hi: int, l: int, r: int):
        if hi<=0: return 0
        if hi.bit_length() > W.H: return r-l
        cnt = 0
        for L in W.L:
            l, r = l-(l1:=L.count1(l)), r-(r1:=L.count1(r))
            if hi>>L.H&1:cnt+=r-l;l,r=L.T0+l1,L.T0+r1
        return cnt
    
    def prev_val(W, hi: int, l: int, r: int):
        return W.kth(cnt-1, l, r) if (cnt := W._cnt(hi, l, r)) else -1
    
    def next_val(W, lo: int, l: int, r: int):
        return W.kth(cnt, l, r) if (cnt := W._cnt(lo, l, r)) < r-l else -1
