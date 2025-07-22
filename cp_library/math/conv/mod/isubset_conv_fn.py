import cp_library.__header__
from cp_library.bit.popcnts_fn import popcnts
import cp_library.math.__header__
import cp_library.math.conv.__header__
from cp_library.math.conv.subset_zeta_pair_fn import subset_zeta_pair
from cp_library.math.conv.subset_mobius_fn import subset_mobius
import cp_library.math.conv.mod.__header__

def isubset_conv(A: list[int], B: list[int], N: int, mod: int) -> list[int]:
    Z = (N+1)*(M := 1<<N)
    Ar,Br,Cr,P = [0]*Z, [0]*Z, [0]*Z, popcnts(N)
    for i,p in enumerate(P):
        P[i] = p = p<<N|i
        Ar[p], Br[p] = A[i], B[i]
    subset_zeta_pair(Ar, Br, N)
    for i in range(Z): Ar[i], Br[i] = Ar[i]%mod, Br[i]%mod
    for i in range(0,Z,M):
        for j in range(0,Z-i,M):
            ij = i+j
            for k in range(M): Cr[ijk] = (Cr[ijk:=ij|k] + Ar[i|k] * Br[j|k]) % mod
    subset_mobius(Cr, N)
    for i,p in enumerate(P): A[i] = Cr[p] % mod
    return A