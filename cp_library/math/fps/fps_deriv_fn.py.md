---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/mint_cls.py
    title: cp_library/math/mod/mint_cls.py
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/fps/fps_exp_fn.py
    title: cp_library/math/fps/fps_exp_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/fps/fps_log_fn.py
    title: cp_library/math/fps/fps_log_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/fps/fps_pow_fn.py
    title: cp_library/math/fps/fps_pow_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/table/stirling1_k_fn.py
    title: cp_library/math/table/stirling1_k_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/table/stirling2_k_fn.py
    title: cp_library/math/table/stirling2_k_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/enumerative-combinatorics/stirling_number_of_the_first_kind_fixed_k.test.py
    title: test/library-checker/enumerative-combinatorics/stirling_number_of_the_first_kind_fixed_k.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/enumerative-combinatorics/stirling_number_of_the_second_kind_fixed_k.test.py
    title: test/library-checker/enumerative-combinatorics/stirling_number_of_the_second_kind_fixed_k.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/polynomial/exp_of_formal_power_series.test.py
    title: test/library-checker/polynomial/exp_of_formal_power_series.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/polynomial/log_of_formal_power_series.test.py
    title: test/library-checker/polynomial/log_of_formal_power_series.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/polynomial/pow_of_formal_power_series.test.py
    title: test/library-checker/polynomial/pow_of_formal_power_series.test.py
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
    \ndef fps_deriv(P: list[int]):\n    mod = mint.mod\n    return [P[i]*i%mod for\
    \ i in range(1,len(P))]\n\n\n    \nclass mint(int):\n    mod: int\n    zero: 'mint'\n\
    \    one: 'mint'\n    two: 'mint'\n    cache: list['mint']\n\n    def __new__(cls,\
    \ *args, **kwargs):\n        if 0<= (x := int(*args, **kwargs)) <= 2:\n      \
    \      return cls.cache[x]\n        else:\n            return cls.fix(x)\n\n \
    \   @classmethod\n    def set_mod(cls, mod: int):\n        mint.mod = cls.mod\
    \ = mod\n        mint.zero = cls.zero = cls.cast(0)\n        mint.one = cls.one\
    \ = cls.fix(1)\n        mint.two = cls.two = cls.fix(2)\n        mint.cache =\
    \ cls.cache = [cls.zero, cls.one, cls.two]\n\n    @classmethod\n    def fix(cls,\
    \ x): return cls.cast(x%cls.mod)\n\n    @classmethod\n    def cast(cls, x): return\
    \ super().__new__(cls,x)\n\n    @classmethod\n    def mod_inv(cls, x):\n     \
    \   a,b,s,t = int(x), cls.mod, 1, 0\n        while b: a,b,s,t = b,a%b,t,s-a//b*t\n\
    \        if a == 1: return cls.fix(s)\n        raise ValueError(f\"{x} is not\
    \ invertible in mod {cls.mod}\")\n    \n    @property\n    def inv(self): return\
    \ mint.mod_inv(self)\n\n    def __add__(self, x): return mint.fix(super().__add__(x))\n\
    \    def __radd__(self, x): return mint.fix(super().__radd__(x))\n    def __sub__(self,\
    \ x): return mint.fix(super().__sub__(x))\n    def __rsub__(self, x): return mint.fix(super().__rsub__(x))\n\
    \    def __mul__(self, x): return mint.fix(super().__mul__(x))\n    def __rmul__(self,\
    \ x): return mint.fix(super().__rmul__(x))\n    def __floordiv__(self, x): return\
    \ self * mint.mod_inv(x)\n    def __rfloordiv__(self, x): return self.inv * x\n\
    \    def __truediv__(self, x): return self * mint.mod_inv(x)\n    def __rtruediv__(self,\
    \ x): return self.inv * x\n    def __pow__(self, x): \n        return self.cast(super().__pow__(x,\
    \ self.mod))\n    def __neg__(self): return mint.mod-self\n    def __pos__(self):\
    \ return self\n    def __abs__(self): return self\n"
  code: "import cp_library.math.fps.__header__\n\ndef fps_deriv(P: list[int]):\n \
    \   mod = mint.mod\n    return [P[i]*i%mod for i in range(1,len(P))]\n\nfrom cp_library.math.mod.mint_cls\
    \ import mint"
  dependsOn:
  - cp_library/math/mod/mint_cls.py
  isVerificationFile: false
  path: cp_library/math/fps/fps_deriv_fn.py
  requiredBy:
  - cp_library/math/table/stirling2_k_fn.py
  - cp_library/math/table/stirling1_k_fn.py
  - cp_library/math/fps/fps_log_fn.py
  - cp_library/math/fps/fps_pow_fn.py
  - cp_library/math/fps/fps_exp_fn.py
  timestamp: '2025-03-19 07:50:34+07:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/enumerative-combinatorics/stirling_number_of_the_first_kind_fixed_k.test.py
  - test/library-checker/enumerative-combinatorics/stirling_number_of_the_second_kind_fixed_k.test.py
  - test/library-checker/polynomial/log_of_formal_power_series.test.py
  - test/library-checker/polynomial/exp_of_formal_power_series.test.py
  - test/library-checker/polynomial/pow_of_formal_power_series.test.py
documentation_of: cp_library/math/fps/fps_deriv_fn.py
layout: document
redirect_from:
- /library/cp_library/math/fps/fps_deriv_fn.py
- /library/cp_library/math/fps/fps_deriv_fn.py.html
title: cp_library/math/fps/fps_deriv_fn.py
---
