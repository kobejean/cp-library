---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/alg/graph/digraph_cls.py
    title: cp_library/alg/graph/digraph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/digraph_weighted_cls.py
    title: cp_library/alg/graph/digraph_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/graph_cls.py
    title: cp_library/alg/graph/graph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/graph_weighted_cls.py
    title: cp_library/alg/graph/graph_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/graph_weighted_proto.py
    title: cp_library/alg/graph/graph_weighted_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_cls.py
    title: cp_library/alg/tree/tree_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_weighted_cls.py
    title: cp_library/alg/tree/tree_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_tree_fn.py
    title: cp_library/io/read_tree_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
    title: test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
    title: test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc337_g_tree_inversion_heavy_light_decomposition.test.py
    title: test/abc337_g_tree_inversion_heavy_light_decomposition.test.py
  - icon: ':heavy_check_mark:'
    path: test/dp_v_subtree_rerooting_iterative.test.py
    title: test/dp_v_subtree_rerooting_iterative.test.py
  - icon: ':heavy_check_mark:'
    path: test/dp_v_subtree_rerooting_recursive.test.py
    title: test/dp_v_subtree_rerooting_recursive.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_1_a_dijkstra.test.py
    title: test/grl_1_a_dijkstra.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_1_b_bellman_ford.test.py
    title: test/grl_1_b_bellman_ford.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_1_c_floyd_warshall.test.py
    title: test/grl_1_c_floyd_warshall.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_3_a_tarjan_articulation_points.test.py
    title: test/grl_3_a_tarjan_articulation_points.test.py
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
    from typing import Iterable\n\n\nimport sys\nimport typing\nfrom collections import\
    \ deque\nfrom numbers import Number\nfrom typing import Callable, Collection,\
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
    \            return cls(next(ts))\n        return parser\n\nclass GraphProtocol(list,\
    \ Parsable):\n\n    def neighbors(G, v: int) -> Iterable[int]:\n        return\
    \ G[v]\n\n    @classmethod\n    def compile(cls, N: int, M: int, E):\n       \
    \ edge = Parser.compile(E)\n        def parse(ts: TokenStream):\n            return\
    \ cls(N, (edge(ts) for _ in range(M)))\n        return parse\n"
  code: "import cp_library.alg.graph.__header__\nfrom typing import Iterable\nfrom\
    \ cp_library.io.parser_cls import Parsable, Parser, TokenStream\n\nclass GraphProtocol(list,\
    \ Parsable):\n\n    def neighbors(G, v: int) -> Iterable[int]:\n        return\
    \ G[v]\n\n    @classmethod\n    def compile(cls, N: int, M: int, E):\n       \
    \ edge = Parser.compile(E)\n        def parse(ts: TokenStream):\n            return\
    \ cls(N, (edge(ts) for _ in range(M)))\n        return parse"
  dependsOn:
  - cp_library/io/parser_cls.py
  isVerificationFile: false
  path: cp_library/alg/graph/graph_proto.py
  requiredBy:
  - cp_library/io/read_tree_fn.py
  - cp_library/alg/graph/graph_weighted_cls.py
  - cp_library/alg/graph/digraph_cls.py
  - cp_library/alg/graph/graph_weighted_proto.py
  - cp_library/alg/graph/graph_cls.py
  - cp_library/alg/graph/digraph_weighted_cls.py
  - cp_library/alg/tree/tree_cls.py
  - cp_library/alg/tree/tree_weighted_cls.py
  timestamp: '2024-10-07 10:08:27+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
  - test/dp_v_subtree_rerooting_iterative.test.py
  - test/dp_v_subtree_rerooting_recursive.test.py
  - test/abc337_g_tree_inversion_heavy_light_decomposition.test.py
  - test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
  - test/grl_1_c_floyd_warshall.test.py
  - test/grl_3_a_tarjan_articulation_points.test.py
  - test/grl_1_a_dijkstra.test.py
  - test/grl_1_b_bellman_ford.test.py
documentation_of: cp_library/alg/graph/graph_proto.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/graph_proto.py
- /library/cp_library/alg/graph/graph_proto.py.html
title: cp_library/alg/graph/graph_proto.py
---
