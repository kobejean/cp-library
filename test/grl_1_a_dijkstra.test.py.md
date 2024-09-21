---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/digraph_cls.py
    title: cp_library/alg/graph/digraph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/digraph_weighted_cls.py
    title: cp_library/alg/graph/digraph_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/dijkstra_fn.py
    title: cp_library/alg/graph/dijkstra_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge_cls.py
    title: cp_library/alg/graph/edge_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge_weighted_cls.py
    title: cp_library/alg/graph/edge_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_specs_fn.py
    title: cp_library/io/read_specs_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/1/GRL/all/GRL_1_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/1/GRL/all/GRL_1_A
  bundledCode: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/1/GRL/all/GRL_1_A\n\
    \nfrom math import inf\n\ndef main():\n    N, M, r = read()\n    G = read(DiGraphWeighted[N,\
    \ M, 0])\n    D = dijkstra(G, N, r)\n    print(*('INF' if d == inf else d for\
    \ d in D), sep='\\n')\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library \
    \              \n'''\n\nimport sys\nfrom typing import Iterator, Type, TypeVar,\
    \ overload\n\nimport typing\nfrom collections import deque\nfrom numbers import\
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
    \  return cls(next(ts))\n        return parser\n\nT = TypeVar('T')\n@overload\n\
    def read(spec: int|None) -> Iterator[int]: ...\n@overload\ndef read(spec: Type[T]|T)\
    \ -> T: ...\ndef read(spec: Type[T]|T=None):\n    match spec:\n        case None:\n\
    \            return map(int, input().split())\n        case int(i0):\n       \
    \     return (int(s)-i0 for s in input().split())\n        case _:\n         \
    \   stream = TokenStream(sys.stdin)\n            parser: T = Parser.compile(spec)\n\
    \            return parser(stream)\n\nimport heapq\n\ndef dijkstra(G, N, root)\
    \ -> list[int]:\n    D = [inf for _ in range(N)]\n    D[root] = 0\n    q = [(0,\
    \ root)]\n    while q:\n        d, v = heapq.heappop(q)\n        if d > D[v]:\
    \ continue\n\n        for w, u in G[v]:\n            if (nd := d + w) < D[u]:\n\
    \                D[u] = nd\n                heapq.heappush(q, (nd, u))\n    return\
    \ D\n\n\n\nH = TypeVar('H')\nclass Edge(tuple, Parsable):\n    @property\n   \
    \ def u(self) -> int: return self[0]\n    @property\n    def v(self) -> int: return\
    \ self[1]\n    @property\n    def forw(self) -> H: return self[1]\n    @property\n\
    \    def back(self) -> H: return self[0]\n    @classmethod\n    def compile(cls,\
    \ I=1):\n        def parse(ts: TokenStream):\n            return cls((int(s)-I\
    \ for s in ts.line()))\n        return parse\n\nclass EdgeWeighted(Edge, Parsable):\n\
    \    H: TypeAlias = tuple[int,int]\n    @property\n    def w(self): return self[0]\n\
    \    @property\n    def u(self): return self[1]\n    @property\n    def v(self):\
    \ return self[2]\n    @property\n    def forw(self) -> H: return self[0], self[2]\n\
    \    @property\n    def back(self) -> H: return self[0], self[1]\n    @classmethod\n\
    \    def compile(cls, I=1):\n        def parse(ts: TokenStream):\n           \
    \ u,v,w = map(int,ts.line())\n            return cls((w,u-I,v-I))\n        return\
    \ parse\n\n\n\nN = TypeVar('N', bound=int)\nE = TypeVar('N', bound=Edge)\nclass\
    \ DiGraph(list[H], Parsable):\n    def __init__(G, N: N, edges: list[E]=[]):\n\
    \        super().__init__([] for _ in range(N))\n        for edge in edges:\n\
    \            G[edge.u].append(edge.forw)\n\n    @classmethod\n    def compile(cls,\
    \ N: int, M: int, E: E|int = Edge[-1]):\n        if isinstance(E, int):\n    \
    \        E = Edge[E]\n        edge = Parser.compile(E)\n        def parse(ts:\
    \ TokenStream):\n            return cls(N, (edge(ts) for _ in range(M)))\n   \
    \     return parse\n\nclass DiGraphWeighted(DiGraph[EdgeWeighted]):\n    @classmethod\n\
    \    def compile(cls, N: int, M: int, E: EdgeWeighted|int = EdgeWeighted[-1]):\n\
    \        if isinstance(E, int): E = EdgeWeighted[E]\n        return super().compile(N,\
    \ M, E)\n\nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/1/GRL/all/GRL_1_A\n\
    \nfrom math import inf\n\ndef main():\n    N, M, r = read()\n    G = read(DiGraphWeighted[N,\
    \ M, 0])\n    D = dijkstra(G, N, r)\n    print(*('INF' if d == inf else d for\
    \ d in D), sep='\\n')\n\nfrom cp_library.io.read_specs_fn import read\nfrom cp_library.alg.graph.dijkstra_fn\
    \ import dijkstra\nfrom cp_library.alg.graph.digraph_weighted_cls import DiGraphWeighted\n\
    \nif __name__ == '__main__':\n    main()"
  dependsOn:
  - cp_library/io/read_specs_fn.py
  - cp_library/alg/graph/dijkstra_fn.py
  - cp_library/alg/graph/digraph_weighted_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/alg/graph/edge_weighted_cls.py
  - cp_library/alg/graph/digraph_cls.py
  - cp_library/alg/graph/edge_cls.py
  isVerificationFile: true
  path: test/grl_1_a_dijkstra.test.py
  requiredBy: []
  timestamp: '2024-09-21 16:55:32+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/grl_1_a_dijkstra.test.py
layout: document
redirect_from:
- /verify/test/grl_1_a_dijkstra.test.py
- /verify/test/grl_1_a_dijkstra.test.py.html
title: test/grl_1_a_dijkstra.test.py
---
