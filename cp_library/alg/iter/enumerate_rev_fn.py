import cp_library.alg.iter.__header__
from typing import Reversible

def enumerate_rev(A: Reversible, start: int = 0):
    A = list(enumerate(reversed(A), start))
    return A