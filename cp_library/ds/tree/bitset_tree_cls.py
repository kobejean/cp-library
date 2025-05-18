import cp_library.__header__
from cp_library.alg.dp.min2_fn import min2
from cp_library.ds.array.u32f_fn import u32f
import cp_library.ds.__header__
import cp_library.ds.tree.__header__

class BitsetTree:
    def __init__(B, S: str):
        B.N = N = len(S)
        L = u32f((N+31)>>5)
        for k,c in enumerate(S):
            k,r = k>>5,k&31
            if c=='1': L[k]|=1<<r
        B.levels = [L]
        while (N := len(L := B.levels[-1])) > 1:
            A = u32f((N+31)>>5)
            for i in range(0,N,32):
                a=j=0;r=min2(i+32,N)
                while i+j<r:a|=(0<L[i+j])<<j;j+=1
                A[i>>5]=a
            B.levels.append(A)
        B.depth = len(B.levels)

    def set0(B, k):
        if B.levels[0][k>>5]>>(k&31)&1: 
            l = -1
            while (l:=l+1) < B.depth:
                B.levels[l][k>>5]&=~(1<<(k&31));k>>=5
                if B.levels[l][k]: break

    def set1(B, k):
        if not B.levels[0][k>>5]>>(k&31)&1: 
            l = -1
            while (l:=l+1) < B.depth: B.levels[l][k>>5]|=1<<(k&31);k>>=5

    def __setitem__(B, k: int, v: int):
        if v: B.set1(k)
        else: B.set0(k)

    def __getitem__(B, k: int):
        b,r=k>>5,k&31
        return B.levels[0][b]>>r&1
    
    def ge(B, k: int):
        if not B.levels[-1][0]: return -1
        l = -1
        while True:
            k,r=k>>5,k&31
            if m:=(B.levels[l:=l+1][k]>>r)<<r: break
            if (k:=k+1) >= len(B.levels[l]): return -1
        while l:m=B.levels[l:=l-1][k:=k<<5|(m&-m).bit_length()-1]
        return k<<5|(m&-m).bit_length()-1
    
    def le(B, k: int):
        if not B.levels[-1][0]: return -1
        l = -1
        while True:
            k,r=k>>5,k&31
            if m:=B.levels[l:=l+1][k]&((1<<(r+1))-1): break
            if (k:=k-1)<0: return -1
        while l:m=B.levels[l:=l-1][k:=k<<5|m.bit_length()-1]
        return k<<5|m.bit_length()-1
