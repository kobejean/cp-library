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
  bundledCode: "\nfrom itertools import accumulate\nfrom typing import Callable, Iterable,\
    \ TypeVar\n\nT = TypeVar('T')\ndef presum(iter: Iterable[T], func: Callable[[T,T],T]\
    \ = None, initial: T = None) -> list[T]:\n    return list(accumulate(iter, func,\
    \ initial=initial))\n"
  code: "import cp_library.alg.iter.__header__\nfrom itertools import accumulate\n\
    from typing import Callable, Iterable, TypeVar\n\nT = TypeVar('T')\ndef presum(iter:\
    \ Iterable[T], func: Callable[[T,T],T] = None, initial: T = None) -> list[T]:\n\
    \    return list(accumulate(iter, func, initial=initial))"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/presum_fn.py
  requiredBy:
  - cp_library/alg/tree/tree_weighted_proto.py
  - cp_library/alg/tree/tree_weighted_cls.py
  - cp_library/alg/tree/lca_table_weighted_iterative_cls.py
  timestamp: '2024-11-25 19:30:19+09:00'
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
