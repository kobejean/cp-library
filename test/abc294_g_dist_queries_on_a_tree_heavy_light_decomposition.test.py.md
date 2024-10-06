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
    path: cp_library/alg/graph/graph_proto.py
    title: cp_library/alg/graph/graph_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/graph_weighted_cls.py
    title: cp_library/alg/graph/graph_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/heavy_light_decomposition_weighted_cls.py
    title: cp_library/alg/tree/heavy_light_decomposition_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_weighted_cls.py
    title: cp_library/alg/tree/tree_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/bit_cls.py
    title: cp_library/ds/bit_cls.py
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
    PROBLEM: https://atcoder.jp/contests/abc294/tasks/abc294_g
    links:
    - https://atcoder.jp/contests/abc294/tasks/abc294_g
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc294/tasks/abc294_g\n\
    \ndef main():\n    N = read(int)\n    T = read(TreeWeighted[N])\n\n    hld = HLDWeighted(T)\n\
    \    W = [hld.weights[i] for i in hld.order]\n    bit = BinaryIndexTree(W)\n\n\
    \    Q = read(int)\n    for query in read(list[tuple[int, int, int], Q]):\n  \
    \      match query:\n            case 1, i, w:\n                i -= 1  # Convert\
    \ to 0-based index\n                u, v, _ = T.E[i]\n                # Find child\
    \ node in edge (u, v)\n                if hld.par[u] == v:\n                 \
    \   node = u\n                else:\n                    node = v\n          \
    \      idx = hld[node]\n                bit.set(idx, w)\n            case 2, u,\
    \ v:\n                u, v = u - 1, v - 1\n                ans = sum(bit.range_sum(l,r)\
    \ for l,r in hld.path(u,v, True))\n                print(ans)\n\n'''\n\u257A\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\nclass BinaryIndexTree:\n    def __init__(self, v: int|list):\n\
    \        if isinstance(v, int):\n            self.data, self.size = [0]*v, v\n\
    \        else:\n            self.build(v)\n\n    def build(self, data):\n    \
    \    self.data, self.size = data, len(data)\n        for i in range(self.size):\n\
    \            if (r := i|(i+1)) < self.size: \n                self.data[r] +=\
    \ self.data[i]\n\n    def get(self, i: int):\n        assert 0 <= i < self.size\n\
    \        s = self.data[i]\n        z = i&(i+1)\n        for _ in range((i^z).bit_count()):\n\
    \            s, i = s-self.data[i-1], i-(i&-i)\n        return s\n    \n    def\
    \ set(self, i: int, x: int):\n        self.add(i, x-self.get(i))\n        \n \
    \   def add(self, i: int, x: object) -> None:\n        assert 0 <= i <= self.size\n\
    \        i += 1\n        while i <= self.size:\n            self.data[i-1], i\
    \ = self.data[i-1] + x, i+(i&-i)\n\n    def pref_sum(self, i: int):\n        assert\
    \ 0 <= i <= self.size\n        s = 0\n        for _ in range(i.bit_count()):\n\
    \            s, i = s+self.data[i-1], i-(i&-i)\n        return s\n    \n    def\
    \ range_sum(self, l: int, r: int):\n        return self.pref_sum(r) - self.pref_sum(l)\n\
    \n\n\n\n\n\nimport sys\nimport typing\nfrom collections import deque\nfrom numbers\
    \ import Number\nfrom typing import Callable, Collection, Iterator, TypeAlias,\
    \ TypeVar\n\nclass TokenStream(Iterator):\n    def __init__(self, stream = sys.stdin):\n\
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
    \       return parse\n\nfrom typing import Iterable\n\nclass GraphProtocol(list,\
    \ Parsable):\n\n    def neighbors(G, v: int) -> Iterable[int]:\n        return\
    \ G[v]\n\n    @classmethod\n    def compile(cls, N: int, M: int, E):\n       \
    \ edge = Parser.compile(E)\n        def parse(ts: TokenStream):\n            return\
    \ cls(N, (edge(ts) for _ in range(M)))\n        return parse\nfrom operator import\
    \ itemgetter\n\nclass GraphWeighted(GraphProtocol):\n    def __init__(G, N: int,\
    \ edges=[]):\n        super().__init__([] for _ in range(N))\n        G.E = list(edges)\n\
    \        for u,v,*w in G.E:\n            G[u].append((v,*w))\n            G[v].append((u,*w))\n\
    \    \n    def neighbors(G, v: int):\n        return map(itemgetter(0), G[v])\n\
    \    \n    @classmethod\n    def compile(cls, N: int, M: int, E: type|int = EdgeWeighted[-1]):\n\
    \        if isinstance(E, int): E = EdgeWeighted[E]\n        return super().compile(N,\
    \ M, E)\n\nclass TreeWeighted(GraphWeighted):\n    @classmethod\n    def compile(cls,\
    \ N: int, E: type|int = EdgeWeighted[-1]):\n        return super().compile(N,\
    \ N-1, E)\n\nclass HLDWeighted:\n    def __init__(self, T, r=0):\n        N =\
    \ len(T)\n        # build\n        size = [1]*N\n        start = [0]*N\n     \
    \   end = [0]*N\n        par = [-1]*N\n        heavy = [-1]*N\n        head =\
    \ [-1]*N\n        depth = [0]*N\n        weights = [0]*N\n        order = [0]*N\n\
    \        time = 0\n\n        stack = [(2,r,r), (0,r,-1)]\n        while stack:\n\
    \            match stack.pop():\n                case 0, v, p: # dfs down\n  \
    \                  par[v] = p\n                    stack.append((1, v, p))\n \
    \                   for c, w in T[v]:\n                        if c != p:\n  \
    \                          depth[c] = depth[v] + 1 \n                        \
    \    weights[c] = w\n                            stack.append((0, c, v))\n\n \
    \               case 1, v, p: # dfs up\n                    l = -1\n         \
    \           for c, w in T[v]:\n                        if c != p:\n          \
    \                  size[v] += size[c]\n                            if l == -1\
    \ or size[c] > size[l]:\n                                l = c\n             \
    \       heavy[v] = l\n\n                case 2, v, h: # decompose down\n     \
    \               head[v] = h\n                    start[v] = time\n           \
    \         order[time] = v\n                    p = par[v]\n                  \
    \  time += 1\n                    l = heavy[v]\n                    stack.append((3,\
    \ v, h))\n                    \n                    for c, _ in T[v]:\n      \
    \                  if c != p and c != l:\n                            stack.append((2,\
    \ c, c))\n\n                    if l != -1:\n                        stack.append((2,\
    \ l, h))\n                case 3, v, h: # decompose up\n                    end[v]\
    \ = time\n        self.N = N\n        self.T = T\n        self.size = size\n \
    \       self.start = start\n        self.end = end\n        self.par = par\n \
    \       self.heavy = heavy\n        self.head = head\n        self.depth = depth\n\
    \        self.weights = weights\n        self.order = order\n\n    def __getitem__(self,\
    \ key):\n        return self.start[key]\n    \n    def path(self, u, v, edge=False):\n\
    \        head, depth, par, start = self.head, self.depth, self.par, self.start\n\
    \        while head[u] != head[v]:\n            if depth[head[u]] < depth[head[v]]:\n\
    \                u,v = v,u\n            yield start[head[u]], start[u]+1\n   \
    \         u = par[head[u]]\n\n        if depth[u] < depth[v]:\n            u,v\
    \ = v,u\n\n        yield start[v]+edge, start[u]+1\n\n\nfrom typing import Type,\
    \ TypeVar, overload\n\nT = TypeVar('T')\n@overload\ndef read(spec: int|None) ->\
    \ list[int]: ...\n@overload\ndef read(spec: Type[T]|T) -> T: ...\ndef read(spec:\
    \ Type[T]|T=None, char=False):\n    match spec, char:\n        case None, False:\n\
    \            return list(map(int, input().split()))\n        case int(offset),\
    \ False:\n            return [int(s)+offset for s in input().split()]\n      \
    \  case _, _:\n            if char:\n                stream = CharStream(sys.stdin)\n\
    \            else:\n                stream = TokenStream(sys.stdin)\n        \
    \    parser: T = Parser.compile(spec)\n            return parser(stream)\n\nif\
    \ __name__ == \"__main__\":\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc294/tasks/abc294_g\n\
    \ndef main():\n    N = read(int)\n    T = read(TreeWeighted[N])\n\n    hld = HLDWeighted(T)\n\
    \    W = [hld.weights[i] for i in hld.order]\n    bit = BinaryIndexTree(W)\n\n\
    \    Q = read(int)\n    for query in read(list[tuple[int, int, int], Q]):\n  \
    \      match query:\n            case 1, i, w:\n                i -= 1  # Convert\
    \ to 0-based index\n                u, v, _ = T.E[i]\n                # Find child\
    \ node in edge (u, v)\n                if hld.par[u] == v:\n                 \
    \   node = u\n                else:\n                    node = v\n          \
    \      idx = hld[node]\n                bit.set(idx, w)\n            case 2, u,\
    \ v:\n                u, v = u - 1, v - 1\n                ans = sum(bit.range_sum(l,r)\
    \ for l,r in hld.path(u,v, True))\n                print(ans)\n\nfrom cp_library.ds.bit_cls\
    \ import BinaryIndexTree\nfrom cp_library.alg.tree.tree_weighted_cls import TreeWeighted\n\
    from cp_library.alg.tree.heavy_light_decomposition_weighted_cls import HLDWeighted\n\
    from cp_library.io.read_specs_fn import read\n\nif __name__ == \"__main__\":\n\
    \    main()"
  dependsOn:
  - cp_library/ds/bit_cls.py
  - cp_library/alg/tree/tree_weighted_cls.py
  - cp_library/alg/tree/heavy_light_decomposition_weighted_cls.py
  - cp_library/io/read_specs_fn.py
  - cp_library/alg/graph/edge_weighted_cls.py
  - cp_library/alg/graph/graph_weighted_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/alg/graph/graph_proto.py
  - cp_library/alg/graph/edge_cls.py
  isVerificationFile: true
  path: test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
  requiredBy: []
  timestamp: '2024-10-06 18:38:39+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
layout: document
redirect_from:
- /verify/test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
- /verify/test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py.html
title: test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
---
