---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/reserve_fn.py
    title: cp_library/ds/reserve_fn.py
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/math/table/linear_sieve_cls.py
    title: cp_library/math/table/linear_sieve_cls.py
  - icon: ':warning:'
    path: cp_library/math/table/linear_sieve_cnts_cls.py
    title: cp_library/math/table/linear_sieve_cnts_cls.py
  - icon: ':warning:'
    path: cp_library/math/table/sieve_cls.py
    title: cp_library/math/table/sieve_cls.py
  - icon: ':warning:'
    path: cp_library/math/table/sieve_proto.py
    title: cp_library/math/table/sieve_proto.py
  - icon: ':warning:'
    path: cp_library/math/table/totient_cls.py
    title: cp_library/math/table/totient_cls.py
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "import operator\nfrom typing import Callable\n'''\n\u257A\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\n\ndef reserve(A: list, est_len: int) -> None: ...\ntry:\n\
    \    from __pypy__ import resizelist_hint\nexcept:\n    def resizelist_hint(A:\
    \ list, est_len: int):\n        pass\nreserve = resizelist_hint\n\nclass Primes(list[int]):\n\
    \    def __init__(P, N: int):\n        super().__init__()\n        spf = [0] *\
    \ (N + 1)\n        spf[0], spf[1] = 0, 1\n        reserve(P, N)\n\n        for\
    \ i in range(2, N + 1):\n            if spf[i] == 0:\n                spf[i] =\
    \ i\n                P.append(i)\n            for p in P:\n                if\
    \ p > spf[i] or i*p > N: break\n                spf[i*p] = p\n        P.spf =\
    \ spf\n\n    def divisor_zeta(P, A: list[int], op: Callable[[int,int], int] =\
    \ operator.add):\n        N = len(A)\n        for p in P:\n            for i in\
    \ range(1, N//p+1):\n                A[i*p] = op(A[i], A[i*p])\n        return\
    \ A\n    \n    def divisor_mobius(P, A: list[int], diff: Callable[[int,int], int]\
    \ = operator.sub):\n        N = len(A)\n        for p in P:\n            for i\
    \ in range(N//p, 0, -1):\n                A[i*p] = diff(A[i*p], A[i])\n      \
    \  return A\n    \n    def multiple_zeta(P, A: list[int], op: Callable[[int,int],\
    \ int] = operator.add):\n        N = len(A)\n        for p in P:\n           \
    \ for i in range(N//p, 0, -1):\n                A[i] = op(A[i*p], A[i])\n    \
    \    return A\n    \n    def multiple_mobius(P, A: list[int], diff: Callable[[int,int],\
    \ int] = operator.sub):\n        N = len(A)\n        for p in P:\n           \
    \ for i in range(1, N//p+1):\n                A[i] = diff(A[i], A[i*p])\n    \
    \    return A\n\n"
  code: "import operator\nfrom typing import Callable\nimport cp_library.math.table.__header__\n\
    from cp_library.ds.reserve_fn import reserve\n\nclass Primes(list[int]):\n   \
    \ def __init__(P, N: int):\n        super().__init__()\n        spf = [0] * (N\
    \ + 1)\n        spf[0], spf[1] = 0, 1\n        reserve(P, N)\n\n        for i\
    \ in range(2, N + 1):\n            if spf[i] == 0:\n                spf[i] = i\n\
    \                P.append(i)\n            for p in P:\n                if p >\
    \ spf[i] or i*p > N: break\n                spf[i*p] = p\n        P.spf = spf\n\
    \n    def divisor_zeta(P, A: list[int], op: Callable[[int,int], int] = operator.add):\n\
    \        N = len(A)\n        for p in P:\n            for i in range(1, N//p+1):\n\
    \                A[i*p] = op(A[i], A[i*p])\n        return A\n    \n    def divisor_mobius(P,\
    \ A: list[int], diff: Callable[[int,int], int] = operator.sub):\n        N = len(A)\n\
    \        for p in P:\n            for i in range(N//p, 0, -1):\n             \
    \   A[i*p] = diff(A[i*p], A[i])\n        return A\n    \n    def multiple_zeta(P,\
    \ A: list[int], op: Callable[[int,int], int] = operator.add):\n        N = len(A)\n\
    \        for p in P:\n            for i in range(N//p, 0, -1):\n             \
    \   A[i] = op(A[i*p], A[i])\n        return A\n    \n    def multiple_mobius(P,\
    \ A: list[int], diff: Callable[[int,int], int] = operator.sub):\n        N = len(A)\n\
    \        for p in P:\n            for i in range(1, N//p+1):\n               \
    \ A[i] = diff(A[i], A[i*p])\n        return A\n\n"
  dependsOn:
  - cp_library/ds/reserve_fn.py
  isVerificationFile: false
  path: cp_library/math/table/primes_cls.py
  requiredBy:
  - cp_library/math/table/sieve_cls.py
  - cp_library/math/table/totient_cls.py
  - cp_library/math/table/linear_sieve_cnts_cls.py
  - cp_library/math/table/linear_sieve_cls.py
  - cp_library/math/table/sieve_proto.py
  timestamp: '2025-02-18 02:22:25+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/table/primes_cls.py
layout: document
redirect_from:
- /library/cp_library/math/table/primes_cls.py
- /library/cp_library/math/table/primes_cls.py.html
title: cp_library/math/table/primes_cls.py
---
