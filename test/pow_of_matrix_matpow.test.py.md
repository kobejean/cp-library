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
    \n\ndef main():\n    mod = 998244353\n    N, K = read()\n    if N < 10:\n    \
    \    '''\n        \u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2578\n                     https://kobejean.github.io/cp-library     \
    \          \n        '''\n        \n        def mat_pow(A,K):\n            N =\
    \ len(A)\n            ret = A if K & 1 else mat_id(N)\n            for i in range(1,K.bit_length()):\n\
    \                A = mat_mul(A,A) \n                if K >> i & 1:\n         \
    \           ret = mat_mul(ret,A) \n            return ret \n        \n       \
    \ '''\n        \u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n                     https://kobejean.github.io/cp-library           \
    \    \n        '''\n        \n        def mat_mul(A,B):\n            assert len(A[0])\
    \ == len(B)\n            R = [[0]*len(B[0]) for _ in range(len(A))] \n       \
    \     for i,Ri in enumerate(R):\n                for k,Aik in enumerate(A[i]):\n\
    \                    for j,Bkj in enumerate(B[k]):\n                        Ri[j]\
    \ = Bkj*Aik + Ri[j]  \n            return R \n        '''\n        \u257A\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n               \
    \      https://kobejean.github.io/cp-library               \n        '''\n   \
    \     \n        def mat_id(N):\n            return [[int(i==j) for j in range(N)]\
    \ for i in range(N)]\n        '''\n        \u257A\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2578\n                     https://kobejean.github.io/cp-library\
    \               \n        '''\n        \n        class mint(int):\n          \
    \  mod = zero = one = None\n        \n            def __new__(cls, *args, **kwargs):\n\
    \                match int(*args, **kwargs):\n                    case 0: return\
    \ cls.zero\n                    case 1: return cls.one\n                    case\
    \ x: return cls.fix(x)\n        \n            @classmethod\n            def set_mod(cls,\
    \ mod):\n                cls.mod = mod\n                cls.zero, cls.one = cls.cast(0),\
    \ cls.fix(1)\n        \n            @classmethod\n            def fix(cls, x):\
    \ return cls.cast(x%cls.mod)\n        \n            @classmethod\n           \
    \ def cast(cls, x): return super().__new__(cls,x)\n        \n            @classmethod\n\
    \            def mod_inv(cls, x):\n                a,b,s,t = int(x), cls.mod,\
    \ 1, 0\n                while b: a,b,s,t = b,a%b,t,s-a//b*t\n                if\
    \ a == 1: return cls.fix(s)\n                raise ValueError(f\"{x} is not invertible\"\
    )\n            \n            @property\n            def inv(self): return mint.mod_inv(self)\n\
    \        \n            def __add__(self, x): return mint.fix(super().__add__(x))\n\
    \            def __radd__(self, x): return mint.fix(super().__radd__(x))\n   \
    \         def __sub__(self, x): return mint.fix(super().__sub__(x))\n        \
    \    def __rsub__(self, x): return mint.fix(super().__rsub__(x))\n           \
    \ def __mul__(self, x): return mint.fix(super().__mul__(x))\n            def __rmul__(self,\
    \ x): return mint.fix(super().__rmul__(x))\n            def __floordiv__(self,\
    \ x): return self * mint.mod_inv(x)\n            def __rfloordiv__(self, x): return\
    \ self.inv * x\n            def __truediv__(self, x): return self * mint.mod_inv(x)\n\
    \            def __rtruediv__(self, x): return self.inv * x\n            def __pow__(self,\
    \ x): \n                return self.cast(super().__pow__(x, self.mod))\n     \
    \       def __neg__(self): return mint.mod-self\n            def __pos__(self):\
    \ return self\n            def __abs__(self): return self\n        \n        mint.set_mod(998244353)\n\
    \n        A = [read(mint) for _ in range(N)]\n        B = mat_pow(A, K)\n    else:\n\
    \        '''\n        \u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2578\n                     https://kobejean.github.io/cp-library     \
    \          \n        '''\n        \n        def mat_pow(A,K,mod):\n          \
    \  N = len(A)\n            ret = A if K & 1 else mat_id(N)\n            for i\
    \ in range(1,K.bit_length()):\n                A = mat_mul(A,A,mod) \n       \
    \         if K >> i & 1:\n                    ret = mat_mul(ret,A,mod) \n    \
    \        return ret \n        \n        '''\n        \u257A\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2578\n                     https://kobejean.github.io/cp-library\
    \               \n        '''\n        \n        def mat_mul(A,B,mod):\n     \
    \       assert len(A[0]) == len(B)\n            R = [[0]*len(B[0]) for _ in range(len(A))]\
    \ \n            for i,Ri in enumerate(R):\n                for k,Aik in enumerate(A[i]):\n\
    \                    for j,Bkj in enumerate(B[k]):\n                        Ri[j]\
    \ = (Ri[j] + Aik*Bkj) % mod\n            return R\n        '''\n        \u257A\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n         \
    \            https://kobejean.github.io/cp-library               \n        '''\n\
    \        \n        def mat_id(N):\n            return [[int(i==j) for j in range(N)]\
    \ for i in range(N)]\n\n        A = [read() for _ in range(N)]\n        B = mat_pow(A,\
    \ K, mod)\n\n    for row in B:\n        print(*row)\n\n'''\n\u257A\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\ndef read(func=0, /):\n    if callable(func): return [func(s)\
    \ for s in input().split()]\n    return [int(s)+func for s in input().split()]\n\
    if __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_matrix\n\
    \n\ndef main():\n    mod = 998244353\n    N, K = read()\n    if N < 10:\n    \
    \    from cp_library.math.mat_pow_fn import mat_pow\n        from cp_library.math.mod.mint_cls\
    \ import mint\n        mint.set_mod(998244353)\n\n        A = [read(mint) for\
    \ _ in range(N)]\n        B = mat_pow(A, K)\n    else:\n        from cp_library.math.mod.mat_pow_fn\
    \ import mat_pow\n\n        A = [read() for _ in range(N)]\n        B = mat_pow(A,\
    \ K, mod)\n\n    for row in B:\n        print(*row)\n\nfrom cp_library.io.read_func_fn\
    \ import read\nif __name__ == '__main__':\n    main()"
  dependsOn:
  - cp_library/math/mat_pow_fn.py
  - cp_library/math/mod/mint_cls.py
  - cp_library/math/mod/mat_pow_fn.py
  - cp_library/io/read_func_fn.py
  - cp_library/math/mat_mul_fn.py
  - cp_library/math/mat_id_fn.py
  - cp_library/math/mod/mat_mul_fn.py
  isVerificationFile: true
  path: test/pow_of_matrix_matpow.test.py
  requiredBy: []
  timestamp: '2024-11-22 04:31:33+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/pow_of_matrix_matpow.test.py
layout: document
redirect_from:
- /verify/test/pow_of_matrix_matpow.test.py
- /verify/test/pow_of_matrix_matpow.test.py.html
title: test/pow_of_matrix_matpow.test.py
---
