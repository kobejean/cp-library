import cp_library.__header__
from typing import Sequence
from cp_library.misc.typing import _T
import cp_library.alg.__header__
import cp_library.alg.iter.__header__

def shift(A: Sequence[_T], offset=-1):
    return [a+offset for a in A]