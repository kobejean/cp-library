---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/segtree_cls.py
    title: cp_library/ds/tree/segtree_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_int_fn.py
    title: cp_library/io/read_int_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/write_fn.py
    title: cp_library/io/write_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_A
  bundledCode: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_A\n\
    \ndef main():\n    N, Q = read()\n    seg = SegTree(min, 2147483647, N)\n    for\
    \ _ in range(Q):\n        com, x, y = read()\n        if com: write(seg.prod(x,y+1))\n\
    \        else: seg[x] = y\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library \
    \              \n'''\nfrom typing import Callable, Generic, Union\nfrom typing\
    \ import TypeVar\n_T = TypeVar('T')\n\n\n\nclass SegTree(Generic[_T]):\n    def\
    \ __init__(seg, op: Callable[[_T, _T], _T], e: _T, v: Union[int, list[_T]]) ->\
    \ None:\n        if isinstance(v, int): v = [e] * v\n        seg.op, seg.e, seg.n\
    \ = op, e, (n := len(v))\n        seg.log, seg.sz, seg.d = (log := (n-1).bit_length()+1),\
    \ (sz := 1 << log), [e] * (sz << 1)\n        for i in range(n): seg.d[sz + i]\
    \ = v[i]\n        for i in range(sz-1,0,-1): seg.d[i] = op(seg.d[i<<1], seg.d[i<<1|1])\n\
    \n    def set(seg, p: int, x: _T) -> None:\n        seg.d[p := p + seg.sz], op\
    \ = x, seg.op\n        for _ in range(seg.log): seg.d[p:=p>>1] = op(seg.d[p:=p^(p&1)],\
    \ seg.d[p|1])\n    __setitem__ = set\n\n    def get(seg, p: int) -> _T:\n    \
    \    return seg.d[p + seg.sz]\n    __getitem__ = get\n\n    def prod(seg, l: int,\
    \ r: int) -> _T:\n        sml = smr = seg.e\n        l, r = l+seg.sz, r+seg.sz\n\
    \        while l < r:\n            if l&1: sml, l = seg.op(sml, seg.d[l]), l+1\n\
    \            if r&1: smr = seg.op(seg.d[r:=r-1], smr)\n            l, r = l >>\
    \ 1, r >> 1\n        return seg.op(sml, smr)\n\n    def all_prod(seg) -> _T:\n\
    \        return seg.d[1]\n\n    def max_right(seg, l: int, f: Callable[[_T], bool])\
    \ -> int:\n        assert 0 <= l <= seg.n\n        assert f(seg.e)\n        if\
    \ l == seg.n: return seg.n\n        l, op, d, sm = l+(sz := seg.sz), seg.op, seg.d,\
    \ seg.e\n        while True:\n            while l&1 == 0: l >>= 1\n          \
    \  if not f(op(sm, d[l])):\n                while l < sz:\n                  \
    \  if f(op(sm, d[l:=l<<1])): sm, l = op(sm, d[l]), l+1\n                return\
    \ l - sz\n            sm, l = op(sm, d[l]), l+1\n            if l&-l == l: return\
    \ seg.n\n\n    def min_left(seg, r: int, f: Callable[[_T], bool]) -> int:\n  \
    \      assert 0 <= r <= seg.n\n        assert f(seg.e)\n        if r == 0: return\
    \ 0\n        r, op, d, sm = r+(sz := seg.sz), seg.op, seg.d, seg.e\n        while\
    \ True:\n            r -= 1\n            while r > 1 and r & 1: r >>= 1\n    \
    \        if not f(op(d[r], sm)):\n                while r < sz:\n            \
    \        if f(op(d[r:=r<<1|1], sm)): sm, r = op(d[r], sm), r-1\n             \
    \   return r + 1 - sz\n            sm = op(d[r], sm)\n            if (r & -r)\
    \ == r: return 0\n\n\ndef read(shift=0, base=10):\n    return [int(s, base) +\
    \ shift for s in input().split()]\nimport os\nimport sys\nfrom io import BytesIO,\
    \ IOBase\n\n\nclass FastIO(IOBase):\n    BUFSIZE = 8192\n    newlines = 0\n\n\
    \    def __init__(self, file):\n        self._fd = file.fileno()\n        self.buffer\
    \ = BytesIO()\n        self.writable = \"x\" in file.mode or \"r\" not in file.mode\n\
    \        self.write = self.buffer.write if self.writable else None\n\n    def\
    \ read(self):\n        BUFSIZE = self.BUFSIZE\n        while True:\n         \
    \   b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))\n        \
    \    if not b:\n                break\n            ptr = self.buffer.tell()\n\
    \            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)\n\
    \        self.newlines = 0\n        return self.buffer.read()\n\n    def readline(self):\n\
    \        BUFSIZE = self.BUFSIZE\n        while self.newlines == 0:\n         \
    \   b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))\n        \
    \    self.newlines = b.count(b\"\\n\") + (not b)\n            ptr = self.buffer.tell()\n\
    \            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)\n\
    \        self.newlines -= 1\n        return self.buffer.readline()\n\n    def\
    \ flush(self):\n        if self.writable:\n            os.write(self._fd, self.buffer.getvalue())\n\
    \            self.buffer.truncate(0), self.buffer.seek(0)\n\n\nclass IOWrapper(IOBase):\n\
    \    stdin: 'IOWrapper' = None\n    stdout: 'IOWrapper' = None\n    \n    def\
    \ __init__(self, file):\n        self.buffer = FastIO(file)\n        self.flush\
    \ = self.buffer.flush\n        self.writable = self.buffer.writable\n\n    def\
    \ write(self, s):\n        return self.buffer.write(s.encode(\"ascii\"))\n   \
    \ \n    def read(self):\n        return self.buffer.read().decode(\"ascii\")\n\
    \    \n    def readline(self):\n        return self.buffer.readline().decode(\"\
    ascii\")\n\nsys.stdin = IOWrapper.stdin = IOWrapper(sys.stdin)\nsys.stdout = IOWrapper.stdout\
    \ = IOWrapper(sys.stdout)\n\ndef write(*args, **kwargs):\n    '''Prints the values\
    \ to a stream, or to stdout_fast by default.'''\n    sep, file = kwargs.pop(\"\
    sep\", \" \"), kwargs.pop(\"file\", IOWrapper.stdout)\n    at_start = True\n \
    \   for x in args:\n        if not at_start:\n            file.write(sep)\n  \
    \      file.write(str(x))\n        at_start = False\n    file.write(kwargs.pop(\"\
    end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n        file.flush()\n\
    \nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_A\n\
    \ndef main():\n    N, Q = read()\n    seg = SegTree(min, 2147483647, N)\n    for\
    \ _ in range(Q):\n        com, x, y = read()\n        if com: write(seg.prod(x,y+1))\n\
    \        else: seg[x] = y\n\nfrom cp_library.ds.tree.segtree_cls import SegTree\n\
    from cp_library.io.read_int_fn import read\nfrom cp_library.io.write_fn import\
    \ write\n\nif __name__ == '__main__':\n    main()"
  dependsOn:
  - cp_library/ds/tree/segtree_cls.py
  - cp_library/io/read_int_fn.py
  - cp_library/io/write_fn.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: true
  path: test/aoj/dsl/dsl_2_a_segtree.test.py
  requiredBy: []
  timestamp: '2025-04-03 08:59:41+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/dsl/dsl_2_a_segtree.test.py
layout: document
redirect_from:
- /verify/test/aoj/dsl/dsl_2_a_segtree.test.py
- /verify/test/aoj/dsl/dsl_2_a_segtree.test.py.html
title: test/aoj/dsl/dsl_2_a_segtree.test.py
---
