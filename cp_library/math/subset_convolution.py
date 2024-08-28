from cp_library.math.fzt import fzt
from cp_library.math.ifzt import ifzt

def subset_convolution(A, B):
    N = max(len(A), len(B)).bit_length()
    Z = 1 << (N-1)

    # Prepare arrays for rank (popcount) decomposition
    Arank = [[0]*Z for _ in range(N)]
    Brank = [[0]*Z for _ in range(N)]

    # Initialize rank arrays
    for mask in range(Z):
        rank = mask.bit_count()
        Arank[rank][mask] = A[mask]
        Brank[rank][mask] = B[mask]

    # Zeta transform for each rank
    for Ar in Arank: fzt(Ar)
    for Br in Brank: fzt(Br)

    # Convolution
    Crank = [[0 for _ in range(Z)] for _ in range(N)]
    for mask in range(Z):
        L = mask.bit_count()+1
        for i in range(L):
            for j in range(min(L, N-i)):
                k = i+j
                Crank[k][mask] = Crank[k][mask] + Arank[i][mask] * Brank[j][mask]

    # Möbius transform (inverse of Zeta transform)
    for Cr in Crank: ifzt(Cr)
        
    # Combine results
    C = [0] * Z
    for mask in range(Z):
        rank = mask.bit_count()
        C[mask] = Crank[rank][mask]

    return C
