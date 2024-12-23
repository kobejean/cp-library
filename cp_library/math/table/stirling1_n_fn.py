import cp_library.math.table.__header__
from typing import SupportsIndex
from cp_library.math.mod.mint_ntt_cls import mint
from cp_library.math.fps.tayler_shift_fn import tayler_shift

def stirling1_n(n: SupportsIndex, signed = True):
    conv,res,t = mint.ntt.conv,[1],0
    for i in range(n.bit_length()-1,-1,-1):
        res,t = conv(res,tayler_shift(res,-t)),t<<1
        if n>>i&1:res,t = conv(res,[-t,1]),t+1
    if signed: return [mint(res[k]) for k in range(n+1)]
    else: return [mint(-res[k] if (k^n)&1 else res[k]) for k in range(n+1)]
