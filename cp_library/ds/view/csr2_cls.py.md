---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/arg/argsort_ranged_fn.py
    title: cp_library/alg/iter/arg/argsort_ranged_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/sort/isort_ranged_fn.py
    title: cp_library/alg/iter/sort/isort_ranged_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer_cls.py
    title: cp_library/bit/pack/packer_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/view/view2_cls.py
    title: cp_library/ds/view/view2_cls.py
  _extendedRequiredBy:
  - icon: ':warning:'
    path: perf/csr2.py
    title: perf/csr2.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/view/csr2_cls_test.py
    title: test/unittests/ds/view/csr2_cls_test.py
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
    \  \n'''\nfrom typing import Generic\nfrom typing import TypeVar\n_S = TypeVar('S')\n\
    _T = TypeVar('T')\n_U = TypeVar('U')\n_T1 = TypeVar('T1')\n_T2 = TypeVar('T2')\n\
    _T3 = TypeVar('T3')\n_T4 = TypeVar('T4')\n_T5 = TypeVar('T5')\n_T6 = TypeVar('T6')\n\
    \n\n\n\n\n\n\ndef argsort_ranged(A: list[int], l: int, r: int, reverse=False):\n\
    \    P = Packer(r-l-1); I = [A[l+i] for i in range(r-l)]; P.ienumerate(I, reverse);\
    \ I.sort()\n    for i in range(r-l): I[i] = (I[i] & P.m) + l\n    return I\n\n\
    \n\nclass Packer:\n    __slots__ = 's', 'm'\n    def __init__(P, mx: int): P.s\
    \ = mx.bit_length(); P.m = (1 << P.s) - 1\n    def enc(P, a: int, b: int): return\
    \ a << P.s | b\n    def dec(P, x: int) -> tuple[int, int]: return x >> P.s, x\
    \ & P.m\n    def enumerate(P, A, reverse=False): P.ienumerate(A:=list(A), reverse);\
    \ return A\n    def ienumerate(P, A, reverse=False):\n        if reverse:\n  \
    \          for i,a in enumerate(A): A[i] = P.enc(-a, i)\n        else:\n     \
    \       for i,a in enumerate(A): A[i] = P.enc(a, i)\n    def indices(P, A: list[int]):\
    \ P.iindices(A:=list(A)); return A\n    def iindices(P, A):\n        for i,a in\
    \ enumerate(A): A[i] = P.m&a\n\n\ndef isort_ranged(*L: list, l: int, r: int, reverse=False):\n\
    \    n = r - l\n    order = argsort_ranged(L[0], l, r, reverse=reverse)\n    inv\
    \ = [0] * n\n    # order contains indices in range [l, r), need to map to [0,\
    \ n)\n    for i in range(n): inv[order[i]-l] = i\n    for i in range(n):\n   \
    \     j = order[i] - l  # j is in range [0, n)\n        for A in L: A[l+i], A[l+j]\
    \ = A[l+j], A[l+i]\n        order[inv[i]], order[inv[j]] = order[inv[j]], order[inv[i]]\n\
    \        inv[i], inv[j] = inv[j], inv[i]\n    return L\n\nclass view2(Generic[_S,\
    \ _T]):\n    __slots__ = 'A', 'B', 'l', 'r'\n    def __init__(V, A: list[_S],\
    \ B: list[_T], l: int, r: int): V.A, V.B, V.l, V.r = A, B, l, r\n    def __len__(V):\
    \ return V.r - V.l\n    def __getitem__(V, i: int): \n        if 0 <= i < V.r\
    \ - V.l: return V.A[V.l+i], V.B[V.l+i]\n        else: raise IndexError\n    def\
    \ __setitem__(V, i: int, v: tuple[_S, _T]): V.A[V.l+i], V.B[V.l+i] = v\n    def\
    \ __contains__(V, v: tuple[_S, _T]): raise NotImplemented\n    def set_range(V,\
    \ l: int, r: int): V.l, V.r = l, r\n    def index(V, v: tuple[_S, _T]): raise\
    \ NotImplemented\n    def reverse(V):\n        l, r = V.l, V.r-1\n        while\
    \ l < r: V.A[l], V.A[r] = V.A[r], V.A[l]; V.B[l], V.B[r] = V.B[r], V.B[l]; l +=\
    \ 1; r -= 1\n    def sort(V, reverse=False): isort_ranged(V.A, V.B, l=V.l, r=V.r,\
    \ reverse=reverse)\n    def pop(V): V.r -= 1; return V.A[V.r], V.B[V.r]\n    def\
    \ append(V, v: tuple[_S, _T]): V.A[V.r], V.B[V.r] = v; V.r += 1\n    def popleft(V):\
    \ V.l += 1; return V.A[V.l-1], V.B[V.l-1]\n    def appendleft(V, v: tuple[_S,\
    \ _T]): V.l -= 1; V.A[V.l], V.B[V.l]  = v; \n    def validate(V): return 0 <=\
    \ V.l <= V.r <= len(V.A)\n\nclass CSR2(Generic[_T]):\n    __slots__ = 'A', 'B',\
    \ 'O'\n    def __init__(csr, A: list[_S], B: list[_T], O: list[int]): csr.A, csr.B,\
    \ csr.O = A, B, O\n    def __len__(csr): return len(csr.O)-1\n    def __getitem__(csr,\
    \ i: int): return view2(csr.A, csr.B, csr.O[i], csr.O[i+1])\n    def __call__(csr,\
    \ i: int, j: int): ij = csr.O[i]+j; return csr.A[ij], csr.B[ij]\n    def set(csr,\
    \ i: int, j: int, v: _T): ij = csr.O[i]+j; csr.A[ij], csr.B[ij] = v\n    @classmethod\n\
    \    def bucketize(cls, N: int, K: list[int], V: list[_T], W: list[_T]):\n   \
    \     A: list[_S] = [0]*len(K); B: list[_T] = [0]*len(K); O = [0]*(N+1)\n    \
    \    for k in K: O[k] += 1\n        for i in range(N): O[i+1] += O[i]\n      \
    \  for e in range(len(K)): k = K[~e]; O[k] -= 1; A[O[k]] = V[~e]; B[O[k]] = W[~e]\n\
    \        return cls(A, B, O)\n"
  code: "\nimport cp_library.__header__\nfrom typing import Generic\nfrom cp_library.misc.typing\
    \ import _S, _T\nimport cp_library.ds.__header__\nimport cp_library.ds.view.__header__\n\
    from cp_library.ds.view.view2_cls import view2\n\nclass CSR2(Generic[_T]):\n \
    \   __slots__ = 'A', 'B', 'O'\n    def __init__(csr, A: list[_S], B: list[_T],\
    \ O: list[int]): csr.A, csr.B, csr.O = A, B, O\n    def __len__(csr): return len(csr.O)-1\n\
    \    def __getitem__(csr, i: int): return view2(csr.A, csr.B, csr.O[i], csr.O[i+1])\n\
    \    def __call__(csr, i: int, j: int): ij = csr.O[i]+j; return csr.A[ij], csr.B[ij]\n\
    \    def set(csr, i: int, j: int, v: _T): ij = csr.O[i]+j; csr.A[ij], csr.B[ij]\
    \ = v\n    @classmethod\n    def bucketize(cls, N: int, K: list[int], V: list[_T],\
    \ W: list[_T]):\n        A: list[_S] = [0]*len(K); B: list[_T] = [0]*len(K); O\
    \ = [0]*(N+1)\n        for k in K: O[k] += 1\n        for i in range(N): O[i+1]\
    \ += O[i]\n        for e in range(len(K)): k = K[~e]; O[k] -= 1; A[O[k]] = V[~e];\
    \ B[O[k]] = W[~e]\n        return cls(A, B, O)"
  dependsOn:
  - cp_library/ds/view/view2_cls.py
  - cp_library/alg/iter/sort/isort_ranged_fn.py
  - cp_library/alg/iter/arg/argsort_ranged_fn.py
  - cp_library/bit/pack/packer_cls.py
  isVerificationFile: false
  path: cp_library/ds/view/csr2_cls.py
  requiredBy:
  - perf/csr2.py
  timestamp: '2025-07-20 06:26:01+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/unittests/ds/view/csr2_cls_test.py
documentation_of: cp_library/ds/view/csr2_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/view/csr2_cls.py
- /library/cp_library/ds/view/csr2_cls.py.html
title: cp_library/ds/view/csr2_cls.py
---
