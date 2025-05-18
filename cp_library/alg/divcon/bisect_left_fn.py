import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.divcon.__header__

def bisect_left(A, x, l, r):
    while l<r:
        if A[m:=(l+r)>>1]<x:l=m+1
        else:r=m
    return l