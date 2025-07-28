import cp_library.math.fps.__header__

def fps_ideriv_k(P: list[int], k: int):
    fact, inv, mod = mcomb.fact, mcomb.fact_inv, mint.mod
    for i in range(k,len(P)): P[i-k] = P[i]*inv[i-k]%mod*fact[i]%mod
    del P[-k:]
    return P
from cp_library.math.mod.mint_cls import mint
from cp_library.math.table.mcomb_cls import mcomb