---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/divcon/bisect_left_fn.py
    title: cp_library/alg/divcon/bisect_left_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/chmin_fn.py
    title: cp_library/alg/dp/chmin_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/lis_fn.py
    title: cp_library/alg/dp/lis_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/max2_fn.py
    title: cp_library/alg/dp/max2_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast/fast_io_fn.py
    title: cp_library/io/fast/fast_io_fn.py
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
    \  \n'''\n\n\n\ndef bisect_left(A, x, l, r):\n    while l<r:\n        if A[m:=(l+r)>>1]<x:l=m+1\n\
    \        else:r=m\n    return l\n\n\ndef max2(a, b):\n    return a if a > b else\
    \ b\n\ndef chmin(dp, i, v):\n    if ch:=dp[i]>v:dp[i]=v\n    return ch\n\ndef\
    \ lis(A: list):\n    '''Returns indices of a longest increasing sequence'''\n\
    \    N = len(A)\n    mn, mx = min(A), max(A)\n    dp, idx, prev = [mx+1]*(N+1),\
    \ [-1]*(N+1), [-1]*N\n    dp[0], r = mn-1, 0\n    for i,a in enumerate(A):\n \
    \       if chmin(dp, p := bisect_left(dp,a,0,r+1), a):\n            idx[p], prev[i],\
    \ r = i, idx[p-1], max2(r,p)\n    ans, i = [0]*r, idx[r]\n    for j in range(r-1,-1,-1):\
    \ ans[j], i = i, prev[i]\n    return ans\n\n    \n\n\n\nfrom __pypy__.builders\
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
    \ l)))\n\nmain()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/longest_increasing_subsequence\n\
    def main():\n    N = rd()\n    A = rdl(N)\n    ans = lis(A)\n    wtn(len(ans))\n\
    \    wtnl(ans)\n\nfrom cp_library.alg.dp.lis_fn import lis\nfrom cp_library.io.fast.fast_io_fn\
    \ import rd, rdl, wtn, wtnl\n\nmain()"
  dependsOn:
  - cp_library/alg/dp/lis_fn.py
  - cp_library/io/fast/fast_io_fn.py
  - cp_library/alg/divcon/bisect_left_fn.py
  - cp_library/alg/dp/max2_fn.py
  - cp_library/alg/dp/chmin_fn.py
  isVerificationFile: true
  path: test/library-checker/other/longest_increasing_sequence.test.py
  requiredBy: []
  timestamp: '2025-05-19 05:52:10+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/other/longest_increasing_sequence.test.py
layout: document
redirect_from:
- /verify/test/library-checker/other/longest_increasing_sequence.test.py
- /verify/test/library-checker/other/longest_increasing_sequence.test.py.html
title: test/library-checker/other/longest_increasing_sequence.test.py
---
