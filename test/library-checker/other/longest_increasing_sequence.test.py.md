---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/alg/dp/chmin_fn.py
    title: cp_library/alg/dp/chmin_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/lis_fn.py
    title: cp_library/alg/dp/lis_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/max2_fn.py
    title: cp_library/alg/dp/max2_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/longest_increasing_subsequence
    links:
    - https://judge.yosupo.jp/problem/longest_increasing_subsequence
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/longest_increasing_subsequence\n\
    def main():\n    N = rd()\n    A = rdl(N)\n    ans = lis(A)\n    wtn(len(ans))\n\
    \    wtnl(ans)\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2578\n             https://kobejean.github.io/cp-library             \
    \  \n'''\nfrom bisect import bisect_left\n\n\n\ndef max2(a, b):\n    return a\
    \ if a > b else b\n\ndef chmin(dp, i, v):\n    if ch:=dp[i]>v:dp[i]=v\n    return\
    \ ch\n\ndef lis(A: list):\n    N = len(A)\n    mn, mx = min(A), max(A)\n    dp,\
    \ idx, prev = [mx+1]*(N+1), [-1]*(N+1), [-1]*N\n    dp[0], r = mn-1, 0\n    for\
    \ i,a in enumerate(A):\n        if chmin(dp, p := bisect_left(dp,a,hi=r+1), a):\n\
    \            idx[p], prev[i], r = i, idx[p-1], max2(r,p)\n    ans, i = [0]*r,\
    \ idx[r]\n    for j in range(r-1,-1,-1): ans[j], i = i, prev[i]\n    return ans\n\
    \n    \n\n\nfrom atexit import register\nfrom os import read, write\nimport sys\n\
    from __pypy__ import builders\nclass Fastio:\n    ibuf = bytes()\n    pil = pir\
    \ = 0\n    sb = builders.StringBuilder()\n    def load(self):\n        self.ibuf\
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
    def wtnl(l): wtn(' '.join(map(str, l)))\n\nmain()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/longest_increasing_subsequence\n\
    def main():\n    N = rd()\n    A = rdl(N)\n    ans = lis(A)\n    wtn(len(ans))\n\
    \    wtnl(ans)\n\nfrom cp_library.alg.dp.lis_fn import lis\n\nfrom atexit import\
    \ register\nfrom os import read, write\nimport sys\nfrom __pypy__ import builders\n\
    class Fastio:\n    ibuf = bytes()\n    pil = pir = 0\n    sb = builders.StringBuilder()\n\
    \    def load(self):\n        self.ibuf = self.ibuf[self.pil:]\n        self.ibuf\
    \ += read(0, 131072)\n        self.pil = 0; self.pir = len(self.ibuf)\n    def\
    \ flush(self): write(1, self.sb.build().encode())\n    def fastin(self):\n   \
    \     if self.pir - self.pil < 64: self.load()\n        minus = x = 0\n      \
    \  while self.ibuf[self.pil] < 45: self.pil += 1\n        if self.ibuf[self.pil]\
    \ == 45: minus = 1; self.pil += 1\n        while self.ibuf[self.pil] >= 48:\n\
    \            x = x * 10 + (self.ibuf[self.pil] & 15)\n            self.pil +=\
    \ 1\n        if minus: return -x\n        return x\n    def fastout(self, x):\
    \ self.sb.append(str(x))\n    def fastoutln(self, x): self.sb.append(str(x));\
    \ self.sb.append('\\n')\nfastio = Fastio()\nrd = fastio.fastin; wt = fastio.fastout;\
    \ wtn = fastio.fastoutln; flush = fastio.flush\nregister(flush)\nsys.stdin = None;\
    \ sys.stdout = None\ndef rdl(n): return [rd() for _ in range(n)]\ndef wtnl(l):\
    \ wtn(' '.join(map(str, l)))\n\nmain()"
  dependsOn:
  - cp_library/alg/dp/lis_fn.py
  - cp_library/alg/dp/max2_fn.py
  - cp_library/alg/dp/chmin_fn.py
  isVerificationFile: true
  path: test/library-checker/other/longest_increasing_sequence.test.py
  requiredBy: []
  timestamp: '2025-03-28 19:21:24+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/other/longest_increasing_sequence.test.py
layout: document
redirect_from:
- /verify/test/library-checker/other/longest_increasing_sequence.test.py
- /verify/test/library-checker/other/longest_increasing_sequence.test.py.html
title: test/library-checker/other/longest_increasing_sequence.test.py
---
