import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.iter.__header__

def coord_compress(A: list[int], distinct = False):
    s, m = pack_sm((N := len(A))-1)
    R, V, S = [0]*N, elist(N), [a<<s|i for i,a in enumerate(A)]; S.sort()
    r = p = -1
    for ai in S:
        a, i = pack_dec(ai, s, m)
        if a != p or distinct: r, p = r+1, a; V.append(a)
        R[i] = r
    return R, V

from cp_library.ds.elist_fn import elist
from cp_library.bit.pack_sm_fn import pack_dec, pack_sm