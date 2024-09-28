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
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
    title: test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
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
    \ Iterator, TypeAlias, TypeVar\n\nclass TokenStream(Iterator):\n    def __init__(self,\
    \ stream = sys.stdin):\n        self.stream = stream\n        self.queue = deque()\n\
    \n    def __next__(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        return self.queue.popleft()\n    \n    def wait(self):\n        if not\
    \ self.queue: self.queue.extend(self.line())\n        while self.queue: yield\n\
    \        \n    def line(self):\n        assert not self.queue\n        return\
    \ next(self.stream).rstrip().split()\n\nclass CharStream(Iterator):\n    def line(self):\n\
    \        assert not self.queue\n        return next(self.stream).rstrip()\n  \
    \      \nT = TypeVar('T')\nParseFn: TypeAlias = Callable[[TokenStream],T]\nclass\
    \ Parser:\n    def __init__(self, spec: type[T]|T):\n        self.parse = Parser.compile(spec)\n\
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
    \ spec=int) -> ParseFn[T]:\n        fn = Parser.compile(spec)\n        def parse(ts:\
    \ TokenStream):\n            return cls(fn(ts) for _ in ts.wait())\n        return\
    \ parse\n\n    @staticmethod\n    def compile_repeat(cls: T, spec, N) -> ParseFn[T]:\n\
    \        fn = Parser.compile(spec)\n        def parse(ts: TokenStream):\n    \
    \        return cls(fn(ts) for _ in range(N))\n        return parse\n\n    @staticmethod\n\
    \    def compile_children(cls: T, specs) -> ParseFn[T]:\n        fns = tuple(Parser.compile(spec)\
    \ for spec in specs)\n        def parse(ts: TokenStream):\n            return\
    \ cls(fn(ts) for fn in fns)  \n        return parse\n\n    @staticmethod\n   \
    \ def compile_tuple(cls: type[T], specs) -> ParseFn[T]:\n        match specs:\n\
    \            case [spec, end] if end is ...:\n                return Parser.compile_line(cls,\
    \ spec)\n            case specs:   \n                return Parser.compile_children(cls,\
    \ specs)\n    \n    @staticmethod\n    def compile_collection(cls, specs):\n \
    \       match specs:\n            case [ ] | [_] | set():\n                return\
    \ Parser.compile_line(cls, *specs)\n            case [spec, int() as n]:\n   \
    \             return Parser.compile_repeat(cls, spec, n)\n            case _:\n\
    \                raise NotImplementedError()\n\n        \nclass Parsable:\n  \
    \  @classmethod\n    def compile(cls):\n        def parser(ts: TokenStream):\n\
    \            return cls(next(ts))\n        return parser\n\nH = TypeVar('H')\n\
    class Edge(tuple, Parsable):\n    @property\n    def u(self) -> int: return self[0]\n\
    \    @property\n    def v(self) -> int: return self[1]\n    @property\n    def\
    \ forw(self) -> H: return self[1]\n    @property\n    def back(self) -> H: return\
    \ self[0]\n    @classmethod\n    def compile(cls, I=1):\n        def parse(ts:\
    \ TokenStream):\n            return cls((int(s)+I for s in ts.line()))\n     \
    \   return parse\n\nclass EdgeWeighted(Edge, Parsable):\n    H: TypeAlias = tuple[int,int]\n\
    \    @property\n    def u(self): return self[0]\n    @property\n    def v(self):\
    \ return self[1]\n    @property\n    def w(self): return self[2]\n    @property\n\
    \    def forw(self) -> H: return self[1], self[2]\n    @property\n    def back(self)\
    \ -> H: return self[0], self[2]\n\n    def __lt__(self, other: tuple) -> bool:\n\
    \        a = self[2],self[0],self[1]\n        b = other[2],other[0],other[1]\n\
    \        return a < b\n    \n    @classmethod\n    def compile(cls, I=-1):\n \
    \       def parse(ts: TokenStream):\n            u,v,w = ts.line()\n         \
    \   return cls((int(u)+I, int(v)+I, int(w)))\n        return parse\n\n\nclass\
    \ Graph(list[H], Parsable):\n    def __init__(G, N: int, edges=[]):\n        super().__init__([]\
    \ for _ in range(N))\n        G.E = list(edges)\n        for edge in G.E:\n  \
    \          G[edge.u].append(edge.forw)\n            G[edge.v].append(edge.back)\n\
    \n    @classmethod\n    def compile(cls, N: int, M: int, E = Edge[-1]):\n    \
    \    if isinstance(E, int): E = Edge[E]\n        edge = Parser.compile(E)\n  \
    \      def parse(ts: TokenStream):\n            return cls(N, (edge(ts) for _\
    \ in range(M)))\n        return parse\n\nclass GraphWeighted(Graph):\n    @classmethod\n\
    \    def compile(cls, N: int, M: int, E: EdgeWeighted|int = EdgeWeighted[-1]):\n\
    \        if isinstance(E, int): E = EdgeWeighted[E]\n        return super().compile(N,\
    \ M, E)\n"
  code: "import cp_library.alg.graph.__header__\n\nfrom cp_library.alg.graph.edge_weighted_cls\
    \ import EdgeWeighted\nfrom cp_library.alg.graph.graph_cls import Graph\n\nclass\
    \ GraphWeighted(Graph):\n    @classmethod\n    def compile(cls, N: int, M: int,\
    \ E: EdgeWeighted|int = EdgeWeighted[-1]):\n        if isinstance(E, int): E =\
    \ EdgeWeighted[E]\n        return super().compile(N, M, E)"
  dependsOn:
  - cp_library/alg/graph/edge_weighted_cls.py
  - cp_library/alg/graph/graph_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/alg/graph/edge_cls.py
  isVerificationFile: false
  path: cp_library/alg/graph/graph_weighted_cls.py
  requiredBy: []
  timestamp: '2024-09-28 19:50:41+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
documentation_of: cp_library/alg/graph/graph_weighted_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/graph_weighted_cls.py
- /library/cp_library/alg/graph/graph_weighted_cls.py.html
title: cp_library/alg/graph/graph_weighted_cls.py
---
