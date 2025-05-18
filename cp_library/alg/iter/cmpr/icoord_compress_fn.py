import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.iter.__header__
import cp_library.alg.iter.cmpr.__header__

def coord_compress(A: list[int], distinct = False):
    s, m = pack_sm(len(A)-1)
    V = [a<<s|i for i,a in enumerate(A)]; V.sort()
    if distinct:
        for r, ai in enumerate(V): a, i = pack_dec(ai, s, m); A[i], V[r] = r, a
    else:
        r = p = -1
        for ai in V:
            a, i = pack_dec(ai, s, m)
            if a != p: r = r+1; V[r] = p = a
            A[i] = r
        del V[r+1:]
    return A, V
from cp_library.bit.pack.pack_dec_fn import pack_dec
from cp_library.bit.pack.pack_sm_fn import pack_sm