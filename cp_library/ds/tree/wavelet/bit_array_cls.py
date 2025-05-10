import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.tree.__header__
import cp_library.ds.tree.wavelet.__header__

class BitArray:
    def __init__(B, N: int, H: int):
        B.N, B.Z, B.H = N, (N+31)>>5, H
        B.bits, B.pre = u32f(B.Z+1), u32f(B.Z+1)
    def build(B):
        B.bits.pop()
        for i,b in enumerate(B.bits): B.pre[i+1] = B.pre[i]+popcnt32(b)
        B.bits.append(0)
        B.T0, B.T1 = B.N-B.pre[-1], B.pre[-1]
    def __len__(B): return B.N
    def __getitem__(B, i: int): return B.bits[i>>5]>>(31-(i&31))&1
    def set0(B, i: int): B.bits[i>>5]&=~(1<<31-(i&31))
    def set1(B, i: int): B.bits[i>>5]|=1<<31-(i&31)
    def count0(B, r: int): return r-B.count1(r)
    def count1(B, r: int): return B.pre[r>>5]+popcnt32(B.bits[r>>5]>>32-(r&31))
    def select0(B, k: int):
        if not 0<=k<B.N-B.pre[-1]: return -1
        l,r,k=0,B.N,k+1
        while 1<r-l:
            if B.count0(m:=(l+r)>>1)<k:l=m
            else:r=m
        return l
    def select1(B, k: int):
        if not 0<=k<B.pre[-1]: return -1
        l,r,k=0,B.N,k+1
        while 1<r-l:
            if B.count1(m:=(l+r)>>1)<k:l=m
            else:r=m
        return l
    
    def pos(B, bit: int, i: int): return B.T0+B.count1(i) if bit else B.count0(i)

    def pos_pair(B, bit: int, i: int, j: int):
        return (B.T0+B.count1(i), B.T0+B.count1(j)) if bit else (B.count0(i), B.count0(j))

from cp_library.bit.popcnt32_fn import popcnt32
from cp_library.ds.array_init_fn import u32f
