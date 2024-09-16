---
data:
  _extendedDependsOn:
  - icon: ':question:'
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
    from itertools import accumulate\n\nclass mint(int):\n    mod = None\n    def\
    \ __new__(cls, x=0): return super().__new__(cls, int(x) % cls.mod)\n    @classmethod\n\
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
    \   res *= cls.comb(n, k)\n            n -= k\n        return res\nmint.mod =\
    \ 998244353\n\ndef read(shift=0, base=10):\n    return [int(s, base) + shift for\
    \ s in  input().split()]\n\nN, K = read()\nmint.precomp(N)\nS = input()\nA, B,\
    \ C = S.count('A'), S.count('B'), S.count('C')\n\n# x A <-> B\n# y B <-> C\n#\
    \ z C <-> A\n# w A -> B -> C -> A or A -> C -> B -> A \n\nans = mint()\nfor x\
    \ in range(K+1):\n    for y in range(K-x+1):\n        for z in range(K-x-y+1):\n\
    \            for w in range(((K-x-y-z)//2+1)):\n                cnt =   mint.multinom(A,x,z+w)\
    \ * \\\n                        mint.multinom(B,y,x+w) * \\\n                \
    \        mint.multinom(C,z,y+w)\n                if w > 0: cnt*=2\n          \
    \      ans += cnt\nprint(ans)\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/arc168/tasks/arc168_c\n\
    from cp_library.math.mod.mint_comb_cls import mint\nmint.mod = 998244353\nfrom\
    \ cp_library.io.read_int_fn import read\n\nN, K = read()\nmint.precomp(N)\nS =\
    \ input()\nA, B, C = S.count('A'), S.count('B'), S.count('C')\n\n# x A <-> B\n\
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
  timestamp: '2024-09-16 19:46:13+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/arc168_c_swap_characters_mint_comb.test.py
layout: document
redirect_from:
- /verify/test/arc168_c_swap_characters_mint_comb.test.py
- /verify/test/arc168_c_swap_characters_mint_comb.test.py.html
title: test/arc168_c_swap_characters_mint_comb.test.py
---
