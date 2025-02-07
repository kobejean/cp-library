import cp_library.alg.divcon.__header__
from random import randint
from cp_library.alg.divcon.partition_fn import partition

def qselect(A, k, l=0, r=None):
    '''Find kth element in subarray [l,r)'''
    if r is None: r = len(A)
    while l != r-1:
        if k < (p := partition(A, l, r, randint(l,r-1))): r = p
        elif k > p: l = p+1
        else: return A[k]
    return A[k]
