def matmul(A, B, mod):
    N1, N2, N3 = len(A),len(B),len(B[0])
    R = [[0]*N3 for _ in range(N1)]
    for i in range(N1):
        for j in range(N3):
            for k in range(N2):
                R[i][j] += A[i][k]*B[k][j] % mod
                R[i][j] %= mod
    return R