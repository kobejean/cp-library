---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/chmin_fn.py
    title: cp_library/alg/dp/chmin_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/csr/graph_base_cls.py
    title: cp_library/alg/graph/csr/graph_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/csr/graph_cls.py
    title: cp_library/alg/graph/csr/graph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/csr/snippets/cut_vertices_fn.py
    title: cp_library/alg/graph/csr/snippets/cut_vertices_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/dfs_options_cls.py
    title: cp_library/alg/graph/dfs_options_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/masks/i32_max_cnst.py
    title: cp_library/bit/masks/i32_max_cnst.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/masks/u32_max_cnst.py
    title: cp_library/bit/masks/u32_max_cnst.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/array/i32f_fn.py
    title: cp_library/ds/array/i32f_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/array/u32f_fn.py
    title: cp_library/ds/array/u32f_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/array/u8f_fn.py
    title: cp_library/ds/array/u8f_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/packet_list_cls.py
    title: cp_library/ds/packet_list_cls.py
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
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_A
  bundledCode: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_A\n\
    \ndef main():\n    N, M = read()\n    G = read(Graph[N,M,0])\n    for i,is_ap\
    \ in enumerate(cut_vertices(G)):\n        if is_ap:\n            write(i)\n\n\
    '''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n   \
    \          https://kobejean.github.io/cp-library               \n'''\nfrom typing\
    \ import Union\n\n\n\ndef chmin(dp, i, v):\n    if ch:=dp[i]>v:dp[i]=v\n    return\
    \ ch\n\n\nfrom math import inf\nfrom collections import deque\nfrom typing import\
    \ Callable, Sequence, Union, overload\n\nimport typing\nfrom numbers import Number\n\
    from types import GenericAlias \nfrom typing import Callable, Collection, Iterator,\
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
    ascii\")\ntry:\n    sys.stdin = IOWrapper.stdin = IOWrapper(sys.stdin)\n    sys.stdout\
    \ = IOWrapper.stdout = IOWrapper(sys.stdout)\nexcept:\n    pass\nfrom typing import\
    \ TypeVar\n_T = TypeVar('T')\n_U = TypeVar('U')\n\nclass TokenStream(Iterator):\n\
    \    stream = IOWrapper.stdin\n\n    def __init__(self):\n        self.queue =\
    \ deque()\n\n    def __next__(self):\n        if not self.queue: self.queue.extend(self._line())\n\
    \        return self.queue.popleft()\n    \n    def wait(self):\n        if not\
    \ self.queue: self.queue.extend(self._line())\n        while self.queue: yield\n\
    \ \n    def _line(self):\n        return TokenStream.stream.readline().split()\n\
    \n    def line(self):\n        if self.queue:\n            A = list(self.queue)\n\
    \            self.queue.clear()\n            return A\n        return self._line()\n\
    TokenStream.default = TokenStream()\n\nclass CharStream(TokenStream):\n    def\
    \ _line(self):\n        return TokenStream.stream.readline().rstrip()\nCharStream.default\
    \ = CharStream()\n\nParseFn = Callable[[TokenStream],_T]\nclass Parser:\n    def\
    \ __init__(self, spec: Union[type[_T],_T]):\n        self.parse = Parser.compile(spec)\n\
    \n    def __call__(self, ts: TokenStream) -> _T:\n        return self.parse(ts)\n\
    \    \n    @staticmethod\n    def compile_type(cls: type[_T], args = ()) -> _T:\n\
    \        if issubclass(cls, Parsable):\n            return cls.compile(*args)\n\
    \        elif issubclass(cls, (Number, str)):\n            def parse(ts: TokenStream):\
    \ return cls(next(ts))              \n            return parse\n        elif issubclass(cls,\
    \ tuple):\n            return Parser.compile_tuple(cls, args)\n        elif issubclass(cls,\
    \ Collection):\n            return Parser.compile_collection(cls, args)\n    \
    \    elif callable(cls):\n            def parse(ts: TokenStream):\n          \
    \      return cls(next(ts))              \n            return parse\n        else:\n\
    \            raise NotImplementedError()\n    \n    @staticmethod\n    def compile(spec:\
    \ Union[type[_T],_T]=int) -> ParseFn[_T]:\n        if isinstance(spec, (type,\
    \ GenericAlias)):\n            cls = typing.get_origin(spec) or spec\n       \
    \     args = typing.get_args(spec) or tuple()\n            return Parser.compile_type(cls,\
    \ args)\n        elif isinstance(offset := spec, Number): \n            cls =\
    \ type(spec)  \n            def parse(ts: TokenStream): return cls(next(ts)) +\
    \ offset\n            return parse\n        elif isinstance(args := spec, tuple):\
    \      \n            return Parser.compile_tuple(type(spec), args)\n        elif\
    \ isinstance(args := spec, Collection):\n            return Parser.compile_collection(type(spec),\
    \ args)\n        elif isinstance(fn := spec, Callable): \n            def parse(ts:\
    \ TokenStream): return fn(next(ts))\n            return parse\n        else:\n\
    \            raise NotImplementedError()\n\n    @staticmethod\n    def compile_line(cls:\
    \ _T, spec=int) -> ParseFn[_T]:\n        if spec is int:\n            fn = Parser.compile(spec)\n\
    \            def parse(ts: TokenStream): return cls([int(token) for token in ts.line()])\n\
    \            return parse\n        else:\n            fn = Parser.compile(spec)\n\
    \            def parse(ts: TokenStream): return cls([fn(ts) for _ in ts.wait()])\n\
    \            return parse\n\n    @staticmethod\n    def compile_repeat(cls: _T,\
    \ spec, N) -> ParseFn[_T]:\n        fn = Parser.compile(spec)\n        def parse(ts:\
    \ TokenStream): return cls([fn(ts) for _ in range(N)])\n        return parse\n\
    \n    @staticmethod\n    def compile_children(cls: _T, specs) -> ParseFn[_T]:\n\
    \        fns = tuple((Parser.compile(spec) for spec in specs))\n        def parse(ts:\
    \ TokenStream): return cls([fn(ts) for fn in fns])  \n        return parse\n \
    \           \n    @staticmethod\n    def compile_tuple(cls: type[_T], specs) ->\
    \ ParseFn[_T]:\n        if isinstance(specs, (tuple,list)) and len(specs) == 2\
    \ and specs[1] is ...:\n            return Parser.compile_line(cls, specs[0])\n\
    \        else:\n            return Parser.compile_children(cls, specs)\n\n   \
    \ @staticmethod\n    def compile_collection(cls, specs):\n        if not specs\
    \ or len(specs) == 1 or isinstance(specs, set):\n            return Parser.compile_line(cls,\
    \ *specs)\n        elif (isinstance(specs, (tuple,list)) and len(specs) == 2 and\
    \ isinstance(specs[1], int)):\n            return Parser.compile_repeat(cls, specs[0],\
    \ specs[1])\n        else:\n            raise NotImplementedError()\n\nclass Parsable:\n\
    \    @classmethod\n    def compile(cls):\n        def parser(ts: TokenStream):\
    \ return cls(next(ts))\n        return parser\n    \n    @classmethod\n    def\
    \ __class_getitem__(cls, item):\n        return GenericAlias(cls, item)\n\nfrom\
    \ enum import auto, IntFlag, IntEnum\n\nclass DFSFlags(IntFlag):\n    ENTER =\
    \ auto()\n    DOWN = auto()\n    BACK = auto()\n    CROSS = auto()\n    LEAVE\
    \ = auto()\n    UP = auto()\n    MAXDEPTH = auto()\n\n    RETURN_PARENTS = auto()\n\
    \    RETURN_DEPTHS = auto()\n    BACKTRACK = auto()\n    CONNECT_ROOTS = auto()\n\
    \n    # Common combinations\n    ALL_EDGES = DOWN | BACK | CROSS\n    EULER_TOUR\
    \ = DOWN | UP\n    INTERVAL = ENTER | LEAVE\n    TOPDOWN = DOWN | CONNECT_ROOTS\n\
    \    BOTTOMUP = UP | CONNECT_ROOTS\n    RETURN_ALL = RETURN_PARENTS | RETURN_DEPTHS\n\
    \nclass DFSEvent(IntEnum):\n    ENTER = DFSFlags.ENTER \n    DOWN = DFSFlags.DOWN\
    \ \n    BACK = DFSFlags.BACK \n    CROSS = DFSFlags.CROSS \n    LEAVE = DFSFlags.LEAVE\
    \ \n    UP = DFSFlags.UP \n    MAXDEPTH = DFSFlags.MAXDEPTH\n    \n\nclass GraphBase(Parsable):\n\
    \    def __init__(G, N: int, M: int, U: list[int], V: list[int], \n          \
    \       deg: list[int], La: list[int], Ra: list[int],\n                 Ua: list[int],\
    \ Va: list[int], Ea: list[int], twin: list[int] = None):\n        G.N = N\n  \
    \      '''The number of vertices.'''\n        G.M = M\n        '''The number of\
    \ edges.'''\n        G.U = U\n        '''A list of source vertices in the original\
    \ edge list.'''\n        G.V = V\n        '''A list of destination vertices in\
    \ the original edge list.'''\n        G.deg = deg\n        '''deg[u] is the out\
    \ degree of vertex u.'''\n        G.La = La\n        '''La[u] stores the start\
    \ index of the list of adjacent vertices from u.'''\n        G.Ra = Ra\n     \
    \   '''Ra[u] stores the stop index of the list of adjacent vertices from u.'''\n\
    \        G.Ua = Ua\n        '''Ua[i] = u for La[u] <= i < Ra[u], useful for backtracking.'''\n\
    \        G.Va = Va\n        '''Va[i] lists adjacent vertices to u for La[u] <=\
    \ i < Ra[u].'''\n        G.Ea = Ea\n        '''Ea[i] lists the edge ids that start\
    \ from u for La[u] <= i < Ra[u].\n        For undirected graphs, edge ids in range\
    \ M<= e <2*M are edges from V[e-M] -> U[e-M].\n        '''\n        G.twin = twin\
    \ if twin is not None else range(len(Ua))\n        '''twin[i] in undirected graphs\
    \ stores index j of the same edge but with u and v swapped.'''\n        G.st:\
    \ list[int] = None\n        G.order: list[int] = None\n        G.vis: list[int]\
    \ = None\n        G.back: list[int] = None\n        G.tin: list[int] = None\n\
    \    \n    def clear(G):\n        G.vis = G.back = G.tin = None\n\n    def prep_vis(G):\n\
    \        if G.vis is None: G.vis = u8f(G.N)\n        return G.vis\n    \n    def\
    \ prep_st(G):\n        if G.st is None: G.st = elist(G.N)\n        else: G.st.clear()\n\
    \        return G.st\n    \n    def prep_order(G):\n        if G.order is None:\
    \ G.order = elist(G.N)\n        else: G.order.clear()\n        return G.order\n\
    \    \n    def prep_back(G):\n        if G.back is None: G.back = i32f(G.N, -2)\n\
    \        return G.back\n    \n    def prep_tin(G):\n        if G.tin is None:\
    \ G.tin = i32f(G.N, -1)\n        return G.tin\n\n    def __len__(G) -> int: return\
    \ G.N\n    def __getitem__(G, u): return G.Va[G.La[u]:G.Ra[u]]\n    def range(G,\
    \ u): return range(G.La[u],G.Ra[u])\n    \n    @overload\n    def distance(G)\
    \ -> list[list[int]]: ...\n    @overload\n    def distance(G, s: int = 0) -> list[int]:\
    \ ...\n    @overload\n    def distance(G, s: int, g: int) -> int: ...\n    def\
    \ distance(G, s = None, g = None):\n        if s == None: return G.floyd_warshall()\n\
    \        else: return G.bfs(s, g)\n\n    def recover_path(G, s, t):\n        Ua,\
    \ back, vertices = G.Ua, G.back, u32f(1, v := t)\n        while v != s: vertices.append(v\
    \ := Ua[back[v]])\n        return vertices\n    \n    def recover_path_edge_ids(G,\
    \ s, t):\n        Ea, Ua, back, edges, v = G.Ea, G.Ua, G.back, u32f(0), t\n  \
    \      while v != s: edges.append(Ea[i := back[v]]), (v := Ua[i])\n        return\
    \ edges\n\n    def shortest_path(G, s: int, t: int):\n        if G.distance(s,\
    \ t) >= inf: return None\n        vertices = G.recover_path(s, t)\n        vertices.reverse()\n\
    \        return vertices\n    \n    def shortest_path_edge_ids(G, s: int, t: int):\n\
    \        if G.distance(s, t) >= inf: return None\n        edges = G.recover_path_edge_ids(s,\
    \ t)\n        edges.reverse()\n        return edges\n    \n    @overload\n   \
    \ def bfs(G, s: Union[int,list] = 0) -> list[int]: ...\n    @overload\n    def\
    \ bfs(G, s: Union[int,list], g: int) -> int: ...\n    def bfs(G, s: int = 0, g:\
    \ int = None):\n        S, Va, back, D = G.starts(s), G.Va, i32f(N := G.N, -1),\
    \ [inf]*N\n        G.back, G.D = back, D\n        for u in S: D[u] = 0\n     \
    \   que = deque(S)\n        while que:\n            nd = D[u := que.popleft()]+1\n\
    \            if u == g: return nd-1\n            for i in G.range(u):\n      \
    \          if nd < D[v := Va[i]]:\n                    D[v], back[v] = nd, i\n\
    \                    que.append(v)\n        return D if g is None else inf \n\n\
    \    def floyd_warshall(G) -> list[list[int]]:\n        G.D = D = [[inf]*G.N for\
    \ _ in range(G.N)]\n        for u in range(G.N): D[u][u] = 0\n        for i in\
    \ range(len(G.Ua)): D[G.Ua[i]][G.Va[i]] = 1\n        for k, Dk in enumerate(D):\n\
    \            for Di in D:\n                if (Dik := Di[k]) == inf: continue\n\
    \                for j in range(G.N):\n                    chmin(Di, j, Dik+Dk[j])\n\
    \        return D\n\n    def find_cycle_indices(G, s: Union[int, None] = None):\n\
    \        Ea, Ua, Va, vis, back = G.Ea, G. Ua, G.Va, u8f(N := G.N), u32f(N, i32_max)\n\
    \        G.vis, G.back, st = vis, back, elist(N)\n        for s in G.starts(s):\n\
    \            if vis[s]: continue\n            st.append(s)\n            while\
    \ st:\n                if not vis[u := st.pop()]:\n                    st.append(u)\n\
    \                    vis[u], pe = 1, Ea[j] if (j := back[u]) != i32_max else i32_max\n\
    \                    for i in G.range(u):\n                        if not vis[v\
    \ := Va[i]]:\n                            back[v] = i\n                      \
    \      st.append(v)\n                        elif vis[v] == 1 and pe != Ea[i]:\n\
    \                            I = u32f(1,i)\n                            while\
    \ v != u: I.append(i := back[u]), (u := Ua[i])\n                            I.reverse()\n\
    \                            return I\n                else:\n               \
    \     vis[u] = 2\n        # check for self loops\n        for i in range(len(Ua)):\n\
    \            if Ua[i] == Va[i]:\n                return u32f(1,i)\n    \n    def\
    \ find_cycle(G, s: Union[int, None] = None):\n        if I := G.find_cycle_indices(s):\
    \ return [G.Ua[i] for i in I]\n    \n    def find_cycle_edge_ids(G, s: Union[int,\
    \ None] = None):\n        if I := G.find_cycle_indices(s): return [G.Ea[i] for\
    \ i in I]\n\n    def find_minimal_cycle(G, s=0):\n        D, par, que, Va = u32f(N\
    \ := G.N, u32_max), i32f(N, -1), deque([s]), G.Va\n        D[s] = 0\n        while\
    \ que:\n            for i in G.range(u := que.popleft()):\n                if\
    \ (v := Va[i]) == s:  # Found cycle back to start\n                    cycle =\
    \ [u]\n                    while u != s: cycle.append(u := par[u])\n         \
    \           return cycle\n                if D[v] < u32_max: continue\n      \
    \          D[v], par[v] = D[u]+1, u; que.append(v)\n\n    def dfs_topdown(G, s:\
    \ Union[int,list] = None) -> list[int]:\n        '''Returns lists of indices i\
    \ where Ua[i] -> Va[i] are edges in order of top down discovery'''\n        vis,\
    \ st, order = G.prep_vis(), G.prep_st(), G.prep_order()\n        for s in G.starts(s):\n\
    \            if vis[s]: continue\n            vis[s] = 1; st.append(s) \n    \
    \        while st:\n                for i in G.range(st.pop()):\n            \
    \        if vis[v := G.Va[i]]: continue\n                    vis[v] = 1; order.append(i);\
    \ st.append(v)\n        return order\n\n    def dfs(G, s: Union[int,list] = None,\
    \ /, \n            backtrack = False,\n            max_depth = None,\n       \
    \     enter_fn: Callable[[int],None] = None,\n            leave_fn: Callable[[int],None]\
    \ = None,\n            max_depth_fn: Callable[[int],None] = None,\n          \
    \  down_fn: Callable[[int,int,int],None] = None,\n            back_fn: Callable[[int,int,int],None]\
    \ = None,\n            forward_fn: Callable[[int,int,int],None] = None,\n    \
    \        cross_fn: Callable[[int,int,int],None] = None,\n            up_fn: Callable[[int,int,int],None]\
    \ = None):\n        I, time, vis, st, back, tin = G.La[:], -1, G.prep_vis(), G.prep_st(),\
    \ G.prep_back(), G.prep_tin()\n        for s in G.starts(s):\n            if vis[s]:\
    \ continue\n            back[s], tin[s] = -1, (time := time+1); st.append(s)\n\
    \            while st:\n                if vis[u := st[-1]] == 0:\n          \
    \          vis[u] = 1\n                    if enter_fn: enter_fn(u)\n        \
    \            if max_depth is not None and len(st) > max_depth:\n             \
    \           I[u] = G.Ra[u]\n                        if max_depth_fn: max_depth_fn(u)\n\
    \                if (i := I[u]) < G.Ra[u]:\n                    I[u] += 1\n  \
    \                  if (s := vis[v := G.Va[i]]) == 0:\n                       \
    \ back[v], tin[v] = i, (time := time+1); st.append(v)\n                      \
    \  if down_fn: down_fn(u,v,i)\n                    elif back_fn and s == 1 and\
    \ back[u] != G.twin[i]: back_fn(u,v,i)\n                    elif (cross_fn or\
    \ forward_fn) and s == 2:\n                        if forward_fn and tin[u] <\
    \ tin[v]: forward_fn(u,v,i)\n                        elif cross_fn: cross_fn(u,v,i)\n\
    \                else:\n                    vis[u] = 2; st.pop()\n           \
    \         if backtrack: vis[u], I[u] = 0, G.La[u]\n                    if leave_fn:\
    \ leave_fn(u)\n                    if up_fn and st: up_fn(u, st[-1], back[u])\n\
    \    \n    def dfs_enter_leave(G, s: Union[int,list[int],None] = None) -> Sequence[tuple[DFSEvent,int]]:\n\
    \        N, I = G.N, G.La[:]\n        st, back, plst = elist(N), i32f(N,-2), PacketList(order\
    \ := elist(2*N), N-1)\n        G.back, ENTER, LEAVE = back, int(DFSEvent.ENTER)\
    \ << plst.shift, int(DFSEvent.LEAVE) << plst.shift\n        for s in G.starts(s):\n\
    \            if back[s] >= -1: continue\n            back[s] = -1\n          \
    \  order.append(ENTER | s), st.append(s)\n            while st:\n            \
    \    if (i := I[u := st[-1]]) < G.Ra[u]:\n                    I[u] += 1\n    \
    \                if back[v := G.Va[i]] >= -1: continue\n                    back[v]\
    \ = i; order.append(ENTER | v); st.append(v)\n                else:\n        \
    \            order.append(LEAVE | u); st.pop()\n        return plst\n    \n  \
    \  def starts(G, s: Union[int,list[int],None] = None) -> list[int]:\n        if\
    \ isinstance(s, int): return [s]\n        elif s is None: return range(G.N)\n\
    \        elif isinstance(s, list): return s\n        else: return list(s)\n\n\
    \    @classmethod\n    def compile(cls, N: int, M: int, shift: int = -1):\n  \
    \      def parse(ts: TokenStream):\n            U, V = u32f(M), u32f(M)\n    \
    \        for i in range(M):\n                u, v = ts._line()\n             \
    \   U[i], V[i] = int(u)+shift, int(v)+shift\n            return cls(N, U, V)\n\
    \        return parse\n\n\nu32_max = (1<<32)-1\ni32_max = (1<<31)-1\n\n\nfrom\
    \ array import array\ndef u8f(N: int, elm: int = 0):      return array('B', (elm,))*N\
    \  # unsigned char\ndef u32f(N: int, elm: int = 0):     return array('I', (elm,))*N\
    \  # unsigned int\ndef i32f(N: int, elm: int = 0):     return array('i', (elm,))*N\
    \  # signed int\n\ndef elist(est_len: int) -> list: ...\ntry:\n    from __pypy__\
    \ import newlist_hint\nexcept:\n    def newlist_hint(hint):\n        return []\n\
    elist = newlist_hint\n    \n\nclass PacketList(Sequence[tuple[int,int]]):\n  \
    \  def __init__(lst, A: list[int], max1: int):\n        lst.A = A\n        lst.mask\
    \ = (1 << (shift := (max1).bit_length())) - 1\n        lst.shift = shift\n   \
    \ def __len__(lst): return lst.A.__len__()\n    def __contains__(lst, x: tuple[int,int]):\
    \ return lst.A.__contains__(x[0] << lst.shift | x[1])\n    def __getitem__(lst,\
    \ key) -> tuple[int,int]:\n        x = lst.A[key]\n        return x >> lst.shift,\
    \ x & lst.mask\n\ndef cut_vertices(G: GraphBase, s: Union[int,list,None] = None):\n\
    \    '''\n    Find cut vertices in an undirected graph using DFS edge types.\n\
    \    Returns a boolean list that is True for indices of cut vertices.\n    '''\n\
    \    low, children, ap = [N := G.N]*N, [0]*N, [False]*N\n\n    def enter(v):\n\
    \        low[v] = G.tin[v]\n\n    def back(u,v,i):\n        chmin(low, u, G.tin[v])\n\
    \n    def up(u,p,i):\n        children[p] += 1\n        if G.back[p] < 0:\n  \
    \          # root case\n            ap[p] |= children[p] > 1\n        else:\n\
    \            chmin(low, p, low[u])\n            ap[p] |= low[u] >= G.tin[p]\n\n\
    \    G.dfs(s, enter_fn=enter, back_fn=back, up_fn=up)\n    return ap\n\nclass\
    \ Graph(GraphBase):\n    def __init__(G, N: int, U: list[int], V: list[int]):\n\
    \        M, Ma, deg = len(U), 0, u32f(N)\n        for e in range(M := len(U)):\n\
    \            distinct = (u := U[e]) != (v := V[e])\n            deg[u] += 1; deg[v]\
    \ += distinct; Ma += 1+distinct\n        twin, Ea, Ua, Va, La, Ra, i = i32f(Ma),\
    \ i32f(Ma), u32f(Ma), u32f(Ma), u32f(N), u32f(N), 0\n        for u in range(N):\
    \ La[u] = Ra[u] = i; i = i+deg[u]\n        for e in range(M):\n            i,\
    \ j = Ra[u := U[e]], Ra[v := V[e]]\n            Ra[u], Ua[i], Va[i], Ea[i], twin[i]\
    \ = i+1, u, v, e, j\n            if i == j: continue\n            Ra[v], Ua[j],\
    \ Va[j], Ea[j], twin[j] = j+1, v, u, e, i\n        super().__init__(N, M, U, V,\
    \ deg, La, Ra, Ua, Va, Ea, twin)\n\nfrom typing import Type, Union, overload\n\
    \n@overload\ndef read() -> list[int]: ...\n@overload\ndef read(spec: Type[_T],\
    \ char=False) -> _T: ...\n@overload\ndef read(spec: _U, char=False) -> _U: ...\n\
    @overload\ndef read(*specs: Type[_T], char=False) -> tuple[_T, ...]: ...\n@overload\n\
    def read(*specs: _U, char=False) -> tuple[_U, ...]: ...\ndef read(*specs: Union[Type[_T],_U],\
    \ char=False):\n    if not char and not specs: return [int(s) for s in TokenStream.default.line()]\n\
    \    parser: _T = Parser.compile(specs[0] if len(specs) == 1 else specs)\n   \
    \ return parser(CharStream.default if char else TokenStream.default)\n\ndef write(*args,\
    \ **kwargs):\n    '''Prints the values to a stream, or to stdout_fast by default.'''\n\
    \    sep, file = kwargs.pop(\"sep\", \" \"), kwargs.pop(\"file\", IOWrapper.stdout)\n\
    \    at_start = True\n    for x in args:\n        if not at_start:\n         \
    \   file.write(sep)\n        file.write(str(x))\n        at_start = False\n  \
    \  file.write(kwargs.pop(\"end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n\
    \        file.flush()\n\nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_A\n\
    \ndef main():\n    N, M = read()\n    G = read(Graph[N,M,0])\n    for i,is_ap\
    \ in enumerate(cut_vertices(G)):\n        if is_ap:\n            write(i)\n\n\
    from cp_library.alg.graph.csr.snippets.cut_vertices_fn import cut_vertices\nfrom\
    \ cp_library.alg.graph.csr.graph_cls import Graph\nfrom cp_library.io.read_fn\
    \ import read\nfrom cp_library.io.write_fn import write\n\nif __name__ == '__main__':\n\
    \    main()"
  dependsOn:
  - cp_library/alg/graph/csr/snippets/cut_vertices_fn.py
  - cp_library/alg/graph/csr/graph_cls.py
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/alg/dp/chmin_fn.py
  - cp_library/alg/graph/csr/graph_base_cls.py
  - cp_library/ds/array/i32f_fn.py
  - cp_library/ds/array/u32f_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  - cp_library/alg/graph/dfs_options_cls.py
  - cp_library/bit/masks/u32_max_cnst.py
  - cp_library/bit/masks/i32_max_cnst.py
  - cp_library/ds/array/u8f_fn.py
  - cp_library/ds/elist_fn.py
  - cp_library/ds/packet_list_cls.py
  isVerificationFile: true
  path: test/aoj/grl/grl_3_a_graph_articulation_points.test.py
  requiredBy: []
  timestamp: '2025-07-10 00:37:15+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl/grl_3_a_graph_articulation_points.test.py
layout: document
redirect_from:
- /verify/test/aoj/grl/grl_3_a_graph_articulation_points.test.py
- /verify/test/aoj/grl/grl_3_a_graph_articulation_points.test.py.html
title: test/aoj/grl/grl_3_a_graph_articulation_points.test.py
---
