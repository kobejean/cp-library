---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_specs_fn.py
    title: cp_library/io/read_specs_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mobius_transform_fn.py
    title: cp_library/math/mobius_transform_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/mint_cls.py
    title: cp_library/math/mod/mint_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/mobius_transform_fn.py
    title: cp_library/math/mod/mobius_transform_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/subset_convolution_fn.py
    title: cp_library/math/mod/subset_convolution_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/zeta_transform_fn.py
    title: cp_library/math/mod/zeta_transform_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/subset_convolution_fn.py
    title: cp_library/math/subset_convolution_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/zeta_transform_fn.py
    title: cp_library/math/zeta_transform_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/subset_convolution
    links:
    - https://judge.yosupo.jp/problem/subset_convolution
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/subset_convolution\n\
    \ndef read(*specs: tuple[type]):\n    S = input().split()\n    return [func(s)\
    \ for func, s in io_specs(specs, S)]\n\ndef io_specs(specs, S):\n    def shift(shift):\n\
    \        return lambda s: int(s) + shift\n    def spec_func(spec):\n        return\
    \ shift(spec) if isinstance(spec, int) else spec\n    if len(specs) > 1:\n   \
    \     return zip(map(spec_func, specs), S)\n    func = spec_func(specs[0] if specs\
    \ else int)\n    return ((func, s) for s in S)\nmod = 998244353\n\nN, = read()\n\
    if N < 10:\n    def subset_convolution(A, B, N):\n        Z = 1 << N\n    \n \
    \       # Prepare arrays for rank (popcount) decomposition\n        Arank = [[0]*Z\
    \ for _ in range(N+1)]\n        Brank = [[0]*Z for _ in range(N+1)]\n    \n  \
    \      # Initialize rank arrays\n        for mask in range(Z):\n            rank\
    \ = mask.bit_count()\n            Arank[rank][mask] = A[mask]\n            Brank[rank][mask]\
    \ = B[mask]\n    \n        # Zeta transform for each rank\n        for Ar in Arank:\
    \ zeta_transform(Ar, N)\n        for Br in Brank: zeta_transform(Br, N)\n    \n\
    \        # Convolution\n        Crank = [[0 for _ in range(Z)] for _ in range(N+1)]\n\
    \        for mask in range(Z):\n            L = mask.bit_count()+1\n         \
    \   for i in range(L):\n                for j in range(min(L, N+1-i)):\n     \
    \               k = i+j\n                    Crank[k][mask] = Crank[k][mask] +\
    \ Arank[i][mask] * Brank[j][mask]\n    \n        # M\xF6bius transform (inverse\
    \ of Zeta transform)\n        for Cr in Crank: mobius_transform(Cr, N)\n     \
    \       \n        # Combine results\n        C = [0] * Z\n        for mask in\
    \ range(Z):\n            rank = mask.bit_count()\n            C[mask] = Crank[rank][mask]\n\
    \    \n        return C\n    \n    \n    def zeta_transform(A, N):\n        for\
    \ i in range(N):\n            bit = 1 << i\n            for mask in range(1 <<\
    \ N):\n                if mask & bit:\n                    A[mask] += A[mask ^\
    \ bit]\n        return A\n    \n    def mobius_transform(A, N):\n        for i\
    \ in range(N):\n            bit = 1 << i\n            for mask in range(1 << N):\n\
    \                if mask & bit:\n                    A[mask] -= A[mask ^ bit]\n\
    \        return A\n    \n    class mint(int):\n        mod = None\n        def\
    \ __new__(cls, x=0): return super().__new__(cls, int(x) % cls.mod)\n        @classmethod\n\
    \        def wrap(cls, x): return super().__new__(cls, x % cls.mod)\n        @classmethod\n\
    \        def cast(cls, x): return super().__new__(cls, x)\n        def __add__(self,\
    \ x): return mint.wrap(super().__add__(x))\n        def __radd__(self, x): return\
    \ mint.wrap(super().__radd__(x))\n        def __sub__(self, x): return mint.wrap(super().__sub__(x))\n\
    \        def __rsub__(self, x): return mint.wrap(super().__rsub__(x))\n      \
    \  def __mul__(self, x): return mint.wrap(super().__mul__(x))\n        def __rmul__(self,\
    \ x): return mint.wrap(super().__rmul__(x))\n        def __floordiv__(self, x):\
    \ return mint.wrap(super().__mul__(pow(int(x),-1,self.mod)))\n        def __rfloordiv__(self,\
    \ x): return mint.wrap(int.__mul__(x,pow(int(self),-1,self.mod)))\n        def\
    \ __pow__(self, x): return mint.cast(pow(int(self),x,self.mod))\n        def __eq__(self,\
    \ x): return super().__eq__(mint.wrap(x))\n        def __req__(self, x): return\
    \ super().__eq__(mint.wrap(x))\n    mint.mod = mod\n    F = read(mint)\n    G\
    \ = read(mint)\n    print(*subset_convolution(F, G, N))\nelse:\n    \n    def\
    \ subset_convolution(A, B, N, mod):\n        Z = 1 << N\n    \n        # Prepare\
    \ arrays for rank (popcount) decomposition\n        Arank = [[0]*Z for _ in range(N+1)]\n\
    \        Brank = [[0]*Z for _ in range(N+1)]\n    \n        # Initialize rank\
    \ arrays\n        for mask in range(Z):\n            rank = mask.bit_count()\n\
    \            Arank[rank][mask] = A[mask]\n            Brank[rank][mask] = B[mask]\n\
    \    \n        # Zeta transform for each rank\n        for Ar in Arank: zeta_transform(Ar,\
    \ N, mod)\n        for Br in Brank: zeta_transform(Br, N, mod)\n    \n       \
    \ # Convolution\n        Crank = [[0]*Z for _ in range(N+1)]\n        for mask\
    \ in range(Z):\n            L = mask.bit_count()+1\n            for i in range(L):\n\
    \                for j in range(min(L, N+1-i)):\n                    k = i+j\n\
    \                    Crank[k][mask] = (Crank[k][mask] + Arank[i][mask] * Brank[j][mask])\
    \ % mod\n    \n        # M\xF6bius transform (inverse of Zeta transform)\n   \
    \     for Cr in Crank: mobius_transform(Cr, N, mod)\n            \n        # Combine\
    \ results\n        C = [0] * Z\n        for mask in range(Z):\n            rank\
    \ = mask.bit_count()\n            C[mask] = Crank[rank][mask]\n    \n        return\
    \ C\n    \n    \n    def zeta_transform(A, N, mod):\n        for i in range(N):\n\
    \            bit = 1 << i\n            for mask in range(1 << N):\n          \
    \      if mask & bit:\n                    A[mask] = (A[mask] + A[mask ^ bit])\
    \ % mod\n        return A\n    \n    def mobius_transform(A, N, mod):\n      \
    \  for i in range(N):\n            bit = 1 << i\n            for mask in range(1\
    \ << N):\n                if mask & bit:\n                    A[mask] = (A[mask]\
    \ - A[mask ^ bit]) % mod\n        return A\n    \n    F = read()\n    G = read()\n\
    \    print(*subset_convolution(F, G, N, mod))\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/subset_convolution\n\
    from cp_library.io.read_specs_fn import read\nmod = 998244353\n\nN, = read()\n\
    if N < 10:\n    from cp_library.math.subset_convolution_fn import subset_convolution\n\
    \    from cp_library.math.mod.mint_cls import mint\n    mint.mod = mod\n    F\
    \ = read(mint)\n    G = read(mint)\n    print(*subset_convolution(F, G, N))\n\
    else:\n    from cp_library.math.mod.subset_convolution_fn import subset_convolution\n\
    \    \n    F = read()\n    G = read()\n    print(*subset_convolution(F, G, N,\
    \ mod))"
  dependsOn:
  - cp_library/io/read_specs_fn.py
  - cp_library/math/subset_convolution_fn.py
  - cp_library/math/mod/mint_cls.py
  - cp_library/math/mod/subset_convolution_fn.py
  - cp_library/math/zeta_transform_fn.py
  - cp_library/math/mobius_transform_fn.py
  - cp_library/math/mod/zeta_transform_fn.py
  - cp_library/math/mod/mobius_transform_fn.py
  isVerificationFile: true
  path: test/subset_convolution.test.py
  requiredBy: []
  timestamp: '2024-09-16 19:46:13+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/subset_convolution.test.py
layout: document
redirect_from:
- /verify/test/subset_convolution.test.py
- /verify/test/subset_convolution.test.py.html
title: test/subset_convolution.test.py
---
