# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_matrix


def mat_mul(A,B,mod):
    assert len(A[0]) == len(B)
    R = [[0]*len(B[0]) for _ in range(len(A))] 
    for i,Ri in enumerate(R):
        for k,Aik in enumerate(A[i]):
            for j,Bkj in enumerate(B[k]):
                Ri[j] = (Ri[j] + Aik*Bkj) % mod  
    return R 

def mat_id(N):
    return [[int(i==j) for j in range(N)] for i in range(N)]

def mat_pow(A,K,mod):
    N = len(A)
    ret = A if K & 1 else mat_id(N)
    for i in range(1,K.bit_length()):
        A = mat_mul(A,A,mod) 
        if K >> i & 1:
            ret = mat_mul(ret,A,mod) 
    return ret 

mod = 998244353

def rint(shift=0, base=10):
    return [int(x, base) + shift for x in input().split()]

N, K = rint()
A = [rint() for _ in range(N)]
B = mat_pow(A, K, mod)

for row in B:
    print(*row)
