---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/abc304_f_mobius_inv.test.py
    title: test/abc304_f_mobius_inv.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \    \nclass UniqueFactors(list[int]):\n    def __init__(P, N: int):\n       \
    \ super().__init__()\n        P.N = N\n        d = 2\n        while N > 1:\n \
    \           if N % d == 0:\n                P.append(d)\n                N //=\
    \ d\n                while N % d == 0:\n                    N //= d\n        \
    \    d += 1\n            if d * d > N:\n                if N > 1: P.append(N)\n\
    \                break\n    \n    def mobius_inv(P, F, full=True):\n        C,\
    \ f = [P.N]*(1<<len(P)), F(P.N) if full else 0\n        for i,p in enumerate(P):\n\
    \            l = 2*(b := 1<<i)-1\n            for m in range(b, b << 1):\n   \
    \             C[m], f = (c := C[l^m]//p), F(c)-f\n        return -f if full else\
    \ f\n    \n    def totient(P):\n        N = P.N\n        phi = 1\n        for\
    \ p in P:\n            phi *= N - N//p\n        return phi\n"
  code: "import cp_library.math.table.__header__\n    \nclass UniqueFactors(list[int]):\n\
    \    def __init__(P, N: int):\n        super().__init__()\n        P.N = N\n \
    \       d = 2\n        while N > 1:\n            if N % d == 0:\n            \
    \    P.append(d)\n                N //= d\n                while N % d == 0:\n\
    \                    N //= d\n            d += 1\n            if d * d > N:\n\
    \                if N > 1: P.append(N)\n                break\n    \n    def mobius_inv(P,\
    \ F, full=True):\n        C, f = [P.N]*(1<<len(P)), F(P.N) if full else 0\n  \
    \      for i,p in enumerate(P):\n            l = 2*(b := 1<<i)-1\n           \
    \ for m in range(b, b << 1):\n                C[m], f = (c := C[l^m]//p), F(c)-f\n\
    \        return -f if full else f\n    \n    def totient(P):\n        N = P.N\n\
    \        phi = 1\n        for p in P:\n            phi *= N - N//p\n        return\
    \ phi"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/table/unique_factors_cls.py
  requiredBy: []
  timestamp: '2024-12-25 17:59:38+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/abc304_f_mobius_inv.test.py
documentation_of: cp_library/math/table/unique_factors_cls.py
layout: document
redirect_from:
- /library/cp_library/math/table/unique_factors_cls.py
- /library/cp_library/math/table/unique_factors_cls.py.html
title: cp_library/math/table/unique_factors_cls.py
---
