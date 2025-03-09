import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.conv.__header__

def subset_zeta(A: list[int], N: int):
    Z = len(A)
    for i in range(N):
        m = b = 1<<i
        while m < Z:
            A[m] += A[m^b]
            m = m+1|b
    return A