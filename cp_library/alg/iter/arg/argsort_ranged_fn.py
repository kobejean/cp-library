import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.iter.__header__
import cp_library.alg.iter.arg.__header__

def argsort_ranged(A: list[int], l: int, r: int, reverse=False):
    P = Packer(r-l-1); I = [A[l+i] for i in range(r-l)]; P.ienumerate(I, reverse); I.sort()
    for i in range(r-l): I[i] = (I[i] & P.m) + l
    return I
from cp_library.bit.pack.packer_cls import Packer