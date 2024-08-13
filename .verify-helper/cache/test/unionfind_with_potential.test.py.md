---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/unionfind_with_potential
    links:
    - https://judge.yosupo.jp/problem/unionfind_with_potential
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind_with_potential\n\
    \nclass PotentializedDSU:\n\n    def __init__(self, op, inv, e, v) -> None:\n\
    \        n = v if isinstance(v, int) else len(v)\n        self.n = n\n       \
    \ self.par = [-1] * n\n        self.op = op\n        self.inv = inv\n        self.e\
    \ = e\n        self.pot = [e] * n if isinstance(v, int) else v\n\n    def leader(self,\
    \ x: int) -> int:\n        assert 0 <= x < self.n\n        path = []\n       \
    \ while self.par[x] >= 0:\n            path.append(x)\n            x = self.par[x]\n\
    \        for y in reversed(path):\n            self.pot[y] = self.op(self.pot[y],\
    \ self.pot[self.par[y]])\n            self.par[y] = x\n        return x\n    \n\
    \    def consistent(self, x: int, y: int, w) -> bool:\n        rx = self.leader(x)\n\
    \        ry = self.leader(y)\n        if rx == ry:\n            return self.op(self.pot[x],\
    \ self.inv(self.pot[y])) == w\n        return True\n\n    def merge(self, x: int,\
    \ y: int, w) -> int:\n        assert 0 <= x < self.n\n        assert 0 <= y <\
    \ self.n\n        rx = self.leader(x)\n        ry = self.leader(y)\n        if\
    \ rx == ry:\n            return rx\n        \n        if self.par[rx] < self.par[ry]:\n\
    \            x,y,w,rx,ry = y,x,self.inv(w),ry,rx\n            \n        self.par[ry]\
    \ += self.par[rx]\n        self.par[rx] = ry\n        self.pot[rx] = self.op(\n\
    \            self.op(self.inv(self.pot[x]), w), self.pot[y]\n        )\n     \
    \   return ry\n\n    def same(self, x: int, y: int) -> bool:\n        assert 0\
    \ <= x < self.n\n        assert 0 <= y < self.n\n        return self.leader(x)\
    \ == self.leader(y)\n    \n    def size(self, x: int) -> int:\n        assert\
    \ 0 <= x < self.n\n        return -self.par[self.leader(x)]\n    \n    def groups(self):\n\
    \        leader_buf = [self.leader(i) for i in range(self.n)]\n\n        result\
    \ = [[] for _ in range(self.n)]\n        for i in range(self.n):\n           \
    \ result[leader_buf[i]].append(i)\n\n        return list(filter(lambda r: r, result))\n\
    \n    def diff(self, x: int, y: int):\n        assert self.same(x, y)\n      \
    \  return self.op(self.pot[x], self.inv(self.pot[y]))\n\n\nmod = 998244353\n\n\
    def rint(shift=0, base=10):\n    return [int(x, base) + shift for x in input().split()]\n\
    \nN, Q = rint()\n\ndef op(x,y):\n    return (x+y)%mod\n\ndef inv(x):\n    return\
    \ (-x)%mod\n\npdsu = PotentializedDSU(op,inv,0,N)\n\nfor _ in range(Q):\n    t,\
    \ *q = rint()\n    if t:\n        u, v = q\n        ans = pdsu.diff(u, v) if pdsu.same(u,\
    \ v) else -1\n        print(ans)\n    else:\n        u, v, x = q\n        print(int(pdsu.consistent(u,v,x)))\n\
    \        pdsu.merge(u, v, x)\n\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind_with_potential\n\
    \nclass PotentializedDSU:\n\n    def __init__(self, op, inv, e, v) -> None:\n\
    \        n = v if isinstance(v, int) else len(v)\n        self.n = n\n       \
    \ self.par = [-1] * n\n        self.op = op\n        self.inv = inv\n        self.e\
    \ = e\n        self.pot = [e] * n if isinstance(v, int) else v\n\n    def leader(self,\
    \ x: int) -> int:\n        assert 0 <= x < self.n\n        path = []\n       \
    \ while self.par[x] >= 0:\n            path.append(x)\n            x = self.par[x]\n\
    \        for y in reversed(path):\n            self.pot[y] = self.op(self.pot[y],\
    \ self.pot[self.par[y]])\n            self.par[y] = x\n        return x\n    \n\
    \    def consistent(self, x: int, y: int, w) -> bool:\n        rx = self.leader(x)\n\
    \        ry = self.leader(y)\n        if rx == ry:\n            return self.op(self.pot[x],\
    \ self.inv(self.pot[y])) == w\n        return True\n\n    def merge(self, x: int,\
    \ y: int, w) -> int:\n        assert 0 <= x < self.n\n        assert 0 <= y <\
    \ self.n\n        rx = self.leader(x)\n        ry = self.leader(y)\n        if\
    \ rx == ry:\n            return rx\n        \n        if self.par[rx] < self.par[ry]:\n\
    \            x,y,w,rx,ry = y,x,self.inv(w),ry,rx\n            \n        self.par[ry]\
    \ += self.par[rx]\n        self.par[rx] = ry\n        self.pot[rx] = self.op(\n\
    \            self.op(self.inv(self.pot[x]), w), self.pot[y]\n        )\n     \
    \   return ry\n\n    def same(self, x: int, y: int) -> bool:\n        assert 0\
    \ <= x < self.n\n        assert 0 <= y < self.n\n        return self.leader(x)\
    \ == self.leader(y)\n    \n    def size(self, x: int) -> int:\n        assert\
    \ 0 <= x < self.n\n        return -self.par[self.leader(x)]\n    \n    def groups(self):\n\
    \        leader_buf = [self.leader(i) for i in range(self.n)]\n\n        result\
    \ = [[] for _ in range(self.n)]\n        for i in range(self.n):\n           \
    \ result[leader_buf[i]].append(i)\n\n        return list(filter(lambda r: r, result))\n\
    \n    def diff(self, x: int, y: int):\n        assert self.same(x, y)\n      \
    \  return self.op(self.pot[x], self.inv(self.pot[y]))\n\n\nmod = 998244353\n\n\
    def rint(shift=0, base=10):\n    return [int(x, base) + shift for x in input().split()]\n\
    \nN, Q = rint()\n\ndef op(x,y):\n    return (x+y)%mod\n\ndef inv(x):\n    return\
    \ (-x)%mod\n\npdsu = PotentializedDSU(op,inv,0,N)\n\nfor _ in range(Q):\n    t,\
    \ *q = rint()\n    if t:\n        u, v = q\n        ans = pdsu.diff(u, v) if pdsu.same(u,\
    \ v) else -1\n        print(ans)\n    else:\n        u, v, x = q\n        print(int(pdsu.consistent(u,v,x)))\n\
    \        pdsu.merge(u, v, x)\n\n"
  dependsOn: []
  isVerificationFile: true
  path: unionfind_with_potential.test.py
  requiredBy: []
  timestamp: '2024-08-14 06:01:40+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: unionfind_with_potential.test.py
layout: document
redirect_from:
- /verify/unionfind_with_potential.test.py
- /verify/unionfind_with_potential.test.py.html
title: unionfind_with_potential.test.py
---
