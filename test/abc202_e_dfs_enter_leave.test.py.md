---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/dfs_options_cls.py
    title: cp_library/alg/graph/dfs_options_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge_cls.py
    title: cp_library/alg/graph/edge_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/graph_cls.py
    title: cp_library/alg/graph/graph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/graph_proto.py
    title: cp_library/alg/graph/graph_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/lca_table_iterative_cls.py
    title: cp_library/alg/tree/lca_table_iterative_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_cls.py
    title: cp_library/alg/tree/tree_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_proto.py
    title: cp_library/alg/tree/tree_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/bit_cls.py
    title: cp_library/ds/bit_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/sparse_table_cls.py
    title: cp_library/ds/sparse_table_cls.py
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
    PROBLEM: https://atcoder.jp/contests/abc202/tasks/abc202_e
    links:
    - https://atcoder.jp/contests/abc202/tasks/abc202_e
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc202/tasks/abc202_e\n\
    \n\nfrom bisect import bisect_left\n\ndef main():\n    N = read(int)\n    P =\
    \ read(list[-1])\n    E = []\n    for u,p in enumerate(P, start=1):\n        E.append((p,u))\n\
    \n    cnt = [[] for _ in range(N)]\n\n    G = Tree(N, E)\n    depth = [0]*(N+1)\n\
    \    for p,u in G.dfs_topdown():\n        depth[u] = depth[p]+1\n    time = 0\n\
    \    tin = [0]*N\n    tout = [0]*N\n    \n    for event in G.dfs_enter_leave(0):\n\
    \        match event:\n            case DFSEvent.ENTER, u:\n                tin[u]\
    \ = time\n                cnt[depth[u]].append(time)\n                time +=\
    \ 1\n            case DFSEvent.LEAVE, u:\n                tout[u] = time\n   \
    \             time += 1\n    Q = read(int)\n    for u,d in read(list[tuple[-1,int],Q]):\n\
    \        ans = bisect_left(cnt[d], tout[u]) - bisect_left(cnt[d], tin[u])\n  \
    \      print(ans)\n\n    \n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library \
    \              \n'''\n\nfrom enum import auto, IntFlag, IntEnum\n\nclass DFSFlags(IntFlag):\n\
    \    ENTER = auto()\n    DOWN = auto()\n    BACK = auto()\n    CROSS = auto()\n\
    \    LEAVE = auto()\n    UP = auto()\n    MAXDEPTH = auto()\n\n    RETURN_PARENTS\
    \ = auto()\n    RETURN_DEPTHS = auto()\n    BACKTRACK = auto()\n    CONNECT_ROOTS\
    \ = auto()\n\n    # Common combinations\n    ALL_EDGES = DOWN | BACK | CROSS\n\
    \    EULER_TOUR = DOWN | UP\n    INTERVAL = ENTER | LEAVE\n    TOPDOWN = DOWN\
    \ | CONNECT_ROOTS\n    BOTTOMUP = UP | CONNECT_ROOTS\n    RETURN_ALL = RETURN_PARENTS\
    \ | RETURN_DEPTHS\n\nclass DFSEvent(IntEnum):\n    ENTER = DFSFlags.ENTER \n \
    \   DOWN = DFSFlags.DOWN \n    BACK = DFSFlags.BACK \n    CROSS = DFSFlags.CROSS\
    \ \n    LEAVE = DFSFlags.LEAVE \n    UP = DFSFlags.UP \n    MAXDEPTH = DFSFlags.MAXDEPTH\n\
    \    \n\n\nfrom io import TextIOBase\n\n\nimport sys\nimport typing\nfrom collections\
    \ import deque\nfrom numbers import Number\nfrom types import GenericAlias \n\
    from typing import Callable, Collection, Iterator, TypeAlias, TypeVar\n\nclass\
    \ TokenStream(Iterator):\n    def __init__(self, stream: TextIOBase = sys.stdin):\n\
    \        self.queue = deque()\n        self.stream = stream\n\n    def __next__(self):\n\
    \        if not self.queue: self.queue.extend(self.line())\n        return self.queue.popleft()\n\
    \    \n    def wait(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        while self.queue: yield\n        \n    def line(self):\n        assert\
    \ not self.queue\n        return sys.stdin.readline().split()\n\n    def n_uints(self,\
    \ n: int, shift = 0, max_digits: int = 20):\n        # sync buffers\n        tokens:\
    \ list[str] = []\n        while (lim := sys.stdin.buffer.tell() - sys.stdin.tell())\
    \ and len(tokens) < n:\n            residual_str: str = sys.stdin.readline(lim)\n\
    \            tokens.extend(residual_str.split())\n        \n        result = [0]\
    \ * n\n        pos = 0\n        \n        # Process residual string and check\
    \ for partial token\n        partial = None\n        if tokens:\n            if\
    \ not residual_str[-1].isspace():\n                partial = tokens.pop()\n  \
    \          for pos, token in enumerate(tokens):\n                result[pos] =\
    \ int(token)+shift\n            pos += 1\n        # Process remaining data token\
    \ by token\n        stdin_buffer = sys.stdin.buffer\n        num = int(partial)\
    \ if partial else 0\n        have_digit = partial is not None\n\n        original_chunk_size\
    \ = sys.stdin._CHUNK_SIZE\n        sys.stdin._CHUNK_SIZE = max(original_chunk_size,\
    \ max_digits * (n - pos))\n        \n        while pos < n:\n            byte\
    \ = stdin_buffer.read(1)\n\n            match byte[0]:\n                case 10\
    \ | 32:\n                    if have_digit:\n                        result[pos]\
    \ = num+shift\n                        pos += 1\n                        num =\
    \ 0\n                        have_digit = False\n                case char:  #\
    \ digit\n                    num = (num * 10) + (char - 48)\n                \
    \    have_digit = True\n\n        if have_digit:\n            result[pos] = num+shift\n\
    \            pos += 1\n\n        sys.stdin._CHUNK_SIZE = original_chunk_size \n\
    \        if pos < n:\n            raise EOFError(f\"Only found {pos} numbers,\
    \ expected {n}\")\n            \n        return result\n    \n    def n_ints(self,\
    \ n: int, shift = 0, max_digits: int = 20):\n        # sync buffers\n        tokens:\
    \ list[str] = []\n        while (lim := sys.stdin.buffer.tell() - sys.stdin.tell())\
    \ and len(tokens) < n:\n            residual_str: str = sys.stdin.readline(lim)\n\
    \            tokens.extend(residual_str.split())\n        \n        result = [0]\
    \ * n\n        pos = 0\n        \n        # Process residual string and check\
    \ for partial token\n        partial = None\n        if tokens:\n            if\
    \ not residual_str[-1].isspace():\n                partial = tokens.pop()\n  \
    \          for pos, token in enumerate(tokens):\n                result[pos] =\
    \ int(token)+shift\n            pos += 1\n        # Process remaining data token\
    \ by token\n        stdin_buffer = sys.stdin.buffer\n        num = abs(int(partial))\
    \ if partial else 0\n        is_negative = partial and partial.startswith('-')\n\
    \        have_digit = partial is not None\n\n        original_chunk_size = sys.stdin._CHUNK_SIZE\n\
    \        sys.stdin._CHUNK_SIZE = max(original_chunk_size, max_digits * (n - pos))\n\
    \        \n        while pos < n:\n            byte = stdin_buffer.read(1)\n\n\
    \            match byte[0]:\n                case 10 | 32:\n                 \
    \   if have_digit:\n                        result[pos] = -num+shift if is_negative\
    \ else num+shift\n                        pos += 1\n                        num\
    \ = 0\n                        is_negative = False\n                        have_digit\
    \ = False\n                case 45:  # minus sign\n                    is_negative\
    \ = True\n                case char:  # digit\n                    num = (num\
    \ * 10) + (char - 48)\n                    have_digit = True\n\n        if have_digit:\n\
    \            result[pos] = -num+shift if is_negative else num+shift\n        \
    \    pos += 1\n\n        sys.stdin._CHUNK_SIZE = original_chunk_size \n      \
    \  if pos < n:\n            raise EOFError(f\"Only found {pos} numbers, expected\
    \ {n}\")\n            \n        return result\n\nclass CharStream(TokenStream):\n\
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
    \ type[T]|T=int) -> ParseFn[T]:\n        if isinstance(spec, (type, GenericAlias)):\n\
    \            cls = typing.get_origin(spec) or spec\n            args = typing.get_args(spec)\
    \ or tuple()\n            return Parser.compile_type(cls, args)\n        elif\
    \ isinstance(offset := spec, Number): \n            cls = type(spec)  \n     \
    \       def parse(ts: TokenStream):\n                return cls(next(ts)) + offset\n\
    \            return parse\n        elif isinstance(args := spec, tuple):     \
    \ \n            return Parser.compile_tuple(type(spec), args)\n        elif isinstance(args\
    \ := spec, Collection):  \n            return Parser.compile_collection(type(spec),\
    \ args)\n        else:\n            raise NotImplementedError()\n    \n    @staticmethod\n\
    \    def compile_line(cls: T, spec=int) -> ParseFn[T]:\n        fn = Parser.compile(spec)\n\
    \        def parse(ts: TokenStream):\n            return cls(fn(ts) for _ in ts.wait())\n\
    \        return parse\n    \n    # @staticmethod\n    # def compile_n_ints(cls:\
    \ T, N, shift = int) -> ParseFn[T]:\n    #     shift = shift if isinstance(shift,\
    \ int) else 0\n    #     def parse(ts: TokenStream):\n    #         return cls(ts.n_ints(N,\
    \ shift))\n    #     return parse\n\n    @staticmethod\n    def compile_repeat(cls:\
    \ T, spec, N) -> ParseFn[T]:\n        fn = Parser.compile(spec)\n        def parse(ts:\
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
    \            case [spec, int() as N]:\n                # if issubclass(spec, int)\
    \ or isinstance(spec, int):\n                #     return Parser.compile_n_ints(cls,\
    \ N, spec)\n                return Parser.compile_repeat(cls, spec, N)\n     \
    \       case _:\n                raise NotImplementedError()\n\n        \nclass\
    \ Parsable:\n    @classmethod\n    def compile(cls):\n        def parser(ts: TokenStream):\n\
    \            return cls(next(ts))\n        return parser\n\nclass Edge(tuple,\
    \ Parsable):\n    @classmethod\n    def compile(cls, I=-1):\n        def parse(ts:\
    \ TokenStream):\n            u,v = ts.line()\n            return cls((int(u)+I,int(v)+I))\n\
    \        return parse\n\ntry:\n    from __pypy__ import newlist_hint\nexcept:\n\
    \    def newlist_hint(hint):\n        return []\n    \ndef elist(est_len: int)\
    \ -> list:\n    return newlist_hint(est_len)\nfrom typing import Iterable, overload\n\
    from math import inf\n\nclass GraphProtocol(list, Parsable):\n    def __init__(G,\
    \ N: int, E: list = None, adj: Iterable = None):\n        G.N = N\n        if\
    \ E is not None:\n            G.M, G.E = len(E), E\n        if adj is not None:\n\
    \            super().__init__(adj)\n\n    def neighbors(G, v: int) -> Iterable[int]:\n\
    \        return G[v]\n    \n    def edge_ids(G) -> list[list[int]]: ...\n\n  \
    \  @overload\n    def distance(G) -> list[list[int]]: ...\n    @overload\n   \
    \ def distance(G, s: int = 0) -> list[int]: ...\n    @overload\n    def distance(G,\
    \ s: int, g: int) -> int: ...\n    def distance(G, s = None, g = None):\n    \
    \    match s, g:\n            case None, None:\n                return G.floyd_warshall()\n\
    \            case s, None:\n                return G.bfs(s)\n            case\
    \ s, g:\n                return G.bfs(s, g)\n\n    @overload\n    def bfs(G, s:\
    \ int|list = 0) -> list[int]: ...\n    @overload\n    def bfs(G, s: int|list,\
    \ g: int) -> int: ...\n    def bfs(G, s = 0, g = None):\n        D = [inf for\
    \ _ in range(G.N)]\n        q = deque([s] if isinstance(s, int) else s)\n    \
    \    for u in q: D[u] = 0\n        while q:\n            nd = D[u := q.popleft()]+1\n\
    \            if u == g: return D[u]\n            for v in G.neighbors(u):\n  \
    \              if nd < D[v]:\n                    D[v] = nd\n                \
    \    q.append(v)\n        return D if g is None else inf    \n    \n    \n   \
    \ def floyd_warshall(G) -> list[list[int]]:\n        D = [[inf]*G.N for _ in range(G.N)]\n\
    \n        for u in G:\n            D[u][u] = 0\n            for v in G.neighbors(u):\n\
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
    \        return edges\n\n    def dfs_topdown_indexed(G, s: int|list[int]|None\
    \ = None, connect_roots = False):\n        '''Returns list of (u,v) representing\
    \ u->v edges in order of top down discovery'''\n        stack = [0] * G.N\n  \
    \      vis: list[bool] = [False]*G.N\n        edges: list[tuple[int,int,int]]\
    \ = []\n\n        for r,s in enumerate(G.starts(s)):\n            if vis[s]: continue\n\
    \            if connect_roots:\n                edges.append((r,-1,s))\n     \
    \       vis[s] = True\n            stack[idx := 0] = s\n            while idx\
    \ != -1:\n                u, idx = stack[idx], idx-1\n                for c,v\
    \ in enumerate(G[u]):\n                    if vis[v]: continue\n             \
    \       vis[v] = True\n                    edges.append((c,u,v))\n           \
    \         stack[idx := idx+1] = v \n\n        return edges\n    \n    def dfs_bottomup(G,\
    \ s: int|list[int]|None = None, connect_roots = False):\n        '''Returns list\
    \ of (p,u) representing p->u edges in bottom up order'''\n        edges = G.dfs_topdown(s,\
    \ connect_roots)\n        edges.reverse()\n        return edges\n    \n    def\
    \ starts(G, v: int|list[int]|None) -> Iterable:\n        match v:\n          \
    \  case int(v): return (v,)\n            case None: return range(G.N)\n      \
    \      case V: return V\n\n    @classmethod\n    def compile(cls, N: int, M: int,\
    \ E):\n        edge = Parser.compile(E)\n        def parse(ts: TokenStream):\n\
    \            return cls(N, [edge(ts) for _ in range(M)])\n        return parse\n\
    \    \n\nclass Graph(GraphProtocol):\n    def __init__(G, N: int, E: list[Edge]=[]):\n\
    \        super().__init__(N, E, ([] for _ in range(N)))\n        for u,v in G.E:\n\
    \            G[u].append(v)\n            G[v].append(u)\n\n    def edge_ids(G)\
    \ -> list[list[int]]:\n        Eid = [[] for _ in range(G.N)]\n        for e,(u,v)\
    \ in enumerate(G.E):\n            Eid[u].append(e)\n            Eid[v].append(e)\n\
    \        return Eid\n\n    @classmethod\n    def compile(cls, N: int, M: int,\
    \ E: type|int = Edge[-1]):\n        if isinstance(E, int): E = Edge[E]\n     \
    \   return super().compile(N, M, E)\n\nfrom typing import overload, Literal\n\
    from functools import cached_property\n\n\nfrom typing import Any, Callable, List\n\
    \nclass SparseTable:\n    def __init__(self, op: Callable[[Any, Any], Any], arr:\
    \ List[Any]):\n        self.n = len(arr)\n        self.log = self.n.bit_length()\n\
    \        self.op = op\n        self.st = [[None] * (self.n-(1<<i)+1) for i in\
    \ range(self.log)]\n        self.st[0] = arr[:]\n        \n        for i in range(self.log-1):\n\
    \            row, d = self.st[i], 1<<i\n            for j in range(len(self.st[i+1])):\n\
    \                self.st[i+1][j] = op(row[j], row[j+d])\n\n    def query(self,\
    \ l: int, r: int) -> Any:\n        k = (r-l).bit_length()-1\n        return self.op(self.st[k][l],\
    \ self.st[k][r-(1<<k)])\n    \n    def __repr__(self) -> str:\n        return\
    \ '\\n'.join(f'{i:<2d} {row}' for i,row in enumerate(self.st))\n\nclass BinaryIndexTree:\n\
    \    def __init__(self, v: int|list):\n        if isinstance(v, int):\n      \
    \      self.data, self.size = [0]*v, v\n        else:\n            self.build(v)\n\
    \n    def build(self, data):\n        self.data, self.size = data, len(data)\n\
    \        for i in range(self.size):\n            if (r := i|(i+1)) < self.size:\
    \ \n                self.data[r] += self.data[i]\n\n    def get(self, i: int):\n\
    \        assert 0 <= i < self.size\n        s = self.data[i]\n        z = i&(i+1)\n\
    \        for _ in range((i^z).bit_count()):\n            s, i = s-self.data[i-1],\
    \ i-(i&-i)\n        return s\n    \n    def set(self, i: int, x: int):\n     \
    \   self.add(i, x-self.get(i))\n        \n    def add(self, i: int, x: int) ->\
    \ None:\n        assert 0 <= i <= self.size\n        i += 1\n        data, size\
    \ = self.data, self.size\n        while i <= size:\n            data[i-1], i =\
    \ data[i-1] + x, i+(i&-i)\n\n    def pref_sum(self, i: int):\n        assert 0\
    \ <= i <= self.size\n        s = 0\n        data = self.data\n        for _ in\
    \ range(i.bit_count()):\n            s, i = s+data[i-1], i-(i&-i)\n        return\
    \ s\n    \n    def range_sum(self, l: int, r: int):\n        return self.pref_sum(r)\
    \ - self.pref_sum(l)\n\nclass LCATable(SparseTable):\n    def __init__(self, T,\
    \ root = 0):\n        self.start = [-1] * len(T)\n        self.end = [-1] * len(T)\n\
    \        self.euler = []\n        self.depth = []\n        \n        # Iterative\
    \ DFS\n        stack = [(root, -1, 0)]\n        while stack:\n            u, p,\
    \ d = stack.pop()\n            \n            if self.start[u] == -1:\n       \
    \         self.start[u] = len(self.euler)\n                \n                for\
    \ v in reversed(T[u]):\n                    if v != p:\n                     \
    \   stack.append((u, p, d))\n                        stack.append((v, u, d+1))\n\
    \                        \n            self.euler.append(u)\n            self.depth.append(d)\n\
    \            self.end[u] = len(self.euler)\n        super().__init__(min, list(zip(self.depth,\
    \ self.euler)))\n\n    def query(self, u, v) -> tuple[int,int]:\n        l, r\
    \ = min(self.start[u], self.start[v]), max(self.start[u], self.start[v])+1\n \
    \       d, a = super().query(l, r)\n        return a, d\n    \n    def distance(self,\
    \ u, v) -> int:\n        l, r = min(self.start[u], self.start[v]), max(self.start[u],\
    \ self.start[v])+1\n        d, _ = super().query(l, r)\n        return self.depth[l]\
    \ + self.depth[r] - 2*d\n        \n\nclass TreeProtocol(GraphProtocol):\n\n  \
    \  @cached_property\n    def lca(T):\n        return LCATable(T)\n    \n    @overload\n\
    \    def diameter(T) -> int: ...\n    @overload\n    def diameter(T, endpoints:\
    \ Literal[True]) -> tuple[int,int,int]: ...\n    def diameter(T, endpoints = False):\n\
    \        _, s = max((d,v) for v,d in enumerate(T.dfs(0)))\n        diam, g = max((d,v)\
    \ for v,d in enumerate(T.dfs(s)))\n        return (diam, s, g) if endpoints else\
    \ diam\n    \n    @overload\n    def distance(T) -> list[list[int]]: ...\n   \
    \ @overload\n    def distance(T, s: int = 0) -> list[int]: ...\n    @overload\n\
    \    def distance(T, s: int, g: int) -> int: ...\n    def distance(T, s = None,\
    \ g = None):\n        match s, g:\n            case None, None:\n            \
    \    return [T.dfs(u) for u in range(T.N)]\n            case s, g:\n         \
    \       return T.dfs(s, g)\n            \n    @overload\n    def dfs(T, s: int\
    \ = 0) -> list[int]: ...\n    @overload\n    def dfs(T, s: int, g: int) -> int:\
    \ ...\n    def dfs(T, s = 0, g = None):\n        D = [inf for _ in range(T.N)]\n\
    \        D[s] = 0\n        state = [True for _ in range(T.N)]\n        stack =\
    \ [s]\n\n        while stack:\n            u = stack.pop()\n            if u ==\
    \ g: return D[u]\n            state[u] = False\n            for v in T[u]:\n \
    \               if state[v]:\n                    D[v] = D[u]+1\n            \
    \        stack.append(v)\n        return D if g is None else inf \n\n\n    def\
    \ dfs_events(G, opts: DFSFlags, s: int = 0):         \n        events = []\n \
    \       # stack = deque([(s,-1)], maxlen=G.N)\n        stack = [(s,-1)]\n    \
    \    adj = [None]*G.N\n\n\n        while stack:\n            u, p = stack[-1]\n\
    \            \n            if adj[u] is None:\n                adj[u] = iter(G.neighbors(u))\n\
    \                if DFSFlags.ENTER in opts:\n                    events.append((DFSEvent.ENTER,\
    \ u))\n            \n            if (v := next(adj[u], None)) is not None:\n \
    \               if v == p:\n                    if DFSFlags.BACK in opts:\n  \
    \                      events.append((DFSEvent.BACK, u, v))\n                else:\n\
    \                    if DFSFlags.DOWN in opts:\n                        events.append((DFSEvent.DOWN,\
    \ u, v))\n                    stack.append((v,u))\n            else:\n       \
    \         stack.pop()\n\n                if DFSFlags.LEAVE in opts:\n        \
    \            events.append((DFSEvent.LEAVE, u))\n                if p != -1 and\
    \ DFSFlags.UP in opts:\n                    events.append((DFSEvent.UP, u, p))\n\
    \        return events\n\nclass Tree(Graph, TreeProtocol):\n    @classmethod\n\
    \    def compile(cls, N: int, E: type|int = Edge[-1]):\n        return super().compile(N,\
    \ N-1, E)\n    \n    \n\nfrom typing import Type, TypeVar, overload\n\nT = TypeVar('T')\n\
    @overload\ndef read() -> list[int]: ...\n@overload\ndef read(spec: int|None) ->\
    \ list[int]: ...\n@overload\ndef read(spec: Type[T]|T, char=False) -> T: ...\n\
    def read(spec: Type[T]|T=None, char=False):\n    match spec, char:\n        case\
    \ None, False:\n            return list(map(int, input().split()))\n        case\
    \ int(offset), False:\n            return [int(s)+offset for s in input().split()]\n\
    \        case _, _:\n            if char:\n                stream = CharStream()\n\
    \            else:\n                stream = TokenStream()\n            parser:\
    \ T = Parser.compile(spec)\n            return parser(stream)\n\nif __name__ ==\
    \ \"__main__\":\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc202/tasks/abc202_e\n\
    \n\nfrom bisect import bisect_left\n\ndef main():\n    N = read(int)\n    P =\
    \ read(list[-1])\n    E = []\n    for u,p in enumerate(P, start=1):\n        E.append((p,u))\n\
    \n    cnt = [[] for _ in range(N)]\n\n    G = Tree(N, E)\n    depth = [0]*(N+1)\n\
    \    for p,u in G.dfs_topdown():\n        depth[u] = depth[p]+1\n    time = 0\n\
    \    tin = [0]*N\n    tout = [0]*N\n    \n    for event in G.dfs_enter_leave(0):\n\
    \        match event:\n            case DFSEvent.ENTER, u:\n                tin[u]\
    \ = time\n                cnt[depth[u]].append(time)\n                time +=\
    \ 1\n            case DFSEvent.LEAVE, u:\n                tout[u] = time\n   \
    \             time += 1\n    Q = read(int)\n    for u,d in read(list[tuple[-1,int],Q]):\n\
    \        ans = bisect_left(cnt[d], tout[u]) - bisect_left(cnt[d], tin[u])\n  \
    \      print(ans)\n\n    \nfrom cp_library.alg.graph.dfs_options_cls import DFSEvent\n\
    from cp_library.alg.tree.tree_cls import Tree\nfrom cp_library.io.read_specs_fn\
    \ import read\n\nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - cp_library/alg/graph/dfs_options_cls.py
  - cp_library/alg/tree/tree_cls.py
  - cp_library/io/read_specs_fn.py
  - cp_library/alg/graph/edge_cls.py
  - cp_library/alg/graph/graph_cls.py
  - cp_library/alg/tree/tree_proto.py
  - cp_library/io/parser_cls.py
  - cp_library/alg/graph/graph_proto.py
  - cp_library/alg/tree/lca_table_iterative_cls.py
  - cp_library/ds/elist_fn.py
  - cp_library/ds/sparse_table_cls.py
  - cp_library/ds/bit_cls.py
  isVerificationFile: true
  path: test/abc202_e_dfs_enter_leave.test.py
  requiredBy: []
  timestamp: '2024-11-16 19:58:23+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/abc202_e_dfs_enter_leave.test.py
layout: document
redirect_from:
- /verify/test/abc202_e_dfs_enter_leave.test.py
- /verify/test/abc202_e_dfs_enter_leave.test.py.html
title: test/abc202_e_dfs_enter_leave.test.py
---
