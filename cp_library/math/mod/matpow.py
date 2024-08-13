from cp_library.math.mod.matmul import matmul

def matpow(A, K, mod):
    N = len(A)
    R = [[int(i == j) for j in range(N)] for i in range(N)]
    An = [[aij for aij in ai] for ai in A]
    while K > 0:
        if K & 1:
            R = matmul(R,An,mod)
        An = matmul(An,An,mod)
        K >>= 1
    return R