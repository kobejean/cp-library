import cp_library.math.__header__
from typing import Callable
from cp_library.ds.elist_fn import elist

def monotone_minima(N: int, M: int, func: Callable[[int,int,int],bool]):
    min_cols = [0] * N
    stack: list[tuple[int, ...]] = elist(N.bit_length() << 2)
    stack.append((0, N, 0, M))

    while stack:
        li, ri, lj, rj = stack.pop()
        if li == ri: continue
        mi = li + ri >> 1
        min_j = lj
        for j in range(lj + 1, rj):
            if func(mi, min_j, j):
                min_j = j
        min_cols[mi] = min_j
        stack.append((li, mi, lj, min_j + 1))
        stack.append((mi + 1, ri, min_j, rj))

    return min_cols

def minplus_conv_arb_cnvx(arb: list[int], cnvx: list[int]) -> list[int]:
    N, M = len(cnvx), len(arb)
    
    def cmp(i, j, k):
        return i >= k and (i-j >= N or (cnvx[i-j] + arb[j] >= cnvx[i-k] + arb[k]))
    
    cols = monotone_minima(N+M-1, M, cmp)
    return [arb[j] + cnvx[i-j] for i, j in enumerate(cols)]

def minplus_conv_inplace(A: list[int], B: list[int]):
    N, M = len(A), len(B)
    for i in range(N-1,-1,-1):
        A[i] = min(B[j] + A[i-j] for j in range(min(M,i+1)))   
