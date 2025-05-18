import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.wavelet.__header__
from cp_library.ds.wavelet.bit_array_cls import BitArray

class WMStatic:
    class Level(BitArray):
        def __init__(L, N: int, H: int):
            super().__init__(N)
            L.H = H
        def build(L):
            super().build()
            L.T0, L.T1 = L.N-L.cnt[-1], L.cnt[-1]
        def pos(L, bit: int, i: int): return L.T0+L.count1(i) if bit else L.count0(i)
        def pos2(L, bit: int, i: int, j: int): return (L.T0+L.count1(i), L.T0+L.count1(j)) if bit else (L.count0(i), L.count0(j))
    def __init__(wm,A,Amax:int=None):wm._build(A,[0]*len(A),max(A,default=0)if Amax is None else Amax)
    def _build(wm, A, nA, Amax):wm.N,wm.H=len(A),Amax.bit_length();wm._build_levels(A,nA)
    def _build_levels(wm, A, nA):
        wm.up=[wm.Level(wm.N,H) for H in range(wm.H)];wm.down=wm.up[::-1]
        for L in wm.down:
            x,y,i=-1,wm.N-1,wm.N
            while i:y-=A[i:=i-1]>>L.H&1
            for i,a in enumerate(A):
                if a>>L.H&1:nA[y:=y+1]=a;L.set1(i)
                else:nA[x:=x+1]=a
            A,nA=nA,A;L.build()
    def __getitem__(wm,i):
        y=0
        for L in wm.down:y=y<<1|(bit:=L[i]);i=L.pos(bit,i)
        return y
    def kth(wm, k: int, l: int, r: int):
        '''Returns the `k+1`-th value in sorted order of values in range `[l, r)`'''
        s=0
        for L in wm.down:
            l,r=l-(l1:=L.count1(l)),r-(r1:=L.count1(r))
            if k>=r-l:s|=1<<L.H;k-=r-l;l,r=L.T0+l1,L.T0+r1
        return s
    def select(wm, y: int, k: int, l: int = 0, r: int = -1):
        '''Returns the index of the `k+1`-th occurance of `y` in range `[l, r)`'''
        if not(0<=y<1<<wm.H):return-1
        if r==-1:r=wm.N-1
        for L in wm.down:l,r=L.pos2(L[y],l,r)
        if not l<=(i:=l+k)<r:return-1
        for L in wm.up:
            if y>>L.H&1:i=L.select1(i-L.T0)
            else:i=L.select0(i)
        return i
    def rank(wm, y: int, r: int): return wm.rank_range(y, 0, r)
    def rank_range(wm, y: int, l: int, r: int):
        if l >= r: return 0
        for L in wm.down:l,r=L.pos2(L[y],l,r)
        return r-l
    def count_at(wm, y: int, l: int, r: int):
        '''Count how many `y` values are in range `[l,r)` '''
        if l >= r: return 0
        return wm._cnt(y+1, l, r)-wm._cnt(y, l, r)
    def count_below(wm, u: int, l: int, r: int):
        '''Count `i`'s in `[l,r)` such that `A[i] < u` '''
        return wm._cnt(u, l, r)
    def count_between(wm, d: int, u: int, l: int, r: int):
        '''Count `i`'s in `[l,r)` such that `d <= A[i] < u` '''
        if l >= r or d >= u: return 0
        return wm._cnt(u, l, r)-wm._cnt(d, l, r)
    def _cnt(wm, u: int, l: int, r: int):
        if u<=0:return 0
        if wm.H<u.bit_length():return r-l
        cnt=0
        for L in wm.down:
            l,r=l-(l1:=L.count1(l)),r-(r1:=L.count1(r))
            if u>>L.H&1:cnt+=r-l;l,r=L.T0+l1,L.T0+r1
        return cnt
    def prev_val(wm,u:int,l:int,r:int):return wm.kth(cnt-1, l, r)if(cnt:=wm._cnt(u,l,r))else-1
    def next_val(wm,d:int,l:int,r:int):return wm.kth(cnt, l, r)if(cnt:=wm._cnt(d,l,r))<r-l else-1