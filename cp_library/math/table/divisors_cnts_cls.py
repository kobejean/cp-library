import cp_library.math.table.__header__

class DivisorCounts(list[tuple[int,int]]):
    def __init__(D, N):
        super().__init__()
        k = 1
        while k <= N:
            D.append((d := N//k, -k + (k := N//d+1)))
        D.reverse()
