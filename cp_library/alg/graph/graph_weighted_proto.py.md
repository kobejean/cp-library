---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/alg/graph/dfs_options_cls.py
    title: cp_library/alg/graph/dfs_options_cls.py
  - icon: ':question:'
    path: cp_library/alg/graph/graph_proto.py
    title: cp_library/alg/graph/graph_proto.py
  - icon: ':question:'
    path: cp_library/ds/dsu_cls.py
    title: cp_library/ds/dsu_cls.py
  - icon: ':question:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  - icon: ':question:'
    path: cp_library/ds/heap_proto.py
    title: cp_library/ds/heap_proto.py
  - icon: ':question:'
    path: cp_library/ds/priority_queue_cls.py
    title: cp_library/ds/priority_queue_cls.py
  - icon: ':question:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':question:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':question:'
    path: cp_library/math/inft_cnst.py
    title: cp_library/math/inft_cnst.py
  _extendedRequiredBy:
  - icon: ':question:'
    path: cp_library/alg/graph/digraph_weighted_cls.py
    title: cp_library/alg/graph/digraph_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/graph_weighted_cls.py
    title: cp_library/alg/graph/graph_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_weighted_cls.py
    title: cp_library/alg/tree/tree_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_weighted_proto.py
    title: cp_library/alg/tree/tree_weighted_proto.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/abc218_f_shortest_path_weighted.test.py
    title: test/abc218_f_shortest_path_weighted.test.py
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
  - icon: ':heavy_check_mark:'
    path: test/grl_1_a_dijkstra.test.py
    title: test/grl_1_a_dijkstra.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_1_a_graph_distance.test.py
    title: test/grl_1_a_graph_distance.test.py
  - icon: ':x:'
    path: test/grl_1_b_bellman_ford.test.py
    title: test/grl_1_b_bellman_ford.test.py
  - icon: ':x:'
    path: test/grl_1_b_graph_bellman_ford.test.py
    title: test/grl_1_b_graph_bellman_ford.test.py
  - icon: ':x:'
    path: test/grl_1_c_floyd_warshall.test.py
    title: test/grl_1_c_floyd_warshall.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_2_a_graph_kruskal.test.py
    title: test/grl_2_a_graph_kruskal.test.py
  - icon: ':heavy_check_mark:'
    path: test/shortest_path_graph_weighted.test.py
    title: test/shortest_path_graph_weighted.test.py
  - icon: ':heavy_check_mark:'
    path: test/shortest_path_min_heap.test.py
    title: test/shortest_path_min_heap.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':question:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \nfrom typing import overload\nfrom heapq import heapify, heappop, heappush\n\
    import operator\n\n\nfrom enum import auto, IntFlag, IntEnum\n\nclass DFSFlags(IntFlag):\n\
    \    ENTER = auto()\n    DOWN = auto()\n    BACK = auto()\n    CROSS = auto()\n\
    \    LEAVE = auto()\n    UP = auto()\n    MAXDEPTH = auto()\n\n    RETURN_PARENTS\
    \ = auto()\n    RETURN_DEPTHS = auto()\n    BACKTRACK = auto()\n    CONNECT_ROOTS\
    \ = auto()\n\n    # Common combinations\n    ALL_EDGES = DOWN | BACK | CROSS\n\
    \    EULER_TOUR = DOWN | UP\n    INTERVAL = ENTER | LEAVE\n    TOPDOWN = DOWN\
    \ | CONNECT_ROOTS\n    BOTTOMUP = UP | CONNECT_ROOTS\n    RETURN_ALL = RETURN_PARENTS\
    \ | RETURN_DEPTHS\n\nclass DFSEvent(IntEnum):\n    ENTER = DFSFlags.ENTER \n \
    \   DOWN = DFSFlags.DOWN \n    BACK = DFSFlags.BACK \n    CROSS = DFSFlags.CROSS\
    \ \n    LEAVE = DFSFlags.LEAVE \n    UP = DFSFlags.UP \n    MAXDEPTH = DFSFlags.MAXDEPTH\n\
    \    \nimport sys\n\n\nimport typing\nfrom collections import deque\nfrom numbers\
    \ import Number\nfrom types import GenericAlias \nfrom typing import Callable,\
    \ Collection, Iterator, TypeVar, Union\nimport os\nfrom io import BytesIO, IOBase\n\
    \n\nclass FastIO(IOBase):\n    BUFSIZE = 8192\n    newlines = 0\n\n    def __init__(self,\
    \ file):\n        self._fd = file.fileno()\n        self.buffer = BytesIO()\n\
    \        self.writable = \"x\" in file.mode or \"r\" not in file.mode\n      \
    \  self.write = self.buffer.write if self.writable else None\n\n    def read(self):\n\
    \        BUFSIZE = self.BUFSIZE\n        while True:\n            b = os.read(self._fd,\
    \ max(os.fstat(self._fd).st_size, BUFSIZE))\n            if not b:\n         \
    \       break\n            ptr = self.buffer.tell()\n            self.buffer.seek(0,\
    \ 2), self.buffer.write(b), self.buffer.seek(ptr)\n        self.newlines = 0\n\
    \        return self.buffer.read()\n\n    def readline(self):\n        BUFSIZE\
    \ = self.BUFSIZE\n        while self.newlines == 0:\n            b = os.read(self._fd,\
    \ max(os.fstat(self._fd).st_size, BUFSIZE))\n            self.newlines = b.count(b\"\
    \\n\") + (not b)\n            ptr = self.buffer.tell()\n            self.buffer.seek(0,\
    \ 2), self.buffer.write(b), self.buffer.seek(ptr)\n        self.newlines -= 1\n\
    \        return self.buffer.readline()\n\n    def flush(self):\n        if self.writable:\n\
    \            os.write(self._fd, self.buffer.getvalue())\n            self.buffer.truncate(0),\
    \ self.buffer.seek(0)\n\n\nclass IOWrapper(IOBase):\n    stdin: 'IOWrapper' =\
    \ None\n    stdout: 'IOWrapper' = None\n    \n    def __init__(self, file):\n\
    \        self.buffer = FastIO(file)\n        self.flush = self.buffer.flush\n\
    \        self.writable = self.buffer.writable\n\n    def write(self, s):\n   \
    \     return self.buffer.write(s.encode(\"ascii\"))\n    \n    def read(self):\n\
    \        return self.buffer.read().decode(\"ascii\")\n    \n    def readline(self):\n\
    \        return self.buffer.readline().decode(\"ascii\")\n\nsys.stdin = IOWrapper.stdin\
    \ = IOWrapper(sys.stdin)\nsys.stdout = IOWrapper.stdout = IOWrapper(sys.stdout)\n\
    \n\nclass TokenStream(Iterator):\n    stream = IOWrapper.stdin\n\n    def __init__(self):\n\
    \        self.queue = deque()\n\n    def __next__(self):\n        if not self.queue:\
    \ self.queue.extend(self.line())\n        return self.queue.popleft()\n    \n\
    \    def wait(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        while self.queue: yield\n        \n    def line(self):\n        return\
    \ TokenStream.stream.readline().split()\n\nclass CharStream(TokenStream):\n  \
    \  def line(self):\n        assert not self.queue\n        return next(TokenStream.stream).rstrip()\n\
    \        \nT = TypeVar('T')\nParseFn = Callable[[TokenStream],T]\nclass Parser:\n\
    \    def __init__(self, spec: Union[type[T],T]):\n        self.parse = Parser.compile(spec)\n\
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
    \    def compile(spec: Union[type[T],T]=int) -> ParseFn[T]:\n        if isinstance(spec,\
    \ (type, GenericAlias)):\n            cls = typing.get_origin(spec) or spec\n\
    \            args = typing.get_args(spec) or tuple()\n            return Parser.compile_type(cls,\
    \ args)\n        elif isinstance(offset := spec, Number): \n            cls =\
    \ type(spec)  \n            def parse(ts: TokenStream):\n                return\
    \ cls(next(ts)) + offset\n            return parse\n        elif isinstance(args\
    \ := spec, tuple):      \n            return Parser.compile_tuple(type(spec),\
    \ args)\n        elif isinstance(args := spec, Collection):  \n            return\
    \ Parser.compile_collection(type(spec), args)\n        else:\n            raise\
    \ NotImplementedError()\n    \n    @staticmethod\n    def compile_line(cls: T,\
    \ spec=int) -> ParseFn[T]:\n        if spec is int:\n            fn = Parser.compile(spec)\n\
    \            def parse(ts: TokenStream):\n                return cls((int(token)\
    \ for token in ts.line()))\n            return parse\n        else:\n        \
    \    fn = Parser.compile(spec)\n            def parse(ts: TokenStream):\n    \
    \            return cls((fn(ts) for _ in ts.wait()))\n            return parse\n\
    \n    @staticmethod\n    def compile_repeat(cls: T, spec, N) -> ParseFn[T]:\n\
    \        fn = Parser.compile(spec)\n        def parse(ts: TokenStream):\n    \
    \        return cls((fn(ts) for _ in range(N)))\n        return parse\n\n    @staticmethod\n\
    \    def compile_children(cls: T, specs) -> ParseFn[T]:\n        fns = tuple((Parser.compile(spec)\
    \ for spec in specs))\n        def parse(ts: TokenStream):\n            return\
    \ cls((fn(ts) for fn in fns))  \n        return parse\n            \n    @staticmethod\n\
    \    def compile_tuple(cls: type[T], specs) -> ParseFn[T]:\n        if isinstance(specs,\
    \ (tuple,list)) and len(specs) == 2 and specs[1] is ...:\n            return Parser.compile_line(cls,\
    \ specs[0])\n        else:\n            return Parser.compile_children(cls, specs)\n\
    \n    @staticmethod\n    def compile_collection(cls, specs):\n        if not specs\
    \ or len(specs) == 1 or isinstance(specs, set):\n            return Parser.compile_line(cls,\
    \ *specs)\n        elif (isinstance(specs, (tuple,list)) and len(specs) == 2 \n\
    \            and isinstance(specs[1], int)):\n            return Parser.compile_repeat(cls,\
    \ specs[0], specs[1])\n        else:\n            raise NotImplementedError()\n\
    \nclass Parsable:\n    @classmethod\n    def compile(cls):\n        def parser(ts:\
    \ TokenStream):\n            return cls(next(ts))\n        return parser\n\n\n\
    def elist(est_len: int) -> list: ...\ntry:\n    from __pypy__ import newlist_hint\n\
    except:\n    def newlist_hint(hint):\n        return []\nelist = newlist_hint\n\
    \    \nfrom typing import Iterable, overload\n\n\ninft = sys.maxsize\n\nclass\
    \ GraphProtocol(list, Parsable):\n    def __init__(G, N: int, E: list = None,\
    \ adj: Iterable = None):\n        G.N = N\n        if E is not None:\n       \
    \     G.M, G.E = len(E), E\n        if adj is not None:\n            super().__init__(adj)\n\
    \n    def neighbors(G, v: int) -> Iterable[int]:\n        return G[v]\n    \n\
    \    def edge_ids(G) -> list[list[int]]: ...\n\n    @overload\n    def distance(G)\
    \ -> list[list[int]]: ...\n    @overload\n    def distance(G, s: int = 0) -> list[int]:\
    \ ...\n    @overload\n    def distance(G, s: int, g: int) -> int: ...\n    def\
    \ distance(G, s = None, g = None):\n        match s, g:\n            case None,\
    \ None:\n                return G.floyd_warshall()\n            case s, None:\n\
    \                return G.bfs(s)\n            case s, g:\n                return\
    \ G.bfs(s, g)\n\n    @overload\n    def bfs(G, s: int|list = 0) -> list[int]:\
    \ ...\n    @overload\n    def bfs(G, s: int|list, g: int) -> int: ...\n    def\
    \ bfs(G, s = 0, g = None):\n        D = [inft for _ in range(G.N)]\n        q\
    \ = deque([s] if isinstance(s, int) else s)\n        for u in q: D[u] = 0\n  \
    \      while q:\n            nd = D[u := q.popleft()]+1\n            if u == g:\
    \ return D[u]\n            for v in G.neighbors(u):\n                if nd < D[v]:\n\
    \                    D[v] = nd\n                    q.append(v)\n        return\
    \ D if g is None else inft \n\n    @overload\n    def shortest_path(G, s: int,\
    \ g: int) -> list[int]|None: ...\n    @overload\n    def shortest_path(G, s: int,\
    \ g: int, distances = True) -> tuple[list[int]|None,list[int]]: ...\n    def shortest_path(G,\
    \ s: int, g: int, distances = False) -> list[int]:\n        D = [inft] * G.N\n\
    \        D[s] = 0\n        if s == g:\n            return ([], D) if distances\
    \ else []\n            \n        par = [-1] * G.N\n        par_edge = [-1] * G.N\n\
    \        Eid = G.edge_ids()\n        q = deque([s])\n        \n        while q:\n\
    \            nd = D[u := q.popleft()] + 1\n            if u == g: break\n    \
    \            \n            for v, eid in zip(G[u], Eid[u]):\n                if\
    \ nd < D[v]:\n                    D[v] = nd\n                    par[v] = u\n\
    \                    par_edge[v] = eid\n                    q.append(v)\n    \
    \    \n        if D[g] == inft:\n            return (None, D) if distances else\
    \ None\n            \n        path = []\n        current = g\n        while current\
    \ != s:\n            path.append(par_edge[current])\n            current = par[current]\n\
    \            \n        return (path[::-1], D) if distances else path[::-1]\n \
    \           \n     \n            \n        \n    def floyd_warshall(G) -> list[list[int]]:\n\
    \        D = [[inft]*G.N for _ in range(G.N)]\n\n        for u in range(G.N):\n\
    \            D[u][u] = 0\n            for v in G.neighbors(u):\n             \
    \   D[u][v] = 1\n        \n        for k, Dk in enumerate(D):\n            for\
    \ Di in D:\n                for j in range(G.N):\n                    Di[j] =\
    \ min(Di[j], Di[k]+Dk[j])\n        return D\n    \n    \n    def find_cycle(G,\
    \ s = 0, vis = None, par = None):\n        N = G.N\n        vis = vis or [0] *\
    \ N\n        par = par or [-1] * N\n        if vis[s]: return None\n        vis[s]\
    \ = 1\n        stack = [(True, s)]\n        while stack:\n            forw, v\
    \ = stack.pop()\n            if forw:\n                stack.append((False, v))\n\
    \                vis[v] = 1\n                for u in G.neighbors(v):\n      \
    \              if vis[u] == 1 and u != par[v]:\n                        # Cycle\
    \ detected\n                        cyc = [u]\n                        vis[u]\
    \ = 2\n                        while v != u:\n                            cyc.append(v)\n\
    \                            vis[v] = 2\n                            v = par[v]\n\
    \                        return cyc\n                    elif vis[u] == 0:\n \
    \                       par[u] = v\n                        stack.append((True,\
    \ u))\n            else:\n                vis[v] = 2\n        return None\n  \
    \  \n    def bridges(G):\n        tin = [-1] * G.N\n        low = [-1] * G.N\n\
    \        par = [-1] * G.N\n        vis = [0] * G.N\n        in_edge = [-1] * G.N\n\
    \n        Eid = G.edge_ids()\n        time = 0\n        bridges = []\n       \
    \ stack = list(range(G.N))\n        while stack:\n            v = stack.pop()\n\
    \            p = par[v]\n            match vis[v]:\n                case 0:\n\
    \                    vis[v] = 1\n                    tin[v] = low[v] = time\n\
    \                    time += 1\n                    stack.append(v)\n        \
    \            for i, child in enumerate(G.neighbors(v)):\n                    \
    \    if child == p:\n                            continue\n                  \
    \      match vis[child]:\n                            case 0:\n              \
    \                  # Tree edge - recurse\n                                par[child]\
    \ = v\n                                in_edge[child] = Eid[v][i]\n          \
    \                      stack.append(child)\n                            case 1:\n\
    \                                # Back edge - update low-link value\n       \
    \                         low[v] = min(low[v], tin[child])\n                case\
    \ 1:\n                    vis[v] = 2\n                    if p != -1:\n      \
    \                  low[p] = min(low[p], low[v])\n                        if low[v]\
    \ > tin[p]:\n                            bridges.append(in_edge[v])\n        \
    \        \n        return bridges\n\n    def articulation_points(G):\n       \
    \ \"\"\"\n        Find articulation points in an undirected graph using DFS events.\n\
    \        Returns a boolean list that is True for indices where the vertex is an\
    \ articulation point.\n        \"\"\"\n        N = G.N\n        order = [-1] *\
    \ N\n        low = [-1] * N\n        par = [-1] * N\n        state = [0] * N\n\
    \        children = [0] * N\n        ap = [False] * N\n        time = 0\n    \
    \    stack = list(range(N))\n\n        while stack:\n            v = stack.pop()\n\
    \            p = par[v]\n            if state[v] == 0:\n                state[v]\
    \ = 1\n                order[v] = low[v] = time\n                time += 1\n \
    \           \n                stack.append(v)\n                for child in G[v]:\n\
    \                    if order[child] == -1:\n                        par[child]\
    \ = v\n                        stack.append(child)\n                    elif child\
    \ != p:\n                        low[v] = min(low[v], order[child])\n        \
    \        if p != -1:\n                    children[p] += 1\n            elif state[v]\
    \ == 1:\n                state[v] = 2\n                ap[v] |= p == -1 and children[v]\
    \ > 1\n                if p != -1:\n                    low[p] = min(low[p], low[v])\n\
    \                    ap[p] |= par[p] != -1 and low[v] >= order[p]\n\n        return\
    \ ap\n    \n    def dfs_events(G, flags: DFSFlags, s: int|list|None = None, max_depth:\
    \ int|None = None):\n        match flags:\n            case DFSFlags.INTERVAL:\n\
    \                if max_depth is None:\n                    return G.dfs_enter_leave(s)\n\
    \            case DFSFlags.DOWN|DFSFlags.TOPDOWN:\n                if max_depth\
    \ is None:\n                    edges = G.dfs_topdown(s, DFSFlags.CONNECT_ROOTS\
    \ in flags)\n                    return [(DFSEvent.DOWN, p, u) for p,u in edges]\n\
    \            case DFSFlags.UP|DFSFlags.BOTTOMUP:\n                if max_depth\
    \ is None:\n                    edges = G.dfs_bottomup(s, DFSFlags.CONNECT_ROOTS\
    \ in flags)\n                    return [(DFSEvent.UP, p, u) for p,u in edges]\n\
    \            case flags if flags & DFSFlags.BACKTRACK:\n                return\
    \ G.dfs_backtrack(flags, s, max_depth)\n        state = [0] * G.N\n        child\
    \ = [0] * G.N\n        stack = [0] * G.N\n        if flags & DFSFlags.RETURN_PARENTS:\n\
    \            parents = [-1] * G.N\n        if flags & DFSFlags.RETURN_DEPTHS:\n\
    \            depths = [-1] * G.N\n\n        events = []\n        for s in G.starts(s):\n\
    \            stack[depth := 0] = s\n            if (DFSFlags.DOWN|DFSFlags.CONNECT_ROOTS)\
    \ in flags:\n                events.append((DFSEvent.DOWN,-1,s))\n           \
    \ while depth != -1:\n                u = stack[depth]\n                \n   \
    \             if not state[u]:\n                    state[u] = 1\n           \
    \         if flags & DFSFlags.ENTER:\n                        events.append((DFSEvent.ENTER,\
    \ u))\n                    if flags & DFSFlags.RETURN_DEPTHS:\n              \
    \          depths[u] = depth\n                \n                if (c := child[u])\
    \ < len(G[u]):\n                    child[u] += 1\n                    match state[v\
    \ := G[u][c]]:\n                        case 0:  # Unvisited\n               \
    \             if max_depth is None or depth <= max_depth:\n                  \
    \              if flags & DFSFlags.DOWN:\n                                   \
    \ events.append((DFSEvent.DOWN, u, v))\n                                stack[depth\
    \ := depth+1] = v\n                                if flags & DFSFlags.RETURN_PARENTS:\n\
    \                                    parents[v] = u\n                        case\
    \ 1:  # In progress\n                            if flags & DFSFlags.BACK:\n \
    \                               events.append((DFSEvent.BACK, u, v))\n       \
    \                 case 2:  # Completed\n                            if flags &\
    \ DFSFlags.CROSS:\n                                events.append((DFSEvent.CROSS,\
    \ u, v))\n                else:\n                    depth -= 1\n            \
    \        state[u] = 0 if DFSFlags.BACKTRACK in flags else 2\n                \
    \    if flags & DFSFlags.LEAVE:\n                        events.append((DFSEvent.LEAVE,\
    \ u))\n                    if depth != -1 and flags & DFSFlags.UP:\n         \
    \               events.append((DFSEvent.UP, stack[depth], u))\n            if\
    \ (DFSFlags.UP|DFSFlags.CONNECT_ROOTS) in flags:\n                events.append((DFSEvent.UP,-1,s))\n\
    \        ret = tuple((events,)) if DFSFlags.RETURN_ALL & flags else events\n \
    \       if DFSFlags.RETURN_PARENTS in flags:\n            ret += (parents,)\n\
    \        if DFSFlags.RETURN_DEPTHS in flags:\n            ret += (depths,)\n \
    \       return ret\n\n    def dfs_backtrack(G, flags: DFSFlags, s: int|list =\
    \ None, max_depth: int|None = None):\n        stack_depth = (max_depth+1 if max_depth\
    \ is not None else G.N)\n        stack = [0]*stack_depth\n        child = [0]*stack_depth\n\
    \        state = [0]*G.N\n        events: list[tuple[DFSEvent, int]|tuple[DFSEvent,\
    \ int, int]] = []\n\n        for s in G.starts(s):\n            if state[s]: continue\n\
    \            state[s] = 1\n            stack[depth := 0] = s\n            if DFSFlags.DOWN|DFSFlags.CONNECT_ROOTS\
    \ in flags:\n                events.append((DFSEvent.DOWN,-1,s))\n           \
    \ while depth != -1:\n                u = stack[depth]\n                if state[u]\
    \ == 1:\n                    state[u] = 2\n                    if DFSFlags.ENTER\
    \ in flags:\n                        events.append((DFSEvent.ENTER,u))\n     \
    \               if max_depth is not None and depth >= max_depth:\n           \
    \             child[depth] = len(G[u])\n                        if DFSFlags.MAXDEPTH\
    \ in flags:\n                            events.append((DFSEvent.MAXDEPTH,u))\n\
    \n                if (c := child[depth]) < len(G[u]):\n                    child[depth]\
    \ += 1\n                    if state[v := G[u][c]]:\n                        if\
    \ DFSFlags.BACK in flags:\n                            events.append((DFSEvent.BACK,u,v))\n\
    \                        continue\n                    state[v] = 1\n        \
    \            if DFSFlags.DOWN in flags:\n                        events.append((DFSEvent.DOWN,u,v))\n\
    \                    stack[depth := depth+1] = v\n                else:\n    \
    \                state[u] = 0\n                    if DFSFlags.LEAVE in flags:\n\
    \                        events.append((DFSEvent.LEAVE,u))\n                 \
    \   child[depth] = 0\n                    depth -= 1\n                    if depth\
    \ and DFSFlags.UP in flags:\n                        events.append((DFSEvent.UP,\
    \ stack[depth], u))\n            if DFSFlags.UP|DFSFlags.CONNECT_ROOTS in flags:\n\
    \                events.append((DFSEvent.UP,-1,s))\n        return events\n\n\
    \    def dfs_enter_leave(G, s: int|list|None = None):\n        state = [True]\
    \ * G.N\n        child: list[int] = elist(G.N)\n        stack: list[int] = elist(G.N)\n\
    \n        events = []\n        for s in G.starts(s):\n            stack.append(s)\n\
    \            child.append(0)\n            \n            while stack:\n       \
    \         u = stack[-1]\n                \n                if state[u]:\n    \
    \                state[u] = False\n                    events.append((DFSEvent.ENTER,\
    \ u))\n\n                \n                if (c := child[-1]) < len(G[u]):\n\
    \                    child[-1] += 1\n                    if state[v := G[u][c]]:\n\
    \                        stack.append(v)\n                        child.append(0)\n\
    \                else:\n                    stack.pop()\n                    child.pop()\n\
    \                    events.append((DFSEvent.LEAVE, u))\n\n        return events\n\
    \    \n    def dfs_topdown(G, s: int|list[int]|None = None, connect_roots = False):\n\
    \        '''Returns list of (u,v) representing u->v edges in order of top down\
    \ discovery'''\n        stack: list[int] = elist(G.N)\n        vis = [False]*G.N\n\
    \        edges: list[tuple[int,int]] = elist(G.N)\n\n        for s in G.starts(s):\n\
    \            if vis[s]: continue\n            if connect_roots:\n            \
    \    edges.append((-1,s))\n            vis[s] = True\n            stack.append(s)\n\
    \            while stack:\n                u = stack.pop()\n                for\
    \ v in G[u]:\n                    if vis[v]: continue\n                    vis[v]\
    \ = True\n                    edges.append((u,v))\n                    stack.append(v)\n\
    \        return edges\n    \n    def dfs_bottomup(G, s: int|list[int]|None = None,\
    \ connect_roots = False):\n        '''Returns list of (p,u) representing p->u\
    \ edges in bottom up order'''\n        edges = G.dfs_topdown(s, connect_roots)\n\
    \        edges.reverse()\n        return edges\n    \n    def starts(G, v: int|list[int]|None)\
    \ -> Iterable:\n        match v:\n            case int(v): return (v,)\n     \
    \       case None: return range(G.N)\n            case V: return V\n\n    @classmethod\n\
    \    def compile(cls, N: int, M: int, E):\n        edge = Parser.compile(E)\n\
    \        def parse(ts: TokenStream):\n            return cls(N, [edge(ts) for\
    \ _ in range(M)])\n        return parse\n    \n\nclass GraphWeightedProtocol(GraphProtocol):\n\
    \n    def neighbors(G, v: int):\n        return map(operator.itemgetter(0), G[v])\n\
    \    \n    @overload\n    def distance(G) -> list[list[int]]: ...\n    @overload\n\
    \    def distance(G, s: int = 0) -> list[int]: ...\n    @overload\n    def distance(G,\
    \ s: int, g: int) -> int: ...\n    def distance(G, s = None, g = None):\n    \
    \    match s, g:\n            case None, None:\n                return G.floyd_warshall()\n\
    \            case s, None:\n                return G.dijkstra(s)\n           \
    \ case s, g:\n                return G.dijkstra(s, g)\n    \n    def dijkstra(G,\
    \ s = 0, g = None):\n        D = [inft for _ in range(G.N)]\n        D[s] = 0\n\
    \        q = [(0, s)]\n        while q:\n            d, v = heappop(q)\n     \
    \       if d > D[v]: continue\n            if v == g: return d\n            for\
    \ u, w, *_ in G[v]:\n                if (nd := d + w) < D[u]:\n              \
    \      D[u] = nd\n                    heappush(q, (nd, u))\n        return D if\
    \ g is None else inft\n    \n    @overload\n    def shortest_path(G, s: int, g:\
    \ int) -> list[int]|None: ...\n    @overload\n    def shortest_path(G, s: int,\
    \ g: int, distances = True) -> tuple[list[int]|None,list[int]]: ...\n    def shortest_path(G,\
    \ s: int, g: int, distances = False):\n        D = [inft] * G.N\n        D[s]\
    \ = 0\n        if s == g:\n            return ([], D) if distances else []\n \
    \           \n        par = [-1] * G.N\n        par_edge = [-1] * G.N\n      \
    \  Eid = G.edge_ids()\n        q = [(0, s)]\n        que = PriorityQueue(G.N)\n\
    \        \n        while q:\n            d, v = heappop(q)\n            if d >\
    \ D[v]: continue\n            if v == g: break\n                \n           \
    \ for (u, w, *_), eid in zip(G[v], Eid[v]):\n                if (nd := d + w)\
    \ < D[u]:\n                    D[u] = nd\n                    par[u] = v\n   \
    \                 par_edge[u] = eid\n                    heappush(q, (nd, u))\n\
    \        \n        if D[g] == inft:\n            return (None, D) if distances\
    \ else None\n            \n        path = []\n        current = g\n        while\
    \ current != s:\n            path.append(par_edge[current])\n            current\
    \ = par[current]\n            \n        return (path[::-1], D) if distances else\
    \ path[::-1]\n    \n    def kruskal(G):\n        E, N = G.E, G.N\n        heapify(E)\n\
    \        dsu = DSU(N)\n        MST = []\n        need = N-1\n        while E and\
    \ need:\n            edge = heappop(E)\n            u,v,*_ = edge\n          \
    \  u,v = dsu.merge(u,v,True)\n            if u != v:\n                MST.append(edge)\n\
    \                need -= 1\n        return MST\n    \n    def bellman_ford(G,\
    \ s = 0) -> list[int]:\n        D = [inft]*G.N\n        D[s] = 0\n        for\
    \ _ in range(G.N-1):\n            for u, edges in enumerate(G):\n            \
    \    for v,w,*_ in edges:\n                    D[v] = min(D[v], D[u] + w)\n  \
    \      return D\n    \n    def floyd_warshall(G) -> list[list[int]]:\n       \
    \ D = [[inft]*G.N for _ in range(G.N)]\n\n        for u, edges in enumerate(G):\n\
    \            D[u][u] = 0\n            for v,w in edges:\n                D[u][v]\
    \ = min(D[u][v], w)\n        \n        for k, Dk in enumerate(D):\n          \
    \  for Di in D:\n                for j in range(G.N):\n                    Di[j]\
    \ = min(Di[j], Di[k]+Dk[j])\n        return D\n    \n    def dfs_events(G, flags:\
    \ DFSFlags, s: int|list|None = None, max_depth: int|None = None):\n        match\
    \ flags:\n            case DFSFlags.INTERVAL:\n                if max_depth is\
    \ None:\n                    return G.dfs_enter_leave(s)\n            case DFSFlags.DOWN|DFSFlags.TOPDOWN:\n\
    \                if max_depth is None:\n                    edges = G.dfs_topdown(s,\
    \ DFSFlags.CONNECT_ROOTS in flags)\n                    return [(DFSEvent.DOWN,\
    \ p, u) for p,u in edges]\n            case DFSFlags.UP|DFSFlags.BOTTOMUP:\n \
    \               if max_depth is None:\n                    edges = G.dfs_bottomup(s,\
    \ DFSFlags.CONNECT_ROOTS in flags)\n                    return [(DFSEvent.UP,\
    \ p, u) for p,u in edges]\n            case flags if flags & DFSFlags.BACKTRACK:\n\
    \                return G.dfs_backtrack(flags, s, max_depth)\n        state =\
    \ [0] * G.N\n        child = elist(G.N)\n        weights = elist(G.N)\n      \
    \  stack = elist(G.N)\n        if flags & DFSFlags.RETURN_PARENTS:\n         \
    \   parents = [-1] * G.N\n        if flags & DFSFlags.RETURN_DEPTHS:\n       \
    \     depths = [-1] * G.N\n\n        events = []\n        for s in G.starts(s):\n\
    \            stack.append(s)\n            child.append(0)\n            if (DFSFlags.DOWN|DFSFlags.CONNECT_ROOTS)\
    \ in flags:\n                events.append((DFSEvent.DOWN,-1,s,-1))\n        \
    \    while stack:\n                u = stack[-1]\n                \n         \
    \       if not state[u]:\n                    state[u] = 1\n                 \
    \   if flags & DFSFlags.ENTER:\n                        events.append((DFSEvent.ENTER,\
    \ u))\n                    if flags & DFSFlags.RETURN_DEPTHS:\n              \
    \          depths[u] = len(stack)-1\n                \n                if (c :=\
    \ child[-1]) < len(G[u]):\n                    child[-1] += 1\n              \
    \      v, w = G[u][c]\n                    match state[v]:\n                 \
    \       case 0:  # Unvisited\n                            if max_depth is None\
    \ or len(stack)-1 <= max_depth:\n                                if flags & DFSFlags.DOWN:\n\
    \                                    events.append((DFSEvent.DOWN, u, v, w))\n\
    \                                stack.append(v)\n                           \
    \     weights.append(w)\n                                child.append(0)\n   \
    \                             if flags & DFSFlags.RETURN_PARENTS:\n          \
    \                          parents[v] = u\n                        case 1:  #\
    \ In progress\n                            if flags & DFSFlags.BACK:\n       \
    \                         events.append((DFSEvent.BACK, u, v, w))\n          \
    \              case 2:  # Completed\n                            if flags & DFSFlags.CROSS:\n\
    \                                events.append((DFSEvent.CROSS, u, v, w))\n  \
    \              else:\n                    stack.pop()\n                    child.pop()\n\
    \                    state[u] = 0 if DFSFlags.BACKTRACK in flags else 2\n    \
    \                if flags & DFSFlags.LEAVE:\n                        events.append((DFSEvent.LEAVE,\
    \ u))\n                    if stack and flags & DFSFlags.UP:\n               \
    \         pw = weights.pop()\n                        events.append((DFSEvent.UP,\
    \ stack[-1], u, pw))\n            if (DFSFlags.UP|DFSFlags.CONNECT_ROOTS) in flags:\n\
    \                events.append((DFSEvent.UP,-1,s,-1))\n        ret = tuple((events,))\
    \ if DFSFlags.RETURN_ALL & flags else events\n        if DFSFlags.RETURN_PARENTS\
    \ in flags:\n            ret += (parents,)\n        if DFSFlags.RETURN_DEPTHS\
    \ in flags:\n            ret += (depths,)\n        return ret\n\n    def dfs_backtrack(G,\
    \ flags: DFSFlags, s: int|list = None, max_depth: int|None = None):\n        stack_depth\
    \ = (max_depth+1 if max_depth is not None else G.N)\n        stack = elist(stack_depth)\n\
    \        child = elist(stack_depth)\n        weights = elist(stack_depth)\n  \
    \      state = [0]*G.N\n        events: list[tuple[DFSEvent, int]|tuple[DFSEvent,\
    \ int, int]] = []\n\n        for s in G.starts(s):\n            if state[s]: continue\n\
    \            state[s] = 1\n            stack.append(s)\n            child.append(0)\n\
    \            if DFSFlags.DOWN|DFSFlags.CONNECT_ROOTS in flags:\n             \
    \   events.append((DFSEvent.DOWN,-1,s,-1))\n            while stack:\n       \
    \         u = stack[-1]\n                if state[u] == 1:\n                 \
    \   state[u] = 2\n                    if DFSFlags.ENTER in flags:\n          \
    \              events.append((DFSEvent.ENTER,u))\n                    if max_depth\
    \ is not None and len(stack) > max_depth:\n                        child[-1] =\
    \ len(G[u])\n                        if DFSFlags.MAXDEPTH in flags:\n        \
    \                    events.append((DFSEvent.MAXDEPTH,u))\n\n                if\
    \ (c := child[-1]) < len(G[u]):\n                    child[-1] += 1\n        \
    \            v, w = G[u][c]\n                    if state[v]:\n              \
    \          if DFSFlags.BACK in flags:\n                            events.append((DFSEvent.BACK,u,v,w))\n\
    \                        continue\n                    state[v] = 1\n        \
    \            if DFSFlags.DOWN in flags:\n                        events.append((DFSEvent.DOWN,u,v,w))\n\
    \                    stack.append(v)\n                    child.append(0)\n  \
    \                  weights.append(w)\n                else:\n                \
    \    state[u] = 0\n                    if DFSFlags.LEAVE in flags:\n         \
    \               events.append((DFSEvent.LEAVE,u))\n                    stack.pop()\n\
    \                    child.pop()\n                    if stack and DFSFlags.UP\
    \ in flags:\n                        pw = weights.pop()\n                    \
    \    events.append((DFSEvent.UP, stack[-1], u, pw))\n                    \n  \
    \          if DFSFlags.UP|DFSFlags.CONNECT_ROOTS in flags:\n                events.append((DFSEvent.UP,-1,s,-1))\n\
    \        return events\n    \n    def dfs_topdown(G, s: int|list[int]|None = None,\
    \ connect_roots = False):\n        '''Returns list of (u,v) representing u->v\
    \ edges in order of top down discovery'''\n        stack: list[int] = elist(G.N)\n\
    \        vis = [False]*G.N\n        edges: list[tuple[int,int]] = elist(G.N)\n\
    \n        for s in G.starts(s):\n            if vis[s]: continue\n           \
    \ if connect_roots:\n                edges.append((-1,s,-1))\n            vis[s]\
    \ = True\n            stack.append(s)\n            while stack:\n            \
    \    u = stack.pop()\n                for v,w in G[u]:\n                    if\
    \ vis[v]: continue\n                    vis[v] = True\n                    edges.append((u,v,w))\n\
    \                    stack.append(v)\n        return edges\n\n\nclass DSU:\n \
    \   def __init__(self, n):\n        self.n = n\n        self.par = [-1] * n\n\n\
    \    def merge(self, u, v, src = False):\n        assert 0 <= u < self.n\n   \
    \     assert 0 <= v < self.n\n\n        x, y = self.leader(u), self.leader(v)\n\
    \        if x == y: return (x,y) if src else x\n\n        if -self.par[x] < -self.par[y]:\n\
    \            x, y = y, x\n\n        self.par[x] += self.par[y]\n        self.par[y]\
    \ = x\n\n        return (x,y) if src else x\n\n    def same(self, u: int, v: int):\n\
    \        assert 0 <= u < self.n\n        assert 0 <= v < self.n\n        return\
    \ self.leader(u) == self.leader(v)\n\n    def leader(self, i) -> int:\n      \
    \  assert 0 <= i < self.n\n\n        p = self.par[i]\n        while p >= 0:\n\
    \            if self.par[p] < 0:\n                return p\n            self.par[i],\
    \ i, p = self.par[p], self.par[p], self.par[self.par[p]]\n\n        return i\n\
    \n    def size(self, i) -> int:\n        assert 0 <= i < self.n\n        \n  \
    \      return -self.par[self.leader(i)]\n\n    def groups(self) -> list[list[int]]:\n\
    \        leader_buf = [self.leader(i) for i in range(self.n)]\n\n        result\
    \ = [[] for _ in range(self.n)]\n        for i in range(self.n):\n           \
    \ result[leader_buf[i]].append(i)\n\n        return list(filter(lambda r: r, result))\n\
    \nfrom collections import UserList\nfrom heapq import heapify, heappop, heappush,\
    \ heappushpop, heapreplace\nfrom typing import Generic, TypeVar\n\nT = TypeVar('T')\n\
    class HeapProtocol(Generic[T]):\n    def pop(self) -> T: ...\n    def push(self,\
    \ item: T): ...\n    def pushpop(self, item: T) -> T: ...\n    def replace(self,\
    \ item: T) -> T: ...\n\nclass PriorityQueue(HeapProtocol[int], UserList[int]):\n\
    \    \n    def __init__(self, N: int, ids: Iterable[int] = None, priorities: Iterable[int]\
    \ = None, /):\n        self.shift = N.bit_length()\n        self.mask = (1 <<\
    \ self.shift)-1\n        if ids is None:\n            super().__init__()\n   \
    \     elif priorities is None:\n            self.data = ids\n            heapify(self.data)\n\
    \        else:\n            self.data = [self.encode(id, priority) for id, priority\
    \ in zip(ids, priorities)]\n            heapify(self.data)\n\n    def encode(self,\
    \ id, priority):\n        return priority << self.shift | id\n    \n    def decode(self,\
    \ encoded):\n        return self.mask & encoded, encoded >> self.shift\n    \n\
    \    def pop(self):\n        return self.decode(heappop(self.data))\n    \n  \
    \  def push(self, id: int, priority: int):\n        heappush(self.data, self.encode(id,\
    \ priority))\n\n    def pushpop(self, id: int, priority: int):\n        return\
    \ self.decode(heappushpop(self.data, self.encode(id, priority)))\n    \n    def\
    \ replace(self, id: int, priority: int):\n        return self.decode(heapreplace(self.data,\
    \ self.encode(id, priority)))\n\n"
  code: "import cp_library.alg.graph.__header__\n\nfrom typing import overload\nfrom\
    \ heapq import heapify, heappop, heappush\nimport operator\n\nfrom cp_library.alg.graph.dfs_options_cls\
    \ import DFSEvent, DFSFlags\nfrom cp_library.alg.graph.graph_proto import GraphProtocol\n\
    \nclass GraphWeightedProtocol(GraphProtocol):\n\n    def neighbors(G, v: int):\n\
    \        return map(operator.itemgetter(0), G[v])\n    \n    @overload\n    def\
    \ distance(G) -> list[list[int]]: ...\n    @overload\n    def distance(G, s: int\
    \ = 0) -> list[int]: ...\n    @overload\n    def distance(G, s: int, g: int) ->\
    \ int: ...\n    def distance(G, s = None, g = None):\n        match s, g:\n  \
    \          case None, None:\n                return G.floyd_warshall()\n     \
    \       case s, None:\n                return G.dijkstra(s)\n            case\
    \ s, g:\n                return G.dijkstra(s, g)\n    \n    def dijkstra(G, s\
    \ = 0, g = None):\n        D = [inft for _ in range(G.N)]\n        D[s] = 0\n\
    \        q = [(0, s)]\n        while q:\n            d, v = heappop(q)\n     \
    \       if d > D[v]: continue\n            if v == g: return d\n            for\
    \ u, w, *_ in G[v]:\n                if (nd := d + w) < D[u]:\n              \
    \      D[u] = nd\n                    heappush(q, (nd, u))\n        return D if\
    \ g is None else inft\n    \n    @overload\n    def shortest_path(G, s: int, g:\
    \ int) -> list[int]|None: ...\n    @overload\n    def shortest_path(G, s: int,\
    \ g: int, distances = True) -> tuple[list[int]|None,list[int]]: ...\n    def shortest_path(G,\
    \ s: int, g: int, distances = False):\n        D = [inft] * G.N\n        D[s]\
    \ = 0\n        if s == g:\n            return ([], D) if distances else []\n \
    \           \n        par = [-1] * G.N\n        par_edge = [-1] * G.N\n      \
    \  Eid = G.edge_ids()\n        q = [(0, s)]\n        que = PriorityQueue(G.N)\n\
    \        \n        while q:\n            d, v = heappop(q)\n            if d >\
    \ D[v]: continue\n            if v == g: break\n                \n           \
    \ for (u, w, *_), eid in zip(G[v], Eid[v]):\n                if (nd := d + w)\
    \ < D[u]:\n                    D[u] = nd\n                    par[u] = v\n   \
    \                 par_edge[u] = eid\n                    heappush(q, (nd, u))\n\
    \        \n        if D[g] == inft:\n            return (None, D) if distances\
    \ else None\n            \n        path = []\n        current = g\n        while\
    \ current != s:\n            path.append(par_edge[current])\n            current\
    \ = par[current]\n            \n        return (path[::-1], D) if distances else\
    \ path[::-1]\n    \n    def kruskal(G):\n        E, N = G.E, G.N\n        heapify(E)\n\
    \        dsu = DSU(N)\n        MST = []\n        need = N-1\n        while E and\
    \ need:\n            edge = heappop(E)\n            u,v,*_ = edge\n          \
    \  u,v = dsu.merge(u,v,True)\n            if u != v:\n                MST.append(edge)\n\
    \                need -= 1\n        return MST\n    \n    def bellman_ford(G,\
    \ s = 0) -> list[int]:\n        D = [inft]*G.N\n        D[s] = 0\n        for\
    \ _ in range(G.N-1):\n            for u, edges in enumerate(G):\n            \
    \    for v,w,*_ in edges:\n                    D[v] = min(D[v], D[u] + w)\n  \
    \      return D\n    \n    def floyd_warshall(G) -> list[list[int]]:\n       \
    \ D = [[inft]*G.N for _ in range(G.N)]\n\n        for u, edges in enumerate(G):\n\
    \            D[u][u] = 0\n            for v,w in edges:\n                D[u][v]\
    \ = min(D[u][v], w)\n        \n        for k, Dk in enumerate(D):\n          \
    \  for Di in D:\n                for j in range(G.N):\n                    Di[j]\
    \ = min(Di[j], Di[k]+Dk[j])\n        return D\n    \n    def dfs_events(G, flags:\
    \ DFSFlags, s: int|list|None = None, max_depth: int|None = None):\n        match\
    \ flags:\n            case DFSFlags.INTERVAL:\n                if max_depth is\
    \ None:\n                    return G.dfs_enter_leave(s)\n            case DFSFlags.DOWN|DFSFlags.TOPDOWN:\n\
    \                if max_depth is None:\n                    edges = G.dfs_topdown(s,\
    \ DFSFlags.CONNECT_ROOTS in flags)\n                    return [(DFSEvent.DOWN,\
    \ p, u) for p,u in edges]\n            case DFSFlags.UP|DFSFlags.BOTTOMUP:\n \
    \               if max_depth is None:\n                    edges = G.dfs_bottomup(s,\
    \ DFSFlags.CONNECT_ROOTS in flags)\n                    return [(DFSEvent.UP,\
    \ p, u) for p,u in edges]\n            case flags if flags & DFSFlags.BACKTRACK:\n\
    \                return G.dfs_backtrack(flags, s, max_depth)\n        state =\
    \ [0] * G.N\n        child = elist(G.N)\n        weights = elist(G.N)\n      \
    \  stack = elist(G.N)\n        if flags & DFSFlags.RETURN_PARENTS:\n         \
    \   parents = [-1] * G.N\n        if flags & DFSFlags.RETURN_DEPTHS:\n       \
    \     depths = [-1] * G.N\n\n        events = []\n        for s in G.starts(s):\n\
    \            stack.append(s)\n            child.append(0)\n            if (DFSFlags.DOWN|DFSFlags.CONNECT_ROOTS)\
    \ in flags:\n                events.append((DFSEvent.DOWN,-1,s,-1))\n        \
    \    while stack:\n                u = stack[-1]\n                \n         \
    \       if not state[u]:\n                    state[u] = 1\n                 \
    \   if flags & DFSFlags.ENTER:\n                        events.append((DFSEvent.ENTER,\
    \ u))\n                    if flags & DFSFlags.RETURN_DEPTHS:\n              \
    \          depths[u] = len(stack)-1\n                \n                if (c :=\
    \ child[-1]) < len(G[u]):\n                    child[-1] += 1\n              \
    \      v, w = G[u][c]\n                    match state[v]:\n                 \
    \       case 0:  # Unvisited\n                            if max_depth is None\
    \ or len(stack)-1 <= max_depth:\n                                if flags & DFSFlags.DOWN:\n\
    \                                    events.append((DFSEvent.DOWN, u, v, w))\n\
    \                                stack.append(v)\n                           \
    \     weights.append(w)\n                                child.append(0)\n   \
    \                             if flags & DFSFlags.RETURN_PARENTS:\n          \
    \                          parents[v] = u\n                        case 1:  #\
    \ In progress\n                            if flags & DFSFlags.BACK:\n       \
    \                         events.append((DFSEvent.BACK, u, v, w))\n          \
    \              case 2:  # Completed\n                            if flags & DFSFlags.CROSS:\n\
    \                                events.append((DFSEvent.CROSS, u, v, w))\n  \
    \              else:\n                    stack.pop()\n                    child.pop()\n\
    \                    state[u] = 0 if DFSFlags.BACKTRACK in flags else 2\n    \
    \                if flags & DFSFlags.LEAVE:\n                        events.append((DFSEvent.LEAVE,\
    \ u))\n                    if stack and flags & DFSFlags.UP:\n               \
    \         pw = weights.pop()\n                        events.append((DFSEvent.UP,\
    \ stack[-1], u, pw))\n            if (DFSFlags.UP|DFSFlags.CONNECT_ROOTS) in flags:\n\
    \                events.append((DFSEvent.UP,-1,s,-1))\n        ret = tuple((events,))\
    \ if DFSFlags.RETURN_ALL & flags else events\n        if DFSFlags.RETURN_PARENTS\
    \ in flags:\n            ret += (parents,)\n        if DFSFlags.RETURN_DEPTHS\
    \ in flags:\n            ret += (depths,)\n        return ret\n\n    def dfs_backtrack(G,\
    \ flags: DFSFlags, s: int|list = None, max_depth: int|None = None):\n        stack_depth\
    \ = (max_depth+1 if max_depth is not None else G.N)\n        stack = elist(stack_depth)\n\
    \        child = elist(stack_depth)\n        weights = elist(stack_depth)\n  \
    \      state = [0]*G.N\n        events: list[tuple[DFSEvent, int]|tuple[DFSEvent,\
    \ int, int]] = []\n\n        for s in G.starts(s):\n            if state[s]: continue\n\
    \            state[s] = 1\n            stack.append(s)\n            child.append(0)\n\
    \            if DFSFlags.DOWN|DFSFlags.CONNECT_ROOTS in flags:\n             \
    \   events.append((DFSEvent.DOWN,-1,s,-1))\n            while stack:\n       \
    \         u = stack[-1]\n                if state[u] == 1:\n                 \
    \   state[u] = 2\n                    if DFSFlags.ENTER in flags:\n          \
    \              events.append((DFSEvent.ENTER,u))\n                    if max_depth\
    \ is not None and len(stack) > max_depth:\n                        child[-1] =\
    \ len(G[u])\n                        if DFSFlags.MAXDEPTH in flags:\n        \
    \                    events.append((DFSEvent.MAXDEPTH,u))\n\n                if\
    \ (c := child[-1]) < len(G[u]):\n                    child[-1] += 1\n        \
    \            v, w = G[u][c]\n                    if state[v]:\n              \
    \          if DFSFlags.BACK in flags:\n                            events.append((DFSEvent.BACK,u,v,w))\n\
    \                        continue\n                    state[v] = 1\n        \
    \            if DFSFlags.DOWN in flags:\n                        events.append((DFSEvent.DOWN,u,v,w))\n\
    \                    stack.append(v)\n                    child.append(0)\n  \
    \                  weights.append(w)\n                else:\n                \
    \    state[u] = 0\n                    if DFSFlags.LEAVE in flags:\n         \
    \               events.append((DFSEvent.LEAVE,u))\n                    stack.pop()\n\
    \                    child.pop()\n                    if stack and DFSFlags.UP\
    \ in flags:\n                        pw = weights.pop()\n                    \
    \    events.append((DFSEvent.UP, stack[-1], u, pw))\n                    \n  \
    \          if DFSFlags.UP|DFSFlags.CONNECT_ROOTS in flags:\n                events.append((DFSEvent.UP,-1,s,-1))\n\
    \        return events\n    \n    def dfs_topdown(G, s: int|list[int]|None = None,\
    \ connect_roots = False):\n        '''Returns list of (u,v) representing u->v\
    \ edges in order of top down discovery'''\n        stack: list[int] = elist(G.N)\n\
    \        vis = [False]*G.N\n        edges: list[tuple[int,int]] = elist(G.N)\n\
    \n        for s in G.starts(s):\n            if vis[s]: continue\n           \
    \ if connect_roots:\n                edges.append((-1,s,-1))\n            vis[s]\
    \ = True\n            stack.append(s)\n            while stack:\n            \
    \    u = stack.pop()\n                for v,w in G[u]:\n                    if\
    \ vis[v]: continue\n                    vis[v] = True\n                    edges.append((u,v,w))\n\
    \                    stack.append(v)\n        return edges\n\nfrom cp_library.ds.dsu_cls\
    \ import DSU\nfrom cp_library.ds.priority_queue_cls import PriorityQueue\nfrom\
    \ cp_library.ds.elist_fn import elist\nfrom cp_library.math.inft_cnst import inft"
  dependsOn:
  - cp_library/alg/graph/dfs_options_cls.py
  - cp_library/alg/graph/graph_proto.py
  - cp_library/ds/dsu_cls.py
  - cp_library/ds/priority_queue_cls.py
  - cp_library/ds/elist_fn.py
  - cp_library/math/inft_cnst.py
  - cp_library/io/parser_cls.py
  - cp_library/ds/heap_proto.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: false
  path: cp_library/alg/graph/graph_weighted_proto.py
  requiredBy:
  - cp_library/alg/graph/graph_weighted_cls.py
  - cp_library/alg/graph/digraph_weighted_cls.py
  - cp_library/alg/tree/tree_weighted_proto.py
  - cp_library/alg/tree/tree_weighted_cls.py
  timestamp: '2024-11-28 18:07:28+09:00'
  verificationStatus: LIBRARY_SOME_WA
  verifiedWith:
  - test/abc375_g_find_bridges.test.py
  - test/shortest_path_min_heap.test.py
  - test/grl_1_b_bellman_ford.test.py
  - test/grl_1_a_graph_distance.test.py
  - test/grl_1_b_graph_bellman_ford.test.py
  - test/shortest_path_graph_weighted.test.py
  - test/grl_1_c_floyd_warshall.test.py
  - test/abc361_e_tree_diameter.test.py
  - test/abc218_f_shortest_path_weighted.test.py
  - test/grl_2_a_graph_kruskal.test.py
  - test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
  - test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
  - test/grl_1_a_dijkstra.test.py
documentation_of: cp_library/alg/graph/graph_weighted_proto.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/graph_weighted_proto.py
- /library/cp_library/alg/graph/graph_weighted_proto.py.html
title: cp_library/alg/graph/graph_weighted_proto.py
---