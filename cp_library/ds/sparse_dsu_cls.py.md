---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    from collections import defaultdict\n\nclass SparseDSU:\n    def __init__(self,\
    \ n) -> None:\n        self.par = defaultdict(lambda:-1)\n\n    def merge(self,\
    \ u, v) -> int:\n        x, y = self.leader(u), self.leader(v)\n        if x ==\
    \ y: return x\n\n        if -self.par[x] < -self.par[y]:\n            x, y = y,\
    \ x\n\n        self.par[x] += self.par[y]\n        self.par[y] = x\n\n       \
    \ return x\n\n    def same(self, u: int, v: int) -> bool:\n        return self.leader(u)\
    \ == self.leader(v)\n\n    def leader(self, i) -> int:\n        p = self.par[i]\n\
    \        while p >= 0:\n            if self.par[p] < 0:\n                return\
    \ p\n            self.par[i], i, p = self.par[p], self.par[p], self.par[self.par[p]]\n\
    \n        return i\n\n    def size(self, i) -> int:\n        return -self.par[self.leader(i)]\n\
    \n    def groups(self) -> list[list[int]]:\n        idx = list(self.par.keys())\n\
    \        leader_buf = [self.leader(i) for i in idx]\n\n        result = [[] for\
    \ _ in idx]\n        for i in idx:\n            result[leader_buf[i]].append(i)\n\
    \n        return list(filter(lambda r: r, result))\n"
  code: "import cp_library.ds.__header__\nfrom collections import defaultdict\n\n\
    class SparseDSU:\n    def __init__(self, n) -> None:\n        self.par = defaultdict(lambda:-1)\n\
    \n    def merge(self, u, v) -> int:\n        x, y = self.leader(u), self.leader(v)\n\
    \        if x == y: return x\n\n        if -self.par[x] < -self.par[y]:\n    \
    \        x, y = y, x\n\n        self.par[x] += self.par[y]\n        self.par[y]\
    \ = x\n\n        return x\n\n    def same(self, u: int, v: int) -> bool:\n   \
    \     return self.leader(u) == self.leader(v)\n\n    def leader(self, i) -> int:\n\
    \        p = self.par[i]\n        while p >= 0:\n            if self.par[p] <\
    \ 0:\n                return p\n            self.par[i], i, p = self.par[p], self.par[p],\
    \ self.par[self.par[p]]\n\n        return i\n\n    def size(self, i) -> int:\n\
    \        return -self.par[self.leader(i)]\n\n    def groups(self) -> list[list[int]]:\n\
    \        idx = list(self.par.keys())\n        leader_buf = [self.leader(i) for\
    \ i in idx]\n\n        result = [[] for _ in idx]\n        for i in idx:\n   \
    \         result[leader_buf[i]].append(i)\n\n        return list(filter(lambda\
    \ r: r, result))\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/sparse_dsu_cls.py
  requiredBy: []
  timestamp: '2025-03-27 22:10:43+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/sparse_dsu_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/sparse_dsu_cls.py
- /library/cp_library/ds/sparse_dsu_cls.py.html
title: cp_library/ds/sparse_dsu_cls.py
---
