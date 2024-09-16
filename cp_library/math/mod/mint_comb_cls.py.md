---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/arc168_c_swap_characters_mint_comb.test.py
    title: test/arc168_c_swap_characters_mint_comb.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "from itertools import accumulate\n\nclass mint(int):\n    mod = None\n\
    \    def __new__(cls, x=0): return super().__new__(cls, int(x) % cls.mod)\n  \
    \  @classmethod\n    def wrap(cls, x): return super().__new__(cls, x % cls.mod)\n\
    \    @classmethod\n    def cast(cls, x): return super().__new__(cls, x)\n    def\
    \ __add__(self, x): return mint.wrap(super().__add__(x))\n    def __radd__(self,\
    \ x): return mint.wrap(super().__radd__(x))\n    def __sub__(self, x): return\
    \ mint.wrap(super().__sub__(x))\n    def __rsub__(self, x): return mint.wrap(super().__rsub__(x))\n\
    \    def __mul__(self, x): return mint.wrap(super().__mul__(x))\n    def __rmul__(self,\
    \ x): return mint.wrap(super().__rmul__(x))\n    def __floordiv__(self, x): return\
    \ mint.wrap(super().__mul__(pow(int(x),-1,self.mod)))\n    def __rfloordiv__(self,\
    \ x): return mint.wrap(int.__mul__(x,pow(int(self),-1,self.mod)))\n    def __pow__(self,\
    \ x): return mint.cast(pow(int(self),x,self.mod))\n    def __eq__(self, x): return\
    \ super().__eq__(mint.wrap(x))\n    def __req__(self, x): return super().__eq__(mint.wrap(x))\n\
    \    @classmethod\n    def precomp(cls,n):\n        cls.F = list(accumulate(range(1,n+1),\
    \ cls.__mul__, initial=cls(1)))\n        cls.Finv = list(accumulate(range(n,0,-1),\
    \ cls.__mul__, initial=1//cls.F[n]))[::-1]\n    @classmethod\n    def comb(cls,\
    \ n, k, /):\n        if n < k: return 0\n        return cls.F[n]*cls.Finv[k]*cls.Finv[n\
    \ - k]\n    @classmethod\n    def multinom(cls, n, *K):\n        res = cls(1)\n\
    \        for k in K:\n            res *= cls.comb(n, k)\n            n -= k\n\
    \        return res\n"
  code: "from itertools import accumulate\n\nclass mint(int):\n    mod = None\n  \
    \  def __new__(cls, x=0): return super().__new__(cls, int(x) % cls.mod)\n    @classmethod\n\
    \    def wrap(cls, x): return super().__new__(cls, x % cls.mod)\n    @classmethod\n\
    \    def cast(cls, x): return super().__new__(cls, x)\n    def __add__(self, x):\
    \ return mint.wrap(super().__add__(x))\n    def __radd__(self, x): return mint.wrap(super().__radd__(x))\n\
    \    def __sub__(self, x): return mint.wrap(super().__sub__(x))\n    def __rsub__(self,\
    \ x): return mint.wrap(super().__rsub__(x))\n    def __mul__(self, x): return\
    \ mint.wrap(super().__mul__(x))\n    def __rmul__(self, x): return mint.wrap(super().__rmul__(x))\n\
    \    def __floordiv__(self, x): return mint.wrap(super().__mul__(pow(int(x),-1,self.mod)))\n\
    \    def __rfloordiv__(self, x): return mint.wrap(int.__mul__(x,pow(int(self),-1,self.mod)))\n\
    \    def __pow__(self, x): return mint.cast(pow(int(self),x,self.mod))\n    def\
    \ __eq__(self, x): return super().__eq__(mint.wrap(x))\n    def __req__(self,\
    \ x): return super().__eq__(mint.wrap(x))\n    @classmethod\n    def precomp(cls,n):\n\
    \        cls.F = list(accumulate(range(1,n+1), cls.__mul__, initial=cls(1)))\n\
    \        cls.Finv = list(accumulate(range(n,0,-1), cls.__mul__, initial=1//cls.F[n]))[::-1]\n\
    \    @classmethod\n    def comb(cls, n, k, /):\n        if n < k: return 0\n \
    \       return cls.F[n]*cls.Finv[k]*cls.Finv[n - k]\n    @classmethod\n    def\
    \ multinom(cls, n, *K):\n        res = cls(1)\n        for k in K:\n         \
    \   res *= cls.comb(n, k)\n            n -= k\n        return res\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/mod/mint_comb_cls.py
  requiredBy: []
  timestamp: '2024-09-16 19:46:13+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/arc168_c_swap_characters_mint_comb.test.py
documentation_of: cp_library/math/mod/mint_comb_cls.py
layout: document
redirect_from:
- /library/cp_library/math/mod/mint_comb_cls.py
- /library/cp_library/math/mod/mint_comb_cls.py.html
title: cp_library/math/mod/mint_comb_cls.py
---
