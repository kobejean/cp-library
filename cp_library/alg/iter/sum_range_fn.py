import cp_library.__header__
from typing import SupportsIndex
import cp_library.alg.__header__
import cp_library.alg.iter.__header__
from cp_library.misc.typing import _T

def sum_range(A: list[_T], l: SupportsIndex, r: SupportsIndex, step: SupportsIndex = 1, /, initial: _T = 0) -> _T:
    for i in range(l,r,step): initial += A[i]
    return initial
