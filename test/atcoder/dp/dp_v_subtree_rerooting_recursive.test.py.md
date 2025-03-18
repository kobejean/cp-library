---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/rerooting_recursive_cls.py
    title: cp_library/alg/dp/rerooting_recursive_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/sort2_fn.py
    title: cp_library/alg/dp/sort2_fn.py
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
    path: cp_library/alg/iter/presum_fn.py
    title: cp_library/alg/iter/presum_fn.py
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
    path: cp_library/ds/bidirectional_array_cls.py
    title: cp_library/ds/bidirectional_array_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/min_sparse_table_cls.py
    title: cp_library/ds/min_sparse_table_cls.py
  - icon: ':question:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_fn.py
    title: cp_library/io/read_fn.py
  - icon: ':question:'
    path: cp_library/io/write_fn.py
    title: cp_library/io/write_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/misc/setrecursionlimit.py
    title: cp_library/misc/setrecursionlimit.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/dp/tasks/dp_v
    links:
    - https://atcoder.jp/contests/dp/tasks/dp_v
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/dp/tasks/dp_v\n\
    \ndef main():\n    N, M = read()\n    T = read(Tree[N])\n\n    def mul(a,b):\n\
    \        return a*b%M\n\n    def add_node(v,res):\n        return (res+1)%M\n\n\
    \    rr = ReRootingDP(T, 1, mul, add_node)\n\n    write(*rr.solve(), sep='\\n')\n\
    \n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\
    \n             https://kobejean.github.io/cp-library               \n'''\n\n\n\
    import sys\nsys.setrecursionlimit(10**6)\nimport pypyjit\npypyjit.set_param(\"\
    max_unroll_recursion=-1\")\nimport typing\n\n\nclass BidirectionalArray:\n   \
    \ def __init__(self, e, op, data):\n        self.size = len(data)\n        self.prefix\
    \ = [e] + data.copy()\n        self.suffix = data.copy() + [e]\n        self.e\
    \ = e\n        self.op = op\n        for i in range(self.size):\n            self.prefix[i+1]\
    \ = op(self.prefix[i], self.prefix[i+1])\n        for i in range(self.size,0,-1):\n\
    \            self.suffix[i-1] = op(self.suffix[i-1], self.suffix[i])\n    def\
    \ left(self, l): return self.prefix[l]\n    def right(self, r): return self.suffix[r]\n\
    \    def all(self): return self.prefix[-1]\n    def out(self, l, r=None):\n  \
    \      r = l+1 if r is None else r\n        return self.op(self.prefix[l], self.suffix[r])\n\
    \nclass ReRootingDP():\n    \"\"\" A class implementation of the Re-rooting Dynamic\
    \ Programming technique. \"\"\"\n    S = typing.TypeVar('S')\n    MergeOp = typing.Callable[[S,\
    \ S], S]\n    AddNodeOp = typing.Callable[[int, S], S]\n    AddEdgeOp = typing.Callable[[int,\
    \ int, S], S]\n\n    def __init__(self, T: list[list[int]], e: S,\n          \
    \       merge: MergeOp, \n                 add_node: AddNodeOp = lambda u,s:s,\
    \ \n                 add_edge: AddEdgeOp = lambda u,v,s:s):\n        \"\"\"\n\
    \        T: list[list[int]] - Adjacency list representation of the tree.\n   \
    \     e: S - Identity element for the merge operation.\n        merge: (S,S) ->\
    \ S - Function to merge two states.\n        add_node: (int,S) -> S - Function\
    \ to incorporate a node into the state.\n        add_edge: (int,int,S) -> S -\
    \ Function to incorporate an edge into the state.\n        \"\"\"\n        self.T\
    \ = T\n        self.e = e\n        self.merge = merge\n        self.add_node =\
    \ add_node\n        self.add_edge = add_edge\n    \n    def solve(self) -> list[S]:\n\
    \        dp = [[self.e]*len(adj) for adj in self.T]\n        ans = [None for _\
    \ in range(len(self.T))]\n\n        def dfs_up(u, p=None):\n            res =\
    \ self.e\n            for i,v in enumerate(self.T[u]):\n                if v !=\
    \ p:\n                    dp[u][i] = self.add_edge(u, v, dfs_up(v, u))\n     \
    \               res = self.merge(res, dp[u][i])\n            return self.add_node(u,\
    \ res)\n\n        def dfs_down(u, p=None):\n            ba = BidirectionalArray(self.e,\
    \ self.merge, dp[u])\n            for i,v in enumerate(self.T[u]):\n         \
    \       if v != p:\n                    dp[v][self.T[v].index(u)] = self.add_edge(v,\
    \ u, self.add_node(u, ba.out(i)))\n                    dfs_down(v, u)\n      \
    \      ans[u] = ba.all()\n\n        dfs_up(0)\n        dfs_down(0)\n        return\
    \ ans\n\n\nfrom typing import Iterable, Type, Union, overload\nfrom collections\
    \ import deque\nfrom numbers import Number\nfrom types import GenericAlias \n\
    from typing import Callable, Collection, Iterator, Union\nimport os\nfrom io import\
    \ BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n    BUFSIZE = 8192\n    newlines\
    \ = 0\n\n    def __init__(self, file):\n        self._fd = file.fileno()\n   \
    \     self.buffer = BytesIO()\n        self.writable = \"x\" in file.mode or \"\
    r\" not in file.mode\n        self.write = self.buffer.write if self.writable\
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
    \ return cls(next(ts))\n        return parser\n\n@overload\ndef read() -> Iterable[int]:\
    \ ...\n@overload\ndef read(spec: int) -> list[int]: ...\n@overload\ndef read(spec:\
    \ Union[Type[_T],_T], char=False) -> _T: ...\ndef read(spec: Union[Type[_T],_T]\
    \ = None, char=False):\n    if not char and spec is None: return map(int, TokenStream.default.line())\n\
    \    parser: _T = Parser.compile(spec)\n    return parser(CharStream.default if\
    \ char else TokenStream.default)\n\ndef write(*args, **kwargs):\n    \"\"\"Prints\
    \ the values to a stream, or to stdout_fast by default.\"\"\"\n    sep, file =\
    \ kwargs.pop(\"sep\", \" \"), kwargs.pop(\"file\", IOWrapper.stdout)\n    at_start\
    \ = True\n    for x in args:\n        if not at_start:\n            file.write(sep)\n\
    \        file.write(str(x))\n        at_start = False\n    file.write(kwargs.pop(\"\
    end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n        file.flush()\n\
    \n\n\nclass Edge(tuple, Parsable):\n    @classmethod\n    def compile(cls, I=-1):\n\
    \        def parse(ts: TokenStream):\n            u,v = ts.line()\n          \
    \  return cls((int(u)+I,int(v)+I))\n        return parse\n\nfrom enum import auto,\
    \ IntFlag, IntEnum\n\nclass DFSFlags(IntFlag):\n    ENTER = auto()\n    DOWN =\
    \ auto()\n    BACK = auto()\n    CROSS = auto()\n    LEAVE = auto()\n    UP =\
    \ auto()\n    MAXDEPTH = auto()\n\n    RETURN_PARENTS = auto()\n    RETURN_DEPTHS\
    \ = auto()\n    BACKTRACK = auto()\n    CONNECT_ROOTS = auto()\n\n    # Common\
    \ combinations\n    ALL_EDGES = DOWN | BACK | CROSS\n    EULER_TOUR = DOWN | UP\n\
    \    INTERVAL = ENTER | LEAVE\n    TOPDOWN = DOWN | CONNECT_ROOTS\n    BOTTOMUP\
    \ = UP | CONNECT_ROOTS\n    RETURN_ALL = RETURN_PARENTS | RETURN_DEPTHS\n\nclass\
    \ DFSEvent(IntEnum):\n    ENTER = DFSFlags.ENTER \n    DOWN = DFSFlags.DOWN \n\
    \    BACK = DFSFlags.BACK \n    CROSS = DFSFlags.CROSS \n    LEAVE = DFSFlags.LEAVE\
    \ \n    UP = DFSFlags.UP \n    MAXDEPTH = DFSFlags.MAXDEPTH\n    \n\ndef elist(est_len:\
    \ int) -> list: ...\ntry:\n    from __pypy__ import newlist_hint\nexcept:\n  \
    \  def newlist_hint(hint):\n        return []\nelist = newlist_hint\n    \nfrom\
    \ math import inf\n\nclass GraphProtocol(list, Parsable):\n    def __init__(G,\
    \ N: int, E: list = None, adj: Iterable = None):\n        G.N = N\n        if\
    \ E is not None:\n            G.M, G.E = len(E), E\n        if adj is not None:\n\
    \            super().__init__(adj)\n\n    def neighbors(G, v: int) -> Iterable[int]:\n\
    \        return G[v]\n    \n    def edge_ids(G) -> list[list[int]]: ...\n\n  \
    \  @overload\n    def distance(G) -> list[list[int]]: ...\n    @overload\n   \
    \ def distance(G, s: int = 0) -> list[int]: ...\n    @overload\n    def distance(G,\
    \ s: int, g: int) -> int: ...\n    def distance(G, s = None, g = None):\n    \
    \    if s == None:\n            return G.floyd_warshall()\n        else:\n   \
    \         return G.bfs(s, g)\n\n    @overload\n    def bfs(G, s: Union[int,list]\
    \ = 0) -> list[int]: ...\n    @overload\n    def bfs(G, s: Union[int,list], g:\
    \ int) -> int: ...\n    def bfs(G, s = 0, g = None):\n        D = [inf for _ in\
    \ range(G.N)]\n        q = deque([s] if isinstance(s, int) else s)\n        for\
    \ u in q: D[u] = 0\n        while q:\n            nd = D[u := q.popleft()]+1\n\
    \            if u == g: return D[u]\n            for v in G.neighbors(u):\n  \
    \              if nd < D[v]:\n                    D[v] = nd\n                \
    \    q.append(v)\n        return D if g is None else inf \n\n    @overload\n \
    \   def shortest_path(G, s: int, g: int) -> Union[list[int],None]: ...\n    @overload\n\
    \    def shortest_path(G, s: int, g: int, distances = True) -> tuple[Union[list[int],None],list[int]]:\
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
    \ D) if distances else path[::-1]\n            \n     \n            \n       \
    \ \n    def floyd_warshall(G) -> list[list[int]]:\n        D = [[inf]*G.N for\
    \ _ in range(G.N)]\n\n        for u in range(G.N):\n            D[u][u] = 0\n\
    \            for v in G.neighbors(u):\n                D[u][v] = 1\n        \n\
    \        for k, Dk in enumerate(D):\n            for Di in D:\n              \
    \  if Di[k] == inf: continue\n                for j in range(G.N):\n         \
    \           if Dk[j] == inf: continue\n                    Di[j] = min(Di[j],\
    \ Di[k]+Dk[j])\n        return D\n    \n    def find_cycle(G, s = 0, vis = None,\
    \ par = None):\n        N = G.N\n        vis = vis or [0] * N\n        par = par\
    \ or [-1] * N\n        if vis[s]: return None\n        vis[s] = 1\n        stack\
    \ = [(True, s)]\n        while stack:\n            forw, v = stack.pop()\n   \
    \         if forw:\n                stack.append((False, v))\n               \
    \ vis[v] = 1\n                for u in G.neighbors(v):\n                    if\
    \ vis[u] == 1 and u != par[v]:\n                        # Cycle detected\n   \
    \                     cyc = [u]\n                        vis[u] = 2\n        \
    \                while v != u:\n                            cyc.append(v)\n  \
    \                          vis[v] = 2\n                            v = par[v]\n\
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
    \        return bridges\n\n    def articulation_points(G):\n        \"\"\"\n \
    \       Find articulation points in an undirected graph using DFS events.\n  \
    \      Returns a boolean list that is True for indices where the vertex is an\
    \ articulation point.\n        \"\"\"\n        N = G.N\n        order = [-1] *\
    \ N\n        low = [-1] * N\n        par = [-1] * N\n        state = [0] * N\n\
    \        children = [0] * N\n        ap = [False] * N\n        time = 0\n    \
    \    stack = list(range(N))\n\n        while stack:\n            v = stack.pop()\n\
    \            p = par[v]\n            if state[v] == 0:\n                state[v]\
    \ = 1\n                order[v] = low[v] = time\n                time += 1\n \
    \           \n                stack.append(v)\n                for child in G[v]:\n\
    \                    if order[child] == -1:\n                        par[child]\
    \ = v\n                        stack.append(child)\n                    elif child\
    \ != p:\n                        low[v] = min(low[v], order[child])\n        \
    \        if p != -1:\n                    children[p] += 1\n            elif state[v]\
    \ == 1:\n                state[v] = 2\n                ap[v] |= p == -1 and children[v]\
    \ > 1\n                if p != -1:\n                    low[p] = min(low[p], low[v])\n\
    \                    ap[p] |= par[p] != -1 and low[v] >= order[p]\n\n        return\
    \ ap\n    \n    def dfs_events(G, flags: DFSFlags, s: Union[int,list,None] = None,\
    \ max_depth: Union[int,None] = None):\n        if flags == DFSFlags.INTERVAL:\n\
    \            if max_depth is None:\n                return G.dfs_enter_leave(s)\n\
    \        elif flags == DFSFlags.DOWN or flags == DFSFlags.TOPDOWN:\n         \
    \   if max_depth is None:\n                edges = G.dfs_topdown(s, DFSFlags.CONNECT_ROOTS\
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
    \ u))\n\n        return events\n    \n    def dfs_topdown(G, s: Union[int,list,None]\
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
    \ G.dfs_topdown(s, connect_roots)\n        edges.reverse()\n        return edges\n\
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
    \        def parse(ts: TokenStream):\n            return cls(N, [edge(ts) for\
    \ _ in range(M)])\n        return parse\n    \n\nclass Graph(GraphProtocol):\n\
    \    def __init__(G, N: int, E: list[Edge]=[]):\n        super().__init__(N, E,\
    \ ([] for _ in range(N)))\n        for u,v in G.E:\n            G[u].append(v)\n\
    \            G[v].append(u)\n\n    def edge_ids(G) -> list[list[int]]:\n     \
    \   Eid = [[] for _ in range(G.N)]\n        for e,(u,v) in enumerate(G.E):\n \
    \           Eid[u].append(e)\n            Eid[v].append(e)\n        return Eid\n\
    \n    @classmethod\n    def compile(cls, N: int, M: int, E: Union[type,int] =\
    \ Edge[-1]):\n        if isinstance(E, int): E = Edge[E]\n        return super().compile(N,\
    \ M, E)\n\n    \n\nfrom typing import overload, Literal, Union\nfrom functools\
    \ import cached_property\n\ndef sort2(a, b):\n    return (a,b) if a < b else (b,a)\n\
    \nimport operator\nfrom itertools import accumulate\n\ndef presum(iter: Iterable[_T],\
    \ func: Callable[[_T,_T],_T] = None, initial: _T = None, step = 1) -> list[_T]:\n\
    \    if step == 1:\n        return list(accumulate(iter, func, initial=initial))\n\
    \    else:\n        assert step >= 2\n        if func is None:\n            func\
    \ = operator.add\n        A = list(iter)\n        if initial is not None:\n  \
    \          A = [initial] + A\n        for i in range(step,len(A)):\n         \
    \   A[i] = func(A[i], A[i-step])\n        return A\nfrom itertools import pairwise\n\
    from typing import Any, List\n\nclass MinSparseTable:\n    def __init__(self,\
    \ arr: List[Any]):\n        self.N = N = len(arr)\n        self.log = N.bit_length()\n\
    \        \n        self.offsets = offsets = [0]\n        for i in range(1, self.log):\n\
    \            offsets.append(offsets[-1] + N - (1 << (i-1)) + 1)\n            \n\
    \        self.st = st = [0] * (offsets[-1] + N - (1 << (self.log-1)) + 1)\n  \
    \      st[:N] = arr \n        \n        for i,ni in pairwise(range(self.log)):\n\
    \            start, nxt, d = offsets[i], offsets[ni], 1 << i\n            for\
    \ j in range(N - (1 << ni) + 1):\n                st[nxt+j] = min(st[k := start+j],\
    \ st[k + d])\n\n    def query(self, l: int, r: int) -> Any:\n        k = (r-l).bit_length()\
    \ - 1\n        start, st = self.offsets[k], self.st\n        return min(st[start\
    \ + l], st[start + r - (1 << k)])\n    \n    def __repr__(self) -> str:\n    \
    \    rows, offsets, log, st = [], self.offsets, self.log, self.st\n        for\
    \ i in range(log):\n            start = offsets[i]\n            end = offsets[i+1]\
    \ if i+1 < log else len(st)\n            rows.append(f\"{i:<2d} {st[start:end]}\"\
    )\n        return '\\n'.join(rows)\n\nclass LCATable(MinSparseTable):\n    def\
    \ __init__(lca, T, root = 0):\n        N = len(T)\n        T.euler_tour(root)\n\
    \        lca.depth = depth = presum(T.delta)\n        lca.tin, lca.tout = T.tin[:],\
    \ T.tout[:]\n        lca.mask = (1 << (shift := N.bit_length()))-1\n        lca.shift\
    \ = shift\n        order = T.order\n        M = len(order)\n        packets =\
    \ [0]*M\n        for i in range(M):\n            packets[i] = depth[i] << shift\
    \ | order[i] \n        super().__init__(packets)\n\n    def _query(lca, u, v):\n\
    \        tin = lca.tin\n        l, r = sort2(tin[u], tin[v]); r += 1\n       \
    \ da = super().query(l, r)\n        return l, r, da & lca.mask, da >> lca.shift\n\
    \n    def query(lca, u, v) -> tuple[int,int]:\n        l, r, a, d = lca._query(u,\
    \ v)\n        return a, d\n    \n    def distance(lca, u, v) -> int:\n       \
    \ l, r, a, d = lca._query(u, v)\n        return lca.depth[l] + lca.depth[r-1]\
    \ - 2*d\n    \n    def path(lca, u, v):\n        path, par, lca, c = [], lca.T.par,\
    \ lca.query(u, v)[0], u\n        while c != lca:\n            path.append(c)\n\
    \            c = par[c]\n        path.append(lca)\n        rev_path, c = [], v\n\
    \        while c != lca:\n            rev_path.append(c)\n            c = par[c]\n\
    \        path.extend(reversed(rev_path))\n        return path\n\nclass TreeProtocol(GraphProtocol):\n\
    \n    @cached_property\n    def lca(T):\n        return LCATable(T)\n    \n  \
    \  @overload\n    def diameter(T) -> int: ...\n    @overload\n    def diameter(T,\
    \ endpoints: Literal[True]) -> tuple[int,int,int]: ...\n    def diameter(T, endpoints\
    \ = False):\n        mask = (1 << (shift := T.N.bit_length())) - 1\n        s\
    \ = max(d << shift | v for v,d in enumerate(T.distance(0))) & mask\n        dg\
    \ = max(d << shift | v for v,d in enumerate(T.distance(s))) \n        diam, g\
    \ = dg >> shift, dg & mask\n        return (diam, s, g) if endpoints else diam\n\
    \    \n    @overload\n    def distance(T) -> list[list[int]]: ...\n    @overload\n\
    \    def distance(T, s: int = 0) -> list[int]: ...\n    @overload\n    def distance(T,\
    \ s: int, g: int) -> int: ...\n    def distance(T, s = None, g = None):\n    \
    \    if s == None:\n            return [T.dfs(u) for u in range(T.N)]\n      \
    \  else:\n            return T.dfs(s, g)\n            \n    @overload\n    def\
    \ dfs(T, s: int = 0) -> list[int]: ...\n    @overload\n    def dfs(T, s: int,\
    \ g: int) -> int: ...\n    def dfs(T, s = 0, g = None):\n        D = [inf for\
    \ _ in range(T.N)]\n        D[s] = 0\n        state = [True for _ in range(T.N)]\n\
    \        stack = [s]\n\n        while stack:\n            u = stack.pop()\n  \
    \          if u == g: return D[u]\n            state[u] = False\n            for\
    \ v in T[u]:\n                if state[v]:\n                    D[v] = D[u]+1\n\
    \                    stack.append(v)\n        return D if g is None else inf \n\
    \n\n    def dfs_events(G, flags: DFSFlags, s: int = 0):         \n        events\
    \ = []\n        stack = [(s,-1)]\n        adj = [None]*G.N\n\n\n        while\
    \ stack:\n            u, p = stack[-1]\n            \n            if adj[u] is\
    \ None:\n                adj[u] = iter(G.neighbors(u))\n                if DFSFlags.ENTER\
    \ in flags:\n                    events.append((DFSEvent.ENTER, u))\n        \
    \    \n            if (v := next(adj[u], None)) is not None:\n               \
    \ if v == p:\n                    if DFSFlags.BACK in flags:\n               \
    \         events.append((DFSEvent.BACK, u, v))\n                else:\n      \
    \              if DFSFlags.DOWN in flags:\n                        events.append((DFSEvent.DOWN,\
    \ u, v))\n                    stack.append((v,u))\n            else:\n       \
    \         stack.pop()\n\n                if DFSFlags.LEAVE in flags:\n       \
    \             events.append((DFSEvent.LEAVE, u))\n                if p != -1 and\
    \ DFSFlags.UP in flags:\n                    events.append((DFSEvent.UP, u, p))\n\
    \        return events\n    \n    def euler_tour(T, s = 0):\n        N = len(T)\n\
    \        T.tin = tin = [-1] * N\n        T.tout = tout = [-1] * N\n        T.par\
    \ = par = [-1] * N\n        T.order = order = elist(2*N)\n        T.delta = delta\
    \ = elist(2*N)\n        \n        stack = elist(N)\n        stack.append(s)\n\n\
    \        while stack:\n            u = stack.pop()\n            p = par[u]\n \
    \           \n            if tin[u] == -1:\n                tin[u] = len(order)\n\
    \                \n                for v in T[u]:\n                    if v !=\
    \ p:\n                        par[v] = u\n                        stack.append(u)\n\
    \                        stack.append(v)\n                \n                delta.append(1)\n\
    \            else:\n                delta.append(-1)\n            \n         \
    \   order.append(u)\n            tout[u] = len(order)\n        delta[0] = delta[-1]\
    \ = 0\n\n    def hld_precomp(T, r = 0):\n        N, time = T.N, 0\n        tin,\
    \ tout, size = [0]*N, [0]*N, [1]*N+[0]\n        par, heavy, head = [-1]*N, [-1]*N,\
    \ [r]*N\n        depth, order, state = [0]*N, [0]*N, [0]*N\n        stack = elist(N)\n\
    \        stack.append(r)\n        while stack:\n            if (s := state[v :=\
    \ stack.pop()]) == 0: # dfs down\n                p, state[v] = par[v], 1\n  \
    \              stack.append(v)\n                for c in T[v]:\n             \
    \       if c != p:\n                        depth[c], par[c] = depth[v]+1, v\n\
    \                        stack.append(c)\n\n            elif s == 1: # dfs up\n\
    \                p, l = par[v], -1\n                for c in T[v]:\n         \
    \           if c != p:\n                        size[v] += size[c]\n         \
    \               if size[c] > size[l]:\n                            l = c\n   \
    \             heavy[v] = l\n                if p == -1:\n                    state[v]\
    \ = 2\n                    stack.append(v)\n\n            elif s == 2: # decompose\
    \ down\n                p, h, l = par[v], head[v], heavy[v]\n                tin[v],\
    \ order[time], state[v] = time, v, 3\n                time += 1\n            \
    \    stack.append(v)\n                \n                for c in T[v]:\n     \
    \               if c != p and c != l:\n                        head[c], state[c]\
    \ = c, 2\n                        stack.append(c)\n\n                if l != -1:\n\
    \                    head[l], state[l] = h, 2\n                    stack.append(l)\n\
    \n            elif s == 3: # decompose up\n                tout[v] = time\n  \
    \      T.size, T.depth = size, depth\n        T.order, T.tin, T.tout = order,\
    \ tin, tout\n        T.par, T.heavy, T.head = par, heavy, head\n\nclass Tree(TreeProtocol,\
    \ Graph):\n    @classmethod\n    def compile(cls, N: int, E: Union[type,int] =\
    \ Edge[-1]):\n        return Graph.compile.__func__(cls, N, N-1, E)\n    \n  \
    \  \n\nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/dp/tasks/dp_v\n\
    \ndef main():\n    N, M = read()\n    T = read(Tree[N])\n\n    def mul(a,b):\n\
    \        return a*b%M\n\n    def add_node(v,res):\n        return (res+1)%M\n\n\
    \    rr = ReRootingDP(T, 1, mul, add_node)\n\n    write(*rr.solve(), sep='\\n')\n\
    \nfrom cp_library.alg.dp.rerooting_recursive_cls import ReRootingDP\nfrom cp_library.io.read_fn\
    \ import read\nfrom cp_library.io.write_fn import write\nfrom cp_library.alg.tree.tree_cls\
    \ import Tree\n\nif __name__ == '__main__':\n    main()"
  dependsOn:
  - cp_library/alg/dp/rerooting_recursive_cls.py
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/alg/tree/tree_cls.py
  - cp_library/misc/setrecursionlimit.py
  - cp_library/ds/bidirectional_array_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  - cp_library/alg/graph/edge_cls.py
  - cp_library/alg/graph/graph_cls.py
  - cp_library/alg/tree/tree_proto.py
  - cp_library/alg/graph/graph_proto.py
  - cp_library/ds/elist_fn.py
  - cp_library/alg/graph/dfs_options_cls.py
  - cp_library/alg/tree/lca_table_iterative_cls.py
  - cp_library/alg/dp/sort2_fn.py
  - cp_library/alg/iter/presum_fn.py
  - cp_library/ds/min_sparse_table_cls.py
  isVerificationFile: true
  path: test/atcoder/dp/dp_v_subtree_rerooting_recursive.test.py
  requiredBy: []
  timestamp: '2025-03-19 01:19:38+07:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/atcoder/dp/dp_v_subtree_rerooting_recursive.test.py
layout: document
redirect_from:
- /verify/test/atcoder/dp/dp_v_subtree_rerooting_recursive.test.py
- /verify/test/atcoder/dp/dp_v_subtree_rerooting_recursive.test.py.html
title: test/atcoder/dp/dp_v_subtree_rerooting_recursive.test.py
---
