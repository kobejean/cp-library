from cp_library.alg.kthelement import kth_element

def median(A):
    A = list(A)
    n = len(A)
    m = n // 2
    ret = kth_element(A, m)
    if n % 2 == 0:
        return (ret + kth_element(A, m-1)) / 2
    return ret