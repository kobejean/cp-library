---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/butterfly/butterfly_masks_fn.py
    title: cp_library/alg/dp/butterfly/butterfly_masks_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/popcnts_fn.py
    title: cp_library/bit/popcnts_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast/fast_io_fn.py
    title: cp_library/io/fast/fast_io_fn.py
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
    \ndef main():\n    mod = 998244353\n    n = rd()\n    a = rdl(1 << n)\n    b =\
    \ rdl(1 << n)\n    wtnl(isubset_conv(a, b, n, mod))\n\n'''\n\u257A\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2578\n    x\u2080 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u25BA X\u2080\n                \u2573          \u2572 \u2571\
    \          \u2572     \u2571          \n    x\u2084 \u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25CF\u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25CF\u2500\u2572\u2500\u2500\u2500\u2571\u2500\u25CF\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u25BA X\u2081\n                           \u2573\
    \ \u2573          \u2572 \u2572 \u2571 \u2571          \n    x\u2082 \u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25CF\u2500\u2572\u2500\u2573\u2500\u2571\u2500\u25CF\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2082\n             \
    \   \u2573          \u2571 \u2572          \u2572 \u2573 \u2573 \u2571       \
    \   \n    x\u2086 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\
    \u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\
    \u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2573\u2500\
    \u2573\u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25BA X\u2083\n                                        \u2573 \u2573 \u2573 \u2573\
    \         \n    x\u2081 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2573\
    \u2500\u2573\u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25BA X\u2084\n                \u2573          \u2572 \u2571          \u2571\
    \ \u2573 \u2573 \u2572          \n    x\u2085 \u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25CF\u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25CF\u2500\u2571\u2500\u2573\u2500\u2572\u2500\u25CF\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u25BA X\u2085\n                           \u2573 \u2573\
    \          \u2571 \u2571 \u2572 \u2572          \n    x\u2083 \u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u25CF\u2500\u2573\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u25CF\u2500\u2571\u2500\u2500\u2500\u2572\u2500\u25CF\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2086\n                \u2573\
    \          \u2571 \u2572          \u2571     \u2572          \n    x\u2087 \u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u25CF\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25BA X\u2087\n\u257A\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n               \
    \  Algorithms - DP - Butterfly                     \n'''\n\ndef butterfly_masks(N,\
    \ Z):\n    for i in range(N):\n        m = b = 1<<i\n        while m < Z:\n  \
    \          yield m^b, m\n            m = (m+1)|b\n\ndef fwht(A: list, N: int):\n\
    \    for m0, m1 in butterfly_masks(N, len(A)):\n        a0, a1 = A[m0], A[m1]\n\
    \        A[m0], A[m1] = a0+a1, a0-a1\n    return A\n\ndef subset_zeta(A: list[int],\
    \ N: int):\n    for m0, m1 in butterfly_masks(N, len(A)):\n        A[m1] += A[m0]\n\
    \    return A\n\ndef subset_zeta_pair(A: list[int], B: list[int], N: int):\n \
    \   for m0, m1 in butterfly_masks(N, len(A)):\n        A[m1] += A[m0]\n      \
    \  B[m1] += B[m0]\n    return A, B\n\ndef subset_mobius(A: list[int], N: int):\n\
    \    for m0, m1 in butterfly_masks(N, len(A)):\n        A[m1] -= A[m0]\n    return\
    \ A\n\ndef superset_zeta(A, N: int):\n    for m0, m1 in butterfly_masks(N, len(A)):\n\
    \        A[m0] += A[m1]\n    return A\n\ndef superset_mobius(A, N: int):\n   \
    \ for m0, m1 in butterfly_masks(N, len(A)):\n        A[m0] -= A[m1]\n    return\
    \ A\n\ndef popcnts(N):\n    P = [0]*(1 << N)\n    for i in range(N):\n       \
    \ for m in range(b := 1<<i):\n            P[m^b] = P[m] + 1\n    return P\n\n\n\
    def subset_conv(A,B,N):\n    assert len(A) == len(B)\n    Z = (N+1)*(M := 1<<N)\n\
    \    Ar,Br,Cr,P = [0]*Z, [0]*Z, [0]*Z, popcnts(N)\n    for i,p in enumerate(P):\
    \ Ar[p<<N|i], Br[p<<N|i] = A[i], B[i]\n    subset_zeta_pair(Ar, Br, N)\n    for\
    \ i in range(0,Z,M):\n        for j in range(0,Z-i,M):\n            ij = i+j\n\
    \            for k in range(M): Cr[ij|k] += Ar[i|k] * Br[j|k]\n    subset_mobius(Cr,\
    \ N)\n    for i,p in enumerate(P): A[i] = Cr[p<<N|i]\n    return A\n\n\ndef popcnts(N):\n\
    \    P = [0]*(1 << N)\n    for i in range(N):\n        for m in range(b := 1<<i):\n\
    \            P[m^b] = P[m] + 1\n    return P\n\ndef isubset_conv(A,B,N,mod):\n\
    \    assert len(A) == len(B)\n    Z = (N+1)*(M := 1<<N)\n    Ar,Br,Cr,P = [0]*Z,\
    \ [0]*Z, [0]*Z, popcnts(N)\n    for i,p in enumerate(P): Ar[p<<N|i], Br[p<<N|i]\
    \ = A[i], B[i]\n    subset_zeta_pair(Ar, Br, N)\n    for i in range(Z): Ar[i],\
    \ Br[i] = Ar[i]%mod, Br[i]%mod\n    for i in range(0,Z,M):\n        for j in range(0,Z-i,M):\n\
    \            ij = i+j\n            for k in range(M): Cr[ijk] = (Cr[ijk:=ij|k]\
    \ + Ar[i|k] * Br[j|k]) % mod\n    subset_mobius(Cr, N)\n    for i,p in enumerate(P):\
    \ A[i] = Cr[p<<N|i] % mod\n    return A\n\n\n\nfrom __pypy__.builders import StringBuilder\n\
    import sys\nfrom os import read as os_read, write as os_write\nfrom atexit import\
    \ register as atexist_register\n\nclass Fastio:\n    ibuf = bytes()\n    pil =\
    \ pir = 0\n    sb = StringBuilder()\n    def load(self):\n        self.ibuf =\
    \ self.ibuf[self.pil:]\n        self.ibuf += os_read(0, 131072)\n        self.pil\
    \ = 0; self.pir = len(self.ibuf)\n    def flush_atexit(self): os_write(1, self.sb.build().encode())\n\
    \    def flush(self):\n        os_write(1, self.sb.build().encode())\n       \
    \ self.sb = StringBuilder()\n    def fastin(self):\n        if self.pir - self.pil\
    \ < 64: self.load()\n        minus = x = 0\n        while self.ibuf[self.pil]\
    \ < 45: self.pil += 1\n        if self.ibuf[self.pil] == 45: minus = 1; self.pil\
    \ += 1\n        while self.ibuf[self.pil] >= 48:\n            x = x * 10 + (self.ibuf[self.pil]\
    \ & 15)\n            self.pil += 1\n        if minus: return -x\n        return\
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
    \ndef main():\n    mod = 998244353\n    n = rd()\n    a = rdl(1 << n)\n    b =\
    \ rdl(1 << n)\n    wtnl(isubset_conv(a, b, n, mod))\n\nfrom cp_library.alg.dp.butterfly.butterfly_masks_fn\
    \ import subset_zeta_pair, subset_mobius\nfrom cp_library.bit.popcnts_fn import\
    \ popcnts\n\ndef isubset_conv(A,B,N,mod):\n    assert len(A) == len(B)\n    Z\
    \ = (N+1)*(M := 1<<N)\n    Ar,Br,Cr,P = [0]*Z, [0]*Z, [0]*Z, popcnts(N)\n    for\
    \ i,p in enumerate(P): Ar[p<<N|i], Br[p<<N|i] = A[i], B[i]\n    subset_zeta_pair(Ar,\
    \ Br, N)\n    for i in range(Z): Ar[i], Br[i] = Ar[i]%mod, Br[i]%mod\n    for\
    \ i in range(0,Z,M):\n        for j in range(0,Z-i,M):\n            ij = i+j\n\
    \            for k in range(M): Cr[ijk] = (Cr[ijk:=ij|k] + Ar[i|k] * Br[j|k])\
    \ % mod\n    subset_mobius(Cr, N)\n    for i,p in enumerate(P): A[i] = Cr[p<<N|i]\
    \ % mod\n    return A\n\nfrom cp_library.io.fast.fast_io_fn import rd, rdl, wtnl\n\
    \nmain()"
  dependsOn:
  - cp_library/alg/dp/butterfly/butterfly_masks_fn.py
  - cp_library/bit/popcnts_fn.py
  - cp_library/io/fast/fast_io_fn.py
  isVerificationFile: true
  path: test/library-checker/set-power-series/subset_convolution_snippet.test.py
  requiredBy: []
  timestamp: '2025-04-25 16:40:50+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/set-power-series/subset_convolution_snippet.test.py
layout: document
redirect_from:
- /verify/test/library-checker/set-power-series/subset_convolution_snippet.test.py
- /verify/test/library-checker/set-power-series/subset_convolution_snippet.test.py.html
title: test/library-checker/set-power-series/subset_convolution_snippet.test.py
---
