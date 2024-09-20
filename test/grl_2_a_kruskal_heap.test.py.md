---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge_cls.py
    title: cp_library/alg/graph/edge_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge_list_cls.py
    title: cp_library/alg/graph/edge_list_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge_list_weighted_cls.py
    title: cp_library/alg/graph/edge_list_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge_weighted_cls.py
    title: cp_library/alg/graph/edge_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/kruskal_heap_fn.py
    title: cp_library/alg/graph/kruskal_heap_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/dsu_cls.py
    title: cp_library/ds/dsu_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/legacy/read_specs_fn.py
    title: cp_library/io/legacy/read_specs_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_edges_weighted_fn.py
    title: cp_library/io/read_edges_weighted_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_specs_fn.py
    title: cp_library/io/read_specs_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A
  bundledCode: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A\n\
    \ndef main():\n    N, M = read()\n    E = read_edges(M, 0)\n    MST = kruskal(E,\
    \ N)\n    ans = sum(w for w,u,v in MST)\n    print(ans)\n\n'''\n\u257A\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\nimport sys\nfrom typing import Iterator, Type, TypeVar,\
    \ overload\n\nimport typing\nfrom collections import deque\nfrom numbers import\
    \ Number\nfrom typing import Callable, Collection, Iterator, TypeVar\n\nclass\
    \ TokenStream(Iterator):\n    def __init__(self, stream = sys.stdin):\n      \
    \  self.stream = stream\n        self.queue = deque()\n\n    def __next__(self):\n\
    \        if not self.queue: self.queue.extend(self.line())\n        return self.queue.popleft()\n\
    \    \n    def wait(self):\n        if not self.queue: self.queue.extend(self.line())\n\
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
    \    def compile(cls):\n        return lambda ts: cls(next(ts))\n\nT = TypeVar('T')\n\
    @overload\ndef read(spec: int|None) -> Iterator[int]: ...\n@overload\ndef read(spec:\
    \ Type[T]|T) -> T: ...\ndef read(spec: Type[T]|T=None):\n    match spec:\n   \
    \     case None:\n            return map(int, input().split())\n        case int(i0):\n\
    \            return (int(s)-i0 for s in input().split())\n        case _:\n  \
    \          stream = TokenStream(sys.stdin)\n            parser = Parser(spec)\n\
    \            return parser(stream)\n\n\n\nfrom typing import TypeAlias, TypeVar\n\
    \nH = TypeVar('H')\nclass Edge(tuple, Parsable):\n    @property\n    def u(self)\
    \ -> int: return self[0]\n    @property\n    def v(self) -> int: return self[1]\n\
    \    @property\n    def forw(self) -> H: return self[1]\n    @property\n    def\
    \ back(self) -> H: return self[0]\n    @classmethod\n    def compile(cls, I=1):\n\
    \        def parse(ts: TokenStream):\n            return cls((int(s)-I for s in\
    \ ts.line()))\n        return parse\n\nE = TypeVar('E', bound=Edge)\nM = TypeVar('M',\
    \ bound=int)\n\nclass EdgeCollection(Parsable):\n    @classmethod\n    def compile(cls,\
    \ M: M, E: E = Edge[-1]):\n        if isinstance(I := E, int):\n            E\
    \ = Edge[I]\n        edge = Parser.compile(E)\n        def parse(ts: TokenStream):\n\
    \            return cls(edge(ts) for _ in range(M))\n        return parse\n\n\
    class EdgeList(EdgeCollection, list[E]):\n    pass\n\nclass EdgeSet(EdgeCollection,\
    \ set[E]):\n    pass\n\n\nclass EdgeWeighted(Edge, Parsable):\n    H: TypeAlias\
    \ = tuple[int,int]\n    @property\n    def w(self): return self[0]\n    @property\n\
    \    def u(self): return self[1]\n    @property\n    def v(self): return self[2]\n\
    \    @property\n    def forw(self) -> H: return self[0], self[2]\n    @property\n\
    \    def back(self) -> H: return self[0], self[1]\n    @classmethod\n    def compile(cls,\
    \ I=1):\n        def parse(ts: TokenStream):\n            u,v,w = map(int,ts.line())\n\
    \            return cls((w,u-I,v-I))\n        return parse\n\nM = TypeVar('M',\
    \ bound=int)\nE = TypeVar('E', bound=EdgeWeighted)\nclass EdgeCollectionWeighted(EdgeCollection):\n\
    \    @classmethod\n    def compile(cls, M: M, E: E = EdgeWeighted[-1]):\n    \
    \    if isinstance(I := E, int):\n            E = EdgeWeighted[I]\n        return\
    \ super().compile(M, E)\n\nclass EdgeListWeighted(EdgeCollectionWeighted, list[E]):\n\
    \    pass\n\nclass EdgeSetWeighted(EdgeCollectionWeighted, set[E]):\n    pass\n\
    \ndef read_edges(M, I=-1):\n    return read(EdgeListWeighted[M,I])\n\n\nT = TypeVar('T')\n\
    def read(spec: Type[T]|T=[int]) -> T:\n    stream = TokenStream(sys.stdin)\n \
    \   parser = Parser.compile(spec)\n    return parser(stream)\n\nfrom heapq import\
    \ heapify, heappop\n\n\nclass DSU:\n    def __init__(self, n):\n        self.n\
    \ = n\n        self.par = [-1] * n\n\n    def merge(self, u, v):\n        assert\
    \ 0 <= u < self.n\n        assert 0 <= v < self.n\n\n        x, y = self.leader(u),\
    \ self.leader(v)\n        if x == y: return x\n\n        if -self.par[x] < -self.par[y]:\n\
    \            x, y = y, x\n\n        self.par[x] += self.par[y]\n        self.par[y]\
    \ = x\n\n        return x\n\n    def same(self, u: int, v: int):\n        assert\
    \ 0 <= u < self.n\n        assert 0 <= v < self.n\n        return self.leader(u)\
    \ == self.leader(v)\n\n    def leader(self, i) -> int:\n        assert 0 <= i\
    \ < self.n\n\n        p = self.par[i]\n        while p >= 0:\n            if self.par[p]\
    \ < 0:\n                return p\n            self.par[i], i, p = self.par[p],\
    \ self.par[p], self.par[self.par[p]]\n\n        return i\n\n    def size(self,\
    \ i) -> int:\n        assert 0 <= i < self.n\n        \n        return -self.par[self.leader(i)]\n\
    \n    def groups(self) -> list[list[int]]:\n        leader_buf = [self.leader(i)\
    \ for i in range(self.n)]\n\n        result = [[] for _ in range(self.n)]\n  \
    \      for i in range(self.n):\n            result[leader_buf[i]].append(i)\n\n\
    \        return list(filter(lambda r: r, result))\n\ndef kruskal(E, N):\n    heapify(E)\n\
    \    dsu = DSU(N)\n    MST = []\n    need = N-1\n    while E and need > 0:\n \
    \       edge = heappop(E)\n        _,u,v = edge\n        if not dsu.same(u,v):\n\
    \            dsu.merge(u,v)\n            MST.append(edge)\n            need -=\
    \ 1\n    return MST\n\nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A\n\
    \ndef main():\n    N, M = read()\n    E = read_edges(M, 0)\n    MST = kruskal(E,\
    \ N)\n    ans = sum(w for w,u,v in MST)\n    print(ans)\n\nfrom cp_library.io.read_edges_weighted_fn\
    \ import read_edges\nfrom cp_library.io.legacy.read_specs_fn import read\nfrom\
    \ cp_library.alg.graph.kruskal_heap_fn import kruskal\n\nif __name__ == '__main__':\n\
    \    main()"
  dependsOn:
  - cp_library/io/read_edges_weighted_fn.py
  - cp_library/io/legacy/read_specs_fn.py
  - cp_library/alg/graph/kruskal_heap_fn.py
  - cp_library/io/read_specs_fn.py
  - cp_library/alg/graph/edge_list_weighted_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/ds/dsu_cls.py
  - cp_library/alg/graph/edge_list_cls.py
  - cp_library/alg/graph/edge_weighted_cls.py
  - cp_library/alg/graph/edge_cls.py
  isVerificationFile: true
  path: test/grl_2_a_kruskal_heap.test.py
  requiredBy: []
  timestamp: '2024-09-21 04:14:27+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/grl_2_a_kruskal_heap.test.py
layout: document
redirect_from:
- /verify/test/grl_2_a_kruskal_heap.test.py
- /verify/test/grl_2_a_kruskal_heap.test.py.html
title: test/grl_2_a_kruskal_heap.test.py
---
