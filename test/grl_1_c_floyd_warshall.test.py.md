---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/digraph_weighted_cls.py
    title: cp_library/alg/graph/digraph_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge_cls.py
    title: cp_library/alg/graph/edge_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge_weighted_cls.py
    title: cp_library/alg/graph/edge_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/floyd_warshall_check_neg_cycle_fn.py
    title: cp_library/alg/graph/floyd_warshall_check_neg_cycle_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/floyd_warshall_directed_fn.py
    title: cp_library/alg/graph/floyd_warshall_directed_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/floyd_warshall_fn.py
    title: cp_library/alg/graph/floyd_warshall_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/graph_proto.py
    title: cp_library/alg/graph/graph_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/legacy/read_specs_fn.py
    title: cp_library/io/legacy/read_specs_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_C
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_C
  bundledCode: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_C\n\
    from math import inf\n\ndef main():\n    N, M = read((int,int))\n    G = read(DiGraphWeighted[N,M,0])\n\
    \    neg_cycle, D = floyd_warshall(G, N)\n\n    if neg_cycle:\n        print(\"\
    NEGATIVE CYCLE\")\n    else:\n        for row in D:\n            print(*('INF'\
    \ if d == inf else d for d in row))\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\nimport sys\nfrom typing import Type, TypeVar\n\nT = TypeVar('T')\n\
    def read(spec: Type[T]|T=[int]) -> T:\n    stream = TokenStream(sys.stdin)\n \
    \   parser = Parser.compile(spec)\n    return parser(stream)\n\n\nimport typing\n\
    from collections import deque\nfrom numbers import Number\nfrom typing import\
    \ Callable, Collection, Iterator, TypeAlias, TypeVar\n\nclass TokenStream(Iterator):\n\
    \    def __init__(self, stream = sys.stdin):\n        self.stream = stream\n \
    \       self.queue = deque()\n\n    def __next__(self):\n        if not self.queue:\
    \ self.queue.extend(self.line())\n        return self.queue.popleft()\n    \n\
    \    def wait(self):\n        if not self.queue: self.queue.extend(self.line())\n\
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
    \ parser\n\n\n\n\n\nclass Edge(tuple, Parsable):\n    @classmethod\n    def compile(cls,\
    \ I=-1):\n        def parse(ts: TokenStream):\n            u,v = ts.line()\n \
    \           return cls((int(u)+I,int(v)+I))\n        return parse\n\nfrom functools\
    \ import total_ordering \n\n@total_ordering\nclass EdgeWeighted(Edge):\n    def\
    \ __lt__(self, other: tuple) -> bool:\n        a = self[2],self[0],self[1]\n \
    \       b = other[2],other[0],other[1]\n        return a < b\n    \n    @classmethod\n\
    \    def compile(cls, I=-1):\n        def parse(ts: TokenStream):\n          \
    \  u,v,w = ts.line()\n            return cls((int(u)+I, int(v)+I, int(w)))\n \
    \       return parse\nfrom typing import Iterable\n\nclass GraphProtocol(list,\
    \ Parsable):\n\n    def neighbors(G, v: int) -> Iterable[int]:\n        return\
    \ G[v]\n\n    @classmethod\n    def compile(cls, N: int, M: int, E):\n       \
    \ edge = Parser.compile(E)\n        def parse(ts: TokenStream):\n            return\
    \ cls(N, (edge(ts) for _ in range(M)))\n        return parse\n\nfrom operator\
    \ import itemgetter\n\nclass DiGraphWeighted(GraphProtocol):\n    def __init__(G,\
    \ N, E: list = []):\n        super().__init__([] for _ in range(N))\n        G.E\
    \ = list(E)\n        for u,v,*w in G.E:\n            G[u].append((v,*w))\n   \
    \ \n    def neighbors(G, v: int) -> Iterable[int]:\n        return map(itemgetter(0),\
    \ G[v])\n    \n    @classmethod\n    def compile(cls, N: int, M: int, E: type|int\
    \ = EdgeWeighted[-1]):\n        if isinstance(E, int): E = EdgeWeighted[E]\n \
    \       return super().compile(N, M, E)\n\ndef floyd_warshall(G, N, directed=True)\
    \ -> tuple[bool, list[int]]:\n    if directed:\n        \n        def floyd_warshall(G,\
    \ N) -> list[int]:\n            D = [[inf]*N for _ in range(N)]\n        \n  \
    \          for u, edges in enumerate(G):\n                D[u][u] = 0\n      \
    \          for v,w in edges:\n                    D[u][v] = min(D[u][v], w)\n\
    \            \n            for k, Dk in enumerate(D):\n                for Di\
    \ in D:\n                    for j in range(N):\n                        Di[j]\
    \ = min(Di[j], Di[k]+Dk[j])\n            return D\n    else:\n        \n     \
    \   def floyd_warshall(G, N) -> list[int]:\n            D = [[inf]*N for _ in\
    \ range(N)]\n        \n            for u, edges in enumerate(G):\n           \
    \     D[u][u] = 0\n                for v,w in edges:\n                    D[u][v]\
    \ = min(D[u][v], w)\n            \n            for k, Dk in enumerate(D):\n  \
    \              for i, Di in enumerate(D):\n                    for j in range(i):\n\
    \                        Di[j] = D[j][i] = min(Di[j], Di[k]+Dk[j])\n         \
    \   return D\n    D = floyd_warshall(G, N)\n    return any(D[i][i] < 0 for i in\
    \ range(N)), D\n\nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_C\n\
    from math import inf\n\ndef main():\n    N, M = read((int,int))\n    G = read(DiGraphWeighted[N,M,0])\n\
    \    neg_cycle, D = floyd_warshall(G, N)\n\n    if neg_cycle:\n        print(\"\
    NEGATIVE CYCLE\")\n    else:\n        for row in D:\n            print(*('INF'\
    \ if d == inf else d for d in row))\n\nfrom cp_library.io.legacy.read_specs_fn\
    \ import read\nfrom cp_library.alg.graph.digraph_weighted_cls import DiGraphWeighted\n\
    from cp_library.alg.graph.floyd_warshall_check_neg_cycle_fn import floyd_warshall\n\
    \nif __name__ == '__main__':\n    main()"
  dependsOn:
  - cp_library/io/legacy/read_specs_fn.py
  - cp_library/alg/graph/digraph_weighted_cls.py
  - cp_library/alg/graph/floyd_warshall_check_neg_cycle_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/alg/graph/edge_weighted_cls.py
  - cp_library/alg/graph/graph_proto.py
  - cp_library/alg/graph/floyd_warshall_directed_fn.py
  - cp_library/alg/graph/floyd_warshall_fn.py
  - cp_library/alg/graph/edge_cls.py
  isVerificationFile: true
  path: test/grl_1_c_floyd_warshall.test.py
  requiredBy: []
  timestamp: '2024-10-06 18:38:39+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/grl_1_c_floyd_warshall.test.py
layout: document
redirect_from:
- /verify/test/grl_1_c_floyd_warshall.test.py
- /verify/test/grl_1_c_floyd_warshall.test.py.html
title: test/grl_1_c_floyd_warshall.test.py
---
