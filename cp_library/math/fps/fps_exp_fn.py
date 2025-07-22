import cp_library.math.fps.__header__
from cp_library.math.fps.fps_deriv_fn import fps_deriv

def fps_exp(P: list) -> list:
    max_sz = 1 << ((deg := len(P))-1).bit_length()
    mcomb.extend_inv(max_sz)
    inv, mod, ntt = mcomb.inv, mint.mod, mint.ntt
    fntt, ifntt, conv_half = ntt.fntt, ntt.ifntt, ntt.conv_half
    dP = fps_deriv(P) + [0]*(max_sz-deg+1)
    R, E, Eres = [1, (P[1] if 1 < deg else 0)], [1], [1, 1]
    reserve(R, max_sz), reserve(E, max_sz)
    p = 2
    while p < deg:
        Rres = fntt(R + [0]*p)
        x = ifntt([Rres[i]*-e%mod for i, e in enumerate(Eres)])
        for i in range(h:=p>>1): x[i] = 0
        E.extend(conv_half(x, Eres)[h:])
        Eres = fntt(E + [0]*p)
        x = conv_half(dP[:p-1]+[0], Rres[:p])
        for i in range(1,p): x[i-1] -= R[i]*i % mod
        x += [0] * p
        for i in range(p-1): x[p+i],x[i] = x[i],0
        conv_half(x,Eres)
        for i in range(min(deg, p<<1)-1,p-1,-1): x[i] = P[i]+x[i-1]*inv[i]%mod 
        for i in range(p): x[i] = 0
        R.extend(conv_half(x,Rres)[p:])
        p <<= 1
    return R[:deg]

from cp_library.ds.reserve_fn import reserve
from cp_library.math.table.mcomb_cls import mcomb
from cp_library.math.mod.mint_ntt_cls import mint