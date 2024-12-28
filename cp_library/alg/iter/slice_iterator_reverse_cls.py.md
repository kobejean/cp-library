---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/fast/digraph_cls.py
    title: cp_library/alg/graph/fast/digraph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/functional_graph_cls.py
    title: cp_library/alg/graph/functional_graph_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/partial_functional_graph_cls.py
    title: cp_library/alg/graph/partial_functional_graph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/permutation_cls.py
    title: cp_library/alg/graph/permutation_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc175_d_permutation.test.py
    title: test/atcoder/abc/abc175_d_permutation.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc218_f_fast_shortest_path.test.py
    title: test/atcoder/abc/abc218_f_fast_shortest_path.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/graph/cycle_detection.test.py
    title: test/library-checker/graph/cycle_detection.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/graph/scc.test.py
    title: test/library-checker/graph/scc.test.py
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
    from typing import Iterator, SupportsIndex, TypeVar\n\nT = TypeVar('T')\nclass\
    \ SliceIteratorReverse(Iterator[T]):\n    def __init__(self, A: list[T], L: list[SupportsIndex]):\n\
    \        self.A, self.L, self.r = A, L, len(A)\n    def __len__(self): return\
    \ len(self.L)\n    def __next__(self):\n        L = self.L\n        if not L:\
    \ raise StopIteration\n        self.r, r = (l := L.pop()), self.r\n        return\
    \ self.A[l:r]\n"
  code: "import cp_library.alg.iter.__header__\nfrom typing import Iterator, SupportsIndex,\
    \ TypeVar\n\nT = TypeVar('T')\nclass SliceIteratorReverse(Iterator[T]):\n    def\
    \ __init__(self, A: list[T], L: list[SupportsIndex]):\n        self.A, self.L,\
    \ self.r = A, L, len(A)\n    def __len__(self): return len(self.L)\n    def __next__(self):\n\
    \        L = self.L\n        if not L: raise StopIteration\n        self.r, r\
    \ = (l := L.pop()), self.r\n        return self.A[l:r]"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/slice_iterator_reverse_cls.py
  requiredBy:
  - cp_library/alg/graph/fast/digraph_cls.py
  - cp_library/alg/graph/functional_graph_cls.py
  - cp_library/alg/graph/permutation_cls.py
  - cp_library/alg/graph/partial_functional_graph_cls.py
  timestamp: '2024-12-28 12:13:01+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/abc/abc218_f_fast_shortest_path.test.py
  - test/atcoder/abc/abc175_d_permutation.test.py
  - test/library-checker/graph/scc.test.py
  - test/library-checker/graph/cycle_detection.test.py
documentation_of: cp_library/alg/iter/slice_iterator_reverse_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/slice_iterator_reverse_cls.py
- /library/cp_library/alg/iter/slice_iterator_reverse_cls.py.html
title: cp_library/alg/iter/slice_iterator_reverse_cls.py
---
