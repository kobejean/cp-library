---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/reserve_fn.py
    title: cp_library/ds/reserve_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/table/primes_cls.py
    title: cp_library/math/table/primes_cls.py
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
    import operator\nfrom typing import Callable\nfrom typing import TypeVar\n_T =\
    \ TypeVar('T')\n_U = TypeVar('U')\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2578\n    x\u2080 \u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25CF\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u25BA X\u2080\n                \u2573         \
    \ \u2572 \u2571          \u2572     \u2571          \n    x\u2084 \u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u2572\u2500\u2500\u2500\u2571\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2081\n             \
    \              \u2573 \u2573          \u2572 \u2572 \u2571 \u2571          \n\
    \    x\u2082 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2572\u2500\u2573\
    \u2500\u2571\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA\
    \ X\u2082\n                \u2573          \u2571 \u2572          \u2572 \u2573\
    \ \u2573 \u2571          \n    x\u2086 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u2573\u2500\u2573\u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u25BA X\u2083\n                                        \u2573\
    \ \u2573 \u2573 \u2573         \n    x\u2081 \u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25CF\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25CF\u2500\u2573\u2500\u2573\u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25BA X\u2084\n                \u2573          \u2572\
    \ \u2571          \u2571 \u2573 \u2573 \u2572          \n    x\u2085 \u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u2571\u2500\u2573\u2500\u2572\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2085\n             \
    \              \u2573 \u2573          \u2571 \u2571 \u2572 \u2572          \n\
    \    x\u2083 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2571\u2500\u2500\
    \u2500\u2572\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA\
    \ X\u2086\n                \u2573          \u2571 \u2572          \u2571     \u2572\
    \          \n    x\u2087 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25BA X\u2087\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2578\n                      Math - Convolution                     \n\
    '''\n\ndef gcd_conv(A: list[_T], B: list[_T], N: int,\n            mul: Callable[[_T,_T],_T]\
    \ = operator.mul,\n            sub: Callable[[_T,_T],_T] = operator.sub,\n   \
    \         add: Callable[[_T,_T],_T] = operator.add) -> list[_T]:\n    return Primes(N).gcd_conv(A,\
    \ B, add, sub, mul)\n\n\n\n\ndef reserve(A: list, est_len: int) -> None: ...\n\
    try:\n    from __pypy__ import resizelist_hint\nexcept:\n    def resizelist_hint(A:\
    \ list, est_len: int):\n        pass\nreserve = resizelist_hint\n\nclass Primes(list[int]):\n\
    \    def __init__(P, N: int):\n        super().__init__()\n        spf = [0] *\
    \ (N + 1)\n        spf[0], spf[1] = 0, 1\n        reserve(P, N)\n\n        for\
    \ i in range(2, N + 1):\n            if spf[i] == 0:\n                spf[i] =\
    \ i\n                P.append(i)\n            for p in P:\n                if\
    \ p > spf[i] or i*p > N: break\n                spf[i*p] = p\n        P.spf =\
    \ spf\n\n    def divisor_zeta(P, A: list[int], op: Callable[[int,int], int] =\
    \ operator.add) -> list[int]:\n        N = len(A)-1\n        for p in P:\n   \
    \         for i in range(1, N//p+1): A[i*p] = op(A[i*p], A[i])\n        return\
    \ A\n    \n    def divisor_mobius(P, A: list[int], diff: Callable[[int,int], int]\
    \ = operator.sub) -> list[int]:\n        N = len(A)-1\n        for p in P:\n \
    \           for i in range(N//p, 0, -1): A[i*p] = diff(A[i*p], A[i])\n       \
    \ return A\n    \n    def multiple_zeta(P, A: list[int], op: Callable[[int,int],\
    \ int] = operator.add) -> list[int]:\n        N = len(A)-1\n        for p in P:\n\
    \            for i in range(N//p, 0, -1): A[i] = op(A[i], A[i*p])\n        return\
    \ A\n    \n    def multiple_mobius(P, A: list[int], diff: Callable[[int,int],\
    \ int] = operator.sub) -> list[int]:\n        N = len(A)-1\n        for p in P:\n\
    \            for i in range(1, N//p+1): A[i] = diff(A[i], A[i*p])\n        return\
    \ A\n    \n    def gcd_conv(P, A: list[int], B: list[int], add = operator.add,\
    \ sub = operator.sub, mul = operator.mul):\n        A, B = P.multiple_zeta(A,\
    \ add), P.multiple_zeta(B, add)\n        for i, b in enumerate(B): A[i] = mul(A[i],\
    \ b)\n        return P.multiple_mobius(A, sub)\n    \n    def lcm_conv(P, A: list[int],\
    \ B: list[int], add = operator.add, sub = operator.sub, mul = operator.mul):\n\
    \        A, B = P.divisor_zeta(A, add), P.divisor_zeta(B, add)\n        for i,\
    \ b in enumerate(B): A[i] = mul(A[i], b)\n        return P.divisor_mobius(A, sub)\n"
  code: "import cp_library.__header__\nimport operator\nfrom typing import Callable\n\
    from cp_library.misc.typing import _T\nimport cp_library.math.__header__\nimport\
    \ cp_library.math.conv.__header__\n\ndef gcd_conv(A: list[_T], B: list[_T], N:\
    \ int,\n            mul: Callable[[_T,_T],_T] = operator.mul,\n            sub:\
    \ Callable[[_T,_T],_T] = operator.sub,\n            add: Callable[[_T,_T],_T]\
    \ = operator.add) -> list[_T]:\n    return Primes(N).gcd_conv(A, B, add, sub,\
    \ mul)\n\nfrom cp_library.math.table.primes_cls import Primes"
  dependsOn:
  - cp_library/math/table/primes_cls.py
  - cp_library/ds/reserve_fn.py
  isVerificationFile: false
  path: cp_library/math/conv/gcd_conv_fn.py
  requiredBy: []
  timestamp: '2025-07-10 00:37:15+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/conv/gcd_conv_fn.py
layout: document
redirect_from:
- /library/cp_library/math/conv/gcd_conv_fn.py
- /library/cp_library/math/conv/gcd_conv_fn.py.html
title: cp_library/math/conv/gcd_conv_fn.py
---
