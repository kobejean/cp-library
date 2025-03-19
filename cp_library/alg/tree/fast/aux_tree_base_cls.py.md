---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/chmin_fn.py
    title: cp_library/alg/dp/chmin_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/sort2_fn.py
    title: cp_library/alg/dp/sort2_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/dfs_options_cls.py
    title: cp_library/alg/graph/dfs_options_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/fast/graph_base_cls.py
    title: cp_library/alg/graph/fast/graph_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/argsort_fn.py
    title: cp_library/alg/iter/argsort_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/presum_fn.py
    title: cp_library/alg/iter/presum_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/fast/tree_base_cls.py
    title: cp_library/alg/tree/fast/tree_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/lca_table_iterative_cls.py
    title: cp_library/alg/tree/lca_table_iterative_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack_sm_fn.py
    title: cp_library/bit/pack_sm_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/array_init_fn.py
    title: cp_library/ds/array_init_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/min_sparse_table_cls.py
    title: cp_library/ds/min_sparse_table_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/packet_list_cls.py
    title: cp_library/ds/packet_list_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/fast/aux_tree_cls.py
    title: cp_library/alg/tree/fast/aux_tree_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/fast/aux_tree_weighted_cls.py
    title: cp_library/alg/tree/fast/aux_tree_weighted_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/vol/0439_aux_dijkstra.test.py
    title: test/aoj/vol/0439_aux_dijkstra.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/vol/0439_aux_rerooting_dp.test.py
    title: test/aoj/vol/0439_aux_rerooting_dp.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/vol/0439_aux_weighted_rerooting_dp.test.py
    title: test/aoj/vol/0439_aux_weighted_rerooting_dp.test.py
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
    from typing import Callable, Literal, TypeVar, Union, overload\nfrom math import\
    \ inf\nfrom collections import deque\nfrom typing import Callable, Sequence, Union,\
    \ overload\n\nimport typing\nfrom numbers import Number\nfrom types import GenericAlias\
    \ \nfrom typing import Callable, Collection, Iterator, Union\nimport os\nimport\
    \ sys\nfrom io import BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n    BUFSIZE\
    \ = 8192\n    newlines = 0\n\n    def __init__(self, file):\n        self._fd\
    \ = file.fileno()\n        self.buffer = BytesIO()\n        self.writable = \"\
    x\" in file.mode or \"r\" not in file.mode\n        self.write = self.buffer.write\
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
    \ = IOWrapper(sys.stdout)\n_T = TypeVar('T')\n\nclass TokenStream(Iterator):\n\
    \    stream = IOWrapper.stdin\n\n    def __init__(self):\n        self.queue =\
    \ deque()\n\n    def __next__(self):\n        if not self.queue: self.queue.extend(self._line())\n\
    \        return self.queue.popleft()\n    \n    def wait(self):\n        if not\
    \ self.queue: self.queue.extend(self._line())\n        while self.queue: yield\n\
    \ \n    def _line(self):\n        return TokenStream.stream.readline().split()\n\
    \n    def line(self):\n        if self.queue:\n            A = list(self.queue)\n\
    \            self.queue.clear()\n            return A\n        return self._line()\n\
    TokenStream.default = TokenStream()\n\nclass CharStream(TokenStream):\n    def\
    \ _line(self):\n        return TokenStream.stream.readline().rstrip()\nCharStream.default\
    \ = CharStream()\n\n\nParseFn = Callable[[TokenStream],_T]\nclass Parser:\n  \
    \  def __init__(self, spec: Union[type[_T],_T]):\n        self.parse = Parser.compile(spec)\n\
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
    \ isinstance(args := spec, Collection):  \n            return Parser.compile_collection(type(spec),\
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
    \ return cls(next(ts))\n        return parser\n\n\n\ndef chmin(dp, i, v):\n  \
    \  if ch:=dp[i]>v:dp[i]=v\n    return ch\n\n\n\nfrom enum import auto, IntFlag,\
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
    \ = None\n        G.back: list[int] = None\n        G.tin: list[int] = None\n\n\
    \    def prep_vis(G):\n        if G.vis is None: G.vis = u8f(G.N)\n        return\
    \ G.vis\n    \n    def prep_st(G):\n        if G.st is None: G.st = elist(G.N)\n\
    \        else: G.st.clear()\n        return G.st\n    \n    def prep_order(G):\n\
    \        if G.order is None: G.order = elist(G.N)\n        else: G.order.clear()\n\
    \        return G.order\n    \n    def prep_back(G):\n        if G.back is None:\
    \ G.back = i32f(G.N, -2)\n        return G.back\n    \n    def prep_tin(G):\n\
    \        if G.tin is None: G.tin = i32f(G.N, -1)\n        return G.tin\n    \n\
    \    def __len__(G) -> int: return G.N\n    def __getitem__(G, u): return G.Va[G.La[u]:G.Ra[u]]\n\
    \    def range(G, u): return range(G.La[u],G.Ra[u])\n    \n    @overload\n   \
    \ def distance(G) -> list[list[int]]: ...\n    @overload\n    def distance(G,\
    \ s: int = 0) -> list[int]: ...\n    @overload\n    def distance(G, s: int, g:\
    \ int) -> int: ...\n    def distance(G, s = None, g = None):\n        if s ==\
    \ None: return G.floyd_warshall()\n        else: return G.bfs(s, g)\n\n    def\
    \ recover_path(G, s, t):\n        Ua, back, vertices = G.Ua, G.back, u32f(1, v\
    \ := t)\n        while v != s: vertices.append(v := Ua[back[v]])\n        return\
    \ vertices\n    \n    def recover_path_edge_ids(G, s, t):\n        Ea, Ua, back,\
    \ edges, v = G.Ea, G.Ua, G.back, u32f(0), t\n        while v != s: edges.append(Ea[i\
    \ := back[v]]), (v := Ua[i])\n        return edges\n\n    def shortest_path(G,\
    \ s: int, t: int):\n        if G.distance(s, t) >= inf: return None\n        vertices\
    \ = G.recover_path(s, t)\n        vertices.reverse()\n        return vertices\n\
    \    \n    def shortest_path_edge_ids(G, s: int, t: int):\n        if G.distance(s,\
    \ t) >= inf: return None\n        edges = G.recover_path_edge_ids(s, t)\n    \
    \    edges.reverse()\n        return edges\n    \n    @overload\n    def bfs(G,\
    \ s: Union[int,list] = 0) -> list[int]: ...\n    @overload\n    def bfs(G, s:\
    \ Union[int,list], g: int) -> int: ...\n    def bfs(G, s: int = 0, g: int = None):\n\
    \        S, Va, back, D = G.starts(s), G.Va, i32f(N := G.N, -1), [inf]*N\n   \
    \     G.back, G.D = back, D\n        for u in S: D[u] = 0\n        que = deque(S)\n\
    \        while que:\n            nd = D[u := que.popleft()]+1\n            if\
    \ u == g: return nd-1\n            for i in G.range(u):\n                if nd\
    \ < D[v := Va[i]]:\n                    D[v], back[v] = nd, i\n              \
    \      que.append(v)\n        return D if g is None else inf \n\n    def floyd_warshall(G)\
    \ -> list[list[int]]:\n        G.D = D = [[inf]*G.N for _ in range(G.N)]\n   \
    \     for u in range(G.N): D[u][u] = 0\n        for i in range(len(G.Ua)): D[G.Ua[i]][G.Va[i]]\
    \ = 1\n        for k, Dk in enumerate(D):\n            for Di in D:\n        \
    \        if (Dik := Di[k]) == inf: continue\n                for j in range(G.N):\n\
    \                    chmin(Di, j, Dik+Dk[j])\n        return D\n\n    def find_cycle_indices(G,\
    \ s: Union[int, None] = None):\n        Ea, Ua, Va, vis, back = G.Ea, G. Ua, G.Va,\
    \ u8f(N := G.N), u32f(N, i32_max)\n        G.vis, G.back, st = vis, back, elist(N)\n\
    \        for s in G.starts(s):\n            if vis[s]: continue\n            st.append(s)\n\
    \            while st:\n                if not vis[u := st.pop()]:\n         \
    \           st.append(u)\n                    vis[u], pe = 1, Ea[j] if (j := back[u])\
    \ != i32_max else i32_max\n                    for i in G.range(u):\n        \
    \                if not vis[v := Va[i]]:\n                            back[v]\
    \ = i\n                            st.append(v)\n                        elif\
    \ vis[v] == 1 and pe != Ea[i]:\n                            I = u32f(1,i)\n  \
    \                          while v != u: I.append(i := back[u]), (u := Ua[i])\n\
    \                            I.reverse()\n                            return I\n\
    \                else:\n                    vis[u] = 2\n        # check for self\
    \ loops\n        for i in range(len(Ua)):\n            if Ua[i] == Va[i]:\n  \
    \              return u32f(1,i)\n    \n    def find_cycle(G, s: Union[int, None]\
    \ = None):\n        if I := G.find_cycle_indices(s): return [G.Ua[i] for i in\
    \ I]\n    \n    def find_cycle_edge_ids(G, s: Union[int, None] = None):\n    \
    \    if I := G.find_cycle_indices(s): return [G.Ea[i] for i in I]\n\n    def find_minimal_cycle(G,\
    \ s=0):\n        D, par, que, Va = u32f(N := G.N, u32_max), i32f(N, -1), deque([s]),\
    \ G.Va\n        D[s] = 0\n        while que:\n            for i in G.range(u :=\
    \ que.popleft()):\n                if (v := Va[i]) == s:  # Found cycle back to\
    \ start\n                    cycle = [u]\n                    while u != s: cycle.append(u\
    \ := par[u])\n                    return cycle\n                if D[v] < u32_max:\
    \ continue\n                D[v], par[v] = D[u]+1, u; que.append(v)\n\n    def\
    \ dfs_topdown(G, s: Union[int,list] = None) -> list[int]:\n        '''Returns\
    \ lists of indices i where Ua[i] -> Va[i] are edges in order of top down discovery'''\n\
    \        vis, st, order = G.prep_vis(), G.prep_st(), G.prep_order()\n        for\
    \ s in G.starts(s):\n            if vis[s]: continue\n            vis[s] = 1;\
    \ st.append(s) \n            while st:\n                for i in G.range(st.pop()):\n\
    \                    if vis[v := G.Va[i]]: continue\n                    vis[v]\
    \ = 1; order.append(i); st.append(v)\n        return order\n\n    def dfs(G, s:\
    \ Union[int,list] = None, /, \n            backtrack = False,\n            max_depth\
    \ = None,\n            enter_fn: Callable[[int],None] = None,\n            leave_fn:\
    \ Callable[[int],None] = None,\n            max_depth_fn: Callable[[int],None]\
    \ = None,\n            down_fn: Callable[[int,int,int],None] = None,\n       \
    \     back_fn: Callable[[int,int,int],None] = None,\n            forward_fn: Callable[[int,int,int],None]\
    \ = None,\n            cross_fn: Callable[[int,int,int],None] = None,\n      \
    \      up_fn: Callable[[int,int,int],None] = None):\n        I, time, vis, st,\
    \ back, tin = G.La[:], -1, G.prep_vis(), G.prep_st(), G.prep_back(), G.prep_tin()\n\
    \        for s in G.starts(s):\n            if vis[s]: continue\n            back[s],\
    \ tin[s] = -1, (time := time+1); st.append(s)\n            while st:\n       \
    \         if vis[u := st[-1]] == 0:\n                    vis[u] = 1\n        \
    \            if enter_fn: enter_fn(u)\n                    if max_depth is not\
    \ None and len(st) > max_depth:\n                        I[u] = G.Ra[u]\n    \
    \                    if max_depth_fn: max_depth_fn(u)\n                if (i :=\
    \ I[u]) < G.Ra[u]:\n                    I[u] += 1\n                    if (s :=\
    \ vis[v := G.Va[i]]) == 0:\n                        back[v], tin[v] = i, (time\
    \ := time+1); st.append(v)\n                        if down_fn: down_fn(u,v,i)\n\
    \                    elif back_fn and s == 1 and back[u] != G.twin[i]: back_fn(u,v,i)\n\
    \                    elif (cross_fn or forward_fn) and s == 2:\n             \
    \           if forward_fn and tin[u] < tin[v]: forward_fn(u,v,i)\n           \
    \             elif cross_fn: cross_fn(u,v,i)\n                else:\n        \
    \            vis[u] = 2; st.pop()\n                    if backtrack: vis[u], I[u]\
    \ = 0, G.La[u]\n                    if leave_fn: leave_fn(u)\n               \
    \     if up_fn and st: up_fn(u, st[-1], back[u])\n    \n    def dfs_enter_leave(G,\
    \ s: Union[int,list[int],None] = None) -> Sequence[tuple[DFSEvent,int]]:\n   \
    \     N, I = G.N, G.La[:]\n        st, back, plst = elist(N), i32f(N,-2), PacketList(order\
    \ := elist(2*N), N-1)\n        G.back, ENTER, LEAVE = back, int(DFSEvent.ENTER)\
    \ << plst.shift, int(DFSEvent.LEAVE) << plst.shift\n        for s in G.starts(s):\n\
    \            if back[s] >= -1: continue\n            back[s] = -1\n          \
    \  order.append(ENTER | s), st.append(s)\n            while st:\n            \
    \    if (i := I[u := st[-1]]) < G.Ra[u]:\n                    I[u] += 1\n    \
    \                if back[v := G.Va[i]] >= -1: continue\n                    back[v]\
    \ = i; order.append(ENTER | v); st.append(v)\n                else:\n        \
    \            order.append(LEAVE | u); st.pop()\n        return plst\n    \n  \
    \  def starts(G, s: Union[int,list[int],None]) -> list[int]:\n        if isinstance(s,\
    \ int): return [s]\n        elif s is None: return range(G.N)\n        elif isinstance(s,\
    \ list): return s\n        else: return list(s)\n\n    @classmethod\n    def compile(cls,\
    \ N: int, M: int, shift: int = -1):\n        def parse(ts: TokenStream):\n   \
    \         U, V = u32f(M), u32f(M)\n            for i in range(M):\n          \
    \      u, v = ts._line()\n                U[i], V[i] = int(u)+shift, int(v)+shift\n\
    \            return cls(N, U, V)\n        return parse\n    \n\n\ndef elist(est_len:\
    \ int) -> list: ...\ntry:\n    from __pypy__ import newlist_hint\nexcept:\n  \
    \  def newlist_hint(hint):\n        return []\nelist = newlist_hint\n    \nfrom\
    \ typing import Iterable\nfrom array import array\n\ndef i8f(N: int, elm: int\
    \ = 0):      return array('b', (elm,))*N  # signed char\ndef u8f(N: int, elm:\
    \ int = 0):      return array('B', (elm,))*N  # unsigned char\ndef i16f(N: int,\
    \ elm: int = 0):     return array('h', (elm,))*N  # signed short\ndef u16f(N:\
    \ int, elm: int = 0):     return array('H', (elm,))*N  # unsigned short\ndef i32f(N:\
    \ int, elm: int = 0):     return array('i', (elm,))*N  # signed int\ndef u32f(N:\
    \ int, elm: int = 0):     return array('I', (elm,))*N  # unsigned int\ndef i64f(N:\
    \ int, elm: int = 0):     return array('q', (elm,))*N  # signed long long\n# def\
    \ u64f(N: int, elm: int = 0):     return array('Q', (elm,))*N  # unsigned long\
    \ long\ndef f32f(N: int, elm: float = 0.0): return array('f', (elm,))*N  # float\n\
    def f64f(N: int, elm: float = 0.0): return array('d', (elm,))*N  # double\n\n\
    def i8a(init = None):  return array('b') if init is None else array('b', init)\
    \  # signed char\ndef u8a(init = None):  return array('B') if init is None else\
    \ array('B', init)  # unsigned char\ndef i16a(init = None): return array('h')\
    \ if init is None else array('h', init)  # signed short\ndef u16a(init = None):\
    \ return array('H') if init is None else array('H', init)  # unsigned short\n\
    def i32a(init = None): return array('i') if init is None else array('i', init)\
    \  # signed int\ndef u32a(init = None): return array('I') if init is None else\
    \ array('I', init)  # unsigned int\ndef i64a(init = None): return array('q') if\
    \ init is None else array('q', init)  # signed long long\n# def u64a(init = None):\
    \ return array('Q') if init is None else array('Q', init)  # unsigned long long\n\
    def f32a(init = None): return array('f') if init is None else array('f', init)\
    \  # float\ndef f64a(init = None): return array('d') if init is None else array('d',\
    \ init)  # double\n\ni8_max = (1 << 7)-1\nu8_max = (1 << 8)-1\ni16_max = (1 <<\
    \ 15)-1\nu16_max = (1 << 16)-1\ni32_max = (1 << 31)-1\nu32_max = (1 << 32)-1\n\
    i64_max = (1 << 63)-1\nu64_max = (1 << 64)-1\n\nclass PacketList(Sequence[tuple[int,int]]):\n\
    \    def __init__(lst, A: list[int], max1: int):\n        lst.A = A\n        lst.mask\
    \ = (1 << (shift := (max1).bit_length())) - 1\n        lst.shift = shift\n   \
    \ def __len__(lst): return lst.A.__len__()\n    def __contains__(lst, x: tuple[int,int]):\
    \ return lst.A.__contains__(x[0] << lst.shift | x[1])\n    def __getitem__(lst,\
    \ key) -> tuple[int,int]:\n        x = lst.A[key]\n        return x >> lst.shift,\
    \ x & lst.mask\n\nclass TreeBase(GraphBase):\n    @overload\n    def distance(T)\
    \ -> list[list[int]]: ...\n    @overload\n    def distance(T, s: int = 0) -> list[int]:\
    \ ...\n    @overload\n    def distance(T, s: int, g: int) -> int: ...\n    def\
    \ distance(T, s = None, g = None):\n        if s == None:\n            return\
    \ [T.dfs_distance(u) for u in range(T.N)]\n        else:\n            return T.dfs_distance(s,\
    \ g)\n\n    @overload\n    def diameter(T) -> int: ...\n    @overload\n    def\
    \ diameter(T, endpoints: Literal[True]) -> tuple[int,int,int]: ...\n    def diameter(T,\
    \ endpoints = False):\n        mask = (1 << (shift := T.N.bit_length())) - 1\n\
    \        s = max(d << shift | v for v,d in enumerate(T.distance(0))) & mask\n\
    \        dg = max(d << shift | v for v,d in enumerate(T.distance(s))) \n     \
    \   diam, g = dg >> shift, dg & mask\n        return (diam, s, g) if endpoints\
    \ else diam\n    \n    def dfs_distance(T, s: int, g: Union[int,None] = None):\n\
    \        st, Va = elist(N := T.N), T.Va\n        T.D, T.back = D, back = [inf]*N,\
    \ i32f(N, -1)\n        D[s] = 0\n        st.append(s)\n        while st:\n   \
    \         nd = D[u := st.pop()]+1\n            if u == g: return nd-1\n      \
    \      for i in T.range(u):\n                if nd < D[v := Va[i]]:\n        \
    \            D[v], back[v] = nd, i\n                    st.append(v)\n       \
    \ return D if g is None else inf\n\n    def rerooting_dp(T, e: _T, \n        \
    \             merge: Callable[[_T,_T],_T], \n                     edge_op: Callable[[_T,int,int,int],_T]\
    \ = lambda s,i,p,u:s,\n                     s: int = 0):\n        La, Ua, Va =\
    \ T.La, T.Ua, T.Va\n        order, dp, suf, I = T.dfs_topdown(s), [e]*T.N, [e]*len(Ua),\
    \ T.Ra[:]\n        # up\n        for i in order[::-1]:\n            u,v = Ua[i],\
    \ Va[i]\n            # subtree v finished up pass, store value to accumulate for\
    \ u\n            dp[v] = new = edge_op(dp[v], i, u, v)\n            dp[u] = merge(dp[u],\
    \ new)\n            # suffix accumulation\n            if (c:=I[u]-1) > La[u]:\
    \ suf[c-1] = merge(suf[c], new)\n            I[u] = c\n        # down\n      \
    \  dp[s] = e # at this point dp stores values to be merged in parent\n       \
    \ for i in order:\n            u,v = Ua[i], Va[i]\n            dp[u] = merge(pre\
    \ := dp[u], dp[v])\n            dp[v] = edge_op(merge(suf[I[u]], pre), i, v, u)\n\
    \            I[u] += 1\n        return dp\n    \n    def euler_tour(T, s = 0):\n\
    \        N, Va = len(T), T.Va\n        tin, tout, par, back = [-1]*N,[-1]*N,[-1]*N,[0]*N\n\
    \        order, delta = elist(2*N), elist(2*N)\n        \n        st = elist(N);\
    \ st.append(s)\n        while st:\n            p = par[u := st.pop()]\n      \
    \      if tin[u] == -1:\n                tin[u] = len(order)\n               \
    \ for i in T.range(u):\n                    if (v := Va[i]) != p:\n          \
    \              par[v], back[v] = u, i\n                        st.append(u); st.append(v)\n\
    \                delta.append(1)\n            else:\n                delta.append(-1)\n\
    \            \n            order.append(u)\n            tout[u] = len(order)\n\
    \        delta[0] = delta[-1] = 0\n        T.tin, T.tout, T.par, T.back = tin,\
    \ tout, par, back\n        T.order, T.delta = order, delta\n\n    def hld_precomp(T,\
    \ r = 0):\n        N, time, Va = T.N, 0, T.Va\n        tin, tout, size = [0]*N,\
    \ [0]*N, [1]*N+[0]\n        par, heavy, head = [-1]*N, [-1]*N, [r]*N\n       \
    \ depth, order, vis = [0]*N, [0]*N, [0]*N\n        st = elist(N)\n        st.append(r)\n\
    \        while st:\n            if (s := vis[v := st.pop()]) == 0: # dfs down\n\
    \                p, vis[v] = par[v], 1; st.append(v)\n                for i in\
    \ T.range(v):\n                    if (c := Va[i]) != p:\n                   \
    \     depth[c], par[c] = depth[v]+1, v; st.append(c)\n            elif s == 1:\
    \ # dfs up\n                p, l = par[v], -1\n                for i in T.range(v):\n\
    \                    if (c := Va[i]) != p:\n                        size[v] +=\
    \ size[c]\n                        if size[c] > size[l]:\n                   \
    \         l = c\n                heavy[v] = l\n                if p == -1:\n \
    \                   vis[v] = 2\n                    st.append(v)\n\n         \
    \   elif s == 2: # decompose down\n                p, h, l = par[v], head[v],\
    \ heavy[v]\n                tin[v], order[time], vis[v] = time, v, 3\n       \
    \         time += 1\n                st.append(v)\n                \n        \
    \        for i in T.range(v):\n                    if (c := Va[i]) != p and c\
    \ != l:\n                        head[c], vis[c] = c, 2\n                    \
    \    st.append(c)\n\n                if l != -1:\n                    head[l],\
    \ vis[l] = h, 2\n                    st.append(l)\n\n            elif s == 3:\
    \ # decompose up\n                tout[v] = time\n        T.size, T.depth = size,\
    \ depth\n        T.order, T.tin, T.tout = order, tin, tout\n        T.par, T.heavy,\
    \ T.head = par, heavy, head\n\n    @classmethod\n    def compile(cls, N: int,\
    \ shift: int = -1):\n        return GraphBase.compile.__func__(cls, N, N-1, shift)\n\
    \    \n\ndef sort2(a, b):\n    return (a,b) if a < b else (b,a)\n\nimport operator\n\
    from itertools import accumulate\n\ndef presum(iter: Iterable[_T], func: Callable[[_T,_T],_T]\
    \ = None, initial: _T = None, step = 1) -> list[_T]:\n    if step == 1:\n    \
    \    return list(accumulate(iter, func, initial=initial))\n    else:\n       \
    \ assert step >= 2\n        if func is None:\n            func = operator.add\n\
    \        A = list(iter)\n        if initial is not None:\n            A = [initial]\
    \ + A\n        for i in range(step,len(A)):\n            A[i] = func(A[i], A[i-step])\n\
    \        return A\nfrom itertools import pairwise\nfrom typing import Any, List\n\
    \nclass MinSparseTable:\n    def __init__(self, arr: List[Any]):\n        self.N\
    \ = N = len(arr)\n        self.log = N.bit_length()\n        \n        self.offsets\
    \ = offsets = [0]\n        for i in range(1, self.log):\n            offsets.append(offsets[-1]\
    \ + N - (1 << (i-1)) + 1)\n            \n        self.st = st = [0] * (offsets[-1]\
    \ + N - (1 << (self.log-1)) + 1)\n        st[:N] = arr \n        \n        for\
    \ i,ni in pairwise(range(self.log)):\n            start, nxt, d = offsets[i],\
    \ offsets[ni], 1 << i\n            for j in range(N - (1 << ni) + 1):\n      \
    \          st[nxt+j] = min(st[k := start+j], st[k + d])\n\n    def query(self,\
    \ l: int, r: int) -> Any:\n        k = (r-l).bit_length() - 1\n        start,\
    \ st = self.offsets[k], self.st\n        return min(st[start + l], st[start +\
    \ r - (1 << k)])\n    \n    def __repr__(self) -> str:\n        rows, offsets,\
    \ log, st = [], self.offsets, self.log, self.st\n        for i in range(log):\n\
    \            start = offsets[i]\n            end = offsets[i+1] if i+1 < log else\
    \ len(st)\n            rows.append(f\"{i:<2d} {st[start:end]}\")\n        return\
    \ '\\n'.join(rows)\n\nclass LCATable(MinSparseTable):\n    def __init__(lca, T,\
    \ root = 0):\n        N = len(T)\n        T.euler_tour(root)\n        lca.depth\
    \ = depth = presum(T.delta)\n        lca.tin, lca.tout = T.tin[:], T.tout[:]\n\
    \        lca.mask = (1 << (shift := N.bit_length()))-1\n        lca.shift = shift\n\
    \        order = T.order\n        M = len(order)\n        packets = [0]*M\n  \
    \      for i in range(M):\n            packets[i] = depth[i] << shift | order[i]\
    \ \n        super().__init__(packets)\n\n    def _query(lca, u, v):\n        tin\
    \ = lca.tin\n        l, r = sort2(tin[u], tin[v]); r += 1\n        da = super().query(l,\
    \ r)\n        return l, r, da & lca.mask, da >> lca.shift\n\n    def query(lca,\
    \ u, v) -> tuple[int,int]:\n        l, r, a, d = lca._query(u, v)\n        return\
    \ a, d\n    \n    def distance(lca, u, v) -> int:\n        l, r, a, d = lca._query(u,\
    \ v)\n        return lca.depth[l] + lca.depth[r-1] - 2*d\n    \n    def path(lca,\
    \ u, v):\n        path, par, lca, c = [], lca.T.par, lca.query(u, v)[0], u\n \
    \       while c != lca:\n            path.append(c)\n            c = par[c]\n\
    \        path.append(lca)\n        rev_path, c = [], v\n        while c != lca:\n\
    \            rev_path.append(c)\n            c = par[c]\n        path.extend(reversed(rev_path))\n\
    \        return path\n\n\ndef pack_sm(N: int):\n    s = N.bit_length()\n    return\
    \ s, (1<<s)-1\n\ndef pack_enc(a: int, b: int, s: int):\n    return a << s | b\n\
    \    \ndef pack_dec(ab: int, s: int, m: int):\n    return ab >> s, ab & m\n\n\
    def pack_indices(A, s):\n    return [a << s | i for i,a in enumerate(A)]\n\ndef\
    \ argsort(A: list[int], reverse=False):\n    s, m = pack_sm(len(A))\n    if reverse:\n\
    \        I = [a<<s|i^m for i,a in enumerate(A)]\n        I.sort(reverse=True)\n\
    \        for i,ai in enumerate(I): I[i] = (ai^m)&m\n    else:\n        I = [a<<s|i\
    \ for i,a in enumerate(A)]\n        I.sort()\n        for i,ai in enumerate(I):\
    \ I[i] = ai&m\n    return I\n\nclass AuxTreeBase(TreeBase):\n\n    def __init__(T,\
    \ lca: LCATable):\n        T.lca = lca\n\n    def add(T, u, v):\n        w = T.lca.distance(u,v)\n\
    \        i, j = T.Ra[u], T.Ra[v]\n        T.Ua[i], T.Va[i], T.Wa[i], T.Ua[j],\
    \ T.Va[j], T.Wa[j] = u, v, w, v, u, w\n        T.twin[i], T.twin[j] = j, i\n \
    \       T.Ra[u], T.Ra[v] = i+1, j+1\n        return j\n\n    def trees(T, C: list[int]):\n\
    \        lca, N = T.lca, T.N\n        T.Ra, cnt, order = T.La[:], [0]*N, argsort(T.tin)\n\
    \        for c in C: cnt[c] += 1\n        L = [0]*N\n        for i in range(N-1):\
    \ L[i+1] = L[i]+cnt[i]\n        R, G = L[:], [0]*N\n        \n        for i in\
    \ order: c = C[i]; G[R[c]] = i; R[c] += 1\n        st, V, post = elist(N), elist(N),\
    \ elist(N)\n        La, Ra, tin = T.La, T.Ra, T.tin\n\n        for c in range(N):\n\
    \            l, r = L[c], R[c]\n            if l == r: continue\n            st.append(G[l])\n\
    \            for j in range(l,r-1):\n                u, v = G[j], G[j+1]\n   \
    \             a, _ = lca.query(u, v)\n                if a != u:\n           \
    \         l = st.pop()\n                    while st and tin[t := st[-1]] > tin[a]:\n\
    \                        V.append(l); post.append(T.add(l, l := st.pop()))\n \
    \                   if not st or t != a: st.append(a)\n                    V.append(l);\
    \ post.append(T.add(l, a))\n                st.append(v)\n            l = st.pop()\n\
    \            while st: V.append(l); post.append(T.add(l, l := st.pop()))\n   \
    \         V.append(l)\n            yield c, V, post\n            while V:\n  \
    \              Ra[u] = La[u := V.pop()]\n                if T.vis: T.vis[u] =\
    \ 0\n            post.clear()\n\n    def rerooting_dp(T, C: list[int], e: _T,\
    \ \n                     merge: Callable[[_T,_T],_T], \n                     edge_op:\
    \ Callable[[_T,int,int,int,int],_T] = lambda s,i,p,u,c:s):\n        ans, dp, suf,\
    \ I = [e]*T.N, [e]*T.N, [e]*len(T.Ua), T.La[:]\n\n        for c, V, post in T.trees(C):\n\
    \            r = V[-1]\n            for v in V: I[v] = T.Ra[v]\n\n           \
    \ # up\n            for i in post:\n                u,v = T.Ua[i], T.Va[i]\n \
    \               # subtree v finished up pass, store value to accumulate for u\n\
    \                dp[v] = new = edge_op(dp[v], i, u, v, c)\n                dp[u]\
    \ = merge(dp[u], new)\n                # suffix accumulation\n               \
    \ if (j:=I[u]-1) > T.La[u]: suf[j-1] = merge(suf[j], new)\n                I[u]\
    \ = j\n            # down\n            dp[r] = e # at this point dp stores values\
    \ to be merged in parent\n            for i in reversed(post):\n             \
    \   u,v = T.Ua[i], T.Va[i]\n                dp[u] = merge(pre := dp[u], dp[v])\n\
    \                dp[v] = edge_op(merge(suf[I[u]], pre), i, v, u, c)\n        \
    \        I[u] += 1\n            \n            # store ans and reset\n        \
    \    for v in V:\n                if C[v] == c: ans[v] = dp[v]\n             \
    \   dp[v] = e\n            for i in post:\n                suf[i] = e\n      \
    \  return ans\n"
  code: "from cp_library.alg.tree.fast.tree_base_cls import TreeBase\nfrom cp_library.alg.tree.lca_table_iterative_cls\
    \ import LCATable\nfrom cp_library.ds.elist_fn import elist\nfrom cp_library.alg.iter.argsort_fn\
    \ import argsort\nfrom typing import Callable\nfrom cp_library.misc.typing import\
    \ _T\n\nclass AuxTreeBase(TreeBase):\n\n    def __init__(T, lca: LCATable):\n\
    \        T.lca = lca\n\n    def add(T, u, v):\n        w = T.lca.distance(u,v)\n\
    \        i, j = T.Ra[u], T.Ra[v]\n        T.Ua[i], T.Va[i], T.Wa[i], T.Ua[j],\
    \ T.Va[j], T.Wa[j] = u, v, w, v, u, w\n        T.twin[i], T.twin[j] = j, i\n \
    \       T.Ra[u], T.Ra[v] = i+1, j+1\n        return j\n\n    def trees(T, C: list[int]):\n\
    \        lca, N = T.lca, T.N\n        T.Ra, cnt, order = T.La[:], [0]*N, argsort(T.tin)\n\
    \        for c in C: cnt[c] += 1\n        L = [0]*N\n        for i in range(N-1):\
    \ L[i+1] = L[i]+cnt[i]\n        R, G = L[:], [0]*N\n        \n        for i in\
    \ order: c = C[i]; G[R[c]] = i; R[c] += 1\n        st, V, post = elist(N), elist(N),\
    \ elist(N)\n        La, Ra, tin = T.La, T.Ra, T.tin\n\n        for c in range(N):\n\
    \            l, r = L[c], R[c]\n            if l == r: continue\n            st.append(G[l])\n\
    \            for j in range(l,r-1):\n                u, v = G[j], G[j+1]\n   \
    \             a, _ = lca.query(u, v)\n                if a != u:\n           \
    \         l = st.pop()\n                    while st and tin[t := st[-1]] > tin[a]:\n\
    \                        V.append(l); post.append(T.add(l, l := st.pop()))\n \
    \                   if not st or t != a: st.append(a)\n                    V.append(l);\
    \ post.append(T.add(l, a))\n                st.append(v)\n            l = st.pop()\n\
    \            while st: V.append(l); post.append(T.add(l, l := st.pop()))\n   \
    \         V.append(l)\n            yield c, V, post\n            while V:\n  \
    \              Ra[u] = La[u := V.pop()]\n                if T.vis: T.vis[u] =\
    \ 0\n            post.clear()\n\n    def rerooting_dp(T, C: list[int], e: _T,\
    \ \n                     merge: Callable[[_T,_T],_T], \n                     edge_op:\
    \ Callable[[_T,int,int,int,int],_T] = lambda s,i,p,u,c:s):\n        ans, dp, suf,\
    \ I = [e]*T.N, [e]*T.N, [e]*len(T.Ua), T.La[:]\n\n        for c, V, post in T.trees(C):\n\
    \            r = V[-1]\n            for v in V: I[v] = T.Ra[v]\n\n           \
    \ # up\n            for i in post:\n                u,v = T.Ua[i], T.Va[i]\n \
    \               # subtree v finished up pass, store value to accumulate for u\n\
    \                dp[v] = new = edge_op(dp[v], i, u, v, c)\n                dp[u]\
    \ = merge(dp[u], new)\n                # suffix accumulation\n               \
    \ if (j:=I[u]-1) > T.La[u]: suf[j-1] = merge(suf[j], new)\n                I[u]\
    \ = j\n            # down\n            dp[r] = e # at this point dp stores values\
    \ to be merged in parent\n            for i in reversed(post):\n             \
    \   u,v = T.Ua[i], T.Va[i]\n                dp[u] = merge(pre := dp[u], dp[v])\n\
    \                dp[v] = edge_op(merge(suf[I[u]], pre), i, v, u, c)\n        \
    \        I[u] += 1\n            \n            # store ans and reset\n        \
    \    for v in V:\n                if C[v] == c: ans[v] = dp[v]\n             \
    \   dp[v] = e\n            for i in post:\n                suf[i] = e\n      \
    \  return ans\n"
  dependsOn:
  - cp_library/alg/tree/fast/tree_base_cls.py
  - cp_library/alg/tree/lca_table_iterative_cls.py
  - cp_library/ds/elist_fn.py
  - cp_library/alg/iter/argsort_fn.py
  - cp_library/alg/graph/fast/graph_base_cls.py
  - cp_library/ds/array_init_fn.py
  - cp_library/alg/dp/sort2_fn.py
  - cp_library/alg/iter/presum_fn.py
  - cp_library/ds/min_sparse_table_cls.py
  - cp_library/bit/pack_sm_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/alg/dp/chmin_fn.py
  - cp_library/alg/graph/dfs_options_cls.py
  - cp_library/ds/packet_list_cls.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: false
  path: cp_library/alg/tree/fast/aux_tree_base_cls.py
  requiredBy:
  - cp_library/alg/tree/fast/aux_tree_cls.py
  - cp_library/alg/tree/fast/aux_tree_weighted_cls.py
  timestamp: '2025-03-19 15:35:53+07:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/aoj/vol/0439_aux_dijkstra.test.py
  - test/aoj/vol/0439_aux_rerooting_dp.test.py
  - test/aoj/vol/0439_aux_weighted_rerooting_dp.test.py
documentation_of: cp_library/alg/tree/fast/aux_tree_base_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/tree/fast/aux_tree_base_cls.py
- /library/cp_library/alg/tree/fast/aux_tree_base_cls.py.html
title: cp_library/alg/tree/fast/aux_tree_base_cls.py
---
