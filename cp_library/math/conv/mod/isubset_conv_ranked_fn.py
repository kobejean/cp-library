import cp_library.__header__
from cp_library.alg.dp.max2_fn import max2
import cp_library.math.__header__
import cp_library.math.conv.__header__
import cp_library.math.conv.mod.__header__
from cp_library.math.conv.ior_zeta_pair_ranked_fn import ior_zeta_pair_ranked
from cp_library.math.conv.ior_mobius_ranked_fn import ior_mobius_ranked

def isubset_conv_ranked(Ar, Br, N, M, Z, mod) -> list[int]:
    ior_zeta_pair_ranked(Ar, Br, N, M, Z)
    for i in range(Z): Ar[i], Br[i] = Ar[i]%mod, Br[i]%mod
    for ij in range(Z-M,-1,-M):
        for k in range(M): Ar[ij|k] = (Ar[ij|k] * Br[k]) % mod
        r = M-(1 << (N-(ij>>N)))+1
        for i in range(0,ij,M):
            j = ij-i; l = (1 << (max2(i,j)>>N))-1
            for k in range(l,r): Ar[ij|k] += Ar[i|k] * Br[j|k] % mod
    return ior_mobius_ranked(Ar, N, M, Z)