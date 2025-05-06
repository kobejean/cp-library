import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.iter.__header__

def icoord_compress(A: list[int]):
    s, m = pack_sm((N := len(A))-1)
    R, V = [0]*N, [0]*N
    for i,a in enumerate(A): A[i] = a<<s|i
    A.sort()
    r = p = -1
    for ai in A:
        a, i = pack_dec(ai, s, m)
        if a != p: V[r:=r+1] = p = a
        R[i] = r
    del V[r+1:]
    return R, V

from cp_library.bit.pack_sm_fn import pack_dec, pack_sm