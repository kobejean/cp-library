---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: cp_library/alg/graph/dfs_options_cls.py
    title: cp_library/alg/graph/dfs_options_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/edge_cls.py
    title: cp_library/alg/graph/edge_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/graph_proto.py
    title: cp_library/alg/graph/graph_proto.py
  - icon: ':warning:'
    path: cp_library/alg/graph/graph_set_cls.py
    title: cp_library/alg/graph/graph_set_cls.py
  - icon: ':warning:'
    path: cp_library/alg/iter/presum_fn.py
    title: cp_library/alg/iter/presum_fn.py
  - icon: ':warning:'
    path: cp_library/alg/tree/lca_table_iterative_cls.py
    title: cp_library/alg/tree/lca_table_iterative_cls.py
  - icon: ':warning:'
    path: cp_library/alg/tree/tree_proto.py
    title: cp_library/alg/tree/tree_proto.py
  - icon: ':warning:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  - icon: ':warning:'
    path: cp_library/ds/sparse_table_cls.py
    title: cp_library/ds/sparse_table_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':warning:'
    path: cp_library/math/inft_cnst.py
    title: cp_library/math/inft_cnst.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \n\n\nimport typing\nfrom collections import deque\nfrom numbers import Number\n\
    from types import GenericAlias \nfrom typing import Callable, Collection, Iterator,\
    \ TypeVar, Union\nimport os\nimport sys\nfrom io import BytesIO, IOBase\n\n\n\
    class FastIO(IOBase):\n    BUFSIZE = 8192\n    newlines = 0\n\n    def __init__(self,\
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
    \ TokenStream):\n            return cls(next(ts))\n        return parser\n\nclass\
    \ Edge(tuple, Parsable):\n    @classmethod\n    def compile(cls, I=-1):\n    \
    \    def parse(ts: TokenStream):\n            u,v = ts.line()\n            return\
    \ cls((int(u)+I,int(v)+I))\n        return parse\n\n\nfrom enum import auto, IntFlag,\
    \ IntEnum\n\nclass DFSFlags(IntFlag):\n    ENTER = auto()\n    DOWN = auto()\n\
    \    BACK = auto()\n    CROSS = auto()\n    LEAVE = auto()\n    UP = auto()\n\
    \    MAXDEPTH = auto()\n\n    RETURN_PARENTS = auto()\n    RETURN_DEPTHS = auto()\n\
    \    BACKTRACK = auto()\n    CONNECT_ROOTS = auto()\n\n    # Common combinations\n\
    \    ALL_EDGES = DOWN | BACK | CROSS\n    EULER_TOUR = DOWN | UP\n    INTERVAL\
    \ = ENTER | LEAVE\n    TOPDOWN = DOWN | CONNECT_ROOTS\n    BOTTOMUP = UP | CONNECT_ROOTS\n\
    \    RETURN_ALL = RETURN_PARENTS | RETURN_DEPTHS\n\nclass DFSEvent(IntEnum):\n\
    \    ENTER = DFSFlags.ENTER \n    DOWN = DFSFlags.DOWN \n    BACK = DFSFlags.BACK\
    \ \n    CROSS = DFSFlags.CROSS \n    LEAVE = DFSFlags.LEAVE \n    UP = DFSFlags.UP\
    \ \n    MAXDEPTH = DFSFlags.MAXDEPTH\n    \n\n\ndef elist(est_len: int) -> list:\
    \ ...\ntry:\n    from __pypy__ import newlist_hint\nexcept:\n    def newlist_hint(hint):\n\
    \        return []\nelist = newlist_hint\n    \nfrom typing import Iterable, overload\n\
    \ninft: int\n\ninft = sys.maxsize\n\nclass GraphProtocol(list, Parsable):\n  \
    \  def __init__(G, N: int, E: list = None, adj: Iterable = None):\n        G.N\
    \ = N\n        if E is not None:\n            G.M, G.E = len(E), E\n        if\
    \ adj is not None:\n            super().__init__(adj)\n\n    def neighbors(G,\
    \ v: int) -> Iterable[int]:\n        return G[v]\n    \n    def edge_ids(G) ->\
    \ list[list[int]]: ...\n\n    @overload\n    def distance(G) -> list[list[int]]:\
    \ ...\n    @overload\n    def distance(G, s: int = 0) -> list[int]: ...\n    @overload\n\
    \    def distance(G, s: int, g: int) -> int: ...\n    def distance(G, s = None,\
    \ g = None):\n        match s, g:\n            case None, None:\n            \
    \    return G.floyd_warshall()\n            case s, None:\n                return\
    \ G.bfs(s)\n            case s, g:\n                return G.bfs(s, g)\n\n   \
    \ @overload\n    def bfs(G, s: int|list = 0) -> list[int]: ...\n    @overload\n\
    \    def bfs(G, s: int|list, g: int) -> int: ...\n    def bfs(G, s = 0, g = None):\n\
    \        D = [inft for _ in range(G.N)]\n        q = deque([s] if isinstance(s,\
    \ int) else s)\n        for u in q: D[u] = 0\n        while q:\n            nd\
    \ = D[u := q.popleft()]+1\n            if u == g: return D[u]\n            for\
    \ v in G.neighbors(u):\n                if nd < D[v]:\n                    D[v]\
    \ = nd\n                    q.append(v)\n        return D if g is None else inft\
    \ \n\n    @overload\n    def shortest_path(G, s: int, g: int) -> list[int]|None:\
    \ ...\n    @overload\n    def shortest_path(G, s: int, g: int, distances = True)\
    \ -> tuple[list[int]|None,list[int]]: ...\n    def shortest_path(G, s: int, g:\
    \ int, distances = False) -> list[int]:\n        D = [inft] * G.N\n        D[s]\
    \ = 0\n        if s == g:\n            return ([], D) if distances else []\n \
    \           \n        par = [-1] * G.N\n        par_edge = [-1] * G.N\n      \
    \  Eid = G.edge_ids()\n        q = deque([s])\n        \n        while q:\n  \
    \          nd = D[u := q.popleft()] + 1\n            if u == g: break\n      \
    \          \n            for v, eid in zip(G[u], Eid[u]):\n                if\
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
    \ Di in D:\n                if Di[k] == inft: continue\n                for j\
    \ in range(G.N):\n                    if Dk[j] == inft: continue\n           \
    \         Di[j] = min(Di[j], Di[k]+Dk[j])\n        return D\n    \n    \n    def\
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
    \        \"\"\"\n        Find articulation points in an undirected graph using\
    \ DFS events.\n        Returns a boolean list that is True for indices where the\
    \ vertex is an articulation point.\n        \"\"\"\n        N = G.N\n        order\
    \ = [-1] * N\n        low = [-1] * N\n        par = [-1] * N\n        state =\
    \ [0] * N\n        children = [0] * N\n        ap = [False] * N\n        time\
    \ = 0\n        stack = list(range(N))\n\n        while stack:\n            v =\
    \ stack.pop()\n            p = par[v]\n            if state[v] == 0:\n       \
    \         state[v] = 1\n                order[v] = low[v] = time\n           \
    \     time += 1\n            \n                stack.append(v)\n             \
    \   for child in G[v]:\n                    if order[child] == -1:\n         \
    \               par[child] = v\n                        stack.append(child)\n\
    \                    elif child != p:\n                        low[v] = min(low[v],\
    \ order[child])\n                if p != -1:\n                    children[p]\
    \ += 1\n            elif state[v] == 1:\n                state[v] = 2\n      \
    \          ap[v] |= p == -1 and children[v] > 1\n                if p != -1:\n\
    \                    low[p] = min(low[p], low[v])\n                    ap[p] |=\
    \ par[p] != -1 and low[v] >= order[p]\n\n        return ap\n    \n    def dfs_events(G,\
    \ flags: DFSFlags, s: int|list|None = None, max_depth: int|None = None):\n   \
    \     match flags:\n            case DFSFlags.INTERVAL:\n                if max_depth\
    \ is None:\n                    return G.dfs_enter_leave(s)\n            case\
    \ DFSFlags.DOWN|DFSFlags.TOPDOWN:\n                if max_depth is None:\n   \
    \                 edges = G.dfs_topdown(s, DFSFlags.CONNECT_ROOTS in flags)\n\
    \                    return [(DFSEvent.DOWN, p, u) for p,u in edges]\n       \
    \     case DFSFlags.UP|DFSFlags.BOTTOMUP:\n                if max_depth is None:\n\
    \                    edges = G.dfs_bottomup(s, DFSFlags.CONNECT_ROOTS in flags)\n\
    \                    return [(DFSEvent.UP, p, u) for p,u in edges]\n         \
    \   case flags if flags & DFSFlags.BACKTRACK:\n                return G.dfs_backtrack(flags,\
    \ s, max_depth)\n        state = [0] * G.N\n        child = [0] * G.N\n      \
    \  stack = [0] * G.N\n        if flags & DFSFlags.RETURN_PARENTS:\n          \
    \  parents = [-1] * G.N\n        if flags & DFSFlags.RETURN_DEPTHS:\n        \
    \    depths = [-1] * G.N\n\n        events = []\n        for s in G.starts(s):\n\
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
    \n        events = []\n        for s in G.starts(s):\n            if not state[s]:\
    \ continue\n            stack.append(s)\n            child.append(0)\n       \
    \     \n            while stack:\n                u = stack[-1]\n            \
    \    \n                if state[u]:\n                    state[u] = False\n  \
    \                  events.append((DFSEvent.ENTER, u))\n\n                \n  \
    \              if (c := child[-1]) < len(G[u]):\n                    child[-1]\
    \ += 1\n                    if state[v := G[u][c]]:\n                        stack.append(v)\n\
    \                        child.append(0)\n                else:\n            \
    \        stack.pop()\n                    child.pop()\n                    events.append((DFSEvent.LEAVE,\
    \ u))\n\n        return events\n    \n    def dfs_topdown(G, s: int|list[int]|None\
    \ = None, connect_roots = False):\n        '''Returns list of (u,v) representing\
    \ u->v edges in order of top down discovery'''\n        stack: list[int] = elist(G.N)\n\
    \        vis = [False]*G.N\n        edges: list[tuple[int,int]] = elist(G.N)\n\
    \n        for s in G.starts(s):\n            if vis[s]: continue\n           \
    \ if connect_roots:\n                edges.append((-1,s))\n            vis[s]\
    \ = True\n            stack.append(s)\n            while stack:\n            \
    \    u = stack.pop()\n                for v in G[u]:\n                    if vis[v]:\
    \ continue\n                    vis[v] = True\n                    edges.append((u,v))\n\
    \                    stack.append(v)\n        return edges\n    \n    def dfs_bottomup(G,\
    \ s: int|list[int]|None = None, connect_roots = False):\n        '''Returns list\
    \ of (p,u) representing p->u edges in bottom up order'''\n        edges = G.dfs_topdown(s,\
    \ connect_roots)\n        edges.reverse()\n        return edges\n\n    def is_bipartite(G):\n\
    \        N = G.N\n        que = deque()\n        color = [-1]*N\n            \
    \    \n        for s in range(N):\n            if color[s] >= 0:\n           \
    \     continue\n            color[s] = 1\n            que.append(s)\n        \
    \    while que:\n                u = que.popleft()\n                for v in G[u]:\n\
    \                    if color[v] == -1:\n                        color[v] = 1\
    \ - color[u]\n                        que.append(v)\n                    elif\
    \ color[v] == color[u]:\n                        return False\n        return\
    \ True\n    \n    def starts(G, v: int|list[int]|None) -> Iterable:\n        match\
    \ v:\n            case int(v): return (v,)\n            case None: return range(G.N)\n\
    \            case V: return V\n\n    @classmethod\n    def compile(cls, N: int,\
    \ M: int, E):\n        edge = Parser.compile(E)\n        def parse(ts: TokenStream):\n\
    \            return cls(N, [edge(ts) for _ in range(M)])\n        return parse\n\
    \    \n\nclass Graph(GraphProtocol):\n    def __init__(G, N: int, edges=[]):\n\
    \        super().__init__(set() for _ in range(N))\n        G.E = list(edges)\n\
    \        G.N, G.M = N, len(G.E)\n        for u,v in G.E:\n            G[u].add(v)\n\
    \            G[v].add(u)\n\n    @classmethod\n    def compile(cls, N: int, M:\
    \ int, E: type|int = Edge[-1]):\n        if isinstance(E, int): E = Edge[E]\n\
    \        return super().compile(N, M, E)\n\nfrom typing import overload, Literal\n\
    from functools import cached_property\n\nfrom typing import Any, Callable, List\n\
    \nclass SparseTable:\n    def __init__(self, op: Callable[[Any, Any], Any], arr:\
    \ List[Any]):\n        self.N = N = len(arr)\n        self.log = N.bit_length()\n\
    \        self.op = op\n        \n        self.offsets = offsets = [0]\n      \
    \  for i in range(1, self.log):\n            offsets.append(offsets[-1] + N -\
    \ (1 << (i-1)) + 1)\n            \n        self.st = st = [0] * (offsets[-1] +\
    \ N - (1 << (self.log-1)) + 1)\n        st[:N] = arr \n        \n        for i\
    \ in range(self.log - 1):\n            d = 1 << i\n            start = offsets[i]\n\
    \            next_start = offsets[i + 1]\n            for j in range(N - (1 <<\
    \ (i+1)) + 1):\n                st[next_start + j] = op(st[k := start+j], st[k\
    \ + d])\n\n    def query(self, l: int, r: int) -> Any:\n        k = (r-l).bit_length()\
    \ - 1\n        start, st = self.offsets[k], self.st\n        return self.op(st[start\
    \ + l], st[start + r - (1 << k)])\n    \n    def __repr__(self) -> str:\n    \
    \    rows = []\n        for i in range(self.log):\n            start = self.offsets[i]\n\
    \            end = self.offsets[i+1] if i+1 < self.log else len(self.st)\n   \
    \         rows.append(f\"{i:<2d} {self.st[start:end]}\")\n        return '\\n'.join(rows)\n\
    \nimport operator\nfrom itertools import accumulate\n\nT = TypeVar('T')\ndef presum(iter:\
    \ Iterable[T], func: Callable[[T,T],T] = None, initial: T = None, step = 1) ->\
    \ list[T]:\n    match step:\n        case 1:\n            return list(accumulate(iter,\
    \ func, initial=initial))\n        case step:\n            assert step >= 2\n\
    \            if func is None:\n                func = operator.add\n         \
    \   A = list(iter)\n            if initial is not None:\n                A = [initial]\
    \ + A\n            for i in range(step,len(A)):\n                A[i] = func(A[i],\
    \ A[i-step])\n            return A\n\nclass LCATable(SparseTable):\n    def __init__(self,\
    \ T, root = 0):\n        N = len(T)\n        T.euler_tour(root)\n        self.depth\
    \ = depth = presum(T.delta)\n        self.start, self.stop = T.tin, T.tout\n\n\
    \        self.mask = (1 << (shift := N.bit_length()))-1\n        self.shift =\
    \ shift\n        order = T.order\n        M = len(order)\n        packets = [0]*M\n\
    \        for i in range(M):\n            packets[i] = depth[i] << shift | order[i]\
    \ \n\n        super().__init__(min, packets)\n\n    def _query(self, u, v):\n\
    \        l,r = min(self.start[u], self.start[v]), max(self.start[u], self.start[v])+1\n\
    \        da = super().query(l, r)\n        return l, r, da & self.mask, da >>\
    \ self.shift\n\n    def query(self, u, v) -> tuple[int,int]:\n        l, r, a,\
    \ d = self._query(u, v)\n        return a, d\n    \n    def distance(self, u,\
    \ v) -> int:\n        l, r, a, d = self._query(u, v)\n        return self.depth[l]\
    \ + self.depth[r] - 2*d\n\nclass TreeProtocol(GraphProtocol):\n\n    @cached_property\n\
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
    \ 0, g = None):\n        D = [inft for _ in range(T.N)]\n        D[s] = 0\n  \
    \      state = [True for _ in range(T.N)]\n        stack = [s]\n\n        while\
    \ stack:\n            u = stack.pop()\n            if u == g: return D[u]\n  \
    \          state[u] = False\n            for v in T[u]:\n                if state[v]:\n\
    \                    D[v] = D[u]+1\n                    stack.append(v)\n    \
    \    return D if g is None else inft \n\n\n    def dfs_events(G, flags: DFSFlags,\
    \ s: int = 0):         \n        events = []\n        # stack = deque([(s,-1)],\
    \ maxlen=G.N)\n        stack = [(s,-1)]\n        adj = [None]*G.N\n\n\n      \
    \  while stack:\n            u, p = stack[-1]\n            \n            if adj[u]\
    \ is None:\n                adj[u] = iter(G.neighbors(u))\n                if\
    \ DFSFlags.ENTER in flags:\n                    events.append((DFSEvent.ENTER,\
    \ u))\n            \n            if (v := next(adj[u], None)) is not None:\n \
    \               if v == p:\n                    if DFSFlags.BACK in flags:\n \
    \                       events.append((DFSEvent.BACK, u, v))\n               \
    \ else:\n                    if DFSFlags.DOWN in flags:\n                    \
    \    events.append((DFSEvent.DOWN, u, v))\n                    stack.append((v,u))\n\
    \            else:\n                stack.pop()\n\n                if DFSFlags.LEAVE\
    \ in flags:\n                    events.append((DFSEvent.LEAVE, u))\n        \
    \        if p != -1 and DFSFlags.UP in flags:\n                    events.append((DFSEvent.UP,\
    \ u, p))\n        return events\n    \n    def euler_tour(T, s = 0):\n       \
    \ N = len(T)\n        T.tin = tin = [-1] * N\n        T.tout = tout = [-1] * N\n\
    \        T.par = par = [-1] * N\n        T.order = order = elist(2*N)\n      \
    \  T.delta = delta = elist(2*N)\n        \n        stack = elist(N)\n        stack.append(s)\n\
    \n        while stack:\n            u = stack.pop()\n            p = par[u]\n\
    \            \n            if tin[u] == -1:\n                tin[u] = len(order)\n\
    \                \n                for v in T[u]:\n                    if v !=\
    \ p:\n                        par[v] = u\n                        stack.append(u)\n\
    \                        stack.append(v)\n                \n                delta.append(1)\n\
    \            else:\n                delta.append(-1)\n            \n         \
    \   order.append(u)\n            tout[u] = len(order)\n        delta[0] = delta[-1]\
    \ = 0\n\n    def hld_precomp(T, r = 0):\n        N, time = T.N, 0\n        tin,\
    \ tout, size = [0]*N, [0]*N, [1]*N+[0]\n        par, heavy, head = [-1]*N, [-1]*N,\
    \ [r]*N\n        depth, order, state = [0]*N, [0]*N, [0]*N\n        stack = elist(N)\n\
    \        stack.append(r)\n        while stack:\n            match state[v := stack.pop()]:\n\
    \                case 0: # dfs down\n                    p, state[v] = par[v],\
    \ 1\n                    stack.append(v)\n                    for c in T[v]:\n\
    \                        if c != p:\n                            depth[c], par[c]\
    \ = depth[v]+1, v\n                            stack.append(c)\n\n           \
    \     case 1: # dfs up\n                    p, l = par[v], -1\n              \
    \      for c in T[v]:\n                        if c != p:\n                  \
    \          size[v] += size[c]\n                            if size[c] > size[l]:\n\
    \                                l = c\n                    heavy[v] = l\n   \
    \                 if p == -1:\n                        state[v] = 2\n        \
    \                stack.append(v)\n\n                case 2: # decompose down\n\
    \                    p, h, l = par[v], head[v], heavy[v]\n                   \
    \ tin[v], order[time], state[v] = time, v, 3\n                    time += 1\n\
    \                    stack.append(v)\n                    \n                 \
    \   for c in T[v]:\n                        if c != p and c != l:\n          \
    \                  head[c], state[c] = c, 2\n                            stack.append(c)\n\
    \n                    if l != -1:\n                        head[l], state[l] =\
    \ h, 2\n                        stack.append(l)\n                case 3: # decompose\
    \ up\n                    tout[v] = time\n        T.size, T.depth = size, depth\n\
    \        T.order, T.tin, T.tout = order, tin, tout\n        T.par, T.heavy, T.head\
    \ = par, heavy, head\n\nclass Tree(Graph, TreeProtocol):\n    @classmethod\n \
    \   def compile(cls, N: int, E: type|int = Edge[-1]):\n        return super().compile(N,\
    \ N-1, E)\n    \n    \n"
  code: "import cp_library.alg.tree.__header__\n\nfrom cp_library.alg.graph.edge_cls\
    \ import Edge\nfrom cp_library.alg.graph.graph_set_cls import Graph\nfrom cp_library.alg.tree.tree_proto\
    \ import TreeProtocol\n\nclass Tree(Graph, TreeProtocol):\n    @classmethod\n\
    \    def compile(cls, N: int, E: type|int = Edge[-1]):\n        return super().compile(N,\
    \ N-1, E)\n    \n    "
  dependsOn:
  - cp_library/alg/graph/edge_cls.py
  - cp_library/alg/graph/graph_set_cls.py
  - cp_library/alg/tree/tree_proto.py
  - cp_library/alg/graph/graph_proto.py
  - cp_library/ds/elist_fn.py
  - cp_library/math/inft_cnst.py
  - cp_library/alg/graph/dfs_options_cls.py
  - cp_library/alg/tree/lca_table_iterative_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/ds/sparse_table_cls.py
  - cp_library/alg/iter/presum_fn.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: false
  path: cp_library/alg/tree/tree_set_cls.py
  requiredBy: []
  timestamp: '2024-12-17 21:59:33+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/tree/tree_set_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/tree/tree_set_cls.py
- /library/cp_library/alg/tree/tree_set_cls.py.html
title: cp_library/alg/tree/tree_set_cls.py
---