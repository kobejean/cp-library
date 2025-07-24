import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.conv.__header__
import cp_library.math.conv.mod.__header__
from cp_library.math.conv.mod.ixor_mobius_fn import ixor_mobius
from cp_library.math.conv.ixor_zeta_pair_fn import ixor_zeta_pair

def ixor_conv(A: list[int], B: list[int], N: int, mod: int) -> list[int]:
    assert len(A) == len(B)
    ixor_zeta_pair(A, B, N)
    for i, b in enumerate(B): A[i] = A[i]%mod * (b%mod) % mod
    ixor_mobius(A, N, mod)
    return A
