import cp_library.math.table.__header__

class Divisors(list[int]):
    def __init__(D, N):
        super().__init__()
        C = []
        for x in range(1,N+1):
            if x*x>N: break
            if N % x == 0:
                D.append(x)
                C.append(N//x)
        if C[-1] == D[-1]: C.pop()
        D.extend(reversed(C))
