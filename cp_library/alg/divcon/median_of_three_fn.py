import cp_library.alg.divcon.__header__

def median_of_three(A, l, r):
    '''Select pivot as median of first, middle, and last elements'''
    if r - l < 3: return l
    mid = (l+r) >> 1
    if A[mid] < A[l]: A[l], A[mid] = A[mid], A[l]
    if A[r-1] < A[mid]:
        A[mid], A[r-1] = A[r-1], A[mid]
        if A[mid] < A[l]: A[l], A[mid] = A[mid], A[l]
    return mid