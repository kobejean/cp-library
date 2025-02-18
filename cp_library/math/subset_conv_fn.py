import cp_library.math.mod.__header__
from cp_library.bit.popcnts_fn import popcnts
from cp_library.math.subset_zeta_pair_fn import subset_zeta_pair
from cp_library.math.subset_mobius_fn import subset_mobius

def subset_conv(A,B,N):
    Z = (N+1)*(M := 1<<N)
    Ar,Br,Cr,P = [0]*Z, [0]*Z, [0]*Z, popcnts(N)
    for i,p in enumerate(P): Ar[p<<N|i], Br[p<<N|i] = A[i], B[i]
    subset_zeta_pair(Ar, Br, N, Z)
    for i in range(0,Z,M):
        for j in range(0,Z-i,M):
            ij = i+j
            for k in range(M): Cr[ij|k] += Ar[i|k] * Br[j|k]
    subset_mobius(Cr, N, Z)
    for i,p in enumerate(P): A[i] = Cr[p<<N|i]
    return A