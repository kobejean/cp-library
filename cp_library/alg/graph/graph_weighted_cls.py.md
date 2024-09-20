---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge_cls.py
    title: cp_library/alg/graph/edge_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge_weighted_cls.py
    title: cp_library/alg/graph/edge_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/graph_cls.py
    title: cp_library/alg/graph/graph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \n\nfrom typing import TypeAlias\n\n\nimport sys\nimport typing\nfrom collections\
    \ import deque\nfrom numbers import Number\nfrom typing import Callable, Collection,\
    \ Iterator, TypeVar\n\nclass TokenStream(Iterator):\n    def __init__(self, stream\
    \ = sys.stdin):\n        self.stream = stream\n        self.queue = deque()\n\n\
    \    def __next__(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        return self.queue.popleft()\n    \n    def wait(self):\n        if not\
    \ self.queue: self.queue.extend(self.line())\n        while self.queue: yield\n\
    \        \n    def line(self):\n        assert not self.queue\n        return\
    \ next(self.stream).rstrip().split()\n    \n        \nT = TypeVar('T')\nclass\
    \ Parser:\n    def __init__(self, spec: type[T]|T):\n        self.parse = Parser.compile(spec)\n\
    \n    def __call__(self, ts: TokenStream) -> T:\n        return self.parse(ts)\n\
    \n    @staticmethod\n    def compile(spec: type[T]|T=int) -> Callable[[TokenStream],T]:\n\
    \            \n        def compile_tuple(cls, specs):\n            match specs:\n\
    \                case [spec, end] if end is ...: \n                    fn = Parser.compile(spec)\
    \ \n                    return lambda ts: cls(fn(ts) for _ in ts.wait())\n   \
    \             case specs:\n                    fns = tuple(Parser.compile(spec)\
    \ for spec in specs)               \n                    return lambda ts: cls(fn(ts)\
    \ for fn in fns)\n\n        def compile_collection(cls, specs) -> list:\n    \
    \        match specs:\n                case [ ] | [_] | set():   \n          \
    \          fn = Parser.compile(*specs)       \n                    return lambda\
    \ ts: cls(fn(ts) for _ in ts.wait())\n                case [spec, int() as n]:\
    \ \n                    fn = Parser.compile(spec)\n                    return\
    \ lambda ts: cls(fn(ts) for _ in range(n))\n                case _:\n        \
    \            raise NotImplementedError()\n        \n        def match_spec(spec,\
    \ types):\n            if issubclass(cls := type(specs := spec), types):\n   \
    \             return cls, specs\n            elif (isinstance(spec, type) and\
    \ \n                issubclass(cls := typing.get_origin(spec) or spec, types)):\n\
    \                return cls, (typing.get_args(spec) or tuple())\n            \n\
    \        if args := match_spec(spec, Parsable):\n            cls, args = args\n\
    \            return cls.compile(*args)\n        elif issubclass(cls := type(offset\
    \ := spec), Number):         \n            return lambda ts: cls(next(ts)) + offset\n\
    \        elif args := match_spec(spec, tuple):      \n            return compile_tuple(*args)\n\
    \        elif args := match_spec(spec, Collection): \n            return compile_collection(*args)\n\
    \        elif callable(cls := spec):                  \n            return lambda\
    \ ts: cls(next(ts))\n        else:\n            raise NotImplementedError()\n\
    \        \nclass Parsable:\n    @classmethod\n    def compile(cls):\n        return\
    \ lambda ts: cls(next(ts))\n\nH = TypeVar('H')\nclass Edge(tuple, Parsable):\n\
    \    @property\n    def u(self) -> int: return self[0]\n    @property\n    def\
    \ v(self) -> int: return self[1]\n    @property\n    def forw(self) -> H: return\
    \ self[1]\n    @property\n    def back(self) -> H: return self[0]\n    @classmethod\n\
    \    def compile(cls, I=1):\n        def parse(ts: TokenStream):\n           \
    \ return cls((int(s)-I for s in ts.line()))\n        return parse\n\nclass EdgeWeighted(Edge,\
    \ Parsable):\n    H: TypeAlias = tuple[int,int]\n    @property\n    def w(self):\
    \ return self[0]\n    @property\n    def u(self): return self[1]\n    @property\n\
    \    def v(self): return self[2]\n    @property\n    def forw(self) -> H: return\
    \ self[0], self[2]\n    @property\n    def back(self) -> H: return self[0], self[1]\n\
    \    @classmethod\n    def compile(cls, I=1):\n        def parse(ts: TokenStream):\n\
    \            u,v,w = map(int,ts.line())\n            return cls((w,u-I,v-I))\n\
    \        return parse\n\n\n\n\nN = TypeVar('N', bound=int)\nE = TypeVar('E', bound=Edge)\n\
    class Graph(list[H], Parsable):\n    def __init__(G, N: N, edges: list[E]=[]):\n\
    \        super().__init__([] for _ in range(N))\n        for edge in edges:\n\
    \            G[edge.u].append(edge.forw)\n            G[edge.v].append(edge.back)\n\
    \n    @classmethod\n    def compile(cls, N: int, M: int, E: E|int = Edge[-1]):\n\
    \        if isinstance(E, int):\n            E = Edge[E]\n        edge = Parser.compile(E)\n\
    \        def parse(ts: TokenStream):\n            return cls(N, (edge(ts) for\
    \ _ in range(M)))\n        return parse\n\nclass GraphWeighted(Graph[EdgeWeighted]):\n\
    \    @classmethod\n    def compile(cls, N: int, M: int, E: EdgeWeighted|int =\
    \ EdgeWeighted[-1]):\n        if isinstance(E, int):\n            E = EdgeWeighted[E]\n\
    \        return super().compile(N, M, E)\n"
  code: "import cp_library.alg.__init__\n\nfrom cp_library.alg.graph.edge_weighted_cls\
    \ import EdgeWeighted\nfrom cp_library.alg.graph.graph_cls import Graph\n\nclass\
    \ GraphWeighted(Graph[EdgeWeighted]):\n    @classmethod\n    def compile(cls,\
    \ N: int, M: int, E: EdgeWeighted|int = EdgeWeighted[-1]):\n        if isinstance(E,\
    \ int):\n            E = EdgeWeighted[E]\n        return super().compile(N, M,\
    \ E)"
  dependsOn:
  - cp_library/alg/graph/edge_weighted_cls.py
  - cp_library/alg/graph/graph_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/alg/graph/edge_cls.py
  isVerificationFile: false
  path: cp_library/alg/graph/graph_weighted_cls.py
  requiredBy: []
  timestamp: '2024-09-21 04:14:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/graph/graph_weighted_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/graph_weighted_cls.py
- /library/cp_library/alg/graph/graph_weighted_cls.py.html
title: cp_library/alg/graph/graph_weighted_cls.py
---
