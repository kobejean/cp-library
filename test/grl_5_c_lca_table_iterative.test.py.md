---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/lca_table_iterative_cls.py
    title: cp_library/alg/tree/lca_table_iterative_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/sparse_table_cls.py
    title: cp_library/ds/sparse_table_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parsable_cls.py
    title: cp_library/io/parsable_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parse_stream_fn.py
    title: cp_library/io/parse_stream_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_specs_fn.py
    title: cp_library/io/read_specs_fn.py
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
    '''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n   \
    \          https://kobejean.github.io/cp-library               \n'''\n\nfrom typing\
    \ import Any, Callable, List\n\nclass SparseTable:\n    def __init__(self, op:\
    \ Callable[[Any, Any], Any], arr: List[Any]):\n        self.n = len(arr)\n   \
    \     self.log = self.n.bit_length()\n        self.op = op\n        self.st =\
    \ [[None] * (self.n-(1<<i)+1) for i in range(self.log)]\n        self.st[0] =\
    \ arr[:]\n        \n        for i in range(self.log-1):\n            row, d =\
    \ self.st[i], 1<<i\n            for j in range(len(self.st[i+1])):\n         \
    \       self.st[i+1][j] = op(row[j], row[j+d])\n\n    def query(self, l: int,\
    \ r: int) -> Any:\n        k = (r-l).bit_length()-1\n        return self.op(self.st[k][l],\
    \ self.st[k][r-(1<<k)])\n    \n    def __repr__(self) -> str:\n        return\
    \ '\\n'.join(f'{i:<2d} {row}' for i,row in enumerate(self.st))\n\nclass LCATable(SparseTable):\n\
    \    def __init__(self, T, root = 0):\n        self.start = [-1] * len(T)\n  \
    \      self.euler = []\n        self.depth = []\n        \n        # Iterative\
    \ DFS\n        stack = [(root, -1, 0)]\n        while stack:\n            u, p,\
    \ d = stack.pop()\n            \n            if self.start[u] == -1:  # start\
    \ visit to this node\n                self.start[u] = len(self.euler)\n      \
    \          self.euler.append(u)\n                self.depth.append(d)\n      \
    \          \n                # Add children to stack in reverse order\n      \
    \          for child in reversed(T[u]):\n                    if child != p:\n\
    \                        stack.append((u, p, d))  # Re-add parent for backtracking\n\
    \                        stack.append((child, u, d + 1))\n            else:  #\
    \ Revisiting node (backtracking)\n                self.euler.append(u)\n     \
    \           self.depth.append(d)\n        super().__init__(min, list(zip(self.depth,\
    \ self.euler)))\n\n    def query(self, u, v) -> tuple[int,int]:\n        l, r\
    \ = min(self.start[u], self.start[v]), max(self.start[u], self.start[v])+1\n \
    \       d, a = super().query(l, r)\n        return a, d\n\n\nimport sys\nfrom\
    \ typing import Type, TypeVar\n\nT = TypeVar('T')\ndef read(spec: Type[T]|T=[int])\
    \ -> T:\n    return parse_stream(sys.stdin, spec)\n\n\nimport typing\nfrom collections\
    \ import deque\nfrom numbers import Number\nfrom typing import Collection, Iterator,\
    \ Type, TypeVar\n\n\nclass Parsable:\n    @classmethod\n    def parse(cls, parse_spec):\n\
    \        return parse_spec(lambda s: cls(s))\n\nT = TypeVar('T')\ndef parse_stream(stream:\
    \ Iterator[str], spec: Type[T]|T) -> T:\n\n    def parse_tuple(cls, specs):\n\
    \        match specs:\n            case [spec, end] if end is ...: \n        \
    \        return cls(parse_line(spec))\n            case specs:               \
    \      \n                return cls(parse_spec(spec) for spec in specs)\n\n  \
    \  def parse_collection(cls, specs) -> list:\n        match specs:\n         \
    \   case [ ] | [_] | set():          \n                return cls(parse_line(*specs))\n\
    \            case [spec, int() as n]: \n                return cls(parse_spec(spec)\
    \ for _ in range(n))\n            case _:\n                raise NotImplementedError()\n\
    \n    def parse_spec(spec):\n        if args := match_spec(spec, Parsable):\n\
    \            cls, args = args\n            return cls.parse(parse_spec, *args)\n\
    \        elif args := match_spec(spec, tuple):      \n            return parse_tuple(*args)\n\
    \        elif args := match_spec(spec, Collection): \n            return parse_collection(*args)\n\
    \        elif issubclass(cls := type(offset := spec), Number):         \n    \
    \        return cls(next_token()) + offset\n        elif callable(cls := spec):\
    \                  \n            return cls(next_token())\n        else:\n   \
    \         raise NotImplementedError()\n\n    def next_token():\n        if not\
    \ queue: queue.extend(next_line())\n        return queue.popleft()\n    \n   \
    \ def parse_line(spec=int):\n        if not queue: queue.extend(next_line())\n\
    \        while queue: yield parse_spec(spec)\n        \n    def next_line():\n\
    \        return next(stream).rstrip().split()\n    \n    def match_spec(spec,\
    \ types):\n        if issubclass(cls := type(specs := spec), types):\n       \
    \     return cls, specs\n        elif (isinstance(spec, type) and \n         \
    \    issubclass(cls := typing.get_origin(spec) or spec, types)):\n           \
    \ return cls, (typing.get_args(spec) or tuple())\n        \n    queue = deque()\
    \ \n    return parse_spec(spec)\n\nN, = read()\nT = []\nfor _ in range(N):\n \
    \   k, *adj = read()\n    T.append(adj)\nlca = LCATable(T, 0)\nQ, = read()\nfor\
    \ _ in range(Q):\n    u, v = read()\n    print(lca.query(u,v)[0])\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_5_C\n\
    from cp_library.alg.tree.lca_table_iterative_cls import LCATable\nfrom cp_library.io.read_specs_fn\
    \ import read\n\nN, = read()\nT = []\nfor _ in range(N):\n    k, *adj = read()\n\
    \    T.append(adj)\nlca = LCATable(T, 0)\nQ, = read()\nfor _ in range(Q):\n  \
    \  u, v = read()\n    print(lca.query(u,v)[0])"
  dependsOn:
  - cp_library/alg/tree/lca_table_iterative_cls.py
  - cp_library/io/read_specs_fn.py
  - cp_library/ds/sparse_table_cls.py
  - cp_library/io/parse_stream_fn.py
  - cp_library/io/parsable_cls.py
  isVerificationFile: true
  path: test/grl_5_c_lca_table_iterative.test.py
  requiredBy: []
  timestamp: '2024-09-20 03:21:05+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/grl_5_c_lca_table_iterative.test.py
layout: document
redirect_from:
- /verify/test/grl_5_c_lca_table_iterative.test.py
- /verify/test/grl_5_c_lca_table_iterative.test.py.html
title: test/grl_5_c_lca_table_iterative.test.py
---
