import cp_library.math.__header__

def subset_conv(A, B, N):
    Z = 1 << N

    # Prepare arrays for rank (popcount) decomposition
    Arank = [[0]*Z for _ in range(N+1)]
    Brank = [[0]*Z for _ in range(N+1)]

    # Initialize rank arrays
    for mask in range(Z):
        rank = mask.bit_count()
        Arank[rank][mask] = A[mask]
        Brank[rank][mask] = B[mask]

    # Zeta transform for each rank
    for Ar in Arank: subset_zeta(Ar, N)
    for Br in Brank: subset_zeta(Br, N)

    # Convolution
    Crank = [[0 for _ in range(Z)] for _ in range(N+1)]
    for mask in range(Z):
        for i in range(L := mask.bit_count()+1):
            for j in range(min(L, N+1-i)):
                k = i+j
                Crank[k][mask] = Crank[k][mask] + Arank[i][mask] * Brank[j][mask]

    # Möbius transform (inverse of Zeta transform)
    for Cr in Crank: subset_mobius(Cr, N)
        
    # Combine results
    C = [0] * Z
    for mask in range(Z):
        rank = mask.bit_count()
        C[mask] = Crank[rank][mask]

    return C

from cp_library.math.subset_zeta_fn import subset_zeta
from cp_library.math.subset_mobius_fn import subset_mobius