import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.iter.__header__
import cp_library.alg.iter.arg.__header__
from cp_library.alg.iter.arg.argsort_fn import argsort

def argsort_bounded(A, mx=None, reverse=False):
    N = len(A)
    if mx is None: mx = max(A)
    if N*N.bit_length() < mx or mx < 1000: return argsort(A, reverse)
    I, cnt, t = [0]*N, [0]*(mx+1), 0
    for a in A: cnt[a] += 1
    if reverse:
        for a in range(mx+1): cnt[~a], t = t, t+cnt[~a]
    else:
        for a in range(mx+1): cnt[a], t = t, t+cnt[a]
    for i,a in enumerate(A): I[cnt[a]] = i; cnt[a] += 1
    return I