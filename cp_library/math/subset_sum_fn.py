import cp_library.math.__header__

def subset_sum(A):
    dp = [0]*(1<<len(A))
    for i, a in enumerate(A):
        for m in range(b := 1<<i): dp[m^b] = dp[m] + a
    return dp
