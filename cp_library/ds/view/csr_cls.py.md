---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/list_find_fn.py
    title: cp_library/ds/list/list_find_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/view/view_cls.py
    title: cp_library/ds/view/view_cls.py
  _extendedRequiredBy:
  - icon: ':warning:'
    path: perf/csr.py
    title: perf/csr.py
  - icon: ':warning:'
    path: perf/heap_csr.py
    title: perf/heap_csr.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/view/csr_cls_test.py
    title: test/unittests/ds/view/csr_cls_test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2578\n             https://kobejean.github.io/cp-library             \
    \  \n'''\nfrom typing import Generic\nfrom typing import TypeVar\n_S = TypeVar('S');\
    \ _T = TypeVar('T'); _U = TypeVar('U'); _T1 = TypeVar('T1'); _T2 = TypeVar('T2');\
    \ _T3 = TypeVar('T3'); _T4 = TypeVar('T4'); _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\
    \n\n\n\nimport sys\n\ndef list_find(lst: list, value, start = 0, stop = sys.maxsize):\n\
    \    try:\n        return lst.index(value, start, stop)\n    except:\n       \
    \ return -1\n\nclass view(Generic[_T]):\n    __slots__ = 'A', 'l', 'r'\n    def\
    \ __init__(V, A: list[_T], l: int = 0, r: int = 0): V.A, V.l, V.r = A, l, r\n\
    \    def __len__(V): return V.r - V.l\n    def __getitem__(V, i: int): \n    \
    \    if 0 <= i < V.r - V.l: return V.A[V.l+i]\n        else: raise IndexError\n\
    \    def __setitem__(V, i: int, v: _T): V.A[V.l+i] = v\n    def __contains__(V,\
    \ v: _T): return list_find(V.A, v, V.l, V.r) != -1\n    def set_range(V, l: int,\
    \ r: int): V.l, V.r = l, r\n    def index(V, v: _T): return V.A.index(v, V.l,\
    \ V.r) - V.l\n    def reverse(V):\n        l, r = V.l, V.r-1\n        while l\
    \ < r: V.A[l], V.A[r] = V.A[r], V.A[l]; l += 1; r -= 1\n    def sort(V, /, *args,\
    \ **kwargs):\n        A = V.A[V.l:V.r]; A.sort(*args, **kwargs)\n        for i,a\
    \ in enumerate(A,V.l): V.A[i] = a\n    def pop(V): V.r -= 1; return V.A[V.r]\n\
    \    def append(V, v: _T): V.A[V.r] = v; V.r += 1\n    def popleft(V): V.l +=\
    \ 1; return V.A[V.l-1]\n    def appendleft(V, v: _T): V.l -= 1; V.A[V.l] = v;\
    \ \n    def validate(V): return 0 <= V.l <= V.r <= len(V.A)\n\nclass CSR(Generic[_T]):\n\
    \    __slots__ = 'A', 'O'\n    def __init__(csr, A: list[_T], O: list[int]): csr.A,\
    \ csr.O = A, O\n    def __len__(csr): return len(csr.O)-1\n    def __getitem__(csr,\
    \ i: int): return view(csr.A, csr.O[i], csr.O[i+1])\n    def __call__(csr, i:\
    \ int, j: int): return csr.A[csr.O[i]+j]\n    def set(csr, i: int, j: int, v:\
    \ _T): csr.A[csr.O[i]+j] = v\n    @classmethod\n    def bucketize(cls, N: int,\
    \ K: list[int], V: list[_T]):\n        A: list[_T] = [0]*len(K); O = [0]*(N+1)\n\
    \        for k in K: O[k] += 1\n        for i in range(N): O[i+1] += O[i]\n  \
    \      for e in range(len(K)): k = K[~e]; O[k] -= 1; A[O[k]] = V[~e]\n       \
    \ return cls(A, O)\n"
  code: "\nimport cp_library.__header__\nfrom typing import Generic\nfrom cp_library.misc.typing\
    \ import _T\nimport cp_library.ds.__header__\nimport cp_library.ds.view.__header__\n\
    from cp_library.ds.view.view_cls import view\n\nclass CSR(Generic[_T]):\n    __slots__\
    \ = 'A', 'O'\n    def __init__(csr, A: list[_T], O: list[int]): csr.A, csr.O =\
    \ A, O\n    def __len__(csr): return len(csr.O)-1\n    def __getitem__(csr, i:\
    \ int): return view(csr.A, csr.O[i], csr.O[i+1])\n    def __call__(csr, i: int,\
    \ j: int): return csr.A[csr.O[i]+j]\n    def set(csr, i: int, j: int, v: _T):\
    \ csr.A[csr.O[i]+j] = v\n    @classmethod\n    def bucketize(cls, N: int, K: list[int],\
    \ V: list[_T]):\n        A: list[_T] = [0]*len(K); O = [0]*(N+1)\n        for\
    \ k in K: O[k] += 1\n        for i in range(N): O[i+1] += O[i]\n        for e\
    \ in range(len(K)): k = K[~e]; O[k] -= 1; A[O[k]] = V[~e]\n        return cls(A,\
    \ O)"
  dependsOn:
  - cp_library/ds/view/view_cls.py
  - cp_library/ds/list/list_find_fn.py
  isVerificationFile: false
  path: cp_library/ds/view/csr_cls.py
  requiredBy:
  - perf/csr.py
  - perf/heap_csr.py
  timestamp: '2025-07-28 14:17:34+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/unittests/ds/view/csr_cls_test.py
documentation_of: cp_library/ds/view/csr_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/view/csr_cls.py
- /library/cp_library/ds/view/csr_cls.py.html
title: cp_library/ds/view/csr_cls.py
---
