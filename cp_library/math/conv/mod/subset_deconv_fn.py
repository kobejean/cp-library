import cp_library.__header__
from cp_library.bit.popcnts_fn import popcnts
import cp_library.math.__header__
import cp_library.math.conv.__header__
from cp_library.math.conv.subset_zeta_pair_fn import subset_zeta_pair
from cp_library.math.conv.subset_mobius_fn import subset_mobius
import cp_library.math.conv.mod.__header__

def subset_deconv(A: list[int], C: list[int], N: int, mod: int) -> list[int]:
    Z = (N+1)*(M := 1<<N)
    Ar,Br,Cr,P = [0]*Z, [0]*Z, [0]*Z, popcnts(N)
    for i,p in enumerate(P):
        P[i] = p = p<<N|i
        Ar[p], Cr[p] = A[i], C[i]
    subset_zeta_pair(Ar, Cr, N)
    for i in range(Z): Ar[i], Cr[i] = Ar[i]%mod, Cr[i]%mod
    inv_A0 = pow(Ar[0], -1, mod)
    for j in range(0, Z, M):
        for k in range(M):
            # Ar[0|k] * Br[j|k] = Cr[ij|k]
            Br[j|k] = (Cr[j|k] * inv_A0) % mod
        for i in range(M, Z-j, M):
            ij = i + j
            for k in range(M):
                # Subtract known terms: Cr[ij|k] -= Ar[i|k] * Br[j|k]
                Cr[ij|k] = (Cr[ij|k] - Ar[i|k] * Br[j|k]) % mod
    subset_mobius(Br, N)
    return [Br[p] % mod for p in P]