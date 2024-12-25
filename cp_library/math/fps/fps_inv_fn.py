import cp_library.math.fps.__header__

def fps_inv(P: list) -> list:
    ntt, inv, d = mint.ntt, [0]*(deg:=len(P)), 1
    inv[0] = mod_inv(P[0], mod := mint.mod)
    while d < deg:
        sz, f, g = min(deg,z:=d<<1), [0]*z, [0]*z
        f[:sz], g[:d] = P[:sz], inv[:d]
        ntt.conv_half(f,gres:=ntt.fntt(g))
        f[:d] = [0]*d
        ntt.conv_half(f,gres)
        for j in range(d,sz): inv[j] = mod-f[j] if f[j] else 0
        d = z
    return inv

from cp_library.math.mod.mint_ntt_cls import mint
from cp_library.math.nt.mod_inv_fn import mod_inv