import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.iter.__header__
from cp_library.alg.iter.arg.argsort_ranged_fn import argsort_ranged
import cp_library.alg.iter.sort.__header__

def isort_ranged(*L: list, l: int, r: int, reverse=False):
    n = r - l
    order = argsort_ranged(L[0], l, r, reverse=reverse)
    inv = [0] * n
    # order contains indices in range [l, r), need to map to [0, n)
    for i in range(n): inv[order[i]-l] = i
    for i in range(n):
        j = order[i] - l  # j is in range [0, n)
        for A in L: A[l+i], A[l+j] = A[l+j], A[l+i]
        order[inv[i]], order[inv[j]] = order[inv[j]], order[inv[i]]
        inv[i], inv[j] = inv[j], inv[i]
    return L