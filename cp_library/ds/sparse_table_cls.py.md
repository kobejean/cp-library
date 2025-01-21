---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/lca_table_recursive_cls.py
    title: cp_library/alg/tree/lca_table_recursive_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_5_c_lca_table_recursive.test.py
    title: test/aoj/grl/grl_5_c_lca_table_recursive.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    from typing import Any, Callable, List\n\nclass SparseTable:\n    def __init__(self,\
    \ op: Callable[[Any, Any], Any], arr: List[Any]):\n        self.N = N = len(arr)\n\
    \        self.log = N.bit_length()\n        self.op = op\n        \n        self.offsets\
    \ = offsets = [0]\n        for i in range(1, self.log):\n            offsets.append(offsets[-1]\
    \ + N - (1 << (i-1)) + 1)\n            \n        self.st = st = [0] * (offsets[-1]\
    \ + N - (1 << (self.log-1)) + 1)\n        st[:N] = arr \n        \n        for\
    \ i in range(self.log - 1):\n            d = 1 << i\n            start = offsets[i]\n\
    \            next_start = offsets[i + 1]\n            for j in range(N - (1 <<\
    \ (i+1)) + 1):\n                st[next_start + j] = op(st[k := start+j], st[k\
    \ + d])\n\n    def query(self, l: int, r: int) -> Any:\n        k = (r-l).bit_length()\
    \ - 1\n        start, st = self.offsets[k], self.st\n        return self.op(st[start\
    \ + l], st[start + r - (1 << k)])\n    \n    def __repr__(self) -> str:\n    \
    \    rows = []\n        for i in range(self.log):\n            start = self.offsets[i]\n\
    \            end = self.offsets[i+1] if i+1 < self.log else len(self.st)\n   \
    \         rows.append(f\"{i:<2d} {self.st[start:end]}\")\n        return '\\n'.join(rows)\n"
  code: "import cp_library.ds.__header__\nfrom typing import Any, Callable, List\n\
    \nclass SparseTable:\n    def __init__(self, op: Callable[[Any, Any], Any], arr:\
    \ List[Any]):\n        self.N = N = len(arr)\n        self.log = N.bit_length()\n\
    \        self.op = op\n        \n        self.offsets = offsets = [0]\n      \
    \  for i in range(1, self.log):\n            offsets.append(offsets[-1] + N -\
    \ (1 << (i-1)) + 1)\n            \n        self.st = st = [0] * (offsets[-1] +\
    \ N - (1 << (self.log-1)) + 1)\n        st[:N] = arr \n        \n        for i\
    \ in range(self.log - 1):\n            d = 1 << i\n            start = offsets[i]\n\
    \            next_start = offsets[i + 1]\n            for j in range(N - (1 <<\
    \ (i+1)) + 1):\n                st[next_start + j] = op(st[k := start+j], st[k\
    \ + d])\n\n    def query(self, l: int, r: int) -> Any:\n        k = (r-l).bit_length()\
    \ - 1\n        start, st = self.offsets[k], self.st\n        return self.op(st[start\
    \ + l], st[start + r - (1 << k)])\n    \n    def __repr__(self) -> str:\n    \
    \    rows = []\n        for i in range(self.log):\n            start = self.offsets[i]\n\
    \            end = self.offsets[i+1] if i+1 < self.log else len(self.st)\n   \
    \         rows.append(f\"{i:<2d} {self.st[start:end]}\")\n        return '\\n'.join(rows)"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/sparse_table_cls.py
  requiredBy:
  - cp_library/alg/tree/lca_table_recursive_cls.py
  timestamp: '2025-01-21 19:55:16+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/grl/grl_5_c_lca_table_recursive.test.py
documentation_of: cp_library/ds/sparse_table_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/sparse_table_cls.py
- /library/cp_library/ds/sparse_table_cls.py.html
title: cp_library/ds/sparse_table_cls.py
---
