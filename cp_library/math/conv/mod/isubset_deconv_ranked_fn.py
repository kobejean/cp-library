import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.conv.__header__
from cp_library.math.conv.ior_zeta_pair_fn import ior_zeta_pair
from cp_library.math.conv.ior_mobius_fn import ior_mobius
import cp_library.math.conv.mod.__header__

def isubset_deconv_ranked(Ar, Br, N, Z, M, mod: int) -> list[int]:
    inv = pow(Br[0], -1, mod)
    ior_zeta_pair(Br, Ar, N)
    for i in range(Z): Br[i], Ar[i] = Br[i]%mod, Ar[i]%mod
    for j in range(0, Z, M):
        for k in range(M): Ar[j|k] = (Ar[j|k] * inv) % mod
        for i in range(M, Z-j, M):
            ij = i + j
            for k in range(M): Ar[ij|k] -= Br[i|k] * Ar[j|k] % mod
    return ior_mobius(Ar, N)