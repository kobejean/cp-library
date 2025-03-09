import cp_library.math.series.mod.__header__
from cp_library.math.nt.mod_inv_fn import mod_inv

def geosum(a, r, n, mod):
    if r == 1: return a*n
    return a*(pow(r,n,mod)-1)%mod*mod_inv(r-1, mod)%mod
