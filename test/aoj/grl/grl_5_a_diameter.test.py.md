---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/min2_fn.py
    title: cp_library/alg/dp/min2_fn.py
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
    path: cp_library/alg/graph/edge_weighted_cls.py
    title: cp_library/alg/graph/edge_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/graph_proto.py
    title: cp_library/alg/graph/graph_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/graph_weighted_cls.py
    title: cp_library/alg/graph/graph_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/graph_weighted_proto.py
    title: cp_library/alg/graph/graph_weighted_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/presum_fn.py
    title: cp_library/alg/iter/presum_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/lca_table_iterative_cls.py
    title: cp_library/alg/tree/lca_table_iterative_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
    title: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_proto.py
    title: cp_library/alg/tree/tree_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_weighted_cls.py
    title: cp_library/alg/tree/tree_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_weighted_proto.py
    title: cp_library/alg/tree/tree_weighted_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/csr/csr_incremental_cls.py
    title: cp_library/ds/csr/csr_incremental_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/dsu_cls.py
    title: cp_library/ds/dsu_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/fast_heapq.py
    title: cp_library/ds/heap/fast_heapq.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/heap_proto.py
    title: cp_library/ds/heap/heap_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/priority_queue_cls.py
    title: cp_library/ds/heap/priority_queue_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/min_sparse_table_cls.py
    title: cp_library/ds/min_sparse_table_cls.py
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
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_5_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_5_A
  bundledCode: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_5_A\n\
    \ndef main():\n    N = read(int)\n    T = read(TreeWeighted[N, 0])\n    write(T.diameter())\n\
    \n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\
    \n             https://kobejean.github.io/cp-library               \n'''\n\nfrom\
    \ typing import Iterable, Type, Union, overload\nimport typing\nfrom collections\
    \ import deque\nfrom numbers import Number\nfrom types import GenericAlias \n\
    from typing import Callable, Collection, Iterator, Union\nimport os\nimport sys\n\
    from io import BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n    BUFSIZE = 8192\n\
    \    newlines = 0\n\n    def __init__(self, file):\n        self._fd = file.fileno()\n\
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
    \ char else TokenStream.default)\n\ndef write(*args, **kwargs):\n    '''Prints\
    \ the values to a stream, or to stdout_fast by default.'''\n    sep, file = kwargs.pop(\"\
    sep\", \" \"), kwargs.pop(\"file\", IOWrapper.stdout)\n    at_start = True\n \
    \   for x in args:\n        if not at_start:\n            file.write(sep)\n  \
    \      file.write(str(x))\n        at_start = False\n    file.write(kwargs.pop(\"\
    end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n        file.flush()\n\
    \n\n\n\nclass Edge(tuple, Parsable):\n    @classmethod\n    def compile(cls, I=-1):\n\
    \        def parse(ts: TokenStream):\n            u,v = ts.line()\n          \
    \  return cls((int(u)+I,int(v)+I))\n        return parse\n\nfrom functools import\
    \ total_ordering \n\n@total_ordering\nclass EdgeWeighted(Edge):\n    def __lt__(self,\
    \ other: tuple) -> bool:\n        a = self[2],self[0],self[1]\n        b = other[2],other[0],other[1]\n\
    \        return a < b\n    \n    @classmethod\n    def compile(cls, I=-1):\n \
    \       def parse(ts: TokenStream):\n            u,v,w = ts.line()\n         \
    \   return cls((int(u)+I, int(v)+I, int(w)))\n        return parse\n\n\n\n\ndef\
    \ heappush(heap: list, item):\n    heap.append(item)\n    heapsiftdown(heap, 0,\
    \ len(heap)-1)\n\ndef heappop(heap: list):\n    item = heap.pop()\n    if heap:\
    \ item, heap[0] = heap[0], item; heapsiftup(heap, 0)\n    return item\n\ndef heapreplace(heap:\
    \ list, item):\n    item, heap[0] = heap[0], item; heapsiftup(heap, 0)\n    return\
    \ item\n\ndef heappushpop(heap: list, item):\n    if heap and heap[0] < item:\
    \ item, heap[0] = heap[0], item; heapsiftup(heap, 0)\n    return item\n\ndef heapify(x:\
    \ list):\n    for i in reversed(range(len(x)//2)): heapsiftup(x, i)\n\ndef heapsiftdown(heap:\
    \ list, root: int, pos: int):\n    item = heap[pos]\n    while root < pos and\
    \ item < heap[p := (pos-1)>>1]: heap[pos], pos = heap[p], p\n    heap[pos] = item\n\
    \ndef heapsiftup(heap: list, pos: int):\n    n, item, c = len(heap)-1, heap[pos],\
    \ pos<<1|1\n    while c < n and heap[c := c+(heap[c+1]<heap[c])] < item: heap[pos],\
    \ pos, c = heap[c], c, c<<1|1\n    if c == n and heap[c] < item: heap[pos], pos\
    \ = heap[c], c\n    heap[pos] = item\n\ndef heappop_max(heap: list):\n    item\
    \ = heap.pop()\n    if heap: item, heap[0] = heap[0], item; heapsiftup_max(heap,\
    \ 0)\n    return item\n\ndef heapreplace_max(heap: list, item):\n    item, heap[0]\
    \ = heap[0], item; heapsiftup_max(heap, 0)\n    return item\n\ndef heapify_max(x:\
    \ list):\n    for i in reversed(range(len(x)//2)): heapsiftup_max(x, i)\n\ndef\
    \ heappush_max(heap: list, item):\n    heap.append(item); heapsiftdown_max(heap,\
    \ 0, len(heap)-1)\n\ndef heapreplace_max(heap: list, item):\n    item, heap[0]\
    \ = heap[0], item; heapsiftup_max(heap, 0)\n    return item\n\ndef heappushpop_max(heap:\
    \ list, item):\n    if heap and heap[0] > item: item, heap[0] = heap[0], item;\
    \ heapsiftup_max(heap, 0)\n    return item\n\ndef heapsiftdown_max(heap: list,\
    \ root: int, pos: int):\n    item = heap[pos]\n    while root < pos and heap[p\
    \ := (pos-1)>>1] < item: heap[pos], pos = heap[p], p\n    heap[pos] = item\n\n\
    def heapsiftup_max(heap: list, pos: int):\n    n, item, c = len(heap)-1, heap[pos],\
    \ pos<<1|1\n    while c < n and item < heap[c := c+(heap[c]<heap[c+1])]: heap[pos],\
    \ pos, c = heap[c], c, c<<1|1\n    if c == n and item < heap[c]: heap[pos], pos\
    \ = heap[c], c\n    heap[pos] = item\n\n# def heapsiftdown(heap: list, root: int,\
    \ pos: int):\n#     item = heap[pos]\n#     while root < pos and item < heap[p\
    \ := (pos-1)>>1]: heap[pos], pos = heap[p], p\n#     heap[pos] = item\n\n# def\
    \ heapsiftup(heap: list, pos: int):\n#     n, item, c = len(heap)-1, heap[pos],\
    \ pos<<1|1\n#     while c < n and heap[c := c+(heap[c+1]<heap[c])] < item: heap[pos],\
    \ pos, c = heap[c], c, c<<1|1\n#     if c == n and heap[c] < item: heap[pos],\
    \ pos = heap[c], c\n#     heap[pos] = item\nimport operator\n\n\nfrom enum import\
    \ auto, IntFlag, IntEnum\n\nclass DFSFlags(IntFlag):\n    ENTER = auto()\n   \
    \ DOWN = auto()\n    BACK = auto()\n    CROSS = auto()\n    LEAVE = auto()\n \
    \   UP = auto()\n    MAXDEPTH = auto()\n\n    RETURN_PARENTS = auto()\n    RETURN_DEPTHS\
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
    \        return bridges\n\n    def articulation_points(G):\n        '''\n    \
    \    Find articulation points in an undirected graph using DFS events.\n     \
    \   Returns a boolean list that is True for indices where the vertex is an articulation\
    \ point.\n        '''\n        N = G.N\n        order = [-1] * N\n        low\
    \ = [-1] * N\n        par = [-1] * N\n        state = [0] * N\n        children\
    \ = [0] * N\n        ap = [False] * N\n        time = 0\n        stack = list(range(N))\n\
    \n        while stack:\n            v = stack.pop()\n            p = par[v]\n\
    \            if state[v] == 0:\n                state[v] = 1\n               \
    \ order[v] = low[v] = time\n                time += 1\n            \n        \
    \        stack.append(v)\n                for child in G[v]:\n               \
    \     if order[child] == -1:\n                        par[child] = v\n       \
    \                 stack.append(child)\n                    elif child != p:\n\
    \                        low[v] = min(low[v], order[child])\n                if\
    \ p != -1:\n                    children[p] += 1\n            elif state[v] ==\
    \ 1:\n                state[v] = 2\n                ap[v] |= p == -1 and children[v]\
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
    \ _ in range(M)])\n        return parse\n    \n\nclass GraphWeightedProtocol(GraphProtocol):\n\
    \n    def neighbors(G, v: int):\n        return map(operator.itemgetter(0), G[v])\n\
    \    \n    @overload\n    def distance(G) -> list[list[int]]: ...\n    @overload\n\
    \    def distance(G, s: int = 0) -> list[int]: ...\n    @overload\n    def distance(G,\
    \ s: int, g: int) -> int: ...\n    def distance(G, s = None, g = None):\n    \
    \    if s == None:\n            return G.floyd_warshall()\n        else:\n   \
    \         return G.dijkstra(s, g)\n    \n    def dijkstra(G, s = 0, g = None):\n\
    \        D = [inf for _ in range(G.N)]\n        D[s] = 0\n        que = PriorityQueue(G.N)\n\
    \        que.push(s, 0)\n        while que:\n            v, d = que.pop()\n  \
    \          if v == g: return d\n            if d > D[v]: continue\n          \
    \  for c, w, *_ in G[v]:\n                if (nd := d + w) < D[c]:\n         \
    \           D[c] = nd\n                    que.push(c, nd)\n        return D if\
    \ g is None else inf\n    \n    @overload\n    def shortest_path(G, s: int, t:\
    \ int) -> list[int]|None: ...\n    @overload\n    def shortest_path(G, s: int,\
    \ t: int, distances = True) -> tuple[list[int]|None,list[int]]: ...\n    def shortest_path(G,\
    \ s: int, t: int, distances = False):\n        D = [inf] * G.N\n        D[s] =\
    \ 0\n        if s == t:\n            return ([], D) if distances else []\n   \
    \         \n        par = [-1] * G.N\n        down = [-1] * G.N\n        Eid =\
    \ G.edge_ids()\n        que = PriorityQueue(G.N)\n        que.push(s, 0)\n   \
    \     \n        while que:\n            v, d = que.pop()\n            if v ==\
    \ t: break\n            if d > D[v]: continue\n                \n            for\
    \ i in range(len(G[v])):\n                c, w, *_ = G[v][i]\n               \
    \ if (nd := d + w) < D[c]:\n                    D[c] = nd\n                  \
    \  par[c] = v\n                    down[c] = Eid[v][i]\n                    que.push(c,\
    \ nd)\n        \n        if D[t] == inf:\n            return (None, D) if distances\
    \ else None\n            \n        path = []\n        v = t\n        while v !=\
    \ s:\n            path.append(down[v])\n            v = par[v]\n            \n\
    \        return (path[::-1], D) if distances else path[::-1]\n    \n    def kruskal(G):\n\
    \        E, N = G.E, G.N\n        heapify(E)\n        dsu = DSU(N)\n        MST\
    \ = []\n        need = N-1\n        while E and need:\n            edge = heappop(E)\n\
    \            u,v,*_ = edge\n            u,v = dsu.merge(u,v,True)\n          \
    \  if u != v:\n                MST.append(edge)\n                need -= 1\n \
    \       return MST\n    \n    def bellman_ford(G, s = 0) -> list[int]:\n     \
    \   D = [inf]*G.N\n        D[s] = 0\n        for _ in range(G.N-1):\n        \
    \    for u, edges in enumerate(G):\n                if D[u] == inf: continue\n\
    \                for v,w,*_ in edges:\n                    D[v] = min(D[v], D[u]\
    \ + w)\n        return D\n    \n    def floyd_warshall(G) -> list[list[int]]:\n\
    \        D = [[inf]*G.N for _ in range(G.N)]\n\n        for u, edges in enumerate(G):\n\
    \            D[u][u] = 0\n            for v,w in edges:\n                D[u][v]\
    \ = min(D[u][v], w)\n        \n        for k, Dk in enumerate(D):\n          \
    \  for Di in D:\n                if Di[k] == inf: continue\n                for\
    \ j in range(G.N):\n                    if Dk[j] == inf: continue\n          \
    \          Di[j] = min(Di[j], Di[k]+Dk[j])\n        return D\n    \n    def dfs_events(G,\
    \ flags: DFSFlags, s: Union[int,list,None] = None, max_depth: Union[int,None]\
    \ = None):\n        if flags == DFSFlags.INTERVAL:\n            if max_depth is\
    \ None:\n                return G.dfs_enter_leave(s)\n        elif flags == DFSFlags.DOWN\
    \ or flags == DFSFlags.TOPDOWN:\n            if max_depth is None:\n         \
    \       edges = G.dfs_topdown(s, DFSFlags.CONNECT_ROOTS in flags)\n          \
    \      return [(DFSEvent.DOWN, p, u) for p,u in edges]\n        elif flags ==\
    \ DFSFlags.UP or flags == DFSFlags.BOTTOMUP:\n            if max_depth is None:\n\
    \                edges = G.dfs_bottomup(s, DFSFlags.CONNECT_ROOTS in flags)\n\
    \                return [(DFSEvent.UP, p, u) for p,u in edges]\n        elif flags\
    \ & DFSFlags.BACKTRACK:\n            return G.dfs_backtrack(flags, s, max_depth)\n\
    \        state = [0] * G.N\n        child = elist(G.N)\n        weights = elist(G.N)\n\
    \        stack = elist(G.N)\n        if flags & DFSFlags.RETURN_PARENTS:\n   \
    \         parents = [-1] * G.N\n        if flags & DFSFlags.RETURN_DEPTHS:\n \
    \           depths = [-1] * G.N\n\n        events = []\n        for s in G.starts(s):\n\
    \            stack.append(s)\n            child.append(0)\n            if (DFSFlags.DOWN|DFSFlags.CONNECT_ROOTS)\
    \ in flags:\n                events.append((DFSEvent.DOWN,-1,s,-1))\n        \
    \    while stack:\n                u = stack[-1]\n                \n         \
    \       if not state[u]:\n                    state[u] = 1\n                 \
    \   if flags & DFSFlags.ENTER:\n                        events.append((DFSEvent.ENTER,\
    \ u))\n                    if flags & DFSFlags.RETURN_DEPTHS:\n              \
    \          depths[u] = len(stack)-1\n                \n                if (c :=\
    \ child[-1]) < len(G[u]):\n                    child[-1] += 1\n              \
    \      v, w = G[u][c]\n                    if (s := state[v]) == 0:  # Unvisited\n\
    \                        if max_depth is None or len(stack)-1 <= max_depth:\n\
    \                            if flags & DFSFlags.DOWN:\n                     \
    \           events.append((DFSEvent.DOWN, u, v, w))\n                        \
    \    stack.append(v)\n                            weights.append(w)\n        \
    \                    child.append(0)\n                            if flags & DFSFlags.RETURN_PARENTS:\n\
    \                                parents[v] = u\n                    elif s ==\
    \ 1:  # In progress\n                        if flags & DFSFlags.BACK:\n     \
    \                       events.append((DFSEvent.BACK, u, v, w))\n            \
    \        elif s == 2:  # Completed\n                        if flags & DFSFlags.CROSS:\n\
    \                            events.append((DFSEvent.CROSS, u, v, w))\n      \
    \          else:\n                    stack.pop()\n                    child.pop()\n\
    \                    state[u] = 0 if DFSFlags.BACKTRACK in flags else 2\n    \
    \                if flags & DFSFlags.LEAVE:\n                        events.append((DFSEvent.LEAVE,\
    \ u))\n                    if stack and flags & DFSFlags.UP:\n               \
    \         pw = weights.pop()\n                        events.append((DFSEvent.UP,\
    \ stack[-1], u, pw))\n            if (DFSFlags.UP|DFSFlags.CONNECT_ROOTS) in flags:\n\
    \                events.append((DFSEvent.UP,-1,s,-1))\n        ret = tuple((events,))\
    \ if DFSFlags.RETURN_ALL & flags else events\n        if DFSFlags.RETURN_PARENTS\
    \ in flags:\n            ret += (parents,)\n        if DFSFlags.RETURN_DEPTHS\
    \ in flags:\n            ret += (depths,)\n        return ret\n\n    def dfs_backtrack(G,\
    \ flags: DFSFlags, s: Union[int,list] = None, max_depth: Union[int,None] = None):\n\
    \        stack_depth = (max_depth+1 if max_depth is not None else G.N)\n     \
    \   stack = elist(stack_depth)\n        child = elist(stack_depth)\n        weights\
    \ = elist(stack_depth)\n        state = [0]*G.N\n        events: list[tuple[DFSEvent,\
    \ int]|tuple[DFSEvent, int, int]] = []\n\n        for s in G.starts(s):\n    \
    \        if state[s]: continue\n            state[s] = 1\n            stack.append(s)\n\
    \            child.append(0)\n            if DFSFlags.DOWN|DFSFlags.CONNECT_ROOTS\
    \ in flags:\n                events.append((DFSEvent.DOWN,-1,s,-1))\n        \
    \    while stack:\n                u = stack[-1]\n                if state[u]\
    \ == 1:\n                    state[u] = 2\n                    if DFSFlags.ENTER\
    \ in flags:\n                        events.append((DFSEvent.ENTER,u))\n     \
    \               if max_depth is not None and len(stack) > max_depth:\n       \
    \                 child[-1] = len(G[u])\n                        if DFSFlags.MAXDEPTH\
    \ in flags:\n                            events.append((DFSEvent.MAXDEPTH,u))\n\
    \n                if (c := child[-1]) < len(G[u]):\n                    child[-1]\
    \ += 1\n                    v, w = G[u][c]\n                    if state[v]:\n\
    \                        if DFSFlags.BACK in flags:\n                        \
    \    events.append((DFSEvent.BACK,u,v,w))\n                        continue\n\
    \                    state[v] = 1\n                    if DFSFlags.DOWN in flags:\n\
    \                        events.append((DFSEvent.DOWN,u,v,w))\n              \
    \      stack.append(v)\n                    child.append(0)\n                \
    \    weights.append(w)\n                else:\n                    state[u] =\
    \ 0\n                    if DFSFlags.LEAVE in flags:\n                       \
    \ events.append((DFSEvent.LEAVE,u))\n                    stack.pop()\n       \
    \             child.pop()\n                    if stack and DFSFlags.UP in flags:\n\
    \                        pw = weights.pop()\n                        events.append((DFSEvent.UP,\
    \ stack[-1], u, pw))\n                    \n            if DFSFlags.UP|DFSFlags.CONNECT_ROOTS\
    \ in flags:\n                events.append((DFSEvent.UP,-1,s,-1))\n        return\
    \ events\n    \n    def dfs_topdown(G, s: Union[int,list[int],None] = None, connect_roots\
    \ = False):\n        '''Returns list of (u,v) representing u->v edges in order\
    \ of top down discovery'''\n        stack: list[int] = elist(G.N)\n        vis\
    \ = [False]*G.N\n        edges: list[tuple[int,int]] = elist(G.N)\n\n        for\
    \ s in G.starts(s):\n            if vis[s]: continue\n            if connect_roots:\n\
    \                edges.append((-1,s,-1))\n            vis[s] = True\n        \
    \    stack.append(s)\n            while stack:\n                u = stack.pop()\n\
    \                for v,w in G[u]:\n                    if vis[v]: continue\n \
    \                   vis[v] = True\n                    edges.append((u,v,w))\n\
    \                    stack.append(v)\n        return edges\n\nfrom typing import\
    \ Sequence\n\n\nclass CSRIncremental(Sequence[list[_T]]):\n    def __init__(csr,\
    \ sizes: list[int]):\n        csr.L, N = [0]*len(sizes), 0\n        for i,sz in\
    \ enumerate(sizes):\n            csr.L[i] = N; N += sz\n        csr.R, csr.A =\
    \ csr.L[:], [0]*N\n\n    def append(csr, i: int, x: _T):\n        csr.A[csr.R[i]]\
    \ = x; csr.R[i] += 1\n    \n    def __iter__(csr):\n        for i,l in enumerate(csr.L):\n\
    \            yield csr.A[l:csr.R[i]]\n    \n    def __getitem__(csr, i: int) ->\
    \ _T:\n        return csr.A[i]\n    \n    def __len__(dsu):\n        return len(dsu.L)\n\
    \n    def range(csr, i: int) -> _T:\n        return range(csr.L[i], csr.R[i])\n\
    \nclass DSU(Parsable, Collection):\n    def __init__(dsu, N):\n        dsu.N,\
    \ dsu.cc, dsu.par = N, N, [-1]*N\n\n    def merge(dsu, u, v, src = False):\n \
    \       x, y = dsu.leader(u), dsu.leader(v)\n        if x == y: return (x,y) if\
    \ src else x\n        if dsu.par[x] > dsu.par[y]: x, y = y, x\n        dsu.par[x]\
    \ += dsu.par[y]; dsu.par[y] = x; dsu.cc -= 1\n        return (x,y) if src else\
    \ x\n\n    def same(dsu, u: int, v: int):\n        return dsu.leader(u) == dsu.leader(v)\n\
    \n    def leader(dsu, i) -> int:\n        p = (par := dsu.par)[i]\n        while\
    \ p >= 0:\n            if par[p] < 0: return p\n            par[i], i, p = par[p],\
    \ par[p], par[par[p]]\n        return i\n\n    def size(dsu, i) -> int:\n    \
    \    return -dsu.par[dsu.leader(i)]\n\n    def groups(dsu) -> CSRIncremental[int]:\n\
    \        sizes, row, p = [0]*dsu.cc, [-1]*dsu.N, 0\n        for i in range(dsu.cc):\n\
    \            while dsu.par[p] >= 0: p += 1\n            sizes[i], row[p] = -dsu.par[p],\
    \ i; p += 1\n        csr = CSRIncremental(sizes)\n        for i in range(dsu.N):\
    \ csr.append(row[dsu.leader(i)], i)\n        return csr\n    \n    __iter__ =\
    \ groups\n    \n    def __len__(dsu):\n        return dsu.cc\n    \n    def __contains__(dsu,\
    \ uv):\n        u, v = uv\n        return dsu.same(u, v)\n    \n    @classmethod\n\
    \    def compile(cls, N: int, M: int, shift = -1):\n        def parse_fn(ts: TokenStream):\n\
    \            dsu = cls(N)\n            for _ in range(M):\n                u,\
    \ v = ts._line()\n                dsu.merge(int(u)+shift, int(v)+shift)\n    \
    \        return dsu\n        return parse_fn\n\nfrom collections import UserList\n\
    from typing import Generic\n\nclass HeapProtocol(Generic[_T]):\n    def pop(self)\
    \ -> _T: ...\n    def push(self, item: _T): ...\n    def pushpop(self, item: _T)\
    \ -> _T: ...\n    def replace(self, item: _T) -> _T: ...\n\nclass PriorityQueue(HeapProtocol[int],\
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
    \ self.encode(id, priority)))\n    \n\nclass GraphWeighted(GraphWeightedProtocol):\n\
    \    def __init__(G, N: int, E=[]):\n        super().__init__(N, E, ([] for _\
    \ in range(N)))\n        G.E = E\n        for u,v,*w in G.E:\n            G[u].append((v,*w))\n\
    \            G[v].append((u,*w))\n    \n    def edge_ids(G) -> list[list[int]]:\n\
    \        Eid = [[] for _ in range(G.N)]\n        for e,(u,v,*w) in enumerate(G.E):\n\
    \            Eid[u].append(e)\n            Eid[v].append(e)\n        return Eid\n\
    \    \n    @classmethod\n    def compile(cls, N: int, M: int, E: Union[type,int]\
    \ = EdgeWeighted[-1]):\n        if isinstance(E, int): E = EdgeWeighted[E]\n \
    \       return super().compile(N, M, E)\n\nfrom functools import cached_property\n\
    \nfrom typing import overload, Literal, Union\n\n\ndef sort2(a, b):\n    return\
    \ (a,b) if a < b else (b,a)\n\nfrom itertools import accumulate\n\ndef presum(iter:\
    \ Iterable[_T], func: Callable[[_T,_T],_T] = None, initial: _T = None, step =\
    \ 1) -> list[_T]:\n    if step == 1:\n        return list(accumulate(iter, func,\
    \ initial=initial))\n    else:\n        assert step >= 2\n        if func is None:\n\
    \            func = operator.add\n        A = list(iter)\n        if initial is\
    \ not None:\n            A = [initial] + A\n        for i in range(step,len(A)):\n\
    \            A[i] = func(A[i], A[i-step])\n        return A\n# from typing import\
    \ Generic\n# from cp_library.misc.typing import _T\n\ndef min2(a, b):\n    return\
    \ a if a < b else b\n\n\nclass MinSparseTable:\n    def __init__(st, arr: list):\n\
    \        st.N = N = len(arr)\n        st.log = N.bit_length()\n        st.data\
    \ = data = [0] * (st.log*N)\n        data[:N] = arr \n        for i in range(1,st.log):\n\
    \            a, b, c = i*N, (i-1)*N, (i-1)*N + (1 << (i-1))\n            for j\
    \ in range(N - (1 << i) + 1):\n                data[a+j] = min2(data[b+j], data[c+j])\n\
    \n    def query(st, l: int, r: int):\n        k = (r-l).bit_length() - 1\n   \
    \     return min2(st.data[k*st.N + l], st.data[k*st.N + r - (1<<k)])\n    \n\n\
    class LCATable(MinSparseTable):\n    def __init__(lca, T, root = 0):\n       \
    \ N = len(T)\n        T.euler_tour(root)\n        lca.depth = depth = presum(T.delta)\n\
    \        lca.tin, lca.tout = T.tin[:], T.tout[:]\n        lca.mask = (1 << (shift\
    \ := N.bit_length()))-1\n        lca.shift = shift\n        order = T.order\n\
    \        M = len(order)\n        packets = [0]*M\n        for i in range(M):\n\
    \            packets[i] = depth[i] << shift | order[i] \n        super().__init__(packets)\n\
    \n    def _query(lca, u, v):\n        l, r = sort2(lca.tin[u], lca.tin[v]); r\
    \ += 1\n        da = super().query(l, r)\n        return l, r, da & lca.mask,\
    \ da >> lca.shift\n\n    def query(lca, u, v) -> tuple[int,int]:\n        l, r,\
    \ a, d = lca._query(u, v)\n        return a, d\n    \n    def distance(lca, u,\
    \ v) -> int:\n        l, r, a, d = lca._query(u, v)\n        return lca.depth[l]\
    \ + lca.depth[r-1] - 2*d\n    \n    def path(lca, u, v):\n        path, par, lca,\
    \ c = [], lca.T.par, lca.query(u, v)[0], u\n        while c != lca:\n        \
    \    path.append(c)\n            c = par[c]\n        path.append(lca)\n      \
    \  rev_path, c = [], v\n        while c != lca:\n            rev_path.append(c)\n\
    \            c = par[c]\n        path.extend(reversed(rev_path))\n        return\
    \ path\n\nclass TreeProtocol(GraphProtocol):\n\n    @cached_property\n    def\
    \ lca(T):\n        return LCATable(T)\n    \n    @overload\n    def diameter(T)\
    \ -> int: ...\n    @overload\n    def diameter(T, endpoints: Literal[True]) ->\
    \ tuple[int,int,int]: ...\n    def diameter(T, endpoints = False):\n        mask\
    \ = (1 << (shift := T.N.bit_length())) - 1\n        s = max(d << shift | v for\
    \ v,d in enumerate(T.distance(0))) & mask\n        dg = max(d << shift | v for\
    \ v,d in enumerate(T.distance(s))) \n        diam, g = dg >> shift, dg & mask\n\
    \        return (diam, s, g) if endpoints else diam\n    \n    @overload\n   \
    \ def distance(T) -> list[list[int]]: ...\n    @overload\n    def distance(T,\
    \ s: int = 0) -> list[int]: ...\n    @overload\n    def distance(T, s: int, g:\
    \ int) -> int: ...\n    def distance(T, s = None, g = None):\n        if s ==\
    \ None:\n            return [T.dfs(u) for u in range(T.N)]\n        else:\n  \
    \          return T.dfs(s, g)\n            \n    @overload\n    def dfs(T, s:\
    \ int = 0) -> list[int]: ...\n    @overload\n    def dfs(T, s: int, g: int) ->\
    \ int: ...\n    def dfs(T, s = 0, g = None):\n        D = [inf for _ in range(T.N)]\n\
    \        D[s] = 0\n        state = [True for _ in range(T.N)]\n        stack =\
    \ [s]\n\n        while stack:\n            u = stack.pop()\n            if u ==\
    \ g: return D[u]\n            state[u] = False\n            for v in T[u]:\n \
    \               if state[v]:\n                    D[v] = D[u]+1\n            \
    \        stack.append(v)\n        return D if g is None else inf \n\n\n    def\
    \ dfs_events(G, flags: DFSFlags, s: int = 0):         \n        events = []\n\
    \        stack = [(s,-1)]\n        adj = [None]*G.N\n\n\n        while stack:\n\
    \            u, p = stack[-1]\n            \n            if adj[u] is None:\n\
    \                adj[u] = iter(G.neighbors(u))\n                if DFSFlags.ENTER\
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
    \ tin, tout\n        T.par, T.heavy, T.head = par, heavy, head\n\nclass LCATableWeighted(LCATable):\n\
    \    def __init__(lca, T, root = 0):\n        super().__init__(T, root)\n    \
    \    lca.weights = T.Wdelta\n        lca.weighted_depth = None\n\n    def distance(lca,\
    \ u, v) -> int:\n        if lca.weighted_depth is None:\n            lca.weighted_depth\
    \ = presum(lca.weights)\n        l, r, a, _ = lca._query(u, v)\n        m = lca.tin[a]\n\
    \        return lca.weighted_depth[l] + lca.weighted_depth[r-1] - 2*lca.weighted_depth[m]\n\
    \nclass TreeWeightedProtocol(GraphWeightedProtocol, TreeProtocol):\n\n    @cached_property\n\
    \    def lca(T):\n        return LCATableWeighted(T)\n    \n    @overload\n  \
    \  def dfs(T, s: int = 0) -> list[int]: ...\n    @overload\n    def dfs(T, s:\
    \ int, g: int) -> int: ...\n    def dfs(T, s = 0, g = None):\n        D = [inf\
    \ for _ in range(T.N)]\n        D[s] = 0\n        state = [True for _ in range(T.N)]\n\
    \        stack = [s]\n\n        while stack:\n            u = stack.pop()\n  \
    \          if u == g: return D[u]\n            state[u] = False\n            for\
    \ v, w, *_ in T[u]:\n                if state[v]:\n                    D[v] =\
    \ D[u]+w\n                    stack.append(v)\n        return D if g is None else\
    \ inf\n    \n    def euler_tour(T, s = 0):\n        N = len(T)\n        T.tin\
    \ = tin = [-1] * N\n        T.tout = tout = [-1] * N\n        T.par = par = [-1]\
    \ * N\n        T.order = order = elist(2*N)\n        T.delta = delta = elist(2*N)\n\
    \        T.Wdelta = Wdelta = elist(2*N)\n        stack = elist(N)\n        Wstack\
    \ = elist(N)\n        stack.append(s)\n        Wstack.append(0)\n\n        while\
    \ stack:\n            u = stack.pop()\n            wd = Wstack.pop()\n       \
    \     p = par[u]\n            \n            if tin[u] == -1:\n               \
    \ tin[u] = len(order)\n                \n                for v,w,*_ in T[u]:\n\
    \                    if v != p:\n                        par[v] = u\n        \
    \                stack.append(u)\n                        stack.append(v)\n  \
    \                      Wstack.append(-w)\n                        Wstack.append(w)\n\
    \                delta.append(1)\n            else:\n                delta.append(-1)\n\
    \            \n            Wdelta.append(wd)\n            order.append(u)\n  \
    \          tout[u] = len(order)\n        delta[0] = delta[-1] = 0\n\n    def hld_precomp(T,\
    \ r = 0):\n        N, time = T.N, 0\n        tin, tout, size = [0]*N, [0]*N, [1]*N+[0]\n\
    \        par, heavy, head = [-1]*N, [-1]*N, [r]*N\n        depth, order, state\
    \ = [0]*N, [0]*N, [0]*N\n        Wpar = [0]*N\n        stack = elist(N)\n    \
    \    stack.append(r)\n        while stack:\n            if (s := state[v := stack.pop()])\
    \ == 0: # dfs down\n                p, state[v] = par[v], 1\n                stack.append(v)\n\
    \                for c, w, *_ in T[v]:\n                    if c != p:\n     \
    \                   depth[c], par[c], Wpar[c] = depth[v]+1, v, w\n           \
    \             stack.append(c)\n\n            elif s == 1: # dfs up\n         \
    \       p, l = par[v], -1\n                for c, w, *_ in T[v]:\n           \
    \         if c != p:\n                        size[v] += size[c]\n           \
    \             if size[c] > size[l]:\n                            l = c\n     \
    \           heavy[v] = l\n                if p == -1:\n                    state[v]\
    \ = 2\n                    stack.append(v)\n\n            elif s == 2: # decompose\
    \ down\n                p, h, l = par[v], head[v], heavy[v]\n                tin[v],\
    \ order[time], state[v] = time, v, 3\n                time += 1\n            \
    \    stack.append(v)\n                \n                for c, *_ in T[v]:\n \
    \                   if c != p and c != l:\n                        head[c], state[c]\
    \ = c, 2\n                        stack.append(c)\n\n                if l != -1:\n\
    \                    head[l], state[l] = h, 2\n                    stack.append(l)\n\
    \n            elif s == 3: # decompose up\n                tout[v] = time\n  \
    \      T.size, T.depth = size, depth\n        T.order, T.tin, T.tout = order,\
    \ tin, tout\n        T.par, T.heavy, T.head = par, heavy, head\n        T.Wpar\
    \ = Wpar\n\n\nclass TreeWeighted(TreeWeightedProtocol, GraphWeighted):\n    @classmethod\n\
    \    def compile(cls, N: int, E: Union[type,int] = EdgeWeighted[-1]):\n      \
    \  return GraphWeighted.compile.__func__(cls, N, N-1, E)\n\nif __name__ == '__main__':\n\
    \    main()\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_5_A\n\
    \ndef main():\n    N = read(int)\n    T = read(TreeWeighted[N, 0])\n    write(T.diameter())\n\
    \nfrom cp_library.io.read_fn import read\nfrom cp_library.io.write_fn import write\n\
    from cp_library.alg.tree.tree_weighted_cls import TreeWeighted\n\nif __name__\
    \ == '__main__':\n    main()"
  dependsOn:
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/alg/tree/tree_weighted_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  - cp_library/alg/graph/edge_weighted_cls.py
  - cp_library/alg/graph/graph_weighted_cls.py
  - cp_library/alg/tree/tree_weighted_proto.py
  - cp_library/alg/graph/graph_weighted_proto.py
  - cp_library/alg/tree/tree_proto.py
  - cp_library/alg/tree/lca_table_weighted_iterative_cls.py
  - cp_library/ds/elist_fn.py
  - cp_library/alg/graph/edge_cls.py
  - cp_library/ds/heap/fast_heapq.py
  - cp_library/alg/graph/dfs_options_cls.py
  - cp_library/alg/graph/graph_proto.py
  - cp_library/ds/dsu_cls.py
  - cp_library/ds/heap/priority_queue_cls.py
  - cp_library/alg/tree/lca_table_iterative_cls.py
  - cp_library/alg/iter/presum_fn.py
  - cp_library/ds/csr/csr_incremental_cls.py
  - cp_library/ds/heap/heap_proto.py
  - cp_library/alg/dp/sort2_fn.py
  - cp_library/ds/min_sparse_table_cls.py
  - cp_library/alg/dp/min2_fn.py
  isVerificationFile: true
  path: test/aoj/grl/grl_5_a_diameter.test.py
  requiredBy: []
  timestamp: '2025-04-28 05:45:14+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl/grl_5_a_diameter.test.py
layout: document
redirect_from:
- /verify/test/aoj/grl/grl_5_a_diameter.test.py
- /verify/test/aoj/grl/grl_5_a_diameter.test.py.html
title: test/aoj/grl/grl_5_a_diameter.test.py
---
