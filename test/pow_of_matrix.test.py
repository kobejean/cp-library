from cp_library.math.mod.matpow import matpow

def rint(shift=0, base=10):
    return [int(x, base) + shift for x in input().split()]

mod = 998244353

N, K = rint()
A = [rint() for _ in range(N)]
B = matpow(A, K, mod)
for bi in B:
    print(*bi) 
    