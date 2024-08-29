import random
from cp_library.alg.divcon.partition_fn import partition

def qselect(A, k, l=0, r=None):
    '''Find kth element in subarray [l,r)'''
    if r is None: r = len(A)
    while True:
        if l == r-1: return A[k]
        pi = partition(A, l, r, random.randint(l, r-1))
        if k == pi:
            return A[k]
        elif k < pi:
            r = pi
        else:
            l = pi + 1
