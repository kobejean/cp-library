---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/fast/digraph_cls.py
    title: cp_library/alg/graph/fast/digraph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/fast/snippets/biconnected_components_vertices_fn.py
    title: cp_library/alg/graph/fast/snippets/biconnected_components_vertices_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/fast/snippets/strongly_connected_components_fn.py
    title: cp_library/alg/graph/fast/snippets/strongly_connected_components_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/fast/snippets/two_edge_connected_components_fn.py
    title: cp_library/alg/graph/fast/snippets/two_edge_connected_components_fn.py
  - icon: ':warning:'
    path: cp_library/alg/graph/strongly_connected_components_fn.py
    title: cp_library/alg/graph/strongly_connected_components_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc218_f_fast_shortest_path.test.py
    title: test/atcoder/abc/abc218_f_fast_shortest_path.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/graph/biconnected_components.test.py
    title: test/library-checker/graph/biconnected_components.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/graph/cycle_detection.test.py
    title: test/library-checker/graph/cycle_detection.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/graph/scc.test.py
    title: test/library-checker/graph/scc.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/graph/scc_strongly_connected_components.test.py
    title: test/library-checker/graph/scc_strongly_connected_components.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/graph/two_edge_connected_components.test.py
    title: test/library-checker/graph/two_edge_connected_components.test.py
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
    from typing import Iterator, SupportsIndex\nfrom typing import TypeVar\n_T = TypeVar('T')\n\
    \nclass SliceIteratorReverse(Iterator[_T]):\n    def __init__(self, A: list[_T],\
    \ L: list[SupportsIndex]):\n        self.A, self.L, self.r = A, L, len(A)\n  \
    \  def __len__(self): return len(self.L)\n    def __next__(self):\n        L =\
    \ self.L\n        if not L: raise StopIteration\n        self.r, r = (l := L.pop()),\
    \ self.r\n        return self.A[l:r]\n"
  code: "import cp_library.alg.iter.__header__\nfrom typing import Iterator, SupportsIndex\n\
    from cp_library.misc.typing import _T\n\nclass SliceIteratorReverse(Iterator[_T]):\n\
    \    def __init__(self, A: list[_T], L: list[SupportsIndex]):\n        self.A,\
    \ self.L, self.r = A, L, len(A)\n    def __len__(self): return len(self.L)\n \
    \   def __next__(self):\n        L = self.L\n        if not L: raise StopIteration\n\
    \        self.r, r = (l := L.pop()), self.r\n        return self.A[l:r]"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/slice_iterator_reverse_cls.py
  requiredBy:
  - cp_library/alg/graph/fast/snippets/biconnected_components_vertices_fn.py
  - cp_library/alg/graph/fast/snippets/two_edge_connected_components_fn.py
  - cp_library/alg/graph/fast/snippets/strongly_connected_components_fn.py
  - cp_library/alg/graph/fast/digraph_cls.py
  - cp_library/alg/graph/strongly_connected_components_fn.py
  timestamp: '2025-03-30 20:17:47+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/graph/cycle_detection.test.py
  - test/library-checker/graph/scc.test.py
  - test/library-checker/graph/scc_strongly_connected_components.test.py
  - test/library-checker/graph/biconnected_components.test.py
  - test/library-checker/graph/two_edge_connected_components.test.py
  - test/atcoder/abc/abc218_f_fast_shortest_path.test.py
documentation_of: cp_library/alg/iter/slice_iterator_reverse_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/slice_iterator_reverse_cls.py
- /library/cp_library/alg/iter/slice_iterator_reverse_cls.py.html
title: cp_library/alg/iter/slice_iterator_reverse_cls.py
---
