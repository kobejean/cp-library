import random

def partition(A, l, r):
    pi = random.randint(l, r)
    A[pi], A[r] = A[r], A[pi]
    pivot = A[r]
    i = l - 1
    
    for j in range(l, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1
