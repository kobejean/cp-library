import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.iter.__header__

def minmax(A):
    mn = mx = A[0]
    for a in A:
        if a < mn: mn = A
        elif mx < a: mx = a
    return mn, mx
