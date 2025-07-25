import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.conv.__header__

def ior_mobius_ranked(A: list[int], N: int, M: int, Z: int):
    for i in range(0, Z, M):
        l, r = i, i+M-(1<<(N-(i>>N)))+1
        for j in range(N):
            m = l|(b := 1<<j)
            while m < r: A[m] -= A[m^b]; m = m+1|b
    return A