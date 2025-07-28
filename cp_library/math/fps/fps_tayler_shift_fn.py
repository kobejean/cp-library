import cp_library.math.fps.__header__
from cp_library.math.table.mcomb_cls import mcomb
from cp_library.math.mod.mint_ntt_cls import mint

def fps_tayler_shift(P, t: int) -> list[int]:
    fact, fact_inv, inv, N, mod = mcomb.fact, mcomb.fact_inv, mcomb.inv, len(P), mint.mod
    mcomb.extend_inv(N)
    R, B = [P[i]*fact[i]%mod for i in range(N-1,-1,-1)], [0]*N; B[0] = 1
    for i in range(1,N): B[i] = B[i-1] * t % mod * inv[i] % mod
    R = mint.ntt.conv(R, B, N)
    return [a*fact_inv[i]%mod for i, a in enumerate(reversed(R))]