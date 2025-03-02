---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/alg/tree/auxiliary_tree_cls.py
    title: cp_library/alg/tree/auxiliary_tree_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/lca_table_iterative_cls.py
    title: cp_library/alg/tree/lca_table_iterative_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
    title: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_cls.py
    title: cp_library/alg/tree/tree_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_proto.py
    title: cp_library/alg/tree/tree_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_weighted_cls.py
    title: cp_library/alg/tree/tree_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_weighted_proto.py
    title: cp_library/alg/tree/tree_weighted_proto.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_5_a_diameter.test.py
    title: test/aoj/grl/grl_5_a_diameter.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_5_c_lca_table_iterative.test.py
    title: test/aoj/grl/grl_5_c_lca_table_iterative.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc175_d_permutation.test.py
    title: test/atcoder/abc/abc175_d_permutation.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc202_e_dfs_enter_leave.test.py
    title: test/atcoder/abc/abc202_e_dfs_enter_leave.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
    title: test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc294_g_tree_heavy_light_decomposition.test.py
    title: test/atcoder/abc/abc294_g_tree_heavy_light_decomposition.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc294_g_tree_lca_table_weighted_bit.test.py
    title: test/atcoder/abc/abc294_g_tree_lca_table_weighted_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc337_g_tree_inversion_heavy_light_decomposition.test.py
    title: test/atcoder/abc/abc337_g_tree_inversion_heavy_light_decomposition.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc361_e_tree_diameter.test.py
    title: test/atcoder/abc/abc361_e_tree_diameter.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/dp/dp_v_subtree_rerooting_iterative.test.py
    title: test/atcoder/dp/dp_v_subtree_rerooting_iterative.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/dp/dp_v_subtree_rerooting_recursive.test.py
    title: test/atcoder/dp/dp_v_subtree_rerooting_recursive.test.py
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
    import operator\nfrom itertools import accumulate\nfrom typing import Callable,\
    \ Iterable, TypeVar\n_T = TypeVar('T')\n\ndef presum(iter: Iterable[_T], func:\
    \ Callable[[_T,_T],_T] = None, initial: _T = None, step = 1) -> list[_T]:\n  \
    \  if step == 1:\n        return list(accumulate(iter, func, initial=initial))\n\
    \    else:\n        assert step >= 2\n        if func is None:\n            func\
    \ = operator.add\n        A = list(iter)\n        if initial is not None:\n  \
    \          A = [initial] + A\n        for i in range(step,len(A)):\n         \
    \   A[i] = func(A[i], A[i-step])\n        return A\n"
  code: "import cp_library.alg.iter.__header__\nimport operator\nfrom itertools import\
    \ accumulate\nfrom typing import Callable, Iterable, TypeVar\nfrom cp_library.misc.typing\
    \ import _T\n\ndef presum(iter: Iterable[_T], func: Callable[[_T,_T],_T] = None,\
    \ initial: _T = None, step = 1) -> list[_T]:\n    if step == 1:\n        return\
    \ list(accumulate(iter, func, initial=initial))\n    else:\n        assert step\
    \ >= 2\n        if func is None:\n            func = operator.add\n        A =\
    \ list(iter)\n        if initial is not None:\n            A = [initial] + A\n\
    \        for i in range(step,len(A)):\n            A[i] = func(A[i], A[i-step])\n\
    \        return A"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/presum_fn.py
  requiredBy:
  - cp_library/alg/tree/tree_weighted_proto.py
  - cp_library/alg/tree/tree_proto.py
  - cp_library/alg/tree/tree_cls.py
  - cp_library/alg/tree/lca_table_iterative_cls.py
  - cp_library/alg/tree/tree_weighted_cls.py
  - cp_library/alg/tree/auxiliary_tree_cls.py
  - cp_library/alg/tree/lca_table_weighted_iterative_cls.py
  timestamp: '2025-03-02 23:16:20+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/grl/grl_5_c_lca_table_iterative.test.py
  - test/aoj/grl/grl_5_a_diameter.test.py
  - test/atcoder/abc/abc361_e_tree_diameter.test.py
  - test/atcoder/abc/abc175_d_permutation.test.py
  - test/atcoder/abc/abc337_g_tree_inversion_heavy_light_decomposition.test.py
  - test/atcoder/abc/abc294_g_tree_heavy_light_decomposition.test.py
  - test/atcoder/abc/abc202_e_dfs_enter_leave.test.py
  - test/atcoder/abc/abc294_g_tree_lca_table_weighted_bit.test.py
  - test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
  - test/atcoder/dp/dp_v_subtree_rerooting_iterative.test.py
  - test/atcoder/dp/dp_v_subtree_rerooting_recursive.test.py
documentation_of: cp_library/alg/iter/presum_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/presum_fn.py
- /library/cp_library/alg/iter/presum_fn.py.html
title: cp_library/alg/iter/presum_fn.py
---
