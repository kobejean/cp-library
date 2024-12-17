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
    \    def __getitem__(self, key) -> int: ...\n\nclass LinearSieveCounts(list[int],\
    \ SieveProtocol):\n\n    def __init__(spf, N: int):\n        super().__init__([0]\
    \ * (N + 1))\n        exp = [0] * (N + 1)\n        nxt = [0] * (N + 1)\n     \
    \   primes = Primes.__new__(Primes)\n        spf[0], spf[1] = 0, 1\n        exp[1]\
    \ = 1\n        for x in range(2,N+1):\n            if spf[x] == 0:\n         \
    \       spf[x],exp[x] = x,1\n                primes.append(x)\n            for\
    \ p in primes:\n                if (y := x*p) > N or p > spf[x]: break\n     \
    \           spf[y] = p\n                if x%p:\n                    nxt[y], exp[y]\
    \ = x, 1\n                else:\n                    nxt[y], exp[y] = nxt[x],\
    \ exp[x]+1\n        spf.primes = primes\n        spf.exp = exp\n        spf.nxt\
    \ = nxt\n    \n    def factor_cnts(spf, N: int):\n        assert N < len(spf)\n\
    \        exp,nxt = spf.exp, spf.nxt\n        pairs = []\n        while spf[N]\
    \ != N:\n            pairs.append((spf[N],exp[N]))\n            N = nxt[N]\n \
    \       if N:\n            pairs.append((spf[N],exp[N]))\n        return pairs\n\
    \n    def factors(spf, N):\n        assert N < len(spf)\n        exp,nxt = spf.exp,\
    \ spf.nxt\n        factors = []\n        while N > 1:\n            factors.extend(spf[N]\
    \ for _ in range(exp[N]))\n            N = nxt[N]\n        return factors\n"
  code: "import cp_library.math.table.__header__\nfrom cp_library.math.table.sieve_proto\
    \ import SieveProtocol\nfrom cp_library.math.table.primes_cls import Primes\n\n\
    class LinearSieveCounts(list[int], SieveProtocol):\n\n    def __init__(spf, N:\
    \ int):\n        super().__init__([0] * (N + 1))\n        exp = [0] * (N + 1)\n\
    \        nxt = [0] * (N + 1)\n        primes = Primes.__new__(Primes)\n      \
    \  spf[0], spf[1] = 0, 1\n        exp[1] = 1\n        for x in range(2,N+1):\n\
    \            if spf[x] == 0:\n                spf[x],exp[x] = x,1\n          \
    \      primes.append(x)\n            for p in primes:\n                if (y :=\
    \ x*p) > N or p > spf[x]: break\n                spf[y] = p\n                if\
    \ x%p:\n                    nxt[y], exp[y] = x, 1\n                else:\n   \
    \                 nxt[y], exp[y] = nxt[x], exp[x]+1\n        spf.primes = primes\n\
    \        spf.exp = exp\n        spf.nxt = nxt\n    \n    def factor_cnts(spf,\
    \ N: int):\n        assert N < len(spf)\n        exp,nxt = spf.exp, spf.nxt\n\
    \        pairs = []\n        while spf[N] != N:\n            pairs.append((spf[N],exp[N]))\n\
    \            N = nxt[N]\n        if N:\n            pairs.append((spf[N],exp[N]))\n\
    \        return pairs\n\n    def factors(spf, N):\n        assert N < len(spf)\n\
    \        exp,nxt = spf.exp, spf.nxt\n        factors = []\n        while N > 1:\n\
    \            factors.extend(spf[N] for _ in range(exp[N]))\n            N = nxt[N]\n\
    \        return factors\n"
  dependsOn:
  - cp_library/math/table/sieve_proto.py
  - cp_library/math/table/primes_cls.py
  isVerificationFile: false
  path: cp_library/math/table/linear_sieve_cnts_cls.py
  requiredBy: []
  timestamp: '2024-12-17 21:24:00+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/table/linear_sieve_cnts_cls.py
layout: document
redirect_from:
- /library/cp_library/math/table/linear_sieve_cnts_cls.py
- /library/cp_library/math/table/linear_sieve_cnts_cls.py.html
title: cp_library/math/table/linear_sieve_cnts_cls.py
---
