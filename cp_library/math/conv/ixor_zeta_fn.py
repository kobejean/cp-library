import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.conv.__header__

def ixor_zeta(A: list, N: int):
    Z = len(A)
    for i in range(N):
        m = b = 1<<i
        while m < Z:
            a0, a1 = A[m^b], A[m]
            A[m^b], A[m] = a0+a1, a0-a1
            m = m+1|b
    return A
