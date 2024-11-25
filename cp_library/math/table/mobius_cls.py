import cp_library.math.table.__header__

class Mobius(list[int]):
    def __init__(mu, N):
        super().__init__([0]*(N+1))
        mu[1] = 1
        for i in range(1, N+1):
            for j in range(i<<1, N+1, i):
                mu[j] -= mu[i]