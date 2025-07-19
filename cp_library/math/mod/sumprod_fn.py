import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.mod.__header__

def sumprod(A, B, mod):
    assert len(A) == len(B)
    ret = 0
    for i in range(len(A)): ret = (ret + A[i]*B[i]%mod) % mod
    return ret