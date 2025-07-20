---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/func/func_graph_cls.py
    title: cp_library/alg/graph/func/func_graph_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/func/mut_perm_graph_cls.py
    title: cp_library/alg/graph/func/mut_perm_graph_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/func/partial_func_graph_cls.py
    title: cp_library/alg/graph/func/partial_func_graph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/func/perm_graph_cls.py
    title: cp_library/alg/graph/func/perm_graph_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc175_d_permutation.test.py
    title: test/atcoder/abc/abc175_d_permutation.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/agc/agc038_b_sliding_min_max.test.py
    title: test/atcoder/agc/agc038_b_sliding_min_max.test.py
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
    from typing import Generic\nfrom typing import TypeVar\n_S = TypeVar('S'); _T\
    \ = TypeVar('T'); _U = TypeVar('U'); _T1 = TypeVar('T1'); _T2 = TypeVar('T2');\
    \ _T3 = TypeVar('T3'); _T4 = TypeVar('T4'); _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\
    \n\n\nclass CRFList(Generic[_T]):\n    def __init__(crf, A: list[_T], S: list[int]):\n\
    \        crf.N, crf.A, crf.S = len(S), A, S\n        S.append(len(A))\n\n    def\
    \ __len__(crf) -> int: return crf.N\n\n    def __getitem__(crf, i: int) -> list[_T]:\n\
    \        return crf.A[crf.S[i]:crf.S[i+1]]\n    \n    def get(crf, i: int, j:\
    \ int) -> _T:\n        return crf.A[crf.S[i]+j]\n    \n    def len(crf, i: int)\
    \ -> int:\n        return crf.S[i+1] - crf.S[i]\n"
  code: "import cp_library.__header__\nfrom typing import Generic\nfrom cp_library.misc.typing\
    \ import _T\nimport cp_library.alg.__header__\nimport cp_library.alg.iter.__header__\n\
    \nclass CRFList(Generic[_T]):\n    def __init__(crf, A: list[_T], S: list[int]):\n\
    \        crf.N, crf.A, crf.S = len(S), A, S\n        S.append(len(A))\n\n    def\
    \ __len__(crf) -> int: return crf.N\n\n    def __getitem__(crf, i: int) -> list[_T]:\n\
    \        return crf.A[crf.S[i]:crf.S[i+1]]\n    \n    def get(crf, i: int, j:\
    \ int) -> _T:\n        return crf.A[crf.S[i]+j]\n    \n    def len(crf, i: int)\
    \ -> int:\n        return crf.S[i+1] - crf.S[i]"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/crf_list_cls.py
  requiredBy:
  - cp_library/alg/graph/func/perm_graph_cls.py
  - cp_library/alg/graph/func/func_graph_cls.py
  - cp_library/alg/graph/func/mut_perm_graph_cls.py
  - cp_library/alg/graph/func/partial_func_graph_cls.py
  timestamp: '2025-07-21 03:35:11+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/agc/agc038_b_sliding_min_max.test.py
  - test/atcoder/abc/abc175_d_permutation.test.py
documentation_of: cp_library/alg/iter/crf_list_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/crf_list_cls.py
- /library/cp_library/alg/iter/crf_list_cls.py.html
title: cp_library/alg/iter/crf_list_cls.py
---
