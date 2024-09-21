import cp_library.math.mod.__header__

def zeta_transform(A, N, mod):
    for i in range(N):
        bit = 1 << i
        for mask in range(1 << N):
            if mask & bit:
                A[mask] = (A[mask] + A[mask ^ bit]) % mod
    return A
