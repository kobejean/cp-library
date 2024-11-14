---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: cp_library/math/table/primes_cls.py
    title: cp_library/math/table/primes_cls.py
  - icon: ':warning:'
    path: cp_library/math/table/sieve_proto.py
    title: cp_library/math/table/sieve_proto.py
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/math/table/sieve_benchmarks.py
    title: cp_library/math/table/sieve_benchmarks.py
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
    from functools import cached_property\nfrom typing import Protocol\n\nclass Primes(list):\n\
    \    def __init__(primes, N: int):\n        super().__init__()\n        spf =\
    \ [0] * (N + 1)\n        spf[0], spf[1] = 0, 1\n\n        for i in range(2, N\
    \ + 1):\n            if spf[i] == 0:\n                spf[i] = i\n           \
    \     primes.append(i)\n            for p in primes:\n                if p > spf[i]\
    \ or i * p > N:\n                    break\n                spf[i * p] = p\n\n\
    class SieveProtocol(Protocol):\n    primes: Primes\n    def factor_cnts(self,\
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
  isVerificationFile: false
  path: cp_library/math/table/sieve_cls.py
  requiredBy:
  - cp_library/math/table/sieve_benchmarks.py
  timestamp: '2024-11-15 01:34:01+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/table/sieve_cls.py
layout: document
redirect_from:
- /library/cp_library/math/table/sieve_cls.py
- /library/cp_library/math/table/sieve_cls.py.html
title: cp_library/math/table/sieve_cls.py
---
