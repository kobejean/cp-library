import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.iter.__header__

def coord_compress(A, distinct = False):
    s, m = pack_sm(N := len(A))
    ranks, vals, S = [0]*N, elist(N), [a<<s|j for j,a in enumerate(A)]
    S.sort()
    rank = last = -1
    for i,aj in enumerate(S):
        a,j = pack_dec(aj, s, m)
        if a != last or distinct: ranks[j], last = (rank := rank+1), a; vals.append(a)
        S[i] = a
    return ranks, vals

from cp_library.ds.elist_fn import elist
from cp_library.bit.pack_sm_fn import pack_dec, pack_sm