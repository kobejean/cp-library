import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.conv.__header__
from cp_library.math.conv.fwht_fn import fwht
import cp_library.math.conv.mod.__header__

def fwht_inv(A: list, N: int, mod: int):
    fwht(A, N)
    inv = pow(len(A), -1, mod)
    for i, a in enumerate(A): A[i] = a%mod * inv%mod
    return A
