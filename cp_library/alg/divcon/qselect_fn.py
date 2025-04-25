import cp_library.alg.divcon.__header__
from cp_library.alg.divcon.median_of_three_fn import median_of_three
from cp_library.alg.divcon.partition_fn import partition

def qselect(A, k, l=0, r=None):
    '''Find kth element in subarray [l,r)'''
    if r is None: r = len(A)
    while l != r-1:
        if k < (p := partition(A, l, r, median_of_three(A,l,r))): r = p
        elif k > p: l = p+1
        else: return A[k]
    return A[k]
