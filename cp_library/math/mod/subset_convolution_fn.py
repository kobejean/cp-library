
def subset_convolution(A, B, N, mod):
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
    for Ar in Arank: zeta_transform(Ar, N, mod)
    for Br in Brank: zeta_transform(Br, N, mod)

    # Convolution
    Crank = [[0]*Z for _ in range(N+1)]
    for mask in range(Z):
        L = mask.bit_count()+1
        for i in range(L):
            for j in range(min(L, N+1-i)):
                k = i+j
                Crank[k][mask] = (Crank[k][mask] + Arank[i][mask] * Brank[j][mask]) % mod

    # Möbius transform (inverse of Zeta transform)
    for Cr in Crank: mobius_transform(Cr, N, mod)
        
    # Combine results
    C = [0] * Z
    for mask in range(Z):
        rank = mask.bit_count()
        C[mask] = Crank[rank][mask]

    return C

from cp_library.math.mod.zeta_transform_fn import zeta_transform
from cp_library.math.mod.mobius_transform_fn import mobius_transform