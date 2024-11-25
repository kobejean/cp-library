import cp_library.alg.iter.__header__
from itertools import groupby
from operator import itemgetter

def sort_groups(A, key=None):
    if isinstance(key,int):
        key = itemgetter(key)
    A.sort(key=key)
    return sorted((k,list(g)) for k,g in groupby(A, key=key))
    