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
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    from typing import Union, List, Tuple\n\nclass mint(int):\n    mod = zero = one\
    \ = None\n\n    def __new__(cls, *args, **kwargs):\n        match int(*args, **kwargs):\n\
    \            case 0: return cls.zero\n            case 1: return cls.one\n   \
    \         case x: return cls.fix(x)\n\n    @classmethod\n    def set_mod(cls,\
    \ mod):\n        cls.mod = mod\n        cls.zero, cls.one = cls.cast(0), cls.fix(1)\n\
    \n    @classmethod\n    def fix(cls, x): return cls.cast(x%cls.mod)\n\n    @classmethod\n\
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
    \  def __abs__(self): return self\n\n\nimport array\n\nclass ModMat:\n    def\
    \ __init__(s, r, c, v=0):\n        s.r, s.c = r, c\n        s.d = array.array('q',\
    \ [v] * (r * c) if isinstance(v, int) else [x for row in v for x in row])\n\n\
    \    def __getitem__(s, k): return mint(s.d[k[0]*s.c + k[1]])\n    def __setitem__(s,\
    \ k, v): s.d[k[0]*s.c + k[1]] = v % mint.mod\n    def __str__(s): return '\\n'.join('\
    \ '.join(map(str, (mint(x) for x in s.d[i*s.c:(i+1)*s.c]))) for i in range(s.r))\n\
    \n    def __add__(s, o):\n        d = (a+o for a in s.d) if isinstance(o,int)\
    \ else (a+b for a,b in zip(s.d, o.d))\n        return ModMat(s.r, s.c, d)\n\n\
    \    def __matmul__(s, o):\n        if s.c != o.r: raise ValueError(\"Dimension\
    \ mismatch\")\n        r = ModMat(s.r, o.c)\n        for i in range(s.r):\n  \
    \          i_sc = i * s.c\n            for j in range(o.c):\n                r[i,j]\
    \ = sum(s.d[i_sc+k]*o.d[k*o.c+j]%mint.mod for k in range(s.c))\n        return\
    \ r\n\n    @classmethod\n    def I(cls, n):\n        r = cls(n, n)\n        for\
    \ i in range(n): r[i,i] = 1\n        return r\n\n"
  code: "import cp_library.math.mod.__init__\nfrom typing import Union, List, Tuple\n\
    from cp_library.math.mod.mint_cls import mint\n\nimport array\n\nclass ModMat:\n\
    \    def __init__(s, r, c, v=0):\n        s.r, s.c = r, c\n        s.d = array.array('q',\
    \ [v] * (r * c) if isinstance(v, int) else [x for row in v for x in row])\n\n\
    \    def __getitem__(s, k): return mint(s.d[k[0]*s.c + k[1]])\n    def __setitem__(s,\
    \ k, v): s.d[k[0]*s.c + k[1]] = v % mint.mod\n    def __str__(s): return '\\n'.join('\
    \ '.join(map(str, (mint(x) for x in s.d[i*s.c:(i+1)*s.c]))) for i in range(s.r))\n\
    \n    def __add__(s, o):\n        d = (a+o for a in s.d) if isinstance(o,int)\
    \ else (a+b for a,b in zip(s.d, o.d))\n        return ModMat(s.r, s.c, d)\n\n\
    \    def __matmul__(s, o):\n        if s.c != o.r: raise ValueError(\"Dimension\
    \ mismatch\")\n        r = ModMat(s.r, o.c)\n        for i in range(s.r):\n  \
    \          i_sc = i * s.c\n            for j in range(o.c):\n                r[i,j]\
    \ = sum(s.d[i_sc+k]*o.d[k*o.c+j]%mint.mod for k in range(s.c))\n        return\
    \ r\n\n    @classmethod\n    def I(cls, n):\n        r = cls(n, n)\n        for\
    \ i in range(n): r[i,i] = 1\n        return r\n\n"
  dependsOn:
  - cp_library/math/mod/mint_cls.py
  isVerificationFile: false
  path: cp_library/math/mod/_modmat_cls.py
  requiredBy: []
  timestamp: '2024-09-20 02:31:14+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/mod/_modmat_cls.py
layout: document
redirect_from:
- /library/cp_library/math/mod/_modmat_cls.py
- /library/cp_library/math/mod/_modmat_cls.py.html
title: cp_library/math/mod/_modmat_cls.py
---
