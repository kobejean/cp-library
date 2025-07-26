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
    path: cp_library/math/sps/mod/sps_exp_adaptive_fn.py
    title: cp_library/math/sps/mod/sps_exp_adaptive_fn.py
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
    \nfrom typing import Generic\nfrom typing import TypeVar\n_S = TypeVar('S'); _T\
    \ = TypeVar('T'); _U = TypeVar('U'); _T1 = TypeVar('T1'); _T2 = TypeVar('T2');\
    \ _T3 = TypeVar('T3'); _T4 = TypeVar('T4'); _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\
    \n\nimport sys\n\ndef list_find(lst: list, value, start = 0, stop = sys.maxsize):\n\
    \    try:\n        return lst.index(value, start, stop)\n    except:\n       \
    \ return -1\n\n\nclass view(Generic[_T]):\n    __slots__ = 'A', 'l', 'r'\n   \
    \ def __init__(V, A: list[_T], l: int = 0, r: int = 0): V.A, V.l, V.r = A, l,\
    \ r\n    def __len__(V): return V.r - V.l\n    def __getitem__(V, i: int): \n\
    \        if 0 <= i < V.r - V.l: return V.A[V.l+i]\n        else: raise IndexError\n\
    \    def __setitem__(V, i: int, v: _T): V.A[V.l+i] = v\n    def __contains__(V,\
    \ v: _T): return list_find(V.A, v, V.l, V.r) != -1\n    def set_range(V, l: int,\
    \ r: int): V.l, V.r = l, r\n    def index(V, v: _T): return V.A.index(v, V.l,\
    \ V.r) - V.l\n    def reverse(V):\n        l, r = V.l, V.r-1\n        while l\
    \ < r: V.A[l], V.A[r] = V.A[r], V.A[l]; l += 1; r -= 1\n    def sort(V, /, *args,\
    \ **kwargs):\n        A = V.A[V.l:V.r]; A.sort(*args, **kwargs)\n        for i,a\
    \ in enumerate(A,V.l): V.A[i] = a\n    def pop(V): V.r -= 1; return V.A[V.r]\n\
    \    def append(V, v: _T): V.A[V.r] = v; V.r += 1\n    def popleft(V): V.l +=\
    \ 1; return V.A[V.l-1]\n    def appendleft(V, v: _T): V.l -= 1; V.A[V.l] = v;\
    \ \n    def validate(V): return 0 <= V.l <= V.r <= len(V.A)\n\n\n\ndef sps_exp_small(P,\
    \ mod):\n    assert P[0] == 0\n    N = len(P).bit_length() - 1\n    Z = 1<<N\n\
    \    exp = [0]*Z; exp[0] = 1\n    for i in range(1, Z):\n        fg, b, j = 0,\
    \ 1 << (i.bit_length() - 1), i-1&i\n        while b <= j:\n            fg += P[j]\
    \ * exp[i^j] % mod\n            j = j-1&i\n        exp[i] = (P[i] + fg) % mod\n\
    \    return exp\n"
  code: "import cp_library.__header__\nfrom cp_library.ds.view.view_cls import view\n\
    import cp_library.math.__header__\nimport cp_library.math.sps.__header__\n\ndef\
    \ sps_exp_small(P, mod):\n    assert P[0] == 0\n    N = len(P).bit_length() -\
    \ 1\n    Z = 1<<N\n    exp = [0]*Z; exp[0] = 1\n    for i in range(1, Z):\n  \
    \      fg, b, j = 0, 1 << (i.bit_length() - 1), i-1&i\n        while b <= j:\n\
    \            fg += P[j] * exp[i^j] % mod\n            j = j-1&i\n        exp[i]\
    \ = (P[i] + fg) % mod\n    return exp\n"
  dependsOn:
  - cp_library/ds/view/view_cls.py
  - cp_library/ds/list/list_find_fn.py
  isVerificationFile: false
  path: cp_library/math/sps/mod/sps_exp_small_fn.py
  requiredBy:
  - cp_library/math/sps/mod/sps_exp_adaptive_fn.py
  timestamp: '2025-07-26 11:14:31+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/sps/mod/sps_exp_small_fn.py
layout: document
redirect_from:
- /library/cp_library/math/sps/mod/sps_exp_small_fn.py
- /library/cp_library/math/sps/mod/sps_exp_small_fn.py.html
title: cp_library/math/sps/mod/sps_exp_small_fn.py
---
