import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.iter.__header__
import cp_library.alg.iter.arg.__header__

def argsort(A: list[int], reverse=False):
    s, m = pack_sm(len(A))
    if reverse:
        I = [a<<s|m^i for i,a in enumerate(A)]
        I.sort(reverse=True)
        for i,ai in enumerate(I): I[i] = m^ai&m
    else:
        I = [a<<s|i for i,a in enumerate(A)]
        I.sort()
        for i,ai in enumerate(I): I[i] = ai&m
    return I
from cp_library.bit.pack.pack_sm_fn import pack_sm