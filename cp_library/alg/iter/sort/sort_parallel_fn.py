import cp_library.alg.iter.__header__
from cp_library.alg.iter.arg.argsort_fn import argsort

def sort_parallel(*L: list, reverse=False):
    N, K, order = len(L[0]), len(L), argsort(L[0], reverse)
    R = tuple([0]*N for _ in range(K))
    for k, Lk in enumerate(L):
        Rk = R[k]
        for i, j in enumerate(order): Rk[i] = Lk[j]
    return R
