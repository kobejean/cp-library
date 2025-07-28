import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.nt.__header__

def mod_inv(x, mod):
    a, b, s, t = x, mod, 1, 0
    while b:
        a, b, s, t = b,a%b,t,s-a//b*t
    if a == 1: return s % mod
    raise ValueError(f"{x} is not invertible in mod {mod}")
