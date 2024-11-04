---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/abc185_e_dp2d.test.py
    title: test/abc185_e_dp2d.test.py
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
    from typing import TypeVar, Generic\nfrom dataclasses import dataclass\nfrom math\
    \ import inf\n\nT = TypeVar('T')\n\n@dataclass\nclass Transition2D(Generic[T]):\n\
    \    di: int\n    dj: int\n    \n    def __call__(self, i: int, j: int, src_val:\
    \ T, dest_val: T) -> T:\n        \"\"\"Override this to implement transition logic\"\
    \"\"\n        return src_val  # Default no-op\n\nclass DynamicProgramming2D(Generic[T]):\n\
    \    def __init__(self, rows: int, cols: int, default: T = inf):\n        self.rows\
    \ = rows\n        self.cols = cols\n        self.table = [[default] * cols for\
    \ _ in range(rows)]\n    \n    def __getitem__(self, pos: tuple[int, int]) ->\
    \ T:\n        i, j = pos\n        return self.table[i][j]\n    \n    def __setitem__(self,\
    \ pos: tuple[int, int], value: T) -> None:\n        i, j = pos\n        self.table[i][j]\
    \ = value\n    \n    def solve(self, transitions: list[Transition2D[T]]) -> None:\n\
    \        for i in range(self.rows):\n            for j in range(self.cols):\n\
    \                curr_val = self.table[i][j]\n                for trans in transitions:\n\
    \                    ni, nj = i + trans.di, j + trans.dj\n                   \
    \ if 0 <= ni < self.rows and 0 <= nj < self.cols:\n                        self.table[ni][nj]\
    \ = trans(i, j, curr_val, self.table[ni][nj])\n"
  code: "import cp_library.alg.dp.__header__\nfrom typing import TypeVar, Generic\n\
    from dataclasses import dataclass\nfrom math import inf\n\nT = TypeVar('T')\n\n\
    @dataclass\nclass Transition2D(Generic[T]):\n    di: int\n    dj: int\n    \n\
    \    def __call__(self, i: int, j: int, src_val: T, dest_val: T) -> T:\n     \
    \   \"\"\"Override this to implement transition logic\"\"\"\n        return src_val\
    \  # Default no-op\n\nclass DynamicProgramming2D(Generic[T]):\n    def __init__(self,\
    \ rows: int, cols: int, default: T = inf):\n        self.rows = rows\n       \
    \ self.cols = cols\n        self.table = [[default] * cols for _ in range(rows)]\n\
    \    \n    def __getitem__(self, pos: tuple[int, int]) -> T:\n        i, j = pos\n\
    \        return self.table[i][j]\n    \n    def __setitem__(self, pos: tuple[int,\
    \ int], value: T) -> None:\n        i, j = pos\n        self.table[i][j] = value\n\
    \    \n    def solve(self, transitions: list[Transition2D[T]]) -> None:\n    \
    \    for i in range(self.rows):\n            for j in range(self.cols):\n    \
    \            curr_val = self.table[i][j]\n                for trans in transitions:\n\
    \                    ni, nj = i + trans.di, j + trans.dj\n                   \
    \ if 0 <= ni < self.rows and 0 <= nj < self.cols:\n                        self.table[ni][nj]\
    \ = trans(i, j, curr_val, self.table[ni][nj])\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/dp/dp2d_cls.py
  requiredBy: []
  timestamp: '2024-11-05 04:28:32+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/abc185_e_dp2d.test.py
documentation_of: cp_library/alg/dp/dp2d_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/dp/dp2d_cls.py
- /library/cp_library/alg/dp/dp2d_cls.py.html
title: cp_library/alg/dp/dp2d_cls.py
---
