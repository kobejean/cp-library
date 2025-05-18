import cp_library.__header__
from cp_library.alg.divcon.bisect_left_fn import bisect_left
import cp_library.alg.__header__
import cp_library.alg.dp.__header__
from cp_library.alg.dp.max2_fn import max2
from cp_library.alg.dp.chmin_fn import chmin

def lis(A: list):
    '''Returns indices of a longest increasing sequence'''
    N = len(A)
    mn, mx = min(A), max(A)
    dp, idx, prev = [mx+1]*(N+1), [-1]*(N+1), [-1]*N
    dp[0], r = mn-1, 0
    for i,a in enumerate(A):
        if chmin(dp, p := bisect_left(dp,a,0,r+1), a):
            idx[p], prev[i], r = i, idx[p-1], max2(r,p)
    ans, i = [0]*r, idx[r]
    for j in range(r-1,-1,-1): ans[j], i = i, prev[i]
    return ans

    

