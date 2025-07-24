import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.conv.__header__
from cp_library.math.conv.ior_zeta_pair_fn import ior_zeta_pair
from cp_library.math.conv.ior_mobius_fn import ior_mobius

def ior_conv(A: list[int], B: list[int], N: int, mod: int) -> list[int]:
    assert len(A) == len(B)
    Z = 1 << N
    ior_zeta_pair(A, B, N)
    for i, b in enumerate(B): A[i] = A[i]*b%mod
    ior_mobius(A, N)
    for i, a in enumerate(Z): A[i] = a%mod
    return A
