import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.conv.__header__
from cp_library.math.conv.ixor_zeta_fn import ixor_zeta
import cp_library.math.conv.mod.__header__

def ixor_mobius(A: list[int], N: int, mod: int) -> list[int]:
    ixor_zeta(A, N)
    inv = pow(1 << N, -1, mod)
    for i, a in enumerate(A): A[i] = a%mod * inv%mod
    return A
