---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/func_graph_cls.py
    title: cp_library/alg/graph/func_graph_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/mut_perm_graph_cls.py
    title: cp_library/alg/graph/mut_perm_graph_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/partial_func_graph_cls.py
    title: cp_library/alg/graph/partial_func_graph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/perm_graph_cls.py
    title: cp_library/alg/graph/perm_graph_cls.py
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
  bundledCode: "from itertools import pairwise\n'''\n\u257A\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\nfrom typing import Generic\nfrom typing import TypeVar\n\
    _T = TypeVar('T')\n\nclass CRFList(Generic[_T]):\n    def __init__(crf, A: list[_T],\
    \ S: list[int]):\n        crf.N, crf.A, crf.S = len(S), A, S\n        S.append(len(A))\n\
    \n    def __len__(crf) -> int: return crf.N\n\n    def __getitem__(crf, i: int)\
    \ -> list[_T]:\n        return crf.A[crf.S[i]:crf.S[i+1]]\n    \n    def get(crf,\
    \ i: int, j: int) -> _T:\n        return crf.A[crf.S[i]+j]\n    \n    def len(crf,\
    \ i: int) -> int:\n        return crf.S[i+1] - crf.S[i]\n"
  code: "from itertools import pairwise\nimport cp_library.alg.iter.__header__\nfrom\
    \ typing import Generic\nfrom cp_library.misc.typing import _T\n\nclass CRFList(Generic[_T]):\n\
    \    def __init__(crf, A: list[_T], S: list[int]):\n        crf.N, crf.A, crf.S\
    \ = len(S), A, S\n        S.append(len(A))\n\n    def __len__(crf) -> int: return\
    \ crf.N\n\n    def __getitem__(crf, i: int) -> list[_T]:\n        return crf.A[crf.S[i]:crf.S[i+1]]\n\
    \    \n    def get(crf, i: int, j: int) -> _T:\n        return crf.A[crf.S[i]+j]\n\
    \    \n    def len(crf, i: int) -> int:\n        return crf.S[i+1] - crf.S[i]"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/crf_list_cls.py
  requiredBy:
  - cp_library/alg/graph/func_graph_cls.py
  - cp_library/alg/graph/partial_func_graph_cls.py
  - cp_library/alg/graph/mut_perm_graph_cls.py
  - cp_library/alg/graph/perm_graph_cls.py
  timestamp: '2025-03-15 12:29:05+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/abc/abc175_d_permutation.test.py
  - test/atcoder/agc/agc038_b_sliding_min_max.test.py
documentation_of: cp_library/alg/iter/crf_list_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/crf_list_cls.py
- /library/cp_library/alg/iter/crf_list_cls.py.html
title: cp_library/alg/iter/crf_list_cls.py
---
