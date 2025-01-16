import cp_library.alg.iter.__header__
from typing import MutableSequence
from cp_library.misc.typing import _T

def shift(A: MutableSequence[_T], offset=1):
    for i in range(len(A)): A[i] += offset
    return A