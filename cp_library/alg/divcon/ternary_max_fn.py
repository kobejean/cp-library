import cp_library.alg.divcon.__header__

def ternary_max(lo, hi, f):
    while hi - lo > 2:
        m2 = (m1 := (lo+hi)//2)+1
        if f(m1) < f(m2): lo = m1
        else: hi = m2
    return f(lo+1)