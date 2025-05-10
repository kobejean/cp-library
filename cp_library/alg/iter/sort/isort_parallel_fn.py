import cp_library.alg.iter.__header__
from cp_library.alg.iter.arg.argsort_fn import argsort

def isort_parallel(*L: list, reverse=False):
    inv, order = [0]*len(L[0]), argsort(L[0], reverse=reverse)
    for i, j in enumerate(order): inv[j] = i
    for i, j in enumerate(order):
        for A in L: A[i], A[j] = A[j], A[i]
        order[inv[i]], inv[j] = j, inv[i]
    return L
