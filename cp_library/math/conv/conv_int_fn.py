import cp_library.__header__
from typing import Union
import cp_library.math.__header__
import cp_library.math.conv.__header__

def conv_int(A: list[int], B: list[int], N: Union[int, None] = None) -> list[int]:
    n,m = len(A),len(B)
    N = n+m-1 if N is None else N
    m1, m2, m3 = 754974721, 167772161, 469762049
    m2m3, m1m3, m1m2, m1m2m3 = m2*m3, m1*m3, m1*m2, m1*m2*m3
    i1, i2, i3 = mod_inv(m2m3, m1), mod_inv(m1m3, m2), mod_inv(m1m2, m3)
    ntt1, ntt2, ntt3 = NTT(m1), NTT(m2), NTT(m3)
    C,C1,C2,C3 = [0]*N, ntt1.conv(A, B), ntt2.conv(A, B), ntt3.conv(A, B)
    for i in range(N):
        C[i] = (C1[i]*i1%m1*m2m3+C2[i]*i2%m2*m1m3+C3[i]*i3%m3*m1m2)%m1m2m3
    return C

from cp_library.math.nt.ntt_cls import NTT
from cp_library.math.nt.mod_inv_fn import mod_inv