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
    \nclass UniqueFactors(list[int]):\n    def __init__(P, N: int):\n        super().__init__()\n\
    \        P.N = N\n        d = 2\n        while N > 1:\n            if N % d ==\
    \ 0:\n                P.append(d)\n                N //= d\n                while\
    \ N % d == 0:\n                    N //= d\n            d += 1\n            if\
    \ d * d > N:\n                if N > 1: P.append(N)\n                break\n \
    \   \n    def mobius_inv(P, F, inclusive=True):\n        D = P.N\n        # codivisors\
    \ of square free divisors\n        C = [D]*(1<<len(P))\n        f = F(D) if inclusive\
    \ else 0\n        for i,p in enumerate(P):\n            for mask in range(bit\
    \ := 1<<i, bit<<1):\n                C[mask] = C[mask^bit] // p\n            \
    \    Fn = F(C[mask])\n                f = f-Fn if mask.bit_count()&1 else f+Fn\n\
    \        return f if inclusive else -f\n"
  code: "import cp_library.math.table.__header__\n\nclass UniqueFactors(list[int]):\n\
    \    def __init__(P, N: int):\n        super().__init__()\n        P.N = N\n \
    \       d = 2\n        while N > 1:\n            if N % d == 0:\n            \
    \    P.append(d)\n                N //= d\n                while N % d == 0:\n\
    \                    N //= d\n            d += 1\n            if d * d > N:\n\
    \                if N > 1: P.append(N)\n                break\n    \n    def mobius_inv(P,\
    \ F, inclusive=True):\n        D = P.N\n        # codivisors of square free divisors\n\
    \        C = [D]*(1<<len(P))\n        f = F(D) if inclusive else 0\n        for\
    \ i,p in enumerate(P):\n            for mask in range(bit := 1<<i, bit<<1):\n\
    \                C[mask] = C[mask^bit] // p\n                Fn = F(C[mask])\n\
    \                f = f-Fn if mask.bit_count()&1 else f+Fn\n        return f if\
    \ inclusive else -f"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/table/unique_factors_cls.py
  requiredBy: []
  timestamp: '2024-10-02 19:58:00+09:00'
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
