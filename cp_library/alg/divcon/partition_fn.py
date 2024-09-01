
def partition(A, l, r, pi) -> int:
    '''Partition subarray [l,r)'''
    r -= 1
    A[pi], A[r] = A[r], A[pi]
    pi = l
    for j in range(l, r):
        if A[j] <= A[r]:
            A[pi], A[j] = A[j], A[pi]
            pi += 1
    A[pi], A[r] = A[r], A[pi]
    return pi
