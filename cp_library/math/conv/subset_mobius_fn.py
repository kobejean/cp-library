import cp_library.math.conv.__header__

def subset_mobius(A: list[int], N: int, Z: int = None):
    Z = len(A)
    for i in range(N):
        m = b = 1<<i
        while m < Z:
            A[m] -= A[m^b]
            m = m+1|b
    return A