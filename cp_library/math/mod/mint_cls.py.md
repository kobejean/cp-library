---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
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
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \nclass mint(int):\n    mod = zero = one = None\n\n    def __new__(cls, *args,\
    \ **kwargs):\n        match int(*args, **kwargs):\n            case 0: return\
    \ cls.zero\n            case 1: return cls.one\n            case x: return cls.fix(x)\n\
    \n    @classmethod\n    def set_mod(cls, mod):\n        cls.mod = mod\n      \
    \  cls.zero, cls.one = cls.cast(0), cls.fix(1)\n\n    @classmethod\n    def fix(cls,\
    \ x): return cls.cast(x%cls.mod)\n\n    @classmethod\n    def cast(cls, x): return\
    \ super().__new__(cls,x)\n\n    @classmethod\n    def mod_inv(cls, x):\n     \
    \   a,b,s,t = int(x), cls.mod, 1, 0\n        while b: a,b,s,t = b,a%b,t,s-a//b*t\n\
    \        if a == 1: return cls.fix(s)\n        raise ValueError(f\"{x} is not\
    \ invertible\")\n    \n    @property\n    def inv(self): return mint.mod_inv(self)\n\
    \n    def __add__(self, x): return mint.fix(super().__add__(x))\n    def __radd__(self,\
    \ x): return mint.fix(super().__radd__(x))\n    def __sub__(self, x): return mint.fix(super().__sub__(x))\n\
    \    def __rsub__(self, x): return mint.fix(super().__rsub__(x))\n    def __mul__(self,\
    \ x): return mint.fix(super().__mul__(x))\n    def __rmul__(self, x): return mint.fix(super().__rmul__(x))\n\
    \    def __floordiv__(self, x): return self * mint.mod_inv(x)\n    def __rfloordiv__(self,\
    \ x): return self.inv * x\n    def __truediv__(self, x): return self * mint.mod_inv(x)\n\
    \    def __rtruediv__(self, x): return self.inv * x\n    def __pow__(self, x):\
    \ \n        return self.cast(super().__pow__(x, self.mod))\n    def __eq__(self,\
    \ x): return super().__eq__(self-x, 0)\n    def __neg__(self): return mint.mod-self\n\
    \    def __pos__(self): return self\n    def __abs__(self): return self\n\n"
  code: "import cp_library.math.mod.__header__\n\nclass mint(int):\n    mod = zero\
    \ = one = None\n\n    def __new__(cls, *args, **kwargs):\n        match int(*args,\
    \ **kwargs):\n            case 0: return cls.zero\n            case 1: return\
    \ cls.one\n            case x: return cls.fix(x)\n\n    @classmethod\n    def\
    \ set_mod(cls, mod):\n        cls.mod = mod\n        cls.zero, cls.one = cls.cast(0),\
    \ cls.fix(1)\n\n    @classmethod\n    def fix(cls, x): return cls.cast(x%cls.mod)\n\
    \n    @classmethod\n    def cast(cls, x): return super().__new__(cls,x)\n\n  \
    \  @classmethod\n    def mod_inv(cls, x):\n        a,b,s,t = int(x), cls.mod,\
    \ 1, 0\n        while b: a,b,s,t = b,a%b,t,s-a//b*t\n        if a == 1: return\
    \ cls.fix(s)\n        raise ValueError(f\"{x} is not invertible\")\n    \n   \
    \ @property\n    def inv(self): return mint.mod_inv(self)\n\n    def __add__(self,\
    \ x): return mint.fix(super().__add__(x))\n    def __radd__(self, x): return mint.fix(super().__radd__(x))\n\
    \    def __sub__(self, x): return mint.fix(super().__sub__(x))\n    def __rsub__(self,\
    \ x): return mint.fix(super().__rsub__(x))\n    def __mul__(self, x): return mint.fix(super().__mul__(x))\n\
    \    def __rmul__(self, x): return mint.fix(super().__rmul__(x))\n    def __floordiv__(self,\
    \ x): return self * mint.mod_inv(x)\n    def __rfloordiv__(self, x): return self.inv\
    \ * x\n    def __truediv__(self, x): return self * mint.mod_inv(x)\n    def __rtruediv__(self,\
    \ x): return self.inv * x\n    def __pow__(self, x): \n        return self.cast(super().__pow__(x,\
    \ self.mod))\n    def __eq__(self, x): return super().__eq__(self-x, 0)\n    def\
    \ __neg__(self): return mint.mod-self\n    def __pos__(self): return self\n  \
    \  def __abs__(self): return self\n\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/mod/mint_cls.py
  requiredBy:
  - cp_library/math/mod/modmat_cls.py
  timestamp: '2024-09-28 19:50:41+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/subset_convolution.test.py
  - test/pow_of_matrix_modmat.test.py
  - test/pow_of_matrix_matpow.test.py
documentation_of: cp_library/math/mod/mint_cls.py
layout: document
redirect_from:
- /library/cp_library/math/mod/mint_cls.py
- /library/cp_library/math/mod/mint_cls.py.html
title: cp_library/math/mod/mint_cls.py
---
