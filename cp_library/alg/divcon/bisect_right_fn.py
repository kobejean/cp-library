import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.divcon.__header__

def bisect_right(A, x, l, r):
    while l<r:
        if x<A[m:=(l+r)>>1]:r=m
        else:l=m+1
    return l