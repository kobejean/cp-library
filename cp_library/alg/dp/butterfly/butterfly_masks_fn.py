import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.dp.__header__
import cp_library.alg.dp.butterfly.__header__

def butterfly_masks(N, Z):
    for i in range(N):
        m = b = 1<<i
        while m < Z:
            yield m^b, m
            m = (m+1)|b

def ixor(A: list, N: int):
    for m0, m1 in butterfly_masks(N, len(A)):
        a0, a1 = A[m0], A[m1]
        A[m0], A[m1] = a0+a1, a0-a1
    return A

def ior_zeta(A: list[int], N: int):
    for m0, m1 in butterfly_masks(N, len(A)):
        A[m1] += A[m0]
    return A

def ior_zeta_pair(A: list[int], B: list[int], N: int):
    for m0, m1 in butterfly_masks(N, len(A)):
        A[m1] += A[m0]
        B[m1] += B[m0]
    return A, B

def ior_mobius(A: list[int], N: int):
    for m0, m1 in butterfly_masks(N, len(A)):
        A[m1] -= A[m0]
    return A

def iand_zeta(A, N: int):
    for m0, m1 in butterfly_masks(N, len(A)):
        A[m0] += A[m1]
    return A

def iand_mobius(A, N: int):
    for m0, m1 in butterfly_masks(N, len(A)):
        A[m0] -= A[m1]
    return A

def popcnts(N):
    P = [0]*(1 << N)
    for i in range(N):
        for m in range(b := 1<<i):
            P[m^b] = P[m] + 1
    return P

def subset_conv(A,B,N):
    assert len(A) == len(B)
    Z = (N+1)*(M := 1<<N)
    Ar,Br,Cr,P = [0]*Z, [0]*Z, [0]*Z, popcnts(N)
    for i,p in enumerate(P): Ar[p<<N|i], Br[p<<N|i] = A[i], B[i]
    ior_zeta_pair(Ar, Br, N)
    for i in range(0,Z,M):
        for j in range(0,Z-i,M):
            ij = i+j
            for k in range(M): Cr[ij|k] += Ar[i|k] * Br[j|k]
    ior_mobius(Cr, N)
    for i,p in enumerate(P): A[i] = Cr[p<<N|i]
    return A