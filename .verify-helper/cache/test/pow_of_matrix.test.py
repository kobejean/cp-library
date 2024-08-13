# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_matrix

def matmul(A,B,mod):
    assert len(A[0]) == len(B)
    N = len(A)
    M = len(B)
    ret = [[0]*M for _ in range(N)] 
    for i,reti in enumerate(ret):
        for k,a_ik in enumerate(A[i]):
            for j,b_kj in enumerate(B[k]):
                reti[j] = (reti[j] + a_ik*b_kj) % mod  

    return ret 

def matpow(A,k,mod):
    N = len(A)
    ret = [[int(i==j) for j in range(N)] for i in range(N)]
    tmp = A
    for i in range(k.bit_length()):
        if (k >> i) & 1:
            ret = matmul(ret,tmp,mod) 
        tmp = matmul(tmp,tmp,mod) 
    return ret 

mod = 998244353

def rint(shift=0, base=10):
    return [int(x, base) + shift for x in input().split()]

N, K = rint()
A = [rint() for _ in range(N)]
B = matpow(A, K,mod)

for row in B:
    print(*row)
