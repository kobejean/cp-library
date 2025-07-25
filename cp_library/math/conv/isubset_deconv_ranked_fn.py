import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.conv.__header__
from cp_library.math.conv.ior_zeta_pair_ranked_fn import ior_zeta_pair_ranked
from cp_library.math.conv.ior_mobius_ranked_fn import ior_mobius_ranked

def isubset_deconv_ranked(Ar, Br, N, Z, M):
    inv = 1 // Br[0]; ior_zeta_pair_ranked(Ar, Br, N, M, Z)
    for i in range(0, Z, M):
        for k in range(M): Ar[i|k] *= inv
        for j in range(M, Z-i, M):
            ij = i + j; l = (1 << (j>>N))-1
            for k in range(l, M): Ar[ij|k] -= Ar[i|k] * Br[j|k]
    return ior_mobius_ranked(Ar, N, M, Z)