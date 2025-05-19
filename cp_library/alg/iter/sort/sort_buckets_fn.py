import cp_library.__header__
from itertools import groupby
from operator import itemgetter
import cp_library.alg.__header__
import cp_library.alg.iter.__header__
import cp_library.alg.iter.sort.__header__

def sort_buckets(A, N, key=0):
    if isinstance(key,int): key = itemgetter(key)
    B = [[] for _ in range(N)]; A.sort(key=key)
    for k, g in groupby(A, key=key): B[k] = list(g)
    return B
    