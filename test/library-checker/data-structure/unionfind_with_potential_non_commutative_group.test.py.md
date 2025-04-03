---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/potentialized_dsu_cls.py
    title: PotentializedDSU (generalized with groups)
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
    PROBLEM: https://judge.yosupo.jp/problem/unionfind_with_potential_non_commutative_group
    links:
    - https://judge.yosupo.jp/problem/unionfind_with_potential_non_commutative_group
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind_with_potential_non_commutative_group\n\
    \nmod = 998244353\n\ndef main():\n    N, Q = read()\n    pdsu = PotentializedDSU(matmul2,matinv2,e,N)\n\
    \    for _ in range(Q):\n        t, *q = read()\n        if t:\n            u,\
    \ v = q\n            ans = pdsu.diff(u, v) if pdsu.same(u, v) else (-1,)\n   \
    \         write(*ans)\n        else:\n            u, v, *w = q\n            write(int(pdsu.consistent(u,v,\
    \ w)))\n            pdsu.merge(u, v, w)\n\ndef matmul2(x, y):\n    return [\n\
    \        (y[0] * x[0] + y[1] * x[2]) % mod,\n        (y[0] * x[1] + y[1] * x[3])\
    \ % mod,\n        (y[2] * x[0] + y[3] * x[2]) % mod,\n        (y[2] * x[1] + y[3]\
    \ * x[3]) % mod,\n    ]\n\ndef matinv2(x) -> list[int]:\n    return [x[3], -x[1]\
    \ % mod, -x[2] % mod, x[0]]\n\ne = [1, 0, 0, 1]\n\n            \n'''\n\u257A\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\nclass PotentializedDSU:\n\n    def __init__(self, op,\
    \ inv, e, v) -> None:\n        n = v if isinstance(v, int) else len(v)\n     \
    \   self.n = n\n        self.par = [-1] * n\n        self.op = op\n        self.inv\
    \ = inv\n        self.e = e\n        self.pot = [e] * n if isinstance(v, int)\
    \ else v\n\n    def leader(self, x: int) -> int:\n        assert 0 <= x < self.n\n\
    \        path = []\n        while self.par[x] >= 0:\n            path.append(x)\n\
    \            x = self.par[x]\n        for y in reversed(path):\n            self.pot[y]\
    \ = self.op(self.pot[y], self.pot[self.par[y]])\n            self.par[y] = x\n\
    \        return x\n    \n    def consistent(self, x: int, y: int, w) -> bool:\n\
    \        rx = self.leader(x)\n        ry = self.leader(y)\n        if rx == ry:\n\
    \            return self.op(self.pot[x], self.inv(self.pot[y])) == w\n       \
    \ return True\n\n    def merge(self, x: int, y: int, w) -> tuple[int, int]:\n\
    \        assert 0 <= x < self.n\n        assert 0 <= y < self.n\n        rx =\
    \ self.leader(x)\n        ry = self.leader(y)\n        if rx != ry:\n        \
    \    par = self.par\n            if par[rx] < par[ry]:\n                x,y,w,rx,ry\
    \ = y,x,self.inv(w),ry,rx\n                \n            par[ry] += par[rx]\n\
    \            par[rx] = ry\n            self.pot[rx] = self.op(\n             \
    \   self.op(self.inv(self.pot[x]), w), self.pot[y]\n            )\n        return\
    \ ry, rx\n\n    def same(self, x: int, y: int) -> bool:\n        assert 0 <= x\
    \ < self.n\n        assert 0 <= y < self.n\n        return self.leader(x) == self.leader(y)\n\
    \    \n    def size(self, x: int) -> int:\n        assert 0 <= x < self.n\n  \
    \      return -self.par[self.leader(x)]\n    \n    def groups(self):\n       \
    \ leader_buf = [self.leader(i) for i in range(self.n)]\n\n        result = [[]\
    \ for _ in range(self.n)]\n        for i in range(self.n):\n            result[leader_buf[i]].append(i)\n\
    \n        return list(filter(lambda r: r, result))\n\n    def diff(self, x: int,\
    \ y: int):\n        assert self.same(x, y)\n        return self.op(self.pot[x],\
    \ self.inv(self.pot[y]))\n\n\ndef read(shift=0, base=10):\n    return [int(s,\
    \ base) + shift for s in input().split()]\nimport os\nimport sys\nfrom io import\
    \ BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n    BUFSIZE = 8192\n    newlines\
    \ = 0\n\n    def __init__(self, file):\n        self._fd = file.fileno()\n   \
    \     self.buffer = BytesIO()\n        self.writable = \"x\" in file.mode or \"\
    r\" not in file.mode\n        self.write = self.buffer.write if self.writable\
    \ else None\n\n    def read(self):\n        BUFSIZE = self.BUFSIZE\n        while\
    \ True:\n            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))\n\
    \            if not b:\n                break\n            ptr = self.buffer.tell()\n\
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
    \nif __name__ == \"__main__\":\n    main()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/unionfind_with_potential_non_commutative_group\n\
    \nmod = 998244353\n\ndef main():\n    N, Q = read()\n    pdsu = PotentializedDSU(matmul2,matinv2,e,N)\n\
    \    for _ in range(Q):\n        t, *q = read()\n        if t:\n            u,\
    \ v = q\n            ans = pdsu.diff(u, v) if pdsu.same(u, v) else (-1,)\n   \
    \         write(*ans)\n        else:\n            u, v, *w = q\n            write(int(pdsu.consistent(u,v,\
    \ w)))\n            pdsu.merge(u, v, w)\n\ndef matmul2(x, y):\n    return [\n\
    \        (y[0] * x[0] + y[1] * x[2]) % mod,\n        (y[0] * x[1] + y[1] * x[3])\
    \ % mod,\n        (y[2] * x[0] + y[3] * x[2]) % mod,\n        (y[2] * x[1] + y[3]\
    \ * x[3]) % mod,\n    ]\n\ndef matinv2(x) -> list[int]:\n    return [x[3], -x[1]\
    \ % mod, -x[2] % mod, x[0]]\n\ne = [1, 0, 0, 1]\n\n            \nfrom cp_library.ds.potentialized_dsu_cls\
    \ import PotentializedDSU\nfrom cp_library.io.read_int_fn import read\nfrom cp_library.io.write_fn\
    \ import write\n\nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - cp_library/ds/potentialized_dsu_cls.py
  - cp_library/io/read_int_fn.py
  - cp_library/io/write_fn.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: true
  path: test/library-checker/data-structure/unionfind_with_potential_non_commutative_group.test.py
  requiredBy: []
  timestamp: '2025-04-03 08:59:41+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/data-structure/unionfind_with_potential_non_commutative_group.test.py
layout: document
redirect_from:
- /verify/test/library-checker/data-structure/unionfind_with_potential_non_commutative_group.test.py
- /verify/test/library-checker/data-structure/unionfind_with_potential_non_commutative_group.test.py.html
title: test/library-checker/data-structure/unionfind_with_potential_non_commutative_group.test.py
---
