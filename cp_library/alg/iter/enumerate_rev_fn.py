import cp_library.alg.iter.__header__
from typing import Reversible

def enumerate_rev(A: Reversible, start: int = 0):
    start -= 1
    for i in range(len(A)-1,-1,-1):
        yield (start:=start+1), A[i]