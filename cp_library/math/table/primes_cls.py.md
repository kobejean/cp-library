---
data:
  _extendedDependsOn: []
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
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \nclass Primes(list[int]):\n    def __init__(primes, N: int):\n        super().__init__()\n\
    \        spf = [0] * (N + 1)\n        spf[0], spf[1] = 0, 1\n\n        for i in\
    \ range(2, N + 1):\n            if spf[i] == 0:\n                spf[i] = i\n\
    \                primes.append(i)\n            for p in primes:\n            \
    \    if p > spf[i] or i * p > N:\n                    break\n                spf[i\
    \ * p] = p\n        primes.spf = spf\n"
  code: "import cp_library.math.table.__header__\n\nclass Primes(list[int]):\n   \
    \ def __init__(primes, N: int):\n        super().__init__()\n        spf = [0]\
    \ * (N + 1)\n        spf[0], spf[1] = 0, 1\n\n        for i in range(2, N + 1):\n\
    \            if spf[i] == 0:\n                spf[i] = i\n                primes.append(i)\n\
    \            for p in primes:\n                if p > spf[i] or i * p > N:\n \
    \                   break\n                spf[i * p] = p\n        primes.spf\
    \ = spf\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/table/primes_cls.py
  requiredBy:
  - cp_library/math/table/sieve_cls.py
  - cp_library/math/table/totient_cls.py
  - cp_library/math/table/linear_sieve_cnts_cls.py
  - cp_library/math/table/linear_sieve_cls.py
  - cp_library/math/table/sieve_proto.py
  timestamp: '2025-02-12 22:25:56+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/table/primes_cls.py
layout: document
redirect_from:
- /library/cp_library/math/table/primes_cls.py
- /library/cp_library/math/table/primes_cls.py.html
title: cp_library/math/table/primes_cls.py
---
