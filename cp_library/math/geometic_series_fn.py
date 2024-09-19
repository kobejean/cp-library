import cp_library.math.__init__

def geometric_series(r, n, a=1):
    if r == 1:
        return a * n
    else:
        return a * (1 - r**n) // (1 - r)
