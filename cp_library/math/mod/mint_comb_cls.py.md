---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/arc168_c_swap_characters_mint_comb.test.py
    title: test/arc168_c_swap_characters_mint_comb.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "from itertools import accumulate\n\nclass mint(int):\n    mod = None\n\
    \    def __new__(cls, x=0): return super().__new__(cls, x % cls.mod)\n    def\
    \ __add__(self, other): return mint(super().__add__(other))\n    def __radd__(self,\
    \ other): return mint(super().__radd__(other))\n    def __sub__(self, other):\
    \ return mint(super().__sub__(other))\n    def __rsub__(self, other): return mint(super().__rsub__(other))\n\
    \    def __mul__(self, other): return mint(super().__mul__(other))\n    def __rmul__(self,\
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
    \ -= arg\n        return res\n"
  code: "from itertools import accumulate\n\nclass mint(int):\n    mod = None\n  \
    \  def __new__(cls, x=0): return super().__new__(cls, x % cls.mod)\n    def __add__(self,\
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
    \ -= arg\n        return res"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/mod/mint_comb_cls.py
  requiredBy: []
  timestamp: '2024-09-03 23:33:52+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/arc168_c_swap_characters_mint_comb.test.py
documentation_of: cp_library/math/mod/mint_comb_cls.py
layout: document
redirect_from:
- /library/cp_library/math/mod/mint_comb_cls.py
- /library/cp_library/math/mod/mint_comb_cls.py.html
title: cp_library/math/mod/mint_comb_cls.py
---
