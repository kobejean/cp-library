import cp_library.alg.iter.__header__
from cp_library.alg.iter.argsort_fn import argsort

def sort_parallel(*L: list, reverse=False):
    inv, order = [-1]*(N := len(L[0])), argsort(L[0], reverse=reverse)
    for i, idx in enumerate(order): inv[idx] = i
    for j in range(N):
        i, k = inv[j], order[j]
        for A in L: A[j], A[k] = A[k], A[j] 
        order[i], inv[k] = k, i
    return L
