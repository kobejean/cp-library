---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
    title: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_weighted_cls.py
    title: cp_library/alg/tree/tree_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_weighted_proto.py
    title: cp_library/alg/tree/tree_weighted_proto.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/abc175_d_permutation.test.py
    title: test/abc175_d_permutation.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
    title: test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
    title: test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc337_g_tree_inversion_heavy_light_decomposition.test.py
    title: test/abc337_g_tree_inversion_heavy_light_decomposition.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc361_e_tree_diameter.test.py
    title: test/abc361_e_tree_diameter.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "\nimport operator\nfrom itertools import accumulate\nfrom typing import\
    \ Callable, Iterable, TypeVar\n\nT = TypeVar('T')\ndef presum(iter: Iterable[T],\
    \ func: Callable[[T,T],T] = None, initial: T = None, step = 1) -> list[T]:\n \
    \   match step:\n        case 1:\n            return list(accumulate(iter, func,\
    \ initial=initial))\n        case step:\n            assert step >= 2\n      \
    \      if func is None:\n                func = operator.add\n            A =\
    \ list(iter)\n            if initial is not None:\n                A = [initial]\
    \ + A\n            for i in range(step,len(A)):\n                A[i] = func(A[i],\
    \ A[i-step])\n            return A\n"
  code: "import cp_library.alg.iter.__header__\nimport operator\nfrom itertools import\
    \ accumulate\nfrom typing import Callable, Iterable, TypeVar\n\nT = TypeVar('T')\n\
    def presum(iter: Iterable[T], func: Callable[[T,T],T] = None, initial: T = None,\
    \ step = 1) -> list[T]:\n    match step:\n        case 1:\n            return\
    \ list(accumulate(iter, func, initial=initial))\n        case step:\n        \
    \    assert step >= 2\n            if func is None:\n                func = operator.add\n\
    \            A = list(iter)\n            if initial is not None:\n           \
    \     A = [initial] + A\n            for i in range(step,len(A)):\n          \
    \      A[i] = func(A[i], A[i-step])\n            return A"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/presum_fn.py
  requiredBy:
  - cp_library/alg/tree/tree_weighted_proto.py
  - cp_library/alg/tree/tree_weighted_cls.py
  - cp_library/alg/tree/lca_table_weighted_iterative_cls.py
  timestamp: '2024-12-08 04:35:12+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/abc175_d_permutation.test.py
  - test/abc337_g_tree_inversion_heavy_light_decomposition.test.py
  - test/abc361_e_tree_diameter.test.py
  - test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
  - test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
documentation_of: cp_library/alg/iter/presum_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/presum_fn.py
- /library/cp_library/alg/iter/presum_fn.py.html
title: cp_library/alg/iter/presum_fn.py
---
