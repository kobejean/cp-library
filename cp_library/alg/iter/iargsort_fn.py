import cp_library.alg.iter.__header__
from cp_library.bit.pack_sm_fn import pack_sm

def iargsort(A: list[int], reverse=False):
    s, m = pack_sm(len(A))
    if reverse:
        for i,a in enumerate(A): A[i] = a<<s|i^m
        A.sort(reverse=True)
        for i,a in enumerate(A): A[i] = (a^m)&m
    else:
        for i,a in enumerate(A): A[i] = a<<s|i
        A.sort()
        for i,a in enumerate(A): A[i] = a&m
    return A
