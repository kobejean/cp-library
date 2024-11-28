---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  - icon: ':question:'
    path: cp_library/ds/heap_proto.py
    title: cp_library/ds/heap_proto.py
  - icon: ':question:'
    path: cp_library/ds/priority_queue_cls.py
    title: cp_library/ds/priority_queue_cls.py
  - icon: ':question:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':question:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':question:'
    path: cp_library/math/inft_cnst.py
    title: cp_library/math/inft_cnst.py
  _extendedRequiredBy: []
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
    \nfrom typing import Sequence\nimport sys\n\n\nimport typing\nfrom collections\
    \ import deque\nfrom numbers import Number\nfrom types import GenericAlias \n\
    from typing import Callable, Collection, Iterator, TypeVar, Union\nimport os\n\
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
    \ TokenStream):\n            return cls(next(ts))\n        return parser\n\nclass\
    \ StaticDiGraphWeighted(Sequence, Parsable):\n    def __init__(G, N: int, U: list,\
    \ V: list, W: list):\n        M = len(U)\n        deg, adj, Wadj = [0]*N, [0]*M,\
    \ [0]*M\n\n        for u in U:\n            deg[u] += 1\n\n        L, idx = [0]*N,\
    \ 0\n        for u in range(N):\n            L[u], idx = idx, idx + deg[u]\n \
    \       R = L[:]\n\n        for eid in range(M):\n            u, v, w = U[eid],\
    \ V[eid], W[eid]\n            adj[r], Wadj[r], R[u] = v, w, (r := R[u])+1\n  \
    \      G.N, G.M, G.adj, G.Wadj, G.deg = N, M, adj, Wadj, deg\n        G.L, G.R\
    \ = L, R \n\n    def __len__(G) -> int:\n        return G.N\n    \n    def __getitem__(G,\
    \ v):\n        l,r = G.L[v],G.R[v]\n        return zip(G.adj[l:r], G.Wadj[l:r])\n\
    \n    def dijkstra(G, s: int, t: int):\n        N, adj, Wadj = G.N, G.adj, G.Wadj\n\
    \        L, R = G.L, G.R\n        G.par = par = [-1] * N\n        G.D = D = [inft]\
    \ * N\n        D[s] = 0\n        \n        que = PriorityQueue(N)\n        que.push(s,\
    \ 0)\n\n        def expand(i,d):\n            for i in range(L[v],R[v]):\n   \
    \             c, w = adj[i], Wadj[i]\n                if (nd := d + w) < D[c]:\n\
    \                    D[c], par[c] = nd, v\n                    que.push(c, nd)\n\
    \        \n        while que:\n            v, d = que.pop()\n            if v\
    \ == t: break\n            if d > D[v]: continue\n            expand(v,d)\n  \
    \      return D\n        \n    def shortest_path(G, s: int, t: int):\n       \
    \ D = G.dijkstra(s, t)\n        if D[t] == inft: return None\n        par = G.par\n\
    \            \n        path = elist(G.N)\n        path.append(t)\n        v =\
    \ t\n        while v != s:\n            path.append(v := par[v])\n        return\
    \ path[::-1]\n    \n    def shortest_path_edge_ids(G, s: int, t: int):\n     \
    \   D = G.dijkstra(s, t)\n        if D[t] == inft: return None\n        par, par_ei\
    \ = G.par, G.par_ei\n            \n        path = elist(G.N)\n        v = t\n\
    \        while v != s:\n            path.append(par_ei[v])\n            v = par[v]\
    \ \n        return path[::-1]\n    \n    @classmethod\n    def compile(cls, N:\
    \ int, M: int, shift: int = -1):\n        def parse(ts: TokenStream):\n      \
    \      U, V, W = [0]*M, [0]*M, [0]*M\n            for i in range(M):\n       \
    \         U[i], V[i], W[i] = map(int, ts.line())\n                U[i] += shift\n\
    \                V[i] += shift\n            return cls(N, U, V, W)\n        return\
    \ parse\n    \n\n\ndef elist(est_len: int) -> list: ...\ntry:\n    from __pypy__\
    \ import newlist_hint\nexcept:\n    def newlist_hint(hint):\n        return []\n\
    elist = newlist_hint\n    \n\nfrom typing import Iterable\nfrom collections import\
    \ UserList\nfrom heapq import heapify, heappop, heappush, heappushpop, heapreplace\n\
    from typing import Generic, TypeVar\n\nT = TypeVar('T')\nclass HeapProtocol(Generic[T]):\n\
    \    def pop(self) -> T: ...\n    def push(self, item: T): ...\n    def pushpop(self,\
    \ item: T) -> T: ...\n    def replace(self, item: T) -> T: ...\n\nclass PriorityQueue(HeapProtocol[int],\
    \ UserList[int]):\n    \n    def __init__(self, N: int, ids: Iterable[int] = None,\
    \ priorities: Iterable[int] = None, /):\n        self.shift = N.bit_length()\n\
    \        self.mask = (1 << self.shift)-1\n        if ids is None:\n          \
    \  super().__init__()\n        elif priorities is None:\n            self.data\
    \ = ids\n            heapify(self.data)\n        else:\n            self.data\
    \ = [self.encode(id, priority) for id, priority in zip(ids, priorities)]\n   \
    \         heapify(self.data)\n\n    def encode(self, id, priority):\n        return\
    \ priority << self.shift | id\n    \n    def decode(self, encoded):\n        return\
    \ self.mask & encoded, encoded >> self.shift\n    \n    def pop(self):\n     \
    \   return self.decode(heappop(self.data))\n    \n    def push(self, id: int,\
    \ priority: int):\n        heappush(self.data, self.encode(id, priority))\n\n\
    \    def pushpop(self, id: int, priority: int):\n        return self.decode(heappushpop(self.data,\
    \ self.encode(id, priority)))\n    \n    def replace(self, id: int, priority:\
    \ int):\n        return self.decode(heapreplace(self.data, self.encode(id, priority)))\n\
    \n\n\ninft = sys.maxsize\n"
  code: "import cp_library.alg.graph.fast.__header__\n\nfrom typing import Sequence\n\
    from cp_library.io.parser_cls import Parsable, TokenStream\n\nclass StaticDiGraphWeighted(Sequence,\
    \ Parsable):\n    def __init__(G, N: int, U: list, V: list, W: list):\n      \
    \  M = len(U)\n        deg, adj, Wadj = [0]*N, [0]*M, [0]*M\n\n        for u in\
    \ U:\n            deg[u] += 1\n\n        L, idx = [0]*N, 0\n        for u in range(N):\n\
    \            L[u], idx = idx, idx + deg[u]\n        R = L[:]\n\n        for eid\
    \ in range(M):\n            u, v, w = U[eid], V[eid], W[eid]\n            adj[r],\
    \ Wadj[r], R[u] = v, w, (r := R[u])+1\n        G.N, G.M, G.adj, G.Wadj, G.deg\
    \ = N, M, adj, Wadj, deg\n        G.L, G.R = L, R \n\n    def __len__(G) -> int:\n\
    \        return G.N\n    \n    def __getitem__(G, v):\n        l,r = G.L[v],G.R[v]\n\
    \        return zip(G.adj[l:r], G.Wadj[l:r])\n\n    def dijkstra(G, s: int, t:\
    \ int):\n        N, adj, Wadj = G.N, G.adj, G.Wadj\n        L, R = G.L, G.R\n\
    \        G.par = par = [-1] * N\n        G.D = D = [inft] * N\n        D[s] =\
    \ 0\n        \n        que = PriorityQueue(N)\n        que.push(s, 0)\n\n    \
    \    def expand(i,d):\n            for i in range(L[v],R[v]):\n              \
    \  c, w = adj[i], Wadj[i]\n                if (nd := d + w) < D[c]:\n        \
    \            D[c], par[c] = nd, v\n                    que.push(c, nd)\n     \
    \   \n        while que:\n            v, d = que.pop()\n            if v == t:\
    \ break\n            if d > D[v]: continue\n            expand(v,d)\n        return\
    \ D\n        \n    def shortest_path(G, s: int, t: int):\n        D = G.dijkstra(s,\
    \ t)\n        if D[t] == inft: return None\n        par = G.par\n            \n\
    \        path = elist(G.N)\n        path.append(t)\n        v = t\n        while\
    \ v != s:\n            path.append(v := par[v])\n        return path[::-1]\n \
    \   \n    def shortest_path_edge_ids(G, s: int, t: int):\n        D = G.dijkstra(s,\
    \ t)\n        if D[t] == inft: return None\n        par, par_ei = G.par, G.par_ei\n\
    \            \n        path = elist(G.N)\n        v = t\n        while v != s:\n\
    \            path.append(par_ei[v])\n            v = par[v] \n        return path[::-1]\n\
    \    \n    @classmethod\n    def compile(cls, N: int, M: int, shift: int = -1):\n\
    \        def parse(ts: TokenStream):\n            U, V, W = [0]*M, [0]*M, [0]*M\n\
    \            for i in range(M):\n                U[i], V[i], W[i] = map(int, ts.line())\n\
    \                U[i] += shift\n                V[i] += shift\n            return\
    \ cls(N, U, V, W)\n        return parse\n    \nfrom cp_library.ds.elist_fn import\
    \ elist\nfrom cp_library.ds.priority_queue_cls import PriorityQueue\nfrom cp_library.math.inft_cnst\
    \ import inft"
  dependsOn:
  - cp_library/io/parser_cls.py
  - cp_library/ds/elist_fn.py
  - cp_library/ds/priority_queue_cls.py
  - cp_library/math/inft_cnst.py
  - cp_library/io/fast_io_cls.py
  - cp_library/ds/heap_proto.py
  isVerificationFile: false
  path: cp_library/alg/graph/fast/static_graph_cls.py
  requiredBy: []
  timestamp: '2024-11-28 18:07:28+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/graph/fast/static_graph_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/fast/static_graph_cls.py
- /library/cp_library/alg/graph/fast/static_graph_cls.py.html
title: cp_library/alg/graph/fast/static_graph_cls.py
---
