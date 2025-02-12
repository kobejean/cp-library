import cp_library.alg.iter.__header__

def argmin(A, l = 0, r=None):
    if r is None: r = len(A)
    if l == r: return -1
    m = l
    for i in range(l+1,r):
        if A[i] < A[m]: m = i
    return m