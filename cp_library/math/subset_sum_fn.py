import cp_library.math.__header__

def subset_sum(A):
    dp = [0]*(1 << len(A))
    for i,a in enumerate(A):
        for mask in range(bit := 1 << i):
            dp[mask^bit] = dp[mask] + a
    return dp