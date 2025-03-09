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
    path: cp_library/alg/tree/heavy_light_decomposition_cls.py
    title: cp_library/alg/tree/heavy_light_decomposition_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/heavy_light_decomposition_weighted_cls.py
    title: cp_library/alg/tree/heavy_light_decomposition_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack_sm_fn.py
    title: cp_library/bit/pack_sm_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/array_init_fn.py
    title: cp_library/ds/array_init_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/dsu_cls.py
    title: cp_library/ds/dsu_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
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
    path: cp_library/ds/packet_list_cls.py
    title: cp_library/ds/packet_list_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bit_cls.py
    title: cp_library/ds/tree/bit_cls.py
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
    PROBLEM: https://atcoder.jp/contests/abc294/tasks/abc294_g
    links:
    - https://atcoder.jp/contests/abc294/tasks/abc294_g
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc294/tasks/abc294_g\n\
    \ndef main():\n    N = read(int)\n    T = read(TreeWeighted[N])\n\n    hld = HLDWeighted(T)\n\
    \    W = [hld.weights[i] for i in hld.order]\n    bit = BIT(W)\n    ans = 0\n\n\
    \    def query(l, r):\n        nonlocal ans\n        ans += bit.range_sum(l,r)\
    \ \n\n    Q = read(int)\n    for q in read(list[tuple[int, int, int], Q]):\n \
    \       match q:\n            case 1, i, w:\n                i -= 1  # Convert\
    \ to 0-based index\n                u, v = T.U[i], T.V[i]\n                idx\
    \ = hld[u if hld.par[u] == v else v]\n                bit.set(idx, w)\n      \
    \      case 2, u, v:\n                u, v = u - 1, v - 1\n                ans\
    \ = 0\n                hld.path(u,v, query, True)\n                write(ans)\n\
    \n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\
    \n             https://kobejean.github.io/cp-library               \n'''\nfrom\
    \ typing import Sequence\n\nclass BIT(Sequence[int]):\n    def __init__(bit, v):\n\
    \        if isinstance(v, int): bit.d, bit.n = [0]*v, v\n        else: bit.build(v)\n\
    \        bit.lb = 1<<(bit.n.bit_length()-1)\n\n    def build(bit, data):\n   \
    \     bit.d, bit.n = data, len(data)\n        for i in range(bit.n):\n       \
    \     if (r := i|i+1) < bit.n: bit.d[r] += bit.d[i]\n\n    def add(bit, i, x):\n\
    \        assert 0 <= i <= bit.n\n        while i < bit.n:\n            bit.d[i]\
    \ += x\n            i |= i+1\n\n    def sum(bit, r: int) -> int:\n        assert\
    \ 0 <= r <= bit.n\n        s = 0\n        while r: s, r = s+bit.d[r-1], r&r-1\n\
    \        return s\n\n    def range_sum(bit, l, r):\n        assert 0 <= l <= r\
    \ <= bit.n\n        s = 0\n        while r: s, r = s+bit.d[r-1], r&r-1\n     \
    \   while l: s, l = s-bit.d[l-1], l&l-1\n        return s\n\n    def __len__(bit)\
    \ -> int:\n        return bit.n\n    \n    def __getitem__(bit, i: int) -> int:\n\
    \        s, l = bit.d[i], i&(i+1)\n        while l != i: s, i = s-bit.d[i-1],\
    \ i-(i&-i)\n        return s\n    get = __getitem__\n    \n    def __setitem__(bit,\
    \ i: int, x: int) -> None:\n        bit.add(i, x-bit[i])\n    set = __setitem__\n\
    \n    def prelist(bit) -> list[int]:\n        pre = [0]+bit.d\n        for i in\
    \ range(bit.n+1): pre[i] += pre[i&i-1]\n        return pre\n\n    def bisect_left(bit,\
    \ v) -> int:\n        return bit.bisect_right(v-1) if v>0 else 0\n    \n    def\
    \ bisect_right(bit, v) -> int:\n        i, ni = s, m = 0, bit.lb\n        while\
    \ m:\n            if ni <= bit.n and (ns:=s+bit.d[ni-1]) <= v: s, i = ns, ni\n\
    \            ni = (m:=m>>1)|i\n        return i\n\n\n\n\ndef chmin(dp, i, v):\n\
    \    if ch:=dp[i]>v:dp[i]=v\n    return ch\nfrom typing import overload\n\nimport\
    \ typing\nfrom collections import deque\nfrom numbers import Number\nfrom types\
    \ import GenericAlias \nfrom typing import Callable, Collection, Iterator, Union\n\
    import os\nimport sys\nfrom io import BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n\
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
    \ return cls(next(ts))\n        return parser\n\n\n\ndef pack_sm(N: int):\n  \
    \  s = N.bit_length()\n    return s, (1<<s)-1\n\ndef pack_enc(a: int, b: int,\
    \ s: int):\n    return a << s | b\n    \ndef pack_dec(ab: int, s: int, m: int):\n\
    \    return ab >> s, ab & m\n\ndef argsort(A: list[int], reverse=False):\n   \
    \ s, m = pack_sm(len(A))\n    if reverse:\n        I = [a<<s|i^m for i,a in enumerate(A)]\n\
    \        I.sort(reverse=True)\n        for i,ai in enumerate(I): I[i] = (ai^m)&m\n\
    \    else:\n        I = [a<<s|i for i,a in enumerate(A)]\n        I.sort()\n \
    \       for i,ai in enumerate(I): I[i] = ai&m\n    return I\nfrom math import\
    \ inf\nfrom itertools import islice\n\nfrom enum import auto, IntFlag, IntEnum\n\
    \nclass DFSFlags(IntFlag):\n    ENTER = auto()\n    DOWN = auto()\n    BACK =\
    \ auto()\n    CROSS = auto()\n    LEAVE = auto()\n    UP = auto()\n    MAXDEPTH\
    \ = auto()\n\n    RETURN_PARENTS = auto()\n    RETURN_DEPTHS = auto()\n    BACKTRACK\
    \ = auto()\n    CONNECT_ROOTS = auto()\n\n    # Common combinations\n    ALL_EDGES\
    \ = DOWN | BACK | CROSS\n    EULER_TOUR = DOWN | UP\n    INTERVAL = ENTER | LEAVE\n\
    \    TOPDOWN = DOWN | CONNECT_ROOTS\n    BOTTOMUP = UP | CONNECT_ROOTS\n    RETURN_ALL\
    \ = RETURN_PARENTS | RETURN_DEPTHS\n\nclass DFSEvent(IntEnum):\n    ENTER = DFSFlags.ENTER\
    \ \n    DOWN = DFSFlags.DOWN \n    BACK = DFSFlags.BACK \n    CROSS = DFSFlags.CROSS\
    \ \n    LEAVE = DFSFlags.LEAVE \n    UP = DFSFlags.UP \n    MAXDEPTH = DFSFlags.MAXDEPTH\n\
    \    \n\nclass GraphBase(Sequence, Parsable):\n    def __init__(G, N: int, M:\
    \ int, U: list[int], V: list[int], \n                 deg: list[int], La: list[int],\
    \ Ra: list[int],\n                 Ua: list[int], Va: list[int], Ea: list[int]):\n\
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
    \     back_fn: Callable[[int,int,int],None] = None,\n            cross_fn: Callable[[int,int,int],None]\
    \ = None,\n            up_fn: Callable[[int,int,int],None] = None):\n        Va,\
    \ La, Ra, I = G.Va, G.La, G.Ra, G.La[:]\n        G.state, G.stack = state, stack\
    \ = u8f(G.N), elist(G.N if max_depth is None else max_depth+1)\n        G.back\
    \ = back = i32f(G.N, -2)\n        for s in G.starts(s):\n            if state[s]:\
    \ continue\n            back[s] = -1; stack.append(s)\n            while stack:\n\
    \                if state[u := stack[-1]] == 0:\n                    state[u]\
    \ = 1\n                    if enter_fn: enter_fn(u)\n                    if max_depth\
    \ is not None and len(stack) > max_depth:\n                        I[u] = Ra[u]\n\
    \                        if max_depth_fn: max_depth_fn(u)\n                if\
    \ (i := I[u]) < Ra[u]:\n                    I[u] += 1\n                    if\
    \ (s := state[v := Va[i]]) == 0:\n                        back[v] = i\n      \
    \                  stack.append(v)\n                        if down_fn: down_fn(u,v,i)\n\
    \                    elif back_fn and s == 1: back_fn(u,v,i)\n               \
    \     elif cross_fn and s == 2: cross_fn(u,v,i)\n                else:\n     \
    \               stack.pop()\n                    state[u] = 2\n              \
    \      if backtrack: state[u], I[u] = 0, La[u]\n                    if leave_fn:\
    \ leave_fn(u)\n                    if up_fn and stack: up_fn(u, stack[-1], ~back[u])\n\
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
    \            return cls(N, U, V)\n        return parse\n    \n\ndef elist(est_len:\
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
    \ x & lst.mask\n\nclass GraphWeightedBase(GraphBase):\n    def __init__(self,\
    \ N: int, M: int, U: list[int], V: list[int], W: list[int], \n               \
    \  deg: list[int], La: list[int], Ra: list[int],\n                 Ua: list[int],\
    \ Va: list[int], Wa: list[int], Ea: list[int]):\n        super().__init__(N, M,\
    \ U, V, deg, La, Ra, Ua, Va, Ea)\n        self.W = W\n        self.Wa = Wa\n \
    \       \"\"\"Wa[i] lists weights to edges from u for La[u] <= i < Ra[u].\"\"\"\
    \n        \n    def __getitem__(G, u):\n        l,r = G.La[u],G.Ra[u]\n      \
    \  return zip(G.Va[l:r], G.Wa[l:r])\n    \n    @overload\n    def distance(G)\
    \ -> list[list[int]]: ...\n    @overload\n    def distance(G, s: int = 0) -> list[int]:\
    \ ...\n    @overload\n    def distance(G, s: int, g: int) -> int: ...\n    def\
    \ distance(G, s = None, g = None):\n        if s == None: return G.floyd_warshall()\n\
    \        else: return G.dijkstra(s, g)\n\n    def dijkstra(G, s: int, t: int =\
    \ None):\n        N, S, Va, Wa = G.N, G.starts(s), G.Va, G.Wa\n        G.back,\
    \ G.D  = back, D = i32f(N, -1), [inf]*N\n        for s in S: D[s] = 0\n      \
    \  que = PriorityQueue(N, S)\n        while que:\n            u, d = que.pop()\n\
    \            if d > D[u]: continue\n            if u == t: return d\n        \
    \    for i in G.range(u): \n                if chmin(D, v := Va[i], nd := d +\
    \ Wa[i]):\n                    back[v] = i\n                    que.push(v, nd)\n\
    \        return D if t is None else inf \n\n    def kruskal(G):\n        U, V,\
    \ W, dsu, MST, need = G.U, G.V, G.W, DSU(N := G.N), [0]*(N-1), N-1\n        for\
    \ e in argsort(W):\n            u, v = dsu.merge(U[e],V[e],True)\n           \
    \ if u != v:\n                MST[need := need-1] = e\n                if not\
    \ need: break\n        return None if need else MST\n    \n    def kruskal_heap(G):\n\
    \        N, M, U, V, W = G.N, G.M, G.U, G.V, G.W \n        que = PriorityQueue(M,\
    \ list(range(M)), W)\n        dsu = DSU(N)\n        MST = [0]*(N-1)\n        need\
    \ = N-1\n        while que and need:\n            e, _ = que.pop()\n         \
    \   u, v = dsu.merge(U[e],V[e],True)\n            if u != v:\n               \
    \ MST[need := need-1] = e\n        return None if need else MST\n   \n    def\
    \ bellman_ford(G, s: int = 0) -> list[int]:\n        Ua, Va, Wa, D = G.Ua, G.Va,\
    \ G.Wa, [inf]*(N := G.N)\n        D[s] = 0\n        for _ in range(N-1):\n   \
    \         for i, u in enumerate(Ua):\n                if D[u] < inf: chmin(D,\
    \ Va[i], D[u] + Wa[i])\n        return D\n    \n    def bellman_ford_neg_cyc_check(G,\
    \ s: int = 0) -> tuple[bool, list[int]]:\n        M, U, V, W, D = G.M, G.U, G.V,\
    \ G.W, G.bellman_ford(s)\n        neg_cycle = any(D[U[i]]+W[i]<D[V[i]] for i in\
    \ range(M) if D[U[i]] < inf)\n        return neg_cycle, D\n    \n    def floyd_warshall(G)\
    \ -> list[list[int]]:\n        N, Ua, Va, Wa = G.N, G.Ua, G.Va, G.Wa\n       \
    \ D = [[inf]*N for _ in range(N)]\n        for u in range(N): D[u][u] = 0\n  \
    \      for i in range(len(Ua)): chmin(D[Ua[i]], Va[i], Wa[i])\n        for k,\
    \ Dk in enumerate(D):\n            for Di in D:\n                if Di[k] >= inf:\
    \ continue\n                for j in range(N):\n                    if Dk[j] >=\
    \ inf: continue\n                    chmin(Di, j, Di[k]+Dk[j])\n        return\
    \ D\n        \n    def floyd_warshall_neg_cyc_check(G):\n        D = G.floyd_warshall()\n\
    \        return any(D[i][i] < 0 for i in range(G.N)), D\n    \n    @classmethod\n\
    \    def compile(cls, N: int, M: int, shift: int = -1):\n        def parse(ts:\
    \ TokenStream):\n            U, V, W = u32f(M), u32f(M), [0]*M\n            for\
    \ i in range(M):\n                u, v, w = ts._line()\n                U[i],\
    \ V[i], W[i] = int(u)+shift, int(v)+shift, int(w)\n            return cls(N, U,\
    \ V, W)\n        return parse\n\n\nclass DSU:\n    def __init__(self, N):\n  \
    \      self.N = N\n        self.par = [-1] * N\n\n    def merge(self, u, v, src\
    \ = False):\n        assert 0 <= u < self.N\n        assert 0 <= v < self.N\n\n\
    \        x, y = self.leader(u), self.leader(v)\n        if x == y: return (x,y)\
    \ if src else x\n\n        if self.par[x] > self.par[y]:\n            x, y = y,\
    \ x\n\n        self.par[x] += self.par[y]\n        self.par[y] = x\n\n       \
    \ return (x,y) if src else x\n\n    def same(self, u: int, v: int):\n        assert\
    \ 0 <= u < self.N\n        assert 0 <= v < self.N\n        return self.leader(u)\
    \ == self.leader(v)\n\n    def leader(self, i) -> int:\n        assert 0 <= i\
    \ < self.N\n        par = self.par\n        p = par[i]\n        while p >= 0:\n\
    \            if par[p] < 0:\n                return p\n            par[i], i,\
    \ p = par[p], par[p], par[par[p]]\n\n        return i\n\n    def size(self, i)\
    \ -> int:\n        assert 0 <= i < self.N\n        \n        return -self.par[self.leader(i)]\n\
    \n    def groups(self) -> list[list[int]]:\n        leader_buf = [self.leader(i)\
    \ for i in range(self.N)]\n\n        result = [[] for _ in range(self.N)]\n  \
    \      for i in range(self.N):\n            result[leader_buf[i]].append(i)\n\n\
    \        return [r for r in result if r]\n\n\nfrom collections import UserList\n\
    from heapq import heapify, heappop, heappush, heappushpop, heapreplace\nfrom typing\
    \ import Generic\n\nclass HeapProtocol(Generic[_T]):\n    def pop(self) -> _T:\
    \ ...\n    def push(self, item: _T): ...\n    def pushpop(self, item: _T) -> _T:\
    \ ...\n    def replace(self, item: _T) -> _T: ...\n\nclass PriorityQueue(HeapProtocol[int],\
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
    \ self.encode(id, priority)))\n\ndef heappop_max(heap: list[_T], /) -> _T: ...\n\
    def heapsiftdown_max(heap: list[_T], root: int, pos: int): ...\ndef heapsiftup_max(heap:\
    \ list[_T], pos: int): ...\ndef heapsiftdown(heap: list[_T], root: int, pos: int):\
    \ ...\ndef heapsiftup(heap: list[_T], pos: int): ...\n\nfrom heapq import (\n\
    \    _heapify_max as heapify_max, \n    _heappop_max as heappop_max, \n    _siftdown_max\
    \ as heapsiftdown_max,\n    _siftup_max as heapsiftup_max,\n    _siftdown as heapsiftdown,\n\
    \    _siftup as heapsiftup\n)\n\ndef heappush_max(heap: list[_T], item: _T):\n\
    \    \"\"\"Push item onto heap, maintaining the heap invariant.\"\"\"\n    heap.append(item)\n\
    \    heapsiftdown_max(heap, 0, len(heap)-1)\n\ndef heapreplace_max(heap: list[_T],\
    \ item: _T) -> _T:\n    \"\"\"Pop and return the current largest value, and add\
    \ the new item.\n\n    This is more efficient than heappop_max() followed by heappush_max(),\
    \ and can be\n    more appropriate when using a fixed-size heap.  Note that the\
    \ value\n    returned may be larger than item!  That constrains reasonable uses\
    \ of\n    this routine unless written as part of a conditional replacement:\n\n\
    \        if item > heap[0]:\n            item = heapreplace_max(heap, item)\n\
    \    \"\"\"\n    returnitem = heap[0]\n    heap[0] = item\n    heapsiftup_max(heap,\
    \ 0)\n    return returnitem\n\ndef heappushpop_max(heap: list[_T], item: _T) ->\
    \ _T:\n    \"\"\"Fast version of a heappush_max followed by a heappop_max.\"\"\
    \"\n    if heap and heap[0] > item:\n        item, heap[0] = heap[0], item\n \
    \       heapsiftup_max(heap, 0)\n    return item\n\n\nclass MaxPriorityQueue(HeapProtocol[int],\
    \ UserList[int]):\n    \n    def __init__(self, N: int, ids: list[int] = None,\
    \ priorities: list[int] = None, /):\n        self.shift = N.bit_length()\n   \
    \     self.mask = (1 << self.shift)-1\n        if ids is None:\n            super().__init__()\n\
    \        elif priorities is None:\n            heapify_max(ids)\n            self.data\
    \ = ids\n        else:\n            M = len(ids)\n            data = [0]*M\n \
    \           for i in range(M):\n                data[i] = self.encode(ids[i],\
    \ priorities[i]) \n            heapify_max(data)\n            self.data = data\n\
    \n    def encode(self, id, priority):\n        return priority << self.shift |\
    \ id\n    \n    def decode(self, encoded):\n        return self.mask & encoded,\
    \ encoded >> self.shift\n    \n    def pop(self):\n        return self.decode(heappop_max(self.data))\n\
    \    \n    def push(self, id: int, priority: int):\n        heappush_max(self.data,\
    \ self.encode(id, priority))\n\n    def pushpop(self, id: int, priority: int):\n\
    \        return self.decode(heappushpop_max(self.data, self.encode(id, priority)))\n\
    \    \n    def replace(self, id: int, priority: int):\n        return self.decode(heapreplace_max(self.data,\
    \ self.encode(id, priority)))\n\n    def peek(self):\n        return self.decode(self.data[0])\n\
    \    \n\nclass GraphWeighted(GraphWeightedBase):\n    def __init__(G, N: int,\
    \ U: list[int], V: list[int], W: list[int]):\n        Ma, deg = 0, u32f(N)\n \
    \       for e in range(M := len(U)):\n            distinct = (u := U[e]) != (v\
    \ := V[e])\n            deg[u] += 1; deg[v] += distinct; Ma += 1+distinct\n  \
    \      Ea, Ua, Va, Wa = u32f(Ma), u32f(Ma), u32f(Ma), [0]*Ma\n        \n     \
    \   La, i = u32f(N), 0\n        for u,d in enumerate(deg): \n            La[u],\
    \ i = i, i + d\n        Ra = La[:]\n\n        for e in range(M):\n           \
    \ u, v, w = U[e], V[e], W[e]\n            i, j = Ra[u], Ra[v]\n            Ra[u],Ua[i],Va[i],Wa[i],Ea[i]\
    \ = i+1,u,v,w,e\n            if i == j: continue # don't add self loops twice\n\
    \            Ra[v],Ua[j],Va[j],Wa[j],Ea[j] = j+1,v,u,w,e\n\n        super().__init__(N,\
    \ M, U, V, W, deg, La, Ra, Ua, Va, Wa, Ea)\n\nfrom typing import Callable, Literal,\
    \ TypeVar, Union, overload\n\nclass TreeBase(GraphBase):\n    @overload\n    def\
    \ distance(T) -> list[list[int]]: ...\n    @overload\n    def distance(T, s: int\
    \ = 0) -> list[int]: ...\n    @overload\n    def distance(T, s: int, g: int) ->\
    \ int: ...\n    def distance(T, s = None, g = None):\n        if s == None:\n\
    \            return [T.dfs_distance(u) for u in range(T.N)]\n        else:\n \
    \           return T.dfs_distance(s, g)\n\n    @overload\n    def diameter(T)\
    \ -> int: ...\n    @overload\n    def diameter(T, endpoints: Literal[True]) ->\
    \ tuple[int,int,int]: ...\n    def diameter(T, endpoints = False):\n        mask\
    \ = (1 << (shift := T.N.bit_length())) - 1\n        s = max(d << shift | v for\
    \ v,d in enumerate(T.distance(0))) & mask\n        dg = max(d << shift | v for\
    \ v,d in enumerate(T.distance(s))) \n        diam, g = dg >> shift, dg & mask\n\
    \        return (diam, s, g) if endpoints else diam\n    \n    def dfs_distance(T,\
    \ s: int, g: Union[int,None] = None):\n        stack, Va = elist(N := T.N), T.Va\n\
    \        T.D, T.back = D, back = [inf]*N, i32f(N, -1)\n        D[s] = 0\n    \
    \    stack.append(s)\n        while stack:\n            nd = D[u := stack.pop()]+1\n\
    \            if u == g: return nd-1\n            for i in T.range(u):\n      \
    \          if nd < D[v := Va[i]]:\n                    D[v], back[v] = nd, i\n\
    \                    stack.append(v)\n        return D if g is None else inf\n\
    \n    def rerooting_dp(T, e: _T, \n                     merge: Callable[[_T,_T],_T],\
    \ \n                     edge_op: Callable[[_T,int,int,int],_T] = lambda s,i,p,u:s,\n\
    \                     s: int = 0):\n        La, Ua, Va = T.La, T.Ua, T.Va\n  \
    \      order, dp, suf, I = T.dfs_topdown(s), [e]*T.N, [e]*len(Ua), T.Ra[:]\n \
    \       # up\n        for i in order[::-1]:\n            u,v = Ua[i], Va[i]\n\
    \            # subtree v finished up pass, store value to accumulate for u\n \
    \           dp[v] = new = edge_op(dp[v], i, u, v)\n            dp[u] = merge(dp[u],\
    \ new)\n            # suffix accumulation\n            if (c:=I[u]-1) > La[u]:\
    \ suf[c-1] = merge(suf[c], new)\n            I[u] = c\n        # down\n      \
    \  dp[s] = e # at this point dp stores values to be merged in parent\n       \
    \ for i in order:\n            u,v = Ua[i], Va[i]\n            dp[u] = merge(pre\
    \ := dp[u], dp[v])\n            dp[v] = edge_op(merge(suf[I[u]], pre), i, v, u)\n\
    \            I[u] += 1\n        return dp\n    \n    def euler_tour(T, s = 0):\n\
    \        N, Va = len(T), T.Va\n        tin, tout, par, back = [-1]*N,[-1]*N,[-1]*N,[0]*N\n\
    \        order, delta = elist(2*N), elist(2*N)\n        \n        stack = elist(N)\n\
    \        stack.append(s)\n        while stack:\n            p = par[u := stack.pop()]\n\
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
    \ N, N-1, shift)\n    \n\n_T = TypeVar('T')\nclass TreeWeightedBase(TreeBase,\
    \ GraphWeightedBase):\n\n    def dfs_distance(T, s: int, g: Union[int,None] =\
    \ None):\n        stack, Wa, Va = elist(N := T.N), T.Wa, T.Va\n        T.D, T.back\
    \ = D, back = [inf]*N, i32f(N, -1)\n        stack.append(s)\n        D[s] = 0\n\
    \        while stack:\n            d = D[u := stack.pop()]\n            if u ==\
    \ g: return d\n            for i in T.range(u):\n                if (nd := d+Wa[i])\
    \ < D[v := Va[i]]:\n                    D[v], back[v] = nd, i\n              \
    \      stack.append(v)\n        return D if g is None else inf \n    \n    def\
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
    \nclass TreeWeighted(TreeWeightedBase, GraphWeighted):\n    pass\n\n\nclass HLD(Sequence[int]):\n\
    \    def __init__(self, T, r=0):\n        N = len(T)\n        T.hld_precomp(r)\n\
    \        self.N, self.T, self.size, self.depth = N, T, T.size, T.depth\n     \
    \   self.order, self.start, self.end = T.order, T.tin, T.tout\n        self.par,\
    \ self.heavy, self.head = T.par, T.heavy, T.head\n\n    def __getitem__(self,\
    \ key):\n        return self.start[key]\n    \n    def __len__(self):\n      \
    \  return len(self.start)\n    \n    def __contains__(self, value):\n        return\
    \ self.start.__contains__(value)\n    \n    def subtree_range(self, v):\n    \
    \    return self.start[v], self.end[v]\n\n    def path(self, u, v, query_fn, edge=False):\n\
    \        head, depth, par, start = self.head, self.depth, self.par, self.start\n\
    \        while head[u] != head[v]:\n            if depth[head[u]] < depth[head[v]]:\n\
    \                u,v = v,u\n            query_fn(start[head[u]], start[u]+1)\n\
    \            u = par[head[u]]\n\n        if depth[u] < depth[v]:\n           \
    \ u,v = v,u\n        query_fn(start[v]+edge, start[u]+1)\n\nclass HLDWeighted(HLD):\n\
    \    def __init__(self, T, r=0):\n        super().__init__(T, r)\n        self.weights\
    \ = T.Wpar\n\nfrom typing import Iterable, Type, Union, overload\n\n@overload\n\
    def read() -> Iterable[int]: ...\n@overload\ndef read(spec: int) -> list[int]:\
    \ ...\n@overload\ndef read(spec: Union[Type[_T],_T], char=False) -> _T: ...\n\
    def read(spec: Union[Type[_T],_T] = None, char=False):\n    if not char and spec\
    \ is None: return map(int, TokenStream.default.line())\n    parser: _T = Parser.compile(spec)\n\
    \    return parser(CharStream.default if char else TokenStream.default)\n\ndef\
    \ write(*args, **kwargs):\n    \"\"\"Prints the values to a stream, or to stdout_fast\
    \ by default.\"\"\"\n    sep, file = kwargs.pop(\"sep\", \" \"), kwargs.pop(\"\
    file\", IOWrapper.stdout)\n    at_start = True\n    for x in args:\n        if\
    \ not at_start:\n            file.write(sep)\n        file.write(str(x))\n   \
    \     at_start = False\n    file.write(kwargs.pop(\"end\", \"\\n\"))\n    if kwargs.pop(\"\
    flush\", False):\n        file.flush()\n\nif __name__ == \"__main__\":\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc294/tasks/abc294_g\n\
    \ndef main():\n    N = read(int)\n    T = read(TreeWeighted[N])\n\n    hld = HLDWeighted(T)\n\
    \    W = [hld.weights[i] for i in hld.order]\n    bit = BIT(W)\n    ans = 0\n\n\
    \    def query(l, r):\n        nonlocal ans\n        ans += bit.range_sum(l,r)\
    \ \n\n    Q = read(int)\n    for q in read(list[tuple[int, int, int], Q]):\n \
    \       match q:\n            case 1, i, w:\n                i -= 1  # Convert\
    \ to 0-based index\n                u, v = T.U[i], T.V[i]\n                idx\
    \ = hld[u if hld.par[u] == v else v]\n                bit.set(idx, w)\n      \
    \      case 2, u, v:\n                u, v = u - 1, v - 1\n                ans\
    \ = 0\n                hld.path(u,v, query, True)\n                write(ans)\n\
    \nfrom cp_library.ds.tree.bit_cls import BIT\nfrom cp_library.alg.tree.fast.tree_weighted_cls\
    \ import TreeWeighted\nfrom cp_library.alg.tree.heavy_light_decomposition_weighted_cls\
    \ import HLDWeighted\nfrom cp_library.io.read_fn import read\nfrom cp_library.io.write_fn\
    \ import write\n\nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - cp_library/ds/tree/bit_cls.py
  - cp_library/alg/tree/fast/tree_weighted_cls.py
  - cp_library/alg/tree/heavy_light_decomposition_weighted_cls.py
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/alg/graph/fast/graph_weighted_cls.py
  - cp_library/alg/tree/fast/tree_weighted_base_cls.py
  - cp_library/alg/tree/heavy_light_decomposition_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  - cp_library/alg/graph/fast/graph_weighted_base_cls.py
  - cp_library/ds/array_init_fn.py
  - cp_library/alg/tree/fast/tree_base_cls.py
  - cp_library/ds/elist_fn.py
  - cp_library/alg/dp/chmin_fn.py
  - cp_library/alg/iter/argsort_fn.py
  - cp_library/alg/graph/fast/graph_base_cls.py
  - cp_library/ds/dsu_cls.py
  - cp_library/ds/heap/priority_queue_cls.py
  - cp_library/bit/pack_sm_fn.py
  - cp_library/ds/heap/heap_proto.py
  - cp_library/ds/heap/heapq_max_import.py
  - cp_library/alg/graph/dfs_options_cls.py
  - cp_library/ds/packet_list_cls.py
  isVerificationFile: true
  path: test/atcoder/abc/abc294_g_fast_tree_heavy_light_decomposition.test.py
  requiredBy: []
  timestamp: '2025-03-09 09:15:44+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/atcoder/abc/abc294_g_fast_tree_heavy_light_decomposition.test.py
layout: document
redirect_from:
- /verify/test/atcoder/abc/abc294_g_fast_tree_heavy_light_decomposition.test.py
- /verify/test/atcoder/abc/abc294_g_fast_tree_heavy_light_decomposition.test.py.html
title: test/atcoder/abc/abc294_g_fast_tree_heavy_light_decomposition.test.py
---
