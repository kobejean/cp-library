import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.series.__header__

def geosum(a, r, n): return a*n if r == 1 else a*(pow(r,n)-1)//(r-1)