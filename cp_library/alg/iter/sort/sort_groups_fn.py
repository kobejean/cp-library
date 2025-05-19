import cp_library.__header__
from itertools import groupby
from operator import itemgetter
import cp_library.alg.__header__
import cp_library.alg.iter.__header__
import cp_library.alg.iter.sort.__header__

def sort_groups(A, key=0):
    if isinstance(key,int):
        key = itemgetter(key)
    A.sort(key=key)
    return sorted((k,list(g)) for k,g in groupby(A, key=key))

    