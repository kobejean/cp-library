---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/rerooting_recursive_cls.py
    title: cp_library/alg/dp/rerooting_recursive_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/graph_cls.py
    title: cp_library/alg/graph/graph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/bidirectional_array_cls.py
    title: cp_library/ds/bidirectional_array_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parsable_cls.py
    title: cp_library/io/parsable_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parse_stream_fn.py
    title: cp_library/io/parse_stream_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_specs_fn.py
    title: cp_library/io/read_specs_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_tree_fn.py
    title: cp_library/io/read_tree_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/misc/setrecursionlimit.py
    title: cp_library/misc/setrecursionlimit.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/dp/tasks/dp_v
    links:
    - https://atcoder.jp/contests/dp/tasks/dp_v
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/dp/tasks/dp_v\n\
    \n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\
    \n             https://kobejean.github.io/cp-library               \n'''\n\n\n\
    import sys\nsys.setrecursionlimit(10**6)\nimport pypyjit\npypyjit.set_param(\"\
    max_unroll_recursion=-1\")\nimport typing\n\n\nclass BidirectionalArray:\n   \
    \ def __init__(self, e, op, data):\n        self.size = len(data)\n        self.prefix\
    \ = [e] + data.copy()\n        self.suffix = data.copy() + [e]\n        self.e\
    \ = e\n        self.op = op\n        for i in range(self.size):\n            self.prefix[i+1]\
    \ = op(self.prefix[i], self.prefix[i+1])\n        for i in range(self.size,0,-1):\n\
    \            self.suffix[i-1] = op(self.suffix[i-1], self.suffix[i])\n    def\
    \ left(self, l): return self.prefix[l]\n    def right(self, r): return self.suffix[r]\n\
    \    def all(self): return self.prefix[-1]\n    def out(self, l, r=None):\n  \
    \      r = l+1 if r is None else r\n        return self.op(self.prefix[l], self.suffix[r])\n\
    \nclass ReRootingDP():\n    \"\"\" A class implementation of the Re-rooting Dynamic\
    \ Programming technique. \"\"\"\n    S = typing.TypeVar('S')\n    MergeOp = typing.Callable[[S,\
    \ S], S]\n    AddNodeOp = typing.Callable[[int, S], S]\n    AddEdgeOp = typing.Callable[[int,\
    \ int, S], S]\n\n    def __init__(self, T: list[list[int]], e: S,\n          \
    \       merge: MergeOp, \n                 add_node: AddNodeOp = lambda u,s:s,\
    \ \n                 add_edge: AddEdgeOp = lambda u,v,s:s):\n        \"\"\"\n\
    \        T: list[list[int]] - Adjacency list representation of the tree.\n   \
    \     e: S - Identity element for the merge operation.\n        merge: (S,S) ->\
    \ S - Function to merge two states.\n        add_node: (int,S) -> S - Function\
    \ to incorporate a node into the state.\n        add_edge: (int,int,S) -> S -\
    \ Function to incorporate an edge into the state.\n        \"\"\"\n        self.T\
    \ = T\n        self.e = e\n        self.merge = merge\n        self.add_node =\
    \ add_node\n        self.add_edge = add_edge\n    \n    def solve(self) -> list[S]:\n\
    \        dp = [[self.e]*len(adj) for adj in self.T]\n        ans = [None for _\
    \ in range(len(self.T))]\n\n        def dfs_up(u, p=None):\n            res =\
    \ self.e\n            for i,v in enumerate(self.T[u]):\n                if v !=\
    \ p:\n                    dp[u][i] = self.add_edge(u, v, dfs_up(v, u))\n     \
    \               res = self.merge(res, dp[u][i])\n            return self.add_node(u,\
    \ res)\n\n        def dfs_down(u, p=None):\n            ba = BidirectionalArray(self.e,\
    \ self.merge, dp[u])\n            for i,v in enumerate(self.T[u]):\n         \
    \       if v != p:\n                    dp[v][self.T[v].index(u)] = self.add_edge(v,\
    \ u, self.add_node(u, ba.out(i)))\n                    dfs_down(v, u)\n      \
    \      ans[u] = ba.all()\n\n        dfs_up(0)\n        dfs_down(0)\n        return\
    \ ans\n\n\nfrom typing import Type, TypeVar\n\nT = TypeVar('T')\ndef read(spec:\
    \ Type[T]|T=[int]) -> T:\n    return parse_stream(sys.stdin, spec)\n\n\nfrom collections\
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
    \ \n    return parse_spec(spec)\n\n\nclass Graph(list, Parsable):\n    def __init__(self,\
    \ N, edges=[]):\n        super().__init__(([] for _ in range(N)))\n        for\
    \ u,v in edges:\n            self[u].append(v)\n            self[v].append(u)\n\
    \n    @classmethod\n    def parse(cls, parse_spec, N, M, I=-1):\n        return\
    \ cls(N, parse_spec(list[tuple[I,I], M]))\n\n\ndef read_tree(N, i0=1):\n    T:\
    \ Graph = [[] for _ in range(N)]\n    for _ in range(N-1):\n        u,v = read(tuple[-i0,-i0])\n\
    \        T[u].append(v)\n        T[v].append(u)\n    return T\n\n\n# from cp_library.io.read_specs_fn\
    \ import read\n# from cp_library.alg.graph.graph_cls import Graph\n\nN, M = read()\n\
    T = read_tree(N)\n\ndef mul(a,b):\n    return a*b%M\n\ndef add_node(v,res):\n\
    \    return (res+1)%M\n\nrr = ReRootingDP(T, 1, mul, add_node)\n\nprint(*rr.solve(),\
    \ sep='\\n')\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/dp/tasks/dp_v\n\
    \nfrom cp_library.alg.dp.rerooting_recursive_cls import ReRootingDP\nfrom cp_library.io.read_specs_fn\
    \ import read\nfrom cp_library.io.read_tree_fn import read_tree\n\nN, M = read()\n\
    T = read_tree(N)\n\ndef mul(a,b):\n    return a*b%M\n\ndef add_node(v,res):\n\
    \    return (res+1)%M\n\nrr = ReRootingDP(T, 1, mul, add_node)\n\nprint(*rr.solve(),\
    \ sep='\\n')"
  dependsOn:
  - cp_library/alg/dp/rerooting_recursive_cls.py
  - cp_library/io/read_specs_fn.py
  - cp_library/io/read_tree_fn.py
  - cp_library/misc/setrecursionlimit.py
  - cp_library/ds/bidirectional_array_cls.py
  - cp_library/alg/graph/graph_cls.py
  - cp_library/io/parse_stream_fn.py
  - cp_library/io/parsable_cls.py
  isVerificationFile: true
  path: test/dp_v_subtree_rerooting_recursive.test.py
  requiredBy: []
  timestamp: '2024-09-20 03:21:05+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/dp_v_subtree_rerooting_recursive.test.py
layout: document
redirect_from:
- /verify/test/dp_v_subtree_rerooting_recursive.test.py
- /verify/test/dp_v_subtree_rerooting_recursive.test.py.html
title: test/dp_v_subtree_rerooting_recursive.test.py
---
