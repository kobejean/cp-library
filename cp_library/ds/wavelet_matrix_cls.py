import cp_library.ds.__header__

class BitArray:
    def __init__(B, N: int, H: int):
        B.N, B.Z, B.H = N, (N+31)>>5, H
        B.bits, B.pre = u32f(B.Z), u32f(B.Z+1)
    def build(B):
        for i,b in enumerate(B.bits): B.pre[i+1] = B.pre[i]+popcnt32(b)
        B.bits.append(0)
        B.T0, B.T1 = B.N-B.pre[-1], B.pre[-1]
    def __len__(B): return B.N
    def __getitem__(B, i: int): return B.bits[i>>5]>>(31-(i&31))&1
    def set0(B, i: int): B.bits[i>>5]&=~(1<<31-(i&31))
    def set1(B, i: int): B.bits[i>>5]|=1<<31-(i&31)
    def rank0(B, r: int): return r-B.rank1(r)
    def rank1(B, r: int): return B.pre[r>>5]+popcnt32(B.bits[r>>5]>>32-(r&31))
    def select0(B, k: int):
        if not 0<=k<B.N-B.pre[-1]: return -1
        l,r,k=0,B.Z,k+1
        while 1<r-l:
            if B.rank0(m:=(l+r)>>1)<k:l=m
            else:r=m
        return l
    def select1(B, k: int):
        if not 0<=k<B.pre[-1]: return -1
        l,r,k=0,B.Z,k+1
        while 1<r-l:
            if B.rank1(m:=(l+r)>>1)<k:l=m
            else:r=m
        return l

    def next_range(B, bit: int, l: int, r: int):
        if bit: return B.T0+B.rank1(l), B.T0+B.rank1(r)
        else: return B.rank0(l), B.rank0(r)

class WaveletMatrix:
    def __init__(W,A):
        A,W.V = icoord_compress(A)
        W.N=N=len(A); W.H=(len(W.V)-1).bit_length()
        W.L,B=[BitArray(N, H) for H in range(W.H-1,-1,-1)],[0]*N
        for L in W.L:
            x,y,j=-1,N-1,N
            while j:y-=A[j:=j-1]>>L.H&1
            for j,k in enumerate(A):
                if k>>L.H&1:B[y:=y+1]=k;L.set1(j)
                else:B[x:=x+1]=k
            A,B=B,A;L.build()

    def _fval(W, x: int, upper: bool = False):
        l,r=-1,len(W.V)
        while 1<r-l:
            if W.V[m:=(l+r)>>1]<=x:l=m
            else:r=m
        return l + (upper and W.V[l] != x)

    def __contains__(W, x: int):
        return W.V and W.V[W._fval(x)] == x

    def kth(W, l: int, r: int, k: int):
        if k < 0: k = r-l+k
        s=0
        for L in W.L:
            l, r = l-(l1:=L.rank1(l)), r-(r1:=L.rank1(r))
            if k>=r-l:s|=1<<L.H;k-=r-l;l,r=L.T0+l1,L.T0+r1
        return W.V[s]

    def rank(W, x: int, r: int): return W.range_rank(0, r, x)
    def range_rank(W, l: int, r: int, x: int):
        if l >= r or not W.V or x != W.V[x := W._fval(x)]: return -1
        for L in W.L: l, r = L.next_range(L[x], l, r)
        return r-l
    
    def range_freq(W, l: int, r: int, x: int):
        """
        l, r: Range in the original array (0-indexed, half-open)

        x: Value

        Returns: Number of elements in the range equal to x
        """
        if l >= r or not W.V or x != W.V[x := W._fval(x)]: return 0
        return W._rect_freq(l, r, x+1)-W._rect_freq(l, r, x)
    
    def rect_freq(W, l: int, r: int, a: int, b: int):
        """
        l, r: Range in the original array (0-indexed, half-open)

        a, b: Value range (half-open)

        Returns: Number of elements in the range satisfying the condition
        """
        if l >= r or not W.V or (a := W._fval(a, True)) >= (b := W._fval(b, True)): return 0
        return W._rect_freq(l, r, b)-W._rect_freq(l, r, a)

    def _rect_freq(W, l: int, r: int, u: int):
        if u.bit_length() > W.H: return r-l
        cnt = 0
        for L in W.L:
            l, r = l-(l1:=L.rank1(l)), r-(r1:=L.rank1(r))
            if u>>L.H&1:cnt+=r-l;l,r=L.T0+l1,L.T0+r1
        return cnt

from cp_library.alg.iter.icoord_compress_fn import icoord_compress
from cp_library.bit.popcnt32_fn import popcnt32
from cp_library.ds.array_init_fn import u32f
