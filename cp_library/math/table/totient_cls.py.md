---
data:
  _extendedDependsOn:
  - icon: ':warning:'
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
    \nclass Primes(list[int]):\n    def __init__(primes, N: int):\n        super().__init__()\n\
    \        spf = [0] * (N + 1)\n        spf[0], spf[1] = 0, 1\n\n        for i in\
    \ range(2, N + 1):\n            if spf[i] == 0:\n                spf[i] = i\n\
    \                primes.append(i)\n            for p in primes:\n            \
    \    if p > spf[i] or i * p > N:\n                    break\n                spf[i\
    \ * p] = p\n        primes.spf = spf\n\nclass Totient(list[int]):\n    def __init__(phi,\
    \ N):\n        super().__init__([0] * (N + 1))\n        phi[0], phi[1] = 0, 1\n\
    \        primes = Primes.__new__(Primes)\n\n        for x in range(2, N + 1):\n\
    \            if phi[x] == 0:\n                phi[x] = x-1\n                primes.append(x)\n\
    \            for p in primes:\n                if (y := x * p) > N: break\n  \
    \              if x % p == 0:\n                    phi[y] = phi[x] * p\n     \
    \               break\n                phi[y] = phi[x] * (p-1)\n        phi.primes\
    \ = phi\n"
  code: "import cp_library.math.table.__header__\nfrom cp_library.math.table.primes_cls\
    \ import Primes\n\nclass Totient(list[int]):\n    def __init__(phi, N):\n    \
    \    super().__init__([0] * (N + 1))\n        phi[0], phi[1] = 0, 1\n        primes\
    \ = Primes.__new__(Primes)\n\n        for x in range(2, N + 1):\n            if\
    \ phi[x] == 0:\n                phi[x] = x-1\n                primes.append(x)\n\
    \            for p in primes:\n                if (y := x * p) > N: break\n  \
    \              if x % p == 0:\n                    phi[y] = phi[x] * p\n     \
    \               break\n                phi[y] = phi[x] * (p-1)\n        phi.primes\
    \ = phi\n"
  dependsOn:
  - cp_library/math/table/primes_cls.py
  isVerificationFile: false
  path: cp_library/math/table/totient_cls.py
  requiredBy: []
  timestamp: '2024-12-08 02:40:51+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/table/totient_cls.py
layout: document
redirect_from:
- /library/cp_library/math/table/totient_cls.py
- /library/cp_library/math/table/totient_cls.py.html
title: cp_library/math/table/totient_cls.py
---
