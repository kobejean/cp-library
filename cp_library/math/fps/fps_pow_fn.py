import cp_library.math.fps.__header__
from cp_library.math.fps.fps_log_fn import fps_log
from cp_library.math.fps.fps_exp_fn import fps_exp
from cp_library.math.fps.fps_normalize_fn import fps_normalize

def fps_pow(P: list, k: int, deg = -1) -> list:
    deg, mod = (len(P) if deg<0 else deg), mint.mod
    if k == 0: return [1]+[0]*(deg-1) if deg else []
    i = next((i for i, c in enumerate(P) if c), default=deg)
    if i * k >= deg: return [0] * deg
    inv, alpha = mod_inv(P[i],mod), pow(P[i], k, mod)
    R = fps_log([P[j]*inv%mod for j in range(i,deg)])
    for j,r in enumerate(R): R[j] = r*k%mod
    R = fps_exp(R)
    for j,r in enumerate(R): R[j] = r*alpha%mod
    R[:0] = [0] * (i * k)
    return fps_normalize(R, deg)
from cp_library.math.mod.mint_ntt_cls import mint
from cp_library.math.nt.mod_inv_fn import mod_inv
