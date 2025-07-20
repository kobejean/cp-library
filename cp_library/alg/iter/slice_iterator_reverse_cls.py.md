---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/alg/graph/csr/dag_cls.py
    title: cp_library/alg/graph/csr/dag_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/csr/digraph_cls.py
    title: cp_library/alg/graph/csr/digraph_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/csr/snippets/biconnected_components_edge_ids_fn.py
    title: cp_library/alg/graph/csr/snippets/biconnected_components_edge_ids_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/csr/snippets/biconnected_components_vertices_fn.py
    title: cp_library/alg/graph/csr/snippets/biconnected_components_vertices_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/csr/snippets/scc_labels_fn.py
    title: cp_library/alg/graph/csr/snippets/scc_labels_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/csr/snippets/strongly_connected_components_fn.py
    title: cp_library/alg/graph/csr/snippets/strongly_connected_components_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/csr/snippets/two_edge_connected_components_fn.py
    title: cp_library/alg/graph/csr/snippets/two_edge_connected_components_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_2_c_scc.test.py
    title: test/aoj/grl/grl_2_c_scc.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc218_f_fast_shortest_path.test.py
    title: test/atcoder/abc/abc218_f_fast_shortest_path.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc245_f_digraph.test.py
    title: test/atcoder/abc/abc245_f_digraph.test.py
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
    from typing import Iterator, SupportsIndex\nfrom typing import TypeVar\n_S = TypeVar('S');\
    \ _T = TypeVar('T'); _U = TypeVar('U'); _T1 = TypeVar('T1'); _T2 = TypeVar('T2');\
    \ _T3 = TypeVar('T3'); _T4 = TypeVar('T4'); _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\
    \n\n\nclass SliceIteratorReverse(Iterator[_T]):\n    def __init__(self, A: list[_T],\
    \ L: list[SupportsIndex]):\n        self.A, self.L, self.r = A, L, len(A)\n  \
    \  def __len__(self): return len(self.L)\n    def __next__(self):\n        L =\
    \ self.L\n        if not L: raise StopIteration\n        self.r, r = (l := L.pop()),\
    \ self.r\n        return self.A[l:r]\n"
  code: "import cp_library.__header__\nfrom typing import Iterator, SupportsIndex\n\
    from cp_library.misc.typing import _T\nimport cp_library.alg.__header__\nimport\
    \ cp_library.alg.iter.__header__\n\nclass SliceIteratorReverse(Iterator[_T]):\n\
    \    def __init__(self, A: list[_T], L: list[SupportsIndex]):\n        self.A,\
    \ self.L, self.r = A, L, len(A)\n    def __len__(self): return len(self.L)\n \
    \   def __next__(self):\n        L = self.L\n        if not L: raise StopIteration\n\
    \        self.r, r = (l := L.pop()), self.r\n        return self.A[l:r]"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/slice_iterator_reverse_cls.py
  requiredBy:
  - cp_library/alg/graph/csr/digraph_cls.py
  - cp_library/alg/graph/csr/dag_cls.py
  - cp_library/alg/graph/csr/snippets/two_edge_connected_components_fn.py
  - cp_library/alg/graph/csr/snippets/strongly_connected_components_fn.py
  - cp_library/alg/graph/csr/snippets/biconnected_components_edge_ids_fn.py
  - cp_library/alg/graph/csr/snippets/scc_labels_fn.py
  - cp_library/alg/graph/csr/snippets/biconnected_components_vertices_fn.py
  timestamp: '2025-07-21 03:35:11+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/graph/cycle_detection.test.py
  - test/library-checker/graph/scc_strongly_connected_components.test.py
  - test/library-checker/graph/scc.test.py
  - test/library-checker/graph/two_edge_connected_components.test.py
  - test/library-checker/graph/biconnected_components.test.py
  - test/aoj/grl/grl_2_c_scc.test.py
  - test/atcoder/abc/abc245_f_digraph.test.py
  - test/atcoder/abc/abc218_f_fast_shortest_path.test.py
documentation_of: cp_library/alg/iter/slice_iterator_reverse_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/slice_iterator_reverse_cls.py
- /library/cp_library/alg/iter/slice_iterator_reverse_cls.py.html
title: cp_library/alg/iter/slice_iterator_reverse_cls.py
---
