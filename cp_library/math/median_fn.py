import cp_library.__header__
from cp_library.alg.divcon.qselect_fn import qselect
import cp_library.math.__header__

def median(A):
    med = qselect(A, M := (N := len(A)) >> 1)
    return med if N&1 else (med + qselect(A, M-1)) >> 1
