---
data:
  _extendedDependsOn:
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
    path: cp_library/alg/graph/fast/graph_weighted_cls.py
    title: cp_library/alg/graph/fast/graph_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/argsort_fn.py
    title: cp_library/alg/iter/argsort_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/fast/tree_base_cls.py
    title: cp_library/alg/tree/fast/tree_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/fast/tree_weighted_base_cls.py
    title: cp_library/alg/tree/fast/tree_weighted_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/fast/tree_weighted_cls.py
    title: cp_library/alg/tree/fast/tree_weighted_cls.py
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
    path: cp_library/io/read_fn.py
    title: cp_library/io/read_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/write_fn.py
    title: cp_library/io/write_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/inft_cnst.py
    title: cp_library/math/inft_cnst.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_5_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_5_B
  bundledCode: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_5_B\n\
    \ndef main():\n    N = read(int)\n    T = read(TreeWeighted[N, 0])\n    _, _,\
    \ g = T.diameter(True)\n    ans = [max(ds,dg) for ds,dg in zip(T.D, T.distance(g))]\n\
    \    write(*ans, sep='\\n')\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\nfrom typing import Type, TypeVar, Union, overload\nimport\
    \ typing\nfrom collections import deque\nfrom numbers import Number\nfrom types\
    \ import GenericAlias \nfrom typing import Callable, Collection, Iterator, TypeVar,\
    \ Union\nimport os\nimport sys\nfrom io import BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n\
    \    BUFSIZE = 8192\n    newlines = 0\n\n    def __init__(self, file):\n     \
    \   self._fd = file.fileno()\n        self.buffer = BytesIO()\n        self.writable\
    \ = \"x\" in file.mode or \"r\" not in file.mode\n        self.write = self.buffer.write\
    \ if self.writable else None\n\n    def read(self):\n        BUFSIZE = self.BUFSIZE\n\
    \        while True:\n            b = os.read(self._fd, max(os.fstat(self._fd).st_size,\
    \ BUFSIZE))\n            if not b:\n                break\n            ptr = self.buffer.tell()\n\
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
    \ TokenStream):\n            return cls(next(ts))\n        return parser\n\nT\
    \ = TypeVar('T')\n@overload\ndef read() -> list[int]: ...\n@overload\ndef read(spec:\
    \ int) -> list[int]: ...\n@overload\ndef read(spec: Union[Type[T],T], char=False)\
    \ -> T: ...\ndef read(spec: Union[Type[T],T] = None, char=False):\n    if not\
    \ char:\n        if spec is None:\n            return map(int, TokenStream.stream.readline().split())\n\
    \        elif isinstance(offset := spec, int):\n            return [int(s)+offset\
    \ for s in TokenStream.stream.readline().split()]\n        elif spec is int:\n\
    \            return int(TokenStream.stream.readline())\n        else:\n      \
    \      stream = TokenStream()\n    else:\n        stream = CharStream()\n    parser:\
    \ T = Parser.compile(spec)\n    return parser(stream)\n\ndef write(*args, **kwargs):\n\
    \    \"\"\"Prints the values to a stream, or to stdout_fast by default.\"\"\"\n\
    \    sep, file = kwargs.pop(\"sep\", \" \"), kwargs.pop(\"file\", IOWrapper.stdout)\n\
    \    at_start = True\n    for x in args:\n        if not at_start:\n         \
    \   file.write(sep)\n        file.write(str(x))\n        at_start = False\n  \
    \  file.write(kwargs.pop(\"end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n\
    \        file.flush()\n\n\n\n\ndef argsort(A: list[int]):\n    N = len(A)\n  \
    \  mask = (1 << (shift := N.bit_length())) - 1\n    indices = [0]*N\n    for i\
    \ in range(N):\n        indices[i] = A[i] << shift | i\n    indices.sort()\n \
    \   for i in range(N):\n        indices[i] &= mask\n    return indices\nfrom typing\
    \ import Callable, Sequence, Union, overload\n\nfrom enum import auto, IntFlag,\
    \ IntEnum\n\nclass DFSFlags(IntFlag):\n    ENTER = auto()\n    DOWN = auto()\n\
    \    BACK = auto()\n    CROSS = auto()\n    LEAVE = auto()\n    UP = auto()\n\
    \    MAXDEPTH = auto()\n\n    RETURN_PARENTS = auto()\n    RETURN_DEPTHS = auto()\n\
    \    BACKTRACK = auto()\n    CONNECT_ROOTS = auto()\n\n    # Common combinations\n\
    \    ALL_EDGES = DOWN | BACK | CROSS\n    EULER_TOUR = DOWN | UP\n    INTERVAL\
    \ = ENTER | LEAVE\n    TOPDOWN = DOWN | CONNECT_ROOTS\n    BOTTOMUP = UP | CONNECT_ROOTS\n\
    \    RETURN_ALL = RETURN_PARENTS | RETURN_DEPTHS\n\nclass DFSEvent(IntEnum):\n\
    \    ENTER = DFSFlags.ENTER \n    DOWN = DFSFlags.DOWN \n    BACK = DFSFlags.BACK\
    \ \n    CROSS = DFSFlags.CROSS \n    LEAVE = DFSFlags.LEAVE \n    UP = DFSFlags.UP\
    \ \n    MAXDEPTH = DFSFlags.MAXDEPTH\n    \n\nclass GraphBase(Sequence, Parsable):\n\
    \    def __init__(self, N: int, M: int, U: list[int], V: list[int], \n       \
    \          deg: list[int], La: list[int], Ra: list[int],\n                 Ua:\
    \ list[int], Va: list[int], Ea: list[int]):\n        self.N = N\n        \"\"\"\
    The number of vertices.\"\"\"\n        self.M = M\n        \"\"\"The number of\
    \ edges.\"\"\"\n        self.U = U\n        \"\"\"A list of source vertices in\
    \ the original edge list.\"\"\"\n        self.V = V\n        \"\"\"A list of destination\
    \ vertices in the original edge list.\"\"\"\n        self.deg = deg\n        \"\
    \"\"deg[u] is the out degree of vertex u.\"\"\"\n        self.La = La\n      \
    \  \"\"\"La[u] stores the start index of the list of adjacent vertices from u.\"\
    \"\"\n        self.Ra = Ra\n        \"\"\"Ra[u] stores the stop index of the list\
    \ of adjacent vertices from u.\"\"\"\n        self.Ua = Ua\n        \"\"\"Ua[i]\
    \ = u for La[u] <= i < Ra[u], useful for backtracking.\"\"\"\n        self.Va\
    \ = Va\n        \"\"\"Va[i] lists adjacent vertices to u for La[u] <= i < Ra[u].\"\
    \"\"\n        self.Ea = Ea\n        \"\"\"Ea[i] lists the edge ids that start\
    \ from u for La[u] <= i < Ra[u].\n        For undirected graphs, edge ids in range\
    \ M<= e <2*M are edges from V[e-M] -> U[e-M].\n        \"\"\"\n\n    def __len__(G)\
    \ -> int: return G.N\n    def __getitem__(G, u): return G.Va[G.La[u]:G.Ra[u]]\n\
    \    def range(G, u): return range(G.La[u],G.Ra[u])\n    \n    @overload\n   \
    \ def distance(G) -> list[list[int]]: ...\n    @overload\n    def distance(G,\
    \ s: int = 0) -> list[int]: ...\n    @overload\n    def distance(G, s: int, g:\
    \ int) -> int: ...\n    def distance(G, s = None, g = None):\n        if s ==\
    \ None: return G.floyd_warshall()\n        else: return G.bfs(s, g)\n\n    def\
    \ shortest_path(G, s: int, t: int):\n        if G.distance(s, t) >= inft: return\
    \ None\n        Ua, back, vertices = G.Ua, G.back, u32a(1, v := t)\n        while\
    \ v != s: vertices.append(v := Ua[back[v]])\n        return vertices[::-1]\n \
    \   \n    def shortest_path_edge_ids(G, s: int, t: int):\n        if G.distance(s,\
    \ t) >= inft: return None\n        Ea, Ua, back, edges, v = G.Ea, G.Ua, G.back,\
    \ u32a(0), t\n        while v != s:\n            edges.append(Ea[i := back[v]])\n\
    \            v = Ua[i]\n        return edges[::-1]\n    \n    @overload\n    def\
    \ bfs(G, s: Union[int,list] = 0) -> list[int]: ...\n    @overload\n    def bfs(G,\
    \ s: Union[int,list], g: int) -> int: ...\n    def bfs(G, s: int = 0, g: int =\
    \ None):\n        S, Va, back, D = G.starts(s), G.Va, i32a(N := G.N, -1), u64a(N,\
    \ inft)\n        G.back, G.D = back, D\n        for u in S: D[u] = 0\n       \
    \ que = deque(S)\n        while que:\n            nd = D[u := que.popleft()]+1\n\
    \            if u == g: return nd-1\n            for i in G.range(u):\n      \
    \          if nd < D[v := Va[i]]:\n                    D[v], back[v] = nd, i\n\
    \                    que.append(v)\n        return D if g is None else inft \n\
    \n    def floyd_warshall(G) -> list[list[int]]:\n        M, Ua, Va, N = G.M, G.Ua,\
    \ G.Va, G.N\n        G.D = D = [[inft]*N for _ in range(N)]\n        for u in\
    \ range(N): D[u][u] = 0\n        for i in range(M): D[Ua[i]][Va[i]] = 1\n    \
    \    for k, Dk in enumerate(D):\n            for Di in D:\n                if\
    \ Di[k] == inft: continue\n                for j in range(N):\n              \
    \      if Dk[j] == inft: continue\n                    Di[j] = min(Di[j], Di[k]+Dk[j])\n\
    \        return D\n\n    def find_cycle_indices(G, s: Union[int, None] = None):\n\
    \        M, Ea, Ua, Va, vis, back = G.M, G.Ea, G. Ua, G.Va, u8a(N := G.N), i32a(N,\
    \ -1)\n        G.vis, G.back, stack = vis, back, elist(N)\n        for s in G.starts(s):\n\
    \            if vis[s]: continue\n            stack.append(s)\n            while\
    \ stack:\n                if vis[u := stack.pop()] == 0:\n                   \
    \ stack.append(u)\n                    vis[u] = 1\n                    for i in\
    \ G.range(u):\n                        if vis[v := Va[i]] == 1:\n            \
    \                if u != v and ((j := back[u]) == -1 or abs(Ea[j]-Ea[i]) == M):\
    \ continue\n                            I = u32a(1,i)\n                      \
    \      while v != u:\n                                I.append(i := back[u])\n\
    \                                u = Ua[i]\n                            return\
    \ I[::-1]\n                        elif vis[v] == 0:\n                       \
    \     back[v] = i\n                            stack.append(v)\n             \
    \   else:\n                    vis[u] = 2\n    \n    def find_cycle(G, s: Union[int,\
    \ None] = None):\n        if I := G.find_cycle_indices(s): return [G.Ua[i] for\
    \ i in I]\n    \n    def find_cycle_edge_ids(G, s: Union[int, None] = None):\n\
    \        if I := G.find_cycle_indices(s): return [G.Ea[i] for i in I]\n\n    def\
    \ find_minimal_cycle(G, s=0):\n        D, par, que, Va = u64a(N := G.N, inft),\
    \ i32a(N, -1), deque([s]), G.Va\n        D[s] = 0\n        while que:\n      \
    \      for i in G.range(u := que.popleft()):\n                if (v := Va[i])\
    \ == s:  # Found cycle back to start\n                    cycle = [u]\n      \
    \              while u != s: cycle.append(u := par[u])\n                    return\
    \ cycle\n                if D[v] < inft: continue\n                D[v], par[v]\
    \ = D[u]+1, u\n                que.append(v)\n\n    def dfs_discovery(G, s: Union[int,list[int],None]\
    \ = None, include_roots = False):\n        '''Returns lists U and V representing\
    \ U[i] -> V[i] edges in order of top down discovery'''\n        Va, vis, stack,\
    \ order = G.Va, [False]*(N := G.N), elist(N), elist(N)\n        for s in G.starts(s):\n\
    \            if vis[s]: continue\n            if include_roots: order.append(-s-1)\n\
    \            vis[s] = True\n            stack.append(s)\n            while stack:\n\
    \                for i in G.range(stack.pop()):\n                    if vis[v\
    \ := Va[i]]: continue\n                    vis[v] = True\n                   \
    \ order.append(i), stack.append(v)\n        return order\n\n    def dfs(G, s:\
    \ Union[int,list] = None, /, connect_roots = False, backtrack = False, max_depth\
    \ = None, enter_fn: Callable[[int],None] = None, leave_fn: Callable[[int],None]\
    \ = None, max_depth_fn: Callable[[int],None] = None, down_fn: Callable[[int,int],None]\
    \ = None, back_fn: Callable[[int,int],None] = None, cross_fn: Callable[[int,int],None]\
    \ = None, up_fn: Callable[[int,int],None] = None):\n        Va, La, Ra, I = G.Va,\
    \ G.La, G.Ra, G.La[:]\n        state, stack = u8a(G.N), elist(G.N if max_depth\
    \ is None else max_depth+1)\n        for s in G.starts(s):\n            if state[s]:\
    \ continue\n            stack.append(s)\n            if connect_roots and down_fn:\
    \ down_fn(-1,s)\n            while stack:\n                if state[u := stack[-1]]\
    \ == 0:\n                    state[u] = 1\n                    if enter_fn: enter_fn(u)\n\
    \                    if max_depth is not None and len(stack) > max_depth:\n  \
    \                      I[u] = Ra[u]\n                        if max_depth_fn:\
    \ max_depth_fn(u)\n                if (i := I[u]) < Ra[u]:\n                 \
    \   I[u] += 1\n                    if (s := state[v := Va[i]]) == 0:\n       \
    \                 stack.append(v)\n                        if down_fn: down_fn(u,v)\n\
    \                    elif back_fn and s == 1: back_fn(u,v)\n                 \
    \   elif cross_fn and s == 2: cross_fn(u,v)\n                else:\n         \
    \           stack.pop()\n                    state[u] = 2\n                  \
    \  if backtrack: state[u], I[u] = 0, La[u]\n                    if leave_fn: leave_fn(u)\n\
    \                    if up_fn and stack: up_fn(u, stack[-1])\n            if connect_roots\
    \ and up_fn: up_fn(s, -1)\n    \n    def dfs_enter_leave(G, s: Union[int,list[int],None]\
    \ = None) -> tuple[list[int],list[int]]:\n        '''Returns lists U and V representing\
    \ U[i] -> V[i] edges in order of top down discovery'''\n        N, Ra, Va, I =\
    \ G.N, G.Ra, G.Va, G.La[:]\n        stack, order, events, par = elist(N), elist(2*N),\
    \ elist(2*N), i32a(N, -1)\n        G.par, ENTER, LEAVE = par, int(DFSEvent.ENTER),\
    \ int(DFSEvent.LEAVE)\n        for s in G.starts(s):\n            if par[s] >=\
    \ 0: continue\n            par[s] = s\n            order.append(s), events.append(ENTER),\
    \ stack.append(s)\n            while stack:\n                if (i := I[u := stack[-1]])\
    \ < Ra[u]:\n                    I[u] += 1\n                    if par[v := Va[i]]\
    \ >= 0: continue\n                    par[v] = u\n                    order.append(v),\
    \ events.append(ENTER), stack.append(v)\n                else:\n             \
    \       order.append(u), events.append(LEAVE), stack.pop()\n        return events,\
    \ order\n    \n    def is_bipartite(G):\n        Va, que, color = G.Va, deque(),\
    \ u8a(N := G.N)                \n        for s in range(N):\n            if color[s]:\
    \ continue\n            color[s] = 1\n            que.append(s)\n            while\
    \ que:\n                for i in G.range(u := que.popleft()):\n              \
    \      if color[v := Va[i]] == 0:\n                        color[v] = color[u]\
    \ ^ 2\n                        que.append(v)\n                    elif color[v]\
    \ == color[u]: return False\n        return True\n    \n    def starts(G, s: Union[int,list[int],None])\
    \ -> list[int]:\n        if isinstance(s, int): return [s]\n        elif s is\
    \ None: return range(G.N)\n        elif isinstance(s, list): return s\n      \
    \  else: return list(s)\n\n    @classmethod\n    def compile(cls, N: int, M: int,\
    \ shift: int = -1):\n        def parse(ts: TokenStream):\n            U, V = u32a(M),\
    \ u32a(M)\n            stream = ts.stream\n            for i in range(M):\n  \
    \              u, v = map(int, stream.readline().split())\n                U[i],\
    \ V[i] = u+shift, v+shift\n            return cls(N, U, V)\n        return parse\n\
    \    \n\n\ndef elist(est_len: int) -> list: ...\ntry:\n    from __pypy__ import\
    \ newlist_hint\nexcept:\n    def newlist_hint(hint):\n        return []\nelist\
    \ = newlist_hint\n    \nfrom array import array\n\ndef i8a(N: int, elm: int =\
    \ 0): return array('b', (elm,))*N       # signed char\ndef u8a(N: int, elm: int\
    \ = 0): return array('B', (elm,))*N       # unsigned char\ndef i16a(N: int, elm:\
    \ int = 0): return array('h', (elm,))*N      # signed short\ndef u16a(N: int,\
    \ elm: int = 0): return array('H', (elm,))*N      # unsigned short\ndef i32a(N:\
    \ int, elm: int = 0): return array('i', (elm,))*N      # signed int\ndef u32a(N:\
    \ int, elm: int = 0): return array('I', (elm,))*N      # unsigned int\ndef i64a(N:\
    \ int, elm: int = 0): return array('q', (elm,))*N      # signed long long\ndef\
    \ u64a(N: int, elm: int = 0): return array('Q', (elm,))*N      # unsigned long\
    \ long\ndef f32a(N: int, elm: float = 0.0): return array('f', (elm,))*N  # float\n\
    def f64a(N: int, elm: float = 0.0): return array('d', (elm,))*N  # double\n\n\
    inft: int\n\ninft = sys.maxsize\n\nclass GraphWeightedBase(GraphBase):\n    def\
    \ __init__(self, N: int, M: int, U: list[int], V: list[int], W: list[int], \n\
    \                 deg: list[int], La: list[int], Ra: list[int],\n            \
    \     Ua: list[int], Va: list[int], Wa: list[int], Ea: list[int]):\n        super().__init__(N,\
    \ M, U, V, deg, La, Ra, Ua, Va, Ea)\n        self.W = W\n        self.Wa = Wa\n\
    \        \"\"\"Wa[i] lists weights to edges from u for La[u] <= i < Ra[u].\"\"\
    \"\n        \n    def __getitem__(G, u):\n        l,r = G.La[u],G.Ra[u]\n    \
    \    return zip(G.Va[l:r], G.Wa[l:r])\n    \n    @overload\n    def distance(G)\
    \ -> list[list[int]]: ...\n    @overload\n    def distance(G, s: int = 0) -> list[int]:\
    \ ...\n    @overload\n    def distance(G, s: int, g: int) -> int: ...\n    def\
    \ distance(G, s = None, g = None):\n        if s == None:\n            return\
    \ G.floyd_warshall()\n        else:\n            return G.dijkstra(s, g)\n\n \
    \   def dijkstra(G, s: int, t: int = None):\n        N, S, Va, Wa = G.N, G.starts(s),\
    \ G.Va, G.Wa\n        G.back = back = i32a(N, -1)\n        G.D = D = u64a(N, inft)\n\
    \        for s in S: D[s] = 0\n        que = PriorityQueue(N, S)\n        while\
    \ que:\n            u, d = que.pop()\n            if d > D[u]: continue\n    \
    \        if u == t: return d\n            for i in G.range(u): \n            \
    \    if (nd := d + Wa[i]) < D[v := Va[i]]:\n                    D[v], back[v]\
    \ = nd, i\n                    que.push(v, nd)\n        return D if t is None\
    \ else inft \n\n    def kruskal(G):\n        N, U, V, W = G.N, G.U, G.V, G.W \n\
    \        dsu = DSU(N)\n        MST = [0]*(N-1)\n        need = N-1\n        for\
    \ e in argsort(W):\n            u, v = dsu.merge(U[e],V[e],True)\n           \
    \ if u != v:\n                MST[need := need-1] = e\n                if not\
    \ need: break\n        return None if need else MST\n    \n    def kruskal_heap(G):\n\
    \        N, M, U, V, W = G.N, G.M, G.U, G.V, G.W \n        que = PriorityQueue(M,\
    \ list(range(M)), W)\n        dsu = DSU(N)\n        MST = [0]*(N-1)\n        need\
    \ = N-1\n        while que and need:\n            e, _ = que.pop()\n         \
    \   u, v = dsu.merge(U[e],V[e],True)\n            if u != v:\n               \
    \ MST[need := need-1] = e\n        return None if need else MST\n   \n    def\
    \ bellman_ford(G, s: int = 0) -> list[int]:\n        N, Ua, Va, Wa = G.N, G.Ua,\
    \ G.Va, G.Wa\n        D = [inft]*N\n        D[s] = 0\n        for _ in range(N-1):\n\
    \            for i in range(len(Ua)):\n                u,v,w = Ua[i], Va[i], Wa[i]\n\
    \                if D[u] == inft: continue\n                D[v] = min(D[v], D[u]\
    \ + w)\n        return D\n    \n    def bellman_ford_neg_cyc_check(G, s: int =\
    \ 0) -> tuple[bool, list[int]]:\n        D = G.bellman_ford(s)\n        M, U,\
    \ V, W = G.M, G.U, G.V, G.W\n        neg_cycle = any(D[U[i]]+W[i]<D[V[i]] for\
    \ i in range(M) if D[U[i]] < inft)\n        return neg_cycle, D\n    \n    def\
    \ floyd_warshall(G) -> list[list[int]]:\n        N, Ua, Va, Wa = G.N, G.Ua, G.Va,\
    \ G.Wa\n        D = [[inft]*N for _ in range(N)]\n\n        for u in range(N):\n\
    \            D[u][u] = 0\n\n        for i in range(len(Ua)):\n            u,v,w\
    \ = Ua[i], Va[i], Wa[i]\n            D[u][v] = min(D[u][v], w)\n        \n   \
    \     for k, Dk in enumerate(D):\n            for Di in D:\n                if\
    \ Di[k] == inft: continue\n                for j in range(N):\n              \
    \      if Dk[j] == inft: continue\n                    Di[j] = min(Di[j], Di[k]+Dk[j])\n\
    \        return D\n        \n    def floyd_warshall_neg_cyc_check(G):\n      \
    \  D = G.floyd_warshall()\n        return any(D[i][i] < 0 for i in range(G.N)),\
    \ D\n    \n    @classmethod\n    def compile(cls, N: int, M: int, shift: int =\
    \ -1):\n        def parse(ts: TokenStream):\n            U, V, W = u32a(M), u32a(M),\
    \ [0]*M\n            stream = ts.stream\n            for i in range(M):\n    \
    \            u, v, W[i] = map(int, stream.readline().split())\n              \
    \  U[i], V[i] = u+shift, v+shift\n            return cls(N, U, V, W)\n       \
    \ return parse\n\n\nclass DSU:\n    def __init__(self, N):\n        self.N = N\n\
    \        self.par = [-1] * N\n\n    def merge(self, u, v, src = False):\n    \
    \    assert 0 <= u < self.N\n        assert 0 <= v < self.N\n\n        x, y =\
    \ self.leader(u), self.leader(v)\n        if x == y: return (x,y) if src else\
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
    \     self.mask = (1 << self.shift)-1\n        if ids is None:\n            self.data\
    \ = elist(N)\n        elif priorities is None:\n            heapify(ids)\n   \
    \         self.data = ids\n        else:\n            M = len(ids)\n         \
    \   data = [0]*M\n            for i in range(M):\n                data[i] = self.encode(ids[i],\
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
    \    \n\nclass GraphWeighted(GraphWeightedBase):\n    def __init__(G, N: int,\
    \ U: list[int], V: list[int], W: list[int]):\n        M2 = (M := len(U)) << 1\n\
    \        deg, Ea, Ua, Va, Wa = u32a(N), u32a(M2), u32a(M2), u32a(M2), [0]*M2\n\
    \        \n        for u in U:\n            deg[u] += 1\n        for v in V:\n\
    \            deg[v] += 1\n            \n        La, idx = u32a(N), 0\n       \
    \ for u in range(N): \n            La[u], idx = idx, idx + deg[u]\n        Ra\
    \ = La[:]\n\n        # place edge data using R to track\n        for e in range(M):\n\
    \            u, v, w = U[e], V[e], W[e]\n            i, j = Ra[u], Ra[v]\n   \
    \         Ua[i], Va[i], Wa[i], Ea[i] = u, v, w, e\n            Ra[u] += 1\n  \
    \          Ua[j], Va[j], Wa[j], Ea[j] = v, u, w, M+e\n            Ra[v] += 1\n\
    \n        super().__init__(N, M, U, V, W, deg, La, Ra, Ua, Va, Wa, Ea)\n\nfrom\
    \ typing import Callable, Literal, TypeVar, Union, overload\n\n_T = TypeVar('_T')\n\
    \nclass TreeBase(GraphBase):\n    @overload\n    def distance(T) -> list[list[int]]:\
    \ ...\n    @overload\n    def distance(T, s: int = 0) -> list[int]: ...\n    @overload\n\
    \    def distance(T, s: int, g: int) -> int: ...\n    def distance(T, s = None,\
    \ g = None):\n        if s == None:\n            return [T.dfs_distance(u) for\
    \ u in range(T.N)]\n        else:\n            return T.dfs_distance(s, g)\n\n\
    \    @overload\n    def diameter(T) -> int: ...\n    @overload\n    def diameter(T,\
    \ endpoints: Literal[True]) -> tuple[int,int,int]: ...\n    def diameter(T, endpoints\
    \ = False):\n        mask = (1 << (shift := T.N.bit_length())) - 1\n        s\
    \ = max(d << shift | v for v,d in enumerate(T.distance(0))) & mask\n        dg\
    \ = max(d << shift | v for v,d in enumerate(T.distance(s))) \n        diam, g\
    \ = dg >> shift, dg & mask\n        return (diam, s, g) if endpoints else diam\n\
    \    \n    def dfs_distance(T, s: int, g: Union[int,None] = None):\n        stack,\
    \ Va = elist(N := T.N), T.Va\n        T.D, T.back = D, back = u64a(N, inft), i32a(N,\
    \ -1)\n        D[s] = 0\n        stack.append(s)\n        while stack:\n     \
    \       nd = D[u := stack.pop()]+1\n            if u == g: return nd-1\n     \
    \       for i in T.range(u):\n                if nd < D[v := Va[i]]:\n       \
    \             D[v], back[v] = nd, i\n                    stack.append(v)\n   \
    \     return D if g is None else inft\n\n    def rerooting_dp(T, e: _T, \n   \
    \                  merge: Callable[[_T,_T],_T], \n                     add_child:\
    \ Callable[[int,int,int,_T],_T] = lambda p,c,i,s:s,\n                     s: int\
    \ = 0):\n        N, La, Ra, Ua, Va = T.N, T.La, T.Ra, T.Ua, T.Va\n        order,\
    \ dp, suf = T.dfs_discovery(s), [e]*N, [e]*len(Ua)\n        I = Ra[:] # tracks\
    \ current indices for suffix array accumulation\n\n        # up\n        for i\
    \ in order[::-1]:\n            u,v = Ua[i], Va[i]\n            # subtree v finished\
    \ up pass, store value to accumulate for u\n            dp[v] = new = add_child(u,\
    \ v, i, dp[v])\n            dp[u] = merge(dp[u], new)\n            # suffix accumulation\n\
    \            I[u] -= 1\n            if I[u] > La[u]:\n                suf[I[u]-1]\
    \ = merge(suf[I[u]], new)\n\n        # down\n        dp[s] = e # at this point\
    \ dp stores values to be merged in parent\n        for i in order:\n         \
    \   u,v = Ua[i], Va[i]\n            # prefix accumulation\n            dp[u] =\
    \ merge(pre := dp[u], dp[v])\n            # push value to child\n            dp[v]\
    \ = add_child(v, u, i, merge(suf[I[u]], pre))\n            I[u] += 1\n       \
    \ \n        return dp\n    \n    def euler_tour(T, s = 0):\n        N, Va = len(T),\
    \ T.Va\n        tin, tout, par, back = [-1]*N,[-1]*N,[-1]*N,[0]*N\n        order,\
    \ delta = elist(2*N), elist(2*N)\n        \n        stack = elist(N)\n       \
    \ stack.append(s)\n        while stack:\n            p = par[u := stack.pop()]\n\
    \            if tin[u] == -1:\n                tin[u] = len(order)\n         \
    \       for i in T.range(u):\n                    if (v := Va[i]) != p:\n    \
    \                    par[v], back[v] = u, i\n                        stack.append(u)\n\
    \                        stack.append(v)\n                delta.append(1)\n  \
    \          else:\n                delta.append(-1)\n            \n           \
    \ order.append(u)\n            tout[u] = len(order)\n        delta[0] = delta[-1]\
    \ = 0\n        T.tin, T.tout, T.par, T.back = tin, tout, par, back\n        T.order,\
    \ T.delta = order, delta\n\n    def hld_precomp(T, r = 0):\n        N, time, Va\
    \ = T.N, 0, T.Va\n        tin, tout, size = [0]*N, [0]*N, [1]*N+[0]\n        par,\
    \ heavy, head = [-1]*N, [-1]*N, [r]*N\n        depth, order, state = [0]*N, [0]*N,\
    \ [0]*N\n        stack = elist(N)\n        stack.append(r)\n        while stack:\n\
    \            if (s := state[v := stack.pop()]) == 0: # dfs down\n            \
    \    p, state[v] = par[v], 1\n                stack.append(v)\n              \
    \  for i in T.range(v):\n                    if (c := Va[i]) != p:\n         \
    \               depth[c], par[c] = depth[v]+1, v\n                        stack.append(c)\n\
    \n            elif s == 1: # dfs up\n                p, l = par[v], -1\n     \
    \           for i in T.range(v):\n                    if (c := Va[i]) != p:\n\
    \                        size[v] += size[c]\n                        if size[c]\
    \ > size[l]:\n                            l = c\n                heavy[v] = l\n\
    \                if p == -1:\n                    state[v] = 2\n             \
    \       stack.append(v)\n\n            elif s == 2: # decompose down\n       \
    \         p, h, l = par[v], head[v], heavy[v]\n                tin[v], order[time],\
    \ state[v] = time, v, 3\n                time += 1\n                stack.append(v)\n\
    \                \n                for i in T.range(v):\n                    if\
    \ (c := Va[i]) != p and c != l:\n                        head[c], state[c] = c,\
    \ 2\n                        stack.append(c)\n\n                if l != -1:\n\
    \                    head[l], state[l] = h, 2\n                    stack.append(l)\n\
    \n            elif s == 3: # decompose up\n                tout[v] = time\n  \
    \      T.size, T.depth = size, depth\n        T.order, T.tin, T.tout = order,\
    \ tin, tout\n        T.par, T.heavy, T.head = par, heavy, head\n\n    @classmethod\n\
    \    def compile(cls, N: int, shift: int = -1):\n        return GraphBase.compile.__func__(cls,\
    \ N, N-1, shift)\n    \n\n_T = TypeVar('_T')\nclass TreeWeightedBase(TreeBase,\
    \ GraphWeightedBase):\n\n    def dfs_distance(T, s: int, g: Union[int,None] =\
    \ None):\n        stack, Wa, Va = elist(N := T.N), T.Wa, T.Va\n        stack.append(s)\n\
    \        T.D, T.back = D, back = u64a(N, inft), i32a(N, -1)\n        D[s] = 0\n\
    \        while stack:\n            d = D[u := stack.pop()]\n            if u ==\
    \ g: return d\n            for i in T.range(u):\n                if (nd := d+Wa[i])\
    \ < D[v := Va[i]]:\n                    D[v], back[v] = nd, i\n              \
    \      stack.append(v)\n        return D if g is None else inft \n    \n    def\
    \ euler_tour(T, s = 0):\n        N, Va, Wa = len(T), T.Va, T.Wa\n        tin,\
    \ tout, par = [-1]*N,[-1]*N,[-1]*N\n        order, delta, Wdelta = elist(2*N),\
    \ elist(2*N), elist(2*N)\n        \n        stack, Wstack = elist(N), elist(N)\n\
    \        stack.append(s)\n        Wstack.append(0)\n        while stack:\n   \
    \         p, wd = par[u := stack.pop()], Wstack.pop()\n            if tin[u] ==\
    \ -1:\n                tin[u] = len(order)\n                for i in T.range(u):\n\
    \                    if (v := Va[i]) != p:\n                        w, par[v]\
    \ = Wa[i], u\n                        stack.append(u)\n                      \
    \  stack.append(v)\n                        Wstack.append(-w)\n              \
    \          Wstack.append(w)\n                delta.append(1)\n            else:\n\
    \                delta.append(-1)\n            \n            Wdelta.append(wd)\n\
    \            order.append(u)\n            tout[u] = len(order)\n        delta[0]\
    \ = delta[-1] = 0\n        T.tin, T.tout, T.par = tin, tout, par\n        T.order,\
    \ T.delta, T.Wdelta = order, delta, Wdelta\n\n    def hld_precomp(T, r = 0):\n\
    \        N, time, Va, Wa = T.N, 0, T.Va, T.Wa\n        tin, tout, size = [0]*N,\
    \ [0]*N, [1]*N+[0]\n        par, heavy, head = [-1]*N, [-1]*N, [r]*N\n       \
    \ depth, order, state = [0]*N, [0]*N, [0]*N\n        Wpar = [0]*N\n        stack\
    \ = elist(N)\n        stack.append(r)\n        while stack:\n            if (s\
    \ := state[v := stack.pop()]) == 0: # dfs down\n                p, state[v] =\
    \ par[v], 1\n                stack.append(v)\n                for i in T.range(v):\n\
    \                    if (c := Va[i]) != p:\n                        depth[c],\
    \ par[c], Wpar[c] = depth[v]+1, v, Wa[i]\n                        stack.append(c)\n\
    \n            elif s == 1: # dfs up\n                p, l = par[v], -1\n     \
    \           for i in T.range(v):\n                    if (c := Va[i]) != p:\n\
    \                        size[v] += size[c]\n                        if size[c]\
    \ > size[l]:\n                            l = c\n                heavy[v] = l\n\
    \                if p == -1:\n                    state[v] = 2\n             \
    \       stack.append(v)\n\n            elif s == 2: # decompose down\n       \
    \         p, h, l = par[v], head[v], heavy[v]\n                tin[v], order[time],\
    \ state[v] = time, v, 3\n                time += 1\n                stack.append(v)\n\
    \                \n                for i in T.range(v):\n                    if\
    \ (c := Va[i]) != p and c != l:\n                        head[c], state[c] = c,\
    \ 2\n                        stack.append(c)\n\n                if l != -1:\n\
    \                    head[l], state[l] = h, 2\n                    stack.append(l)\n\
    \n            elif s == 3: # decompose up\n                tout[v] = time\n  \
    \      T.size, T.depth = size, depth\n        T.order, T.tin, T.tout = order,\
    \ tin, tout\n        T.par, T.heavy, T.head = par, heavy, head\n        T.Wpar\
    \ = Wpar\n\n    @classmethod\n    def compile(cls, N: int, shift: int = -1):\n\
    \        return GraphWeightedBase.compile.__func__(cls, N, N-1, shift)\n    \n\
    \nclass TreeWeighted(TreeWeightedBase, GraphWeighted):\n    pass\n\n\nif __name__\
    \ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_5_B\n\
    \ndef main():\n    N = read(int)\n    T = read(TreeWeighted[N, 0])\n    _, _,\
    \ g = T.diameter(True)\n    ans = [max(ds,dg) for ds,dg in zip(T.D, T.distance(g))]\n\
    \    write(*ans, sep='\\n')\n\nfrom cp_library.io.read_fn import read\nfrom cp_library.io.write_fn\
    \ import write\nfrom cp_library.alg.tree.fast.tree_weighted_cls import TreeWeighted\n\
    \nif __name__ == '__main__':\n    main()"
  dependsOn:
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/alg/tree/fast/tree_weighted_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  - cp_library/alg/graph/fast/graph_weighted_cls.py
  - cp_library/alg/tree/fast/tree_weighted_base_cls.py
  - cp_library/alg/graph/fast/graph_weighted_base_cls.py
  - cp_library/ds/fill_fn.py
  - cp_library/alg/tree/fast/tree_base_cls.py
  - cp_library/ds/elist_fn.py
  - cp_library/math/inft_cnst.py
  - cp_library/alg/iter/argsort_fn.py
  - cp_library/alg/graph/fast/graph_base_cls.py
  - cp_library/ds/dsu_cls.py
  - cp_library/ds/heap/priority_queue_cls.py
  - cp_library/ds/heap/heap_proto.py
  - cp_library/ds/heap/heapq_max_import.py
  - cp_library/alg/graph/dfs_options_cls.py
  isVerificationFile: true
  path: test/aoj/grl/grl_5_b_fast_height.test.py
  requiredBy: []
  timestamp: '2024-12-27 22:35:21+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl/grl_5_b_fast_height.test.py
layout: document
redirect_from:
- /verify/test/aoj/grl/grl_5_b_fast_height.test.py
- /verify/test/aoj/grl/grl_5_b_fast_height.test.py.html
title: test/aoj/grl/grl_5_b_fast_height.test.py
---
