import cp_library.math.table.__header__
from typing import SupportsIndex
from cp_library.math.table.modcomb_cls import modcomb
from cp_library.math.mod.mint_cls import mint
from cp_library.math.fps.fps_pow_fn import fps_pow

def stirling2_k(n: SupportsIndex, k: SupportsIndex):
    kinv,fact,mod = modcomb.fact_inv[k],modcomb.fact,mint.mod
    R = fps_pow(modcomb.fact_inv[1:n+2-k],k,n+1-k)
    return [mint(r*kinv%mod*fact[i]) for i,r in enumerate(R,start=k)]