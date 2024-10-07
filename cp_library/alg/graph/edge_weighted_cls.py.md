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
    path: cp_library/alg/graph/digraph_weighted_cls.py
    title: cp_library/alg/graph/digraph_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge_list_weighted_cls.py
    title: cp_library/alg/graph/edge_list_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/graph_weighted_cls.py
    title: cp_library/alg/graph/graph_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_weighted_cls.py
    title: cp_library/alg/tree/tree_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_edges_weighted_fn.py
    title: cp_library/io/read_edges_weighted_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
    title: test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
    title: test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
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
    \n\n\nimport sys\nimport typing\nfrom collections import deque\nfrom numbers import\
    \ Number\nfrom typing import Callable, Collection, Iterator, TypeAlias, TypeVar\n\
    \nclass TokenStream(Iterator):\n    def __init__(self, stream = sys.stdin):\n\
    \        self.stream = stream\n        self.queue = deque()\n\n    def __next__(self):\n\
    \        if not self.queue: self.queue.extend(self.line())\n        return self.queue.popleft()\n\
    \    \n    def wait(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        while self.queue: yield\n        \n    def line(self):\n        assert\
    \ not self.queue\n        return next(self.stream).rstrip().split()\n\nclass CharStream(Iterator):\n\
    \    def line(self):\n        assert not self.queue\n        return next(self.stream).rstrip()\n\
    \        \nT = TypeVar('T')\nParseFn: TypeAlias = Callable[[TokenStream],T]\n\
    class Parser:\n    def __init__(self, spec: type[T]|T):\n        self.parse =\
    \ Parser.compile(spec)\n\n    def __call__(self, ts: TokenStream) -> T:\n    \
    \    return self.parse(ts)\n    \n    @staticmethod\n    def compile_type(cls:\
    \ type[T], args = ()) -> T:\n        if issubclass(cls, Parsable):\n         \
    \   return cls.compile(*args)\n        elif issubclass(cls, (Number, str)):\n\
    \            def parse(ts: TokenStream):\n                return cls(next(ts))\
    \              \n            return parse\n        elif issubclass(cls, tuple):\n\
    \            return Parser.compile_tuple(cls, args)\n        elif issubclass(cls,\
    \ Collection):\n            return Parser.compile_collection(cls, args)\n    \
    \    elif callable(cls):\n            def parse(ts: TokenStream):\n          \
    \      return cls(next(ts))              \n            return parse\n        else:\n\
    \            raise NotImplementedError()\n    \n    @staticmethod\n    def compile(spec:\
    \ type[T]|T=int) -> ParseFn[T]:\n        if isinstance(spec, type):\n        \
    \    cls = typing.get_origin(spec) or spec\n            args = typing.get_args(spec)\
    \ or tuple()\n            return Parser.compile_type(cls, args)\n        elif\
    \ isinstance(offset := spec, Number): \n            cls = type(spec)  \n     \
    \       def parse(ts: TokenStream):\n                return cls(next(ts)) + offset\n\
    \            return parse\n        elif isinstance(args := spec, tuple):     \
    \ \n            return Parser.compile_tuple(type(spec), args)\n        elif isinstance(args\
    \ := spec, Collection):  \n            return Parser.compile_collection(type(spec),\
    \ args)\n        else:\n            raise NotImplementedError()\n    \n    @staticmethod\n\
    \    def compile_line(cls: T, spec=int) -> ParseFn[T]:\n        fn = Parser.compile(spec)\n\
    \        def parse(ts: TokenStream):\n            return cls(fn(ts) for _ in ts.wait())\n\
    \        return parse\n\n    @staticmethod\n    def compile_repeat(cls: T, spec,\
    \ N) -> ParseFn[T]:\n        fn = Parser.compile(spec)\n        def parse(ts:\
    \ TokenStream):\n            return cls(fn(ts) for _ in range(N))\n        return\
    \ parse\n\n    @staticmethod\n    def compile_children(cls: T, specs) -> ParseFn[T]:\n\
    \        fns = tuple(Parser.compile(spec) for spec in specs)\n        def parse(ts:\
    \ TokenStream):\n            return cls(fn(ts) for fn in fns)  \n        return\
    \ parse\n\n    @staticmethod\n    def compile_tuple(cls: type[T], specs) -> ParseFn[T]:\n\
    \        match specs:\n            case [spec, end] if end is ...:\n         \
    \       return Parser.compile_line(cls, spec)\n            case specs:   \n  \
    \              return Parser.compile_children(cls, specs)\n    \n    @staticmethod\n\
    \    def compile_collection(cls, specs):\n        match specs:\n            case\
    \ [ ] | [_] | set():\n                return Parser.compile_line(cls, *specs)\n\
    \            case [spec, int() as n]:\n                return Parser.compile_repeat(cls,\
    \ spec, n)\n            case _:\n                raise NotImplementedError()\n\
    \n        \nclass Parsable:\n    @classmethod\n    def compile(cls):\n       \
    \ def parser(ts: TokenStream):\n            return cls(next(ts))\n        return\
    \ parser\n\nclass Edge(tuple, Parsable):\n    @classmethod\n    def compile(cls,\
    \ I=-1):\n        def parse(ts: TokenStream):\n            u,v = ts.line()\n \
    \           return cls((int(u)+I,int(v)+I))\n        return parse\n\nfrom functools\
    \ import total_ordering \n\n@total_ordering\nclass EdgeWeighted(Edge):\n    def\
    \ __lt__(self, other: tuple) -> bool:\n        a = self[2],self[0],self[1]\n \
    \       b = other[2],other[0],other[1]\n        return a < b\n    \n    @classmethod\n\
    \    def compile(cls, I=-1):\n        def parse(ts: TokenStream):\n          \
    \  u,v,w = ts.line()\n            return cls((int(u)+I, int(v)+I, int(w)))\n \
    \       return parse\n"
  code: "import cp_library.alg.graph.__header__\n\nfrom cp_library.io.parser_cls import\
    \ TokenStream\nfrom cp_library.alg.graph.edge_cls import Edge\n\nfrom functools\
    \ import total_ordering \n\n@total_ordering\nclass EdgeWeighted(Edge):\n    def\
    \ __lt__(self, other: tuple) -> bool:\n        a = self[2],self[0],self[1]\n \
    \       b = other[2],other[0],other[1]\n        return a < b\n    \n    @classmethod\n\
    \    def compile(cls, I=-1):\n        def parse(ts: TokenStream):\n          \
    \  u,v,w = ts.line()\n            return cls((int(u)+I, int(v)+I, int(w)))\n \
    \       return parse"
  dependsOn:
  - cp_library/io/parser_cls.py
  - cp_library/alg/graph/edge_cls.py
  isVerificationFile: false
  path: cp_library/alg/graph/edge_weighted_cls.py
  requiredBy:
  - cp_library/io/read_edges_weighted_fn.py
  - cp_library/alg/graph/graph_weighted_cls.py
  - cp_library/alg/graph/edge_list_weighted_cls.py
  - cp_library/alg/graph/digraph_weighted_cls.py
  - cp_library/alg/tree/tree_weighted_cls.py
  timestamp: '2024-10-07 10:08:27+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/grl_2_a_kruskal_sort.test.py
  - test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
  - test/grl_2_b_edmonds_branching.test.py
  - test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
  - test/grl_1_c_floyd_warshall.test.py
  - test/grl_1_a_dijkstra.test.py
  - test/grl_1_b_bellman_ford.test.py
  - test/grl_2_a_kruskal_heap.test.py
documentation_of: cp_library/alg/graph/edge_weighted_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/edge_weighted_cls.py
- /library/cp_library/alg/graph/edge_weighted_cls.py.html
title: cp_library/alg/graph/edge_weighted_cls.py
---
