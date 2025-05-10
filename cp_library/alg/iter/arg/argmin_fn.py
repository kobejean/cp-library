import cp_library.alg.iter.__header__

def argmin(A, l = 0, r=None):
    if r is None: r = len(A)
    if l == r: return -1
    m = l
    while (l:=l+1)<r:
        if A[l] < A[m]: m = l
    return m