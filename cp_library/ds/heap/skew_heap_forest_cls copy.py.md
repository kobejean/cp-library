---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
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
    \ndef elist(est_len: int) -> list: ...\ntry:\n    from __pypy__ import newlist_hint\n\
    except:\n    def newlist_hint(hint):\n        return []\nelist = newlist_hint\n\
    \    \nfrom typing import Container, Generic, Optional\nfrom typing import TypeVar\n\
    _T = TypeVar('T')\ni32max = (1 << 31)-1\n\nclass SkewHeapForest(Generic[_T]):\n\
    \    def __init__(shf, N, M, e: _T = 0):\n        shf.V, shf.A, shf.C = [e]*M,\
    \ [e]*M, [i32max<<31|i32max]*M\n        shf.roots = [i32max]*N\n        shf.id\
    \ = 0\n        shf.st = elist(M)\n    \n    def propagate(shf, u: int):\n    \
    \    if (add := shf.A[u]):\n            l, r = shf.C[u] >> 31, shf.C[u] & i32max\n\
    \            if l < i32max: shf.A[l] += add\n            if r < i32max: shf.A[r]\
    \ += add\n            shf.V[u] += add\n            shf.A[u] = 0\n\n    def merge(shf,\
    \ u: int, v: int):\n        st, V, A, C = shf.st, shf.V, shf.A, shf.C\n      \
    \  while u < i32max and v < i32max:\n            if V[v]+A[v] < V[u]+A[u]: u,\
    \ v = v, u\n            shf.propagate(u)\n            st.append(u)\n         \
    \   C[u], u = C[u] >> 31, C[u] & i32max\n        u = v if u == i32max else u\n\
    \        while st: C[u := st.pop()] |= u << 31\n        return u\n    \n    def\
    \ min(shf, i: int):\n        assert (root := shf.roots[i]) < i32max\n        shf.propagate(root)\n\
    \        return shf.V[root]\n\n    def push(shf, i: int, x: _T):\n        shf.id\
    \ = (id := shf.id)+1\n        shf.V[id] = x\n        shf.roots[i] = shf.merge(shf.roots[i],\
    \ id)\n\n    def pop(shf, i: int) -> _T:\n        assert (root := shf.roots[i])\
    \ < i32max\n        shf.propagate(root)\n        val = shf.V[root]\n        shf.roots[i]\
    \ = shf.merge(shf.C[root] >> 31, shf.C[root] & i32max)\n        return val\n \
    \   \n    def add(shf, i: int, val: _T):\n        shf.A[shf.roots[i]] += val\n\
    \n    def empty(shf, i: int):\n        return shf.roots[i] == i32max\n    \n"
  code: "import cp_library.ds.heap.__header__\nfrom cp_library.ds.elist_fn import\
    \ elist\nfrom typing import Container, Generic, Optional\nfrom cp_library.misc.typing\
    \ import _T\ni32max = (1 << 31)-1\n\nclass SkewHeapForest(Generic[_T]):\n    def\
    \ __init__(shf, N, M, e: _T = 0):\n        shf.V, shf.A, shf.C = [e]*M, [e]*M,\
    \ [i32max<<31|i32max]*M\n        shf.roots = [i32max]*N\n        shf.id = 0\n\
    \        shf.st = elist(M)\n    \n    def propagate(shf, u: int):\n        if\
    \ (add := shf.A[u]):\n            l, r = shf.C[u] >> 31, shf.C[u] & i32max\n \
    \           if l < i32max: shf.A[l] += add\n            if r < i32max: shf.A[r]\
    \ += add\n            shf.V[u] += add\n            shf.A[u] = 0\n\n    def merge(shf,\
    \ u: int, v: int):\n        st, V, A, C = shf.st, shf.V, shf.A, shf.C\n      \
    \  while u < i32max and v < i32max:\n            if V[v]+A[v] < V[u]+A[u]: u,\
    \ v = v, u\n            shf.propagate(u)\n            st.append(u)\n         \
    \   C[u], u = C[u] >> 31, C[u] & i32max\n        u = v if u == i32max else u\n\
    \        while st: C[u := st.pop()] |= u << 31\n        return u\n    \n    def\
    \ min(shf, i: int):\n        assert (root := shf.roots[i]) < i32max\n        shf.propagate(root)\n\
    \        return shf.V[root]\n\n    def push(shf, i: int, x: _T):\n        shf.id\
    \ = (id := shf.id)+1\n        shf.V[id] = x\n        shf.roots[i] = shf.merge(shf.roots[i],\
    \ id)\n\n    def pop(shf, i: int) -> _T:\n        assert (root := shf.roots[i])\
    \ < i32max\n        shf.propagate(root)\n        val = shf.V[root]\n        shf.roots[i]\
    \ = shf.merge(shf.C[root] >> 31, shf.C[root] & i32max)\n        return val\n \
    \   \n    def add(shf, i: int, val: _T):\n        shf.A[shf.roots[i]] += val\n\
    \n    def empty(shf, i: int):\n        return shf.roots[i] == i32max\n    "
  dependsOn:
  - cp_library/ds/elist_fn.py
  isVerificationFile: false
  path: cp_library/ds/heap/skew_heap_forest_cls copy.py
  requiredBy: []
  timestamp: '2025-03-09 09:15:44+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/heap/skew_heap_forest_cls copy.py
layout: document
redirect_from:
- /library/cp_library/ds/heap/skew_heap_forest_cls copy.py
- /library/cp_library/ds/heap/skew_heap_forest_cls copy.py.html
title: cp_library/ds/heap/skew_heap_forest_cls copy.py
---
