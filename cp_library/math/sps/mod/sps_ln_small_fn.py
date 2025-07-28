import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.sps.__header__

def sps_ln_small(P, mod):
    assert P[0] == 1
    ln = [0]*(Z:=1<<(N:=len(P).bit_length()-1))
    for i in range(1, Z):
        fg, b, j = 0, 1<<(i.bit_length()-1), i-1&i
        while b <= j: fg += ln[j]*P[i^j]%mod; j = j-1&i
        ln[i] = (P[i]-fg)%mod
    return ln