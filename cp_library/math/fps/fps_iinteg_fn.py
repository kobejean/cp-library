import cp_library.math.fps.__header__

def fps_iinteg(P: list) -> list:
    N, mod = len(P), mint.mod
    inv = [0] * (N+1)
    P.append(0)
    if N:
        inv[1] = 1
    for i in range(2, N+1):
        j, k = divmod(mod, i)
        inv[i] = (-inv[k] * j) % mod
    for i in range(N,0,-1):
        P[i] = inv[i] * P[i-1] % mod
    P[0] = 0
    return P

from cp_library.math.mod.mint_cls import mint