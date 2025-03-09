import cp_library.math.series.__header__

def geosum(a, r, n):
    if r == 1: return a*n
    return a*(pow(r,n)-1)//(r-1)
