---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/table/pow_cls.py
    title: cp_library/math/table/pow_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/table/unique_factors_cls.py
    title: cp_library/math/table/unique_factors_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/abc304/tasks/abc304_f
    links:
    - https://atcoder.jp/contests/abc304/tasks/abc304_f
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc304/tasks/abc304_f\n\
    \nmod = 998244353\ndef main():\n    N = int(input())\n    S = input()\n\n    work\
    \ = [i for i in range(N) if S[i] == '.']\n    P = UniqueFactors(N)\n    pow2 =\
    \ Pow(2,N)\n    def F(x):\n        schedule = [True]*x\n        for j in work:\n\
    \            schedule[j%x] = False\n        return pow2[sum(schedule)]\n    \n\
    \    fn = P.mobius_inv(F, False) % mod\n    print(fn)\n\n'''\n\u257A\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n    \nclass UniqueFactors(list[int]):\n    def __init__(P,\
    \ N: int):\n        super().__init__()\n        P.N = N\n        d = 2\n     \
    \   while N > 1:\n            if N % d == 0:\n                P.append(d)\n  \
    \              N //= d\n                while N % d == 0:\n                  \
    \  N //= d\n            d += 1\n            if d * d > N:\n                if\
    \ N > 1: P.append(N)\n                break\n    \n    def mobius_inv(P, F, full=True):\n\
    \        C, f = [P.N]*(1<<len(P)), F(P.N) if full else 0\n        for i,p in enumerate(P):\n\
    \            l = 2*(b := 1<<i)-1\n            for m in range(b, b << 1):\n   \
    \             C[m], f = (c := C[l^m]//p), F(c)-f\n        return -f if full else\
    \ f\n    \n    def totient(P):\n        N = P.N\n        phi = 1\n        for\
    \ p in P:\n            phi *= N - N//p\n        return phi\nfrom itertools import\
    \ accumulate\n\nclass Pow(list):\n    def __init__(self,K,N,mod=None):\n     \
    \   super().__init__([1]*(N+1))\n        if mod is None:\n            for i in\
    \ range(N):\n                self[i+1] = self[i]*K\n        else:\n          \
    \  for i in range(N):\n                self[i+1] = self[i]*K % mod\n\nif __name__\
    \ == \"__main__\":\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc304/tasks/abc304_f\n\
    \nmod = 998244353\ndef main():\n    N = int(input())\n    S = input()\n\n    work\
    \ = [i for i in range(N) if S[i] == '.']\n    P = UniqueFactors(N)\n    pow2 =\
    \ Pow(2,N)\n    def F(x):\n        schedule = [True]*x\n        for j in work:\n\
    \            schedule[j%x] = False\n        return pow2[sum(schedule)]\n    \n\
    \    fn = P.mobius_inv(F, False) % mod\n    print(fn)\n\nfrom cp_library.math.table.unique_factors_cls\
    \ import UniqueFactors\nfrom cp_library.math.table.pow_cls import Pow\n\nif __name__\
    \ == \"__main__\":\n    main()"
  dependsOn:
  - cp_library/math/table/unique_factors_cls.py
  - cp_library/math/table/pow_cls.py
  isVerificationFile: true
  path: test/abc304_f_mobius_inv.test.py
  requiredBy: []
  timestamp: '2024-11-16 19:58:23+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/abc304_f_mobius_inv.test.py
layout: document
redirect_from:
- /verify/test/abc304_f_mobius_inv.test.py
- /verify/test/abc304_f_mobius_inv.test.py.html
title: test/abc304_f_mobius_inv.test.py
---
