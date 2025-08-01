import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.conv.__header__
from cp_library.math.conv.iand_zeta_pair_fn import iand_zeta_pair
from cp_library.math.conv.iand_mobius_fn import iand_mobius

def iand_conv(A: list[int], B: list[int], N: int) -> list[int]:
    assert len(A) == len(B)
    iand_zeta_pair(A, B, N)
    for i, b in enumerate(B): A[i] *= b
    iand_mobius(A, N)
    return A