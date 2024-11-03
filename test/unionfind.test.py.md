---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/dsu_cls.py
    title: cp_library/ds/dsu_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_int_fn.py
    title: cp_library/io/read_int_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/unionfind
    links:
    - https://judge.yosupo.jp/problem/unionfind
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind\n\
    \n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\
    \n             https://kobejean.github.io/cp-library               \n'''\n\ndef\
    \ read(shift=0, base=10):\n    return [int(s, base) + shift for s in input().split()]\n\
    \n\nclass DSU:\n    def __init__(self, n):\n        self.n = n\n        self.par\
    \ = [-1] * n\n\n    def merge(self, u, v):\n        assert 0 <= u < self.n\n \
    \       assert 0 <= v < self.n\n\n        x, y = self.leader(u), self.leader(v)\n\
    \        if x == y: return x\n\n        if -self.par[x] < -self.par[y]:\n    \
    \        x, y = y, x\n\n        self.par[x] += self.par[y]\n        self.par[y]\
    \ = x\n\n        return x\n\n    def same(self, u: int, v: int):\n        assert\
    \ 0 <= u < self.n\n        assert 0 <= v < self.n\n        return self.leader(u)\
    \ == self.leader(v)\n\n    def leader(self, i) -> int:\n        assert 0 <= i\
    \ < self.n\n\n        p = self.par[i]\n        while p >= 0:\n            if self.par[p]\
    \ < 0:\n                return p\n            self.par[i], i, p = self.par[p],\
    \ self.par[p], self.par[self.par[p]]\n\n        return i\n\n    def size(self,\
    \ i) -> int:\n        assert 0 <= i < self.n\n        \n        return -self.par[self.leader(i)]\n\
    \n    def groups(self) -> list[list[int]]:\n        leader_buf = [self.leader(i)\
    \ for i in range(self.n)]\n\n        result = [[] for _ in range(self.n)]\n  \
    \      for i in range(self.n):\n            result[leader_buf[i]].append(i)\n\n\
    \        return list(filter(lambda r: r, result))\n\nN, Q = read()\n\ndsu = DSU(N)\n\
    \nfor _ in range(Q):\n    t, u, v = read()\n    if t:\n        print(int(dsu.same(u,\
    \ v)))\n    else:\n        dsu.merge(u, v)\n\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind\n\
    \nfrom cp_library.io.read_int_fn import read\nfrom cp_library.ds.dsu_cls import\
    \ DSU\n\nN, Q = read()\n\ndsu = DSU(N)\n\nfor _ in range(Q):\n    t, u, v = read()\n\
    \    if t:\n        print(int(dsu.same(u, v)))\n    else:\n        dsu.merge(u,\
    \ v)\n\n"
  dependsOn:
  - cp_library/io/read_int_fn.py
  - cp_library/ds/dsu_cls.py
  isVerificationFile: true
  path: test/unionfind.test.py
  requiredBy: []
  timestamp: '2024-11-03 23:46:02+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/unionfind.test.py
layout: document
redirect_from:
- /verify/test/unionfind.test.py
- /verify/test/unionfind.test.py.html
title: test/unionfind.test.py
---
