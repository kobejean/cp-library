import cp_library.alg.divcon.__header__

def fbisect_left(key, hi, x = True, lo = 0.0, tol=1e-9):
    while hi - lo > tol:            
        mid = (lo + hi) / 2
        if key(mid) >= x: hi = mid
        else: lo = mid
    return lo

def fbisect_right(key, hi, x=False, lo=0.0, tol=1e-9):
    while hi - lo > tol:
        mid = (lo + hi) / 2
        if key(mid) > x: hi = mid
        else: lo = mid
    return hi