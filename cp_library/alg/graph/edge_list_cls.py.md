---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge_cls.py
    title: cp_library/alg/graph/edge_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge_list_weighted_cls.py
    title: cp_library/alg/graph/edge_list_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_edges_weighted_fn.py
    title: cp_library/io/read_edges_weighted_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/grl_2_a_kruskal_heap.test.py
    title: test/grl_2_a_kruskal_heap.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_2_a_kruskal_sort.test.py
    title: test/grl_2_a_kruskal_sort.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_2_b_edmonds_branching.test.py
    title: test/grl_2_b_edmonds_branching.test.py
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
    \nfrom typing import TypeVar\n\n\nimport sys\nimport typing\nfrom collections\
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
    \ lambda ts: cls(next(ts))\nfrom typing import TypeAlias, TypeVar\n\nH = TypeVar('H')\n\
    class Edge(tuple, Parsable):\n    @property\n    def u(self) -> int: return self[0]\n\
    \    @property\n    def v(self) -> int: return self[1]\n    @property\n    def\
    \ forw(self) -> H: return self[1]\n    @property\n    def back(self) -> H: return\
    \ self[0]\n    @classmethod\n    def compile(cls, I=1):\n        def parse(ts:\
    \ TokenStream):\n            return cls((int(s)-I for s in ts.line()))\n     \
    \   return parse\n\nE = TypeVar('E', bound=Edge)\nM = TypeVar('M', bound=int)\n\
    \nclass EdgeCollection(Parsable):\n    @classmethod\n    def compile(cls, M: M,\
    \ E: E = Edge[-1]):\n        if isinstance(I := E, int):\n            E = Edge[I]\n\
    \        edge = Parser.compile(E)\n        def parse(ts: TokenStream):\n     \
    \       return cls(edge(ts) for _ in range(M))\n        return parse\n\nclass\
    \ EdgeList(EdgeCollection, list[E]):\n    pass\n\nclass EdgeSet(EdgeCollection,\
    \ set[E]):\n    pass\n"
  code: "import cp_library.alg.__init__\n\nfrom typing import TypeVar\nfrom cp_library.io.parser_cls\
    \ import Parsable, Parser, TokenStream\nfrom cp_library.alg.graph.edge_cls import\
    \ Edge\n\nE = TypeVar('E', bound=Edge)\nM = TypeVar('M', bound=int)\n\nclass EdgeCollection(Parsable):\n\
    \    @classmethod\n    def compile(cls, M: M, E: E = Edge[-1]):\n        if isinstance(I\
    \ := E, int):\n            E = Edge[I]\n        edge = Parser.compile(E)\n   \
    \     def parse(ts: TokenStream):\n            return cls(edge(ts) for _ in range(M))\n\
    \        return parse\n\nclass EdgeList(EdgeCollection, list[E]):\n    pass\n\n\
    class EdgeSet(EdgeCollection, set[E]):\n    pass\n"
  dependsOn:
  - cp_library/io/parser_cls.py
  - cp_library/alg/graph/edge_cls.py
  isVerificationFile: false
  path: cp_library/alg/graph/edge_list_cls.py
  requiredBy:
  - cp_library/io/read_edges_weighted_fn.py
  - cp_library/alg/graph/edge_list_weighted_cls.py
  timestamp: '2024-09-21 04:14:27+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/grl_2_a_kruskal_sort.test.py
  - test/grl_2_b_edmonds_branching.test.py
  - test/grl_2_a_kruskal_heap.test.py
documentation_of: cp_library/alg/graph/edge_list_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/edge_list_cls.py
- /library/cp_library/alg/graph/edge_list_cls.py.html
title: cp_library/alg/graph/edge_list_cls.py
---
