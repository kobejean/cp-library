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
    \ enumerate(G):\n                for w, v in edges:\n                    D[v]\
    \ = min(D[v], D[u] + w)\n        return D\n    D = bellman_ford(G, N, root)\n\
    \    neg_cycle = any(D[u]+w<D[v] for u, edges in enumerate(G) for w,v in edges)\n\
    \    return neg_cycle, D\n\n\nfrom typing import TypeAlias\n\n\nimport sys\nimport\
    \ typing\nfrom collections import deque\nfrom numbers import Number\nfrom typing\
    \ import Callable, Collection, Iterator, TypeVar\n\nclass TokenStream(Iterator):\n\
    \    def __init__(self, stream = sys.stdin):\n        self.stream = stream\n \
    \       self.queue = deque()\n\n    def __next__(self):\n        if not self.queue:\
    \ self.queue.extend(self.line())\n        return self.queue.popleft()\n    \n\
    \    def wait(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        while self.queue: yield\n        \n    def line(self):\n        assert\
    \ not self.queue\n        return next(self.stream).rstrip().split()\n    \n  \
    \      \nT = TypeVar('T')\nclass Parser:\n    def __init__(self, spec: type[T]|T):\n\
    \        self.parse = Parser.compile(spec)\n\n    def __call__(self, ts: TokenStream)\
    \ -> T:\n        return self.parse(ts)\n\n    @staticmethod\n    def compile(spec:\
    \ type[T]|T=int) -> Callable[[TokenStream],T]:\n            \n        def compile_tuple(cls,\
    \ specs):\n            match specs:\n                case [spec, end] if end is\
    \ ...: \n                    fn = Parser.compile(spec) \n                    return\
    \ lambda ts: cls(fn(ts) for _ in ts.wait())\n                case specs:\n   \
    \                 fns = tuple(Parser.compile(spec) for spec in specs)        \
    \       \n                    return lambda ts: cls(fn(ts) for fn in fns)\n\n\
    \        def compile_collection(cls, specs) -> list:\n            match specs:\n\
    \                case [ ] | [_] | set():   \n                    fn = Parser.compile(*specs)\
    \       \n                    return lambda ts: cls(fn(ts) for _ in ts.wait())\n\
    \                case [spec, int() as n]: \n                    fn = Parser.compile(spec)\n\
    \                    return lambda ts: cls(fn(ts) for _ in range(n))\n       \
    \         case _:\n                    raise NotImplementedError()\n        \n\
    \        def match_spec(spec, types):\n            if issubclass(cls := type(specs\
    \ := spec), types):\n                return cls, specs\n            elif (isinstance(spec,\
    \ type) and \n                issubclass(cls := typing.get_origin(spec) or spec,\
    \ types)):\n                return cls, (typing.get_args(spec) or tuple())\n \
    \           \n        if args := match_spec(spec, Parsable):\n            cls,\
    \ args = args\n            return cls.compile(*args)\n        elif issubclass(cls\
    \ := type(offset := spec), Number):         \n            return lambda ts: cls(next(ts))\
    \ + offset\n        elif args := match_spec(spec, tuple):      \n            return\
    \ compile_tuple(*args)\n        elif args := match_spec(spec, Collection): \n\
    \            return compile_collection(*args)\n        elif callable(cls := spec):\
    \                  \n            return lambda ts: cls(next(ts))\n        else:\n\
    \            raise NotImplementedError()\n        \nclass Parsable:\n    @classmethod\n\
    \    def compile(cls):\n        return lambda ts: cls(next(ts))\n\nH = TypeVar('H')\n\
    class Edge(tuple, Parsable):\n    @property\n    def u(self) -> int: return self[0]\n\
    \    @property\n    def v(self) -> int: return self[1]\n    @property\n    def\
    \ forw(self) -> H: return self[1]\n    @property\n    def back(self) -> H: return\
    \ self[0]\n    @classmethod\n    def compile(cls, I=1):\n        def parse(ts:\
    \ TokenStream):\n            return cls((int(s)-I for s in ts.line()))\n     \
    \   return parse\n\nclass EdgeWeighted(Edge, Parsable):\n    H: TypeAlias = tuple[int,int]\n\
    \    @property\n    def w(self): return self[0]\n    @property\n    def u(self):\
    \ return self[1]\n    @property\n    def v(self): return self[2]\n    @property\n\
    \    def forw(self) -> H: return self[0], self[2]\n    @property\n    def back(self)\
    \ -> H: return self[0], self[1]\n    @classmethod\n    def compile(cls, I=1):\n\
    \        def parse(ts: TokenStream):\n            u,v,w = map(int,ts.line())\n\
    \            return cls((w,u-I,v-I))\n        return parse\n\n\n\nN = TypeVar('N',\
    \ bound=int)\nE = TypeVar('N', bound=Edge)\nclass DiGraph(list[H], Parsable):\n\
    \    def __init__(G, N: N, edges: list[E]=[]):\n        super().__init__([] for\
    \ _ in range(N))\n        for edge in edges:\n            G[edge.u].append(edge.forw)\n\
    \n    @classmethod\n    def compile(cls, N: int, M: int, E: E|int = Edge[-1]):\n\
    \        if isinstance(E, int):\n            E = Edge[E]\n        edge = Parser.compile(E)\n\
    \        def parse(ts: TokenStream):\n            return cls(N, (edge(ts) for\
    \ _ in range(M)))\n        return parse\n\nclass DiGraphWeighted(DiGraph[EdgeWeighted]):\n\
    \    @classmethod\n    def compile(cls, N: int, M: int, E: EdgeWeighted|int =\
    \ EdgeWeighted[-1]):\n        if isinstance(E, int):\n            E = EdgeWeighted[E]\n\
    \        return super().compile(N, M, E)\n\nfrom typing import Iterator, Type,\
    \ TypeVar, overload\n\nT = TypeVar('T')\n@overload\ndef read(spec: int|None) ->\
    \ Iterator[int]: ...\n@overload\ndef read(spec: Type[T]|T) -> T: ...\ndef read(spec:\
    \ Type[T]|T=None):\n    match spec:\n        case None:\n            return map(int,\
    \ input().split())\n        case int(i0):\n            return (int(s)-i0 for s\
    \ in input().split())\n        case _:\n            stream = TokenStream(sys.stdin)\n\
    \            parser = Parser(spec)\n            return parser(stream)\n\nif __name__\
    \ == '__main__':\n    main()\n"
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
  timestamp: '2024-09-21 04:14:27+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/grl_1_b_bellman_ford.test.py
layout: document
redirect_from:
- /verify/test/grl_1_b_bellman_ford.test.py
- /verify/test/grl_1_b_bellman_ford.test.py.html
title: test/grl_1_b_bellman_ford.test.py
---
