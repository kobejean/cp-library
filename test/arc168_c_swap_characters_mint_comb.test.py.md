---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/io/rint_fn.py
    title: cp_library/io/rint_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/mint_comb_cls.py
    title: cp_library/math/mod/mint_comb_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/arc168/tasks/arc168_c
    links:
    - https://atcoder.jp/contests/arc168/tasks/arc168_c
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/arc168/tasks/arc168_c\n\
    from itertools import accumulate\n\nclass mint(int):\n    mod = None\n    def\
    \ __new__(cls, x=0): return super().__new__(cls, x % cls.mod)\n    def __add__(self,\
    \ other): return mint(super().__add__(other))\n    def __radd__(self, other):\
    \ return mint(super().__radd__(other))\n    def __sub__(self, other): return mint(super().__sub__(other))\n\
    \    def __rsub__(self, other): return mint(super().__rsub__(other))\n    def\
    \ __mul__(self, other): return mint(super().__mul__(other))\n    def __rmul__(self,\
    \ other): return mint(super().__rmul__(other))\n    def __truediv__(self, other):\
    \ return mint(super().__mul__(pow(int(other),-1,self.mod)))\n    def __rtruediv__(self,\
    \ other): return mint(int.__mul__(other,pow(int(self),-1,self.mod)))\n    def\
    \ __mod__(self, other): return mint(super().__mod__(other))\n    def __rmod__(self,\
    \ other): return mint(super().__rmod__(other))\n    def __pow__(self, other):\
    \ return mint(pow(int(self),int(other),self.mod))\n    def __rpow__(self, other):\
    \ return mint(pow(int(other),int(other),self.mod))\n    def __eq__(self, other):\
    \ return super().__eq__(mint(other))\n    def __req__(self, other): return super().__eq__(mint(other))\n\
    \    @classmethod\n    def precomp(cls,N):\n        cls._fact = list(accumulate(range(1,N+1),\
    \ cls.__mul__, initial=cls(1)))\n        cls._fact_inv = list(accumulate(range(N,0,-1),\
    \ cls.__mul__, initial=1/cls._fact[N]))[::-1]\n    @classmethod\n    def comb(cls,\
    \ N, K):\n        if N < K: return 0\n        return cls._fact[N]*cls._fact_inv[K]*cls._fact_inv[N\
    \ - K]\n    @classmethod\n    def multinom(cls, N, *args):\n        res = cls(1)\n\
    \        for arg in args:\n            res *= cls.comb(N, arg)\n            N\
    \ -= arg\n        return res\nmint.mod = 998244353\ndef rint(shift=0, base=10):\n\
    \    return [int(x, base) + shift for x in input().split()]\n\nN, K = rint()\n\
    mint.precomp(N)\nS = input()\nA, B, C = S.count('A'), S.count('B'), S.count('C')\n\
    \n# x A <-> B\n# y B <-> C\n# z C <-> A\n# w A -> B -> C -> A or A -> C -> B ->\
    \ A \n\nans = mint()\nfor x in range(K+1):\n    for y in range(K-x+1):\n     \
    \   for z in range(K-x-y+1):\n            for w in range(((K-x-y-z)//2+1)):\n\
    \                cnt =   mint.multinom(A,x,z+w) * \\\n                       \
    \ mint.multinom(B,y,x+w) * \\\n                        mint.multinom(C,z,y+w)\n\
    \                if w > 0: cnt*=2\n                ans += cnt\nprint(ans)\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/arc168/tasks/arc168_c\n\
    from cp_library.math.mod.mint_comb_cls import mint\nmint.mod = 998244353\nfrom\
    \ cp_library.io.rint_fn import rint\n\nN, K = rint()\nmint.precomp(N)\nS = input()\n\
    A, B, C = S.count('A'), S.count('B'), S.count('C')\n\n# x A <-> B\n# y B <-> C\n\
    # z C <-> A\n# w A -> B -> C -> A or A -> C -> B -> A \n\nans = mint()\nfor x\
    \ in range(K+1):\n    for y in range(K-x+1):\n        for z in range(K-x-y+1):\n\
    \            for w in range(((K-x-y-z)//2+1)):\n                cnt =   mint.multinom(A,x,z+w)\
    \ * \\\n                        mint.multinom(B,y,x+w) * \\\n                \
    \        mint.multinom(C,z,y+w)\n                if w > 0: cnt*=2\n          \
    \      ans += cnt\nprint(ans)\n"
  dependsOn:
  - cp_library/math/mod/mint_comb_cls.py
  - cp_library/io/rint_fn.py
  isVerificationFile: true
  path: test/arc168_c_swap_characters_mint_comb.test.py
  requiredBy: []
  timestamp: '2024-09-05 11:18:10+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/arc168_c_swap_characters_mint_comb.test.py
layout: document
redirect_from:
- /verify/test/arc168_c_swap_characters_mint_comb.test.py
- /verify/test/arc168_c_swap_characters_mint_comb.test.py.html
title: test/arc168_c_swap_characters_mint_comb.test.py
---
