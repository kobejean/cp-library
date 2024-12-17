---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: cp_library/math/table/primes_cls.py
    title: cp_library/math/table/primes_cls.py
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
    \    def __getitem__(self, key) -> int: ...\n"
  code: "import cp_library.math.table.__header__\nfrom typing import Protocol\nfrom\
    \ cp_library.math.table.primes_cls import Primes\n\nclass SieveProtocol(Protocol):\n\
    \    primes: Primes\n    def factor_cnts(self, N): ...\n    def factors(self,\
    \ N): ...\n    def unique_factors(self, N): ...\n    def __getitem__(self, key)\
    \ -> int: ..."
  dependsOn:
  - cp_library/math/table/primes_cls.py
  isVerificationFile: false
  path: cp_library/math/table/sieve_proto.py
  requiredBy:
  - cp_library/math/table/linear_sieve_cnts_cls.py
  - cp_library/math/table/sieve_cls.py
  - cp_library/math/table/linear_sieve_cls.py
  timestamp: '2024-12-18 00:49:06+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/table/sieve_proto.py
layout: document
redirect_from:
- /library/cp_library/math/table/sieve_proto.py
- /library/cp_library/math/table/sieve_proto.py.html
title: cp_library/math/table/sieve_proto.py
---
