---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/dfs_options_cls.py
    title: cp_library/alg/graph/dfs_options_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/elist_fn.py
    title: cp_library/ds/list/elist_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/io_base_cls.py
    title: cp_library/io/io_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parsable_cls.py
    title: cp_library/io/parsable_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/alg/graph/set/graph_set_cls.py
    title: cp_library/alg/graph/set/graph_set_cls.py
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
    from typing import Iterable, Union, overload\nfrom collections import deque\n\
    from math import inf\nfrom types import GenericAlias\n\n\nclass Parsable:\n  \
    \  @classmethod\n    def compile(cls):\n        def parser(io: 'IOBase'): return\
    \ cls(next(io))\n        return parser\n    @classmethod\n    def __class_getitem__(cls,\
    \ item): return GenericAlias(cls, item)\n\n\n\nfrom enum import auto, IntFlag,\
    \ IntEnum\n\nclass DFSFlags(IntFlag):\n    ENTER = auto()\n    DOWN = auto()\n\
    \    BACK = auto()\n    CROSS = auto()\n    LEAVE = auto()\n    UP = auto()\n\
    \    MAXDEPTH = auto()\n\n    RETURN_PARENTS = auto()\n    RETURN_DEPTHS = auto()\n\
    \    BACKTRACK = auto()\n    CONNECT_ROOTS = auto()\n\n    # Common combinations\n\
    \    ALL_EDGES = DOWN | BACK | CROSS\n    EULER_TOUR = DOWN | UP\n    INTERVAL\
    \ = ENTER | LEAVE\n    TOPDOWN = DOWN | CONNECT_ROOTS\n    BOTTOMUP = UP | CONNECT_ROOTS\n\
    \    RETURN_ALL = RETURN_PARENTS | RETURN_DEPTHS\n\nclass DFSEvent(IntEnum):\n\
    \    ENTER = DFSFlags.ENTER \n    DOWN = DFSFlags.DOWN \n    BACK = DFSFlags.BACK\
    \ \n    CROSS = DFSFlags.CROSS \n    LEAVE = DFSFlags.LEAVE \n    UP = DFSFlags.UP\
    \ \n    MAXDEPTH = DFSFlags.MAXDEPTH\n    \n\n\nclass GraphProtocol(list, Parsable):\n\
    \    def __init__(G, N: int, E: list = None, adj: Iterable = None):\n        G.N\
    \ = N\n        if E is not None: G.M, G.E = len(E), E\n        if adj is not None:\
    \ super().__init__(adj)\n\n    def neighbors(G, v: int) -> Iterable[int]: return\
    \ G[v]\n    \n    def edge_ids(G) -> list[list[int]]: ...\n\n    @overload\n \
    \   def distance(G) -> list[list[int]]: ...\n    @overload\n    def distance(G,\
    \ s: int = 0) -> list[int]: ...\n    @overload\n    def distance(G, s: int, g:\
    \ int) -> int: ...\n    def distance(G, s = None, g = None):\n        if s ==\
    \ None:\n            return G.floyd_warshall()\n        else:\n            return\
    \ G.bfs(s, g)\n\n    @overload\n    def bfs(G, s: Union[int,list] = 0) -> list[int]:\
    \ ...\n    @overload\n    def bfs(G, s: Union[int,list], g: int) -> int: ...\n\
    \    def bfs(G, s = 0, g = None):\n        D = [inf for _ in range(G.N)]\n   \
    \     q = deque([s] if isinstance(s, int) else s)\n        for u in q: D[u] =\
    \ 0\n        while q:\n            nd = D[u := q.popleft()]+1\n            if\
    \ u == g: return D[u]\n            for v in G.neighbors(u):\n                if\
    \ nd < D[v]:\n                    D[v] = nd\n                    q.append(v)\n\
    \        return D if g is None else inf \n\n    @overload\n    def shortest_path(G,\
    \ s: int, g: int) -> Union[list[int],None]: ...\n    @overload\n    def shortest_path(G,\
    \ s: int, g: int, distances = True) -> tuple[Union[list[int],None],list[int]]:\
    \ ...\n    def shortest_path(G, s: int, g: int, distances = False) -> list[int]:\n\
    \        D = [inf] * G.N\n        D[s] = 0\n        if s == g:\n            return\
    \ ([], D) if distances else []\n            \n        par = [-1] * G.N\n     \
    \   par_edge = [-1] * G.N\n        Eid = G.edge_ids()\n        q = deque([s])\n\
    \        \n        while q:\n            nd = D[u := q.popleft()] + 1\n      \
    \      if u == g: break\n                \n            for v, eid in zip(G[u],\
    \ Eid[u]):\n                if nd < D[v]:\n                    D[v] = nd\n   \
    \                 par[v] = u\n                    par_edge[v] = eid\n        \
    \            q.append(v)\n        \n        if D[g] == inf:\n            return\
    \ (None, D) if distances else None\n            \n        path = []\n        current\
    \ = g\n        while current != s:\n            path.append(par_edge[current])\n\
    \            current = par[current]\n            \n        return (path[::-1],\
    \ D) if distances else path[::-1]\n\n    def floyd_warshall(G) -> list[list[int]]:\n\
    \        D = [[inf]*G.N for _ in range(G.N)]\n\n        for u in range(G.N):\n\
    \            D[u][u] = 0\n            for v in G.neighbors(u):\n             \
    \   D[u][v] = 1\n        \n        for k, Dk in enumerate(D):\n            for\
    \ Di in D:\n                if Di[k] == inf: continue\n                for j in\
    \ range(G.N):\n                    if Dk[j] == inf: continue\n               \
    \     Di[j] = min(Di[j], Di[k]+Dk[j])\n        return D\n    \n    def find_cycle(G,\
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
    \ u))\n            else:\n                vis[v] = 2\n        return None\n\n\
    \    def find_minimal_cycle(G, s=0):\n        D, par, que = [inf] * (N := G.N),\
    \ [-1] * N, deque([s])\n        D[s] = 0\n        while que:\n            for\
    \ v in G[u := que.popleft()]:\n                if v == s:  # Found cycle back\
    \ to start\n                    cycle = [u]\n                    while u != s:\
    \ cycle.append(u := par[u])\n                    return cycle\n              \
    \  if D[v] < inf: continue\n                D[v], par[v] = D[u]+1, u\n       \
    \         que.append(v)\n    \n    def bridges(G):\n        tin = [-1] * G.N\n\
    \        low = [-1] * G.N\n        par = [-1] * G.N\n        vis = [0] * G.N\n\
    \        in_edge = [-1] * G.N\n\n        Eid = G.edge_ids()\n        time = 0\n\
    \        bridges = []\n        stack = list(range(G.N))\n        while stack:\n\
    \            p = par[v := stack.pop()]\n            if vis[v] == 0:\n        \
    \        vis[v] = 1\n                tin[v] = low[v] = time\n                time\
    \ += 1\n                stack.append(v)\n                for i, child in enumerate(G.neighbors(v)):\n\
    \                    if child == p: continue\n                    if vis[child]\
    \ == 0: # Tree edge - recurse\n                        par[child] = v\n      \
    \                  in_edge[child] = Eid[v][i]\n                        stack.append(child)\n\
    \                    else: # Back edge - update low-link value\n             \
    \           low[v] = min(low[v], tin[child])\n            elif vis[v] == 1:\n\
    \                vis[v] = 2\n                if p != -1:\n                   \
    \ low[p] = min(low[p], low[v])\n                    if low[v] > tin[p]: bridges.append(in_edge[v])\n\
    \        return bridges\n\n    def articulation_points(G):\n        '''\n    \
    \    Find articulation points in an undirected graph using DFS events.\n     \
    \   Returns a boolean list that is True for indices where the vertex is an articulation\
    \ point.\n        '''\n        N = G.N\n        order = [-1] * N\n        low\
    \ = [-1] * N\n        par = [-1] * N\n        state = [0] * N\n        children\
    \ = [0] * N\n        ap = [False] * N\n        time = 0\n        stack = list(range(N))\n\
    \n        while stack:\n            v = stack.pop()\n            p = par[v]\n\
    \            if state[v] == 0:\n                state[v] = 1\n               \
    \ order[v] = low[v] = time\n                time += 1\n            \n        \
    \        stack.append(v)\n                for child in G[v]:\n               \
    \     if order[child] == -1:\n                        par[child] = v\n       \
    \                 stack.append(child)\n                    elif child != p:\n\
    \                        low[v] = min(low[v], order[child])\n                if\
    \ p != -1:\n                    children[p] += 1\n            elif state[v] ==\
    \ 1:\n                state[v] = 2\n                ap[v] |= p == -1 and children[v]\
    \ > 1\n                if p != -1:\n                    low[p] = min(low[p], low[v])\n\
    \                    ap[p] |= par[p] != -1 and low[v] >= order[p]\n\n        return\
    \ ap\n    \n    def dfs_events(G, flags: DFSFlags, s: Union[int,list,None] = None,\
    \ max_depth: Union[int,None] = None):\n        if flags == DFSFlags.INTERVAL:\n\
    \            if max_depth is None:\n                return G.dfs_enter_leave(s)\n\
    \        elif flags == DFSFlags.DOWN or flags == DFSFlags.TOPDOWN:\n         \
    \   if max_depth is None:\n                edges = G.dfs_topo(s, DFSFlags.CONNECT_ROOTS\
    \ in flags)\n                return [(DFSEvent.DOWN, p, u) for p,u in edges]\n\
    \        elif flags == DFSFlags.UP or flags == DFSFlags.BOTTOMUP:\n          \
    \  if max_depth is None:\n                edges = G.dfs_bottomup(s, DFSFlags.CONNECT_ROOTS\
    \ in flags)\n                return [(DFSEvent.UP, p, u) for p,u in edges]\n \
    \       elif flags & DFSFlags.BACKTRACK:\n            return G.dfs_backtrack(flags,\
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
    \ < len(G[u]):\n                    child[u] += 1\n                    if (s :=\
    \ state[v := G[u][c]]) == 0: # Unvisited\n                        if max_depth\
    \ is None or depth <= max_depth:\n                            if flags & DFSFlags.DOWN:\n\
    \                                events.append((DFSEvent.DOWN, u, v))\n      \
    \                      stack[depth := depth+1] = v\n                         \
    \   if flags & DFSFlags.RETURN_PARENTS:\n                                parents[v]\
    \ = u\n                    elif s == 1:  # In progress\n                     \
    \   if flags & DFSFlags.BACK:\n                            events.append((DFSEvent.BACK,\
    \ u, v))\n                    elif s == 2: # Completed\n                     \
    \   if flags & DFSFlags.CROSS:\n                            events.append((DFSEvent.CROSS,\
    \ u, v))\n                else:\n                    depth -= 1\n            \
    \        state[u] = 0 if DFSFlags.BACKTRACK in flags else 2\n                \
    \    if flags & DFSFlags.LEAVE:\n                        events.append((DFSEvent.LEAVE,\
    \ u))\n                    if depth != -1 and flags & DFSFlags.UP:\n         \
    \               events.append((DFSEvent.UP, stack[depth], u))\n            if\
    \ (DFSFlags.UP|DFSFlags.CONNECT_ROOTS) in flags:\n                events.append((DFSEvent.UP,-1,s))\n\
    \        ret = tuple((events,)) if DFSFlags.RETURN_ALL & flags else events\n \
    \       if DFSFlags.RETURN_PARENTS in flags:\n            ret += (parents,)\n\
    \        if DFSFlags.RETURN_DEPTHS in flags:\n            ret += (depths,)\n \
    \       return ret\n\n    def dfs_backtrack(G, flags: DFSFlags, s: Union[int,list]\
    \ = None, max_depth: Union[int,None] = None):\n        stack_depth = (max_depth+1\
    \ if max_depth is not None else G.N)\n        stack = [0]*stack_depth\n      \
    \  child = [0]*stack_depth\n        state = [0]*G.N\n        events: list[tuple[DFSEvent,\
    \ int]|tuple[DFSEvent, int, int]] = []\n\n        for s in G.starts(s):\n    \
    \        if state[s]: continue\n            state[s] = 1\n            stack[depth\
    \ := 0] = s\n            if DFSFlags.DOWN|DFSFlags.CONNECT_ROOTS in flags:\n \
    \               events.append((DFSEvent.DOWN,-1,s))\n            while depth !=\
    \ -1:\n                u = stack[depth]\n                if state[u] == 1:\n \
    \                   state[u] = 2\n                    if DFSFlags.ENTER in flags:\n\
    \                        events.append((DFSEvent.ENTER,u))\n                 \
    \   if max_depth is not None and depth >= max_depth:\n                       \
    \ child[depth] = len(G[u])\n                        if DFSFlags.MAXDEPTH in flags:\n\
    \                            events.append((DFSEvent.MAXDEPTH,u))\n\n        \
    \        if (c := child[depth]) < len(G[u]):\n                    child[depth]\
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
    \    def dfs_enter_leave(G, s: Union[int,list,None] = None):\n        state =\
    \ [True] * G.N\n        child: list[int] = elist(G.N)\n        stack: list[int]\
    \ = elist(G.N)\n\n        events = []\n        for s in G.starts(s):\n       \
    \     if not state[s]: continue\n            stack.append(s)\n            child.append(0)\n\
    \            \n            while stack:\n                u = stack[-1]\n     \
    \           \n                if state[u]:\n                    state[u] = False\n\
    \                    events.append((DFSEvent.ENTER, u))\n\n                \n\
    \                if (c := child[-1]) < len(G[u]):\n                    child[-1]\
    \ += 1\n                    if state[v := G[u][c]]:\n                        stack.append(v)\n\
    \                        child.append(0)\n                else:\n            \
    \        stack.pop()\n                    child.pop()\n                    events.append((DFSEvent.LEAVE,\
    \ u))\n\n        return events\n    \n    def dfs_topo(G, s: Union[int,list,None]\
    \ = None, connect_roots = False):\n        '''Returns list of (u,v) representing\
    \ u->v edges in order of top down discovery'''\n        stack: list[int] = elist(G.N)\n\
    \        vis = [False]*G.N\n        edges: list[tuple[int,int]] = elist(G.N)\n\
    \n        for s in G.starts(s):\n            if vis[s]: continue\n           \
    \ if connect_roots:\n                edges.append((-1,s))\n            vis[s]\
    \ = True\n            stack.append(s)\n            while stack:\n            \
    \    u = stack.pop()\n                for v in G[u]:\n                    if vis[v]:\
    \ continue\n                    vis[v] = True\n                    edges.append((u,v))\n\
    \                    stack.append(v)\n        return edges\n    \n    def dfs_bottomup(G,\
    \ s: Union[int,list,None] = None, connect_roots = False):\n        '''Returns\
    \ list of (p,u) representing p->u edges in bottom up order'''\n        edges =\
    \ G.dfs_topo(s, connect_roots)\n        edges.reverse()\n        return edges\n\
    \n    def is_bipartite(G):\n        N = G.N\n        que = deque()\n        color\
    \ = [-1]*N\n                \n        for s in range(N):\n            if color[s]\
    \ >= 0:\n                continue\n            color[s] = 1\n            que.append(s)\n\
    \            while que:\n                u = que.popleft()\n                for\
    \ v in G[u]:\n                    if color[v] == -1:\n                       \
    \ color[v] = 1 - color[u]\n                        que.append(v)\n           \
    \         elif color[v] == color[u]:\n                        return False\n \
    \       return True\n    \n    def starts(G, v: Union[int,list,None]) -> Iterable:\n\
    \        if isinstance(v, int):\n            return (v,)\n        elif v is None:\n\
    \            return range(G.N)\n        else:\n            return v\n\n    @classmethod\n\
    \    def compile(cls, N: int, M: int, E):\n        edge = Parser.compile(E)\n\
    \        def parse(io: IOBase):\n            return cls(N, [edge(io) for _ in\
    \ range(M)])\n        return parse\n    \n\n\ndef elist(est_len: int) -> list:\
    \ ...\ntry:\n    from __pypy__ import newlist_hint\nexcept:\n    def newlist_hint(hint):\n\
    \        return []\nelist = newlist_hint\n    \n\nclass IOBase:\n    @property\n\
    \    def char(io) -> bool: ...\n    @property\n    def writable(io) -> bool: ...\n\
    \    def __next__(io) -> str: ...\n    def write(io, s: str) -> None: ...\n  \
    \  def readline(io) -> str: ...\n    def readtoken(io) -> str: ...\n    def readtokens(io)\
    \ -> list[str]: ...\n    def readints(io) -> list[int]: ...\n    def readdigits(io)\
    \ -> list[int]: ...\n    def readnums(io) -> list[int]: ...\n    def readchar(io)\
    \ -> str: ...\n    def readchars(io) -> str: ...\n    def readinto(io, lst: list[str])\
    \ -> list[str]: ...\n    def readcharsinto(io, lst: list[str]) -> list[str]: ...\n\
    \    def readtokensinto(io, lst: list[str]) -> list[str]: ...\n    def readintsinto(io,\
    \ lst: list[int]) -> list[int]: ...\n    def readdigitsinto(io, lst: list[int])\
    \ -> list[int]: ...\n    def readnumsinto(io, lst: list[int]) -> list[int]: ...\n\
    \    def wait(io): ...\n    def flush(io) -> None: ...\n    def line(io) -> list[str]:\
    \ ...\nimport typing\nfrom numbers import Number\nfrom typing import Callable,\
    \ Collection\n\nclass Parser:\n    def __init__(self, spec):  self.parse = Parser.compile(spec)\n\
    \    def __call__(self, io: IOBase): return self.parse(io)\n    @staticmethod\n\
    \    def compile_type(cls, args = ()):\n        if issubclass(cls, Parsable):\
    \ return cls.compile(*args)\n        elif issubclass(cls, (Number, str)):\n  \
    \          def parse(io: IOBase): return cls(next(io))              \n       \
    \     return parse\n        elif issubclass(cls, tuple): return Parser.compile_tuple(cls,\
    \ args)\n        elif issubclass(cls, Collection): return Parser.compile_collection(cls,\
    \ args)\n        elif callable(cls):\n            def parse(io: IOBase): return\
    \ cls(next(io))              \n            return parse\n        else: raise NotImplementedError()\n\
    \    @staticmethod\n    def compile(spec=int):\n        if isinstance(spec, (type,\
    \ GenericAlias)):\n            cls, args = typing.get_origin(spec) or spec, typing.get_args(spec)\
    \ or tuple()\n            return Parser.compile_type(cls, args)\n        elif\
    \ isinstance(offset := spec, Number): \n            cls = type(spec)  \n     \
    \       def parse(io: IOBase): return cls(next(io)) + offset\n            return\
    \ parse\n        elif isinstance(args := spec, tuple): return Parser.compile_tuple(type(spec),\
    \ args)\n        elif isinstance(args := spec, Collection): return Parser.compile_collection(type(spec),\
    \ args)\n        elif isinstance(fn := spec, Callable): \n            def parse(io:\
    \ IOBase): return fn(next(io))\n            return parse\n        else: raise\
    \ NotImplementedError()\n    @staticmethod\n    def compile_line(cls, spec=int):\n\
    \        if spec is int:\n            def parse(io: IOBase): return cls(io.readnums())\n\
    \        else:\n            fn = Parser.compile(spec)\n            def parse(io:\
    \ IOBase): return cls([fn(io) for _ in io.wait()])\n        return parse\n   \
    \ @staticmethod\n    def compile_repeat(cls, spec, N):\n        fn = Parser.compile(spec)\n\
    \        def parse(io: IOBase): return cls([fn(io) for _ in range(N)])\n     \
    \   return parse\n    @staticmethod\n    def compile_children(cls, specs):\n \
    \       fns = tuple((Parser.compile(spec) for spec in specs))\n        def parse(io:\
    \ IOBase): return cls([fn(io) for fn in fns])  \n        return parse\n    @staticmethod\n\
    \    def compile_tuple(cls, specs):\n        if isinstance(specs, (tuple,list))\
    \ and len(specs) == 2 and specs[1] is ...: return Parser.compile_line(cls, specs[0])\n\
    \        else: return Parser.compile_children(cls, specs)\n    @staticmethod\n\
    \    def compile_collection(cls, specs):\n        if not specs or len(specs) ==\
    \ 1 or isinstance(specs, set):\n            return Parser.compile_line(cls, *specs)\n\
    \        elif (isinstance(specs, (tuple,list)) and len(specs) == 2 and isinstance(specs[1],\
    \ int)):\n            return Parser.compile_repeat(cls, specs[0], specs[1])\n\
    \        else:\n            raise NotImplementedError()\n"
  code: "import cp_library.__header__\nfrom typing import Iterable, Union, overload\n\
    from collections import deque\nfrom math import inf\nfrom cp_library.io.parsable_cls\
    \ import Parsable\nimport cp_library.alg.__header__\nimport cp_library.alg.graph.__header__\n\
    from cp_library.alg.graph.dfs_options_cls import DFSFlags, DFSEvent\nimport cp_library.alg.graph.set.__header__\n\
    \nclass GraphProtocol(list, Parsable):\n    def __init__(G, N: int, E: list =\
    \ None, adj: Iterable = None):\n        G.N = N\n        if E is not None: G.M,\
    \ G.E = len(E), E\n        if adj is not None: super().__init__(adj)\n\n    def\
    \ neighbors(G, v: int) -> Iterable[int]: return G[v]\n    \n    def edge_ids(G)\
    \ -> list[list[int]]: ...\n\n    @overload\n    def distance(G) -> list[list[int]]:\
    \ ...\n    @overload\n    def distance(G, s: int = 0) -> list[int]: ...\n    @overload\n\
    \    def distance(G, s: int, g: int) -> int: ...\n    def distance(G, s = None,\
    \ g = None):\n        if s == None:\n            return G.floyd_warshall()\n \
    \       else:\n            return G.bfs(s, g)\n\n    @overload\n    def bfs(G,\
    \ s: Union[int,list] = 0) -> list[int]: ...\n    @overload\n    def bfs(G, s:\
    \ Union[int,list], g: int) -> int: ...\n    def bfs(G, s = 0, g = None):\n   \
    \     D = [inf for _ in range(G.N)]\n        q = deque([s] if isinstance(s, int)\
    \ else s)\n        for u in q: D[u] = 0\n        while q:\n            nd = D[u\
    \ := q.popleft()]+1\n            if u == g: return D[u]\n            for v in\
    \ G.neighbors(u):\n                if nd < D[v]:\n                    D[v] = nd\n\
    \                    q.append(v)\n        return D if g is None else inf \n\n\
    \    @overload\n    def shortest_path(G, s: int, g: int) -> Union[list[int],None]:\
    \ ...\n    @overload\n    def shortest_path(G, s: int, g: int, distances = True)\
    \ -> tuple[Union[list[int],None],list[int]]: ...\n    def shortest_path(G, s:\
    \ int, g: int, distances = False) -> list[int]:\n        D = [inf] * G.N\n   \
    \     D[s] = 0\n        if s == g:\n            return ([], D) if distances else\
    \ []\n            \n        par = [-1] * G.N\n        par_edge = [-1] * G.N\n\
    \        Eid = G.edge_ids()\n        q = deque([s])\n        \n        while q:\n\
    \            nd = D[u := q.popleft()] + 1\n            if u == g: break\n    \
    \            \n            for v, eid in zip(G[u], Eid[u]):\n                if\
    \ nd < D[v]:\n                    D[v] = nd\n                    par[v] = u\n\
    \                    par_edge[v] = eid\n                    q.append(v)\n    \
    \    \n        if D[g] == inf:\n            return (None, D) if distances else\
    \ None\n            \n        path = []\n        current = g\n        while current\
    \ != s:\n            path.append(par_edge[current])\n            current = par[current]\n\
    \            \n        return (path[::-1], D) if distances else path[::-1]\n\n\
    \    def floyd_warshall(G) -> list[list[int]]:\n        D = [[inf]*G.N for _ in\
    \ range(G.N)]\n\n        for u in range(G.N):\n            D[u][u] = 0\n     \
    \       for v in G.neighbors(u):\n                D[u][v] = 1\n        \n    \
    \    for k, Dk in enumerate(D):\n            for Di in D:\n                if\
    \ Di[k] == inf: continue\n                for j in range(G.N):\n             \
    \       if Dk[j] == inf: continue\n                    Di[j] = min(Di[j], Di[k]+Dk[j])\n\
    \        return D\n    \n    def find_cycle(G, s = 0, vis = None, par = None):\n\
    \        N = G.N\n        vis = vis or [0] * N\n        par = par or [-1] * N\n\
    \        if vis[s]: return None\n        vis[s] = 1\n        stack = [(True, s)]\n\
    \        while stack:\n            forw, v = stack.pop()\n            if forw:\n\
    \                stack.append((False, v))\n                vis[v] = 1\n      \
    \          for u in G.neighbors(v):\n                    if vis[u] == 1 and u\
    \ != par[v]:\n                        # Cycle detected\n                     \
    \   cyc = [u]\n                        vis[u] = 2\n                        while\
    \ v != u:\n                            cyc.append(v)\n                       \
    \     vis[v] = 2\n                            v = par[v]\n                   \
    \     return cyc\n                    elif vis[u] == 0:\n                    \
    \    par[u] = v\n                        stack.append((True, u))\n           \
    \ else:\n                vis[v] = 2\n        return None\n\n    def find_minimal_cycle(G,\
    \ s=0):\n        D, par, que = [inf] * (N := G.N), [-1] * N, deque([s])\n    \
    \    D[s] = 0\n        while que:\n            for v in G[u := que.popleft()]:\n\
    \                if v == s:  # Found cycle back to start\n                   \
    \ cycle = [u]\n                    while u != s: cycle.append(u := par[u])\n \
    \                   return cycle\n                if D[v] < inf: continue\n  \
    \              D[v], par[v] = D[u]+1, u\n                que.append(v)\n    \n\
    \    def bridges(G):\n        tin = [-1] * G.N\n        low = [-1] * G.N\n   \
    \     par = [-1] * G.N\n        vis = [0] * G.N\n        in_edge = [-1] * G.N\n\
    \n        Eid = G.edge_ids()\n        time = 0\n        bridges = []\n       \
    \ stack = list(range(G.N))\n        while stack:\n            p = par[v := stack.pop()]\n\
    \            if vis[v] == 0:\n                vis[v] = 1\n                tin[v]\
    \ = low[v] = time\n                time += 1\n                stack.append(v)\n\
    \                for i, child in enumerate(G.neighbors(v)):\n                \
    \    if child == p: continue\n                    if vis[child] == 0: # Tree edge\
    \ - recurse\n                        par[child] = v\n                        in_edge[child]\
    \ = Eid[v][i]\n                        stack.append(child)\n                 \
    \   else: # Back edge - update low-link value\n                        low[v]\
    \ = min(low[v], tin[child])\n            elif vis[v] == 1:\n                vis[v]\
    \ = 2\n                if p != -1:\n                    low[p] = min(low[p], low[v])\n\
    \                    if low[v] > tin[p]: bridges.append(in_edge[v])\n        return\
    \ bridges\n\n    def articulation_points(G):\n        '''\n        Find articulation\
    \ points in an undirected graph using DFS events.\n        Returns a boolean list\
    \ that is True for indices where the vertex is an articulation point.\n      \
    \  '''\n        N = G.N\n        order = [-1] * N\n        low = [-1] * N\n  \
    \      par = [-1] * N\n        state = [0] * N\n        children = [0] * N\n \
    \       ap = [False] * N\n        time = 0\n        stack = list(range(N))\n\n\
    \        while stack:\n            v = stack.pop()\n            p = par[v]\n \
    \           if state[v] == 0:\n                state[v] = 1\n                order[v]\
    \ = low[v] = time\n                time += 1\n            \n                stack.append(v)\n\
    \                for child in G[v]:\n                    if order[child] == -1:\n\
    \                        par[child] = v\n                        stack.append(child)\n\
    \                    elif child != p:\n                        low[v] = min(low[v],\
    \ order[child])\n                if p != -1:\n                    children[p]\
    \ += 1\n            elif state[v] == 1:\n                state[v] = 2\n      \
    \          ap[v] |= p == -1 and children[v] > 1\n                if p != -1:\n\
    \                    low[p] = min(low[p], low[v])\n                    ap[p] |=\
    \ par[p] != -1 and low[v] >= order[p]\n\n        return ap\n    \n    def dfs_events(G,\
    \ flags: DFSFlags, s: Union[int,list,None] = None, max_depth: Union[int,None]\
    \ = None):\n        if flags == DFSFlags.INTERVAL:\n            if max_depth is\
    \ None:\n                return G.dfs_enter_leave(s)\n        elif flags == DFSFlags.DOWN\
    \ or flags == DFSFlags.TOPDOWN:\n            if max_depth is None:\n         \
    \       edges = G.dfs_topo(s, DFSFlags.CONNECT_ROOTS in flags)\n             \
    \   return [(DFSEvent.DOWN, p, u) for p,u in edges]\n        elif flags == DFSFlags.UP\
    \ or flags == DFSFlags.BOTTOMUP:\n            if max_depth is None:\n        \
    \        edges = G.dfs_bottomup(s, DFSFlags.CONNECT_ROOTS in flags)\n        \
    \        return [(DFSEvent.UP, p, u) for p,u in edges]\n        elif flags & DFSFlags.BACKTRACK:\n\
    \            return G.dfs_backtrack(flags, s, max_depth)\n        state = [0]\
    \ * G.N\n        child = [0] * G.N\n        stack = [0] * G.N\n        if flags\
    \ & DFSFlags.RETURN_PARENTS:\n            parents = [-1] * G.N\n        if flags\
    \ & DFSFlags.RETURN_DEPTHS:\n            depths = [-1] * G.N\n\n        events\
    \ = []\n        for s in G.starts(s):\n            stack[depth := 0] = s\n   \
    \         if (DFSFlags.DOWN|DFSFlags.CONNECT_ROOTS) in flags:\n              \
    \  events.append((DFSEvent.DOWN,-1,s))\n            while depth != -1:\n     \
    \           u = stack[depth]\n                \n                if not state[u]:\n\
    \                    state[u] = 1\n                    if flags & DFSFlags.ENTER:\n\
    \                        events.append((DFSEvent.ENTER, u))\n                \
    \    if flags & DFSFlags.RETURN_DEPTHS:\n                        depths[u] = depth\n\
    \                \n                if (c := child[u]) < len(G[u]):\n         \
    \           child[u] += 1\n                    if (s := state[v := G[u][c]]) ==\
    \ 0: # Unvisited\n                        if max_depth is None or depth <= max_depth:\n\
    \                            if flags & DFSFlags.DOWN:\n                     \
    \           events.append((DFSEvent.DOWN, u, v))\n                           \
    \ stack[depth := depth+1] = v\n                            if flags & DFSFlags.RETURN_PARENTS:\n\
    \                                parents[v] = u\n                    elif s ==\
    \ 1:  # In progress\n                        if flags & DFSFlags.BACK:\n     \
    \                       events.append((DFSEvent.BACK, u, v))\n               \
    \     elif s == 2: # Completed\n                        if flags & DFSFlags.CROSS:\n\
    \                            events.append((DFSEvent.CROSS, u, v))\n         \
    \       else:\n                    depth -= 1\n                    state[u] =\
    \ 0 if DFSFlags.BACKTRACK in flags else 2\n                    if flags & DFSFlags.LEAVE:\n\
    \                        events.append((DFSEvent.LEAVE, u))\n                \
    \    if depth != -1 and flags & DFSFlags.UP:\n                        events.append((DFSEvent.UP,\
    \ stack[depth], u))\n            if (DFSFlags.UP|DFSFlags.CONNECT_ROOTS) in flags:\n\
    \                events.append((DFSEvent.UP,-1,s))\n        ret = tuple((events,))\
    \ if DFSFlags.RETURN_ALL & flags else events\n        if DFSFlags.RETURN_PARENTS\
    \ in flags:\n            ret += (parents,)\n        if DFSFlags.RETURN_DEPTHS\
    \ in flags:\n            ret += (depths,)\n        return ret\n\n    def dfs_backtrack(G,\
    \ flags: DFSFlags, s: Union[int,list] = None, max_depth: Union[int,None] = None):\n\
    \        stack_depth = (max_depth+1 if max_depth is not None else G.N)\n     \
    \   stack = [0]*stack_depth\n        child = [0]*stack_depth\n        state =\
    \ [0]*G.N\n        events: list[tuple[DFSEvent, int]|tuple[DFSEvent, int, int]]\
    \ = []\n\n        for s in G.starts(s):\n            if state[s]: continue\n \
    \           state[s] = 1\n            stack[depth := 0] = s\n            if DFSFlags.DOWN|DFSFlags.CONNECT_ROOTS\
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
    \    def dfs_enter_leave(G, s: Union[int,list,None] = None):\n        state =\
    \ [True] * G.N\n        child: list[int] = elist(G.N)\n        stack: list[int]\
    \ = elist(G.N)\n\n        events = []\n        for s in G.starts(s):\n       \
    \     if not state[s]: continue\n            stack.append(s)\n            child.append(0)\n\
    \            \n            while stack:\n                u = stack[-1]\n     \
    \           \n                if state[u]:\n                    state[u] = False\n\
    \                    events.append((DFSEvent.ENTER, u))\n\n                \n\
    \                if (c := child[-1]) < len(G[u]):\n                    child[-1]\
    \ += 1\n                    if state[v := G[u][c]]:\n                        stack.append(v)\n\
    \                        child.append(0)\n                else:\n            \
    \        stack.pop()\n                    child.pop()\n                    events.append((DFSEvent.LEAVE,\
    \ u))\n\n        return events\n    \n    def dfs_topo(G, s: Union[int,list,None]\
    \ = None, connect_roots = False):\n        '''Returns list of (u,v) representing\
    \ u->v edges in order of top down discovery'''\n        stack: list[int] = elist(G.N)\n\
    \        vis = [False]*G.N\n        edges: list[tuple[int,int]] = elist(G.N)\n\
    \n        for s in G.starts(s):\n            if vis[s]: continue\n           \
    \ if connect_roots:\n                edges.append((-1,s))\n            vis[s]\
    \ = True\n            stack.append(s)\n            while stack:\n            \
    \    u = stack.pop()\n                for v in G[u]:\n                    if vis[v]:\
    \ continue\n                    vis[v] = True\n                    edges.append((u,v))\n\
    \                    stack.append(v)\n        return edges\n    \n    def dfs_bottomup(G,\
    \ s: Union[int,list,None] = None, connect_roots = False):\n        '''Returns\
    \ list of (p,u) representing p->u edges in bottom up order'''\n        edges =\
    \ G.dfs_topo(s, connect_roots)\n        edges.reverse()\n        return edges\n\
    \n    def is_bipartite(G):\n        N = G.N\n        que = deque()\n        color\
    \ = [-1]*N\n                \n        for s in range(N):\n            if color[s]\
    \ >= 0:\n                continue\n            color[s] = 1\n            que.append(s)\n\
    \            while que:\n                u = que.popleft()\n                for\
    \ v in G[u]:\n                    if color[v] == -1:\n                       \
    \ color[v] = 1 - color[u]\n                        que.append(v)\n           \
    \         elif color[v] == color[u]:\n                        return False\n \
    \       return True\n    \n    def starts(G, v: Union[int,list,None]) -> Iterable:\n\
    \        if isinstance(v, int):\n            return (v,)\n        elif v is None:\n\
    \            return range(G.N)\n        else:\n            return v\n\n    @classmethod\n\
    \    def compile(cls, N: int, M: int, E):\n        edge = Parser.compile(E)\n\
    \        def parse(io: IOBase):\n            return cls(N, [edge(io) for _ in\
    \ range(M)])\n        return parse\n    \nfrom cp_library.ds.list.elist_fn import\
    \ elist\nfrom cp_library.io.io_base_cls import IOBase\nfrom cp_library.io.parser_cls\
    \ import Parser"
  dependsOn:
  - cp_library/io/parsable_cls.py
  - cp_library/alg/graph/dfs_options_cls.py
  - cp_library/ds/list/elist_fn.py
  - cp_library/io/io_base_cls.py
  - cp_library/io/parser_cls.py
  isVerificationFile: false
  path: cp_library/alg/graph/set/graph_proto.py
  requiredBy:
  - cp_library/alg/graph/set/graph_set_cls.py
  timestamp: '2025-07-28 14:11:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/graph/set/graph_proto.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/set/graph_proto.py
- /library/cp_library/alg/graph/set/graph_proto.py.html
title: cp_library/alg/graph/set/graph_proto.py
---
