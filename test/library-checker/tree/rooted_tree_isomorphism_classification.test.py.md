---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/rev_enumerate_fn.py
    title: cp_library/alg/iter/rev_enumerate_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast/fast_io_fn.py
    title: cp_library/io/fast/fast_io_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/rooted_tree_isomorphism_classification
    links:
    - https://judge.yosupo.jp/problem/rooted_tree_isomorphism_classification
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/rooted_tree_isomorphism_classification\n\
    \ndef main():\n    N = rd()\n    P = rdl(N-1)\n    if all(i == p for i,p in enumerate(P)):\n\
    \        wtn(N)\n        P.append(N-1)\n        wtnl(P)\n        return\n\n  \
    \  H = gen(N+1)\n    sz = [1]*N\n    ans = [1]*N\n    for i, p in rev_enumerate(P,\
    \ 1):\n        ans[p] = mul(ans[p], ans[i] + H[sz[i]])\n        sz[p] += sz[i]\n\
    \    ids = { a: i for i, a in enumerate(set(ans)) }\n    for i,a in enumerate(ans):\n\
    \        ans[i] = ids[a]\n    wtn(len(ids))\n    wtnl(ans)\n\ndef mul(a: int,\
    \ b: int) -> int:\n    au, ad = a >> 31, a & 0x7fffffff\n    bu, bd = b >> 31,\
    \ b & 0x7fffffff\n    m = ad * bu + au * bd\n    mu, md = m >> 30, m & 0x3fffffff\n\
    \    x = (au*bu<<1) + mu + (md << 31) + ad * bd\n    xu, xd = x >> 61, x & 0x1fffffffffffffff\n\
    \    res = xu + xd\n    return res if res < 0x1fffffffffffffff else res - 0x1fffffffffffffff\n\
    \nfrom random import randint\n\ndef gen(N: int):\n    seed = randint(0, 0xffffffff)\n\
    \    H = [0]*N\n    for i in range(N):\n        seed ^= seed<<13&0xFFFFFFFF\n\
    \        seed ^= seed>>17&0xFFFFFFFF\n        seed ^= seed<<5&0xFFFFFFFF\n   \
    \     H[i] = seed &0xFFFFFFFF\n    return H\n\n'''\n\u257A\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\nfrom typing import Reversible\n\ndef rev_enumerate(A: Reversible,\
    \ start: int = 0):\n    start += (N := len(A))\n    for i in range(N-1,-1,-1):\n\
    \        yield (start:=start-1), A[i]\nfrom __pypy__.builders import StringBuilder\n\
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
    sys.stdin = None; sys.stdout = None\ndef rdl(n): return [rd() for _ in range(n)]\n\
    def wtnl(l): wtn(' '.join(map(str, l)))\n\nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/rooted_tree_isomorphism_classification\n\
    \ndef main():\n    N = rd()\n    P = rdl(N-1)\n    if all(i == p for i,p in enumerate(P)):\n\
    \        wtn(N)\n        P.append(N-1)\n        wtnl(P)\n        return\n\n  \
    \  H = gen(N+1)\n    sz = [1]*N\n    ans = [1]*N\n    for i, p in rev_enumerate(P,\
    \ 1):\n        ans[p] = mul(ans[p], ans[i] + H[sz[i]])\n        sz[p] += sz[i]\n\
    \    ids = { a: i for i, a in enumerate(set(ans)) }\n    for i,a in enumerate(ans):\n\
    \        ans[i] = ids[a]\n    wtn(len(ids))\n    wtnl(ans)\n\ndef mul(a: int,\
    \ b: int) -> int:\n    au, ad = a >> 31, a & 0x7fffffff\n    bu, bd = b >> 31,\
    \ b & 0x7fffffff\n    m = ad * bu + au * bd\n    mu, md = m >> 30, m & 0x3fffffff\n\
    \    x = (au*bu<<1) + mu + (md << 31) + ad * bd\n    xu, xd = x >> 61, x & 0x1fffffffffffffff\n\
    \    res = xu + xd\n    return res if res < 0x1fffffffffffffff else res - 0x1fffffffffffffff\n\
    \nfrom random import randint\n\ndef gen(N: int):\n    seed = randint(0, 0xffffffff)\n\
    \    H = [0]*N\n    for i in range(N):\n        seed ^= seed<<13&0xFFFFFFFF\n\
    \        seed ^= seed>>17&0xFFFFFFFF\n        seed ^= seed<<5&0xFFFFFFFF\n   \
    \     H[i] = seed &0xFFFFFFFF\n    return H\n\nfrom cp_library.alg.iter.rev_enumerate_fn\
    \ import rev_enumerate\nfrom cp_library.io.fast.fast_io_fn import rd, rdl, wtn,\
    \ wtnl\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - cp_library/alg/iter/rev_enumerate_fn.py
  - cp_library/io/fast/fast_io_fn.py
  isVerificationFile: true
  path: test/library-checker/tree/rooted_tree_isomorphism_classification.test.py
  requiredBy: []
  timestamp: '2025-03-30 20:17:47+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/tree/rooted_tree_isomorphism_classification.test.py
layout: document
redirect_from:
- /verify/test/library-checker/tree/rooted_tree_isomorphism_classification.test.py
- /verify/test/library-checker/tree/rooted_tree_isomorphism_classification.test.py.html
title: test/library-checker/tree/rooted_tree_isomorphism_classification.test.py
---
