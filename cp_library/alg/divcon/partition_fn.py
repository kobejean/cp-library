import cp_library.alg.divcon.__header__

def partition(A, l, r, p) -> int:
    '''Partition subarray [l,r)'''
    A[p], A[r], p = A[r := r-1], A[p], l
    for j in range(l, r):
        if A[j] <= A[r]: A[p], A[j], p = A[j], A[p], p+1
    A[p], A[r] = A[r], A[p]
    return p
