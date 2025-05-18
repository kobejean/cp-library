import cp_library.math.table.__header__

class Lucas(list[int]):
    def __init__(lucas,N,mod=None):
        super().__init__([0]*(N+1))
        dp0 = 2; dp1 = 1
        if mod is None:
            lucas[0] = dp0
            for i in range(N): dp0, dp1 = dp1, dp0+dp1; lucas[i+1] = dp0
        else:
            lucas[0] = dp0 % mod
            for i in range(N): dp0, dp1 = dp1, (dp0+dp1)%mod; lucas[i+1] = dp0