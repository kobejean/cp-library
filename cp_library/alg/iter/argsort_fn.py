import cp_library.alg.iter.__header__
from cp_library.bit.pack_sm_fn import pack_sm

def argsort(A: list[int], reverse=False):
    s, m = pack_sm(len(A))
    if reverse:
        I = [a<<s|i^m for i,a in enumerate(A)]
        I.sort(reverse=True)
        for i,ai in enumerate(I): I[i] = (ai^m)&m
    else:
        I = [a<<s|i for i,a in enumerate(A)]
        I.sort()
        for i,ai in enumerate(I): I[i] = ai&m
    return I
