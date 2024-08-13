from cp_library.math.mod.matmul import matmul

def matpow(A,k,mod):
    N = len(A)
    ret = [[int(i==j) for j in range(N)] for i in range(N)]
    tmp = A
    for i in range(k.bit_length()):
        if (k >> i) & 1:
            ret = matmul(ret,tmp,mod) 
        tmp = matmul(tmp,tmp,mod) 
    return ret 