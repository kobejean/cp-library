import cp_library.math.conv.mod.__header__
from cp_library.math.conv.fwht_pair_fn import fwht_pair
from cp_library.math.conv.fwht_fn import fwht

def xor_conv(A: list, B: list, N: int, mod: int):
    assert len(A) == len(B)
    fwht_pair(A, B, N)
    for i, b in enumerate(B): A[i] = A[i]%mod * (b%mod) % mod
    fwht(A, N)
    inv = pow(len(A), -1, mod)
    for i, a in enumerate(A): A[i] = a%mod * inv%mod
    return A
