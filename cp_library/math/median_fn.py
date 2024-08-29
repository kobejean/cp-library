from cp_library.alg.divcon.qselect_fn import qselect

def median(A):
    n = len(A)
    m = n // 2
    ret = qselect(A, m)
    if n % 2 == 0:
        return (ret + qselect(A, m-1)) / 2
    return ret