---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/min2_fn.py
    title: cp_library/alg/dp/min2_fn.py
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/fast/aux_tree_base_cls.py
    title: cp_library/alg/tree/fast/aux_tree_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/fast/aux_tree_cls.py
    title: cp_library/alg/tree/fast/aux_tree_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/fast/aux_tree_weighted_cls.py
    title: cp_library/alg/tree/fast/aux_tree_weighted_cls.py
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
    path: test/aoj/vol/0439_aux_dijkstra.test.py
    title: test/aoj/vol/0439_aux_dijkstra.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/vol/0439_aux_rerooting_dp.test.py
    title: test/aoj/vol/0439_aux_rerooting_dp.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/vol/0439_aux_weighted_rerooting_dp.test.py
    title: test/aoj/vol/0439_aux_weighted_rerooting_dp.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc202_e_dfs_enter_leave.test.py
    title: test/atcoder/abc/abc202_e_dfs_enter_leave.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
    title: test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc361_e_tree_diameter.test.py
    title: test/atcoder/abc/abc361_e_tree_diameter.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/dp/dp_v_subtree_rerooting_iterative.test.py
    title: test/atcoder/dp/dp_v_subtree_rerooting_iterative.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/dp/dp_v_subtree_rerooting_recursive.test.py
    title: test/atcoder/dp/dp_v_subtree_rerooting_recursive.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/data-structure/staticrmq.test.py
    title: test/library-checker/data-structure/staticrmq.test.py
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
    # from typing import Generic\n# from cp_library.misc.typing import _T\n\n\ndef\
    \ min2(a, b):\n    return a if a < b else b\n\n\n\nclass MinSparseTable:\n   \
    \ def __init__(st, arr: list):\n        st.N = N = len(arr)\n        st.log =\
    \ N.bit_length()\n        st.data = data = [0] * (st.log*N)\n        data[:N]\
    \ = arr \n        for i in range(1,st.log):\n            a, b, c = i*N, (i-1)*N,\
    \ (i-1)*N + (1 << (i-1))\n            for j in range(N - (1 << i) + 1):\n    \
    \            data[a+j] = min2(data[b+j], data[c+j])\n\n    def query(st, l: int,\
    \ r: int):\n        k = (r-l).bit_length() - 1\n        return min2(st.data[k*st.N\
    \ + l], st.data[k*st.N + r - (1<<k)])\n    \n"
  code: "import cp_library.__header__\n# from typing import Generic\n# from cp_library.misc.typing\
    \ import _T\nfrom cp_library.alg.dp.min2_fn import min2\n\nimport cp_library.ds.__header__\n\
    \nclass MinSparseTable:\n    def __init__(st, arr: list):\n        st.N = N =\
    \ len(arr)\n        st.log = N.bit_length()\n        st.data = data = [0] * (st.log*N)\n\
    \        data[:N] = arr \n        for i in range(1,st.log):\n            a, b,\
    \ c = i*N, (i-1)*N, (i-1)*N + (1 << (i-1))\n            for j in range(N - (1\
    \ << i) + 1):\n                data[a+j] = min2(data[b+j], data[c+j])\n\n    def\
    \ query(st, l: int, r: int):\n        k = (r-l).bit_length() - 1\n        return\
    \ min2(st.data[k*st.N + l], st.data[k*st.N + r - (1<<k)])\n    "
  dependsOn:
  - cp_library/alg/dp/min2_fn.py
  isVerificationFile: false
  path: cp_library/ds/min_sparse_table_cls.py
  requiredBy:
  - cp_library/alg/tree/fast/aux_tree_base_cls.py
  - cp_library/alg/tree/fast/aux_tree_weighted_cls.py
  - cp_library/alg/tree/fast/aux_tree_cls.py
  - cp_library/alg/tree/tree_weighted_cls.py
  - cp_library/alg/tree/tree_weighted_proto.py
  - cp_library/alg/tree/lca_table_iterative_cls.py
  - cp_library/alg/tree/tree_cls.py
  - cp_library/alg/tree/lca_table_weighted_iterative_cls.py
  - cp_library/alg/tree/tree_proto.py
  timestamp: '2025-06-20 03:24:59+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/yukicoder/3407.test.py
  - test/aoj/vol/0439_aux_rerooting_dp.test.py
  - test/aoj/vol/0439_aux_dijkstra.test.py
  - test/aoj/vol/0439_aux_weighted_rerooting_dp.test.py
  - test/aoj/grl/grl_5_c_lca_table_iterative.test.py
  - test/aoj/grl/grl_5_a_diameter.test.py
  - test/library-checker/tree/jump_on_tree.test.py
  - test/library-checker/tree/lca.test.py
  - test/library-checker/data-structure/staticrmq.test.py
  - test/atcoder/abc/abc361_e_tree_diameter.test.py
  - test/atcoder/abc/abc202_e_dfs_enter_leave.test.py
  - test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
  - test/atcoder/dp/dp_v_subtree_rerooting_recursive.test.py
  - test/atcoder/dp/dp_v_subtree_rerooting_iterative.test.py
documentation_of: cp_library/ds/min_sparse_table_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/min_sparse_table_cls.py
- /library/cp_library/ds/min_sparse_table_cls.py.html
title: cp_library/ds/min_sparse_table_cls.py
---
