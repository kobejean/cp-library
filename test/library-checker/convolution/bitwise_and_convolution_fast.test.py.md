---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/math/and_conv_fast_fn.py
    title: cp_library/math/and_conv_fast_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/superset_mobius_fn.py
    title: cp_library/math/superset_mobius_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/superset_zeta_fn.py
    title: cp_library/math/superset_zeta_fn.py
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
    \        \n'''\n\ndef superset_zeta(A, N: int, Z: int = None):\n    Z = 1 << N\
    \ if Z is None else Z\n    for i in range(N):\n        m = b = 1<<i\n        while\
    \ m < Z:\n            A[m ^ b] += A[m]\n            m = m+1|b\n    return A\n\n\
    def superset_mobius(A, N: int, Z: int = None):\n    Z = 1 << N if Z is None else\
    \ Z\n    for i in range(N):\n        m = b = 1<<i\n        while m < Z:\n    \
    \        A[m ^ b] -= A[m]\n            m = m+1|b\n    return A\n\ndef and_conv(A:\
    \ list[int], B: list[int], N: int, mod) -> list[int]:\n    Z = 1 << N\n    superset_zeta(A,\
    \ N, Z), superset_zeta(B, N, Z)\n    for i, b in enumerate(B): A[i] = A[i]*b%mod\n\
    \    superset_mobius(A, N, Z)\n    for i in range(Z): A[i] %= mod\n    return\
    \ A\nfrom atexit import register\nfrom os import read, write\nimport sys\nfrom\
    \ __pypy__ import builders\nclass Fastio:\n    ibuf = bytes()\n    pil = pir =\
    \ 0\n    sb = builders.StringBuilder()\n    def load(self):\n        self.ibuf\
    \ = self.ibuf[self.pil:]\n        self.ibuf += read(0, 131072)\n        self.pil\
    \ = 0; self.pir = len(self.ibuf)\n    def flush(self): write(1, self.sb.build().encode())\n\
    \    def fastin(self):\n        if self.pir - self.pil < 64: self.load()\n   \
    \     minus = x = 0\n        while self.ibuf[self.pil] < 45: self.pil += 1\n \
    \       if self.ibuf[self.pil] == 45: minus = 1; self.pil += 1\n        while\
    \ self.ibuf[self.pil] >= 48:\n            x = x * 10 + (self.ibuf[self.pil] &\
    \ 15)\n            self.pil += 1\n        if minus: return -x\n        return\
    \ x\n    def fastout(self, x): self.sb.append(str(x))\n    def fastoutln(self,\
    \ x): self.sb.append(str(x)); self.sb.append('\\n')\nfastio = Fastio()\nrd = fastio.fastin;\
    \ wt = fastio.fastout; wtn = fastio.fastoutln; flush = fastio.flush\nregister(flush)\n\
    sys.stdin = None; sys.stdout = None\ndef rdl(n): return [rd() for _ in range(n)]\n\
    def wtnl(l): wtn(' '.join(map(str, l)))\n\nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_and_convolution\n\
    \ndef main():\n    N = rd()\n    A = rdl(1 << N)\n    B = rdl(1 << N)\n    wtnl(and_conv(A,\
    \ B, N, 998244353))\n\nfrom cp_library.math.and_conv_fast_fn import and_conv\n\
    from atexit import register\nfrom os import read, write\nimport sys\nfrom __pypy__\
    \ import builders\nclass Fastio:\n    ibuf = bytes()\n    pil = pir = 0\n    sb\
    \ = builders.StringBuilder()\n    def load(self):\n        self.ibuf = self.ibuf[self.pil:]\n\
    \        self.ibuf += read(0, 131072)\n        self.pil = 0; self.pir = len(self.ibuf)\n\
    \    def flush(self): write(1, self.sb.build().encode())\n    def fastin(self):\n\
    \        if self.pir - self.pil < 64: self.load()\n        minus = x = 0\n   \
    \     while self.ibuf[self.pil] < 45: self.pil += 1\n        if self.ibuf[self.pil]\
    \ == 45: minus = 1; self.pil += 1\n        while self.ibuf[self.pil] >= 48:\n\
    \            x = x * 10 + (self.ibuf[self.pil] & 15)\n            self.pil +=\
    \ 1\n        if minus: return -x\n        return x\n    def fastout(self, x):\
    \ self.sb.append(str(x))\n    def fastoutln(self, x): self.sb.append(str(x));\
    \ self.sb.append('\\n')\nfastio = Fastio()\nrd = fastio.fastin; wt = fastio.fastout;\
    \ wtn = fastio.fastoutln; flush = fastio.flush\nregister(flush)\nsys.stdin = None;\
    \ sys.stdout = None\ndef rdl(n): return [rd() for _ in range(n)]\ndef wtnl(l):\
    \ wtn(' '.join(map(str, l)))\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - cp_library/math/and_conv_fast_fn.py
  - cp_library/math/superset_zeta_fn.py
  - cp_library/math/superset_mobius_fn.py
  isVerificationFile: true
  path: test/library-checker/convolution/bitwise_and_convolution_fast.test.py
  requiredBy: []
  timestamp: '2025-02-18 11:27:51+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/convolution/bitwise_and_convolution_fast.test.py
layout: document
redirect_from:
- /verify/test/library-checker/convolution/bitwise_and_convolution_fast.test.py
- /verify/test/library-checker/convolution/bitwise_and_convolution_fast.test.py.html
title: test/library-checker/convolution/bitwise_and_convolution_fast.test.py
---
