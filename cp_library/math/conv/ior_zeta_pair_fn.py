import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.conv.__header__

def ior_zeta_pair(A: list[int], B: list[int], N: int, Z: int = None):
    Z = Z if Z else len(A)
    for i in range(N):
        m = b = 1<<i
        while m < Z: A[m] += A[m^b]; B[m] += B[m^b]; m = m+1|b
    return A, B