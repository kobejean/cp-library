import cp_library.math.series.__header__

def arthsum(d, n, a = 0):
    return (a << 1 + (n-1) * d) * n >> 1
