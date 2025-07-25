import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.conv.__header__

def ior_zeta_pair_ranked(A, B, N, M, Z):
    for i in range(0, Z, M):
        l, r = i+(1<<(i>>N))-1, i+M
        for j in range(N):
            m = l|(b := 1<<j)
            while m < r: A[m] += A[m^b]; B[m] += B[m^b]; m = m+1|b
    return A, B