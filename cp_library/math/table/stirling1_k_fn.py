import cp_library.math.table.__header__
from typing import SupportsIndex
from cp_library.math.mod.mint_ntt_cls import mint
from cp_library.math.table.mcomb_cls import mcomb
from cp_library.math.fps.fps_pow_fn import fps_pow

def stirling1_k(n: SupportsIndex, k: SupportsIndex, signed = True):
    mcomb.extend_inv(n+k)
    kinv,fact,mod,deg = mcomb.fact_inv[k],mcomb.fact,mint.mod,n+1-k
    R = mcomb.inv[1:deg+1]
    if signed:
        for i in range(1,deg,2): R[i] = mod - R[i]
    return [mint(r*kinv%mod*fact[i]) for i,r in enumerate(fps_pow(R,k,deg),start=k)]

