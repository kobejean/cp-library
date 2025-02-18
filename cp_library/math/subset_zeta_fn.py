import cp_library.math.__header__

def subset_zeta(A: list[int], N: int, Z: int = None):
    Z = 1 << N if Z is None else Z
    for i in range(N):
        m = b = 1<<i
        while m < Z:
            A[m] += A[m^b]
            m = m+1|b
    return A