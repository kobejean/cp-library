import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.conv.__header__

def fwht_pair(A: list[int], B: list[int], N: int):
    Z = len(A)
    for i in range(N):
        m = b = 1<<i
        while m < Z:
            a0, a1, b0, b1 = A[m^b], A[m], B[m^b], B[m]
            A[m^b], A[m], B[m^b], B[m] = a0+a1, a0-a1, b0+b1, b0-b1
            m = m+1|b
    return A, B
