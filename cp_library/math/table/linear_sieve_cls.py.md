---
data:
  _extendedDependsOn:
  - icon: ':warning:'
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
    from typing import Protocol\n\nclass Primes(list[int]):\n    def __init__(primes,\
    \ N: int):\n        super().__init__()\n        spf = [0] * (N + 1)\n        spf[0],\
    \ spf[1] = 0, 1\n\n        for i in range(2, N + 1):\n            if spf[i] ==\
    \ 0:\n                spf[i] = i\n                primes.append(i)\n         \
    \   for p in primes:\n                if p > spf[i] or i * p > N:\n          \
    \          break\n                spf[i * p] = p\n        primes.spf = spf\n\n\
    class SieveProtocol(Protocol):\n    primes: Primes\n    def factor_cnts(self,\
    \ N): ...\n    def factors(self, N): ...\n    def unique_factors(self, N): ...\n\
    \    def __getitem__(self, key) -> int: ...\n\nclass LinearSieve(list[int], SieveProtocol):\n\
    \    def __init__(spf, N):\n        super().__init__([0] * (N + 1))\n        spf[0],\
    \ spf[1] = 0, 1\n        primes = Primes.__new__(Primes)\n\n        for i in range(2,\
    \ N + 1):\n            if spf[i] == 0:\n                spf[i] = i\n         \
    \       primes.append(i)\n            for p in primes:\n                if p >\
    \ spf[i] or i * p > N:\n                    break\n                spf[i * p]\
    \ = p\n        spf.primes = spf\n\n    def factor_cnts(spf, N):\n        assert\
    \ N < len(spf)\n        pairs = []\n        while N > 1:\n            match pairs:\n\
    \                case [*_, (f,cnt)] if f == spf[N]:\n                    pairs[-1]\
    \ = (f,cnt+1)\n                case _:\n                    pairs.append((spf[N],\
    \ 1))\n            N //= spf[N]\n        return pairs\n    \n    def factors(spf,\
    \ N):\n        assert N < len(spf)\n        factors = []\n        while N > 1:\n\
    \            factors.append(spf[N])\n            N //= spf[N]\n        return\
    \ factors\n \n"
  code: "import cp_library.math.table.__header__\nfrom cp_library.math.table.sieve_proto\
    \ import SieveProtocol\nfrom cp_library.math.table.primes_cls import Primes\n\n\
    class LinearSieve(list[int], SieveProtocol):\n    def __init__(spf, N):\n    \
    \    super().__init__([0] * (N + 1))\n        spf[0], spf[1] = 0, 1\n        primes\
    \ = Primes.__new__(Primes)\n\n        for i in range(2, N + 1):\n            if\
    \ spf[i] == 0:\n                spf[i] = i\n                primes.append(i)\n\
    \            for p in primes:\n                if p > spf[i] or i * p > N:\n \
    \                   break\n                spf[i * p] = p\n        spf.primes\
    \ = spf\n\n    def factor_cnts(spf, N):\n        assert N < len(spf)\n       \
    \ pairs = []\n        while N > 1:\n            match pairs:\n               \
    \ case [*_, (f,cnt)] if f == spf[N]:\n                    pairs[-1] = (f,cnt+1)\n\
    \                case _:\n                    pairs.append((spf[N], 1))\n    \
    \        N //= spf[N]\n        return pairs\n    \n    def factors(spf, N):\n\
    \        assert N < len(spf)\n        factors = []\n        while N > 1:\n   \
    \         factors.append(spf[N])\n            N //= spf[N]\n        return factors\n\
    \ "
  dependsOn:
  - cp_library/math/table/sieve_proto.py
  - cp_library/math/table/primes_cls.py
  isVerificationFile: false
  path: cp_library/math/table/linear_sieve_cls.py
  requiredBy: []
  timestamp: '2024-11-28 18:07:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/table/linear_sieve_cls.py
layout: document
redirect_from:
- /library/cp_library/math/table/linear_sieve_cls.py
- /library/cp_library/math/table/linear_sieve_cls.py.html
title: cp_library/math/table/linear_sieve_cls.py
---
