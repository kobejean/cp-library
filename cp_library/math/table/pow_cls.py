from itertools import accumulate
import cp_library.math.table.__header__

class Pow(list):
    def __init__(self,K,N,mod=None):
        super().__init__([1]*(N+1))
        if mod is None:
            for i in range(N):
                self[i+1] = self[i]*K
        else:
            for i in range(N):
                self[i+1] = self[i]*K % mod