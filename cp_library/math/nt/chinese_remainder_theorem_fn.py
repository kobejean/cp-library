import cp_library.math.nt.__header__
from math import prod
from cp_library.math.nt.mod_inv_fn import mod_inv

def chinese_remainder_theorem(rems, mods):
    mod = prod(mods)
    a = 0
    for r,m in zip(rems, mods):
        M = mod // m
        N = mod_inv(M, m)
        a += r*M*N % mod
    return a % mod