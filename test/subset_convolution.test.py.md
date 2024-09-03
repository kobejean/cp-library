---
data:
  _extendedDependsOn:
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
    mod = 998244353\n\ndef rint(shift=0, base=10):\n    return [int(x, base) + shift\
    \ for x in input().split()]\n\n\n\nN, = rint()\nF = rint()\nG = rint()\nif N <\
    \ 10:\n    \n    def zeta_transform(A):\n        N = len(A).bit_length()-1\n \
    \   \n        for i in range(N):\n            bit = 1 << i\n            for mask\
    \ in range(1 << N):\n                if mask & bit:\n                    A[mask]\
    \ += A[mask ^ bit]\n    \n        return A\n    \n    def mobius_transform(A):\n\
    \        N = len(A).bit_length()-1\n    \n        for i in range(N):\n       \
    \     bit = 1 << i\n            for mask in range(1 << N):\n                if\
    \ mask & bit:\n                    A[mask] -= A[mask ^ bit]\n    \n        return\
    \ A\n    \n    def subset_convolution(A, B):\n        N = max(len(A), len(B)).bit_length()\n\
    \        Z = 1 << (N-1)\n    \n        # Prepare arrays for rank (popcount) decomposition\n\
    \        Arank = [[0]*Z for _ in range(N)]\n        Brank = [[0]*Z for _ in range(N)]\n\
    \    \n        # Initialize rank arrays\n        for mask in range(Z):\n     \
    \       rank = mask.bit_count()\n            Arank[rank][mask] = A[mask]\n   \
    \         Brank[rank][mask] = B[mask]\n    \n        # Zeta transform for each\
    \ rank\n        for Ar in Arank: zeta_transform(Ar)\n        for Br in Brank:\
    \ zeta_transform(Br)\n    \n        # Convolution\n        Crank = [[0 for _ in\
    \ range(Z)] for _ in range(N)]\n        for mask in range(Z):\n            L =\
    \ mask.bit_count()+1\n            for i in range(L):\n                for j in\
    \ range(min(L, N-i)):\n                    k = i+j\n                    Crank[k][mask]\
    \ = Crank[k][mask] + Arank[i][mask] * Brank[j][mask]\n    \n        # M\xF6bius\
    \ transform (inverse of Zeta transform)\n        for Cr in Crank: mobius_transform(Cr)\n\
    \            \n        # Combine results\n        C = [0] * Z\n        for mask\
    \ in range(Z):\n            rank = mask.bit_count()\n            C[mask] = Crank[rank][mask]\n\
    \    \n        return C\n    \n    class mint(int):\n        mod = None\n    \
    \    def __new__(cls, x=0): return super().__new__(cls, x % cls.mod)\n       \
    \ def __add__(self, other): return mint(super().__add__(other))\n        def __radd__(self,\
    \ other): return mint(super().__radd__(other))\n        def __sub__(self, other):\
    \ return mint(super().__sub__(other))\n        def __rsub__(self, other): return\
    \ mint(super().__rsub__(other))\n        def __mul__(self, other): return mint(super().__mul__(other))\n\
    \        def __rmul__(self, other): return mint(super().__rmul__(other))\n   \
    \     def __truediv__(self, other): return mint(super().__mul__(pow(other,-1,self.mod)))\n\
    \        def __rtruediv__(self, other): return mint(int.__mul__(other,pow(self,-1,self.mod)))\n\
    \        def __mod__(self, other): return mint(super().__mod__(other))\n     \
    \   def __rmod__(self, other): return mint(super().__rmod__(other))\n        def\
    \ __pow__(self, other): return mint(pow(self,other,self.mod))\n        def __rpow__(self,\
    \ other): return mint(pow(other,other,self.mod))\n        def __eq__(self, other):\
    \ return super().__eq__(mint(other))\n        def __req__(self, other): return\
    \ super().__eq__(mint(other))\n    \n    mint.mod = mod\n    \n    F = list(map(mint,\
    \ F))\n    G = list(map(mint, G))\n    print(*subset_convolution(F, G))\nelse:\n\
    \    \n    def zeta_transform(A, mod):\n        N = len(A).bit_length()-1\n  \
    \  \n        for i in range(N):\n            bit = 1 << i\n            for mask\
    \ in range(1 << N):\n                if mask & bit:\n                    A[mask]\
    \ = (A[mask] + A[mask ^ bit]) % mod\n    \n        return A\n    \n    def mobius_transform(A,\
    \ mod):\n        N = len(A).bit_length()-1\n    \n        for i in range(N):\n\
    \            bit = 1 << i\n            for mask in range(1 << N):\n          \
    \      if mask & bit:\n                    A[mask] = (A[mask] - A[mask ^ bit])\
    \ % mod\n    \n        return A\n    \n    def subset_convolution(A, B, mod):\n\
    \        N = max(len(A), len(B)).bit_length()\n        Z = 1 << (N-1)\n    \n\
    \        # Prepare arrays for rank (popcount) decomposition\n        Arank = [[0]*Z\
    \ for _ in range(N)]\n        Brank = [[0]*Z for _ in range(N)]\n    \n      \
    \  # Initialize rank arrays\n        for mask in range(Z):\n            rank =\
    \ mask.bit_count()\n            Arank[rank][mask] = A[mask]\n            Brank[rank][mask]\
    \ = B[mask]\n    \n        # Zeta transform for each rank\n        for Ar in Arank:\
    \ zeta_transform(Ar, mod)\n        for Br in Brank: zeta_transform(Br, mod)\n\
    \    \n        # Convolution\n        Crank = [[0 for _ in range(Z)] for _ in\
    \ range(N)]\n        for mask in range(Z):\n            L = mask.bit_count()+1\n\
    \            for i in range(L):\n                for j in range(min(L, N-i)):\n\
    \                    k = i+j\n                    Crank[k][mask] = (Crank[k][mask]\
    \ + Arank[i][mask] * Brank[j][mask]) % mod\n    \n        # M\xF6bius transform\
    \ (inverse of Zeta transform)\n        for Cr in Crank: mobius_transform(Cr, mod)\n\
    \            \n        # Combine results\n        C = [0] * Z\n        for mask\
    \ in range(Z):\n            rank = mask.bit_count()\n            C[mask] = Crank[rank][mask]\n\
    \    \n        return C\n    \n    print(*subset_convolution(F, G, mod))\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/subset_convolution\n\
    mod = 998244353\n\ndef rint(shift=0, base=10):\n    return [int(x, base) + shift\
    \ for x in input().split()]\n\n\n\nN, = rint()\nF = rint()\nG = rint()\nif N <\
    \ 10:\n    from cp_library.math.subset_convolution_fn import subset_convolution\n\
    \    from cp_library.math.mod.mint_cls import mint\n    mint.mod = mod\n    \n\
    \    F = list(map(mint, F))\n    G = list(map(mint, G))\n    print(*subset_convolution(F,\
    \ G))\nelse:\n    from cp_library.math.mod.subset_convolution_fn import subset_convolution\n\
    \    \n    print(*subset_convolution(F, G, mod))"
  dependsOn:
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
  timestamp: '2024-09-03 19:30:15+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/subset_convolution.test.py
layout: document
redirect_from:
- /verify/test/subset_convolution.test.py
- /verify/test/subset_convolution.test.py.html
title: test/subset_convolution.test.py
---
