---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/max2_fn.py
    title: cp_library/alg/dp/max2_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/popcnts_fn.py
    title: cp_library/bit/popcnts_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast/fast_io_fn.py
    title: cp_library/io/fast/fast_io_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/ior_mobius_ranked_fn.py
    title: cp_library/math/conv/ior_mobius_ranked_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/ior_zeta_pair_ranked_fn.py
    title: cp_library/math/conv/ior_zeta_pair_ranked_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/mod/isubset_conv_ranked_fn.py
    title: cp_library/math/conv/mod/isubset_conv_ranked_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/mod/isubset_deconv_ranked_fn.py
    title: cp_library/math/conv/mod/isubset_deconv_ranked_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/mod/subset_conv_fn.py
    title: cp_library/math/conv/mod/subset_conv_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/mod/subset_deconv_fn.py
    title: cp_library/math/conv/mod/subset_deconv_fn.py
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
    \ndef main():\n    mod, n = 998244353, rd()\n    A, B = rdl(1<<n), rdl(1<<n)\n\
    \    C = subset_conv(A, B, n, mod)\n    wtnl(C)\n    assert subset_deconv(C, B,\
    \ n, mod) == A\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2578\n             https://kobejean.github.io/cp-library             \
    \  \n'''\n\n\ndef popcnts(N):\n    P = [0]*(1 << N)\n    for i in range(N):\n\
    \        for m in range(b := 1<<i):\n            P[m^b] = P[m] + 1\n    return\
    \ P\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n    x\u2080 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\
    \u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\
    \u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25BA X\u2080\n                \u2573          \u2572 \u2571          \u2572\
    \     \u2571          \n    x\u2084 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u2572\u2500\u2500\u2500\u2571\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u25BA X\u2081\n                           \u2573 \u2573   \
    \       \u2572 \u2572 \u2571 \u2571          \n    x\u2082 \u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u2572\u2500\u2573\u2500\u2571\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2082\n                \u2573   \
    \       \u2571 \u2572          \u2572 \u2573 \u2573 \u2571          \n    x\u2086\
    \ \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\u2573\u2500\u2573\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2083\n \
    \                                       \u2573 \u2573 \u2573 \u2573         \n\
    \    x\u2081 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\u2573\
    \u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA\
    \ X\u2084\n                \u2573          \u2572 \u2571          \u2571 \u2573\
    \ \u2573 \u2572          \n    x\u2085 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u2571\u2500\u2573\u2500\u2572\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u25BA X\u2085\n                           \u2573 \u2573   \
    \       \u2571 \u2571 \u2572 \u2572          \n    x\u2083 \u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u2571\u2500\u2500\u2500\u2572\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2086\n                \u2573   \
    \       \u2571 \u2572          \u2571     \u2572          \n    x\u2087 \u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2087\n\u257A\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n               \
    \       Math - Convolution                     \n'''\n\n\ndef max2(a, b):\n  \
    \  return a if a > b else b\n\n\ndef ior_zeta_pair_ranked(A, B, N, M, Z):\n  \
    \  for i in range(0, Z, M):\n        l, r = i+(1<<(i>>N))-1, i+M\n        for\
    \ j in range(N):\n            m = l|(b := 1<<j)\n            while m < r: A[m]\
    \ += A[m^b]; B[m] += B[m^b]; m = m+1|b\n    return A, B\n\ndef ior_mobius_ranked(A:\
    \ list[int], N: int, M: int, Z: int):\n    for i in range(0, Z, M):\n        l,\
    \ r = i, i+M-(1<<(N-(i>>N)))+1\n        for j in range(N):\n            m = l|(b\
    \ := 1<<j)\n            while m < r: A[m] -= A[m^b]; m = m+1|b\n    return A\n\
    \ndef isubset_conv_ranked(Ar, Br, N, M, Z, mod) -> list[int]:\n    ior_zeta_pair_ranked(Ar,\
    \ Br, N, M, Z)\n    for i in range(Z): Ar[i], Br[i] = Ar[i]%mod, Br[i]%mod\n \
    \   for ij in range(Z-M,-1,-M):\n        for k in range(M): Ar[ij|k] = (Ar[ij|k]\
    \ * Br[k]) % mod\n        r = M-(1 << (N-(ij>>N)))+1\n        for i in range(0,ij,M):\n\
    \            j = ij-i; l = (1 << (max2(i,j)>>N))-1\n            for k in range(l,r):\
    \ Ar[ij|k] += Ar[i|k] * Br[j|k] % mod\n    return ior_mobius_ranked(Ar, N, M,\
    \ Z)\n\ndef subset_conv(A: list[int], B: list[int], N: int, mod: int) -> list[int]:\n\
    \    Z = (N+1)*(M:=1<<N)\n    Ar, Br, C, P = [0]*Z, [0]*Z, [0]*M, popcnts(N)\n\
    \    for i, p in enumerate(P): Ar[p<<N|i], Br[p<<N|i] = A[i], B[i]\n    isubset_conv_ranked(Ar,\
    \ Br, N, M, Z, mod)\n    for i, p in enumerate(P): C[i] = Ar[p<<N|i] % mod\n \
    \   return C\n\ndef isubset_deconv_ranked(Ar, Br, N, Z, M, mod):\n    inv = pow(Br[0],\
    \ -1, mod); ior_zeta_pair_ranked(Ar, Br, N, M, Z)\n    for i in range(Z): Br[i],\
    \ Ar[i] = Br[i]%mod, Ar[i]%mod\n    for i in range(0, Z, M):\n        for k in\
    \ range(M): Ar[i|k] = Ar[i|k] * inv % mod\n        for j in range(M, Z-i, M):\n\
    \            ij = i + j; l = (1 << (j>>N))-1\n            for k in range(l,M):\
    \ Ar[ij|k] -= Ar[i|k] * Br[j|k] % mod\n    return ior_mobius_ranked(Ar, N, M,\
    \ Z)\n\ndef subset_deconv(A: list[int], B: list[int], N: int, mod: int) -> list[int]:\n\
    \    Z = (N+1)*(M:=1<<N)\n    Ar, Br, C, P = [0]*Z, [0]*Z, [0]*M, popcnts(N)\n\
    \    for i, p in enumerate(P): Ar[p<<N|i], Br[p<<N|i] = A[i], B[i]\n    isubset_deconv_ranked(Ar,\
    \ Br, N, Z, M, mod)\n    for i, p in enumerate(P): C[i] = Ar[p<<N|i] % mod\n \
    \   return C\n\n\nfrom __pypy__.builders import StringBuilder\nimport sys\nfrom\
    \ os import read as os_read, write as os_write\nfrom atexit import register as\
    \ atexist_register\n\nclass Fastio:\n    ibuf = bytes()\n    pil = pir = 0\n \
    \   sb = StringBuilder()\n    def load(self):\n        self.ibuf = self.ibuf[self.pil:]\n\
    \        self.ibuf += os_read(0, 131072)\n        self.pil = 0; self.pir = len(self.ibuf)\n\
    \    def flush_atexit(self): os_write(1, self.sb.build().encode())\n    def flush(self):\n\
    \        os_write(1, self.sb.build().encode())\n        self.sb = StringBuilder()\n\
    \    def fastin(self):\n        if self.pir - self.pil < 64: self.load()\n   \
    \     minus = x = 0\n        while self.ibuf[self.pil] < 45: self.pil += 1\n \
    \       if self.ibuf[self.pil] == 45: minus = 1; self.pil += 1\n        while\
    \ self.ibuf[self.pil] >= 48:\n            x = x * 10 + (self.ibuf[self.pil] &\
    \ 15)\n            self.pil += 1\n        if minus: return -x\n        return\
    \ x\n    def fastin_string(self):\n        if self.pir - self.pil < 64: self.load()\n\
    \        while self.ibuf[self.pil] <= 32: self.pil += 1\n        res = bytearray()\n\
    \        while self.ibuf[self.pil] > 32:\n            if self.pir - self.pil <\
    \ 64: self.load()\n            res.append(self.ibuf[self.pil])\n            self.pil\
    \ += 1\n        return res\n    def fastout(self, x): self.sb.append(str(x))\n\
    \    def fastoutln(self, x): self.sb.append(str(x)); self.sb.append('\\n')\nfastio\
    \ = Fastio()\nrd = fastio.fastin; rds = fastio.fastin_string; wt = fastio.fastout;\
    \ wtn = fastio.fastoutln; flush = fastio.flush\natexist_register(fastio.flush_atexit)\n\
    sys.stdin = None; sys.stdout = None\ndef rdl(n):\n    lst = [0]*n\n    for i in\
    \ range(n): lst[i] = rd()\n    return lst\ndef wtnl(l): wtn(' '.join(map(str,\
    \ l)))\n\nmain()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/subset_convolution\n\
    \ndef main():\n    mod, n = 998244353, rd()\n    A, B = rdl(1<<n), rdl(1<<n)\n\
    \    C = subset_conv(A, B, n, mod)\n    wtnl(C)\n    assert subset_deconv(C, B,\
    \ n, mod) == A\n\nfrom cp_library.math.conv.mod.subset_conv_fn import subset_conv\n\
    from cp_library.math.conv.mod.subset_deconv_fn import subset_deconv\nfrom cp_library.io.fast.fast_io_fn\
    \ import rd, rdl, wtnl\n\nmain()"
  dependsOn:
  - cp_library/math/conv/mod/subset_conv_fn.py
  - cp_library/math/conv/mod/subset_deconv_fn.py
  - cp_library/io/fast/fast_io_fn.py
  - cp_library/bit/popcnts_fn.py
  - cp_library/math/conv/mod/isubset_conv_ranked_fn.py
  - cp_library/math/conv/mod/isubset_deconv_ranked_fn.py
  - cp_library/alg/dp/max2_fn.py
  - cp_library/math/conv/ior_zeta_pair_ranked_fn.py
  - cp_library/math/conv/ior_mobius_ranked_fn.py
  isVerificationFile: true
  path: test/library-checker/set-power-series/subset_convolution.test.py
  requiredBy: []
  timestamp: '2025-07-28 10:42:29+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/set-power-series/subset_convolution.test.py
layout: document
redirect_from:
- /verify/test/library-checker/set-power-series/subset_convolution.test.py
- /verify/test/library-checker/set-power-series/subset_convolution.test.py.html
title: test/library-checker/set-power-series/subset_convolution.test.py
---
