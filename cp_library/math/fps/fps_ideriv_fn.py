import cp_library.math.fps.__header__

def fps_ideriv(P: list[int]):
    for i in range(1,len(P)): P[i-1] = P[i]*i%mint.mod
    del P[-1]
    return P

from cp_library.math.mod.mint_cls import mint