---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/chmin_fn.py
    title: cp_library/alg/dp/chmin_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/dfs_options_cls.py
    title: cp_library/alg/graph/dfs_options_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/fast/graph_base_cls.py
    title: cp_library/alg/graph/fast/graph_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/fast/grid_graph_base_cls.py
    title: cp_library/alg/graph/fast/grid_graph_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/fast/grid_graph_walled_base_cls.py
    title: cp_library/alg/graph/fast/grid_graph_walled_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/array_init_fn.py
    title: cp_library/ds/array_init_fn.py
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
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc301_e_fast_grid_graph.test.py
    title: test/atcoder/abc/abc301_e_fast_grid_graph.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2578\n             https://kobejean.github.io/cp-library             \
    \  \n'''\nimport sys\n\n\ndef elist(est_len: int) -> list: ...\ntry:\n    from\
    \ __pypy__ import newlist_hint\nexcept:\n    def newlist_hint(hint):\n       \
    \ return []\nelist = newlist_hint\n    \n\n\nimport typing\nfrom collections import\
    \ deque\nfrom numbers import Number\nfrom types import GenericAlias \nfrom typing\
    \ import Callable, Collection, Iterator, Union\nimport os\nfrom io import BytesIO,\
    \ IOBase\n\n\nclass FastIO(IOBase):\n    BUFSIZE = 8192\n    newlines = 0\n\n\
    \    def __init__(self, file):\n        self._fd = file.fileno()\n        self.buffer\
    \ = BytesIO()\n        self.writable = \"x\" in file.mode or \"r\" not in file.mode\n\
    \        self.write = self.buffer.write if self.writable else None\n\n    def\
    \ read(self):\n        BUFSIZE = self.BUFSIZE\n        while True:\n         \
    \   b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))\n        \
    \    if not b:\n                break\n            ptr = self.buffer.tell()\n\
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
    \ = IOWrapper(sys.stdout)\nfrom typing import TypeVar\n_T = TypeVar('T')\n\nclass\
    \ TokenStream(Iterator):\n    stream = IOWrapper.stdin\n\n    def __init__(self):\n\
    \        self.queue = deque()\n\n    def __next__(self):\n        if not self.queue:\
    \ self.queue.extend(self._line())\n        return self.queue.popleft()\n    \n\
    \    def wait(self):\n        if not self.queue: self.queue.extend(self._line())\n\
    \        while self.queue: yield\n \n    def _line(self):\n        return TokenStream.stream.readline().split()\n\
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
    \  if ch:=dp[i]>v:dp[i]=v\n    return ch\nfrom math import inf\nfrom itertools\
    \ import islice\nfrom typing import Callable, Sequence, Union, overload\n\nfrom\
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
    \ Parsable):\n    def __init__(G, N: int, M: int, U: list[int], V: list[int],\
    \ \n                 deg: list[int], La: list[int], Ra: list[int],\n         \
    \        Ua: list[int], Va: list[int], Ea: list[int], twin: list[int] = None):\n\
    \        G.N = N\n        \"\"\"The number of vertices.\"\"\"\n        G.M = M\n\
    \        \"\"\"The number of edges.\"\"\"\n        G.U = U\n        \"\"\"A list\
    \ of source vertices in the original edge list.\"\"\"\n        G.V = V\n     \
    \   \"\"\"A list of destination vertices in the original edge list.\"\"\"\n  \
    \      G.deg = deg\n        \"\"\"deg[u] is the out degree of vertex u.\"\"\"\n\
    \        G.La = La\n        \"\"\"La[u] stores the start index of the list of\
    \ adjacent vertices from u.\"\"\"\n        G.Ra = Ra\n        \"\"\"Ra[u] stores\
    \ the stop index of the list of adjacent vertices from u.\"\"\"\n        G.Ua\
    \ = Ua\n        \"\"\"Ua[i] = u for La[u] <= i < Ra[u], useful for backtracking.\"\
    \"\"\n        G.Va = Va\n        \"\"\"Va[i] lists adjacent vertices to u for\
    \ La[u] <= i < Ra[u].\"\"\"\n        G.Ea = Ea\n        \"\"\"Ea[i] lists the\
    \ edge ids that start from u for La[u] <= i < Ra[u].\n        For undirected graphs,\
    \ edge ids in range M<= e <2*M are edges from V[e-M] -> U[e-M].\n        \"\"\"\
    \n        G.twin = twin if twin is not None else range(len(Ua))\n        \"\"\"\
    twin[i] in undirected graphs stores index j of the same edge but with u and v\
    \ swapped.\"\"\"\n        G.stack: list[int] = None\n        G.order: list[int]\
    \ = None\n        G.vis: list[int] = None\n\n    def __len__(G) -> int: return\
    \ G.N\n    def __getitem__(G, u): return islice(G.Va,G.La[u],G.Ra[u])\n    def\
    \ range(G, u): return range(G.La[u],G.Ra[u])\n    \n    @overload\n    def distance(G)\
    \ -> list[list[int]]: ...\n    @overload\n    def distance(G, s: int = 0) -> list[int]:\
    \ ...\n    @overload\n    def distance(G, s: int, g: int) -> int: ...\n    def\
    \ distance(G, s = None, g = None):\n        if s == None: return G.floyd_warshall()\n\
    \        else: return G.bfs(s, g)\n\n    def shortest_path(G, s: int, t: int):\n\
    \        if G.distance(s, t) >= inf: return None\n        Ua, back, vertices =\
    \ G.Ua, G.back, u32f(1, v := t)\n        while v != s: vertices.append(v := Ua[back[v]])\n\
    \        return vertices[::-1]\n    \n    def shortest_path_edge_ids(G, s: int,\
    \ t: int):\n        if G.distance(s, t) >= inf: return None\n        Ea, Ua, back,\
    \ edges, v = G.Ea, G.Ua, G.back, u32f(0), t\n        while v != s: edges.append(Ea[i\
    \ := back[v]]), (v := Ua[i])\n        return edges[::-1]\n    \n    @overload\n\
    \    def bfs(G, s: Union[int,list] = 0) -> list[int]: ...\n    @overload\n   \
    \ def bfs(G, s: Union[int,list], g: int) -> int: ...\n    def bfs(G, s: int =\
    \ 0, g: int = None):\n        S, Va, back, D = G.starts(s), G.Va, i32f(N := G.N,\
    \ -1), [inf]*N\n        G.back, G.D = back, D\n        for u in S: D[u] = 0\n\
    \        que = deque(S)\n        while que:\n            nd = D[u := que.popleft()]+1\n\
    \            if u == g: return nd-1\n            for i in G.range(u):\n      \
    \          if nd < D[v := Va[i]]:\n                    D[v], back[v] = nd, i\n\
    \                    que.append(v)\n        return D if g is None else inf \n\n\
    \    def floyd_warshall(G) -> list[list[int]]:\n        Ua, Va, N = G.Ua, G.Va,\
    \ G.N\n        G.D = D = [[inf]*N for _ in range(N)]\n        for u in range(N):\
    \ D[u][u] = 0\n        for i in range(len(Ua)): D[Ua[i]][Va[i]] = 1\n        for\
    \ k, Dk in enumerate(D):\n            for Di in D:\n                if (Dik :=\
    \ Di[k]) == inf: continue\n                for j in range(N):\n              \
    \      chmin(Di, j, Dik+Dk[j])\n        return D\n\n    def find_cycle_indices(G,\
    \ s: Union[int, None] = None):\n        Ea, Ua, Va, vis, back = G.Ea, G. Ua, G.Va,\
    \ u8f(N := G.N), u32f(N, i32_max)\n        G.vis, G.back, stack = vis, back, elist(N)\n\
    \        for s in G.starts(s):\n            if vis[s]: continue\n            stack.append(s)\n\
    \            while stack:\n                if not vis[u := stack.pop()]:\n   \
    \                 stack.append(u)\n                    vis[u], pe = 1, Ea[j] if\
    \ (j := back[u]) != i32_max else i32_max\n                    for i in G.range(u):\n\
    \                        if not vis[v := Va[i]]:\n                           \
    \ back[v] = i\n                            stack.append(v)\n                 \
    \       elif vis[v] == 1 and pe != Ea[i]:\n                            I = u32f(1,i)\n\
    \                            while v != u: I.append(i := back[u]), (u := Ua[i])\n\
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
    \        N = G.N\n        G.vis, G.stack, G.order = vis, stack, order = u8f(N),\
    \ G.stack or elist(N), G.order or elist(N)\n        for s in G.starts(s):\n  \
    \          if vis[s]: continue\n            vis[s] = 1; stack.append(s) \n   \
    \         while stack:\n                for i in G.range(stack.pop()):\n     \
    \               if vis[v := G.Va[i]]: continue\n                    vis[v] = 1;\
    \ order.append(i); stack.append(v)\n        return order\n\n    def dfs(G, s:\
    \ Union[int,list] = None, /, \n            backtrack = False,\n            max_depth\
    \ = None,\n            enter_fn: Callable[[int],None] = None,\n            leave_fn:\
    \ Callable[[int],None] = None,\n            max_depth_fn: Callable[[int],None]\
    \ = None,\n            down_fn: Callable[[int,int,int],None] = None,\n       \
    \     back_fn: Callable[[int,int,int],None] = None,\n            forward_fn: Callable[[int,int,int],None]\
    \ = None,\n            cross_fn: Callable[[int,int,int],None] = None,\n      \
    \      up_fn: Callable[[int,int,int],None] = None):\n        Va, La, Ra, I, twin,\
    \ tin, time = G.Va, G.La, G.Ra, G.La[:], G.twin, i32f(G.N, -1), -1\n        G.state,\
    \ G.stack = state, stack = u8f(G.N), elist(G.N if max_depth is None else max_depth+1)\n\
    \        G.back = back = i32f(G.N, -2)\n        G.tin = tin\n        for s in\
    \ G.starts(s):\n            if state[s]: continue\n            back[s], tin[s]\
    \ = -1, (time := time+1); stack.append(s)\n            while stack:\n        \
    \        if state[u := stack[-1]] == 0:\n                    state[u] = 1\n  \
    \                  if enter_fn: enter_fn(u)\n                    if max_depth\
    \ is not None and len(stack) > max_depth:\n                        I[u] = Ra[u]\n\
    \                        if max_depth_fn: max_depth_fn(u)\n                if\
    \ (i := I[u]) < Ra[u]:\n                    I[u] += 1\n                    if\
    \ (s := state[v := Va[i]]) == 0:\n                        back[v], tin[v] = i,\
    \ (time := time+1); stack.append(v)\n                        if down_fn: down_fn(u,v,i)\n\
    \                    elif back_fn and s == 1 and back[u] != twin[i]: back_fn(u,v,i)\n\
    \                    elif (cross_fn or forward_fn) and s == 2:\n             \
    \           if forward_fn and tin[u] < tin[v]: forward_fn(u,v,i)\n           \
    \             elif cross_fn: cross_fn(u,v,i)\n                else:\n        \
    \            stack.pop()\n                    state[u] = 2\n                 \
    \   if backtrack: state[u], I[u] = 0, La[u]\n                    if leave_fn:\
    \ leave_fn(u)\n                    if up_fn and stack: up_fn(u, stack[-1], back[u])\n\
    \    \n    def dfs_enter_leave(G, s: Union[int,list[int],None] = None) -> Sequence[tuple[DFSEvent,int]]:\n\
    \        N, Ra, Va, I = G.N, G.Ra, G.Va, G.La[:]\n        stack, back, plst =\
    \ elist(N), i32f(N,-2), PacketList(order := elist(2*N), N-1)\n        G.back,\
    \ ENTER, LEAVE = back, int(DFSEvent.ENTER) << plst.shift, int(DFSEvent.LEAVE)\
    \ << plst.shift\n        for s in G.starts(s):\n            if back[s] >= -1:\
    \ continue\n            back[s] = -1\n            order.append(ENTER | s), stack.append(s)\n\
    \            while stack:\n                if (i := I[u := stack[-1]]) < Ra[u]:\n\
    \                    I[u] += 1\n                    if back[v := Va[i]] >= -1:\
    \ continue\n                    back[v] = i; order.append(ENTER | v); stack.append(v)\n\
    \                else:\n                    order.append(LEAVE | u); stack.pop()\n\
    \        return plst\n    \n    def is_bipartite(G):\n        Va, que, color =\
    \ G.Va, deque(), u8f(N := G.N)                \n        for s in range(N):\n \
    \           if color[s]: continue\n            color[s] = 1\n            que.append(s)\n\
    \            while que:\n                for i in G.range(u := que.popleft()):\n\
    \                    if color[v := Va[i]] == 0:\n                        color[v]\
    \ = color[u] ^ 2\n                        que.append(v)\n                    elif\
    \ color[v] == color[u]: return False\n        return True\n    \n    def starts(G,\
    \ s: Union[int,list[int],None]) -> list[int]:\n        if isinstance(s, int):\
    \ return [s]\n        elif s is None: return range(G.N)\n        elif isinstance(s,\
    \ list): return s\n        else: return list(s)\n\n    @classmethod\n    def compile(cls,\
    \ N: int, M: int, shift: int = -1):\n        def parse(ts: TokenStream):\n   \
    \         U, V = u32f(M), u32f(M)\n            for i in range(M):\n          \
    \      u, v = ts._line()\n                U[i], V[i] = int(u)+shift, int(v)+shift\n\
    \            return cls(N, U, V)\n        return parse\n    \nfrom typing import\
    \ Iterable\nfrom array import array\n\ndef i8f(N: int, elm: int = 0):      return\
    \ array('b', (elm,))*N  # signed char\ndef u8f(N: int, elm: int = 0):      return\
    \ array('B', (elm,))*N  # unsigned char\ndef i16f(N: int, elm: int = 0):     return\
    \ array('h', (elm,))*N  # signed short\ndef u16f(N: int, elm: int = 0):     return\
    \ array('H', (elm,))*N  # unsigned short\ndef i32f(N: int, elm: int = 0):    \
    \ return array('i', (elm,))*N  # signed int\ndef u32f(N: int, elm: int = 0): \
    \    return array('I', (elm,))*N  # unsigned int\ndef i64f(N: int, elm: int =\
    \ 0):     return array('q', (elm,))*N  # signed long long\n# def u64f(N: int,\
    \ elm: int = 0):     return array('Q', (elm,))*N  # unsigned long long\ndef f32f(N:\
    \ int, elm: float = 0.0): return array('f', (elm,))*N  # float\ndef f64f(N: int,\
    \ elm: float = 0.0): return array('d', (elm,))*N  # double\n\ndef i8a(init = None):\
    \  return array('b') if init is None else array('b', init)  # signed char\ndef\
    \ u8a(init = None):  return array('B') if init is None else array('B', init) \
    \ # unsigned char\ndef i16a(init = None): return array('h') if init is None else\
    \ array('h', init)  # signed short\ndef u16a(init = None): return array('H') if\
    \ init is None else array('H', init)  # unsigned short\ndef i32a(init = None):\
    \ return array('i') if init is None else array('i', init)  # signed int\ndef u32a(init\
    \ = None): return array('I') if init is None else array('I', init)  # unsigned\
    \ int\ndef i64a(init = None): return array('q') if init is None else array('q',\
    \ init)  # signed long long\n# def u64a(init = None): return array('Q') if init\
    \ is None else array('Q', init)  # unsigned long long\ndef f32a(init = None):\
    \ return array('f') if init is None else array('f', init)  # float\ndef f64a(init\
    \ = None): return array('d') if init is None else array('d', init)  # double\n\
    \ni8_max = (1 << 7)-1\nu8_max = (1 << 8)-1\ni16_max = (1 << 15)-1\nu16_max = (1\
    \ << 16)-1\ni32_max = (1 << 31)-1\nu32_max = (1 << 32)-1\ni64_max = (1 << 63)-1\n\
    u64_max = (1 << 64)-1\n\nclass PacketList(Sequence[tuple[int,int]]):\n    def\
    \ __init__(lst, A: list[int], max1: int):\n        lst.A = A\n        lst.mask\
    \ = (1 << (shift := (max1).bit_length())) - 1\n        lst.shift = shift\n   \
    \ def __len__(lst): return lst.A.__len__()\n    def __contains__(lst, x: tuple[int,int]):\
    \ return lst.A.__contains__(x[0] << lst.shift | x[1])\n    def __getitem__(lst,\
    \ key) -> tuple[int,int]:\n        x = lst.A[key]\n        return x >> lst.shift,\
    \ x & lst.mask\n\nclass GridGraphBase(GraphBase):\n\n    def __init__(G, H, W,\
    \ M, S, U, V, deg, La, Ra, Ua, Va, Ea,\n            dirs: list = [(-1,0),(0,1),(1,0),(0,-1)]):\n\
    \        super().__init__(H*W, M, U, V, deg, La, Ra, Ua, Va, Ea)\n        G.W\
    \ = W\n        G.H = H\n        G.S = S\n        G.dirs = dirs\n\n    def vertex(G,\
    \ key: tuple[int,int] | int):\n        if isinstance(key, tuple):\n          \
    \  i,j = key\n            return i*G.W+j\n        else:\n            return key\n\
    \n    def is_valid(G, i, j, v):\n        return 0 <= i < G.H and 0 <= j < G.W\n\
    \    \n    @classmethod\n    def compile(cls, H: int, W: int, *args):\n      \
    \  def parse(ts: TokenStream):\n            S = ''.join(ts.stream.readline().rstrip()\
    \ for _ in range(H))\n            return cls(H, W, S, *args)\n        return parse\n\
    \nclass GridGraphWalledBase(GridGraphBase):\n\n    def __init__(G, H, W, M, S,\
    \ U, V, deg, La, Ra, Ua, Va, Ea,\n            dirs: list = [(-1,0),(0,1),(1,0),(0,-1)],\
    \ wall = '#'):\n        super().__init__(H, W, M, S, U, V, deg, La, Ra, Ua, Va,\
    \ Ea, dirs)\n        G.wall = wall\n\n    def is_valid(G, i, j, v):\n        return\
    \ super().is_valid(i, j, v) and G.S[v] != G.wall\n    \n    @classmethod\n   \
    \ def compile(cls, H: int, W: int, *args):\n        def parse(ts: TokenStream):\n\
    \            S = ''.join(ts.stream.readline().rstrip() for _ in range(H))\n  \
    \          return cls(H, W, S, *args)\n        return parse\n\nclass GridGraph(GridGraphWalledBase):\n\
    \n    def __init__(G, H, W, S=[], dirs = [(-1,0),(0,1),(1,0),(0,-1)], wall = '#'):\n\
    \        N = H*W\n        Mest = N*len(dirs)\n        deg, La, Ra, Ua, Va = u32f(N),\
    \ u32f(N), u32f(N), elist(Mest), elist(Mest)\n        super().__init__(\n    \
    \        H, W, 0, S, Ua, Va, deg, La, Ra, Ua, Va, None, dirs, wall\n        )\n\
    \n        for i in range(H):\n            for j in range(W):\n               \
    \ La[u := i*W+j] = len(Ua)\n                if G.is_valid(i, j, u):\n        \
    \            for di,dj in dirs:\n                        if G.is_valid(ni:=i+di,\
    \ nj:=j+dj, v:=ni*W+nj):\n                            deg[u] += 1\n          \
    \                  Ua.append(u)\n                            Va.append(v)\n  \
    \              Ra[u] = len(Ua)\n\n        G.M = len(Ua)\n        G.Ea = u32a(range(G.M))\n\
    \n"
  code: "\nimport cp_library.alg.graph.__header__\nimport sys\nfrom cp_library.ds.elist_fn\
    \ import elist\nfrom cp_library.alg.graph.fast.grid_graph_walled_base_cls import\
    \ GridGraphWalledBase\n\nclass GridGraph(GridGraphWalledBase):\n\n    def __init__(G,\
    \ H, W, S=[], dirs = [(-1,0),(0,1),(1,0),(0,-1)], wall = '#'):\n        N = H*W\n\
    \        Mest = N*len(dirs)\n        deg, La, Ra, Ua, Va = u32f(N), u32f(N), u32f(N),\
    \ elist(Mest), elist(Mest)\n        super().__init__(\n            H, W, 0, S,\
    \ Ua, Va, deg, La, Ra, Ua, Va, None, dirs, wall\n        )\n\n        for i in\
    \ range(H):\n            for j in range(W):\n                La[u := i*W+j] =\
    \ len(Ua)\n                if G.is_valid(i, j, u):\n                    for di,dj\
    \ in dirs:\n                        if G.is_valid(ni:=i+di, nj:=j+dj, v:=ni*W+nj):\n\
    \                            deg[u] += 1\n                            Ua.append(u)\n\
    \                            Va.append(v)\n                Ra[u] = len(Ua)\n\n\
    \        G.M = len(Ua)\n        G.Ea = u32a(range(G.M))\n\nfrom cp_library.ds.array_init_fn\
    \ import u32f, u32a"
  dependsOn:
  - cp_library/ds/elist_fn.py
  - cp_library/alg/graph/fast/grid_graph_walled_base_cls.py
  - cp_library/ds/array_init_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/alg/graph/fast/grid_graph_base_cls.py
  - cp_library/alg/graph/fast/graph_base_cls.py
  - cp_library/alg/dp/chmin_fn.py
  - cp_library/alg/graph/dfs_options_cls.py
  - cp_library/ds/packet_list_cls.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: false
  path: cp_library/alg/graph/fast/grid_graph_cls.py
  requiredBy: []
  timestamp: '2025-03-12 22:12:43+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/abc/abc301_e_fast_grid_graph.test.py
documentation_of: cp_library/alg/graph/fast/grid_graph_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/fast/grid_graph_cls.py
- /library/cp_library/alg/graph/fast/grid_graph_cls.py.html
title: cp_library/alg/graph/fast/grid_graph_cls.py
---
