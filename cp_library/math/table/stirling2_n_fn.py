import cp_library.math.table.__header__
from typing import SupportsIndex
from cp_library.math.mod.mint_ntt_cls import mint
from cp_library.math.table.mcomb_cls import mcomb

def stirling2_n(n: SupportsIndex):
    inv,conv,sign = mcomb.fact_inv,mint.ntt.conv,(mod:=mint.mod)-1
    A = [inv[t]*pow(t,n,mod)%mod for t in range(n+1)]
    B = [inv[t]*(sign:=mod-sign)%mod for t in range(n+1)]
    return [mint(x) for x in conv(A, B, n+1)]