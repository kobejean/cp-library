---
data:
  _extendedDependsOn:
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
    from itertools import pairwise\n\nimport operator\nfrom itertools import accumulate\n\
    from typing import Callable, Iterable, TypeVar\n\nT = TypeVar('T')\ndef presum(iter:\
    \ Iterable[T], func: Callable[[T,T],T] = None, initial: T = None, step = 1) ->\
    \ list[T]:\n    if step == 1:\n        return list(accumulate(iter, func, initial=initial))\n\
    \    else:\n        assert step >= 2\n        if func is None:\n            func\
    \ = operator.add\n        A = list(iter)\n        if initial is not None:\n  \
    \          A = [initial] + A\n        for i in range(step,len(A)):\n         \
    \   A[i] = func(A[i], A[i-step])\n        return A\n\nfrom typing import Any,\
    \ List\n\nclass MinSparseTable:\n    def __init__(self, arr: List[Any]):\n   \
    \     self.N = N = len(arr)\n        self.log = N.bit_length()\n        \n   \
    \     self.offsets = offsets = [0]\n        for i in range(1, self.log):\n   \
    \         offsets.append(offsets[-1] + N - (1 << (i-1)) + 1)\n            \n \
    \       self.st = st = [0] * (offsets[-1] + N - (1 << (self.log-1)) + 1)\n   \
    \     st[:N] = arr \n        \n        for i,ni in pairwise(range(self.log)):\n\
    \            start, nxt, d = offsets[i], offsets[ni], 1 << i\n            for\
    \ j in range(N - (1 << ni) + 1):\n                st[nxt+j] = min(st[k := start+j],\
    \ st[k + d])\n\n    def query(self, l: int, r: int) -> Any:\n        k = (r-l).bit_length()\
    \ - 1\n        start, st = self.offsets[k], self.st\n        return min(st[start\
    \ + l], st[start + r - (1 << k)])\n    \n    def __repr__(self) -> str:\n    \
    \    rows, offsets, log, st = [], self.offsets, self.log, self.st\n        for\
    \ i in range(log):\n            start = offsets[i]\n            end = offsets[i+1]\
    \ if i+1 < log else len(st)\n            rows.append(f\"{i:<2d} {st[start:end]}\"\
    )\n        return '\\n'.join(rows)\n\nclass LCATable(MinSparseTable):\n    def\
    \ __init__(self, T, root = 0):\n        N = len(T)\n        T.euler_tour(root)\n\
    \        self.depth = depth = presum(T.delta)\n        self.start, self.stop =\
    \ T.tin, T.tout\n        self.mask = (1 << (shift := N.bit_length()))-1\n    \
    \    self.shift = shift\n        order = T.order\n        M = len(order)\n   \
    \     packets = [0]*M\n        for i in range(M):\n            packets[i] = depth[i]\
    \ << shift | order[i] \n        super().__init__(packets)\n\n    def _query(self,\
    \ u, v):\n        start = self.start\n        l,r = min(start[u], start[v]), max(start[u],\
    \ start[v])+1\n        da = super().query(l, r)\n        return l, r, da & self.mask,\
    \ da >> self.shift\n\n    def query(self, u, v) -> tuple[int,int]:\n        l,\
    \ r, a, d = self._query(u, v)\n        return a, d\n    \n    def distance(self,\
    \ u, v) -> int:\n        l, r, a, d = self._query(u, v)\n        return self.depth[l]\
    \ + self.depth[r] - 2*d\n    \n    def path(self, u, v):\n        path, par, lca,\
    \ c = [], self.T.par, self.query(u, v)[0], u\n        while c != lca:\n      \
    \      path.append(c)\n            c = par[c]\n        path.append(lca)\n    \
    \    rev_path, c = [], v\n        while c != lca:\n            rev_path.append(c)\n\
    \            c = par[c]\n        path.extend(reversed(rev_path))\n        return\
    \ path\n\ndef argsort(A: list[int]):\n    N = len(A)\n    mask = (1 << (shift\
    \ := N.bit_length())) - 1\n    indices = [0]*N\n    for i in range(N):\n     \
    \   indices[i] = A[i] << shift | i\n    indices.sort()\n    for i in range(N):\n\
    \        indices[i] &= mask\n    return indices\n\nclass AuxiliaryTree(LCATable):\n\
    \n    def __init__(self, T, root=0):\n        super().__init__(T, root)\n    \
    \    self.par = [-1]*T.N\n\n    def bucketize(self, K, A):\n        self.pre_all\
    \ = pre_all = argsort(self.start)\n        self.buckets = buckets = [[] for _\
    \ in range(K)]\n        for u in pre_all:\n            buckets[A[u]].append(u)\n\
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
  - cp_library/alg/iter/presum_fn.py
  - cp_library/ds/min_sparse_table_cls.py
  isVerificationFile: false
  path: cp_library/alg/tree/auxiliary_tree_cls.py
  requiredBy: []
  timestamp: '2024-12-21 20:47:09+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/tree/auxiliary_tree_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/tree/auxiliary_tree_cls.py
- /library/cp_library/alg/tree/auxiliary_tree_cls.py.html
title: cp_library/alg/tree/auxiliary_tree_cls.py
---
