---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge_cls.py
    title: cp_library/alg/graph/edge_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/graph_cls.py
    title: cp_library/alg/graph/graph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/tarjan_articulation_points_fn.py
    title: cp_library/alg/graph/tarjan_articulation_points_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_specs_fn.py
    title: cp_library/io/read_specs_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/misc/setrecursionlimit.py
    title: cp_library/misc/setrecursionlimit.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_A
  bundledCode: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_A\n\
    \ndef main():\n    N, M = read()\n    G = read(Graph[N,M,0])\n    ans = sorted(tarjan_articulation_points(G,\
    \ N))\n    if ans:\n        print(*ans, sep='\\n')\n\n'''\n\u257A\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\nimport sys\nsys.setrecursionlimit(10**6)\nimport pypyjit\n\
    pypyjit.set_param(\"max_unroll_recursion=-1\")\n\ndef tarjan_articulation_points(G,\
    \ N):\n    order = [None] * N\n    low = [None] * N\n    parent = [-1] * N\n \
    \   ap = set()\n    time = 0\n\n    def dfs(u):\n        nonlocal time\n     \
    \   children = 0\n        order[u] = low[u] = time\n        time += 1\n\n    \
    \    for v in G[u]:\n            if order[v] is None:\n                children\
    \ += 1\n                parent[v] = u\n                dfs(v)\n              \
    \  low[u] = min(low[u], low[v])\n                if parent[u] != -1 and low[v]\
    \ >= order[u]:\n                    ap.add(u)\n            elif v != parent[u]:\n\
    \                low[u] = min(low[u], order[v])\n\n        if parent[u] == -1\
    \ and children > 1:\n            ap.add(u)\n\n    for i in range(N):\n       \
    \ if order[i] is None:\n            dfs(i)\n\n    return ap\n\n\nfrom typing import\
    \ TypeVar\n\n\nimport typing\nfrom collections import deque\nfrom numbers import\
    \ Number\nfrom typing import Callable, Collection, Iterator, TypeAlias, TypeVar\n\
    \nclass TokenStream(Iterator):\n    def __init__(self, stream = sys.stdin):\n\
    \        self.stream = stream\n        self.queue = deque()\n\n    def __next__(self):\n\
    \        if not self.queue: self.queue.extend(self.line())\n        return self.queue.popleft()\n\
    \    \n    def wait(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        while self.queue: yield\n        \n    def line(self):\n        assert\
    \ not self.queue\n        return next(self.stream).rstrip().split()\n        \n\
    T = TypeVar('T')\nParseFn: TypeAlias = Callable[[TokenStream],T]\nclass Parser:\n\
    \    def __init__(self, spec: type[T]|T):\n        self.parse = Parser.compile(spec)\n\
    \n    def __call__(self, ts: TokenStream) -> T:\n        return self.parse(ts)\n\
    \    \n    @staticmethod\n    def compile_type(cls: type[T], args = ()) -> T:\n\
    \        if issubclass(cls, Parsable):\n            return cls.compile(*args)\n\
    \        elif issubclass(cls, (Number, str)):\n            def parse(ts: TokenStream):\n\
    \                return cls(next(ts))              \n            return parse\n\
    \        elif issubclass(cls, tuple):\n            return Parser.compile_tuple(cls,\
    \ args)\n        elif issubclass(cls, Collection):\n            return Parser.compile_collection(cls,\
    \ args)\n        elif callable(cls):\n            def parse(ts: TokenStream):\n\
    \                return cls(next(ts))              \n            return parse\n\
    \        else:\n            raise NotImplementedError()\n    \n    @staticmethod\n\
    \    def compile(spec: type[T]|T=int) -> ParseFn[T]:\n        if isinstance(spec,\
    \ type):\n            cls = typing.get_origin(spec) or spec\n            args\
    \ = typing.get_args(spec) or tuple()\n            return Parser.compile_type(cls,\
    \ args)\n        elif isinstance(offset := spec, Number): \n            cls =\
    \ type(spec)  \n            def parse(ts: TokenStream):\n                return\
    \ cls(next(ts)) + offset\n            return parse\n        elif isinstance(args\
    \ := spec, tuple):      \n            return Parser.compile_tuple(type(spec),\
    \ args)\n        elif isinstance(args := spec, Collection):  \n            return\
    \ Parser.compile_collection(type(spec), args)\n        else:\n            raise\
    \ NotImplementedError()\n    \n    @staticmethod\n    def compile_line(cls: T,\
    \ spec=int) -> ParseFn[T]:\n        fn = Parser.compile(spec)\n        # @parse_stride(stride=inf)\n\
    \        def parse(ts: TokenStream):\n            return cls(fn(ts) for _ in ts.wait())\n\
    \        return parse\n\n    @staticmethod\n    def compile_repeat(cls: T, spec,\
    \ N) -> ParseFn[T]:\n        fn = Parser.compile(spec)\n        # @parse_stride(stride=fn.stride*N)\n\
    \        def parse(ts: TokenStream):\n            return cls(fn(ts) for _ in range(N))\n\
    \        return parse\n\n    @staticmethod\n    def compile_children(cls: T, specs)\
    \ -> ParseFn[T]:\n        fns = tuple(Parser.compile(spec) for spec in specs)\
    \ \n        # @parse_stride(stride=sum(fn.stride for fn in fns))\n        def\
    \ parse(ts: TokenStream):\n            return cls(fn(ts) for fn in fns)  \n  \
    \      return parse\n\n    @staticmethod\n    def compile_tuple(cls: type[T],\
    \ specs) -> ParseFn[T]:\n        match specs:\n            case [spec, end] if\
    \ end is ...:\n                return Parser.compile_line(cls, spec)\n       \
    \     case specs:   \n                return Parser.compile_children(cls, specs)\n\
    \    \n    @staticmethod\n    def compile_collection(cls, specs):\n        match\
    \ specs:\n            case [ ] | [_] | set():\n                return Parser.compile_line(cls,\
    \ *specs)\n            case [spec, int() as n]:\n                return Parser.compile_repeat(cls,\
    \ spec, n)\n            case _:\n                raise NotImplementedError()\n\
    \n        \nclass Parsable:\n    @classmethod\n    def compile(cls):\n       \
    \ # @parse_stride(stride=1)\n        def parser(ts: TokenStream):\n          \
    \  return cls(next(ts))\n        return parser\n\nH = TypeVar('H')\nclass Edge(tuple,\
    \ Parsable):\n    @property\n    def u(self) -> int: return self[0]\n    @property\n\
    \    def v(self) -> int: return self[1]\n    @property\n    def forw(self) ->\
    \ H: return self[1]\n    @property\n    def back(self) -> H: return self[0]\n\
    \    @classmethod\n    def compile(cls, I=1):\n        def parse(ts: TokenStream):\n\
    \            return cls((int(s)-I for s in ts.line()))\n        return parse\n\
    \n\nN = TypeVar('N', bound=int)\nE = TypeVar('E', bound=Edge)\nclass Graph(list[H],\
    \ Parsable):\n    def __init__(G, N: N, edges: list[E]=[]):\n        super().__init__([]\
    \ for _ in range(N))\n        for edge in edges:\n            G[edge.u].append(edge.forw)\n\
    \            G[edge.v].append(edge.back)\n\n    @classmethod\n    def compile(cls,\
    \ N: int, M: int, E: E|int = Edge[-1]):\n        if isinstance(E, int):\n    \
    \        E = Edge[E]\n        edge = Parser.compile(E)\n        def parse(ts:\
    \ TokenStream):\n            return cls(N, (edge(ts) for _ in range(M)))\n   \
    \     return parse\n\nfrom typing import Iterator, Type, TypeVar, overload\n\n\
    T = TypeVar('T')\n@overload\ndef read(spec: int|None) -> Iterator[int]: ...\n\
    @overload\ndef read(spec: Type[T]|T) -> T: ...\ndef read(spec: Type[T]|T=None):\n\
    \    match spec:\n        case None:\n            return map(int, input().split())\n\
    \        case int(i0):\n            return (int(s)-i0 for s in input().split())\n\
    \        case _:\n            stream = TokenStream(sys.stdin)\n            parser:\
    \ T = Parser.compile(spec)\n            return parser(stream)\n\nif __name__ ==\
    \ '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_A\n\
    \ndef main():\n    N, M = read()\n    G = read(Graph[N,M,0])\n    ans = sorted(tarjan_articulation_points(G,\
    \ N))\n    if ans:\n        print(*ans, sep='\\n')\n\nfrom cp_library.alg.graph.tarjan_articulation_points_fn\
    \ import tarjan_articulation_points\nfrom cp_library.alg.graph.graph_cls import\
    \ Graph\nfrom cp_library.io.read_specs_fn import read\n\nif __name__ == '__main__':\n\
    \    main()"
  dependsOn:
  - cp_library/alg/graph/tarjan_articulation_points_fn.py
  - cp_library/alg/graph/graph_cls.py
  - cp_library/io/read_specs_fn.py
  - cp_library/misc/setrecursionlimit.py
  - cp_library/io/parser_cls.py
  - cp_library/alg/graph/edge_cls.py
  isVerificationFile: true
  path: test/grl_3_a_tarjan_articulation_points.test.py
  requiredBy: []
  timestamp: '2024-09-21 16:55:32+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/grl_3_a_tarjan_articulation_points.test.py
layout: document
redirect_from:
- /verify/test/grl_3_a_tarjan_articulation_points.test.py
- /verify/test/grl_3_a_tarjan_articulation_points.test.py.html
title: test/grl_3_a_tarjan_articulation_points.test.py
---
