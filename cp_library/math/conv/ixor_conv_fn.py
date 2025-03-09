import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.conv.__header__
from cp_library.math.conv.fwht_inv_fn import fwht_inv
from cp_library.math.conv.fwht_pair_fn import fwht_pair

def ixor_conv(A: list, B: list, N: int):
    assert len(A) == len(B)
    fwht_pair(A, B, N)
    for i, b in enumerate(B): A[i] *= b
    fwht_inv(A, N)
    return A
