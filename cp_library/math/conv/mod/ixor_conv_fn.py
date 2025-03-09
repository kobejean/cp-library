import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.conv.__header__
import cp_library.math.conv.mod.__header__
from cp_library.math.conv.mod.fwht_inv_fn import fwht_inv
from cp_library.math.conv.fwht_pair_fn import fwht_pair

def ixor_conv(A: list[int], B: list[int], N: int, mod: int) -> list[int]:
    assert len(A) == len(B)
    fwht_pair(A, B, N)
    for i, b in enumerate(B): A[i] = A[i]%mod * (b%mod) % mod
    fwht_inv(A, N, mod)
    return A
