import cp_library.math.__header__

def sumprod(A, B):
    assert len(A) == len(B)
    ret = 0
    for i,a in enumerate(A):
        ret += a*B[i]
    return ret