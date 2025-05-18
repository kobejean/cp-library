
import cp_library.ds.__header__
from cp_library.alg.dp.min2_fn import min2
from math import ceil, sqrt
from cp_library.misc.typing import int

class BitArray:
    def __init__(B, N: int):
        B.N, B.Z = N, (N+31)>>5
        B.bits, B.cnt = u32f(B.Z+1), u32f(B.Z+1)
    def build(B):
        B.bits.pop()
        for i,b in enumerate(B.bits): B.cnt[i+1] = B.cnt[i]+popcnt32(b)
        B.bits.append(0)
    def __len__(B): return B.N
    def __getitem__(B, i: int): return B.bits[i>>5]>>(31-(i&31))&1
    def set0(B, i: int): B.bits[i>>5]&=~(1<<31-(i&31))
    def set1(B, i: int): B.bits[i>>5]|=1<<31-(i&31)
    def count0(B, r: int): return r-B.count1(r)
    def count1(B, r: int): return B.cnt[r>>5]+popcnt32(B.bits[r>>5]>>32-(r&31))
    def select0(B, k: int):
        if not 0<=k<B.N-B.cnt[-1]: return -1
        l,r,k=0,B.N,k+1
        while 1<r-l:
            if B.count0(m:=(l+r)>>1)<k:l=m
            else:r=m
        return l
    def select1(B, k: int):
        if not 0<=k<B.cnt[-1]: return -1
        l,r,k=0,B.N,k+1
        while 1<r-l:
            if B.count1(m:=(l+r)>>1)<k:l=m
            else:r=m
        return l

from cp_library.bit.popcnt32_fn import popcnt32
from cp_library.ds.array.u32f_fn import u32f

# Inspired by: https://github.com/tatyam-prime/SortedSet/blob/main/BucketList.py
class BitList:
    BUCKET_RATIO = 16
    SPLIT_RATIO = 24
    
    def __init__(B, N: int) -> None:
        B.N, B.Z = N, (N+31)>>5
        B = int(ceil(sqrt(B.Z / B.BUCKET_RATIO)))
        M = (B.Z+B-1)//B
        B.bits = [[0]*(min2(i+M,B.Z)-i) for i in range(B)]

    def _insert(B, a: list[int], b: int, i: int, x: int):
        n = len(a)
        if (0x1041042*i)&0x3fffffff<0x1041042:
            a.append(0)
            n+=1
        q = (0x1041042*i)>>30
        r=62-i+b*63
        # b, i = divmod(i, 63)
        # i = 62-i
        while b<(n:=n-1):a[n]=a[n]>>1|(a[n-1]&1)<<62
        m = (1<<(r+1))-1
        a[b]=a[b]&~m|1<<i|(a[b]&m)>>1

        B.size += 1
        if len(a) > len(B.bits) * B.SPLIT_RATIO:
            mid = len(a) >> 1
            B.bits[b:b+1] = [a[:mid], a[mid:]]

    def insert(B, i: int, x: int):
        if B.size == 0:
            if i != 0 and i != -1: raise IndexError
            B.bits.append([x])
            B.size = 1
            return
        for b, a in enumerate(B.bits):
            if i <= len(a): return B._insert(a, b, i, x)
            i -= len(a)
    
    def __getitem__(B, i: int):
        for a in B.bits:
            if i < len(a): return a[i]
            i -= len(a)
        raise IndexError
    
    def __setitem__(B, i: int, x: int):
        for a in B.bits:
            if i < len(a): a[i] = x
            i -= len(a)
        raise IndexError
