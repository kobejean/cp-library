---
data:
  _extendedDependsOn: []
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
    from fractions import Fraction\n\n\n\nclass mfrac(Fraction):\n    @classmethod\n\
    \    def set_mod(cls, mod):\n        cls.mod = mod\n        cls.zero = mfrac(0)\n\
    \        cls.one = mfrac(1)\n        cls.two = mfrac(2)\n\n    @classmethod\n\
    \    def cast(cls, x): return mfrac(x)\n\n    @classmethod\n    def mod_inv(cls,\
    \ x): return mfrac(1, x)\n\n    def __add__(self, x): return self.cast(super().__add__(x))\n\
    \    def __radd__(self, x): return self.cast(super().__radd__(x))\n    def __sub__(self,\
    \ x): return self.cast(super().__sub__(x))\n    def __rsub__(self, x): return\
    \ self.cast(super().__rsub__(x))\n    def __mul__(self, x): return self.cast(super().__mul__(x))\n\
    \    def __rmul__(self, x): return self.cast(super().__rmul__(x))\n    def __floordiv__(self,\
    \ x): return self.cast(super().__floordiv__(x))\n    def __rfloordiv__(self, x):\
    \ return self.cast(super().__rfloordiv__(x))\n    def __truediv__(self, x): return\
    \ self.cast(super().__truediv__(x))\n    def __rtruediv__(self, x): return self.cast(super().__rtruediv__(x))\n\
    \    def __pow__(self, x): return self.cast(super().__pow__(x))\n    def __neg__(self,\
    \ x): return self.cast(super().__neg__(x))\n    def __pos__(self, x): return self.cast(super().__pos__(x))\n\
    \    def __abs__(self, x): return self.cast(super().__abs__(x))\n    def __repr__(self):\
    \ return super().__str__()\n"
  code: "import cp_library.__header__\nfrom fractions import Fraction\nimport cp_library.math.__header__\n\
    import cp_library.math.mod.__header__\n\nclass mfrac(Fraction):\n    @classmethod\n\
    \    def set_mod(cls, mod):\n        cls.mod = mod\n        cls.zero = mfrac(0)\n\
    \        cls.one = mfrac(1)\n        cls.two = mfrac(2)\n\n    @classmethod\n\
    \    def cast(cls, x): return mfrac(x)\n\n    @classmethod\n    def mod_inv(cls,\
    \ x): return mfrac(1, x)\n\n    def __add__(self, x): return self.cast(super().__add__(x))\n\
    \    def __radd__(self, x): return self.cast(super().__radd__(x))\n    def __sub__(self,\
    \ x): return self.cast(super().__sub__(x))\n    def __rsub__(self, x): return\
    \ self.cast(super().__rsub__(x))\n    def __mul__(self, x): return self.cast(super().__mul__(x))\n\
    \    def __rmul__(self, x): return self.cast(super().__rmul__(x))\n    def __floordiv__(self,\
    \ x): return self.cast(super().__floordiv__(x))\n    def __rfloordiv__(self, x):\
    \ return self.cast(super().__rfloordiv__(x))\n    def __truediv__(self, x): return\
    \ self.cast(super().__truediv__(x))\n    def __rtruediv__(self, x): return self.cast(super().__rtruediv__(x))\n\
    \    def __pow__(self, x): return self.cast(super().__pow__(x))\n    def __neg__(self,\
    \ x): return self.cast(super().__neg__(x))\n    def __pos__(self, x): return self.cast(super().__pos__(x))\n\
    \    def __abs__(self, x): return self.cast(super().__abs__(x))\n    def __repr__(self):\
    \ return super().__str__()"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/math/mod/mfrac_cls.py
  requiredBy: []
  timestamp: '2025-07-20 06:26:01+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/mod/mfrac_cls.py
layout: document
redirect_from:
- /library/cp_library/math/mod/mfrac_cls.py
- /library/cp_library/math/mod/mfrac_cls.py.html
title: cp_library/math/mod/mfrac_cls.py
---
