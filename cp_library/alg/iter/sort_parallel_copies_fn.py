import cp_library.alg.iter.__header__
from cp_library.alg.iter.argsort_fn import argsort

def sort_parallel_copies(*L: list, reverse=False):
    N, K = len(L[0]), len(L)
    order = argsort(L[0], reverse)
    R = tuple([0]*N for _ in range(K))
    for k, Llst in enumerate(L):
        Rlst = R[k]
        for ri, li in enumerate(order):
            Rlst[ri] = Llst[li]
    return R
