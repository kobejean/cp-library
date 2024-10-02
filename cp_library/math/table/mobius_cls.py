import cp_library.math.table.__header__

class Mobius(list[int]):
    def __init__(mob, N):
        super().__init__([1]*(N+1))
        for i in range(2, N+1):
            if mob[i] == 1: 
                i2 = i*i
                for j in range(i, N+1, i): 
                    if j % i2 == 0: 
                        mob[j] = 0
                    else: 
                        mob[j] *= -1