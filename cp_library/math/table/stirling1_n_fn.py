import cp_library.math.table.__header__
from typing import SupportsIndex
from cp_library.math.mod.mint_ntt_cls import mint
from cp_library.math.fps.fps_tayler_shift_fn import fps_tayler_shift

def stirling1_n(n: SupportsIndex, signed = True):
    conv,res,t,d = mint.ntt.conv,[1],0,(-1 if signed else 1)
    for i in range(n.bit_length()-1,-1,-1):
        res,t = conv(res,fps_tayler_shift(res,t)),t<<1
        if n>>i&1:res,t = conv(res,[t,1]),t+d
    return [mint(res[k]) for k in range(n+1)]
