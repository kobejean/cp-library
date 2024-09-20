---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_int_fn.py
    title: cp_library/io/read_int_fn.py
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
    '''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n   \
    \          https://kobejean.github.io/cp-library               \n'''\nfrom itertools\
    \ import accumulate\n\nclass mint(int):\n    mod = zero = one = None\n\n    def\
    \ __new__(cls, *args, **kwargs):\n        match int(*args, **kwargs):\n      \
    \      case 0: return cls.zero\n            case 1: return cls.one\n         \
    \   case x: return cls.fix(x)\n\n    @classmethod\n    def set_mod(cls, mod):\n\
    \        cls.mod = mod\n        cls.zero, cls.one = cls.cast(0), cls.fix(1)\n\n\
    \    @classmethod\n    def fix(cls, x): return cls.cast(x%cls.mod)\n\n    @classmethod\n\
    \    def cast(cls, x): return super().__new__(cls,x)\n\n    @classmethod\n   \
    \ def mod_inv(cls, x):\n        a,b,s,t = int(x), cls.mod, 1, 0\n        while\
    \ b: a,b,s,t = b,a%b,t,s-a//b*t\n        if a == 1: return cls.fix(s)\n      \
    \  raise ValueError(f\"{x} is not invertible\")\n    \n    @property\n    def\
    \ inv(self): return mint.mod_inv(self)\n\n    def __add__(self, x): return mint.fix(super().__add__(x))\n\
    \    def __radd__(self, x): return mint.fix(super().__radd__(x))\n    def __sub__(self,\
    \ x): return mint.fix(super().__sub__(x))\n    def __rsub__(self, x): return mint.fix(super().__rsub__(x))\n\
    \    def __mul__(self, x): return mint.fix(super().__mul__(x))\n    def __rmul__(self,\
    \ x): return mint.fix(super().__rmul__(x))\n    def __floordiv__(self, x): return\
    \ self * mint.mod_inv(x)\n    def __rfloordiv__(self, x): return self.inv * x\n\
    \    def __truediv__(self, x): return self * mint.mod_inv(x)\n    def __rtruediv__(self,\
    \ x): return self.inv * x\n    def __pow__(self, x): \n        return self.cast(super().__pow__(x,\
    \ self.mod))\n    def __eq__(self, x): return super().__eq__(self-x, 0)\n    def\
    \ __neg__(self): return mint.mod-self\n    def __pos__(self): return self\n  \
    \  def __abs__(self): return self\n\n    @classmethod\n    def precomp(cls,n):\n\
    \        cls.fac = list(accumulate(\n            range(1,n+1), cls.__mul__, initial=cls(1)))\n\
    \        cls.finv = list(accumulate(\n            range(n,0,-1), cls.__mul__,\
    \ initial=cls.fac[n].inv))[::-1]\n        \n    @classmethod\n    def comb(cls,\
    \ n, k, /):\n        if n < k: return 0\n        return cls.fac[n]*cls.finv[k]*cls.finv[n\
    \ - k]\n    \n    @classmethod\n    def multinom(cls, n, *K):\n        res = cls(1)\n\
    \        for k in K:\n            res *= cls.comb(n, k)\n            n -= k\n\
    \        return res\nmint.set_mod(998244353)\n\n\ndef read(shift=0, base=10):\n\
    \    return [int(s, base) + shift for s in input().split()]\n\nN, K = read()\n\
    mint.precomp(N)\nS = input()\nA, B, C = S.count('A'), S.count('B'), S.count('C')\n\
    \n# x A <-> B\n# y B <-> C\n# z C <-> A\n# w A -> B -> C -> A or A -> C -> B ->\
    \ A \n\nans = mint()\nfor x in range(K+1):\n    for y in range(K-x+1):\n     \
    \   for z in range(K-x-y+1):\n            for w in range(((K-x-y-z)//2+1)):\n\
    \                cnt =   mint.multinom(A,x,z+w) * \\\n                       \
    \ mint.multinom(B,y,x+w) * \\\n                        mint.multinom(C,z,y+w)\n\
    \                if w > 0: cnt*=2\n                ans += cnt\nprint(ans)\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/arc168/tasks/arc168_c\n\
    from cp_library.math.mod.mint_comb_cls import mint\nmint.set_mod(998244353)\n\
    from cp_library.io.read_int_fn import read\n\nN, K = read()\nmint.precomp(N)\n\
    S = input()\nA, B, C = S.count('A'), S.count('B'), S.count('C')\n\n# x A <-> B\n\
    # y B <-> C\n# z C <-> A\n# w A -> B -> C -> A or A -> C -> B -> A \n\nans = mint()\n\
    for x in range(K+1):\n    for y in range(K-x+1):\n        for z in range(K-x-y+1):\n\
    \            for w in range(((K-x-y-z)//2+1)):\n                cnt =   mint.multinom(A,x,z+w)\
    \ * \\\n                        mint.multinom(B,y,x+w) * \\\n                \
    \        mint.multinom(C,z,y+w)\n                if w > 0: cnt*=2\n          \
    \      ans += cnt\nprint(ans)\n"
  dependsOn:
  - cp_library/math/mod/mint_comb_cls.py
  - cp_library/io/read_int_fn.py
  isVerificationFile: true
  path: test/arc168_c_swap_characters_mint_comb.test.py
  requiredBy: []
  timestamp: '2024-09-21 04:14:27+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/arc168_c_swap_characters_mint_comb.test.py
layout: document
redirect_from:
- /verify/test/arc168_c_swap_characters_mint_comb.test.py
- /verify/test/arc168_c_swap_characters_mint_comb.test.py.html
title: test/arc168_c_swap_characters_mint_comb.test.py
---
