import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.iter.__header__

def icoord_compress_multi(*A: list[int], distinct = False):
    N = sum(len(Ai) for Ai in A)
    si, mi = pack_sm(len(A)-1)
    sj, mj = pack_sm((N-1)<<si)
    V, S = elist(N), [0]*N; S.sort()
    k = 0
    for i,Ai in enumerate(A):
        for j, a in enumerate(Ai):
            S[k] = a << sj | j << si | i; k += 1
    S.sort()
    r = p = -1
    for aji in S:
        a, j, i = aji >> sj, (aji&mj) >> si , aji & mi
        if a != p or distinct: r, p = r+1, a; V.append(a)
        Ai = A[i]
        Ai[j] = r
    return *A, V

from cp_library.ds.elist_fn import elist
from cp_library.bit.pack_sm_fn import pack_sm