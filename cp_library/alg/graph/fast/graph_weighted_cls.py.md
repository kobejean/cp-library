---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/bellman_ford_fn.py
    title: cp_library/alg/graph/bellman_ford_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/dfs_options_cls.py
    title: cp_library/alg/graph/dfs_options_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/fast/graph_base_cls.py
    title: cp_library/alg/graph/fast/graph_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/fast/graph_weighted_base_cls.py
    title: cp_library/alg/graph/fast/graph_weighted_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/argsort_fn.py
    title: cp_library/alg/iter/argsort_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/dsu_cls.py
    title: cp_library/ds/dsu_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/fill_fn.py
    title: cp_library/ds/fill_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/heap_proto.py
    title: cp_library/ds/heap/heap_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/heapq_max_import.py
    title: cp_library/ds/heap/heapq_max_import.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/priority_queue_cls.py
    title: cp_library/ds/heap/priority_queue_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/inft_cnst.py
    title: cp_library/math/inft_cnst.py
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/fast/tree_weighted_cls.py
    title: cp_library/alg/tree/fast/tree_weighted_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/abc294_g_fast_tree_heavy_light_decomposition.test.py
    title: test/abc294_g_fast_tree_heavy_light_decomposition.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc294_g_fast_tree_lca_table_weighted_bit.test.py
    title: test/abc294_g_fast_tree_lca_table_weighted_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/minimum_spanning_tree_kruskal.test.py
    title: test/minimum_spanning_tree_kruskal.test.py
  - icon: ':heavy_check_mark:'
    path: test/minimum_spanning_tree_kruskal_heap.test.py
    title: test/minimum_spanning_tree_kruskal_heap.test.py
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
    from typing import overload\n\nimport typing\nfrom collections import deque\n\
    from numbers import Number\nfrom types import GenericAlias \nfrom typing import\
    \ Callable, Collection, Iterator, TypeVar, Union\nimport os\nimport sys\nfrom\
    \ io import BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n    BUFSIZE = 8192\n \
    \   newlines = 0\n\n    def __init__(self, file):\n        self._fd = file.fileno()\n\
    \        self.buffer = BytesIO()\n        self.writable = \"x\" in file.mode or\
    \ \"r\" not in file.mode\n        self.write = self.buffer.write if self.writable\
    \ else None\n\n    def read(self):\n        BUFSIZE = self.BUFSIZE\n        while\
    \ True:\n            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))\n\
    \            if not b:\n                break\n            ptr = self.buffer.tell()\n\
    \            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)\n\
    \        self.newlines = 0\n        return self.buffer.read()\n\n    def readline(self):\n\
    \        BUFSIZE = self.BUFSIZE\n        while self.newlines == 0:\n         \
    \   b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))\n        \
    \    self.newlines = b.count(b\"\\n\") + (not b)\n            ptr = self.buffer.tell()\n\
    \            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)\n\
    \        self.newlines -= 1\n        return self.buffer.readline()\n\n    def\
    \ flush(self):\n        if self.writable:\n            os.write(self._fd, self.buffer.getvalue())\n\
    \            self.buffer.truncate(0), self.buffer.seek(0)\n\n\nclass IOWrapper(IOBase):\n\
    \    stdin: 'IOWrapper' = None\n    stdout: 'IOWrapper' = None\n    \n    def\
    \ __init__(self, file):\n        self.buffer = FastIO(file)\n        self.flush\
    \ = self.buffer.flush\n        self.writable = self.buffer.writable\n\n    def\
    \ write(self, s):\n        return self.buffer.write(s.encode(\"ascii\"))\n   \
    \ \n    def read(self):\n        return self.buffer.read().decode(\"ascii\")\n\
    \    \n    def readline(self):\n        return self.buffer.readline().decode(\"\
    ascii\")\n\nsys.stdin = IOWrapper.stdin = IOWrapper(sys.stdin)\nsys.stdout = IOWrapper.stdout\
    \ = IOWrapper(sys.stdout)\n\n\nclass TokenStream(Iterator):\n    stream = IOWrapper.stdin\n\
    \n    def __init__(self):\n        self.queue = deque()\n\n    def __next__(self):\n\
    \        if not self.queue: self.queue.extend(self.line())\n        return self.queue.popleft()\n\
    \    \n    def wait(self):\n        if not self.queue: self.queue.extend(self.line())\n\
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
    def argsort(A: list[int]):\n    N = len(A)\n    mask = (1 << (shift := N.bit_length()))\
    \ - 1\n    indices = [0]*N\n    for i in range(N):\n        indices[i] = A[i]\
    \ << shift | i\n    indices.sort()\n    for i in range(N):\n        indices[i]\
    \ &= mask\n    return indices\nfrom typing import Callable, Sequence, Union, overload\n\
    \nfrom enum import auto, IntFlag, IntEnum\n\nclass DFSFlags(IntFlag):\n    ENTER\
    \ = auto()\n    DOWN = auto()\n    BACK = auto()\n    CROSS = auto()\n    LEAVE\
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
    \  return array('Q', (elm,)) * N\n\ninft: int\n\ninft = sys.maxsize\n\nclass GraphWeightedBase(GraphBase):\n\
    \    def __init__(self, N: int, M: int, U: list[int], V: list[int], W: list[int],\
    \ \n                 deg: list[int], La: list[int], Ra: list[int],\n         \
    \        Ua: list[int], Va: list[int], Wa: list[int], Ea: list[int]):\n      \
    \  super().__init__(N, M, U, V, deg, La, Ra, Ua, Va, Ea)\n        self.W = W\n\
    \        self.Wa = Wa\n        \"\"\"Va[i] lists weights to edges from u for La[u]\
    \ <= i < Ra[u].\"\"\"\n\n    def __getitem__(G, v):\n        l,r = G.La[v],G.Ra[v]\n\
    \        return zip(G.Va[l:r], G.Wa[l:r])\n    \n    @overload\n    def distance(G)\
    \ -> list[list[int]]: ...\n    @overload\n    def distance(G, s: int = 0) -> list[int]:\
    \ ...\n    @overload\n    def distance(G, s: int, g: int) -> int: ...\n    def\
    \ distance(G, s = None, g = None):\n        match s, g:\n            case None,\
    \ None:\n                return G.floyd_warshall()\n            case s, None:\n\
    \                return G.dijkstra(s)\n            case s, g:\n              \
    \  return G.dijkstra(s, g)\n\n    def dijkstra(G, s: int, t: int = None):\n  \
    \      N, La, Ra, Va, Wa = G.N, G.La, G.Ra, G.Va, G.Wa\n        G.back = back\
    \ = fill_i32(N, -1)\n        G.D = D = fill_u64(N, inft)\n        D[s] = 0\n \
    \           \n        que = PriorityQueue(N, G.starts(s))\n        \n        while\
    \ que:\n            u, d = que.pop()\n            if u == t: break\n         \
    \   if d > D[u]: continue\n            for i in range(La[u], Ra[u]):\n       \
    \         v, w = Va[i], Wa[i], \n                if (nd := d + w) < D[v]:\n  \
    \                  D[v], back[v] = nd, i\n                    que.push(v, nd)\n\
    \        return D\n\n    def shortest_path(G, s: int, t: int):\n        D = G.dijkstra(s,\
    \ t)\n        if D[t] == inft: return None\n\n        Ua, back = G.Ua, G.back\n\
    \            \n        vertices = fill_u32(0)\n        vertices.append(t)\n  \
    \      v = t\n        while v != s:\n            vertices.append(v := Ua[back[v]])\n\
    \        return vertices[::-1]\n    \n    def shortest_path_edge_ids(G, s: int,\
    \ t: int):\n        D = G.dijkstra(s, t)\n        if D[t] == inft: return None\n\
    \n        Ea, back = G.Ea, G.back\n            \n        edges = fill_u32(0)\n\
    \        edges.append(t)\n        v = t\n        while v != s:\n            edges.append(v\
    \ := Ea[back[v]])\n        return edges[::-1]\n\n    def kruskal(G):\n       \
    \ N, U, V, W = G.N, G.U, G.V, G.W \n        dsu = DSU(N)\n        MST = [0]*(N-1)\n\
    \        need = N-1\n        for e in argsort(W):\n            u, v = dsu.merge(U[e],V[e],True)\n\
    \            if u != v:\n                need -= 1\n                MST[need]\
    \ = e\n                if not need: break\n        return None if need else MST\n\
    \    \n    def kruskal_heap(G):\n        N, M, U, V, W = G.N, G.M, G.U, G.V, G.W\
    \ \n        que = PriorityQueue(M, list(range(M)), W)\n        dsu = DSU(N)\n\
    \        MST = [0]*(N-1)\n        need = N-1\n        while que and need:\n  \
    \          e, _ = que.pop()\n            u, v = dsu.merge(U[e],V[e],True)\n  \
    \          if u != v:\n                MST[need := need-1] = e\n        return\
    \ None if need else MST\n   \n    def bellman_ford(G, s: int = 0) -> list[int]:\n\
    \        N, Ua, Va, Wa = G.N, G.Ua, G.Va, G.Wa\n        D = [inft]*N\n       \
    \ D[s] = 0\n        for _ in range(N-1):\n            for i in range(len(Ua)):\n\
    \                u,v,w = Ua[i], Va[i], Wa[i]\n                if D[u] == inft:\
    \ continue\n                D[v] = min(D[v], D[u] + w)\n        return D\n   \
    \ \n    def bellman_ford_neg_cyc_check(G, s: int = 0) -> tuple[bool, list[int]]:\n\
    \        \n        def bellman_ford(G, N, root) -> list[int]:\n            D =\
    \ [inft]*N\n            D[root] = 0\n            for _ in range(N-1):\n      \
    \          for u, edges in enumerate(G):\n                    if D[u] == inft:\
    \ continue\n                    for v,w in edges:\n                        D[v]\
    \ = min(D[v], D[u] + w)\n            return D\n        D = G.bellman_ford(s)\n\
    \        M, U, V, W = G.M, G.U, G.V, G.W\n        neg_cycle = any(D[U[i]]+W[i]<D[V[i]]\
    \ for i in range(M) if D[U[i]] < inft)\n        return neg_cycle, D\n    \n  \
    \  def floyd_warshall(G) -> list[list[int]]:\n        N, Ua, Va, Wa = G.N, G.Ua,\
    \ G.Va, G.Wa\n        D = [[inft]*N for _ in range(N)]\n\n        for u in range(N):\n\
    \            D[u][u] = 0\n\n        for i in range(len(Ua)):\n            u,v,w\
    \ = Ua[i], Va[i], Wa[i]\n            D[u][v] = min(D[u][v], w)\n        \n   \
    \     for k, Dk in enumerate(D):\n            for Di in D:\n                if\
    \ Di[k] == inft: continue\n                for j in range(N):\n              \
    \      if Dk[j] == inft: continue\n                    Di[j] = min(Di[j], Di[k]+Dk[j])\n\
    \        return D\n        \n    def floyd_warshall_neg_cyc_check(G):\n      \
    \  D = G.floyd_warshall()\n        return any(D[i][i] < 0 for i in range(G.N)),\
    \ D\n    \n    @classmethod\n    def compile(cls, N: int, M: int, shift: int =\
    \ -1):\n        def parse(ts: TokenStream):\n            U, V, W = fill_u32(M),\
    \ fill_u32(M), [0]*M\n            stream = ts.stream\n            for i in range(M):\n\
    \                u, v, W[i] = map(int, stream.readline().split())\n          \
    \      U[i], V[i] = u+shift, v+shift\n            return cls(N, U, V, W)\n   \
    \     return parse\n\n\nclass DSU:\n    def __init__(self, N):\n        self.N\
    \ = N\n        self.par = [-1] * N\n\n    def merge(self, u, v, src = False):\n\
    \        assert 0 <= u < self.N\n        assert 0 <= v < self.N\n\n        x,\
    \ y = self.leader(u), self.leader(v)\n        if x == y: return (x,y) if src else\
    \ x\n\n        if self.par[x] > self.par[y]:\n            x, y = y, x\n\n    \
    \    self.par[x] += self.par[y]\n        self.par[y] = x\n\n        return (x,y)\
    \ if src else x\n\n    def same(self, u: int, v: int):\n        assert 0 <= u\
    \ < self.N\n        assert 0 <= v < self.N\n        return self.leader(u) == self.leader(v)\n\
    \n    def leader(self, i) -> int:\n        assert 0 <= i < self.N\n        par\
    \ = self.par\n        p = par[i]\n        while p >= 0:\n            if par[p]\
    \ < 0:\n                return p\n            par[i], i, p = par[p], par[p], par[par[p]]\n\
    \n        return i\n\n    def size(self, i) -> int:\n        assert 0 <= i < self.N\n\
    \        \n        return -self.par[self.leader(i)]\n\n    def groups(self) ->\
    \ list[list[int]]:\n        leader_buf = [self.leader(i) for i in range(self.N)]\n\
    \n        result = [[] for _ in range(self.N)]\n        for i in range(self.N):\n\
    \            result[leader_buf[i]].append(i)\n\n        return [r for r in result\
    \ if r]\n\n\nfrom collections import UserList\nfrom heapq import heapify, heappop,\
    \ heappush, heappushpop, heapreplace\nfrom typing import Generic, TypeVar\n\n\
    T = TypeVar('T')\nclass HeapProtocol(Generic[T]):\n    def pop(self) -> T: ...\n\
    \    def push(self, item: T): ...\n    def pushpop(self, item: T) -> T: ...\n\
    \    def replace(self, item: T) -> T: ...\n\nclass PriorityQueue(HeapProtocol[int],\
    \ UserList[int]):\n    \n    def __init__(self, N: int, ids: list[int] = None,\
    \ priorities: list[int] = None, /):\n        self.shift = N.bit_length()\n   \
    \     self.mask = (1 << self.shift)-1\n        if ids is None:\n            super().__init__()\n\
    \        elif priorities is None:\n            heapify(ids)\n            self.data\
    \ = ids\n        else:\n            M = len(ids)\n            data = [0]*M\n \
    \           for i in range(M):\n                data[i] = self.encode(ids[i],\
    \ priorities[i]) \n            heapify(data)\n            self.data = data\n\n\
    \    def encode(self, id, priority):\n        return priority << self.shift |\
    \ id\n    \n    def decode(self, encoded):\n        return self.mask & encoded,\
    \ encoded >> self.shift\n    \n    def pop(self):\n        return self.decode(heappop(self.data))\n\
    \    \n    def push(self, id: int, priority: int):\n        heappush(self.data,\
    \ self.encode(id, priority))\n\n    def pushpop(self, id: int, priority: int):\n\
    \        return self.decode(heappushpop(self.data, self.encode(id, priority)))\n\
    \    \n    def replace(self, id: int, priority: int):\n        return self.decode(heapreplace(self.data,\
    \ self.encode(id, priority)))\n\nT = TypeVar('T')\ndef heappop_max(heap: list[T],\
    \ /) -> T: ...\ndef heapsiftdown_max(heap: list[T], root: int, pos: int): ...\n\
    def heapsiftup_max(heap: list[T], pos: int): ...\ndef heapsiftdown(heap: list[T],\
    \ root: int, pos: int): ...\ndef heapsiftup(heap: list[T], pos: int): ...\n\n\
    from heapq import (\n    _heapify_max as heapify_max, \n    _heappop_max as heappop_max,\
    \ \n    _siftdown_max as heapsiftdown_max,\n    _siftup_max as heapsiftup_max,\n\
    \    _siftdown as heapsiftdown,\n    _siftup as heapsiftup\n)\n\ndef heappush_max(heap:\
    \ list[T], item: T):\n    \"\"\"Push item onto heap, maintaining the heap invariant.\"\
    \"\"\n    heap.append(item)\n    heapsiftdown_max(heap, 0, len(heap)-1)\n\ndef\
    \ heapreplace_max(heap: list[T], item: T) -> T:\n    \"\"\"Pop and return the\
    \ current largest value, and add the new item.\n\n    This is more efficient than\
    \ heappop_max() followed by heappush_max(), and can be\n    more appropriate when\
    \ using a fixed-size heap.  Note that the value\n    returned may be larger than\
    \ item!  That constrains reasonable uses of\n    this routine unless written as\
    \ part of a conditional replacement:\n\n        if item > heap[0]:\n         \
    \   item = heapreplace_max(heap, item)\n    \"\"\"\n    returnitem = heap[0]\n\
    \    heap[0] = item\n    heapsiftup_max(heap, 0)\n    return returnitem\n\ndef\
    \ heappushpop_max(heap: list[T], item: T) -> T:\n    \"\"\"Fast version of a heappush_max\
    \ followed by a heappop_max.\"\"\"\n    if heap and heap[0] > item:\n        item,\
    \ heap[0] = heap[0], item\n        heapsiftup_max(heap, 0)\n    return item\n\n\
    \nclass MaxPriorityQueue(HeapProtocol[int], UserList[int]):\n    \n    def __init__(self,\
    \ N: int, ids: list[int] = None, priorities: list[int] = None, /):\n        self.shift\
    \ = N.bit_length()\n        self.mask = (1 << self.shift)-1\n        if ids is\
    \ None:\n            super().__init__()\n        elif priorities is None:\n  \
    \          heapify_max(ids)\n            self.data = ids\n        else:\n    \
    \        M = len(ids)\n            data = [0]*M\n            for i in range(M):\n\
    \                data[i] = self.encode(ids[i], priorities[i]) \n            heapify_max(data)\n\
    \            self.data = data\n\n    def encode(self, id, priority):\n       \
    \ return priority << self.shift | id\n    \n    def decode(self, encoded):\n \
    \       return self.mask & encoded, encoded >> self.shift\n    \n    def pop(self):\n\
    \        return self.decode(heappop_max(self.data))\n    \n    def push(self,\
    \ id: int, priority: int):\n        heappush_max(self.data, self.encode(id, priority))\n\
    \n    def pushpop(self, id: int, priority: int):\n        return self.decode(heappushpop_max(self.data,\
    \ self.encode(id, priority)))\n    \n    def replace(self, id: int, priority:\
    \ int):\n        return self.decode(heapreplace_max(self.data, self.encode(id,\
    \ priority)))\n\n    def peek(self):\n        return self.decode(self.data[0])\n\
    \nclass GraphWeighted(GraphWeightedBase):\n    def __init__(G, N: int, U: list[int],\
    \ V: list[int], W: list[int]):\n        M2 = (M := len(U)) << 1\n        deg,\
    \ Ea, Ua, Va, Wa = fill_u32(N), fill_u32(M2), fill_u32(M2), fill_u32(M2), [0]*M2\n\
    \        \n        for u in U:\n            deg[u] += 1\n        for v in V:\n\
    \            deg[v] += 1\n            \n        La, idx = fill_u32(N), 0\n   \
    \     for u in range(N): \n            La[u], idx = idx, idx + deg[u]\n      \
    \  Ra = La[:]\n\n        # place edge data using R to track\n        for e in\
    \ range(M):\n            u, v, w = U[e], V[e], W[e]\n            i, j = Ra[u],\
    \ Ra[v]\n            Ua[i], Va[i], Wa[i], Ea[i] = u, v, w, e\n            Ra[u]\
    \ += 1\n            Ua[j], Va[j], Wa[j], Ea[j] = v, u, w, M+e\n            Ra[v]\
    \ += 1\n\n        super().__init__(N, M, U, V, W, deg, La, Ra, Ua, Va, Wa, Ea)\n\
    \n"
  code: "import cp_library.alg.graph.fast.__header__\nfrom cp_library.alg.graph.fast.graph_weighted_base_cls\
    \ import GraphWeightedBase\n\nclass GraphWeighted(GraphWeightedBase):\n    def\
    \ __init__(G, N: int, U: list[int], V: list[int], W: list[int]):\n        M2 =\
    \ (M := len(U)) << 1\n        deg, Ea, Ua, Va, Wa = fill_u32(N), fill_u32(M2),\
    \ fill_u32(M2), fill_u32(M2), [0]*M2\n        \n        for u in U:\n        \
    \    deg[u] += 1\n        for v in V:\n            deg[v] += 1\n            \n\
    \        La, idx = fill_u32(N), 0\n        for u in range(N): \n            La[u],\
    \ idx = idx, idx + deg[u]\n        Ra = La[:]\n\n        # place edge data using\
    \ R to track\n        for e in range(M):\n            u, v, w = U[e], V[e], W[e]\n\
    \            i, j = Ra[u], Ra[v]\n            Ua[i], Va[i], Wa[i], Ea[i] = u,\
    \ v, w, e\n            Ra[u] += 1\n            Ua[j], Va[j], Wa[j], Ea[j] = v,\
    \ u, w, M+e\n            Ra[v] += 1\n\n        super().__init__(N, M, U, V, W,\
    \ deg, La, Ra, Ua, Va, Wa, Ea)\n\nfrom cp_library.ds.fill_fn import fill_u32\n"
  dependsOn:
  - cp_library/alg/graph/fast/graph_weighted_base_cls.py
  - cp_library/ds/fill_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/alg/iter/argsort_fn.py
  - cp_library/alg/graph/fast/graph_base_cls.py
  - cp_library/alg/graph/bellman_ford_fn.py
  - cp_library/ds/dsu_cls.py
  - cp_library/ds/elist_fn.py
  - cp_library/ds/heap/priority_queue_cls.py
  - cp_library/math/inft_cnst.py
  - cp_library/alg/graph/dfs_options_cls.py
  - cp_library/ds/heap/heap_proto.py
  - cp_library/ds/heap/heapq_max_import.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: false
  path: cp_library/alg/graph/fast/graph_weighted_cls.py
  requiredBy:
  - cp_library/alg/tree/fast/tree_weighted_cls.py
  timestamp: '2024-12-18 00:49:06+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/abc294_g_fast_tree_lca_table_weighted_bit.test.py
  - test/minimum_spanning_tree_kruskal.test.py
  - test/abc294_g_fast_tree_heavy_light_decomposition.test.py
  - test/minimum_spanning_tree_kruskal_heap.test.py
documentation_of: cp_library/alg/graph/fast/graph_weighted_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/fast/graph_weighted_cls.py
- /library/cp_library/alg/graph/fast/graph_weighted_cls.py.html
title: cp_library/alg/graph/fast/graph_weighted_cls.py
---
