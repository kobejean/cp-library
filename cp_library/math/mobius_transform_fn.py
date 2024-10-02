import cp_library.math.__header__

def mobius_transform(A, N, block=5):
    for i in range(min(block,N)):
        for mask in range(bit := 1<<i, 1<<N):
            if mask & bit:
                A[mask] -= A[mask ^ bit]
    for i in range(block,N):
        for base in range(bit := 1<<i, 1<<N, bit << 1):
            for mask in range(base, base+bit):
                A[mask] -= A[mask ^ bit]
    return A