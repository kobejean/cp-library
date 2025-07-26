---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge/edge_list_weighted_cls.py
    title: cp_library/alg/graph/edge/edge_list_weighted_cls.py
  - icon: ':warning:'
    path: perf/edge_list.py
    title: perf/edge_list.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_2_a_edge_list_kruskal.test.py
    title: test/aoj/grl/grl_2_a_edge_list_kruskal.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_2_b_edge_list_edmond.test.py
    title: test/aoj/grl/grl_2_b_edge_list_edmond.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/graph/directedmst_edge_list.test.py
    title: test/library-checker/graph/directedmst_edge_list.test.py
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
    import operator\nfrom typing import Generic\nfrom typing import TypeVar\n_S =\
    \ TypeVar('S'); _T = TypeVar('T'); _U = TypeVar('U'); _T1 = TypeVar('T1'); _T2\
    \ = TypeVar('T2'); _T3 = TypeVar('T3'); _T4 = TypeVar('T4'); _T5 = TypeVar('T5');\
    \ _T6 = TypeVar('T6')\n\n\ndef elist(est_len: int) -> list: ...\ntry:\n    from\
    \ __pypy__ import newlist_hint\nexcept:\n    def newlist_hint(hint):\n       \
    \ return []\nelist = newlist_hint\n    \n\n\nclass SkewHeapForrest(Generic[_T]):\n\
    \    def __init__(shf, N, M, e: _T = 0, op = operator.add):\n        shf.V, shf.A,\
    \ shf.L, shf.R, shf.roots = [e]*M, [e]*M, [-1]*M, [-1]*M, [-1]*N\n        shf.id,\
    \ shf.st, shf.e, shf.op = 0, elist(M), e, op\n    \n    def propagate(shf, u:\
    \ int):\n        if (a := shf.A[u]) != shf.e:\n            if ~(l := shf.L[u]):\
    \ shf.A[l] = shf.op(shf.A[l], a)\n            if ~(r := shf.R[u]): shf.A[r] =\
    \ shf.op(shf.A[r], a)\n            shf.V[u] = shf.op(shf.V[u], a); shf.A[u] =\
    \ shf.e\n\n    def merge(shf, u: int, v: int):\n        while ~u and ~v:\n   \
    \         shf.propagate(u); shf.propagate(v)\n            if shf.V[v] < shf.V[u]:\
    \ u, v = v, u\n            shf.st.append(u); shf.R[u], u = shf.L[u], shf.R[u]\n\
    \        u = u if ~u else v\n        while shf.st: shf.L[u := shf.st.pop()] =\
    \ u\n        return u\n    \n    def min(shf, i: int):\n        assert ~(root\
    \ := shf.roots[i])\n        shf.propagate(root)\n        return shf.V[root]\n\n\
    \    def push(shf, i: int, x: _T):\n        shf.V[shf.id] = x\n        shf.roots[i]\
    \ = shf.merge(shf.roots[i], shf.id)\n        shf.id += 1\n\n    def pop(shf, i:\
    \ int) -> _T:\n        assert ~(root := shf.roots[i])\n        shf.propagate(root)\n\
    \        val, shf.roots[i] = shf.V[root], shf.merge(shf.L[root], shf.R[root])\n\
    \        return val\n    \n    def add(shf, i: int, val: _T): shf.A[shf.roots[i]]\
    \ = shf.op(shf.A[shf.roots[i]], val)\n    def empty(shf, i: int): return shf.roots[i]\
    \ == -1\n    \n"
  code: "import cp_library.__header__\nimport operator\nfrom typing import Generic\n\
    from cp_library.misc.typing import _T\nimport cp_library.ds.__header__\nfrom cp_library.ds.elist_fn\
    \ import elist\nimport cp_library.ds.heap.__header__\n\nclass SkewHeapForrest(Generic[_T]):\n\
    \    def __init__(shf, N, M, e: _T = 0, op = operator.add):\n        shf.V, shf.A,\
    \ shf.L, shf.R, shf.roots = [e]*M, [e]*M, [-1]*M, [-1]*M, [-1]*N\n        shf.id,\
    \ shf.st, shf.e, shf.op = 0, elist(M), e, op\n    \n    def propagate(shf, u:\
    \ int):\n        if (a := shf.A[u]) != shf.e:\n            if ~(l := shf.L[u]):\
    \ shf.A[l] = shf.op(shf.A[l], a)\n            if ~(r := shf.R[u]): shf.A[r] =\
    \ shf.op(shf.A[r], a)\n            shf.V[u] = shf.op(shf.V[u], a); shf.A[u] =\
    \ shf.e\n\n    def merge(shf, u: int, v: int):\n        while ~u and ~v:\n   \
    \         shf.propagate(u); shf.propagate(v)\n            if shf.V[v] < shf.V[u]:\
    \ u, v = v, u\n            shf.st.append(u); shf.R[u], u = shf.L[u], shf.R[u]\n\
    \        u = u if ~u else v\n        while shf.st: shf.L[u := shf.st.pop()] =\
    \ u\n        return u\n    \n    def min(shf, i: int):\n        assert ~(root\
    \ := shf.roots[i])\n        shf.propagate(root)\n        return shf.V[root]\n\n\
    \    def push(shf, i: int, x: _T):\n        shf.V[shf.id] = x\n        shf.roots[i]\
    \ = shf.merge(shf.roots[i], shf.id)\n        shf.id += 1\n\n    def pop(shf, i:\
    \ int) -> _T:\n        assert ~(root := shf.roots[i])\n        shf.propagate(root)\n\
    \        val, shf.roots[i] = shf.V[root], shf.merge(shf.L[root], shf.R[root])\n\
    \        return val\n    \n    def add(shf, i: int, val: _T): shf.A[shf.roots[i]]\
    \ = shf.op(shf.A[shf.roots[i]], val)\n    def empty(shf, i: int): return shf.roots[i]\
    \ == -1\n    "
  dependsOn:
  - cp_library/ds/elist_fn.py
  isVerificationFile: false
  path: cp_library/ds/heap/skew_heap_forrest_cls.py
  requiredBy:
  - cp_library/alg/graph/edge/edge_list_weighted_cls.py
  - perf/edge_list.py
  timestamp: '2025-07-26 11:14:31+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/graph/directedmst_edge_list.test.py
  - test/aoj/grl/grl_2_b_edge_list_edmond.test.py
  - test/aoj/grl/grl_2_a_edge_list_kruskal.test.py
documentation_of: cp_library/ds/heap/skew_heap_forrest_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/heap/skew_heap_forrest_cls.py
- /library/cp_library/ds/heap/skew_heap_forrest_cls.py.html
title: cp_library/ds/heap/skew_heap_forrest_cls.py
---
