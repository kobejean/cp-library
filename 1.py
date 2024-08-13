# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind_with_potential

class PotentializedDSU:

    def __init__(self, op, inv, e, v) -> None:
        n = v if isinstance(v, int) else len(v)
        self.n = n
        self.par = [-1] * n
        self.op = op
        self.inv = inv
        self.e = e
        self.pot = [e] * n if isinstance(v, int) else v

    def leader(self, x: int) -> int:
        assert 0 <= x < self.n
        path = []
        while self.par[x] >= 0:
            path.append(x)
            x = self.par[x]
        for y in reversed(path):
            self.pot[y] = self.op(self.pot[y], self.pot[self.par[y]])
            self.par[y] = x
        return x
    
    def consistent(self, x: int, y: int, w) -> bool:
        rx = self.leader(x)
        ry = self.leader(y)
        if rx == ry:
            return self.op(self.pot[x], self.inv(self.pot[y])) == w
        return True

    def merge(self, x: int, y: int, w) -> int:
        assert 0 <= x < self.n
        assert 0 <= y < self.n
        rx = self.leader(x)
        ry = self.leader(y)
        if rx == ry:
            return rx
        
        if self.par[rx] < self.par[ry]:
            x,y,w,rx,ry = y,x,self.inv(w),ry,rx
            
        self.par[ry] += self.par[rx]
        self.par[rx] = ry
        self.pot[rx] = self.op(
            self.op(self.inv(self.pot[x]), w), self.pot[y]
        )
        return ry

    def same(self, x: int, y: int) -> bool:
        assert 0 <= x < self.n
        assert 0 <= y < self.n
        return self.leader(x) == self.leader(y)
    
    def size(self, x: int) -> int:
        assert 0 <= x < self.n
        return -self.par[self.leader(x)]
    
    def groups(self):
        leader_buf = [self.leader(i) for i in range(self.n)]

        result = [[] for _ in range(self.n)]
        for i in range(self.n):
            result[leader_buf[i]].append(i)

        return list(filter(lambda r: r, result))

    def diff(self, x: int, y: int):
        assert self.same(x, y)
        return self.op(self.pot[x], self.inv(self.pot[y]))

import math
# from bisect import bisect_left
from bisect import bisect_right

def matmul(A, B, mod):
    N1, N2, N3 = len(A),len(B),len(B[0])
    R = [[0]*N3 for _ in range(N1)]
    for i in range(N1):
        for j in range(N3):
            for k in range(N2):
                R[i][j] += A[i][k]*B[k][j] % mod
                R[i][j] %= mod
    return R

from bisect import bisect_left

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

mod = 998244353

def rint(shift=0, base=10):
    return [int(x, base) + shift for x in input().split()]

N, Q = rint()

def op(x,y):
    return (x+y)%mod

def inv(x):
    return (-x)%mod

pdsu = PotentializedDSU(op,inv,0,N)

for _ in range(Q):
    t, *q = rint()
    if t:
        u, v = q
        ans = pdsu.diff(u, v) if pdsu.same(u, v) else -1
        print(ans)
    else:
        u, v, x = q
        print(int(pdsu.consistent(u,v,x)))
        pdsu.merge(u, v, x)

