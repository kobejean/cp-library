import cp_library.math.__header__

def sumprod(A, B):
    assert len(A) == len(B)
    ret = 0
    for i in range(len(A)):
        ret += A[i]*B[i]
    return ret