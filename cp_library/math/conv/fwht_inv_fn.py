import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.conv.__header__
from cp_library.math.conv.fwht_fn import fwht

def fwht_inv(A: list, N: int):
    fwht(A, N)
    for i, a in enumerate(A): A[i] = a >> N
    return A
