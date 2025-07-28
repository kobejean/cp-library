import cp_library.math.fps.__header__

def fps_integ(P: list) -> list:
    N, mod = len(P), mint.mod; res = [0] * (N+1)
    if N: res[1] = 1
    for i in range(2, N+1): j, k = divmod(mod, i); res[i] = (-res[k] * j) % mod
    for i, x in enumerate(P, start=1): res[i] = res[i] * x % mod
    return res

from cp_library.math.mod.mint_cls import mint