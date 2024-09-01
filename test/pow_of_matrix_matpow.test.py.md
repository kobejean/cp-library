---
data:
  _extendedDependsOn:
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
    \n\nmod = 998244353\n\ndef rint(shift=0, base=10):\n    return [int(x, base) +\
    \ shift for x in input().split()]\n\nN, K = rint()\nif N < 10:\n    \n    def\
    \ mat_mul(A,B):\n        assert len(A[0]) == len(B)\n        R = [[0]*len(B[0])\
    \ for _ in range(len(A))] \n        for i,Ri in enumerate(R):\n            for\
    \ k,Aik in enumerate(A[i]):\n                for j,Bkj in enumerate(B[k]):\n \
    \                   Ri[j] = Bkj*Aik + Ri[j]  \n        return R \n    \n    def\
    \ mat_id(N):\n        return [[int(i==j) for j in range(N)] for i in range(N)]\n\
    \    \n    def mat_pow(A,K):\n        N = len(A)\n        ret = A if K & 1 else\
    \ mat_id(N)\n        for i in range(1,K.bit_length()):\n            A = mat_mul(A,A)\
    \ \n            if K >> i & 1:\n                ret = mat_mul(ret,A) \n      \
    \  return ret \n    \n    class mint(int):\n        mod = None\n        def __new__(cls,\
    \ x=0): return super().__new__(cls, x % cls.mod)\n        def __add__(self, other):\
    \ return mint(super().__add__(other))\n        def __radd__(self, other): return\
    \ mint(super().__radd__(other))\n        def __sub__(self, other): return mint(super().__sub__(other))\n\
    \        def __rsub__(self, other): return mint(super().__rsub__(other))\n   \
    \     def __mul__(self, other): return mint(super().__mul__(other))\n        def\
    \ __rmul__(self, other): return mint(super().__rmul__(other))\n        def __truediv__(self,\
    \ other): return mint(super().__mul__(pow(other,-1,self.mod)))\n        def __rtruediv__(self,\
    \ other): return mint(int.__mul__(other,pow(self,-1,self.mod)))\n        def __mod__(self,\
    \ other): return mint(super().__mod__(other))\n        def __rmod__(self, other):\
    \ return mint(super().__rmod__(other))\n        def __pow__(self, other): return\
    \ mint(pow(self,other,self.mod))\n        def __rpow__(self, other): return mint(pow(other,other,self.mod))\n\
    \        def __eq__(self, other): return super().__eq__(mint(other))\n       \
    \ def __req__(self, other): return super().__eq__(mint(other))\n    \n    mint.mod\
    \ = 998244353\n\n    def rmint():\n        return [mint(int(x)) for x in input().split()]\n\
    \n    A = [rmint() for _ in range(N)]\n    B = mat_pow(A, K)\n\nelse:\n    \n\
    \    def mat_mul(A,B,mod):\n        assert len(A[0]) == len(B)\n        R = [[0]*len(B[0])\
    \ for _ in range(len(A))] \n        for i,Ri in enumerate(R):\n            for\
    \ k,Aik in enumerate(A[i]):\n                for j,Bkj in enumerate(B[k]):\n \
    \                   Ri[j] = (Ri[j] + Aik*Bkj) % mod\n        return R\n    \n\
    \    def mat_pow(A,K,mod):\n        N = len(A)\n        ret = A if K & 1 else\
    \ mat_id(N)\n        for i in range(1,K.bit_length()):\n            A = mat_mul(A,A,mod)\
    \ \n            if K >> i & 1:\n                ret = mat_mul(ret,A,mod) \n  \
    \      return ret \n\n    A = [rint() for _ in range(N)]\n    B = mat_pow(A, K,\
    \ mod)\n\nfor row in B:\n    print(*row)\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_matrix\n\
    \n\nmod = 998244353\n\ndef rint(shift=0, base=10):\n    return [int(x, base) +\
    \ shift for x in input().split()]\n\nN, K = rint()\nif N < 10:\n    from cp_library.math.mat_pow_fn\
    \ import mat_pow\n    from cp_library.math.mod.mint_cls import mint\n    mint.mod\
    \ = 998244353\n\n    def rmint():\n        return [mint(int(x)) for x in input().split()]\n\
    \n    A = [rmint() for _ in range(N)]\n    B = mat_pow(A, K)\n\nelse:\n    from\
    \ cp_library.math.mod.mat_pow_fn import mat_pow\n\n    A = [rint() for _ in range(N)]\n\
    \    B = mat_pow(A, K, mod)\n\nfor row in B:\n    print(*row)\n"
  dependsOn:
  - cp_library/math/mat_pow_fn.py
  - cp_library/math/mod/mint_cls.py
  - cp_library/math/mod/mat_pow_fn.py
  - cp_library/math/mat_mul_fn.py
  - cp_library/math/mat_id_fn.py
  - cp_library/math/mod/mat_mul_fn.py
  isVerificationFile: true
  path: test/pow_of_matrix_matpow.test.py
  requiredBy: []
  timestamp: '2024-09-02 01:58:23+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/pow_of_matrix_matpow.test.py
layout: document
redirect_from:
- /verify/test/pow_of_matrix_matpow.test.py
- /verify/test/pow_of_matrix_matpow.test.py.html
title: test/pow_of_matrix_matpow.test.py
---
