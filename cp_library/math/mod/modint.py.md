---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/modmat.py
    title: cp_library/math/mod/modmat.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/pow_of_matrix_mint.test.py
    title: test/pow_of_matrix_mint.test.py
  - icon: ':heavy_check_mark:'
    path: test/pow_of_matrix_modmat.test.py
    title: test/pow_of_matrix_modmat.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "\nclass mint(int):\n    mod = None\n    def __new__(cls, x): return\
    \ super().__new__(cls, x % cls.mod)\n    def __add__(self, other): return mint(super().__add__(other))\n\
    \    def __radd__(self, other): return mint(super().__radd__(other))\n    def\
    \ __sub__(self, other): return mint(super().__sub__(other))\n    def __rsub__(self,\
    \ other): return mint(super().__rsub__(other))\n    def __mul__(self, other):\
    \ return mint(super().__mul__(other))\n    def __rmul__(self, other): return mint(super().__rmul__(other))\n\
    \    def __truediv__(self, other): return mint(super().__mul__(pow(other,-1,self.mod)))\n\
    \    def __rtruediv__(self, other): return mint(int.__mul__(other,pow(self,-1,self.mod)))\n\
    \    def __mod__(self, other): return mint(super().__mod__(other))\n    def __rmod__(self,\
    \ other): return mint(super().__rmod__(other))\n    def __pow__(self, other):\
    \ return mint(pow(self,other,self.mod))\n    def __rpow__(self, other): return\
    \ mint(pow(other,other,self.mod))\n    def __eq__(self, other): return super().__eq__(mint(other))\n\
    \    def __req__(self, other): return super().__eq__(mint(other))\n\n"
  code: "\nclass mint(int):\n    mod = None\n    def __new__(cls, x): return super().__new__(cls,\
    \ x % cls.mod)\n    def __add__(self, other): return mint(super().__add__(other))\n\
    \    def __radd__(self, other): return mint(super().__radd__(other))\n    def\
    \ __sub__(self, other): return mint(super().__sub__(other))\n    def __rsub__(self,\
    \ other): return mint(super().__rsub__(other))\n    def __mul__(self, other):\
    \ return mint(super().__mul__(other))\n    def __rmul__(self, other): return mint(super().__rmul__(other))\n\
    \    def __truediv__(self, other): return mint(super().__mul__(pow(other,-1,self.mod)))\n\
    \    def __rtruediv__(self, other): return mint(int.__mul__(other,pow(self,-1,self.mod)))\n\
    \    def __mod__(self, other): return mint(super().__mod__(other))\n    def __rmod__(self,\
    \ other): return mint(super().__rmod__(other))\n    def __pow__(self, other):\
    \ return mint(pow(self,other,self.mod))\n    def __rpow__(self, other): return\
    \ mint(pow(other,other,self.mod))\n    def __eq__(self, other): return super().__eq__(mint(other))\n\
    \    def __req__(self, other): return super().__eq__(mint(other))\n\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/mod/modint.py
  requiredBy:
  - cp_library/math/mod/modmat.py
  timestamp: '2024-08-18 15:24:28+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/pow_of_matrix_modmat.test.py
  - test/pow_of_matrix_mint.test.py
documentation_of: cp_library/math/mod/modint.py
layout: document
redirect_from:
- /library/cp_library/math/mod/modint.py
- /library/cp_library/math/mod/modint.py.html
title: cp_library/math/mod/modint.py
---