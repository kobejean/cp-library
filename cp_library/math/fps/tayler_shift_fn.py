import cp_library.math.fps.__header__
from cp_library.math.table.modcomb_cls import modcomb
from cp_library.math.mod.mint_ntt_cls import mint

def tayler_shift(P, c: int) -> list[int]:
    fact, inv, N = modcomb.fact, modcomb.fact_inv, len(P)
    res, B = [int(P[i]*fact[i]) for i in range(N-1,-1,-1)], [0]*N
    B[0] = 1
    for i in range(1, N):
        B[i] = int(B[i - 1] * inv[i] * c * fact[i-1])
    res = mint.ntt.conv(res, B, N)
    return [int(x * inv[i]) for i, x in enumerate(reversed(res))]

