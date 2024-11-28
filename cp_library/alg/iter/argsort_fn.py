import cp_library.alg.iter.__header__

def argsort(A: list[int]):
    N = len(A)
    mask = (1 << (shift := N.bit_length())) - 1
    indices = [0]*N
    for i in range(N):
        indices[i] = A[i] << shift | i
    indices.sort()
    for i in range(N):
        indices[i] &= mask
    return indices
