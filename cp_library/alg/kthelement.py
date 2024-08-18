from cp_library.alg.partition import partition

def kth_element(A, k, l=0, r=None):
    if r is None:
        r = len(A) - 1
    
    while True:
        if l == r: return A[k]
        pi = partition(A, l, r)
        
        if k == pi:
            return A[k]
        elif k < pi:
            r = pi - 1
        else:
            l = pi + 1
