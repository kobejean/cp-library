---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/dsu_cls.py
    title: cp_library/ds/dsu_cls.py
  - icon: ':question:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':question:'
    path: cp_library/io/read_int_fn.py
    title: cp_library/io/read_int_fn.py
  - icon: ':question:'
    path: cp_library/io/write_fn.py
    title: cp_library/io/write_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/unionfind
    links:
    - https://judge.yosupo.jp/problem/unionfind
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind\n\
    \n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\
    \n             https://kobejean.github.io/cp-library               \n'''\n\ndef\
    \ read(shift=0, base=10):\n    return [int(s, base) + shift for s in input().split()]\n\
    import os\nimport sys\nfrom io import BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n\
    \    BUFSIZE = 8192\n    newlines = 0\n\n    def __init__(self, file):\n     \
    \   self._fd = file.fileno()\n        self.buffer = BytesIO()\n        self.writable\
    \ = \"x\" in file.mode or \"r\" not in file.mode\n        self.write = self.buffer.write\
    \ if self.writable else None\n\n    def read(self):\n        BUFSIZE = self.BUFSIZE\n\
    \        while True:\n            b = os.read(self._fd, max(os.fstat(self._fd).st_size,\
    \ BUFSIZE))\n            if not b:\n                break\n            ptr = self.buffer.tell()\n\
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
    \ = IOWrapper(sys.stdout)\n\ndef write(*args, **kwargs):\n    \"\"\"Prints the\
    \ values to a stream, or to stdout_fast by default.\"\"\"\n    sep, file = kwargs.pop(\"\
    sep\", \" \"), kwargs.pop(\"file\", IOWrapper.stdout)\n    at_start = True\n \
    \   for x in args:\n        if not at_start:\n            file.write(sep)\n  \
    \      file.write(str(x))\n        at_start = False\n    file.write(kwargs.pop(\"\
    end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n        file.flush()\n\
    \n\nclass DSU:\n    def __init__(self, N):\n        self.N = N\n        self.par\
    \ = [-1] * N\n\n    def merge(self, u, v, src = False):\n        assert 0 <= u\
    \ < self.N\n        assert 0 <= v < self.N\n\n        x, y = self.leader(u), self.leader(v)\n\
    \        if x == y: return (x,y) if src else x\n\n        if self.par[x] > self.par[y]:\n\
    \            x, y = y, x\n\n        self.par[x] += self.par[y]\n        self.par[y]\
    \ = x\n\n        return (x,y) if src else x\n\n    def same(self, u: int, v: int):\n\
    \        assert 0 <= u < self.N\n        assert 0 <= v < self.N\n        return\
    \ self.leader(u) == self.leader(v)\n\n    def leader(self, i) -> int:\n      \
    \  assert 0 <= i < self.N\n        par = self.par\n        p = par[i]\n      \
    \  while p >= 0:\n            if par[p] < 0:\n                return p\n     \
    \       par[i], i, p = par[p], par[p], par[par[p]]\n\n        return i\n\n   \
    \ def size(self, i) -> int:\n        assert 0 <= i < self.N\n        \n      \
    \  return -self.par[self.leader(i)]\n\n    def groups(self) -> list[list[int]]:\n\
    \        leader_buf = [self.leader(i) for i in range(self.N)]\n\n        result\
    \ = [[] for _ in range(self.N)]\n        for i in range(self.N):\n           \
    \ result[leader_buf[i]].append(i)\n\n        return [r for r in result if r]\n\
    \nN, Q = read()\n\ndsu = DSU(N)\n\nfor _ in range(Q):\n    t, u, v = read()\n\
    \    if t:\n        write(int(dsu.same(u, v)))\n    else:\n        dsu.merge(u,\
    \ v)\n\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind\n\
    \nfrom cp_library.io.read_int_fn import read\nfrom cp_library.io.write_fn import\
    \ write\nfrom cp_library.ds.dsu_cls import DSU\n\nN, Q = read()\n\ndsu = DSU(N)\n\
    \nfor _ in range(Q):\n    t, u, v = read()\n    if t:\n        write(int(dsu.same(u,\
    \ v)))\n    else:\n        dsu.merge(u, v)\n\n"
  dependsOn:
  - cp_library/io/read_int_fn.py
  - cp_library/io/write_fn.py
  - cp_library/ds/dsu_cls.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: true
  path: test/library-checker/data-structure/unionfind.test.py
  requiredBy: []
  timestamp: '2025-02-18 11:27:51+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/data-structure/unionfind.test.py
layout: document
redirect_from:
- /verify/test/library-checker/data-structure/unionfind.test.py
- /verify/test/library-checker/data-structure/unionfind.test.py.html
title: test/library-checker/data-structure/unionfind.test.py
---
