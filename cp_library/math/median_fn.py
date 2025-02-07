import cp_library.math.__header__

def median(A):
    med = qselect(A, M := (N := len(A)) >> 1)
    if N&1: return med
    return (med + qselect(A, M-1)) >> 1

from cp_library.alg.divcon.qselect_fn import qselect