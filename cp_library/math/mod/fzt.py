
def fzt(A, mod):
    N = len(A).bit_length()-1

    for i in range(N):
        bit = 1 << i
        for mask in range(1 << N):
            if mask & bit:
                A[mask] = (A[mask] + A[mask ^ bit]) % mod

    return A
