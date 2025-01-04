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
    path: cp_library/alg/graph/fast/graph_cls.py
    title: cp_library/alg/graph/fast/graph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/fast/tree_base_cls.py
    title: cp_library/alg/tree/fast/tree_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/fast/tree_cls.py
    title: cp_library/alg/tree/fast/tree_cls.py
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
    PROBLEM: https://atcoder.jp/contests/abc202/tasks/abc202_e
    links:
    - https://atcoder.jp/contests/abc202/tasks/abc202_e
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc202/tasks/abc202_e\n\
    \n\nfrom bisect import bisect_left\n\ndef main():\n    N = read(int)\n    V =\
    \ read(list[-1])\n    U = list(range(1,N))\n    G = Tree(N, U, V)\n\n    depth\
    \ = [0]*N\n    cnt = [[] for _ in range(N)]\n\n    time = 0\n    tin = [0]*N\n\
    \    tout = [0]*N\n    \n    def down(p,u):\n        depth[u] = depth[p]+1\n\n\
    \    def enter(u):\n        nonlocal time\n        tin[u] = time\n        cnt[depth[u]].append(time)\n\
    \        time += 1\n\n    def leave(u):\n        nonlocal time\n        tout[u]\
    \ = time\n        time += 1\n\n    G.dfs(0, down_fn=down, enter_fn=enter, leave_fn=leave)\n\
    \n    Q = read(int)\n    for u,d in read(list[tuple[-1,int],Q]):\n        ans\
    \ = bisect_left(cnt[d], tout[u]) - bisect_left(cnt[d], tin[u])\n        write(ans)\n\
    \n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\
    \n             https://kobejean.github.io/cp-library               \n'''\n\nfrom\
    \ math import inf\nfrom itertools import islice\nfrom typing import Callable,\
    \ Sequence, Union, overload\nfrom collections import deque\n\nimport typing\n\
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
    \ Parser.compile_collection(type(spec), args)\n        elif isinstance(fn := spec,\
    \ Callable): \n            def parse(ts: TokenStream):\n                return\
    \ fn(next(ts))\n            return parse\n        else:\n            raise NotImplementedError()\n\
    \n    @staticmethod\n    def compile_line(cls: T, spec=int) -> ParseFn[T]:\n \
    \       if spec is int:\n            fn = Parser.compile(spec)\n            def\
    \ parse(ts: TokenStream):\n                return cls((int(token) for token in\
    \ ts.line()))\n            return parse\n        else:\n            fn = Parser.compile(spec)\n\
    \            def parse(ts: TokenStream):\n                return cls((fn(ts) for\
    \ _ in ts.wait()))\n            return parse\n\n    @staticmethod\n    def compile_repeat(cls:\
    \ T, spec, N) -> ParseFn[T]:\n        fn = Parser.compile(spec)\n        def parse(ts:\
    \ TokenStream):\n            return cls((fn(ts) for _ in range(N)))\n        return\
    \ parse\n\n    @staticmethod\n    def compile_children(cls: T, specs) -> ParseFn[T]:\n\
    \        fns = tuple((Parser.compile(spec) for spec in specs))\n        def parse(ts:\
    \ TokenStream):\n            return cls((fn(ts) for fn in fns))  \n        return\
    \ parse\n            \n    @staticmethod\n    def compile_tuple(cls: type[T],\
    \ specs) -> ParseFn[T]:\n        if isinstance(specs, (tuple,list)) and len(specs)\
    \ == 2 and specs[1] is ...:\n            return Parser.compile_line(cls, specs[0])\n\
    \        else:\n            return Parser.compile_children(cls, specs)\n\n   \
    \ @staticmethod\n    def compile_collection(cls, specs):\n        if not specs\
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
    \ Parsable):\n    def __init__(G, N: int, M: int, U: list[int], V: list[int],\
    \ \n                 deg: list[int], La: list[int], Ra: list[int],\n         \
    \        Ua: list[int], Va: list[int], Ea: list[int], self_loops = False):\n \
    \       G.N = N\n        \"\"\"The number of vertices.\"\"\"\n        G.M = M\n\
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
    \n        G.stack: list[int] = None\n        G.order: list[int] = None\n     \
    \   G.vis: list[int] = None\n\n    def __len__(G) -> int: return G.N\n    def\
    \ __getitem__(G, u): return islice(G.Va,G.La[u],G.Ra[u])\n    def range(G, u):\
    \ return range(G.La[u],G.Ra[u])\n    \n    @overload\n    def distance(G) -> list[list[int]]:\
    \ ...\n    @overload\n    def distance(G, s: int = 0) -> list[int]: ...\n    @overload\n\
    \    def distance(G, s: int, g: int) -> int: ...\n    def distance(G, s = None,\
    \ g = None):\n        if s == None: return G.floyd_warshall()\n        else: return\
    \ G.bfs(s, g)\n\n    def shortest_path(G, s: int, t: int):\n        if G.distance(s,\
    \ t) >= inf: return None\n        Ua, back, vertices = G.Ua, G.back, u32f(1, v\
    \ := t)\n        while v != s: vertices.append(v := Ua[back[v]])\n        return\
    \ vertices[::-1]\n    \n    def shortest_path_edge_ids(G, s: int, t: int):\n \
    \       if G.distance(s, t) >= inf: return None\n        Ea, Ua, back, edges,\
    \ v = G.Ea, G.Ua, G.back, u32f(0), t\n        while v != s: edges.append(Ea[i\
    \ := back[v]]), (v := Ua[i])\n        return edges[::-1]\n    \n    @overload\n\
    \    def bfs(G, s: Union[int,list] = 0) -> list[int]: ...\n    @overload\n   \
    \ def bfs(G, s: Union[int,list], g: int) -> int: ...\n    def bfs(G, s: int =\
    \ 0, g: int = None):\n        S, Va, back, D = G.starts(s), G.Va, i32f(N := G.N,\
    \ -1), [inf]*N\n        G.back, G.D = back, D\n        for u in S: D[u] = 0\n\
    \        que = deque(S)\n        while que:\n            nd = D[u := que.popleft()]+1\n\
    \            if u == g: return nd-1\n            for i in G.range(u):\n      \
    \          if nd < D[v := Va[i]]:\n                    D[v], back[v] = nd, i\n\
    \                    que.append(v)\n        return D if g is None else inf \n\n\
    \    def floyd_warshall(G) -> list[list[int]]:\n        M, Ua, Va, N = G.M, G.Ua,\
    \ G.Va, G.N\n        G.D = D = [[inf]*N for _ in range(N)]\n        for u in range(N):\
    \ D[u][u] = 0\n        for i in range(M): D[Ua[i]][Va[i]] = 1\n        for k,\
    \ Dk in enumerate(D):\n            for Di in D:\n                if Di[k] == inf:\
    \ continue\n                for j in range(N):\n                    Di[j] = min(Di[j],\
    \ Di[k]+Dk[j])\n        return D\n\n    def find_cycle_indices(G, s: Union[int,\
    \ None] = None):\n        M, Ea, Ua, Va, vis, back = G.M, G.Ea, G. Ua, G.Va, u8f(N\
    \ := G.N), u32f(N, i32_max)\n        G.vis, G.back, stack = vis, back, elist(N)\n\
    \        for s in G.starts(s):\n            if vis[s]: continue\n            stack.append(s)\n\
    \            while stack:\n                if vis[u := stack.pop()] == 0:\n  \
    \                  stack.append(u)\n                    vis[u], pe = 1, Ea[j]\
    \ if (j := back[u]) != i32_max else i32_max\n                    for i in G.range(u):\n\
    \                        if vis[v := Va[i]] == 0:\n                          \
    \  back[v] = i\n                            stack.append(v)\n                \
    \        elif vis[v] == 1 and pe != Ea[i]:\n                            I = u32f(1,i)\n\
    \                            while v != u: I.append(i := back[u]), (u := Ua[i])\n\
    \                            return I[::-1]\n                else:\n         \
    \           vis[u] = 2\n        # check for self loops\n        for i in range(len(Ua)):\n\
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
    \          D[v], par[v] = D[u]+1, u\n                que.append(v)\n\n    def\
    \ dfs_topdown(G, s: int) -> list[int]:\n        '''Returns lists of indices i\
    \ where Ua[i] -> Va[i] are edges in order of top down discovery'''\n        G.vis,\
    \ G.stack, G.order = vis, stack, order = u8f(N := G.N), G.stack or elist(N), G.order\
    \ or elist(N)\n        vis[s] = 1\n        stack.append(s)\n        while stack:\n\
    \            for i in G.range(stack.pop()):\n                if vis[v := G.Va[i]]:\
    \ continue\n                vis[v] = 1\n                order.append(i), stack.append(v)\n\
    \        return order\n\n    def dfs(G, s: Union[int,list] = None, /, connect_roots\
    \ = False, backtrack = False, max_depth = None, enter_fn: Callable[[int],None]\
    \ = None, leave_fn: Callable[[int],None] = None, max_depth_fn: Callable[[int],None]\
    \ = None, down_fn: Callable[[int,int],None] = None, back_fn: Callable[[int,int],None]\
    \ = None, cross_fn: Callable[[int,int],None] = None, up_fn: Callable[[int,int],None]\
    \ = None):\n        Va, La, Ra, I = G.Va, G.La, G.Ra, G.La[:]\n        G.state,\
    \ G.stack = state, stack = u8f(G.N), elist(G.N if max_depth is None else max_depth+1)\n\
    \        for s in G.starts(s):\n            if state[s]: continue\n          \
    \  stack.append(s)\n            if connect_roots and down_fn: down_fn(-1,s)\n\
    \            while stack:\n                if state[u := stack[-1]] == 0:\n  \
    \                  state[u] = 1\n                    if enter_fn: enter_fn(u)\n\
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
    \ = None) -> Sequence[tuple[DFSEvent,int]]:\n        N, Ra, Va, I = G.N, G.Ra,\
    \ G.Va, G.La[:]\n        stack, par, plist = elist(N), i32f(N,-1), PacketList(order\
    \ := elist(2*N), N-1)\n        G.par, ENTER, LEAVE = par, int(DFSEvent.ENTER)\
    \ << plist.shift, int(DFSEvent.LEAVE) << plist.shift\n        for s in G.starts(s):\n\
    \            if par[s] >= 0: continue\n            par[s] = s\n            order.append(ENTER\
    \ | s), stack.append(s)\n            while stack:\n                if (i := I[u\
    \ := stack[-1]]) < Ra[u]:\n                    I[u] += 1\n                   \
    \ if par[v := Va[i]] >= 0: continue\n                    par[v] = u\n        \
    \            order.append(ENTER | v), stack.append(v)\n                else:\n\
    \                    order.append(LEAVE | u), stack.pop()\n        return PacketList(order,\
    \ N-1)\n    \n    def is_bipartite(G):\n        Va, que, color = G.Va, deque(),\
    \ u8f(N := G.N)                \n        for s in range(N):\n            if color[s]:\
    \ continue\n            color[s] = 1\n            que.append(s)\n            while\
    \ que:\n                for i in G.range(u := que.popleft()):\n              \
    \      if color[v := Va[i]] == 0:\n                        color[v] = color[u]\
    \ ^ 2\n                        que.append(v)\n                    elif color[v]\
    \ == color[u]: return False\n        return True\n    \n    def starts(G, s: Union[int,list[int],None])\
    \ -> list[int]:\n        if isinstance(s, int): return [s]\n        elif s is\
    \ None: return range(G.N)\n        elif isinstance(s, list): return s\n      \
    \  else: return list(s)\n\n    @classmethod\n    def compile(cls, N: int, M: int,\
    \ shift: int = -1):\n        def parse(ts: TokenStream):\n            U, V = u32f(M),\
    \ u32f(M)\n            stream = ts.stream\n            for i in range(M):\n  \
    \              u, v = map(int, stream.readline().split())\n                U[i],\
    \ V[i] = u+shift, v+shift\n            return cls(N, U, V)\n        return parse\n\
    \    \n\n\ndef elist(est_len: int) -> list: ...\ntry:\n    from __pypy__ import\
    \ newlist_hint\nexcept:\n    def newlist_hint(hint):\n        return []\nelist\
    \ = newlist_hint\n    \nfrom typing import Iterable\nfrom array import array\n\
    \ndef i8f(N: int, elm: int = 0):      return array('b', (elm,))*N  # signed char\n\
    def u8f(N: int, elm: int = 0):      return array('B', (elm,))*N  # unsigned char\n\
    def i16f(N: int, elm: int = 0):     return array('h', (elm,))*N  # signed short\n\
    def u16f(N: int, elm: int = 0):     return array('H', (elm,))*N  # unsigned short\n\
    def i32f(N: int, elm: int = 0):     return array('i', (elm,))*N  # signed int\n\
    def u32f(N: int, elm: int = 0):     return array('I', (elm,))*N  # unsigned int\n\
    def i64f(N: int, elm: int = 0):     return array('q', (elm,))*N  # signed long\
    \ long\n# def u64f(N: int, elm: int = 0):     return array('Q', (elm,))*N  # unsigned\
    \ long long\ndef f32f(N: int, elm: float = 0.0): return array('f', (elm,))*N \
    \ # float\ndef f64f(N: int, elm: float = 0.0): return array('d', (elm,))*N  #\
    \ double\n\ndef i8a(init = None):  return array('b') if init is None else array('b',\
    \ init)  # signed char\ndef u8a(init = None):  return array('B') if init is None\
    \ else array('B', init)  # unsigned char\ndef i16a(init = None): return array('h')\
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
    \    def __init__(self, A: list[int], max0: int):\n        self.A = A\n      \
    \  self.mask = (1 << (shift := (max0).bit_length())) - 1\n        self.shift =\
    \ shift\n    def __len__(self): return self.A.__len__()\n    def __contains__(self,\
    \ x): return self.A.__contains__(x)\n    def __getitem__(self, key):\n       \
    \ x = self.A[key]\n        return x >> self.shift, x & self.mask\n\nclass Graph(GraphBase):\n\
    \    def __init__(G, N: int, U: list[int], V: list[int]):\n        deg, Ea, Ua,\
    \ Va, La, Ra, i = u32f(N), i32f(M2 := (M := len(U)) << 1), u32f(M2), u32f(M2),\
    \ u32f(N), u32f(N), 0\n        for u in U: deg[u] += 1\n        for v in V: deg[v]\
    \ += 1\n        for u in range(N): La[u], Ra[u], i = i, i, i+deg[u]\n        for\
    \ e in range(M):\n            Ra[u], Ra[v] = (i := Ra[u := U[e]])+1, (j := Ra[v\
    \ := V[e]])+1\n            Ua[i], Va[i], Ea[i], Ua[j], Va[j], Ea[j] = u, v, e,\
    \ v, u, e\n        super().__init__(N, M, U, V, deg, La, Ra, Ua, Va, Ea)\n\nfrom\
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
    \ Va = elist(N := T.N), T.Va\n        T.D, T.back = D, back = u32f(N, inf), i32f(N,\
    \ -1)\n        D[s] = 0\n        stack.append(s)\n        while stack:\n     \
    \       nd = D[u := stack.pop()]+1\n            if u == g: return nd-1\n     \
    \       for i in T.range(u):\n                if nd < D[v := Va[i]]:\n       \
    \             D[v], back[v] = nd, i\n                    stack.append(v)\n   \
    \     return D if g is None else inf\n\n    def rerooting_dp(T, e: _T, \n    \
    \                 merge: Callable[[_T,_T],_T], \n                     edge_op:\
    \ Callable[[int,int,int,_T],_T] = lambda p,c,i,s:s,\n                     s: int\
    \ = 0):\n        La, Ua, Va = T.La, T.Ua, T.Va\n        order, dp, suf, I = T.dfs_topdown(s),\
    \ [e]*T.N, [e]*len(Ua), T.Ra[:]\n        # up\n        for i in order[::-1]:\n\
    \            u,v = Ua[i], Va[i]\n            # subtree v finished up pass, store\
    \ value to accumulate for u\n            dp[v] = new = edge_op(u, v, i, dp[v])\n\
    \            dp[u] = merge(dp[u], new)\n            # suffix accumulation\n  \
    \          if (c:=I[u]-1) > La[u]: suf[c-1] = merge(suf[c], new)\n           \
    \ I[u] = c\n        # down\n        dp[s] = e # at this point dp stores values\
    \ to be merged in parent\n        for i in order:\n            u,v = Ua[i], Va[i]\n\
    \            dp[u] = merge(pre := dp[u], dp[v])\n            dp[v] = edge_op(v,\
    \ u, i, merge(suf[I[u]], pre))\n            I[u] += 1\n        return dp\n   \
    \ \n    def euler_tour(T, s = 0):\n        N, Va = len(T), T.Va\n        tin,\
    \ tout, par, back = [-1]*N,[-1]*N,[-1]*N,[0]*N\n        order, delta = elist(2*N),\
    \ elist(2*N)\n        \n        stack = elist(N)\n        stack.append(s)\n  \
    \      while stack:\n            p = par[u := stack.pop()]\n            if tin[u]\
    \ == -1:\n                tin[u] = len(order)\n                for i in T.range(u):\n\
    \                    if (v := Va[i]) != p:\n                        par[v], back[v]\
    \ = u, i\n                        stack.append(u)\n                        stack.append(v)\n\
    \                delta.append(1)\n            else:\n                delta.append(-1)\n\
    \            \n            order.append(u)\n            tout[u] = len(order)\n\
    \        delta[0] = delta[-1] = 0\n        T.tin, T.tout, T.par, T.back = tin,\
    \ tout, par, back\n        T.order, T.delta = order, delta\n\n    def hld_precomp(T,\
    \ r = 0):\n        N, time, Va = T.N, 0, T.Va\n        tin, tout, size = [0]*N,\
    \ [0]*N, [1]*N+[0]\n        par, heavy, head = [-1]*N, [-1]*N, [r]*N\n       \
    \ depth, order, state = [0]*N, [0]*N, [0]*N\n        stack = elist(N)\n      \
    \  stack.append(r)\n        while stack:\n            if (s := state[v := stack.pop()])\
    \ == 0: # dfs down\n                p, state[v] = par[v], 1\n                stack.append(v)\n\
    \                for i in T.range(v):\n                    if (c := Va[i]) !=\
    \ p:\n                        depth[c], par[c] = depth[v]+1, v\n             \
    \           stack.append(c)\n\n            elif s == 1: # dfs up\n           \
    \     p, l = par[v], -1\n                for i in T.range(v):\n              \
    \      if (c := Va[i]) != p:\n                        size[v] += size[c]\n   \
    \                     if size[c] > size[l]:\n                            l = c\n\
    \                heavy[v] = l\n                if p == -1:\n                 \
    \   state[v] = 2\n                    stack.append(v)\n\n            elif s ==\
    \ 2: # decompose down\n                p, h, l = par[v], head[v], heavy[v]\n \
    \               tin[v], order[time], state[v] = time, v, 3\n                time\
    \ += 1\n                stack.append(v)\n                \n                for\
    \ i in T.range(v):\n                    if (c := Va[i]) != p and c != l:\n   \
    \                     head[c], state[c] = c, 2\n                        stack.append(c)\n\
    \n                if l != -1:\n                    head[l], state[l] = h, 2\n\
    \                    stack.append(l)\n\n            elif s == 3: # decompose up\n\
    \                tout[v] = time\n        T.size, T.depth = size, depth\n     \
    \   T.order, T.tin, T.tout = order, tin, tout\n        T.par, T.heavy, T.head\
    \ = par, heavy, head\n\n    @classmethod\n    def compile(cls, N: int, shift:\
    \ int = -1):\n        return GraphBase.compile.__func__(cls, N, N-1, shift)\n\
    \    \n\nclass Tree(TreeBase, Graph):\n    pass\n\n\nfrom typing import Type,\
    \ TypeVar, Union, overload\n\nT = TypeVar('T')\n@overload\ndef read() -> list[int]:\
    \ ...\n@overload\ndef read(spec: int) -> list[int]: ...\n@overload\ndef read(spec:\
    \ Union[Type[T],T], char=False) -> T: ...\ndef read(spec: Union[Type[T],T] = None,\
    \ char=False):\n    if not char:\n        if spec is None:\n            return\
    \ map(int, TokenStream.stream.readline().split())\n        elif isinstance(offset\
    \ := spec, int):\n            return [int(s)+offset for s in TokenStream.stream.readline().split()]\n\
    \        elif spec is int:\n            return int(TokenStream.stream.readline())\n\
    \        else:\n            stream = TokenStream()\n    else:\n        stream\
    \ = CharStream()\n    parser: T = Parser.compile(spec)\n    return parser(stream)\n\
    \ndef write(*args, **kwargs):\n    \"\"\"Prints the values to a stream, or to\
    \ stdout_fast by default.\"\"\"\n    sep, file = kwargs.pop(\"sep\", \" \"), kwargs.pop(\"\
    file\", IOWrapper.stdout)\n    at_start = True\n    for x in args:\n        if\
    \ not at_start:\n            file.write(sep)\n        file.write(str(x))\n   \
    \     at_start = False\n    file.write(kwargs.pop(\"end\", \"\\n\"))\n    if kwargs.pop(\"\
    flush\", False):\n        file.flush()\n\nif __name__ == \"__main__\":\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc202/tasks/abc202_e\n\
    \n\nfrom bisect import bisect_left\n\ndef main():\n    N = read(int)\n    V =\
    \ read(list[-1])\n    U = list(range(1,N))\n    G = Tree(N, U, V)\n\n    depth\
    \ = [0]*N\n    cnt = [[] for _ in range(N)]\n\n    time = 0\n    tin = [0]*N\n\
    \    tout = [0]*N\n    \n    def down(p,u):\n        depth[u] = depth[p]+1\n\n\
    \    def enter(u):\n        nonlocal time\n        tin[u] = time\n        cnt[depth[u]].append(time)\n\
    \        time += 1\n\n    def leave(u):\n        nonlocal time\n        tout[u]\
    \ = time\n        time += 1\n\n    G.dfs(0, down_fn=down, enter_fn=enter, leave_fn=leave)\n\
    \n    Q = read(int)\n    for u,d in read(list[tuple[-1,int],Q]):\n        ans\
    \ = bisect_left(cnt[d], tout[u]) - bisect_left(cnt[d], tin[u])\n        write(ans)\n\
    \nfrom cp_library.alg.tree.fast.tree_cls import Tree\nfrom cp_library.io.read_fn\
    \ import read\nfrom cp_library.io.write_fn import write\n\nif __name__ == \"__main__\"\
    :\n    main()"
  dependsOn:
  - cp_library/alg/tree/fast/tree_cls.py
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/alg/graph/fast/graph_cls.py
  - cp_library/alg/tree/fast/tree_base_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  - cp_library/alg/graph/fast/graph_base_cls.py
  - cp_library/ds/array_init_fn.py
  - cp_library/ds/elist_fn.py
  - cp_library/alg/graph/dfs_options_cls.py
  - cp_library/ds/packet_list_cls.py
  isVerificationFile: true
  path: test/atcoder/abc/abc202_e_fast_dfs.test.py
  requiredBy: []
  timestamp: '2025-01-04 20:48:52+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/atcoder/abc/abc202_e_fast_dfs.test.py
layout: document
redirect_from:
- /verify/test/atcoder/abc/abc202_e_fast_dfs.test.py
- /verify/test/atcoder/abc/abc202_e_fast_dfs.test.py.html
title: test/atcoder/abc/abc202_e_fast_dfs.test.py
---
