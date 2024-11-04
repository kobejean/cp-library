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
    path: cp_library/alg/graph/edmonds_fn.py
    title: cp_library/alg/graph/edmonds_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/floyds_cycle_fn.py
    title: cp_library/alg/graph/floyds_cycle_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/dsu_cls.py
    title: cp_library/ds/dsu_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_edges_weighted_fn.py
    title: cp_library/io/read_edges_weighted_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_specs_fn.py
    title: cp_library/io/read_specs_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/misc/setrecursionlimit.py
    title: cp_library/misc/setrecursionlimit.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_B
  bundledCode: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_B\n\
    \ndef main():\n    N, M, root = read((0, ...))\n    E = read_edges(M, 0)\n   \
    \ MCA = edmonds_branching(E, N, root)\n    ans = sum(w for *_,w in MCA)\n    print(ans)\n\
    \n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\
    \n             https://kobejean.github.io/cp-library               \n'''\n\nimport\
    \ sys\nfrom typing import Type, TypeVar, overload\n\nimport typing\nfrom collections\
    \ import deque\nfrom numbers import Number\nfrom typing import Callable, Collection,\
    \ Iterator, TypeAlias, TypeVar\n\nclass TokenStream(Iterator):\n    def __init__(self,\
    \ stream = sys.stdin):\n        self.stream = stream\n        self.queue = deque()\n\
    \n    def __next__(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        return self.queue.popleft()\n    \n    def wait(self):\n        if not\
    \ self.queue: self.queue.extend(self.line())\n        while self.queue: yield\n\
    \        \n    def line(self):\n        assert not self.queue\n        return\
    \ next(self.stream).rstrip().split()\n\nclass CharStream(TokenStream):\n    def\
    \ line(self):\n        assert not self.queue\n        return next(self.stream).rstrip()\n\
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
    \ parser\n\nT = TypeVar('T')\n@overload\ndef read(spec: int|None) -> list[int]:\
    \ ...\n@overload\ndef read(spec: Type[T]|T, char=False) -> T: ...\ndef read(spec:\
    \ Type[T]|T=None, char=False):\n    match spec, char:\n        case None, False:\n\
    \            return list(map(int, input().split()))\n        case int(offset),\
    \ False:\n            return [int(s)+offset for s in input().split()]\n      \
    \  case _, _:\n            if char:\n                stream = CharStream(sys.stdin)\n\
    \            else:\n                stream = TokenStream(sys.stdin)\n        \
    \    parser: T = Parser.compile(spec)\n            return parser(stream)\n\n\n\
    \n\nclass Edge(tuple, Parsable):\n    @classmethod\n    def compile(cls, I=-1):\n\
    \        def parse(ts: TokenStream):\n            u,v = ts.line()\n          \
    \  return cls((int(u)+I,int(v)+I))\n        return parse\n\nE = TypeVar('E', bound=Edge)\n\
    M = TypeVar('M', bound=int)\n\nclass EdgeCollection(Parsable):\n    @classmethod\n\
    \    def compile(cls, M: M, E: E = Edge[-1]):\n        if isinstance(I := E, int):\n\
    \            E = Edge[I]\n        edge = Parser.compile(E)\n        def parse(ts:\
    \ TokenStream):\n            return cls(edge(ts) for _ in range(M))\n        return\
    \ parse\n\nclass EdgeList(EdgeCollection, list[E]):\n    pass\n\nclass EdgeSet(EdgeCollection,\
    \ set[E]):\n    pass\n\n\nfrom functools import total_ordering \n\n@total_ordering\n\
    class EdgeWeighted(Edge):\n    def __lt__(self, other: tuple) -> bool:\n     \
    \   a = self[2],self[0],self[1]\n        b = other[2],other[0],other[1]\n    \
    \    return a < b\n    \n    @classmethod\n    def compile(cls, I=-1):\n     \
    \   def parse(ts: TokenStream):\n            u,v,w = ts.line()\n            return\
    \ cls((int(u)+I, int(v)+I, int(w)))\n        return parse\n\nM = TypeVar('M',\
    \ bound=int)\nEw = TypeVar('Ew', bound=EdgeWeighted)\nclass EdgeCollectionWeighted(EdgeCollection):\n\
    \    @classmethod\n    def compile(cls, M: M, Ew: Ew = EdgeWeighted[-1]):\n  \
    \      if isinstance(I := Ew, int):\n            Ew = EdgeWeighted[I]\n      \
    \  return super().compile(M, Ew)\n\nclass EdgeListWeighted(EdgeCollectionWeighted,\
    \ list[Ew]):\n    pass\n\nclass EdgeSetWeighted(EdgeCollectionWeighted, set[Ew]):\n\
    \    pass\n\ndef read_edges(M, I=-1):\n    return read(EdgeListWeighted[M,I])\n\
    from functools import reduce\nfrom heapq import heapify\nfrom math import inf\n\
    \n\nsys.setrecursionlimit(10**6)\nimport pypyjit\npypyjit.set_param(\"max_unroll_recursion=-1\"\
    )\n\n\nclass DSU:\n    def __init__(self, n):\n        self.n = n\n        self.par\
    \ = [-1] * n\n\n    def merge(self, u, v):\n        assert 0 <= u < self.n\n \
    \       assert 0 <= v < self.n\n\n        x, y = self.leader(u), self.leader(v)\n\
    \        if x == y: return x\n\n        if -self.par[x] < -self.par[y]:\n    \
    \        x, y = y, x\n\n        self.par[x] += self.par[y]\n        self.par[y]\
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
    \        return list(filter(lambda r: r, result))\n\ndef floyds_cycle(F, root):\n\
    \    slow = fast = root\n    while F[fast] != -1 and F[F[fast]] != -1:\n     \
    \   slow, fast = F[slow], F[F[fast]]\n        if slow == fast:\n            cyc\
    \ = [slow]\n            while F[slow] != cyc[0]:\n                slow = F[slow]\n\
    \                cyc.append(slow)\n            return cyc\n    return None\n\n\
    def edmonds_branching(E, N, root) -> list[tuple[int,int,any]]:\n    # obtain incoming\
    \ edges\n    Gin = [[] for _ in range(N)]\n    for id,(u,v,w) in enumerate(E):\n\
    \        if v != root:\n            Gin[v].append([w,u,id])\n    \n\n    # heapify\
    \ for fast access to optimal edges\n    for v in range(N):\n        heapify(Gin[v])\n\
    \n    groups = DSU(N)\n    active = set(range(N))\n    active.discard(root)\n\n\
    \    def find_cycle(min_in):\n        for v in active:\n            cyc = floyds_cycle(min_in,\
    \ v)\n            if cyc: return cyc\n        return None\n    \n    def contract(cyc):\n\
    \        kickout = [-1]*len(E)\n        active.difference_update(cyc)\n      \
    \  nv = reduce(groups.merge, cyc)\n        active.add(nv)\n        new_edges =\
    \ []\n        \n        # Update Gin to reflect the contracted cycle\n       \
    \ for v in cyc:\n            cw, _, cid = Gin[v][0]\n            for edge in Gin[v]:\n\
    \                _, u, id = edge\n                if groups.leader(u) != nv:\n\
    \                    edge[0] -= cw # update weight\n                    kickout[id]\
    \ = cid\n                    new_edges.append(edge)\n                    if new_edges[-1][0]\
    \ < new_edges[0][0]:\n                        new_edges[0], new_edges[-1] = new_edges[-1],\
    \ new_edges[0]\n            Gin[v].clear()\n        Gin[nv] = new_edges\n    \
    \    return kickout\n\n\n    def rec(Gin):\n        min_in = [groups.leader(Gin[v][0][1])\
    \ if Gin[v] else -1 for v in range(N)]\n        cyc = find_cycle(min_in)\n   \
    \     if cyc:\n            C = { Gin[v][0][2] for v in cyc }\n            kickout\
    \ = contract(cyc)\n            MCA = rec(Gin)\n            for id in MCA:\n  \
    \              C.discard(kickout[id])\n            MCA.extend(C)\n           \
    \ return MCA\n        else:\n            return [edges[0][2] for edges in Gin\
    \ if edges]\n\n    return [E[id] for id in rec(Gin)]\n\nif __name__ == '__main__':\n\
    \    main()\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_B\n\
    \ndef main():\n    N, M, root = read((0, ...))\n    E = read_edges(M, 0)\n   \
    \ MCA = edmonds_branching(E, N, root)\n    ans = sum(w for *_,w in MCA)\n    print(ans)\n\
    \nfrom cp_library.io.read_specs_fn import read\nfrom cp_library.io.read_edges_weighted_fn\
    \ import read_edges\nfrom cp_library.alg.graph.edmonds_fn import edmonds_branching\n\
    \nif __name__ == '__main__':\n    main()"
  dependsOn:
  - cp_library/io/read_specs_fn.py
  - cp_library/io/read_edges_weighted_fn.py
  - cp_library/alg/graph/edmonds_fn.py
  - cp_library/alg/graph/edge_list_weighted_cls.py
  - cp_library/misc/setrecursionlimit.py
  - cp_library/ds/dsu_cls.py
  - cp_library/alg/graph/floyds_cycle_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/alg/graph/edge_list_cls.py
  - cp_library/alg/graph/edge_weighted_cls.py
  - cp_library/alg/graph/edge_cls.py
  isVerificationFile: true
  path: test/grl_2_b_edmonds_branching.test.py
  requiredBy: []
  timestamp: '2024-11-04 17:54:46+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/grl_2_b_edmonds_branching.test.py
layout: document
redirect_from:
- /verify/test/grl_2_b_edmonds_branching.test.py
- /verify/test/grl_2_b_edmonds_branching.test.py.html
title: test/grl_2_b_edmonds_branching.test.py
---
