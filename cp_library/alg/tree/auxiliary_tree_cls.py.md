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
    path: cp_library/alg/iter/argsort_fn.py
    title: cp_library/alg/iter/argsort_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/presum_fn.py
    title: cp_library/alg/iter/presum_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/lca_table_iterative_cls.py
    title: cp_library/alg/tree/lca_table_iterative_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack_sm_fn.py
    title: cp_library/bit/pack_sm_fn.py
  - icon: ':question:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/min_sparse_table_cls.py
    title: cp_library/ds/min_sparse_table_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    from itertools import pairwise\n\n\ndef sort2(a, b):\n    return (a,b) if a <\
    \ b else (b,a)\n\nimport operator\nfrom itertools import accumulate\nfrom typing\
    \ import Callable, Iterable, TypeVar\n_T = TypeVar('T')\n\ndef presum(iter: Iterable[_T],\
    \ func: Callable[[_T,_T],_T] = None, initial: _T = None, step = 1) -> list[_T]:\n\
    \    if step == 1:\n        return list(accumulate(iter, func, initial=initial))\n\
    \    else:\n        assert step >= 2\n        if func is None:\n            func\
    \ = operator.add\n        A = list(iter)\n        if initial is not None:\n  \
    \          A = [initial] + A\n        for i in range(step,len(A)):\n         \
    \   A[i] = func(A[i], A[i-step])\n        return A\n# from typing import Generic\n\
    # from cp_library.misc.typing import _T\n\ndef min2(a, b):\n    return a if a\
    \ < b else b\n\n\n\nclass MinSparseTable:\n    def __init__(st, arr: list):\n\
    \        st.N = N = len(arr)\n        st.log = N.bit_length()\n        st.data\
    \ = data = [0] * (st.log*N)\n        data[:N] = arr \n        for i in range(1,st.log):\n\
    \            a, b, c = i*N, (i-1)*N, (i-1)*N + (1 << (i-1))\n            for j\
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
    \ path\n\n\ndef pack_sm(N: int):\n    s = N.bit_length()\n    return s, (1<<s)-1\n\
    \ndef pack_enc(a: int, b: int, s: int):\n    return a << s | b\n    \ndef pack_dec(ab:\
    \ int, s: int, m: int):\n    return ab >> s, ab & m\n\ndef pack_indices(A, s):\n\
    \    return [a << s | i for i,a in enumerate(A)]\n\ndef argsort(A: list[int],\
    \ reverse=False):\n    s, m = pack_sm(len(A))\n    if reverse:\n        I = [a<<s|i^m\
    \ for i,a in enumerate(A)]\n        I.sort(reverse=True)\n        for i,ai in\
    \ enumerate(I): I[i] = (ai^m)&m\n    else:\n        I = [a<<s|i for i,a in enumerate(A)]\n\
    \        I.sort()\n        for i,ai in enumerate(I): I[i] = ai&m\n    return I\n\
    \nclass AuxiliaryTree(LCATable):\n\n    def __init__(self, T, root=0):\n     \
    \   super().__init__(T, root)\n        self.par = [-1]*T.N\n\n    def bucketize(self,\
    \ K, A):\n        self.pre_all = pre_all = argsort(self.start)\n        self.buckets\
    \ = buckets = [[] for _ in range(K)]\n        for u in pre_all:\n            buckets[A[u]].append(u)\n\
    \        return buckets\n\n    def build_postorder(self, V, sort = False):\n \
    \       if sort:\n            V = sorted(V, key=self.start.__getitem__)\n    \
    \    L = len(V)\n        post, stc, start, par = elist(L<<1), elist(L), self.start,\
    \ self.par\n        stc.append(V[0])\n        par[V[0]] = -1\n        for u, v\
    \ in pairwise(V):\n            lca, _ = self.query(u, v)\n            if lca !=\
    \ u:\n                last = stc.pop()\n                while stc and start[top\
    \ := stc[-1]] > start[lca]:\n                    post.append(last)\n         \
    \           par[last] = last = stc.pop()\n                if not stc or top !=\
    \ lca:\n                    stc.append(lca)\n                    par[lca] = -1\n\
    \                    \n                post.append(last)\n                par[last]\
    \ = lca\n            stc.append(v)\n            par[v] = -1\n        \n      \
    \  last = stc.pop()\n        while stc:\n            post.append(last)\n     \
    \       par[last] = last = stc.pop()\n        post.append(last)\n        return\
    \ post, par\n\n\ndef elist(est_len: int) -> list: ...\ntry:\n    from __pypy__\
    \ import newlist_hint\nexcept:\n    def newlist_hint(hint):\n        return []\n\
    elist = newlist_hint\n    \n\n"
  code: "import cp_library.alg.tree.__header__\nfrom itertools import pairwise\nfrom\
    \ cp_library.alg.tree.lca_table_iterative_cls import LCATable\nfrom cp_library.alg.iter.argsort_fn\
    \ import argsort\n\nclass AuxiliaryTree(LCATable):\n\n    def __init__(self, T,\
    \ root=0):\n        super().__init__(T, root)\n        self.par = [-1]*T.N\n\n\
    \    def bucketize(self, K, A):\n        self.pre_all = pre_all = argsort(self.start)\n\
    \        self.buckets = buckets = [[] for _ in range(K)]\n        for u in pre_all:\n\
    \            buckets[A[u]].append(u)\n        return buckets\n\n    def build_postorder(self,\
    \ V, sort = False):\n        if sort:\n            V = sorted(V, key=self.start.__getitem__)\n\
    \        L = len(V)\n        post, stc, start, par = elist(L<<1), elist(L), self.start,\
    \ self.par\n        stc.append(V[0])\n        par[V[0]] = -1\n        for u, v\
    \ in pairwise(V):\n            lca, _ = self.query(u, v)\n            if lca !=\
    \ u:\n                last = stc.pop()\n                while stc and start[top\
    \ := stc[-1]] > start[lca]:\n                    post.append(last)\n         \
    \           par[last] = last = stc.pop()\n                if not stc or top !=\
    \ lca:\n                    stc.append(lca)\n                    par[lca] = -1\n\
    \                    \n                post.append(last)\n                par[last]\
    \ = lca\n            stc.append(v)\n            par[v] = -1\n        \n      \
    \  last = stc.pop()\n        while stc:\n            post.append(last)\n     \
    \       par[last] = last = stc.pop()\n        post.append(last)\n        return\
    \ post, par\n\nfrom cp_library.ds.elist_fn import elist\n\n"
  dependsOn:
  - cp_library/alg/tree/lca_table_iterative_cls.py
  - cp_library/alg/iter/argsort_fn.py
  - cp_library/ds/elist_fn.py
  - cp_library/alg/dp/sort2_fn.py
  - cp_library/alg/iter/presum_fn.py
  - cp_library/ds/min_sparse_table_cls.py
  - cp_library/bit/pack_sm_fn.py
  - cp_library/alg/dp/min2_fn.py
  isVerificationFile: false
  path: cp_library/alg/tree/auxiliary_tree_cls.py
  requiredBy: []
  timestamp: '2025-03-28 19:21:24+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/tree/auxiliary_tree_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/tree/auxiliary_tree_cls.py
- /library/cp_library/alg/tree/auxiliary_tree_cls.py.html
title: cp_library/alg/tree/auxiliary_tree_cls.py
---
