---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/lca_table_recursive_cls.py
    title: cp_library/alg/tree/lca_table_recursive_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/sparse_table_cls.py
    title: cp_library/ds/sparse_table_cls.py
  - icon: ':question:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':question:'
    path: cp_library/io/read_int_fn.py
    title: cp_library/io/read_int_fn.py
  - icon: ':question:'
    path: cp_library/io/write_fn.py
    title: cp_library/io/write_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/misc/setrecursionlimit.py
    title: cp_library/misc/setrecursionlimit.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_5_C
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_5_C
  bundledCode: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_5_C\n\
    \ndef main():\n    N, = read()\n    T = []\n    for _ in range(N):\n        k,\
    \ *adj = read()\n        T.append(adj)\n    lca = LCATable(T, 0)\n    Q, = read()\n\
    \    for _ in range(Q):\n        u, v = read()\n        write(lca.query(u,v)[0])\n\
    \n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\
    \n             https://kobejean.github.io/cp-library               \n'''\n\n\n\
    import sys\nsys.setrecursionlimit(10**6)\nimport pypyjit\npypyjit.set_param(\"\
    max_unroll_recursion=-1\")\n\nfrom typing import Any, Callable, List\n\nclass\
    \ SparseTable:\n    def __init__(self, op: Callable[[Any, Any], Any], arr: List[Any]):\n\
    \        self.N = N = len(arr)\n        self.log = N.bit_length()\n        self.op\
    \ = op\n        \n        self.offsets = offsets = [0]\n        for i in range(1,\
    \ self.log):\n            offsets.append(offsets[-1] + N - (1 << (i-1)) + 1)\n\
    \            \n        self.st = st = [0] * (offsets[-1] + N - (1 << (self.log-1))\
    \ + 1)\n        st[:N] = arr \n        \n        for i in range(self.log - 1):\n\
    \            d = 1 << i\n            start = offsets[i]\n            next_start\
    \ = offsets[i + 1]\n            for j in range(N - (1 << (i+1)) + 1):\n      \
    \          st[next_start + j] = op(st[k := start+j], st[k + d])\n\n    def query(self,\
    \ l: int, r: int) -> Any:\n        k = (r-l).bit_length() - 1\n        start,\
    \ st = self.offsets[k], self.st\n        return self.op(st[start + l], st[start\
    \ + r - (1 << k)])\n    \n    def __repr__(self) -> str:\n        rows = []\n\
    \        for i in range(self.log):\n            start = self.offsets[i]\n    \
    \        end = self.offsets[i+1] if i+1 < self.log else len(self.st)\n       \
    \     rows.append(f\"{i:<2d} {self.st[start:end]}\")\n        return '\\n'.join(rows)\n\
    \nclass LCATable(SparseTable):\n    def __init__(self, T, root):\n        self.start\
    \ = [-1] * len(T)\n        euler_tour = []\n        depths = []\n        \n  \
    \      def dfs(u: int, p: int, depth: int):\n            self.start[u] = len(euler_tour)\n\
    \            euler_tour.append(u)\n            depths.append(depth)\n        \
    \    \n            for child in T[u]:\n                if child != p:\n      \
    \              dfs(child, u, depth + 1)\n                    euler_tour.append(u)\n\
    \                    depths.append(depth)\n        \n        dfs(root, -1, 0)\n\
    \        super().__init__(min, list(zip(depths, euler_tour)))\n\n    def query(self,\
    \ u, v) -> tuple[int,int]:\n        l, r = min(self.start[u], self.start[v]),\
    \ max(self.start[u], self.start[v])+1\n        d, a = super().query(l, r)\n  \
    \      return a, d\n\n    def distance(self, u, v) -> int:\n        l, r = min(self.start[u],\
    \ self.start[v]), max(self.start[u], self.start[v])+1\n        d, _ = super().query(l,\
    \ r)\n        return self.depth[l] + self.depth[r] - 2*d\n\n\ndef read(shift=0,\
    \ base=10):\n    return [int(s, base) + shift for s in input().split()]\nimport\
    \ os\nfrom io import BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n    BUFSIZE =\
    \ 8192\n    newlines = 0\n\n    def __init__(self, file):\n        self._fd =\
    \ file.fileno()\n        self.buffer = BytesIO()\n        self.writable = \"x\"\
    \ in file.mode or \"r\" not in file.mode\n        self.write = self.buffer.write\
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
    \nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_5_C\n\
    \ndef main():\n    N, = read()\n    T = []\n    for _ in range(N):\n        k,\
    \ *adj = read()\n        T.append(adj)\n    lca = LCATable(T, 0)\n    Q, = read()\n\
    \    for _ in range(Q):\n        u, v = read()\n        write(lca.query(u,v)[0])\n\
    \nfrom cp_library.alg.tree.lca_table_recursive_cls import LCATable\nfrom cp_library.io.read_int_fn\
    \ import read\nfrom cp_library.io.write_fn import write\n\nif __name__ == '__main__':\n\
    \    main()"
  dependsOn:
  - cp_library/alg/tree/lca_table_recursive_cls.py
  - cp_library/io/read_int_fn.py
  - cp_library/io/write_fn.py
  - cp_library/misc/setrecursionlimit.py
  - cp_library/ds/sparse_table_cls.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: true
  path: test/aoj/grl/grl_5_c_lca_table_recursive.test.py
  requiredBy: []
  timestamp: '2025-03-19 01:19:38+07:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl/grl_5_c_lca_table_recursive.test.py
layout: document
redirect_from:
- /verify/test/aoj/grl/grl_5_c_lca_table_recursive.test.py
- /verify/test/aoj/grl/grl_5_c_lca_table_recursive.test.py.html
title: test/aoj/grl/grl_5_c_lca_table_recursive.test.py
---
