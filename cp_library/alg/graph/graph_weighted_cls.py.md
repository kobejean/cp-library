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
    path: cp_library/alg/graph/graph_weighted_proto.py
    title: cp_library/alg/graph/graph_weighted_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/dsu_cls.py
    title: cp_library/ds/dsu_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_weighted_cls.py
    title: cp_library/alg/tree/tree_weighted_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
    title: test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
    title: test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc361_e_tree_diameter.test.py
    title: test/abc361_e_tree_diameter.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc375_g_find_bridges.test.py
    title: test/abc375_g_find_bridges.test.py
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
    \n\n\n\nimport sys\nimport typing\nfrom collections import deque\nfrom numbers\
    \ import Number\nfrom typing import Callable, Collection, Iterator, TypeAlias,\
    \ TypeVar\n\nclass TokenStream(Iterator):\n    def __init__(self, stream = sys.stdin):\n\
    \        self.stream = stream\n        self.queue = deque()\n\n    def __next__(self):\n\
    \        if not self.queue: self.queue.extend(self.line())\n        return self.queue.popleft()\n\
    \    \n    def wait(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        while self.queue: yield\n        \n    def line(self):\n        assert\
    \ not self.queue\n        return next(self.stream).rstrip().split()\n\nclass CharStream(TokenStream):\n\
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
    \       return parse\n\nfrom typing import overload\nfrom heapq import heapify,\
    \ heappop, heappush\nimport operator\nfrom math import inf\n\n\nfrom typing import\
    \ Iterable, overload\n\nclass GraphProtocol(list, Parsable):\n\n    def neighbors(G,\
    \ v: int) -> Iterable[int]:\n        return G[v]\n    \n    def edge_ids(G) ->\
    \ list[list[int]]: ...\n\n    @overload\n    def distance(G) -> list[list[int]]:\
    \ ...\n    @overload\n    def distance(G, s: int = 0) -> list[int]: ...\n    @overload\n\
    \    def distance(G, s: int, g: int) -> int: ...\n    def distance(G, s = None,\
    \ g = None):\n        match s, g:\n            case None, None:\n            \
    \    return G.floyd_warshall()\n            case s, None:\n                return\
    \ G.bfs(s)\n            case s, g:\n                return G.bfs(s, g)\n\n   \
    \ @overload\n    def bfs(G, s: int = 0) -> list[int]: ...\n    @overload\n   \
    \ def bfs(G, s: int, g: int) -> int: ...\n    def bfs(G, s = 0, g = None):\n \
    \       D = [inf for _ in range(G.N)]\n        D[s] = 0\n        q = deque([s])\n\
    \        while q:\n            nd = D[u := q.popleft()]+1\n            if u ==\
    \ g: return D[u]\n            for v in G.neighbors(u):\n                if nd\
    \ < D[v]:\n                    D[v] = nd\n                    q.append(v)\n  \
    \      return D if g is None else inf    \n    \n    \n    def floyd_warshall(G)\
    \ -> list[list[int]]:\n        D = [[inf]*G.N for _ in range(G.N)]\n\n       \
    \ for u in G:\n            D[u][u] = 0\n            for v in G.neighbors(u):\n\
    \                D[u][v] = 1\n        \n        for k, Dk in enumerate(D):\n \
    \           for Di in D:\n                for j in range(G.N):\n             \
    \       Di[j] = min(Di[j], Di[k]+Dk[j])\n        return D\n    \n    \n    def\
    \ find_cycle(G, s = 0, vis = None, par = None):\n        N = G.N\n        vis\
    \ = vis or [0] * N\n        par = par or [-1] * N\n        if vis[s]: return None\n\
    \        vis[s] = 1\n        stack = [(True, s)]\n        while stack:\n     \
    \       forw, v = stack.pop()\n            if forw:\n                stack.append((False,\
    \ v))\n                vis[v] = 1\n                for u in G.neighbors(v):\n\
    \                    if vis[u] == 1 and u != par[v]:\n                       \
    \ # Cycle detected\n                        cyc = [u]\n                      \
    \  vis[u] = 2\n                        while v != u:\n                       \
    \     cyc.append(v)\n                            vis[v] = 2\n                \
    \            v = par[v]\n                        return cyc\n                \
    \    elif vis[u] == 0:\n                        par[u] = v\n                 \
    \       stack.append((True, u))\n            else:\n                vis[v] = 2\n\
    \        return None\n    \n    def bridges(G):\n        tin = [-1] * G.N\n  \
    \      low = [-1] * G.N\n        par = [-1] * G.N\n        vis = [0] * G.N\n \
    \       in_edge = [-1] * G.N\n\n        Eid = G.edge_ids()\n        time = 0\n\
    \        bridges = []\n        stack = list(range(G.N))\n        while stack:\n\
    \            v = stack.pop()\n            p = par[v]\n            match vis[v]:\n\
    \                case 0:\n                    vis[v] = 1\n                   \
    \ tin[v] = low[v] = time\n                    time += 1\n                    stack.append(v)\n\
    \                    for i, child in enumerate(G.neighbors(v)):\n            \
    \            if child == p:\n                            continue\n          \
    \              match vis[child]:\n                            case 0:\n      \
    \                          # Tree edge - recurse\n                           \
    \     par[child] = v\n                                in_edge[child] = Eid[v][i]\n\
    \                                stack.append(child)\n                       \
    \     case 1:\n                                # Back edge - update low-link value\n\
    \                                low[v] = min(low[v], tin[child])\n          \
    \      case 1:\n                    vis[v] = 2\n                    if p != -1:\n\
    \                        low[p] = min(low[p], low[v])\n                      \
    \  if low[v] > tin[p]:\n                            bridges.append(in_edge[v])\n\
    \                \n        return bridges\n\n    def articulation_points(G):\n\
    \        N = G.N\n        order = [-1] * N\n        low = [-1] * N\n        par\
    \ = [-1] * N\n        vis = [0] * G.N\n        children = [0] * G.N\n        ap\
    \ = [False] * N\n        time = 0\n        stack = list(range(N))\n\n        while\
    \ stack:\n            v = stack.pop()\n            p = par[v]\n            if\
    \ vis[v] == 0:\n                vis[v] = 1\n                order[v] = low[v]\
    \ = time\n                time += 1\n            \n                stack.append(v)\n\
    \                for child in G[v]:\n                    if order[child] == -1:\n\
    \                        par[child] = v\n                        stack.append(child)\n\
    \                    elif child != p:\n                        low[v] = min(low[v],\
    \ order[child])\n                if p != -1:\n                    children[p]\
    \ += 1\n            elif vis[v] == 1:\n                vis[v] = 2\n          \
    \      ap[v] |= p == -1 and children[v] > 1\n                if p != -1:\n   \
    \                 low[p] = min(low[p], low[v])\n                    ap[p] |= par[p]\
    \ != -1 and low[v] >= order[p]\n\n        return ap\n\n    @classmethod\n    def\
    \ compile(cls, N: int, M: int, E):\n        edge = Parser.compile(E)\n       \
    \ def parse(ts: TokenStream):\n            return cls(N, (edge(ts) for _ in range(M)))\n\
    \        return parse\n    \n\nclass GraphWeightedProtocol(GraphProtocol):\n\n\
    \    def neighbors(G, v: int):\n        return map(operator.itemgetter(0), G[v])\n\
    \    \n    @overload\n    def distance(G) -> list[list[int]]: ...\n    @overload\n\
    \    def distance(G, s: int = 0) -> list[int]: ...\n    @overload\n    def distance(G,\
    \ s: int, g: int) -> int: ...\n    def distance(G, s = None, g = None):\n    \
    \    match s, g:\n            case None, None:\n                return G.floyd_warshall()\n\
    \            case s, None:\n                return G.dijkstra(s)\n           \
    \ case s, g:\n                return G.dijkstra(s, g)\n    \n    def dijkstra(G,\
    \ s = 0, g = None):\n        D = [inf for _ in range(G.N)]\n        D[s] = 0\n\
    \        q = [(0, s)]\n        while q:\n            d, v = heappop(q)\n     \
    \       if d > D[v]: continue\n            if v == g: return d\n            for\
    \ u, w, *_ in G[v]:\n                if (nd := d + w) < D[u]:\n              \
    \      D[u] = nd\n                    heappush(q, (nd, u))\n        return D if\
    \ g is None else inf\n    \n    def kruskal(G):\n        E, N = G.E, G.N\n   \
    \     heapify(E)\n        dsu = DSU(N)\n        MST = []\n        need = N-1\n\
    \        while E and need:\n            edge = heappop(E)\n            u,v,*_\
    \ = edge\n            u,v = dsu.merge(u,v)\n            if u != v:\n         \
    \       MST.append(edge)\n                need -= 1\n        cls = type(G)\n \
    \       return cls(N, MST)\n    \n    def bellman_ford(G, s = 0) -> list[int]:\n\
    \        D = [inf]*G.N\n        D[s] = 0\n        for _ in range(G.N-1):\n   \
    \         for u, edges in enumerate(G):\n                for v,w,*_ in edges:\n\
    \                    D[v] = min(D[v], D[u] + w)\n        return D\n    \n    def\
    \ floyd_warshall(G) -> list[list[int]]:\n        D = [[inf]*G.N for _ in range(G.N)]\n\
    \n        for u, edges in enumerate(G):\n            D[u][u] = 0\n           \
    \ for v,w in edges:\n                D[u][v] = min(D[u][v], w)\n        \n   \
    \     for k, Dk in enumerate(D):\n            for Di in D:\n                for\
    \ j in range(G.N):\n                    Di[j] = min(Di[j], Di[k]+Dk[j])\n    \
    \    return D\n\n\n\nclass DSU:\n    def __init__(self, n):\n        self.n =\
    \ n\n        self.par = [-1] * n\n\n    def merge(self, u, v):\n        assert\
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
    \        return list(filter(lambda r: r, result))\n\nclass GraphWeighted(GraphWeightedProtocol):\n\
    \    def __init__(G, N: int, edges=[]):\n        super().__init__([] for _ in\
    \ range(N))\n        G.E = list(edges)\n        G.N, G.M = N, len(G.E)\n     \
    \   for u,v,*w in G.E:\n            G[u].append((v,*w))\n            G[v].append((u,*w))\n\
    \    \n    def edge_ids(G) -> list[list[int]]:\n        Eid = [[] for _ in range(G.N)]\n\
    \        for e,(u,v,*w) in enumerate(G.E):\n            Eid[u].append(e)\n   \
    \         Eid[v].append(e)\n        return Eid\n    \n    @classmethod\n    def\
    \ compile(cls, N: int, M: int, E: type|int = EdgeWeighted[-1]):\n        if isinstance(E,\
    \ int): E = EdgeWeighted[E]\n        return super().compile(N, M, E)\n"
  code: "import cp_library.alg.graph.__header__\n\nfrom cp_library.alg.graph.edge_weighted_cls\
    \ import EdgeWeighted\nfrom cp_library.alg.graph.graph_weighted_proto import GraphWeightedProtocol\n\
    \nclass GraphWeighted(GraphWeightedProtocol):\n    def __init__(G, N: int, edges=[]):\n\
    \        super().__init__([] for _ in range(N))\n        G.E = list(edges)\n \
    \       G.N, G.M = N, len(G.E)\n        for u,v,*w in G.E:\n            G[u].append((v,*w))\n\
    \            G[v].append((u,*w))\n    \n    def edge_ids(G) -> list[list[int]]:\n\
    \        Eid = [[] for _ in range(G.N)]\n        for e,(u,v,*w) in enumerate(G.E):\n\
    \            Eid[u].append(e)\n            Eid[v].append(e)\n        return Eid\n\
    \    \n    @classmethod\n    def compile(cls, N: int, M: int, E: type|int = EdgeWeighted[-1]):\n\
    \        if isinstance(E, int): E = EdgeWeighted[E]\n        return super().compile(N,\
    \ M, E)\n"
  dependsOn:
  - cp_library/alg/graph/edge_weighted_cls.py
  - cp_library/alg/graph/graph_weighted_proto.py
  - cp_library/io/parser_cls.py
  - cp_library/alg/graph/edge_cls.py
  - cp_library/alg/graph/graph_proto.py
  - cp_library/ds/dsu_cls.py
  isVerificationFile: false
  path: cp_library/alg/graph/graph_weighted_cls.py
  requiredBy:
  - cp_library/alg/tree/tree_weighted_cls.py
  timestamp: '2024-11-05 04:28:32+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/abc375_g_find_bridges.test.py
  - test/abc361_e_tree_diameter.test.py
  - test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
  - test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
documentation_of: cp_library/alg/graph/graph_weighted_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/graph_weighted_cls.py
- /library/cp_library/alg/graph/graph_weighted_cls.py.html
title: cp_library/alg/graph/graph_weighted_cls.py
---
