---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_func_fn.py
    title: cp_library/io/read_func_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mat_id_fn.py
    title: cp_library/math/mat_id_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mat_mul_fn.py
    title: cp_library/math/mat_mul_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mat_pow_fn.py
    title: cp_library/math/mat_pow_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/mat_mul_fn.py
    title: cp_library/math/mod/mat_mul_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/mat_pow_fn.py
    title: cp_library/math/mod/mat_pow_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/mint_cls.py
    title: cp_library/math/mod/mint_cls.py
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
    \n\ndef read(func=0, /):\n    if callable(func): return [func(s) for s in input().split()]\n\
    \    return [int(s)+func for s in input().split()]\n\nmod = 998244353\n\n\nN,\
    \ K = read()\nif N < 10:\n    def mat_pow(A,K):\n        N = len(A)\n        ret\
    \ = A if K & 1 else mat_id(N)\n        for i in range(1,K.bit_length()):\n   \
    \         A = mat_mul(A,A) \n            if K >> i & 1:\n                ret =\
    \ mat_mul(ret,A) \n        return ret \n    \n    \n    def mat_mul(A,B):\n  \
    \      assert len(A[0]) == len(B)\n        R = [[0]*len(B[0]) for _ in range(len(A))]\
    \ \n        for i,Ri in enumerate(R):\n            for k,Aik in enumerate(A[i]):\n\
    \                for j,Bkj in enumerate(B[k]):\n                    Ri[j] = Bkj*Aik\
    \ + Ri[j]  \n        return R \n    \n    def mat_id(N):\n        return [[int(i==j)\
    \ for j in range(N)] for i in range(N)]\n    \n    class mint(int):\n        mod\
    \ = None\n        def __new__(cls, x=0): return super().__new__(cls, int(x) %\
    \ cls.mod)\n        @classmethod\n        def wrap(cls, x): return super().__new__(cls,\
    \ x % cls.mod)\n        @classmethod\n        def cast(cls, x): return super().__new__(cls,\
    \ x)\n        def __add__(self, x): return mint.wrap(super().__add__(x))\n   \
    \     def __radd__(self, x): return mint.wrap(super().__radd__(x))\n        def\
    \ __sub__(self, x): return mint.wrap(super().__sub__(x))\n        def __rsub__(self,\
    \ x): return mint.wrap(super().__rsub__(x))\n        def __mul__(self, x): return\
    \ mint.wrap(super().__mul__(x))\n        def __rmul__(self, x): return mint.wrap(super().__rmul__(x))\n\
    \        def __floordiv__(self, x): return mint.wrap(super().__mul__(pow(int(x),-1,self.mod)))\n\
    \        def __rfloordiv__(self, x): return mint.wrap(int.__mul__(x,pow(int(self),-1,self.mod)))\n\
    \        def __pow__(self, x): return mint.cast(pow(int(self),x,self.mod))\n \
    \       def __eq__(self, x): return super().__eq__(mint.wrap(x))\n        def\
    \ __req__(self, x): return super().__eq__(mint.wrap(x))\n    mint.mod = 998244353\n\
    \n    A = [read(mint) for _ in range(N)]\n    B = mat_pow(A, K)\n\nelse:\n   \
    \ def mat_pow(A,K,mod):\n        N = len(A)\n        ret = A if K & 1 else mat_id(N)\n\
    \        for i in range(1,K.bit_length()):\n            A = mat_mul(A,A,mod) \n\
    \            if K >> i & 1:\n                ret = mat_mul(ret,A,mod) \n     \
    \   return ret \n    \n    \n    def mat_mul(A,B,mod):\n        assert len(A[0])\
    \ == len(B)\n        R = [[0]*len(B[0]) for _ in range(len(A))] \n        for\
    \ i,Ri in enumerate(R):\n            for k,Aik in enumerate(A[i]):\n         \
    \       for j,Bkj in enumerate(B[k]):\n                    Ri[j] = (Ri[j] + Aik*Bkj)\
    \ % mod\n        return R\n\n    A = [read() for _ in range(N)]\n    B = mat_pow(A,\
    \ K, mod)\n\nfor row in B:\n    print(*row)\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_matrix\n\
    \nfrom cp_library.io.read_func_fn import read\n\nmod = 998244353\n\n\nN, K = read()\n\
    if N < 10:\n    from cp_library.math.mat_pow_fn import mat_pow\n    from cp_library.math.mod.mint_cls\
    \ import mint\n    mint.mod = 998244353\n\n    A = [read(mint) for _ in range(N)]\n\
    \    B = mat_pow(A, K)\n\nelse:\n    from cp_library.math.mod.mat_pow_fn import\
    \ mat_pow\n\n    A = [read() for _ in range(N)]\n    B = mat_pow(A, K, mod)\n\n\
    for row in B:\n    print(*row)\n"
  dependsOn:
  - cp_library/io/read_func_fn.py
  - cp_library/math/mat_pow_fn.py
  - cp_library/math/mod/mint_cls.py
  - cp_library/math/mod/mat_pow_fn.py
  - cp_library/math/mat_mul_fn.py
  - cp_library/math/mat_id_fn.py
  - cp_library/math/mod/mat_mul_fn.py
  isVerificationFile: true
  path: test/pow_of_matrix_matpow.test.py
  requiredBy: []
  timestamp: '2024-09-16 19:46:13+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/pow_of_matrix_matpow.test.py
layout: document
redirect_from:
- /verify/test/pow_of_matrix_matpow.test.py
- /verify/test/pow_of_matrix_matpow.test.py.html
title: test/pow_of_matrix_matpow.test.py
---