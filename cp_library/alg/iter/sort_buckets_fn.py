import cp_library.alg.iter.__header__
from itertools import groupby
from operator import itemgetter

def sort_buckets(A, N, key=0):
    if isinstance(key,int):
        key = itemgetter(key)
    A.sort(key=key)
    B = [[] for _ in range(N)]
    for k,g in groupby(A, key=key):
        B[k] = list(g)
    return B
    