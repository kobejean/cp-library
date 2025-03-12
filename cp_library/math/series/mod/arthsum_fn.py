import cp_library.math.series.__header__

def arthsum(d, a, n, mod):
    return (((n-1)*d+(a<<1)) % mod * n >> 1) % mod