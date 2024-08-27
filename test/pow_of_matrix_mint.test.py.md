---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/matid.py
    title: cp_library/math/matid.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/matmul.py
    title: cp_library/math/matmul.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/matpow.py
    title: cp_library/math/matpow.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/modint.py
    title: cp_library/math/mod/modint.py
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
    \n\ndef mat_mul(A,B):\n    assert len(A[0]) == len(B)\n    R = [[0]*len(B[0])\
    \ for _ in range(len(A))] \n    for i,Ri in enumerate(R):\n        for k,Aik in\
    \ enumerate(A[i]):\n            for j,Bkj in enumerate(B[k]):\n              \
    \  Ri[j] = Bkj*Aik + Ri[j]  \n    return R \n\ndef mat_id(N):\n    return [[int(i==j)\
    \ for j in range(N)] for i in range(N)]\n\ndef mat_pow(A,K):\n    N = len(A)\n\
    \    ret = A if K & 1 else mat_id(N)\n    for i in range(1,K.bit_length()):\n\
    \        A = mat_mul(A,A) \n        if K >> i & 1:\n            ret = mat_mul(ret,A)\
    \ \n    return ret \n\nclass mint(int):\n    mod = None\n    def __new__(cls,\
    \ x): return super().__new__(cls, x % cls.mod)\n    def __add__(self, other):\
    \ return mint(super().__add__(other))\n    def __radd__(self, other): return mint(super().__radd__(other))\n\
    \    def __sub__(self, other): return mint(super().__sub__(other))\n    def __rsub__(self,\
    \ other): return mint(super().__rsub__(other))\n    def __mul__(self, other):\
    \ return mint(super().__mul__(other))\n    def __rmul__(self, other): return mint(super().__rmul__(other))\n\
    \    def __truediv__(self, other): return mint(super().__mul__(pow(other,-1,self.mod)))\n\
    \    def __rtruediv__(self, other): return mint(int.__mul__(other,pow(self,-1,self.mod)))\n\
    \    def __mod__(self, other): return mint(super().__mod__(other))\n    def __rmod__(self,\
    \ other): return mint(super().__rmod__(other))\n    def __pow__(self, other):\
    \ return mint(pow(self,other,self.mod))\n    def __rpow__(self, other): return\
    \ mint(pow(other,other,self.mod))\n    def __eq__(self, other): return super().__eq__(mint(other))\n\
    \    def __req__(self, other): return super().__eq__(mint(other))\n\n\nmint.mod\
    \ = 998244353\n\ndef rint(shift=0, base=10):\n    return [int(x, base) + shift\
    \ for x in input().split()]\n\ndef rmint():\n    return [mint(int(x)) for x in\
    \ input().split()]\n\nN, K = rint()\nA = [rmint() for _ in range(N)]\nB = mat_pow(A,\
    \ K)\n\nfor row in B:\n    print(*row)\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_matrix\n\
    \nfrom cp_library.math.matpow import mat_pow\nfrom cp_library.math.mod.modint\
    \ import mint\n\nmint.mod = 998244353\n\ndef rint(shift=0, base=10):\n    return\
    \ [int(x, base) + shift for x in input().split()]\n\ndef rmint():\n    return\
    \ [mint(int(x)) for x in input().split()]\n\nN, K = rint()\nA = [rmint() for _\
    \ in range(N)]\nB = mat_pow(A, K)\n\nfor row in B:\n    print(*row)\n"
  dependsOn:
  - cp_library/math/matpow.py
  - cp_library/math/mod/modint.py
  - cp_library/math/matmul.py
  - cp_library/math/matid.py
  isVerificationFile: true
  path: test/pow_of_matrix_mint.test.py
  requiredBy: []
  timestamp: '2024-08-27 19:43:09+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/pow_of_matrix_mint.test.py
layout: document
redirect_from:
- /verify/test/pow_of_matrix_mint.test.py
- /verify/test/pow_of_matrix_mint.test.py.html
title: test/pow_of_matrix_mint.test.py
---
