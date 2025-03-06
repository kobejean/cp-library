import cp_library.alg.iter.__header__
from typing import MutableSequence
from cp_library.misc.typing import _T

def ishift(A: MutableSequence[_T], offset=-1):
    for i,a in enumerate(A): A[i] = a+offset
    return A