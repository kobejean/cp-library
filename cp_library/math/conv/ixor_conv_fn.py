import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.conv.__header__
from cp_library.math.conv.ixor_mobius_fn import ixor_mobius
from cp_library.math.conv.ixor_zeta_pair_fn import ixor_zeta_pair

def ixor_conv(A: list, B: list, N: int):
    assert len(A) == len(B)
    ixor_zeta_pair(A, B, N)
    for i, b in enumerate(B): A[i] *= b
    ixor_mobius(A, N)
    return A
