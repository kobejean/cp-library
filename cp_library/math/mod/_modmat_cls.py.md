---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/mint_cls.py
    title: cp_library/math/mod/mint_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "from typing import Union, List, Tuple\n\nclass mint(int):\n    mod\
    \ = None\n    def __new__(cls, x=0): return super().__new__(cls, int(x) % cls.mod)\n\
    \    @classmethod\n    def wrap(cls, x): return super().__new__(cls, x % cls.mod)\n\
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
    \nimport array\n\nclass ModMat:\n    def __init__(s, r, c, v=0):\n        s.r,\
    \ s.c = r, c\n        s.d = array.array('q', [v] * (r * c) if isinstance(v, int)\
    \ else [x for row in v for x in row])\n\n    def __getitem__(s, k): return mint(s.d[k[0]*s.c\
    \ + k[1]])\n    def __setitem__(s, k, v): s.d[k[0]*s.c + k[1]] = v % mint.mod\n\
    \    def __str__(s): return '\\n'.join(' '.join(map(str, (mint(x) for x in s.d[i*s.c:(i+1)*s.c])))\
    \ for i in range(s.r))\n\n    def __add__(s, o):\n        d = (a+o for a in s.d)\
    \ if isinstance(o,int) else (a+b for a,b in zip(s.d, o.d))\n        return ModMat(s.r,\
    \ s.c, d)\n\n    def __matmul__(s, o):\n        if s.c != o.r: raise ValueError(\"\
    Dimension mismatch\")\n        r = ModMat(s.r, o.c)\n        for i in range(s.r):\n\
    \            i_sc = i * s.c\n            for j in range(o.c):\n              \
    \  r[i,j] = sum(s.d[i_sc+k]*o.d[k*o.c+j]%mint.mod for k in range(s.c))\n     \
    \   return r\n\n    @classmethod\n    def I(cls, n):\n        r = cls(n, n)\n\
    \        for i in range(n): r[i,i] = 1\n        return r\n\n"
  code: "from typing import Union, List, Tuple\nfrom cp_library.math.mod.mint_cls\
    \ import mint\n\nimport array\n\nclass ModMat:\n    def __init__(s, r, c, v=0):\n\
    \        s.r, s.c = r, c\n        s.d = array.array('q', [v] * (r * c) if isinstance(v,\
    \ int) else [x for row in v for x in row])\n\n    def __getitem__(s, k): return\
    \ mint(s.d[k[0]*s.c + k[1]])\n    def __setitem__(s, k, v): s.d[k[0]*s.c + k[1]]\
    \ = v % mint.mod\n    def __str__(s): return '\\n'.join(' '.join(map(str, (mint(x)\
    \ for x in s.d[i*s.c:(i+1)*s.c]))) for i in range(s.r))\n\n    def __add__(s,\
    \ o):\n        d = (a+o for a in s.d) if isinstance(o,int) else (a+b for a,b in\
    \ zip(s.d, o.d))\n        return ModMat(s.r, s.c, d)\n\n    def __matmul__(s,\
    \ o):\n        if s.c != o.r: raise ValueError(\"Dimension mismatch\")\n     \
    \   r = ModMat(s.r, o.c)\n        for i in range(s.r):\n            i_sc = i *\
    \ s.c\n            for j in range(o.c):\n                r[i,j] = sum(s.d[i_sc+k]*o.d[k*o.c+j]%mint.mod\
    \ for k in range(s.c))\n        return r\n\n    @classmethod\n    def I(cls, n):\n\
    \        r = cls(n, n)\n        for i in range(n): r[i,i] = 1\n        return\
    \ r\n\n"
  dependsOn:
  - cp_library/math/mod/mint_cls.py
  isVerificationFile: false
  path: cp_library/math/mod/_modmat_cls.py
  requiredBy: []
  timestamp: '2024-09-16 19:46:13+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/mod/_modmat_cls.py
layout: document
redirect_from:
- /library/cp_library/math/mod/_modmat_cls.py
- /library/cp_library/math/mod/_modmat_cls.py.html
title: cp_library/math/mod/_modmat_cls.py
---