import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.iter.__header__
import cp_library.alg.iter.arg.__header__

def argmax(A, l = 0, r=None):
    if r is None: r = len(A)
    if l == r: return -1
    m = l
    while (l:=l+1)<r:
        if A[m] < A[l]: m = l
    return m