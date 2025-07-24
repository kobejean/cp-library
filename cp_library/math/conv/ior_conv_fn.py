import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.conv.__header__
from cp_library.math.conv.ior_zeta_pair_fn import ior_zeta_pair
from cp_library.math.conv.ior_mobius_fn import ior_mobius

def ior_conv(A: list[int], B: list[int], N: int) -> list[int]:
    assert len(A) == len(B)
    ior_zeta_pair(A, B, N)
    for i, b in enumerate(B): A[i] *= b
    return ior_mobius(A, N)
