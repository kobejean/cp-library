---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/alg/graph/edge_cls.py
    title: cp_library/alg/graph/edge_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge_weighted_cls.py
    title: cp_library/alg/graph/edge_weighted_cls.py
  - icon: ':question:'
    path: cp_library/alg/graph/graph_proto.py
    title: cp_library/alg/graph/graph_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/graph_weighted_cls.py
    title: cp_library/alg/graph/graph_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/graph_weighted_proto.py
    title: cp_library/alg/graph/graph_weighted_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/heavy_light_decomposition_weighted_cls.py
    title: cp_library/alg/tree/heavy_light_decomposition_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/lca_table_iterative_cls.py
    title: cp_library/alg/tree/lca_table_iterative_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
    title: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_proto.py
    title: cp_library/alg/tree/tree_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_weighted_cls.py
    title: cp_library/alg/tree/tree_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_weighted_proto.py
    title: cp_library/alg/tree/tree_weighted_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/bit_cls.py
    title: cp_library/ds/bit_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/dsu_cls.py
    title: cp_library/ds/dsu_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/sparse_table_cls.py
    title: cp_library/ds/sparse_table_cls.py
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
    \       return parse\n\n\nfrom typing import overload\nfrom heapq import heapify,\
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
    \    return D\n\n\nclass DSU:\n    def __init__(self, n):\n        self.n = n\n\
    \        self.par = [-1] * n\n\n    def merge(self, u, v):\n        assert 0 <=\
    \ u < self.n\n        assert 0 <= v < self.n\n\n        x, y = self.leader(u),\
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
    \ int): E = EdgeWeighted[E]\n        return super().compile(N, M, E)\n\nfrom functools\
    \ import cached_property\n\nfrom typing import overload, Literal\n\nfrom typing\
    \ import Any, Callable, List\n\nclass SparseTable:\n    def __init__(self, op:\
    \ Callable[[Any, Any], Any], arr: List[Any]):\n        self.n = len(arr)\n   \
    \     self.log = self.n.bit_length()\n        self.op = op\n        self.st =\
    \ [[None] * (self.n-(1<<i)+1) for i in range(self.log)]\n        self.st[0] =\
    \ arr[:]\n        \n        for i in range(self.log-1):\n            row, d =\
    \ self.st[i], 1<<i\n            for j in range(len(self.st[i+1])):\n         \
    \       self.st[i+1][j] = op(row[j], row[j+d])\n\n    def query(self, l: int,\
    \ r: int) -> Any:\n        k = (r-l).bit_length()-1\n        return self.op(self.st[k][l],\
    \ self.st[k][r-(1<<k)])\n    \n    def __repr__(self) -> str:\n        return\
    \ '\\n'.join(f'{i:<2d} {row}' for i,row in enumerate(self.st))\n\nclass LCATable(SparseTable):\n\
    \    def __init__(self, T, root = 0):\n        self.start = [-1] * len(T)\n  \
    \      self.end = [-1] * len(T)\n        self.euler = []\n        self.depth =\
    \ []\n        \n        # Iterative DFS\n        stack = [(root, -1, 0)]\n   \
    \     while stack:\n            u, p, d = stack.pop()\n            \n        \
    \    if self.start[u] == -1:\n                self.start[u] = len(self.euler)\n\
    \                \n                for v in reversed(T[u]):\n                \
    \    if v != p:\n                        stack.append((u, p, d))\n           \
    \             stack.append((v, u, d+1))\n                        \n          \
    \  self.euler.append(u)\n            self.depth.append(d)\n            self.end[u]\
    \ = len(self.euler)\n        super().__init__(min, list(zip(self.depth, self.euler)))\n\
    \n    def query(self, u, v) -> tuple[int,int]:\n        l, r = min(self.start[u],\
    \ self.start[v]), max(self.start[u], self.start[v])+1\n        d, a = super().query(l,\
    \ r)\n        return a, d\n    \n    def distance(self, u, v) -> int:\n      \
    \  l, r = min(self.start[u], self.start[v]), max(self.start[u], self.start[v])+1\n\
    \        d, _ = super().query(l, r)\n        return self.depth[l] + self.depth[r]\
    \ - 2*d\n        \n\nclass TreeProtocol(GraphProtocol):\n\n    @cached_property\n\
    \    def lca(T):\n        return LCATable(T)\n    \n    @overload\n    def diameter(T)\
    \ -> int: ...\n    @overload\n    def diameter(T, endpoints: Literal[True]) ->\
    \ tuple[int,int,int]: ...\n    def diameter(T, endpoints = False):\n        _,\
    \ s = max((d,v) for v,d in enumerate(T.dfs(0)))\n        diam, g = max((d,v) for\
    \ v,d in enumerate(T.dfs(s)))\n        return (diam, s, g) if endpoints else diam\n\
    \    \n    @overload\n    def distance(T) -> list[list[int]]: ...\n    @overload\n\
    \    def distance(T, s: int = 0) -> list[int]: ...\n    @overload\n    def distance(T,\
    \ s: int, g: int) -> int: ...\n    def distance(T, s = None, g = None):\n    \
    \    match s, g:\n            case None, None:\n                return [T.dfs(u)\
    \ for u in range(T.N)]\n            case s, g:\n                return T.dfs(s,\
    \ g)\n            \n    @overload\n    def dfs(T, s: int = 0) -> list[int]: ...\n\
    \    @overload\n    def dfs(T, s: int, g: int) -> int: ...\n    def dfs(T, s =\
    \ 0, g = None):\n        D = [inf for _ in range(T.N)]\n        D[s] = 0\n   \
    \     state = [True for _ in range(T.N)]\n        stack = [s]\n\n        while\
    \ stack:\n            u = stack.pop()\n            if u == g: return D[u]\n  \
    \          state[u] = False\n            for v in T[u]:\n                if state[v]:\n\
    \                    D[v] = D[u]+1\n                    stack.append(v)\n    \
    \    return D if g is None else inf \n\n\n    \nfrom itertools import accumulate\n\
    \nclass LCATableWeighted(SparseTable):\n    def __init__(self, T, root = 0):\n\
    \        self.start = [-1] * len(T)\n        self.end = [-1] * len(T)\n      \
    \  self.euler = []\n        self.depth = []\n        self.weights = []\n     \
    \   self.weighted_depth = None\n        \n        # Iterative DFS\n        stack\
    \ = [(root, -1, 0, 0)]\n        while stack:\n            u, p, d, w = stack.pop()\n\
    \            \n            if self.start[u] == -1:\n                self.start[u]\
    \ = len(self.euler)\n                for v, nw in reversed(T[u]):\n          \
    \          if v != p:\n                        stack.append((u, p, d, -nw))\n\
    \                        stack.append((v, u, d+1, nw))\n\n            self.euler.append(u)\n\
    \            self.depth.append(d)\n            self.weights.append(w)\n      \
    \      self.end[u] = len(self.euler)\n        super().__init__(min, list(zip(self.depth,\
    \ self.euler)))\n\n    def query(self, u, v) -> tuple[int,int]:\n        l, r\
    \ = min(self.start[u], self.start[v]), max(self.start[u], self.start[v])+1\n \
    \       d, a = super().query(l, r)\n        return a, d\n\n    def distance(self,\
    \ u, v) -> int:\n        if self.weighted_depth is None:\n            self.weighted_depth\
    \ = list(accumulate(self.weights))\n        l, r = min(self.start[u], self.start[v]),\
    \ max(self.start[u], self.start[v])+1\n        _, a = super().query(l, r)\n  \
    \      m = self.start[a]\n        return self.weighted_depth[l] + self.weighted_depth[r]\
    \ - 2*self.weighted_depth[m]\n\nclass TreeWeightedProtocol(GraphWeightedProtocol,\
    \ TreeProtocol):\n\n    @cached_property\n    def lca(T):\n        return LCATableWeighted(T)\n\
    \    \n    @overload\n    def dfs(T, s: int = 0) -> list[int]: ...\n    @overload\n\
    \    def dfs(T, s: int, g: int) -> int: ...\n    def dfs(T, s = 0, g = None):\n\
    \        D = [inf for _ in range(T.N)]\n        D[s] = 0\n        state = [True\
    \ for _ in range(T.N)]\n        stack = [s]\n\n        while stack:\n        \
    \    u = stack.pop()\n            if u == g: return D[u]\n            state[u]\
    \ = False\n            for v, w, *_ in T[u]:\n                if state[v]:\n \
    \                   D[v] = D[u]+w\n                    stack.append(v)\n     \
    \   return D if g is None else inf \n\nclass TreeWeighted(GraphWeighted, TreeWeightedProtocol):\n\
    \    @classmethod\n    def compile(cls, N: int, E: type|int = EdgeWeighted[-1]):\n\
    \        return super().compile(N, N-1, E)\n\nclass HLDWeighted:\n    def __init__(self,\
    \ T, r=0):\n        N = len(T)\n        # build\n        size = [1]*N\n      \
    \  start = [0]*N\n        end = [0]*N\n        par = [-1]*N\n        heavy = [-1]*N\n\
    \        head = [-1]*N\n        depth = [0]*N\n        weights = [0]*N\n     \
    \   order = [0]*N\n        time = 0\n\n        stack = [(2,r,r), (0,r,-1)]\n \
    \       while stack:\n            match stack.pop():\n                case 0,\
    \ v, p: # dfs down\n                    par[v] = p\n                    stack.append((1,\
    \ v, p))\n                    for c, w in T[v]:\n                        if c\
    \ != p:\n                            depth[c] = depth[v] + 1 \n              \
    \              weights[c] = w\n                            stack.append((0, c,\
    \ v))\n\n                case 1, v, p: # dfs up\n                    l = -1\n\
    \                    for c, w in T[v]:\n                        if c != p:\n \
    \                           size[v] += size[c]\n                            if\
    \ l == -1 or size[c] > size[l]:\n                                l = c\n     \
    \               heavy[v] = l\n\n                case 2, v, h: # decompose down\n\
    \                    head[v] = h\n                    start[v] = time\n      \
    \              order[time] = v\n                    p = par[v]\n             \
    \       time += 1\n                    l = heavy[v]\n                    stack.append((3,\
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
    \ list[int]: ...\n@overload\ndef read(spec: Type[T]|T, char=False) -> T: ...\n\
    def read(spec: Type[T]|T=None, char=False):\n    match spec, char:\n        case\
    \ None, False:\n            return list(map(int, input().split()))\n        case\
    \ int(offset), False:\n            return [int(s)+offset for s in input().split()]\n\
    \        case _, _:\n            if char:\n                stream = CharStream(sys.stdin)\n\
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
  - cp_library/alg/tree/tree_weighted_proto.py
  - cp_library/io/parser_cls.py
  - cp_library/alg/graph/graph_weighted_proto.py
  - cp_library/alg/tree/tree_proto.py
  - cp_library/alg/tree/lca_table_weighted_iterative_cls.py
  - cp_library/alg/graph/edge_cls.py
  - cp_library/alg/graph/graph_proto.py
  - cp_library/ds/dsu_cls.py
  - cp_library/alg/tree/lca_table_iterative_cls.py
  - cp_library/ds/sparse_table_cls.py
  isVerificationFile: true
  path: test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
  requiredBy: []
  timestamp: '2024-11-04 21:00:10+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
layout: document
redirect_from:
- /verify/test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
- /verify/test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py.html
title: test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
---