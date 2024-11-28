import cp_library.alg.iter.__header__
from typing import Reversible

def rev_enumerate(A: Reversible, start: int = 0):
    A = list(enumerate(A, start))
    return A[::-1]