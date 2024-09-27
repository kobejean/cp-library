---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/bellman_ford_fn.py
    title: cp_library/alg/graph/bellman_ford_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/bellman_ford_neg_cyc_check_fn.py
    title: cp_library/alg/graph/bellman_ford_neg_cyc_check_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/digraph_cls.py
    title: cp_library/alg/graph/digraph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/digraph_weighted_cls.py
    title: cp_library/alg/graph/digraph_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge_cls.py
    title: cp_library/alg/graph/edge_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge_weighted_cls.py
    title: cp_library/alg/graph/edge_weighted_cls.py
  - icon: ':question:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':question:'
    path: cp_library/io/read_specs_fn.py
    title: cp_library/io/read_specs_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/1/GRL/all/GRL_1_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/1/GRL/all/GRL_1_B
  bundledCode: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/1/GRL/all/GRL_1_B\n\
    from math import inf\n\ndef main():\n    N, M, r = read()\n    G = read(DiGraphWeighted[N,\
    \ M, 0])\n\n    neg_cycle, D = bellman_ford(G, N, r)\n\n    if neg_cycle:\n  \
    \      print(\"NEGATIVE CYCLE\")\n    else:\n        print(*('INF' if d == inf\
    \ else d for d in D), sep='\\n')\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\ndef bellman_ford(G, N, root) -> tuple[bool, list[int]]:\n\
    \    \n    def bellman_ford(G, N, root) -> list[int]:\n        D = [inf]*N\n \
    \       D[root] = 0\n        for _ in range(N-1):\n            for u, edges in\
    \ enumerate(G):\n                for v,w in edges:\n                    D[v] =\
    \ min(D[v], D[u] + w)\n        return D\n    D = bellman_ford(G, N, root)\n  \
    \  neg_cycle = any(D[u]+w<D[v] for u, edges in enumerate(G) for v,w in edges)\n\
    \    return neg_cycle, D\n\n\nfrom typing import TypeAlias\n\n\nimport sys\nimport\
    \ typing\nfrom collections import deque\nfrom numbers import Number\nfrom typing\
    \ import Callable, Collection, Iterator, TypeAlias, TypeVar\n\nclass TokenStream(Iterator):\n\
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
    \ parser\n\nH = TypeVar('H')\nclass Edge(tuple, Parsable):\n    @property\n  \
    \  def u(self) -> int: return self[0]\n    @property\n    def v(self) -> int:\
    \ return self[1]\n    @property\n    def forw(self) -> H: return self[1]\n   \
    \ @property\n    def back(self) -> H: return self[0]\n    @classmethod\n    def\
    \ compile(cls, I=1):\n        def parse(ts: TokenStream):\n            return\
    \ cls((int(s)+I for s in ts.line()))\n        return parse\n\nclass EdgeWeighted(Edge,\
    \ Parsable):\n    H: TypeAlias = tuple[int,int]\n    @property\n    def u(self):\
    \ return self[0]\n    @property\n    def v(self): return self[1]\n    @property\n\
    \    def w(self): return self[2]\n    @property\n    def forw(self) -> H: return\
    \ self[1], self[2]\n    @property\n    def back(self) -> H: return self[0], self[2]\n\
    \n    def __lt__(self, other: tuple) -> bool:\n        a = self[2],self[0],self[1]\n\
    \        b = other[2],other[0],other[1]\n        return a < b\n    \n    @classmethod\n\
    \    def compile(cls, I=-1):\n        def parse(ts: TokenStream):\n          \
    \  u,v,w = ts.line()\n            return cls((int(u)+I, int(v)+I, int(w)))\n \
    \       return parse\n\n\n\nN = TypeVar('N', bound=int)\nE = TypeVar('N', bound=Edge)\n\
    class DiGraph(list[H], Parsable):\n    def __init__(G, N: N, edges: list[E]=[]):\n\
    \        super().__init__([] for _ in range(N))\n        G.E = list(edges)\n \
    \       for edge in G.E:\n            G[edge.u].append(edge.forw)\n\n    @classmethod\n\
    \    def compile(cls, N: int, M: int, E: E|int = Edge[-1]):\n        if isinstance(E,\
    \ int):\n            E = Edge[E]\n        edge = Parser.compile(E)\n        def\
    \ parse(ts: TokenStream):\n            return cls(N, (edge(ts) for _ in range(M)))\n\
    \        return parse\n\nclass DiGraphWeighted(DiGraph[EdgeWeighted]):\n    @classmethod\n\
    \    def compile(cls, N: int, M: int, E: EdgeWeighted|int = EdgeWeighted[-1]):\n\
    \        if isinstance(E, int): E = EdgeWeighted[E]\n        return super().compile(N,\
    \ M, E)\n\nfrom typing import Iterator, Type, TypeVar, overload\n\nT = TypeVar('T')\n\
    @overload\ndef read(spec: int|None) -> Iterator[int]: ...\n@overload\ndef read(spec:\
    \ Type[T]|T) -> T: ...\ndef read(spec: Type[T]|T=None, char=False):\n    match\
    \ spec, char:\n        case None, False:\n            return map(int, input().split())\n\
    \        case int(offset), False:\n            return (int(s)+offset for s in\
    \ input().split())\n        case _, _:\n            if char:\n               \
    \ stream = CharStream(sys.stdin)\n            else:\n                stream =\
    \ TokenStream(sys.stdin)\n            parser: T = Parser.compile(spec)\n     \
    \       return parser(stream)\n\nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/1/GRL/all/GRL_1_B\n\
    from math import inf\n\ndef main():\n    N, M, r = read()\n    G = read(DiGraphWeighted[N,\
    \ M, 0])\n\n    neg_cycle, D = bellman_ford(G, N, r)\n\n    if neg_cycle:\n  \
    \      print(\"NEGATIVE CYCLE\")\n    else:\n        print(*('INF' if d == inf\
    \ else d for d in D), sep='\\n')\n\nfrom cp_library.alg.graph.bellman_ford_neg_cyc_check_fn\
    \ import bellman_ford\nfrom cp_library.alg.graph.digraph_weighted_cls import DiGraphWeighted\n\
    from cp_library.io.read_specs_fn import read\n\nif __name__ == '__main__':\n \
    \   main()"
  dependsOn:
  - cp_library/alg/graph/bellman_ford_neg_cyc_check_fn.py
  - cp_library/alg/graph/digraph_weighted_cls.py
  - cp_library/io/read_specs_fn.py
  - cp_library/alg/graph/bellman_ford_fn.py
  - cp_library/alg/graph/edge_weighted_cls.py
  - cp_library/alg/graph/digraph_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/alg/graph/edge_cls.py
  isVerificationFile: true
  path: test/grl_1_b_bellman_ford.test.py
  requiredBy: []
  timestamp: '2024-09-28 02:29:45+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/grl_1_b_bellman_ford.test.py
layout: document
redirect_from:
- /verify/test/grl_1_b_bellman_ford.test.py
- /verify/test/grl_1_b_bellman_ford.test.py.html
title: test/grl_1_b_bellman_ford.test.py
---
