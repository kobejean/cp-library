---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/mint_cls.py
    title: cp_library/math/mod/mint_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/arc168_c_swap_characters_combinatoric.test.py
    title: test/arc168_c_swap_characters_combinatoric.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2578\n             https://kobejean.github.io/cp-library             \
    \  \n'''\n\nclass mint(int):\n    mod = zero = one = two = None\n\n    def __new__(cls,\
    \ *args, **kwargs):\n        match int(*args, **kwargs):\n            case 0:\
    \ return cls.zero\n            case 1: return cls.one\n            case 2: return\
    \ cls.two\n            case x: return cls.fix(x)\n\n    @classmethod\n    def\
    \ set_mod(cls, mod):\n        cls.mod = mod\n        cls.zero = cls.cast(0)\n\
    \        cls.one = cls.fix(1)\n        cls.two = cls.fix(2)\n\n    @classmethod\n\
    \    def fix(cls, x): return cls.cast(x%cls.mod)\n\n    @classmethod\n    def\
    \ cast(cls, x): return super().__new__(cls,x)\n\n    @classmethod\n    def mod_inv(cls,\
    \ x):\n        a,b,s,t = int(x), cls.mod, 1, 0\n        while b: a,b,s,t = b,a%b,t,s-a//b*t\n\
    \        if a == 1: return cls.fix(s)\n        raise ValueError(f\"{x} is not\
    \ invertible\")\n    \n    @property\n    def inv(self): return mint.mod_inv(self)\n\
    \n    def __add__(self, x): return mint.fix(super().__add__(x))\n    def __radd__(self,\
    \ x): return mint.fix(super().__radd__(x))\n    def __sub__(self, x): return mint.fix(super().__sub__(x))\n\
    \    def __rsub__(self, x): return mint.fix(super().__rsub__(x))\n    def __mul__(self,\
    \ x): return mint.fix(super().__mul__(x))\n    def __rmul__(self, x): return mint.fix(super().__rmul__(x))\n\
    \    def __floordiv__(self, x): return self * mint.mod_inv(x)\n    def __rfloordiv__(self,\
    \ x): return self.inv * x\n    def __truediv__(self, x): return self * mint.mod_inv(x)\n\
    \    def __rtruediv__(self, x): return self.inv * x\n    def __pow__(self, x):\
    \ \n        return self.cast(super().__pow__(x, self.mod))\n    def __neg__(self):\
    \ return mint.mod-self\n    def __pos__(self): return self\n    def __abs__(self):\
    \ return self\n\n\nfrom itertools import accumulate\n\nclass Combinatorics(list[mint]):\n\
    \    def __init__(table, N: int):\n        super().__init__(accumulate(range(1,N+1),\
    \ mint.__mul__, initial=mint.one))\n        table.inv = list(accumulate(\n   \
    \         range(N,0,-1), mint.__mul__, initial=table[N].inv\n        ))[::-1]\n\
    \        \n        \n    def combinations(table, n: int, k: int, /) -> mint:\n\
    \        if n < k: return mint.zero\n        return table[n] * table.inv[k] *\
    \ table.inv[n - k]\n    \n    nCk = combinations\n    \n    def combinations_with_replacement(table,\
    \ n: int, k: int, /) -> mint:\n        if n <= 0: return mint.zero\n        return\
    \ table.nCk(n + k - 1, k)\n    \n    nHk = combinations\n    \n    def factorial(table,\
    \ n: int, /) -> mint:\n        return table[n]\n    \n    def multinomial(self,\
    \ n: int, *K: int) -> mint:\n        res = mint.one\n        for k in K:\n   \
    \         res *= self.nCk(n, k)\n            n -= k\n        return res\n\n  \
    \  def perm(table, n: int, k: int, /) -> mint:\n        \"\"\"Returns P(n,k) mod\
    \ p\"\"\"\n        if n < k: return mint.zero\n        return table[n] * table.inv[n\
    \ - k]\n    \n    nPk = perm\n\n    \n    def catalan(table, n: int, /) -> mint:\n\
    \        return table.nCk(2 * n, n) * table.inv[n + 1]\n \n"
  code: "\nfrom cp_library.math.mod.mint_cls import mint\n\nfrom itertools import\
    \ accumulate\n\nclass Combinatorics(list[mint]):\n    def __init__(table, N: int):\n\
    \        super().__init__(accumulate(range(1,N+1), mint.__mul__, initial=mint.one))\n\
    \        table.inv = list(accumulate(\n            range(N,0,-1), mint.__mul__,\
    \ initial=table[N].inv\n        ))[::-1]\n        \n        \n    def combinations(table,\
    \ n: int, k: int, /) -> mint:\n        if n < k: return mint.zero\n        return\
    \ table[n] * table.inv[k] * table.inv[n - k]\n    \n    nCk = combinations\n \
    \   \n    def combinations_with_replacement(table, n: int, k: int, /) -> mint:\n\
    \        if n <= 0: return mint.zero\n        return table.nCk(n + k - 1, k)\n\
    \    \n    nHk = combinations\n    \n    def factorial(table, n: int, /) -> mint:\n\
    \        return table[n]\n    \n    def multinomial(self, n: int, *K: int) ->\
    \ mint:\n        res = mint.one\n        for k in K:\n            res *= self.nCk(n,\
    \ k)\n            n -= k\n        return res\n\n    def perm(table, n: int, k:\
    \ int, /) -> mint:\n        \"\"\"Returns P(n,k) mod p\"\"\"\n        if n < k:\
    \ return mint.zero\n        return table[n] * table.inv[n - k]\n    \n    nPk\
    \ = perm\n\n    \n    def catalan(table, n: int, /) -> mint:\n        return table.nCk(2\
    \ * n, n) * table.inv[n + 1]\n \n"
  dependsOn:
  - cp_library/math/mod/mint_cls.py
  isVerificationFile: false
  path: cp_library/math/table/combinatorics_cls.py
  requiredBy: []
  timestamp: '2024-11-28 18:07:28+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/arc168_c_swap_characters_combinatoric.test.py
documentation_of: cp_library/math/table/combinatorics_cls.py
layout: document
redirect_from:
- /library/cp_library/math/table/combinatorics_cls.py
- /library/cp_library/math/table/combinatorics_cls.py.html
title: cp_library/math/table/combinatorics_cls.py
---
