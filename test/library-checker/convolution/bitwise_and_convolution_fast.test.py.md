---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast/fast_io_fn.py
    title: cp_library/io/fast/fast_io_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/and_conv_fast_fn.py
    title: cp_library/math/conv/and_conv_fast_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/superset_mobius_fn.py
    title: cp_library/math/conv/superset_mobius_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/conv/superset_zeta_pair_fn.py
    title: cp_library/math/conv/superset_zeta_pair_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/bitwise_and_convolution
    links:
    - https://judge.yosupo.jp/problem/bitwise_and_convolution
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_and_convolution\n\
    \ndef main():\n    N = rd()\n    A = rdl(1 << N)\n    B = rdl(1 << N)\n    wtnl(and_conv(A,\
    \ B, N, 998244353))\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2578\n             https://kobejean.github.io/cp-library       \
    \        \n'''\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2578\n    x\u2080 \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\
    \u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u25CF\u2500\u2500\u2500\u2500\u2500\u2500\u2500\
    \u2500\u25BA X\u2080\n                \u2573          \u2572 \u2571          \u2572\
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
    \       Math - Convolution                     \n'''\n\ndef superset_zeta_pair(A:\
    \ list[int], B: list[int], N: int):\n    Z = len(A)\n    for i in range(N):\n\
    \        m = b = 1<<i\n        while m < Z: A[m^b] += A[m]; B[m^b] += B[m]; m\
    \ = m+1|b\n    return A\n\ndef superset_mobius(A, N: int):\n    Z = len(A)\n \
    \   for i in range(N):\n        m = b = 1<<i\n        while m < Z: A[m^b] -= A[m];\
    \ m = m+1|b\n    return A\n\ndef and_conv(A: list[int], B: list[int], N: int,\
    \ mod) -> list[int]:\n    assert len(A) == len(B)\n    Z = 1 << N\n    superset_zeta_pair(A,\
    \ B, N)\n    for i, b in enumerate(B): A[i] = A[i]*b%mod\n    superset_mobius(A,\
    \ N)\n    for i in range(Z): A[i] %= mod\n    return A\n\n\nfrom __pypy__.builders\
    \ import StringBuilder\nimport sys\nfrom os import read as os_read, write as os_write\n\
    from atexit import register as atexist_register\n\nclass Fastio:\n    ibuf = bytes()\n\
    \    pil = pir = 0\n    sb = StringBuilder()\n    def load(self):\n        self.ibuf\
    \ = self.ibuf[self.pil:]\n        self.ibuf += os_read(0, 131072)\n        self.pil\
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
    \ l)))\n\nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_and_convolution\n\
    \ndef main():\n    N = rd()\n    A = rdl(1 << N)\n    B = rdl(1 << N)\n    wtnl(and_conv(A,\
    \ B, N, 998244353))\n\nfrom cp_library.math.conv.and_conv_fast_fn import and_conv\n\
    from cp_library.io.fast.fast_io_fn import rd, rdl, wtnl\n\nif __name__ == '__main__':\n\
    \    main()\n"
  dependsOn:
  - cp_library/math/conv/and_conv_fast_fn.py
  - cp_library/io/fast/fast_io_fn.py
  - cp_library/math/conv/superset_zeta_pair_fn.py
  - cp_library/math/conv/superset_mobius_fn.py
  isVerificationFile: true
  path: test/library-checker/convolution/bitwise_and_convolution_fast.test.py
  requiredBy: []
  timestamp: '2025-05-20 05:03:21+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/convolution/bitwise_and_convolution_fast.test.py
layout: document
redirect_from:
- /verify/test/library-checker/convolution/bitwise_and_convolution_fast.test.py
- /verify/test/library-checker/convolution/bitwise_and_convolution_fast.test.py.html
title: test/library-checker/convolution/bitwise_and_convolution_fast.test.py
---
