import cp_library.alg.iter.__header__
from cp_library.alg.iter.argsort_fn import argsort

def sort_parallel(*L: list, reverse=False):
    N = len(L[0])
    order = argsort(L[0])
    if reverse:
        order.reverse()
    inv = [-1]*N
    for i in range(N):
        inv[order[i]] = i
    for j in range(N):
        i, k = inv[j], order[j]
        for A in L:
            A[j], A[k] = A[k], A[j] 
        order[i], inv[k] = k, i
    return L
