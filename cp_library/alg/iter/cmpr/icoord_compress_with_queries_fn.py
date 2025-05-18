import cp_library.__header__
import cp_library.alg.__header__
from cp_library.alg.dp.max2_fn import max2
import cp_library.alg.iter.__header__
import cp_library.alg.iter.cmpr.__header__

def icoord_compress_with_queries(*A: list[int], x=0, distinct=False):
    N = mx = 0
    for Ai in A: N += len(Ai); mx = max2(mx, len(Ai))
    si, mi = pack_sm(mx-1); sj, mj = pack_sm((len(A)-1)<<si)
    S, k = [0]*N, 0
    for i,Ai in enumerate(A):
        for j,a in enumerate(Ai): S[k]=a << sj | i << si | j; k += 1
    S.sort(); r = p = -1
    for aji in S:
        a, i, j = aji >> sj, (aji&mj) >> si , aji & mi
        if x<=i and (distinct or a != p): r = r+1; p = a
        A[i][j] = r+(i<x)
    return A
from cp_library.bit.pack.pack_sm_fn import pack_sm