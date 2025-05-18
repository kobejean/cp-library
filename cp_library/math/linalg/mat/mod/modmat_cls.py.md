---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/mint_cls.py
    title: cp_library/math/mod/mint_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/linear-algebra/pow_of_matrix_modmat.test.py
    title: test/library-checker/linear-algebra/pow_of_matrix_modmat.test.py
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
    from typing import Union, List, Tuple\n    \nclass mint(int):\n    mod: int\n\
    \    zero: 'mint'\n    one: 'mint'\n    two: 'mint'\n    cache: list['mint']\n\
    \n    def __new__(cls, *args, **kwargs):\n        if 0 <= (x := int(*args, **kwargs))\
    \ < 64:\n            return cls.cache[x]\n        else:\n            return cls.fix(x)\n\
    \n    @classmethod\n    def set_mod(cls, mod: int):\n        mint.mod = cls.mod\
    \ = mod\n        mint.zero = cls.zero = cls.cast(0)\n        mint.one = cls.one\
    \ = cls.fix(1)\n        mint.two = cls.two = cls.fix(2)\n        mint.cache =\
    \ cls.cache = [cls.zero, cls.one, cls.two]\n        for x in range(3,64): mint.cache.append(cls.fix(x))\n\
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
    \ return self\n    def __abs__(self): return self\n    def __class_getitem__(self,\
    \ x: int): return self.cache[x]\n\nclass ModMat:\n    __slots__ = 'data', 'R',\
    \ 'C'\n\n    def __init__(self, data: List[Union[int,mint]]):\n        self.data,\
    \ self.R, self.C = data, len(data), len(data[0])\n    \n    @classmethod\n   \
    \ def identity(cls, N) -> 'ModMat': return ModMat([[int(i==j) for j in range(N)]\
    \ for i in range(N)])\n    \n    @classmethod\n    def zeros(cls, R, C) -> 'ModMat':\
    \ return ModMat([[0]*C for _ in range(R)])\n\n    def inv(self) -> 'ModMat':\n\
    \        assert self.R != self.C\n        \n        N = self.R\n        A = [row[:]\
    \ for row in self.data]\n        I = [[int(i==j) for j in range(N)] for i in range(N)]\n\
    \        \n        for i in range(N):\n            if A[i][i] == 0:\n        \
    \        for j in range(i+1, N):\n                    if A[j][i] != 0:\n     \
    \                   A[i], A[j] = A[j], A[i]\n                        I[i], I[j]\
    \ = I[j], I[i]\n                        break\n                else:\n       \
    \             raise ValueError(\"Matrix is not invertible\")\n            \n \
    \           inv = pow(A[i][i], -1, mint.mod)\n            for j in range(N):\n\
    \                A[i][j] = (A[i][j] * inv) % mint.mod\n                I[i][j]\
    \ = (I[i][j] * inv) % mint.mod\n            \n            for j in range(N):\n\
    \                if i != j:\n                    factor = A[j][i]\n          \
    \          for k in range(N):\n                        A[j][k] = (A[j][k] - factor\
    \ * A[i][k]) % mint.mod\n                        I[j][k] = (I[j][k] - factor *\
    \ I[i][k]) % mint.mod\n        \n        return ModMat(I)\n    \n    def T(self)\
    \ -> 'ModMat': return ModMat(list(map(list,zip(*self.data))))\n\n    def elem_wise(self,\
    \ func, other):\n        if isinstance(other, ModMat):\n            return ModMat([[func(a,b)\
    \ for a,b in zip(Ai,Bi)] for Ai,Bi in zip(self.data,other.data)])\n        elif\
    \ isinstance(other, int):\n            return ModMat([[func(a,other) for a in\
    \ Ai] for Ai in self.data])\n        else:\n            return NotImplemented\n\
    \        \n    def __str__(self): return '\\n'.join(' '.join(map(str,row)) for\
    \ row in self.data)\n    def __iter__(self): return self.data\n    def __copy__(self):\
    \ return ModMat([row[:] for row in self.data])\n    def copy(self): return ModMat([row[:]\
    \ for row in self.data])\n    def __add__(self, other): return self.elem_wise(lambda\
    \ a,b: (a+b) % mint.mod, other)\n    def __radd__(self, other): return self.__add__(other)\n\
    \    def __sub__(self, other): return self.elem_wise(lambda a,b: (a-b) % mint.mod,\
    \ other)\n    def __rsub__(self, other): return self.__sub__(other)\n    def __mul__(self,\
    \ other): return self.elem_wise(lambda a,b: (a*b) % mint.mod, other)\n    def\
    \ __rmul__(self, other): return self.__mul__(other)\n    def __truediv__(self,\
    \ other): return self.elem_wise(lambda a,b: a*pow(b,-1,mint.mod) % mint.mod, other)\n\
    \    def __rtruediv__(self, other): return self.elem_wise(lambda a,b: pow(a,-1,mint.mod)*b\
    \ % mint.mod, other)\n    \n    def __matmul__(self, other: 'ModMat'):\n     \
    \   assert self.C == other.R\n        R = [[0]*other.C for _ in range(self.R)]\n\
    \        for i,Ri in enumerate(R):\n            for k,Aik in enumerate(self.data[i]):\n\
    \                for j,Bkj in enumerate(other.data[k]):\n                    Ri[j]\
    \ = (Ri[j] + Aik*Bkj) % mint.mod\n        return ModMat(R)\n    \n    def __pow__(self,\
    \ K):\n        assert isinstance(K,int)\n        assert self.R == self.C\n   \
    \     A = self.copy()\n        R = A if K & 1 else ModMat.identity(self.R)\n \
    \       for i in range(1,K.bit_length()):\n            A @= A \n            if\
    \ K >> i & 1:\n                R @= A \n        return R\n    \n    def __getitem__(self,\
    \ key: Union[int, Tuple[int, int], slice, Tuple[slice, slice]]):\n        if isinstance(key,\
    \ int):\n            return self.data[key]\n        elif isinstance(key, tuple):\n\
    \            if len(key) == 2:\n                if all(isinstance(k, int) for\
    \ k in key):\n                    return mint(self.data[key[0]][key[1]])\n   \
    \             elif all(isinstance(k, slice) for k in key):\n                 \
    \   return ModMat([[self.data[i][j] for j in range(*key[1].indices(self.C))] \n\
    \                                   for i in range(*key[0].indices(self.R))])\n\
    \            raise IndexError(\"Invalid index\")\n        elif isinstance(key,\
    \ slice):\n            return ModMat([row[:] for row in self.data[key]])\n   \
    \     raise IndexError(\"Invalid index\")\n\n    def __setitem__(self, key: Union[Tuple[int,\
    \ int], slice, Tuple[slice, slice]], value):\n        if isinstance(key, tuple):\n\
    \            if len(key) == 2:\n                if all(isinstance(k, int) for\
    \ k in key):\n                    self.data[key[0]][key[1]] = value % mint.mod\n\
    \                elif all(isinstance(k, slice) for k in key):\n              \
    \      if isinstance(value, ModMat):\n                        for i, row in enumerate(range(*key[0].indices(self.R))):\n\
    \                            for j, col in enumerate(range(*key[1].indices(self.C))):\n\
    \                                self.data[row][col] = value.data[i][j] % mint.mod\n\
    \                    else:\n                        for row in range(*key[0].indices(self.R)):\n\
    \                            for col in range(*key[1].indices(self.C)):\n    \
    \                            self.data[row][col] = value % mint.mod\n        \
    \        else:\n                    raise IndexError(\"Invalid index\")\n    \
    \        else:\n                raise IndexError(\"Invalid index\")\n        elif\
    \ isinstance(key, slice):\n            if isinstance(value, ModMat):\n       \
    \         for i, row in enumerate(range(*key.indices(self.R))):\n            \
    \        self.data[row] = [v % mint.mod for v in value.data[i]]\n            else:\n\
    \                for row in range(*key.indices(self.R)):\n                   \
    \ self.data[row] = [value % mint.mod] * self.C\n        else:\n            raise\
    \ IndexError(\"Invalid index\")\n\n    def __delitem__(self, key: Union[int, slice]):\n\
    \        if isinstance(key, (int, slice)):\n            del self.data[key]\n \
    \           self.R = len(self.data)\n            if self.R == 0:\n           \
    \     self.C = 0\n        else:\n            raise IndexError(\"Invalid index\"\
    )\n\n    \n"
  code: "import cp_library.math.mod.__header__\nfrom typing import Union, List, Tuple\n\
    from cp_library.math.mod.mint_cls import mint\n\nclass ModMat:\n    __slots__\
    \ = 'data', 'R', 'C'\n\n    def __init__(self, data: List[Union[int,mint]]):\n\
    \        self.data, self.R, self.C = data, len(data), len(data[0])\n    \n   \
    \ @classmethod\n    def identity(cls, N) -> 'ModMat': return ModMat([[int(i==j)\
    \ for j in range(N)] for i in range(N)])\n    \n    @classmethod\n    def zeros(cls,\
    \ R, C) -> 'ModMat': return ModMat([[0]*C for _ in range(R)])\n\n    def inv(self)\
    \ -> 'ModMat':\n        assert self.R != self.C\n        \n        N = self.R\n\
    \        A = [row[:] for row in self.data]\n        I = [[int(i==j) for j in range(N)]\
    \ for i in range(N)]\n        \n        for i in range(N):\n            if A[i][i]\
    \ == 0:\n                for j in range(i+1, N):\n                    if A[j][i]\
    \ != 0:\n                        A[i], A[j] = A[j], A[i]\n                   \
    \     I[i], I[j] = I[j], I[i]\n                        break\n               \
    \ else:\n                    raise ValueError(\"Matrix is not invertible\")\n\
    \            \n            inv = pow(A[i][i], -1, mint.mod)\n            for j\
    \ in range(N):\n                A[i][j] = (A[i][j] * inv) % mint.mod\n       \
    \         I[i][j] = (I[i][j] * inv) % mint.mod\n            \n            for\
    \ j in range(N):\n                if i != j:\n                    factor = A[j][i]\n\
    \                    for k in range(N):\n                        A[j][k] = (A[j][k]\
    \ - factor * A[i][k]) % mint.mod\n                        I[j][k] = (I[j][k] -\
    \ factor * I[i][k]) % mint.mod\n        \n        return ModMat(I)\n    \n   \
    \ def T(self) -> 'ModMat': return ModMat(list(map(list,zip(*self.data))))\n\n\
    \    def elem_wise(self, func, other):\n        if isinstance(other, ModMat):\n\
    \            return ModMat([[func(a,b) for a,b in zip(Ai,Bi)] for Ai,Bi in zip(self.data,other.data)])\n\
    \        elif isinstance(other, int):\n            return ModMat([[func(a,other)\
    \ for a in Ai] for Ai in self.data])\n        else:\n            return NotImplemented\n\
    \        \n    def __str__(self): return '\\n'.join(' '.join(map(str,row)) for\
    \ row in self.data)\n    def __iter__(self): return self.data\n    def __copy__(self):\
    \ return ModMat([row[:] for row in self.data])\n    def copy(self): return ModMat([row[:]\
    \ for row in self.data])\n    def __add__(self, other): return self.elem_wise(lambda\
    \ a,b: (a+b) % mint.mod, other)\n    def __radd__(self, other): return self.__add__(other)\n\
    \    def __sub__(self, other): return self.elem_wise(lambda a,b: (a-b) % mint.mod,\
    \ other)\n    def __rsub__(self, other): return self.__sub__(other)\n    def __mul__(self,\
    \ other): return self.elem_wise(lambda a,b: (a*b) % mint.mod, other)\n    def\
    \ __rmul__(self, other): return self.__mul__(other)\n    def __truediv__(self,\
    \ other): return self.elem_wise(lambda a,b: a*pow(b,-1,mint.mod) % mint.mod, other)\n\
    \    def __rtruediv__(self, other): return self.elem_wise(lambda a,b: pow(a,-1,mint.mod)*b\
    \ % mint.mod, other)\n    \n    def __matmul__(self, other: 'ModMat'):\n     \
    \   assert self.C == other.R\n        R = [[0]*other.C for _ in range(self.R)]\n\
    \        for i,Ri in enumerate(R):\n            for k,Aik in enumerate(self.data[i]):\n\
    \                for j,Bkj in enumerate(other.data[k]):\n                    Ri[j]\
    \ = (Ri[j] + Aik*Bkj) % mint.mod\n        return ModMat(R)\n    \n    def __pow__(self,\
    \ K):\n        assert isinstance(K,int)\n        assert self.R == self.C\n   \
    \     A = self.copy()\n        R = A if K & 1 else ModMat.identity(self.R)\n \
    \       for i in range(1,K.bit_length()):\n            A @= A \n            if\
    \ K >> i & 1:\n                R @= A \n        return R\n    \n    def __getitem__(self,\
    \ key: Union[int, Tuple[int, int], slice, Tuple[slice, slice]]):\n        if isinstance(key,\
    \ int):\n            return self.data[key]\n        elif isinstance(key, tuple):\n\
    \            if len(key) == 2:\n                if all(isinstance(k, int) for\
    \ k in key):\n                    return mint(self.data[key[0]][key[1]])\n   \
    \             elif all(isinstance(k, slice) for k in key):\n                 \
    \   return ModMat([[self.data[i][j] for j in range(*key[1].indices(self.C))] \n\
    \                                   for i in range(*key[0].indices(self.R))])\n\
    \            raise IndexError(\"Invalid index\")\n        elif isinstance(key,\
    \ slice):\n            return ModMat([row[:] for row in self.data[key]])\n   \
    \     raise IndexError(\"Invalid index\")\n\n    def __setitem__(self, key: Union[Tuple[int,\
    \ int], slice, Tuple[slice, slice]], value):\n        if isinstance(key, tuple):\n\
    \            if len(key) == 2:\n                if all(isinstance(k, int) for\
    \ k in key):\n                    self.data[key[0]][key[1]] = value % mint.mod\n\
    \                elif all(isinstance(k, slice) for k in key):\n              \
    \      if isinstance(value, ModMat):\n                        for i, row in enumerate(range(*key[0].indices(self.R))):\n\
    \                            for j, col in enumerate(range(*key[1].indices(self.C))):\n\
    \                                self.data[row][col] = value.data[i][j] % mint.mod\n\
    \                    else:\n                        for row in range(*key[0].indices(self.R)):\n\
    \                            for col in range(*key[1].indices(self.C)):\n    \
    \                            self.data[row][col] = value % mint.mod\n        \
    \        else:\n                    raise IndexError(\"Invalid index\")\n    \
    \        else:\n                raise IndexError(\"Invalid index\")\n        elif\
    \ isinstance(key, slice):\n            if isinstance(value, ModMat):\n       \
    \         for i, row in enumerate(range(*key.indices(self.R))):\n            \
    \        self.data[row] = [v % mint.mod for v in value.data[i]]\n            else:\n\
    \                for row in range(*key.indices(self.R)):\n                   \
    \ self.data[row] = [value % mint.mod] * self.C\n        else:\n            raise\
    \ IndexError(\"Invalid index\")\n\n    def __delitem__(self, key: Union[int, slice]):\n\
    \        if isinstance(key, (int, slice)):\n            del self.data[key]\n \
    \           self.R = len(self.data)\n            if self.R == 0:\n           \
    \     self.C = 0\n        else:\n            raise IndexError(\"Invalid index\"\
    )\n\n    "
  dependsOn:
  - cp_library/math/mod/mint_cls.py
  isVerificationFile: false
  path: cp_library/math/linalg/mat/mod/modmat_cls.py
  requiredBy: []
  timestamp: '2025-05-19 01:45:33+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/linear-algebra/pow_of_matrix_modmat.test.py
documentation_of: cp_library/math/linalg/mat/mod/modmat_cls.py
layout: document
redirect_from:
- /library/cp_library/math/linalg/mat/mod/modmat_cls.py
- /library/cp_library/math/linalg/mat/mod/modmat_cls.py.html
title: cp_library/math/linalg/mat/mod/modmat_cls.py
---
