---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: cp_library/alg/graph/dfs_options_cls.py
    title: cp_library/alg/graph/dfs_options_cls.py
  - icon: ':warning:'
    path: cp_library/alg/graph/fast/graph_base_cls.py
    title: cp_library/alg/graph/fast/graph_base_cls.py
  - icon: ':warning:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  - icon: ':warning:'
    path: cp_library/ds/fill_fn.py
    title: cp_library/ds/fill_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':warning:'
    path: cp_library/math/inft_cnst.py
    title: cp_library/math/inft_cnst.py
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/alg/tree/fast/tree_cls.py
    title: cp_library/alg/tree/fast/tree_cls.py
  - icon: ':warning:'
    path: cp_library/alg/tree/fast/tree_weighted_base_cls.py
    title: cp_library/alg/tree/fast/tree_weighted_base_cls.py
  - icon: ':warning:'
    path: cp_library/alg/tree/fast/tree_weighted_cls.py
    title: cp_library/alg/tree/fast/tree_weighted_cls.py
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
    from typing import Callable, TypeVar\nfrom typing import Callable, Sequence, Union,\
    \ overload\nfrom collections import deque\n\nimport typing\nfrom numbers import\
    \ Number\nfrom types import GenericAlias \nfrom typing import Callable, Collection,\
    \ Iterator, TypeVar, Union\nimport os\nimport sys\nfrom io import BytesIO, IOBase\n\
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
    \ TokenStream):\n            return cls(next(ts))\n        return parser\n\nfrom\
    \ enum import auto, IntFlag, IntEnum\n\nclass DFSFlags(IntFlag):\n    ENTER =\
    \ auto()\n    DOWN = auto()\n    BACK = auto()\n    CROSS = auto()\n    LEAVE\
    \ = auto()\n    UP = auto()\n    MAXDEPTH = auto()\n\n    RETURN_PARENTS = auto()\n\
    \    RETURN_DEPTHS = auto()\n    BACKTRACK = auto()\n    CONNECT_ROOTS = auto()\n\
    \n    # Common combinations\n    ALL_EDGES = DOWN | BACK | CROSS\n    EULER_TOUR\
    \ = DOWN | UP\n    INTERVAL = ENTER | LEAVE\n    TOPDOWN = DOWN | CONNECT_ROOTS\n\
    \    BOTTOMUP = UP | CONNECT_ROOTS\n    RETURN_ALL = RETURN_PARENTS | RETURN_DEPTHS\n\
    \nclass DFSEvent(IntEnum):\n    ENTER = DFSFlags.ENTER \n    DOWN = DFSFlags.DOWN\
    \ \n    BACK = DFSFlags.BACK \n    CROSS = DFSFlags.CROSS \n    LEAVE = DFSFlags.LEAVE\
    \ \n    UP = DFSFlags.UP \n    MAXDEPTH = DFSFlags.MAXDEPTH\n    \n\nclass GraphBase(Sequence,\
    \ Parsable):\n    def __init__(self, N: int, M: int, U: list[int], V: list[int],\
    \ \n                 deg: list[int], La: list[int], Ra: list[int],\n         \
    \        Ua: list[int], Va: list[int], Ea: list[int]):\n        self.N = N\n \
    \       \"\"\"The number of vertices.\"\"\"\n        self.M = M\n        \"\"\"\
    The number of edges.\"\"\"\n        self.U = U\n        \"\"\"A list of source\
    \ vertices in the original edge list.\"\"\"\n        self.V = V\n        \"\"\"\
    A list of destination vertices in the original edge list.\"\"\"\n        self.deg\
    \ = deg\n        \"\"\"deg[u] is the out degree of vertex u.\"\"\"\n        self.La\
    \ = La\n        \"\"\"La[u] stores the start index of the list of adjacent vertices\
    \ from u.\"\"\"\n        self.Ra = Ra\n        \"\"\"Ra[u] stores the stop index\
    \ of the list of adjacent vertices from u.\"\"\"\n        self.Ua = Ua\n     \
    \   \"\"\"Ua[i] = u for La[u] <= i < Ra[u], useful for backtracking.\"\"\"\n \
    \       self.Va = Va\n        \"\"\"Va[i] lists adjacent vertices to u for La[u]\
    \ <= i < Ra[u].\"\"\"\n        self.Ea = Ea\n        \"\"\"Ea[i] lists the edge\
    \ ids that start from u for La[u] <= i < Ra[u].\n        For undirected graphs,\
    \ edge ids in range M<= e <2*M are edges from V[e-M] -> U[e-M].\n        \"\"\"\
    \n\n    def __len__(G) -> int:\n        return G.N\n\n    def __getitem__(G, u):\n\
    \        l,r = G.La[u],G.Ra[u]\n        return G.Va[l:r]\n    \n    def range(G,\
    \ u):\n        return range(G.La[u],G.Ra[u])\n    \n    @overload\n    def distance(G)\
    \ -> list[list[int]]: ...\n    @overload\n    def distance(G, s: int = 0) -> list[int]:\
    \ ...\n    @overload\n    def distance(G, s: int, g: int) -> int: ...\n    def\
    \ distance(G, s = None, g = None):\n        match s, g:\n            case None,\
    \ None:\n                return G.floyd_warshall()\n            case s, g:\n \
    \               return G.bfs(s, g)\n\n    @overload\n    def bfs(G, s: Union[int,list]\
    \ = 0) -> list[int]: ...\n    @overload\n    def bfs(G, s: Union[int,list], g:\
    \ int) -> int: ...\n    def bfs(G, s: int = 0, g: int = None):\n        N, Va\
    \ = G.N, G.Va\n        D = [inft]*N\n        S = G.starts(s)\n        que = deque(S)\n\
    \        for u in S: D[u] = 0\n        while que:\n            nd = D[u := que.popleft()]+1\n\
    \            if u == g: return nd-1\n            for i in G.range(u):\n      \
    \          if nd < D[v := Va[i]]:\n                    D[v] = nd\n           \
    \         que.append(v)\n        return D if g is None else inft \n\n    def floyd_warshall(G)\
    \ -> list[list[int]]:\n        N, M = G.N, G.M\n        Ua, Va = G.Ua, G.Va\n\
    \        D = [[inft]*N for _ in range(N)]\n\n        for u in range(N):\n    \
    \        D[u][u] = 0\n\n        for i in range(M):\n            u,v = Ua[i], Va[i]\n\
    \            D[u][v] = 1\n        \n        for k, Dk in enumerate(D):\n     \
    \       for Di in D:\n                if Di[k] == inft: continue\n           \
    \     for j in range(N):\n                    if Dk[j] == inft: continue\n   \
    \                 Di[j] = min(Di[j], Di[k]+Dk[j])\n        return D\n    \n\n\
    \    def dfs_discovery(G, s: Union[int,list[int],None] = None, include_roots =\
    \ False):\n        '''Returns lists U and V representing U[i] -> V[i] edges in\
    \ order of top down discovery'''\n        N, Va = G.N, G.Va\n        vis = [False]*N\n\
    \        stack: list[int] = elist(N)\n        order: list[int] = elist(N)\n\n\
    \        for s in G.starts(s):\n            if vis[s]: continue\n            if\
    \ include_roots:\n                order.append(-s-1)\n            vis[s] = True\n\
    \            stack.append(s)\n            while stack:\n                u = stack.pop()\n\
    \                for i in G.range(u):\n                    v = Va[i]\n       \
    \             if vis[v]: continue\n                    vis[v] = True\n       \
    \             order.append(i)\n                    stack.append(v)\n        return\
    \ order\n\n    def dfs(G, s: int|list = None, /,\n            connect_roots =\
    \ False, backtrack = False, max_depth = None,\n            enter_fn: Callable[[int],None]\
    \ = None,\n            leave_fn: Callable[[int],None] = None,\n            max_depth_fn:\
    \ Callable[[int],None] = None,\n            down_fn: Callable[[int,int],None]\
    \ = None, \n            back_fn: Callable[[int,int],None] = None,\n          \
    \  up_fn: Callable[[int,int],None] = None):\n        Va, La, Ra, I = G.Va, G.La,\
    \ G.Ra, G.La[:]\n\n        state = [0]*G.N\n        stack = elist(G.N if max_depth\
    \ is None else max_depth+1)\n        for s in G.starts(s):\n            if state[s]:\
    \ continue\n            stack.append(s)\n            state[s] = 1\n          \
    \  if connect_roots and down_fn: down_fn(-1,s)\n            while stack:\n   \
    \             u = stack[-1]\n                if state[u] == 1:\n             \
    \       state[u] = 2\n                    if enter_fn: enter_fn(u)\n         \
    \           if max_depth is not None and len(stack) > max_depth:\n           \
    \             I[u] = Ra[u]\n                        if max_depth_fn: max_depth_fn(u)\n\
    \n                if (i := I[u]) < Ra[u]:\n                    I[u] += 1\n   \
    \                 if state[v := Va[i]]:\n                        if back_fn: back_fn(u,v)\n\
    \                    else:\n                        stack.append(v)\n        \
    \                state[v] = 1\n                        if down_fn: down_fn(u,v)\n\
    \                else:\n                    stack.pop()\n                    if\
    \ backtrack:\n                        state[u] = 0\n                        I[u]\
    \ = La[u]\n                    if leave_fn: leave_fn(u)\n                    if\
    \ up_fn: up_fn(u, stack[-1])\n            if connect_roots and up_fn: up_fn(s,\
    \ -1)\n\n    \n    def dfs_enter_leave(G, s: Union[int,list[int],None] = None):\n\
    \        '''Returns lists U and V representing U[i] -> V[i] edges in order of\
    \ top down discovery'''\n        N, La, Ra, Va = G.N, G.La, G.Ra, G.Va\n     \
    \   I = La[:]\n        stack: list[int] = elist(N)\n        order: list[int] =\
    \ elist(2*N)\n        events: list[DFSEvent] = elist(2*N)\n        G.par = par\
    \ = [-1]*N\n        ENTER, LEAVE = int(DFSEvent.ENTER), int(DFSEvent.LEAVE)\n\n\
    \        for s in G.starts(s):\n            if par[s] >= 0: continue\n       \
    \     par[s] = s\n            order.append(s)\n            events.append(ENTER)\n\
    \            stack.append(s)\n            while stack:\n                u = stack[-1]\n\
    \                if (i := I[u]) < Ra[u]:\n                    I[u] += 1\n    \
    \                if par[v := Va[i]] >= 0: continue\n                    par[v]\
    \ = u\n                    order.append(v)\n                    events.append(ENTER)\n\
    \                    stack.append(v)\n                else:\n                \
    \    stack.pop()\n                    order.append(u)\n                    events.append(LEAVE)\n\
    \            par[s] = s\n        return events, order\n    \n    def is_bipartite(G):\n\
    \        N, Va = G.N, G.Va\n        que = deque()\n        color = [-1]*N\n  \
    \              \n        for s in range(N):\n            if color[s] >= 0:\n \
    \               continue\n            color[s] = 1\n            que.append(s)\n\
    \            while que:\n                u = que.popleft()\n                for\
    \ i in G.range(u):\n                    if color[v := Va[i]] == -1:\n        \
    \                color[v] = 1 - color[u]\n                        que.append(v)\n\
    \                    elif color[v] == color[u]:\n                        return\
    \ False\n        return True\n    \n    def starts(G, s: Union[int,list[int],None])\
    \ -> list[int]:\n        match s:\n            case int(s): return [s]\n     \
    \       case None: return [*range(G.N)]\n            case V: return V if isinstance(V,\
    \ list) else list(V)\n\n    @classmethod\n    def compile(cls, N: int, M: int,\
    \ shift: int = -1):\n        def parse(ts: TokenStream):\n            U, V = fill_u32(M),\
    \ fill_u32(M)\n            stream = ts.stream\n            for i in range(M):\n\
    \                u, v = map(int, stream.readline().split())\n                U[i],\
    \ V[i] = u+shift, v+shift\n            return cls(N, U, V)\n        return parse\n\
    \    \n\n\ndef elist(est_len: int) -> list: ...\ntry:\n    from __pypy__ import\
    \ newlist_hint\nexcept:\n    def newlist_hint(hint):\n        return []\nelist\
    \ = newlist_hint\n    \nfrom array import array\n\ndef fill_i32(N: int, elm: int\
    \ = 0):\n    return array('i', (elm,)) * N\n\ndef fill_u32(N: int, elm: int =\
    \ 0):\n    return array('I', (elm,)) * N\n\ndef fill_i64(N: int, elm: int = 0):\n\
    \    return array('q', (elm,)) * N\n\ndef fill_u64(N: int, elm: int = 0):\n  \
    \  return array('Q', (elm,)) * N\n\ninft: int\n\ninft = sys.maxsize\n\n_T = TypeVar('_T')\n\
    \nclass TreeBase(GraphBase):\n\n    def rerooting_dp(T, e: _T, \n            \
    \         merge: Callable[[_T,_T],_T], \n                     add_child: Callable[[int,int,int,_T],_T]\
    \ = lambda p,c,i,s:s,\n                     s: int = 0):\n        N, La, Ra, Ua,\
    \ Va = T.N, T.La, T.Ra, T.Ua, T.Va\n        order = T.dfs_discovery(s)\n     \
    \   dp = [e]*N\n        suf = [e]*len(Ua)\n        I = Ra[:] # tracks current\
    \ indices for suffix array accumulation\n\n        # up\n        for i in order[::-1]:\n\
    \            u,v = Ua[i], Va[i]\n            # subtree v finished up pass, store\
    \ value to accumulate for u\n            dp[v] = new = add_child(u, v, i, dp[v])\n\
    \            dp[u] = merge(dp[u], new)\n            # suffix accumulation\n  \
    \          I[u] -= 1\n            if I[u] > La[u]:\n                suf[I[u]-1]\
    \ = merge(suf[I[u]], new)\n\n        # down\n        dp[s] = e\n        for i\
    \ in order:\n            u,v = Ua[i], Va[i]\n            # prefix accumulation\n\
    \            dp[u] = merge(pre := dp[u], dp[v])\n            # push value to child\n\
    \            dp[v] = add_child(v, u, i, merge(suf[I[u]], pre))\n            I[u]\
    \ += 1\n        \n        return dp\n    \n    def euler_tour(T, s = 0):\n   \
    \     N, Va = len(T), T.Va\n        tin, tout, par = [-1]*N,[-1]*N,[-1]*N\n  \
    \      order, delta = elist(2*N), elist(2*N)\n        \n        stack = elist(N)\n\
    \        stack.append(s)\n        while stack:\n            p = par[u := stack.pop()]\n\
    \            if tin[u] == -1:\n                tin[u] = len(order)\n         \
    \       for i in T.range(u):\n                    if (v := Va[i]) != p:\n    \
    \                    par[v] = u\n                        stack.append(u)\n   \
    \                     stack.append(v)\n                delta.append(1)\n     \
    \       else:\n                delta.append(-1)\n            \n            order.append(u)\n\
    \            tout[u] = len(order)\n        delta[0] = delta[-1] = 0\n        T.tin,\
    \ T.tout, T.par = tin, tout, par\n        T.order, T.delta = order, delta\n\n\
    \    def hld_precomp(T, r = 0):\n        N, time, Va = T.N, 0, T.Va\n        tin,\
    \ tout, size = [0]*N, [0]*N, [1]*N+[0]\n        par, heavy, head = [-1]*N, [-1]*N,\
    \ [r]*N\n        depth, order, state = [0]*N, [0]*N, [0]*N\n        stack = elist(N)\n\
    \        stack.append(r)\n        while stack:\n            match state[v := stack.pop()]:\n\
    \                case 0: # dfs down\n                    p, state[v] = par[v],\
    \ 1\n                    stack.append(v)\n                    for i in T.range(v):\n\
    \                        if (c := Va[i]) != p:\n                            depth[c],\
    \ par[c] = depth[v]+1, v\n                            stack.append(c)\n\n    \
    \            case 1: # dfs up\n                    p, l = par[v], -1\n       \
    \             for i in T.range(v):\n                        if (c := Va[i]) !=\
    \ p:\n                            size[v] += size[c]\n                       \
    \     if size[c] > size[l]:\n                                l = c\n         \
    \           heavy[v] = l\n                    if p == -1:\n                  \
    \      state[v] = 2\n                        stack.append(v)\n\n             \
    \   case 2: # decompose down\n                    p, h, l = par[v], head[v], heavy[v]\n\
    \                    tin[v], order[time], state[v] = time, v, 3\n            \
    \        time += 1\n                    stack.append(v)\n                    \n\
    \                    for i in T.range(v):\n                        if (c := Va[i])\
    \ != p and c != l:\n                            head[c], state[c] = c, 2\n   \
    \                         stack.append(c)\n\n                    if l != -1:\n\
    \                        head[l], state[l] = h, 2\n                        stack.append(l)\n\
    \                case 3: # decompose up\n                    tout[v] = time\n\
    \        T.size, T.depth = size, depth\n        T.order, T.tin, T.tout = order,\
    \ tin, tout\n        T.par, T.heavy, T.head = par, heavy, head\n\n    @classmethod\n\
    \    def compile(cls, N: int, shift: int = -1):\n        return super().compile(N,\
    \ N-1, shift)\n    \n"
  code: "import cp_library.alg.graph.__header__\nfrom typing import Callable, TypeVar\n\
    from cp_library.alg.graph.fast.graph_base_cls import GraphBase\n\n_T = TypeVar('_T')\n\
    \nclass TreeBase(GraphBase):\n\n    def rerooting_dp(T, e: _T, \n            \
    \         merge: Callable[[_T,_T],_T], \n                     add_child: Callable[[int,int,int,_T],_T]\
    \ = lambda p,c,i,s:s,\n                     s: int = 0):\n        N, La, Ra, Ua,\
    \ Va = T.N, T.La, T.Ra, T.Ua, T.Va\n        order = T.dfs_discovery(s)\n     \
    \   dp = [e]*N\n        suf = [e]*len(Ua)\n        I = Ra[:] # tracks current\
    \ indices for suffix array accumulation\n\n        # up\n        for i in order[::-1]:\n\
    \            u,v = Ua[i], Va[i]\n            # subtree v finished up pass, store\
    \ value to accumulate for u\n            dp[v] = new = add_child(u, v, i, dp[v])\n\
    \            dp[u] = merge(dp[u], new)\n            # suffix accumulation\n  \
    \          I[u] -= 1\n            if I[u] > La[u]:\n                suf[I[u]-1]\
    \ = merge(suf[I[u]], new)\n\n        # down\n        dp[s] = e\n        for i\
    \ in order:\n            u,v = Ua[i], Va[i]\n            # prefix accumulation\n\
    \            dp[u] = merge(pre := dp[u], dp[v])\n            # push value to child\n\
    \            dp[v] = add_child(v, u, i, merge(suf[I[u]], pre))\n            I[u]\
    \ += 1\n        \n        return dp\n    \n    def euler_tour(T, s = 0):\n   \
    \     N, Va = len(T), T.Va\n        tin, tout, par = [-1]*N,[-1]*N,[-1]*N\n  \
    \      order, delta = elist(2*N), elist(2*N)\n        \n        stack = elist(N)\n\
    \        stack.append(s)\n        while stack:\n            p = par[u := stack.pop()]\n\
    \            if tin[u] == -1:\n                tin[u] = len(order)\n         \
    \       for i in T.range(u):\n                    if (v := Va[i]) != p:\n    \
    \                    par[v] = u\n                        stack.append(u)\n   \
    \                     stack.append(v)\n                delta.append(1)\n     \
    \       else:\n                delta.append(-1)\n            \n            order.append(u)\n\
    \            tout[u] = len(order)\n        delta[0] = delta[-1] = 0\n        T.tin,\
    \ T.tout, T.par = tin, tout, par\n        T.order, T.delta = order, delta\n\n\
    \    def hld_precomp(T, r = 0):\n        N, time, Va = T.N, 0, T.Va\n        tin,\
    \ tout, size = [0]*N, [0]*N, [1]*N+[0]\n        par, heavy, head = [-1]*N, [-1]*N,\
    \ [r]*N\n        depth, order, state = [0]*N, [0]*N, [0]*N\n        stack = elist(N)\n\
    \        stack.append(r)\n        while stack:\n            match state[v := stack.pop()]:\n\
    \                case 0: # dfs down\n                    p, state[v] = par[v],\
    \ 1\n                    stack.append(v)\n                    for i in T.range(v):\n\
    \                        if (c := Va[i]) != p:\n                            depth[c],\
    \ par[c] = depth[v]+1, v\n                            stack.append(c)\n\n    \
    \            case 1: # dfs up\n                    p, l = par[v], -1\n       \
    \             for i in T.range(v):\n                        if (c := Va[i]) !=\
    \ p:\n                            size[v] += size[c]\n                       \
    \     if size[c] > size[l]:\n                                l = c\n         \
    \           heavy[v] = l\n                    if p == -1:\n                  \
    \      state[v] = 2\n                        stack.append(v)\n\n             \
    \   case 2: # decompose down\n                    p, h, l = par[v], head[v], heavy[v]\n\
    \                    tin[v], order[time], state[v] = time, v, 3\n            \
    \        time += 1\n                    stack.append(v)\n                    \n\
    \                    for i in T.range(v):\n                        if (c := Va[i])\
    \ != p and c != l:\n                            head[c], state[c] = c, 2\n   \
    \                         stack.append(c)\n\n                    if l != -1:\n\
    \                        head[l], state[l] = h, 2\n                        stack.append(l)\n\
    \                case 3: # decompose up\n                    tout[v] = time\n\
    \        T.size, T.depth = size, depth\n        T.order, T.tin, T.tout = order,\
    \ tin, tout\n        T.par, T.heavy, T.head = par, heavy, head\n\n    @classmethod\n\
    \    def compile(cls, N: int, shift: int = -1):\n        return super().compile(N,\
    \ N-1, shift)\n    \nfrom cp_library.ds.elist_fn import elist"
  dependsOn:
  - cp_library/alg/graph/fast/graph_base_cls.py
  - cp_library/ds/elist_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/alg/graph/dfs_options_cls.py
  - cp_library/ds/fill_fn.py
  - cp_library/math/inft_cnst.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: false
  path: cp_library/alg/tree/fast/tree_base_cls.py
  requiredBy:
  - cp_library/alg/tree/fast/tree_weighted_cls.py
  - cp_library/alg/tree/fast/tree_weighted_base_cls.py
  - cp_library/alg/tree/fast/tree_cls.py
  timestamp: '2024-12-17 21:59:33+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/tree/fast/tree_base_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/tree/fast/tree_base_cls.py
- /library/cp_library/alg/tree/fast/tree_base_cls.py.html
title: cp_library/alg/tree/fast/tree_base_cls.py
---