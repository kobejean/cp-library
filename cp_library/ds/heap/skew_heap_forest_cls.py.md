---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/graph/directedmst.test.py
    title: test/library-checker/graph/directedmst.test.py
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
    \ndef elist(est_len: int) -> list: ...\ntry:\n    from __pypy__ import newlist_hint\n\
    except:\n    def newlist_hint(hint):\n        return []\nelist = newlist_hint\n\
    \    \nfrom typing import Generic\nfrom typing import TypeVar\n_T = TypeVar('T')\n\
    \nclass SkewHeapForest(Generic[_T]):\n    def __init__(shf, N, M, e: _T = 0):\n\
    \        shf.V, shf.A, shf.L, shf.R, shf.roots = [e]*M, [e]*M, [-1]*M, [-1]*M,\
    \ [-1]*N\n        shf.id, shf.st = 0, elist(M)\n    \n    def propagate(shf, u:\
    \ int):\n        if (add := shf.A[u]):\n            if (l := shf.L[u]) != -1:\
    \ shf.A[l] += add\n            if (r := shf.R[u]) != -1: shf.A[r] += add\n   \
    \         shf.V[u] += add\n            shf.A[u] = 0\n\n    def merge(shf, u: int,\
    \ v: int):\n        st, V, A, L, R = shf.st, shf.V, shf.A, shf.L, shf.R\n    \
    \    while u >= 0 and v >= 0:\n            if V[v]+A[v] < V[u]+A[u]: u, v = v,\
    \ u\n            shf.propagate(u)\n            st.append(u)\n            R[u],\
    \ u = L[u], R[u]\n        u = v if u == -1 else u\n        while st: L[u := st.pop()]\
    \ = u\n        return u\n    \n    def min(shf, i: int):\n        assert (root\
    \ := shf.roots[i]) >= 0\n        shf.propagate(root)\n        return shf.V[root]\n\
    \n    def push(shf, i: int, x: _T):\n        shf.id = (id := shf.id)+1\n     \
    \   shf.V[id] = x\n        shf.roots[i] = shf.merge(shf.roots[i], id)\n\n    def\
    \ pop(shf, i: int) -> _T:\n        assert (root := shf.roots[i]) >= 0\n      \
    \  shf.propagate(root := shf.roots[i])\n        val = shf.V[root]\n        shf.roots[i]\
    \ = shf.merge(shf.L[root], shf.R[root])\n        return val\n    \n    def add(shf,\
    \ i: int, val: _T): shf.A[shf.roots[i]] += val\n    def empty(shf, i: int): return\
    \ shf.roots[i] == -1\n    \n"
  code: "import cp_library.ds.heap.__header__\nfrom cp_library.ds.elist_fn import\
    \ elist\nfrom typing import Generic\nfrom cp_library.misc.typing import _T\n\n\
    class SkewHeapForest(Generic[_T]):\n    def __init__(shf, N, M, e: _T = 0):\n\
    \        shf.V, shf.A, shf.L, shf.R, shf.roots = [e]*M, [e]*M, [-1]*M, [-1]*M,\
    \ [-1]*N\n        shf.id, shf.st = 0, elist(M)\n    \n    def propagate(shf, u:\
    \ int):\n        if (add := shf.A[u]):\n            if (l := shf.L[u]) != -1:\
    \ shf.A[l] += add\n            if (r := shf.R[u]) != -1: shf.A[r] += add\n   \
    \         shf.V[u] += add\n            shf.A[u] = 0\n\n    def merge(shf, u: int,\
    \ v: int):\n        st, V, A, L, R = shf.st, shf.V, shf.A, shf.L, shf.R\n    \
    \    while u >= 0 and v >= 0:\n            if V[v]+A[v] < V[u]+A[u]: u, v = v,\
    \ u\n            shf.propagate(u)\n            st.append(u)\n            R[u],\
    \ u = L[u], R[u]\n        u = v if u == -1 else u\n        while st: L[u := st.pop()]\
    \ = u\n        return u\n    \n    def min(shf, i: int):\n        assert (root\
    \ := shf.roots[i]) >= 0\n        shf.propagate(root)\n        return shf.V[root]\n\
    \n    def push(shf, i: int, x: _T):\n        shf.id = (id := shf.id)+1\n     \
    \   shf.V[id] = x\n        shf.roots[i] = shf.merge(shf.roots[i], id)\n\n    def\
    \ pop(shf, i: int) -> _T:\n        assert (root := shf.roots[i]) >= 0\n      \
    \  shf.propagate(root := shf.roots[i])\n        val = shf.V[root]\n        shf.roots[i]\
    \ = shf.merge(shf.L[root], shf.R[root])\n        return val\n    \n    def add(shf,\
    \ i: int, val: _T): shf.A[shf.roots[i]] += val\n    def empty(shf, i: int): return\
    \ shf.roots[i] == -1\n    "
  dependsOn:
  - cp_library/ds/elist_fn.py
  isVerificationFile: false
  path: cp_library/ds/heap/skew_heap_forest_cls.py
  requiredBy: []
  timestamp: '2025-02-12 22:25:56+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/graph/directedmst.test.py
documentation_of: cp_library/ds/heap/skew_heap_forest_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/heap/skew_heap_forest_cls.py
- /library/cp_library/ds/heap/skew_heap_forest_cls.py.html
title: cp_library/ds/heap/skew_heap_forest_cls.py
---
