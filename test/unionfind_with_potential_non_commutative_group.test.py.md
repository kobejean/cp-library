---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/potentialized_dsu.py
    title: cp_library/ds/potentialized_dsu.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/unionfind_with_potential_non_commutative_group
    links:
    - https://judge.yosupo.jp/problem/unionfind_with_potential_non_commutative_group
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind_with_potential_non_commutative_group\n\
    \nmod = 998244353\n\nclass PotentializedDSU:\n\n    def __init__(self, op, inv,\
    \ e, v) -> None:\n        n = v if isinstance(v, int) else len(v)\n        self.n\
    \ = n\n        self.par = [-1] * n\n        self.op = op\n        self.inv = inv\n\
    \        self.e = e\n        self.pot = [e] * n if isinstance(v, int) else v\n\
    \n    def leader(self, x: int) -> int:\n        assert 0 <= x < self.n\n     \
    \   path = []\n        while self.par[x] >= 0:\n            path.append(x)\n \
    \           x = self.par[x]\n        for y in reversed(path):\n            self.pot[y]\
    \ = self.op(self.pot[y], self.pot[self.par[y]])\n            self.par[y] = x\n\
    \        return x\n    \n    def consistent(self, x: int, y: int, w) -> bool:\n\
    \        rx = self.leader(x)\n        ry = self.leader(y)\n        if rx == ry:\n\
    \            return self.op(self.pot[x], self.inv(self.pot[y])) == w\n       \
    \ return True\n\n    def merge(self, x: int, y: int, w) -> int:\n        assert\
    \ 0 <= x < self.n\n        assert 0 <= y < self.n\n        rx = self.leader(x)\n\
    \        ry = self.leader(y)\n        if rx == ry:\n            return rx\n  \
    \      \n        if self.par[rx] < self.par[ry]:\n            x,y,w,rx,ry = y,x,self.inv(w),ry,rx\n\
    \            \n        self.par[ry] += self.par[rx]\n        self.par[rx] = ry\n\
    \        self.pot[rx] = self.op(\n            self.op(self.inv(self.pot[x]), w),\
    \ self.pot[y]\n        )\n        return ry\n\n    def same(self, x: int, y: int)\
    \ -> bool:\n        assert 0 <= x < self.n\n        assert 0 <= y < self.n\n \
    \       return self.leader(x) == self.leader(y)\n    \n    def size(self, x: int)\
    \ -> int:\n        assert 0 <= x < self.n\n        return -self.par[self.leader(x)]\n\
    \    \n    def groups(self):\n        leader_buf = [self.leader(i) for i in range(self.n)]\n\
    \n        result = [[] for _ in range(self.n)]\n        for i in range(self.n):\n\
    \            result[leader_buf[i]].append(i)\n\n        return list(filter(lambda\
    \ r: r, result))\n\n    def diff(self, x: int, y: int):\n        assert self.same(x,\
    \ y)\n        return self.op(self.pot[x], self.inv(self.pot[y]))\n\n\ndef rint(shift=0,\
    \ base=10):\n    return [int(x, base) + shift for x in input().split()]\n\nN,\
    \ Q = rint()\n\ndef matmul2(x, y):\n    return [\n        (y[0] * x[0] + y[1]\
    \ * x[2]) % mod,\n        (y[0] * x[1] + y[1] * x[3]) % mod,\n        (y[2] *\
    \ x[0] + y[3] * x[2]) % mod,\n        (y[2] * x[1] + y[3] * x[3]) % mod,\n   \
    \ ]\n\ndef matinv2(x) -> list[int]:\n    return [x[3], -x[1] % mod, -x[2] % mod,\
    \ x[0]]\n\ne = [1, 0, 0, 1]\npdsu = PotentializedDSU(matmul2,matinv2,e,N)\n\n\
    for _ in range(Q):\n    t, *q = rint()\n    if t:\n        u, v = q\n        ans\
    \ = pdsu.diff(u, v) if pdsu.same(u, v) else (-1,)\n        print(*ans)\n    else:\n\
    \        u, v, *w = q\n        print(int(pdsu.consistent(u,v, w)))\n        pdsu.merge(u,\
    \ v, w)\n            \n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind_with_potential_non_commutative_group\n\
    \nmod = 998244353\n\nfrom cp_library.ds.potentialized_dsu import PotentializedDSU\n\
    \ndef rint(shift=0, base=10):\n    return [int(x, base) + shift for x in input().split()]\n\
    \nN, Q = rint()\n\ndef matmul2(x, y):\n    return [\n        (y[0] * x[0] + y[1]\
    \ * x[2]) % mod,\n        (y[0] * x[1] + y[1] * x[3]) % mod,\n        (y[2] *\
    \ x[0] + y[3] * x[2]) % mod,\n        (y[2] * x[1] + y[3] * x[3]) % mod,\n   \
    \ ]\n\ndef matinv2(x) -> list[int]:\n    return [x[3], -x[1] % mod, -x[2] % mod,\
    \ x[0]]\n\ne = [1, 0, 0, 1]\npdsu = PotentializedDSU(matmul2,matinv2,e,N)\n\n\
    for _ in range(Q):\n    t, *q = rint()\n    if t:\n        u, v = q\n        ans\
    \ = pdsu.diff(u, v) if pdsu.same(u, v) else (-1,)\n        print(*ans)\n    else:\n\
    \        u, v, *w = q\n        print(int(pdsu.consistent(u,v, w)))\n        pdsu.merge(u,\
    \ v, w)\n            "
  dependsOn:
  - cp_library/ds/potentialized_dsu.py
  isVerificationFile: true
  path: test/unionfind_with_potential_non_commutative_group.test.py
  requiredBy: []
  timestamp: '2024-08-27 19:43:09+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/unionfind_with_potential_non_commutative_group.test.py
layout: document
redirect_from:
- /verify/test/unionfind_with_potential_non_commutative_group.test.py
- /verify/test/unionfind_with_potential_non_commutative_group.test.py.html
title: test/unionfind_with_potential_non_commutative_group.test.py
---
