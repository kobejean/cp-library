import cp_library.__header__
from cp_library.ds.view.view_cls import view
import cp_library.math.__header__
import cp_library.math.sps.__header__

def sps_exp_small(P, mod):
    assert P[0] == 0
    N = len(P).bit_length() - 1
    Z = 1<<N
    exp = [0]*Z; exp[0] = 1
    for i in range(1, Z):
        fg, b, j = 0, 1 << (i.bit_length() - 1), i-1&i
        while b <= j:
            fg += P[j] * exp[i^j] % mod
            j = j-1&i
        exp[i] = (P[i] + fg) % mod
    return exp
