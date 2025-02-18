---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/popcnts_fn.py
    title: cp_library/bit/popcnts_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/subset_conv_fn.py
    title: cp_library/math/mod/subset_conv_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/subset_mobius_fn.py
    title: cp_library/math/subset_mobius_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/subset_zeta_pair_fn.py
    title: cp_library/math/subset_zeta_pair_fn.py
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
    \ rdl(1 << n)\n    wtnl(subset_conv(a, b, n, mod))\n\n'''\n\u257A\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\n\ndef popcnts(N):\n    P = [0]*(1 << N)\n    for i in\
    \ range(N):\n        for m in range(b := 1<<i):\n            P[m^b] = P[m] + 1\n\
    \    return P\n\ndef subset_zeta_pair(A: list[int], B: list[int], N: int, Z: int\
    \ = None):\n    Z = 1 << N if Z is None else Z\n    for i in range(N):\n     \
    \   m = b = 1<<i\n        while m < Z:\n            A[m] += A[m^b]\n         \
    \   B[m] += B[m^b]\n            m = m+1|b\n    return A\n\ndef subset_mobius(A:\
    \ list[int], N: int, Z: int = None):\n    Z = 1 << N if Z is None else Z\n   \
    \ for i in range(N):\n        m = b = 1<<i\n        while m < Z:\n           \
    \ A[m] -= A[m^b]\n            m = m+1|b\n    return A\n\ndef subset_conv(A,B,N,mod):\n\
    \    Z = (N+1)*(M := 1<<N)\n    Ar,Br,Cr,P = [0]*Z, [0]*Z, [0]*Z, popcnts(N)\n\
    \    for i,p in enumerate(P): Ar[p<<N|i], Br[p<<N|i] = A[i], B[i]\n    subset_zeta_pair(Ar,\
    \ Br, N, Z)\n    for i in range(Z): Ar[i], Br[i] = Ar[i]%mod, Br[i]%mod\n    for\
    \ i in range(0,Z,M):\n        for j in range(0,Z-i,M):\n            ij = i+j\n\
    \            for k in range(M): Cr[ijk] = (Cr[ijk:=ij|k] + Ar[i|k] * Br[j|k])\
    \ % mod\n    subset_mobius(Cr, N, Z)\n    for i,p in enumerate(P): A[i] = Cr[p<<N|i]\
    \ % mod\n    return A\n\nfrom atexit import register\nfrom os import read, write\n\
    import sys\nfrom __pypy__ import builders\nclass Fastio:\n    ibuf = bytes()\n\
    \    pil = pir = 0\n    sb = builders.StringBuilder()\n    def load(self):\n \
    \       self.ibuf = self.ibuf[self.pil:]\n        self.ibuf += read(0, 131072)\n\
    \        self.pil = 0; self.pir = len(self.ibuf)\n    def flush(self): write(1,\
    \ self.sb.build().encode())\n    def fastin(self):\n        if self.pir - self.pil\
    \ < 64: self.load()\n        minus = x = 0\n        while self.ibuf[self.pil]\
    \ < 45: self.pil += 1\n        if self.ibuf[self.pil] == 45: minus = 1; self.pil\
    \ += 1\n        while self.ibuf[self.pil] >= 48:\n            x = x * 10 + (self.ibuf[self.pil]\
    \ & 15)\n            self.pil += 1\n        if minus: return -x\n        return\
    \ x\n    def fastout(self, x): self.sb.append(str(x))\n    def fastoutln(self,\
    \ x): self.sb.append(str(x)); self.sb.append('\\n')\nfastio = Fastio()\nrd = fastio.fastin;\
    \ wt = fastio.fastout; wtn = fastio.fastoutln; flush = fastio.flush\nregister(flush)\n\
    sys.stdin = None; sys.stdout = None\ndef rdl(n): return [rd() for _ in range(n)]\n\
    def wtnl(l): wtn(' '.join(map(str, l)))\n\nmain()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/subset_convolution\n\
    \ndef main():\n    mod = 998244353\n    n = rd()\n    a = rdl(1 << n)\n    b =\
    \ rdl(1 << n)\n    wtnl(subset_conv(a, b, n, mod))\n\nfrom cp_library.math.mod.subset_conv_fn\
    \ import subset_conv\n\nfrom atexit import register\nfrom os import read, write\n\
    import sys\nfrom __pypy__ import builders\nclass Fastio:\n    ibuf = bytes()\n\
    \    pil = pir = 0\n    sb = builders.StringBuilder()\n    def load(self):\n \
    \       self.ibuf = self.ibuf[self.pil:]\n        self.ibuf += read(0, 131072)\n\
    \        self.pil = 0; self.pir = len(self.ibuf)\n    def flush(self): write(1,\
    \ self.sb.build().encode())\n    def fastin(self):\n        if self.pir - self.pil\
    \ < 64: self.load()\n        minus = x = 0\n        while self.ibuf[self.pil]\
    \ < 45: self.pil += 1\n        if self.ibuf[self.pil] == 45: minus = 1; self.pil\
    \ += 1\n        while self.ibuf[self.pil] >= 48:\n            x = x * 10 + (self.ibuf[self.pil]\
    \ & 15)\n            self.pil += 1\n        if minus: return -x\n        return\
    \ x\n    def fastout(self, x): self.sb.append(str(x))\n    def fastoutln(self,\
    \ x): self.sb.append(str(x)); self.sb.append('\\n')\nfastio = Fastio()\nrd = fastio.fastin;\
    \ wt = fastio.fastout; wtn = fastio.fastoutln; flush = fastio.flush\nregister(flush)\n\
    sys.stdin = None; sys.stdout = None\ndef rdl(n): return [rd() for _ in range(n)]\n\
    def wtnl(l): wtn(' '.join(map(str, l)))\n\nmain()"
  dependsOn:
  - cp_library/math/mod/subset_conv_fn.py
  - cp_library/bit/popcnts_fn.py
  - cp_library/math/subset_zeta_pair_fn.py
  - cp_library/math/subset_mobius_fn.py
  isVerificationFile: true
  path: test/library-checker/set-power-series/subset_convolution.test.py
  requiredBy: []
  timestamp: '2025-02-18 11:27:51+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/set-power-series/subset_convolution.test.py
layout: document
redirect_from:
- /verify/test/library-checker/set-power-series/subset_convolution.test.py
- /verify/test/library-checker/set-power-series/subset_convolution.test.py.html
title: test/library-checker/set-power-series/subset_convolution.test.py
---
