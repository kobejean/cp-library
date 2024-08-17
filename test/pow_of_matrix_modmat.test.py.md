---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/modint.py
    title: cp_library/math/mod/modint.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/modmat.py
    title: cp_library/math/mod/modmat.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/pow_of_matrix
    links:
    - https://judge.yosupo.jp/problem/pow_of_matrix
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_matrix\n\
    \n\nclass mint(int):\n    mod = None\n    def __new__(cls, x): return super().__new__(cls,\
    \ x % cls.mod)\n    def __add__(self, other): return mint(super().__add__(other))\n\
    \    def __radd__(self, other): return mint(super().__radd__(other))\n    def\
    \ __sub__(self, other): return mint(super().__sub__(other))\n    def __rsub__(self,\
    \ other): return mint(super().__rsub__(other))\n    def __mul__(self, other):\
    \ return mint(super().__mul__(other))\n    def __rmul__(self, other): return mint(super().__rmul__(other))\n\
    \    def __truediv__(self, other): return mint(super().__mul__(pow(other,-1,self.mod)))\n\
    \    def __rtruediv__(self, other): return mint(int.__mul__(other,pow(self,-1,self.mod)))\n\
    \    def __mod__(self, other): return mint(super().__mod__(other))\n    def __rmod__(self,\
    \ other): return mint(super().__rmod__(other))\n    def __pow__(self, other):\
    \ return mint(pow(self,other,self.mod))\n    def __rpow__(self, other): return\
    \ mint(pow(other,other,self.mod))\n    def __eq__(self, other): return super().__eq__(mint(other))\n\
    \    def __req__(self, other): return super().__eq__(mint(other))\n\nfrom functools\
    \ import cached_property\nfrom typing import Union, List, Tuple\n\nclass ModMat:\n\
    \    __slots__ = 'data', 'R', 'C'\n\n    def __init__(self, data: List[Union[int,mint]]):\n\
    \        self.data, self.R, self.C = data, len(data), len(data[0])\n    \n   \
    \ @classmethod\n    def identity(cls, N) -> 'ModMat': return ModMat([[int(i==j)\
    \ for j in range(N)] for i in range(N)])\n    \n    @classmethod\n    def zeros(cls,\
    \ R, C) -> 'ModMat': return ModMat([[0]*C for _ in range(R)])\n\n    @cached_property\n\
    \    def inv(self) -> 'ModMat':\n        assert self.R != self.C\n        \n \
    \       N = self.R\n        A = [row[:] for row in self.data]\n        I = [[int(i==j)\
    \ for j in range(N)] for i in range(N)]\n        \n        for i in range(N):\n\
    \            if A[i][i] == 0:\n                for j in range(i+1, N):\n     \
    \               if A[j][i] != 0:\n                        A[i], A[j] = A[j], A[i]\n\
    \                        I[i], I[j] = I[j], I[i]\n                        break\n\
    \                else:\n                    raise ValueError(\"Matrix is not invertible\"\
    )\n            \n            inv = pow(A[i][i], -1, mint.mod)\n            for\
    \ j in range(N):\n                A[i][j] = (A[i][j] * inv) % mint.mod\n     \
    \           I[i][j] = (I[i][j] * inv) % mint.mod\n            \n            for\
    \ j in range(N):\n                if i != j:\n                    factor = A[j][i]\n\
    \                    for k in range(N):\n                        A[j][k] = (A[j][k]\
    \ - factor * A[i][k]) % mint.mod\n                        I[j][k] = (I[j][k] -\
    \ factor * I[i][k]) % mint.mod\n        \n        return ModMat(I)\n    \n   \
    \ @cached_property\n    def T(self) -> 'ModMat': return ModMat(list(map(list,zip(*self.data))))\n\
    \n    def elem_wise(self, func, other):\n        if isinstance(other, ModMat):\n\
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
    )\n\n    \n\nmint.mod = 998244353\n\ndef rint(shift=0, base=10):\n    return [int(x,\
    \ base) + shift for x in input().split()]\n\n\nN, K = rint()\nA = ModMat([rint()\
    \ for _ in range(N)])\nB = A**K\nprint(B)\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_matrix\n\
    \nfrom cp_library.math.mod.modint import mint\nfrom cp_library.math.mod.modmat\
    \ import ModMat\n\nmint.mod = 998244353\n\ndef rint(shift=0, base=10):\n    return\
    \ [int(x, base) + shift for x in input().split()]\n\n\nN, K = rint()\nA = ModMat([rint()\
    \ for _ in range(N)])\nB = A**K\nprint(B)\n"
  dependsOn:
  - cp_library/math/mod/modint.py
  - cp_library/math/mod/modmat.py
  isVerificationFile: true
  path: test/pow_of_matrix_modmat.test.py
  requiredBy: []
  timestamp: '2024-08-17 16:57:44+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/pow_of_matrix_modmat.test.py
layout: document
redirect_from:
- /verify/test/pow_of_matrix_modmat.test.py
- /verify/test/pow_of_matrix_modmat.test.py.html
title: test/pow_of_matrix_modmat.test.py
---
