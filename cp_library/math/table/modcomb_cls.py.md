---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/mint_cls.py
    title: cp_library/math/mod/mint_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/nt/mod_inv_fn.py
    title: cp_library/math/nt/mod_inv_fn.py
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/fps/fps_exp_fn.py
    title: cp_library/math/fps/fps_exp_fn.py
  - icon: ':warning:'
    path: cp_library/math/fps/fps_ideriv_k_fn.py
    title: cp_library/math/fps/fps_ideriv_k_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/fps/fps_pow_fn.py
    title: cp_library/math/fps/fps_pow_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/fps/fps_tayler_shift_fn.py
    title: cp_library/math/fps/fps_tayler_shift_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/table/stirling1_k_fn.py
    title: cp_library/math/table/stirling1_k_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/table/stirling1_n_fn.py
    title: cp_library/math/table/stirling1_n_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/table/stirling2_k_fn.py
    title: cp_library/math/table/stirling2_k_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/table/stirling2_n_fn.py
    title: cp_library/math/table/stirling2_n_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/arc/arc168_c_swap_characters_combinatoric.test.py
    title: test/atcoder/arc/arc168_c_swap_characters_combinatoric.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/enumerative-combinatorics/stirling_number_of_the_first_kind.test.py
    title: test/library-checker/enumerative-combinatorics/stirling_number_of_the_first_kind.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/enumerative-combinatorics/stirling_number_of_the_first_kind_fixed_k.test.py
    title: test/library-checker/enumerative-combinatorics/stirling_number_of_the_first_kind_fixed_k.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/enumerative-combinatorics/stirling_number_of_the_second_kind.test.py
    title: test/library-checker/enumerative-combinatorics/stirling_number_of_the_second_kind.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/enumerative-combinatorics/stirling_number_of_the_second_kind_fixed_k.test.py
    title: test/library-checker/enumerative-combinatorics/stirling_number_of_the_second_kind_fixed_k.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/polynomial/exp_of_formal_power_series.test.py
    title: test/library-checker/polynomial/exp_of_formal_power_series.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/polynomial/polynomial_taylor_shift.test.py
    title: test/library-checker/polynomial/polynomial_taylor_shift.test.py
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
    \n    \nclass mint(int):\n    mod: int\n    zero: 'mint'\n    one: 'mint'\n  \
    \  two: 'mint'\n    cache: list['mint']\n\n    def __new__(cls, *args, **kwargs):\n\
    \        if 0<= (x := int(*args, **kwargs)) <= 2:\n            return cls.cache[x]\n\
    \        else:\n            return cls.fix(x)\n\n    @classmethod\n    def set_mod(cls,\
    \ mod: int):\n        mint.mod = cls.mod = mod\n        mint.zero = cls.zero =\
    \ cls.cast(0)\n        mint.one = cls.one = cls.fix(1)\n        mint.two = cls.two\
    \ = cls.fix(2)\n        mint.cache = cls.cache = [cls.zero, cls.one, cls.two]\n\
    \n    @classmethod\n    def fix(cls, x): return cls.cast(x%cls.mod)\n\n    @classmethod\n\
    \    def cast(cls, x): return super().__new__(cls,x)\n\n    @classmethod\n   \
    \ def mod_inv(cls, x):\n        a,b,s,t = int(x), cls.mod, 1, 0\n        while\
    \ b: a,b,s,t = b,a%b,t,s-a//b*t\n        if a == 1: return cls.fix(s)\n      \
    \  raise ValueError(f\"{x} is not invertible in mod {cls.mod}\")\n    \n    @property\n\
    \    def inv(self): return mint.mod_inv(self)\n\n    def __add__(self, x): return\
    \ mint.fix(super().__add__(x))\n    def __radd__(self, x): return mint.fix(super().__radd__(x))\n\
    \    def __sub__(self, x): return mint.fix(super().__sub__(x))\n    def __rsub__(self,\
    \ x): return mint.fix(super().__rsub__(x))\n    def __mul__(self, x): return mint.fix(super().__mul__(x))\n\
    \    def __rmul__(self, x): return mint.fix(super().__rmul__(x))\n    def __floordiv__(self,\
    \ x): return self * mint.mod_inv(x)\n    def __rfloordiv__(self, x): return self.inv\
    \ * x\n    def __truediv__(self, x): return self * mint.mod_inv(x)\n    def __rtruediv__(self,\
    \ x): return self.inv * x\n    def __pow__(self, x): \n        return self.cast(super().__pow__(x,\
    \ self.mod))\n    def __neg__(self): return mint.mod-self\n    def __pos__(self):\
    \ return self\n    def __abs__(self): return self\n\n\ndef mod_inv(x, mod):\n\
    \    a,b,s,t = x, mod, 1, 0\n    while b:\n        a,b,s,t = b,a%b,t,s-a//b*t\n\
    \    if a == 1: return s % mod\n    raise ValueError(f\"{x} is not invertible\
    \ in mod {mod}\")\nfrom itertools import accumulate\n\nclass modcomb(list[mint]):\n\
    \    fact: list[int]\n    fact_inv: list[int]\n    inv: list[int] = [0,1]\n\n\
    \    @staticmethod\n    def precomp(N):\n        mod = mint.mod\n        def mod_mul(a,b):\
    \ return a*b%mod\n        fact = list(accumulate(range(1,N+1), mod_mul, initial=1))\n\
    \        fact_inv = list(accumulate(range(N,0,-1), mod_mul, initial=mod_inv(fact[N],\
    \ mod)))\n        fact_inv.reverse()\n        modcomb.fact, modcomb.fact_inv =\
    \ fact, fact_inv\n    \n    @staticmethod\n    def extend_inv(N):\n        N,\
    \ inv, mod = N+1, modcomb.inv, mint.mod\n        while len(inv) < N:\n       \
    \     j, k = divmod(mod, len(inv))\n            inv.append(-inv[k] * j % mod)\n\
    \n    @staticmethod\n    def comb(n: int, k: int, /) -> mint:\n        inv, mod\
    \ = modcomb.fact_inv, mint.mod\n        if n < k: return mint.zero\n        return\
    \ mint(inv[k] * inv[n-k] % mod * modcomb.fact[n])\n    nCk = binom = comb\n  \
    \  \n    @staticmethod\n    def comb_with_replacement(n: int, k: int, /) -> mint:\n\
    \        if n <= 0: return mint.zero\n        return modcomb.nCk(n + k - 1, k)\n\
    \    nHk = comb_with_replacement\n    \n    @staticmethod\n    def multinom(n:\
    \ int, *K: int) -> mint:\n        nCk, res = modcomb.nCk, mint.one\n        for\
    \ k in K: res, n = res*nCk(n,k), n-k\n        return res\n\n    @staticmethod\n\
    \    def perm(n: int, k: int, /) -> mint:\n        \"\"\"Returns P(n,k) mod p\"\
    \"\"\n        if n < k: return mint.zero\n        return mint(modcomb.fact[n]\
    \ * modcomb.fact_inv[n-k])\n    nPk = perm\n    \n    @staticmethod\n    def catalan(n:\
    \ int, /) -> mint:\n        return mint(modcomb.nCk(2*n,n) * modcomb.fact_inv[n+1])\n"
  code: "import cp_library.math.table.__header__\nfrom cp_library.math.mod.mint_cls\
    \ import mint\nfrom cp_library.math.nt.mod_inv_fn import mod_inv\nfrom itertools\
    \ import accumulate\n\nclass modcomb(list[mint]):\n    fact: list[int]\n    fact_inv:\
    \ list[int]\n    inv: list[int] = [0,1]\n\n    @staticmethod\n    def precomp(N):\n\
    \        mod = mint.mod\n        def mod_mul(a,b): return a*b%mod\n        fact\
    \ = list(accumulate(range(1,N+1), mod_mul, initial=1))\n        fact_inv = list(accumulate(range(N,0,-1),\
    \ mod_mul, initial=mod_inv(fact[N], mod)))\n        fact_inv.reverse()\n     \
    \   modcomb.fact, modcomb.fact_inv = fact, fact_inv\n    \n    @staticmethod\n\
    \    def extend_inv(N):\n        N, inv, mod = N+1, modcomb.inv, mint.mod\n  \
    \      while len(inv) < N:\n            j, k = divmod(mod, len(inv))\n       \
    \     inv.append(-inv[k] * j % mod)\n\n    @staticmethod\n    def comb(n: int,\
    \ k: int, /) -> mint:\n        inv, mod = modcomb.fact_inv, mint.mod\n       \
    \ if n < k: return mint.zero\n        return mint(inv[k] * inv[n-k] % mod * modcomb.fact[n])\n\
    \    nCk = binom = comb\n    \n    @staticmethod\n    def comb_with_replacement(n:\
    \ int, k: int, /) -> mint:\n        if n <= 0: return mint.zero\n        return\
    \ modcomb.nCk(n + k - 1, k)\n    nHk = comb_with_replacement\n    \n    @staticmethod\n\
    \    def multinom(n: int, *K: int) -> mint:\n        nCk, res = modcomb.nCk, mint.one\n\
    \        for k in K: res, n = res*nCk(n,k), n-k\n        return res\n\n    @staticmethod\n\
    \    def perm(n: int, k: int, /) -> mint:\n        \"\"\"Returns P(n,k) mod p\"\
    \"\"\n        if n < k: return mint.zero\n        return mint(modcomb.fact[n]\
    \ * modcomb.fact_inv[n-k])\n    nPk = perm\n    \n    @staticmethod\n    def catalan(n:\
    \ int, /) -> mint:\n        return mint(modcomb.nCk(2*n,n) * modcomb.fact_inv[n+1])\n"
  dependsOn:
  - cp_library/math/mod/mint_cls.py
  - cp_library/math/nt/mod_inv_fn.py
  isVerificationFile: false
  path: cp_library/math/table/modcomb_cls.py
  requiredBy:
  - cp_library/math/table/stirling2_k_fn.py
  - cp_library/math/table/stirling1_k_fn.py
  - cp_library/math/table/stirling2_n_fn.py
  - cp_library/math/table/stirling1_n_fn.py
  - cp_library/math/fps/fps_exp_fn.py
  - cp_library/math/fps/fps_ideriv_k_fn.py
  - cp_library/math/fps/fps_tayler_shift_fn.py
  - cp_library/math/fps/fps_pow_fn.py
  timestamp: '2024-12-26 11:51:13+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/arc/arc168_c_swap_characters_combinatoric.test.py
  - test/library-checker/enumerative-combinatorics/stirling_number_of_the_second_kind.test.py
  - test/library-checker/enumerative-combinatorics/stirling_number_of_the_second_kind_fixed_k.test.py
  - test/library-checker/enumerative-combinatorics/stirling_number_of_the_first_kind.test.py
  - test/library-checker/enumerative-combinatorics/stirling_number_of_the_first_kind_fixed_k.test.py
  - test/library-checker/polynomial/pow_of_formal_power_series.test.py
  - test/library-checker/polynomial/exp_of_formal_power_series.test.py
  - test/library-checker/polynomial/polynomial_taylor_shift.test.py
documentation_of: cp_library/math/table/modcomb_cls.py
layout: document
redirect_from:
- /library/cp_library/math/table/modcomb_cls.py
- /library/cp_library/math/table/modcomb_cls.py.html
title: cp_library/math/table/modcomb_cls.py
---
