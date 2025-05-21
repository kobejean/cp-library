---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/min2_fn.py
    title: cp_library/alg/dp/min2_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/sort2_fn.py
    title: cp_library/alg/dp/sort2_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/presum_fn.py
    title: cp_library/alg/iter/presum_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/lca_table_iterative_cls.py
    title: cp_library/alg/tree/lca_table_iterative_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/min_sparse_table_cls.py
    title: cp_library/ds/min_sparse_table_cls.py
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/fast/aux_tree_weighted_cls.py
    title: cp_library/alg/tree/fast/aux_tree_weighted_cls.py
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
    path: test/aoj/vol/0439_aux_weighted_rerooting_dp.test.py
    title: test/aoj/vol/0439_aux_weighted_rerooting_dp.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
    title: test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc361_e_tree_diameter.test.py
    title: test/atcoder/abc/abc361_e_tree_diameter.test.py
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
    \n\nimport operator\nfrom itertools import accumulate\nfrom typing import Callable,\
    \ Iterable\n\nfrom typing import TypeVar\n_T = TypeVar('T')\n_U = TypeVar('U')\n\
    \ndef presum(iter: Iterable[_T], func: Callable[[_T,_T],_T] = None, initial: _T\
    \ = None, step = 1) -> list[_T]:\n    if step == 1:\n        return list(accumulate(iter,\
    \ func, initial=initial))\n    else:\n        assert step >= 2\n        if func\
    \ is None:\n            func = operator.add\n        A = list(iter)\n        if\
    \ initial is not None:\n            A = [initial] + A\n        for i in range(step,len(A)):\n\
    \            A[i] = func(A[i], A[i-step])\n        return A\n\n\ndef sort2(a,\
    \ b):\n    return (a,b) if a < b else (b,a)\n# from typing import Generic\n# from\
    \ cp_library.misc.typing import _T\n\ndef min2(a, b):\n    return a if a < b else\
    \ b\n\n\n\nclass MinSparseTable:\n    def __init__(st, arr: list):\n        st.N\
    \ = N = len(arr)\n        st.log = N.bit_length()\n        st.data = data = [0]\
    \ * (st.log*N)\n        data[:N] = arr \n        for i in range(1,st.log):\n \
    \           a, b, c = i*N, (i-1)*N, (i-1)*N + (1 << (i-1))\n            for j\
    \ in range(N - (1 << i) + 1):\n                data[a+j] = min2(data[b+j], data[c+j])\n\
    \n    def query(st, l: int, r: int):\n        k = (r-l).bit_length() - 1\n   \
    \     return min2(st.data[k*st.N + l], st.data[k*st.N + r - (1<<k)])\n    \n\n\
    class LCATable(MinSparseTable):\n    def __init__(lca, T, root = 0):\n       \
    \ N = len(T)\n        T.euler_tour(root)\n        lca.depth = depth = presum(T.delta)\n\
    \        lca.tin, lca.tout = T.tin[:], T.tout[:]\n        lca.mask = (1 << (shift\
    \ := N.bit_length()))-1\n        lca.shift = shift\n        order = T.order\n\
    \        M = len(order)\n        packets = [0]*M\n        for i in range(M):\n\
    \            packets[i] = depth[i] << shift | order[i] \n        super().__init__(packets)\n\
    \n    def _query(lca, u, v):\n        l, r = sort2(lca.tin[u], lca.tin[v]); r\
    \ += 1\n        da = super().query(l, r)\n        return l, r, da & lca.mask,\
    \ da >> lca.shift\n\n    def query(lca, u, v) -> tuple[int,int]:\n        l, r,\
    \ a, d = lca._query(u, v)\n        return a, d\n    \n    def distance(lca, u,\
    \ v) -> int:\n        l, r, a, d = lca._query(u, v)\n        return lca.depth[l]\
    \ + lca.depth[r-1] - 2*d\n    \n    def path(lca, u, v):\n        path, par, lca,\
    \ c = [], lca.T.par, lca.query(u, v)[0], u\n        while c != lca:\n        \
    \    path.append(c)\n            c = par[c]\n        path.append(lca)\n      \
    \  rev_path, c = [], v\n        while c != lca:\n            rev_path.append(c)\n\
    \            c = par[c]\n        path.extend(reversed(rev_path))\n        return\
    \ path\n\nclass LCATableWeighted(LCATable):\n    def __init__(lca, T, root = 0):\n\
    \        super().__init__(T, root)\n        lca.weights = T.Wdelta\n        lca.weighted_depth\
    \ = None\n\n    def distance(lca, u, v) -> int:\n        if lca.weighted_depth\
    \ is None:\n            lca.weighted_depth = presum(lca.weights)\n        l, r,\
    \ a, _ = lca._query(u, v)\n        m = lca.tin[a]\n        return lca.weighted_depth[l]\
    \ + lca.weighted_depth[r-1] - 2*lca.weighted_depth[m]\n"
  code: "import cp_library.__header__\nimport cp_library.alg.__header__\nimport cp_library.alg.tree.__header__\n\
    from cp_library.alg.iter.presum_fn import presum\nfrom cp_library.alg.tree.lca_table_iterative_cls\
    \ import LCATable\n\nclass LCATableWeighted(LCATable):\n    def __init__(lca,\
    \ T, root = 0):\n        super().__init__(T, root)\n        lca.weights = T.Wdelta\n\
    \        lca.weighted_depth = None\n\n    def distance(lca, u, v) -> int:\n  \
    \      if lca.weighted_depth is None:\n            lca.weighted_depth = presum(lca.weights)\n\
    \        l, r, a, _ = lca._query(u, v)\n        m = lca.tin[a]\n        return\
    \ lca.weighted_depth[l] + lca.weighted_depth[r-1] - 2*lca.weighted_depth[m]"
  dependsOn:
  - cp_library/alg/iter/presum_fn.py
  - cp_library/alg/tree/lca_table_iterative_cls.py
  - cp_library/alg/dp/sort2_fn.py
  - cp_library/ds/min_sparse_table_cls.py
  - cp_library/alg/dp/min2_fn.py
  isVerificationFile: false
  path: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
  requiredBy:
  - cp_library/alg/tree/tree_weighted_cls.py
  - cp_library/alg/tree/tree_weighted_proto.py
  - cp_library/alg/tree/fast/aux_tree_weighted_cls.py
  timestamp: '2025-05-21 18:01:52+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/abc/abc294_g_fast_tree_lca_table_weighted_bit.test.py
  - test/atcoder/abc/abc361_e_tree_diameter.test.py
  - test/yukicoder/3407.test.py
  - test/aoj/vol/0439_aux_weighted_rerooting_dp.test.py
  - test/aoj/grl/grl_5_a_diameter.test.py
documentation_of: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/tree/lca_table_weighted_iterative_cls.py
- /library/cp_library/alg/tree/lca_table_weighted_iterative_cls.py.html
title: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
---
