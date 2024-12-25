import cp_library.math.fps.__header__

def fps_deriv(P: list[int]):
    mod = mint.mod
    return [P[i]*i%mod for i in range(1,len(P))]

from cp_library.math.mod.mint_cls import mint