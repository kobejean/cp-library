import cp_library.__header__
from cp_library.ds.view.view_cls import view
import cp_library.math.__header__
import cp_library.math.conv.__header__
from cp_library.math.conv.ior_zeta_fn import ior_zeta

def isubset_conv_half(Ar: list[int], B: list[int], n: int, N: int, mod: int, pcnt) -> list[int]:
    Br = [0]*(z := (n+1)*(m := 1<<n))
    for i in range(m): Br[pcnt[i]<<n|i] = B[i]
    ior_zeta(Br, n)
    for i in range(z): Br[i] = Br[i]%mod
    for ij in range(n,-1,-1):
        ij_, i_ = (ij+1)<<N|m, ij<<n
        for k in range(m): Ar[ij_|k] = (Br[i_|k] * Ar[k]) % mod
        for i in range(ij):
            j = ij-i; i_, j_ = i<<n, j<<N
            for k in range(m): Ar[ij_|k] = (Ar[ij_|k] + Br[i_|k] * Ar[j_|k]) % mod
    for i in range(n+1):
        i = i << N
        for k in range(m): Ar[i|k|m] += Ar[i|k]
