---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/math/mod/_modmat_cls.py
    title: cp_library/math/mod/_modmat_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/modmat_cls.py
    title: cp_library/math/mod/modmat_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/pow_of_matrix_matpow.test.py
    title: test/pow_of_matrix_matpow.test.py
  - icon: ':heavy_check_mark:'
    path: test/pow_of_matrix_modmat.test.py
    title: test/pow_of_matrix_modmat.test.py
  - icon: ':heavy_check_mark:'
    path: test/subset_convolution.test.py
    title: test/subset_convolution.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "\nclass mint(int):\n    mod = None\n    def __new__(cls, x=0): return\
    \ super().__new__(cls, int(x) % cls.mod)\n    @classmethod\n    def wrap(cls,\
    \ x): return super().__new__(cls, x % cls.mod)\n    @classmethod\n    def cast(cls,\
    \ x): return super().__new__(cls, x)\n    def __add__(self, x): return mint.wrap(super().__add__(x))\n\
    \    def __radd__(self, x): return mint.wrap(super().__radd__(x))\n    def __sub__(self,\
    \ x): return mint.wrap(super().__sub__(x))\n    def __rsub__(self, x): return\
    \ mint.wrap(super().__rsub__(x))\n    def __mul__(self, x): return mint.wrap(super().__mul__(x))\n\
    \    def __rmul__(self, x): return mint.wrap(super().__rmul__(x))\n    def __floordiv__(self,\
    \ x): return mint.wrap(super().__mul__(pow(int(x),-1,self.mod)))\n    def __rfloordiv__(self,\
    \ x): return mint.wrap(int.__mul__(x,pow(int(self),-1,self.mod)))\n    def __pow__(self,\
    \ x): return mint.cast(pow(int(self),x,self.mod))\n    def __eq__(self, x): return\
    \ super().__eq__(mint.wrap(x))\n    def __req__(self, x): return super().__eq__(mint.wrap(x))\n"
  code: "\nclass mint(int):\n    mod = None\n    def __new__(cls, x=0): return super().__new__(cls,\
    \ int(x) % cls.mod)\n    @classmethod\n    def wrap(cls, x): return super().__new__(cls,\
    \ x % cls.mod)\n    @classmethod\n    def cast(cls, x): return super().__new__(cls,\
    \ x)\n    def __add__(self, x): return mint.wrap(super().__add__(x))\n    def\
    \ __radd__(self, x): return mint.wrap(super().__radd__(x))\n    def __sub__(self,\
    \ x): return mint.wrap(super().__sub__(x))\n    def __rsub__(self, x): return\
    \ mint.wrap(super().__rsub__(x))\n    def __mul__(self, x): return mint.wrap(super().__mul__(x))\n\
    \    def __rmul__(self, x): return mint.wrap(super().__rmul__(x))\n    def __floordiv__(self,\
    \ x): return mint.wrap(super().__mul__(pow(int(x),-1,self.mod)))\n    def __rfloordiv__(self,\
    \ x): return mint.wrap(int.__mul__(x,pow(int(self),-1,self.mod)))\n    def __pow__(self,\
    \ x): return mint.cast(pow(int(self),x,self.mod))\n    def __eq__(self, x): return\
    \ super().__eq__(mint.wrap(x))\n    def __req__(self, x): return super().__eq__(mint.wrap(x))"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/mod/mint_cls.py
  requiredBy:
  - cp_library/math/mod/modmat_cls.py
  - cp_library/math/mod/_modmat_cls.py
  timestamp: '2024-09-16 19:46:13+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/pow_of_matrix_matpow.test.py
  - test/subset_convolution.test.py
  - test/pow_of_matrix_modmat.test.py
documentation_of: cp_library/math/mod/mint_cls.py
layout: document
redirect_from:
- /library/cp_library/math/mod/mint_cls.py
- /library/cp_library/math/mod/mint_cls.py.html
title: cp_library/math/mod/mint_cls.py
---
