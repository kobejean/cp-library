import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.iter.__header__
import cp_library.alg.iter.arg.__header__

def argsort(A: list[int], reverse=False):
    P = Packer(len(I := A.copy())-1); P.ienumerate(I, reverse); I.sort(); P.iindices(I)
    return I
from cp_library.bit.pack.packer_cls import Packer