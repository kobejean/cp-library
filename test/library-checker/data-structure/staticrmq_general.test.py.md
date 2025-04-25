---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/min2_fn.py
    title: cp_library/alg/dp/min2_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/sparse_table_cls.py
    title: cp_library/ds/sparse_table_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast/fast_io_fn.py
    title: cp_library/io/fast/fast_io_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/staticrmq
    links:
    - https://judge.yosupo.jp/problem/staticrmq
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/staticrmq\n\
    \n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\
    \n             https://kobejean.github.io/cp-library               \n'''\n\ndef\
    \ min2(a, b):\n    return a if a < b else b\n\ndef main():\n    N, Q = rd(), rd()\n\
    \    A = rdl(N)\n    st = SparseTable(min2, A)\n    for _ in range(Q):\n     \
    \   wtn(st.query(rd(),rd()))\n\nfrom typing import Generic, Callable\nfrom typing\
    \ import TypeVar\n_T = TypeVar('T')\n\n\n\nclass SparseTable(Generic[_T]):\n \
    \   def __init__(st, op: Callable[[_T,_T],_T], arr: list[_T]):\n        st.N =\
    \ N = len(arr)\n        st.log = N.bit_length()\n        st.op = op\n        st.data\
    \ = data = [0] * (st.log*N)\n        data[:N] = arr\n        for i in range(1,st.log):\n\
    \            a, b, c = i*N, (i-1)*N, (i-1)*N + (1 << (i-1))\n            for j\
    \ in range(N - (1 << i) + 1):\n                data[a+j] = op(data[b+j], data[c+j])\n\
    \n    def query(st, l: int, r: int) -> _T:\n        k = (r-l).bit_length() - 1\n\
    \        return st.op(st.data[k*st.N + l], st.data[k*st.N + r - (1<<k)])\n\n\n\
    from __pypy__.builders import StringBuilder\nimport sys\nfrom os import read as\
    \ os_read, write as os_write\nfrom atexit import register as atexist_register\n\
    \nclass Fastio:\n    ibuf = bytes()\n    pil = pir = 0\n    sb = StringBuilder()\n\
    \    def load(self):\n        self.ibuf = self.ibuf[self.pil:]\n        self.ibuf\
    \ += os_read(0, 131072)\n        self.pil = 0; self.pir = len(self.ibuf)\n   \
    \ def flush_atexit(self): os_write(1, self.sb.build().encode())\n    def flush(self):\n\
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
    \ l)))\n\nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/staticrmq\n\
    \nfrom cp_library.alg.dp.min2_fn import min2\n\ndef main():\n    N, Q = rd(),\
    \ rd()\n    A = rdl(N)\n    st = SparseTable(min2, A)\n    for _ in range(Q):\n\
    \        wtn(st.query(rd(),rd()))\n\nfrom cp_library.ds.sparse_table_cls import\
    \ SparseTable\nfrom cp_library.io.fast.fast_io_fn import rd, rdl, wtn\n\nif __name__\
    \ == '__main__':\n    main()\n"
  dependsOn:
  - cp_library/alg/dp/min2_fn.py
  - cp_library/ds/sparse_table_cls.py
  - cp_library/io/fast/fast_io_fn.py
  isVerificationFile: true
  path: test/library-checker/data-structure/staticrmq_general.test.py
  requiredBy: []
  timestamp: '2025-04-25 16:40:50+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/data-structure/staticrmq_general.test.py
layout: document
redirect_from:
- /verify/test/library-checker/data-structure/staticrmq_general.test.py
- /verify/test/library-checker/data-structure/staticrmq_general.test.py.html
title: test/library-checker/data-structure/staticrmq_general.test.py
---
