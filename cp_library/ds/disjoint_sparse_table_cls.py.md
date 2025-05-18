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
    \nclass DisjointSparseTable:\n    def __init__(self, op, arr: list):\n       \
    \ self.n = len(arr)\n        self.log = (self.n-1).bit_length()\n        self.op\
    \ = op\n        self.st = [arr]\n\n        for h in range(1, self.log):\n    \
    \        row = arr.copy()\n            half = 1 << h\n            for m in range(half,\
    \ self.n, 2*half):\n                l,r = m-half,min(m+half,self.n)\n        \
    \        for j in range(m-1,l,-1): row[j-1] = self.op(row[j-1], row[j])\n    \
    \            for j in range(m,r-1): row[j+1] = self.op(row[j], row[j+1])\n   \
    \         self.st.append(row)\n\n    def query(self, l: int, r: int):\n      \
    \  r -= 1\n        if l == r: return self.st[0][l]\n        h = (l ^ r).bit_length()\
    \ - 1\n        return self.op(self.st[h][l], self.st[h][r])\n\n    def __repr__(self):\n\
    \        return '\\n'.join(f'{i:<2d} {row}' for i,row in enumerate(self.st))\n"
  code: "import cp_library.ds.__header__\n\nclass DisjointSparseTable:\n    def __init__(self,\
    \ op, arr: list):\n        self.n = len(arr)\n        self.log = (self.n-1).bit_length()\n\
    \        self.op = op\n        self.st = [arr]\n\n        for h in range(1, self.log):\n\
    \            row = arr.copy()\n            half = 1 << h\n            for m in\
    \ range(half, self.n, 2*half):\n                l,r = m-half,min(m+half,self.n)\n\
    \                for j in range(m-1,l,-1): row[j-1] = self.op(row[j-1], row[j])\n\
    \                for j in range(m,r-1): row[j+1] = self.op(row[j], row[j+1])\n\
    \            self.st.append(row)\n\n    def query(self, l: int, r: int):\n   \
    \     r -= 1\n        if l == r: return self.st[0][l]\n        h = (l ^ r).bit_length()\
    \ - 1\n        return self.op(self.st[h][l], self.st[h][r])\n\n    def __repr__(self):\n\
    \        return '\\n'.join(f'{i:<2d} {row}' for i,row in enumerate(self.st))\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/disjoint_sparse_table_cls.py
  requiredBy: []
  timestamp: '2025-05-19 05:52:10+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/disjoint_sparse_table_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/disjoint_sparse_table_cls.py
- /library/cp_library/ds/disjoint_sparse_table_cls.py.html
title: cp_library/ds/disjoint_sparse_table_cls.py
---
