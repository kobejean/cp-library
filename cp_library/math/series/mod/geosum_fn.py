import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.series.__header__
import cp_library.math.series.mod.__header__
from cp_library.math.nt.mod_inv_fn import mod_inv

def geosum(a, r, n, mod): return a*n if r == 1 else a*(pow(r,n,mod)-1)%mod*mod_inv(r-1, mod)%mod