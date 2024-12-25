import cp_library.math.fps.__header__

def fps_normalize(P: list, deg) -> list:
    if (N:=len(P)) < deg: P[N:] = [0]*(deg-N)
    del P[deg:]
    return P
