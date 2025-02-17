import cp_library.alg.iter.__header__

def argsort(A: list[int], reverse=False):
    mask, I = (1 << (shift := (N := len(A)).bit_length())) - 1, [0]*N
    if reverse:
        for i in range(N): I[i] = A[i] << shift | (i ^ mask)
        I.sort(reverse=True)
        for i in range(N): I[i] = (I[i] & mask) & mask
    else:
        for i in range(N): I[i] = A[i] << shift | i
        I.sort()
        for i in range(N): I[i] &= mask
    return I
