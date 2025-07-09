---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/csr/aux_tree_base_cls.py
    title: cp_library/alg/tree/csr/aux_tree_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/csr/aux_tree_cls.py
    title: cp_library/alg/tree/csr/aux_tree_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/csr/aux_tree_weighted_cls.py
    title: cp_library/alg/tree/csr/aux_tree_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/lca_table_iterative_cls.py
    title: cp_library/alg/tree/lca_table_iterative_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
    title: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_5_c_lca_table_iterative.test.py
    title: test/aoj/grl/grl_5_c_lca_table_iterative.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/vol/0439_aux_dijkstra.test.py
    title: test/aoj/vol/0439_aux_dijkstra.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/vol/0439_aux_rerooting_dp.test.py
    title: test/aoj/vol/0439_aux_rerooting_dp.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/vol/0439_aux_weighted_rerooting_dp.test.py
    title: test/aoj/vol/0439_aux_weighted_rerooting_dp.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc175_d_permutation.test.py
    title: test/atcoder/abc/abc175_d_permutation.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
    title: test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc337_g_tree_inversion_hld_bit.test.py
    title: test/atcoder/abc/abc337_g_tree_inversion_hld_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc337_g_tree_inversion_hld_fast.test.py
    title: test/atcoder/abc/abc337_g_tree_inversion_hld_fast.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/static_range_sum.test.py
    title: test/library-checker/data-structure/static_range_sum.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/tree/jump_on_tree.test.py
    title: test/library-checker/tree/jump_on_tree.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/tree/lca.test.py
    title: test/library-checker/tree/lca.test.py
  - icon: ':heavy_check_mark:'
    path: test/yukicoder/3407.test.py
    title: test/yukicoder/3407.test.py
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
    \ Iterable\n\n\nfrom typing import TypeVar\n_T = TypeVar('T')\n_U = TypeVar('U')\n\
    \ndef presum(iter: Iterable[_T], func: Callable[[_T,_T],_T] = None, initial: _T\
    \ = None, step = 1) -> list[_T]:\n    if step == 1:\n        return list(accumulate(iter,\
    \ func, initial=initial))\n    else:\n        assert step >= 2\n        if func\
    \ is None:\n            func = operator.add\n        A = list(iter)\n        if\
    \ initial is not None:\n            A = [initial] + A\n        for i in range(step,len(A)):\n\
    \            A[i] = func(A[i], A[i-step])\n        return A\n"
  code: "import cp_library.__header__\nimport operator\nfrom itertools import accumulate\n\
    from typing import Callable, Iterable\nimport cp_library.alg.__header__\nimport\
    \ cp_library.alg.iter.__header__\nfrom cp_library.misc.typing import _T\n\ndef\
    \ presum(iter: Iterable[_T], func: Callable[[_T,_T],_T] = None, initial: _T =\
    \ None, step = 1) -> list[_T]:\n    if step == 1:\n        return list(accumulate(iter,\
    \ func, initial=initial))\n    else:\n        assert step >= 2\n        if func\
    \ is None:\n            func = operator.add\n        A = list(iter)\n        if\
    \ initial is not None:\n            A = [initial] + A\n        for i in range(step,len(A)):\n\
    \            A[i] = func(A[i], A[i-step])\n        return A"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/alg/iter/presum_fn.py
  requiredBy:
  - cp_library/alg/tree/csr/aux_tree_base_cls.py
  - cp_library/alg/tree/csr/aux_tree_weighted_cls.py
  - cp_library/alg/tree/csr/aux_tree_cls.py
  - cp_library/alg/tree/lca_table_iterative_cls.py
  - cp_library/alg/tree/lca_table_weighted_iterative_cls.py
  timestamp: '2025-07-09 08:31:42+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/yukicoder/3407.test.py
  - test/aoj/vol/0439_aux_rerooting_dp.test.py
  - test/aoj/vol/0439_aux_dijkstra.test.py
  - test/aoj/vol/0439_aux_weighted_rerooting_dp.test.py
  - test/aoj/grl/grl_5_c_lca_table_iterative.test.py
  - test/library-checker/tree/jump_on_tree.test.py
  - test/library-checker/tree/lca.test.py
  - test/library-checker/data-structure/static_range_sum.test.py
  - test/atcoder/abc/abc337_g_tree_inversion_hld_bit.test.py
  - test/atcoder/abc/abc175_d_permutation.test.py
  - test/atcoder/abc/abc337_g_tree_inversion_hld_fast.test.py
  - test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
documentation_of: cp_library/alg/iter/presum_fn.py
layout: document
redirect_from:
- /library/cp_library/alg/iter/presum_fn.py
- /library/cp_library/alg/iter/presum_fn.py.html
title: cp_library/alg/iter/presum_fn.py
---
