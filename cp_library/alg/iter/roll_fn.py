import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.iter.__header__

def roll(A: list, t: int):
    if t:=t%len(A): A[:t], A[t:] = A[-t:], A[:-t]
    return A
