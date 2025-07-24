import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.conv.__header__
from cp_library.math.conv.ior_zeta_pair_fn import ior_zeta_pair
from cp_library.math.conv.ior_mobius_fn import ior_mobius
import cp_library.math.conv.mod.__header__

def isubset_conv_ranked(Ar, Br, N, Z, M) -> list[int]:
    ior_zeta_pair(Ar, Br, N)
    for ij in range(Z-M,-1,-M):
        for k in range(M): Ar[ij|k] *= Br[k]
        for i in range(0,ij,M):
            j = ij-i
            for k in range(M): Ar[ij|k] += Ar[i|k] * Br[j|k]
    return ior_mobius(Ar, N)