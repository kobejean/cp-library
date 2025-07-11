import cp_library.__header__
from typing import Reversible
import cp_library.alg.__header__
import cp_library.alg.iter.__header__

def rev_enumerate(A: Reversible, start: int = 0):
    start += (N := len(A))
    for i in range(N-1,-1,-1):
        yield (start:=start-1), A[i]