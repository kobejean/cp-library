import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.conv.__header__

def superset_zeta(A, N: int):
    Z = len(A)
    for i in range(N):
        m = b = 1<<i
        while m < Z:
            A[m^b] += A[m]
            m = m+1|b
    return A
