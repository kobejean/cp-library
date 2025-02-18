import cp_library.bit.__header__

def popcnts(N):
    P = [0]*(1 << N)
    for i in range(N):
        for m in range(b := 1<<i):
            P[m^b] = P[m] + 1
    return P
