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
  - icon: ':heavy_check_mark:'
    path: cp_library/opt/lib_load.py
    title: cp_library/opt/lib_load.py
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
    \n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\
    \n             https://kobejean.github.io/cp-library               \n'''\n\ndef\
    \ read(func=0, /):\n    if callable(func): return [func(s) for s in input().split()]\n\
    \    return [int(s)+func for s in input().split()]\n\nmod = 998244353\n\n\nN,\
    \ K = read()\nif N < 10:\n    \n    \n    def mat_pow(A,K,mod):\n        N = len(A)\n\
    \        ret = A if K & 1 else mat_id(N)\n        for i in range(1,K.bit_length()):\n\
    \            A = mat_mul(A,A,mod) \n            if K >> i & 1:\n             \
    \   ret = mat_mul(ret,A,mod) \n        return ret \n    \n    \n    def mat_mul(A,B,mod):\n\
    \        assert len(A[0]) == len(B)\n        R = [[0]*len(B[0]) for _ in range(len(A))]\
    \ \n        for i,Ri in enumerate(R):\n            for k,Aik in enumerate(A[i]):\n\
    \                for j,Bkj in enumerate(B[k]):\n                    Ri[j] = (Ri[j]\
    \ + Aik*Bkj) % mod\n        return R\n    \n    def mat_id(N):\n        return\
    \ [[int(i==j) for j in range(N)] for i in range(N)]\n\n    A = [read() for _ in\
    \ range(N)]\n    B = mat_pow(A, K, mod)\nelse:\n    \n    def mat_pow(A,K):\n\
    \        N = len(A)\n        ret = A if K & 1 else mat_id(N)\n        for i in\
    \ range(1,K.bit_length()):\n            A = mat_mul(A,A) \n            if K >>\
    \ i & 1:\n                ret = mat_mul(ret,A) \n        return ret \n    \n \
    \   \n    def mat_mul(A,B):\n        assert len(A[0]) == len(B)\n        R = [[0]*len(B[0])\
    \ for _ in range(len(A))] \n        for i,Ri in enumerate(R):\n            for\
    \ k,Aik in enumerate(A[i]):\n                for j,Bkj in enumerate(B[k]):\n \
    \                   Ri[j] = Bkj*Aik + Ri[j]  \n        return R \n    \n    class\
    \ mint(int):\n        mod = zero = one = None\n    \n        def __new__(cls,\
    \ *args, **kwargs):\n            match int(*args, **kwargs):\n               \
    \ case 0: return cls.zero\n                case 1: return cls.one\n          \
    \      case x: return cls.fix(x)\n    \n        @classmethod\n        def set_mod(cls,\
    \ mod):\n            cls.mod = mod\n            cls.zero, cls.one = cls.cast(0),\
    \ cls.fix(1)\n    \n        @classmethod\n        def fix(cls, x): return cls.cast(x%cls.mod)\n\
    \    \n        @classmethod\n        def cast(cls, x): return super().__new__(cls,x)\n\
    \    \n        @classmethod\n        def mod_inv(cls, x):\n            ENCODED_BINARY\
    \ = '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'\n\
    \            import os\n            import tempfile\n            import base64\n\
    \            import zlib\n            from cffi import FFI\n            \n   \
    \         def compress_and_encode_library(lib_data):\n                compressed_data\
    \ = zlib.compress(lib_data, level=9)\n                return base64.b64encode(compressed_data).decode()\n\
    \            \n            def decode_and_decompress_library(encoded_data):\n\
    \                compressed_data = base64.b64decode(encoded_data)\n          \
    \      return zlib.decompress(compressed_data)\n            \n            def\
    \ load_library(lib_data, ffi_instance):\n                fd, path = tempfile.mkstemp(suffix='.so')\n\
    \                try:\n                    with os.fdopen(fd, 'wb') as tmp:\n\
    \                        tmp.write(lib_data)\n                    \n         \
    \           return ffi_instance.dlopen(path)\n                except Exception\
    \ as e:\n                    # print(f\"Error loading library: {e}\")\n      \
    \              return None\n                finally:\n                    os.unlink(path)\n\
    \            \n            ffi = FFI()\n            ffi.cdef(\"\"\"\n        \
    \        int64_t mod_inv(int64_t a, int64_t mod);\n            \"\"\")\n     \
    \       decoded_lib_data = decode_and_decompress_library(ENCODED_BINARY)\n   \
    \         lib = load_library(decoded_lib_data, ffi)\n            \n          \
    \  def mod_inv(a, mod):\n                if inv := lib.mod_inv(a, mod):\n    \
    \                return inv\n                raise ValueError(\"No inverse!\"\
    )\n            \n            def test(a, mod):\n                x = mod_inv(a,\
    \ mod)\n                y = pow(a,-1,mod)\n                assert x == y\n   \
    \         if lib:\n                inv = lib.mod_inv(int(x), cls.mod)\n      \
    \          if inv:\n                    return cls.fix(inv)\n            else:\n\
    \                a,b,s,t = int(x), cls.mod, 1, 0\n                while b: a,b,s,t\
    \ = b,a%b,t,s-a//b*t\n                if a == 1: return cls.fix(s)\n         \
    \   raise ValueError(f\"{x} is not invertible\")\n        \n        @property\n\
    \        def inv(self): return mint.mod_inv(self)\n    \n        def __add__(self,\
    \ x): return mint.fix(super().__add__(x))\n        def __radd__(self, x): return\
    \ mint.fix(super().__radd__(x))\n        def __sub__(self, x): return mint.fix(super().__sub__(x))\n\
    \        def __rsub__(self, x): return mint.fix(super().__rsub__(x))\n       \
    \ def __mul__(self, x): return mint.fix(super().__mul__(x))\n        def __rmul__(self,\
    \ x): return mint.fix(super().__rmul__(x))\n        def __floordiv__(self, x):\
    \ return self * mint.mod_inv(x)\n        def __rfloordiv__(self, x): return self.inv\
    \ * x\n        def __truediv__(self, x): return self * mint.mod_inv(x)\n     \
    \   def __rtruediv__(self, x): return self.inv * x\n        def __pow__(self,\
    \ x): \n            return self.cast(super().__pow__(x, self.mod))\n        def\
    \ __eq__(self, x): return super().__eq__(self-x, 0)\n        def __neg__(self):\
    \ return mint.mod-self\n        def __pos__(self): return self\n        def __abs__(self):\
    \ return self\n    \n    mint.set_mod(998244353)\n\n    A = [read(mint) for _\
    \ in range(N)]\n    B = mat_pow(A, K)\n\nfor row in B:\n    print(*row)\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_matrix\n\
    \nfrom cp_library.io.read_func_fn import read\n\nmod = 998244353\n\n\nN, K = read()\n\
    if N < 10:\n    from cp_library.math.mod.mat_pow_fn import mat_pow\n\n    A =\
    \ [read() for _ in range(N)]\n    B = mat_pow(A, K, mod)\nelse:\n    from cp_library.math.mat_pow_fn\
    \ import mat_pow\n    from cp_library.math.mod.mint_cls import mint\n    mint.set_mod(998244353)\n\
    \n    A = [read(mint) for _ in range(N)]\n    B = mat_pow(A, K)\n\nfor row in\
    \ B:\n    print(*row)\n"
  dependsOn:
  - cp_library/io/read_func_fn.py
  - cp_library/math/mod/mat_pow_fn.py
  - cp_library/math/mat_pow_fn.py
  - cp_library/math/mod/mint_cls.py
  - cp_library/math/mod/mat_mul_fn.py
  - cp_library/math/mat_id_fn.py
  - cp_library/math/mat_mul_fn.py
  - cp_library/opt/lib_load.py
  isVerificationFile: true
  path: test/pow_of_matrix_matpow.test.py
  requiredBy: []
  timestamp: '2024-09-21 04:14:27+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/pow_of_matrix_matpow.test.py
layout: document
redirect_from:
- /verify/test/pow_of_matrix_matpow.test.py
- /verify/test/pow_of_matrix_matpow.test.py.html
title: test/pow_of_matrix_matpow.test.py
---
