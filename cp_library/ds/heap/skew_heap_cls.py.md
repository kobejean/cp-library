---
data:
  _extendedDependsOn: []
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
    import operator\nfrom typing import Generic, TypeVar\n_S = TypeVar('S'); _T =\
    \ TypeVar('T'); _U = TypeVar('U'); _T1 = TypeVar('T1'); _T2 = TypeVar('T2'); _T3\
    \ = TypeVar('T3'); _T4 = TypeVar('T4'); _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\
    \n\n_TSkewHeap = TypeVar(\"SkewHeap\", bound=\"SkewHeap\")\nclass SkewHeap(Generic[_T]):\n\
    \    __slots__ = 'root', 'op', 'e'\n    V, A, L, R, st = [-1], [-1], [-1], [-1],\
    \ []\n    def __init__(H, op = operator.add, e: _T = 0):\n        H.root, H.op,\
    \ H.e = -1, op, e\n    \n    def merge(H: _TSkewHeap, O: _TSkewHeap):\n      \
    \  H.root = H.merge_nodes(H.root, O.root)\n        O.root = -1\n\n    def min(H):\n\
    \        assert ~H.root\n        H.propagate(H.root)\n        return H.V[H.root]\n\
    \n    def push(H, x: _T):\n        id = len(H.V)\n        H.V.append(x); H.A.append(H.e);\
    \ H.L.append(-1); H.R.append(-1)\n        H.root = H.merge_nodes(H.root, id)\n\
    \n    def pop(H) -> _T:\n        assert ~H.root\n        H.propagate(H.root)\n\
    \        val, H.root = H.V[H.root], H.merge_nodes(H.L[H.root], H.R[H.root])\n\
    \        return val\n    \n    def add(H, val: _T): H.A[H.root] = H.op(H.A[H.root],\
    \ val)\n    def empty(H): return H.root == -1\n    def __bool__(H): return H.root\
    \ != -1\n    \n    def propagate(H, u: int):\n        if (a := H.A[u]) != H.e:\n\
    \            if ~(l := H.L[u]): H.A[l] = H.op(H.A[l], a)\n            if ~(r :=\
    \ H.R[u]): H.A[r] = H.op(H.A[r], a)\n            H.V[u] = H.op(H.V[u], a); H.A[u]\
    \ = H.e\n\n    def merge_nodes(H, u: int, v:int):\n        while ~u and ~v:\n\
    \            H.propagate(u); H.propagate(v)\n            if H.V[v] < H.V[u]: u,\
    \ v = v, u\n            H.st.append(u); H.R[u], u = H.L[u], H.R[u]\n        u\
    \ = u if ~u else v\n        while H.st: H.L[u := H.st.pop()] = u\n        return\
    \ u\n"
  code: "import cp_library.__header__\nimport operator\nfrom typing import Generic,\
    \ TypeVar\nfrom cp_library.misc.typing import _T\nimport cp_library.ds.__header__\n\
    import cp_library.ds.heap.__header__\n_TSkewHeap = TypeVar(\"SkewHeap\", bound=\"\
    SkewHeap\")\nclass SkewHeap(Generic[_T]):\n    __slots__ = 'root', 'op', 'e'\n\
    \    V, A, L, R, st = [-1], [-1], [-1], [-1], []\n    def __init__(H, op = operator.add,\
    \ e: _T = 0):\n        H.root, H.op, H.e = -1, op, e\n    \n    def merge(H: _TSkewHeap,\
    \ O: _TSkewHeap):\n        H.root = H.merge_nodes(H.root, O.root)\n        O.root\
    \ = -1\n\n    def min(H):\n        assert ~H.root\n        H.propagate(H.root)\n\
    \        return H.V[H.root]\n\n    def push(H, x: _T):\n        id = len(H.V)\n\
    \        H.V.append(x); H.A.append(H.e); H.L.append(-1); H.R.append(-1)\n    \
    \    H.root = H.merge_nodes(H.root, id)\n\n    def pop(H) -> _T:\n        assert\
    \ ~H.root\n        H.propagate(H.root)\n        val, H.root = H.V[H.root], H.merge_nodes(H.L[H.root],\
    \ H.R[H.root])\n        return val\n    \n    def add(H, val: _T): H.A[H.root]\
    \ = H.op(H.A[H.root], val)\n    def empty(H): return H.root == -1\n    def __bool__(H):\
    \ return H.root != -1\n    \n    def propagate(H, u: int):\n        if (a := H.A[u])\
    \ != H.e:\n            if ~(l := H.L[u]): H.A[l] = H.op(H.A[l], a)\n         \
    \   if ~(r := H.R[u]): H.A[r] = H.op(H.A[r], a)\n            H.V[u] = H.op(H.V[u],\
    \ a); H.A[u] = H.e\n\n    def merge_nodes(H, u: int, v:int):\n        while ~u\
    \ and ~v:\n            H.propagate(u); H.propagate(v)\n            if H.V[v] <\
    \ H.V[u]: u, v = v, u\n            H.st.append(u); H.R[u], u = H.L[u], H.R[u]\n\
    \        u = u if ~u else v\n        while H.st: H.L[u := H.st.pop()] = u\n  \
    \      return u"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/heap/skew_heap_cls.py
  requiredBy: []
  timestamp: '2025-07-28 14:17:34+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/graph/directedmst.test.py
documentation_of: cp_library/ds/heap/skew_heap_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/heap/skew_heap_cls.py
- /library/cp_library/ds/heap/skew_heap_cls.py.html
title: cp_library/ds/heap/skew_heap_cls.py
---
