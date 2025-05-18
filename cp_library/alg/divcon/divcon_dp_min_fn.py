import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.divcon.__header__
from cp_library.alg.dp.min2_fn import min2
    
def divcon_dp_min(N, M, cost_fn, default = 1<<62):
    dp, ndp = [default]*N, [default]*N
    for i in range(N): dp[i] = cost_fn(0,i)
    def rec(l, r, optl, optr):
        first, last = optl, optr
        i, j = optl, min2(m := (l+r)>>1, optr+1)
        ndp[m] = default
        while i < j:
            if (cost:=dp[i]+cost_fn(i,m)) < ndp[m]:
                ndp[m] = cost
                first = last = i
            elif ndp[m] == cost:
                last = i
            i += 1
        if r <= l: return
        rec(l, m-1, optl, first)
        rec(m+1, r, last, optr)
    for _ in range(1,M):
        rec(0, N-1, 0, N-1)
        dp, ndp = ndp, dp
    return dp