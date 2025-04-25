---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/reserve_fn.py
    title: cp_library/ds/reserve_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/table/primes_cls.py
    title: cp_library/math/table/primes_cls.py
  - icon: ':warning:'
    path: cp_library/math/table/sieve_proto.py
    title: cp_library/math/table/sieve_proto.py
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
    from functools import cached_property\nfrom typing import Protocol\nimport operator\n\
    from typing import Callable\n\n\ndef reserve(A: list, est_len: int) -> None: ...\n\
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
    \ b in enumerate(B): A[i] = mul(A[i], b)\n        return P.divisor_mobius(A, sub)\n\
    \nclass SieveProtocol(Protocol):\n    primes: Primes\n    def factor_cnts(self,\
    \ N): ...\n    def factors(self, N): ...\n    def unique_factors(self, N): ...\n\
    \    def __getitem__(self, key) -> int: ...\n\nclass Sieve(list[int], SieveProtocol):\n\
    \    def __init__(spf, N):\n        super().__init__(i for i in range(N+1))\n\
    \        spf[0] = 1\n        for x in range(2, N+1):\n            x2 = x*x\n \
    \           if x2 > N: break\n            if spf[x] == x:\n                for\
    \ j in range(x2, N+1, x):\n                    if spf[j] == j:\n             \
    \           spf[j] = x\n    @cached_property\n    def primes(spf) -> Primes:\n\
    \        gen = (x for x,f in enumerate(spf) if f == x)\n        primes = Primes.__new__(Primes)\n\
    \        super(Primes, primes).__init__(gen)\n        return primes\n\n    def\
    \ factor_cnts(spf, N):\n        assert N < len(spf)\n        pairs = []\n    \
    \    while N > 1:\n            match pairs:\n                case [*_, (f,cnt)]\
    \ if f == spf[N]:\n                    pairs[-1] = (f,cnt+1)\n               \
    \ case _:\n                    pairs.append((spf[N], 1))\n            N //= spf[N]\n\
    \        return pairs\n\n    def factors(spf, N):\n        assert N < len(spf)\n\
    \        factors = []\n        while N > 1:\n            factors.append(spf[N])\n\
    \            N //= spf[N]\n        return factors\n    \n    def unique_factors(spf,\
    \ N):\n        assert N < len(spf)\n        factors = []\n        while N > 1:\n\
    \            if factors and factors[-1] != spf[N]: \n                factors.append(spf[N])\n\
    \            N //= spf[N]\n        return factors\n"
  code: "import cp_library.math.table.__header__\nfrom functools import cached_property\n\
    from cp_library.math.table.sieve_proto import SieveProtocol\nfrom cp_library.math.table.primes_cls\
    \ import Primes\n\nclass Sieve(list[int], SieveProtocol):\n    def __init__(spf,\
    \ N):\n        super().__init__(i for i in range(N+1))\n        spf[0] = 1\n \
    \       for x in range(2, N+1):\n            x2 = x*x\n            if x2 > N:\
    \ break\n            if spf[x] == x:\n                for j in range(x2, N+1,\
    \ x):\n                    if spf[j] == j:\n                        spf[j] = x\n\
    \    @cached_property\n    def primes(spf) -> Primes:\n        gen = (x for x,f\
    \ in enumerate(spf) if f == x)\n        primes = Primes.__new__(Primes)\n    \
    \    super(Primes, primes).__init__(gen)\n        return primes\n\n    def factor_cnts(spf,\
    \ N):\n        assert N < len(spf)\n        pairs = []\n        while N > 1:\n\
    \            match pairs:\n                case [*_, (f,cnt)] if f == spf[N]:\n\
    \                    pairs[-1] = (f,cnt+1)\n                case _:\n        \
    \            pairs.append((spf[N], 1))\n            N //= spf[N]\n        return\
    \ pairs\n\n    def factors(spf, N):\n        assert N < len(spf)\n        factors\
    \ = []\n        while N > 1:\n            factors.append(spf[N])\n           \
    \ N //= spf[N]\n        return factors\n    \n    def unique_factors(spf, N):\n\
    \        assert N < len(spf)\n        factors = []\n        while N > 1:\n   \
    \         if factors and factors[-1] != spf[N]: \n                factors.append(spf[N])\n\
    \            N //= spf[N]\n        return factors\n"
  dependsOn:
  - cp_library/math/table/sieve_proto.py
  - cp_library/math/table/primes_cls.py
  - cp_library/ds/reserve_fn.py
  isVerificationFile: false
  path: cp_library/math/table/sieve_cls.py
  requiredBy: []
  timestamp: '2025-04-25 16:40:50+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/table/sieve_cls.py
layout: document
redirect_from:
- /library/cp_library/math/table/sieve_cls.py
- /library/cp_library/math/table/sieve_cls.py.html
title: cp_library/math/table/sieve_cls.py
---
