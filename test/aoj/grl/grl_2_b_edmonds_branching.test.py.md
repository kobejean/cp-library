---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge_cls.py
    title: cp_library/alg/graph/edge_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge_list_cls.py
    title: cp_library/alg/graph/edge_list_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge_list_weighted_cls.py
    title: cp_library/alg/graph/edge_list_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge_weighted_cls.py
    title: cp_library/alg/graph/edge_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edmonds_fn.py
    title: cp_library/alg/graph/edmonds_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/floyds_cycle_fn.py
    title: cp_library/alg/graph/floyds_cycle_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/csr/csr_incremental_cls.py
    title: cp_library/ds/csr/csr_incremental_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/dsu_cls.py
    title: cp_library/ds/dsu_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/fast_heapq.py
    title: cp_library/ds/heap/fast_heapq.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_edges_weighted_fn.py
    title: cp_library/io/read_edges_weighted_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_fn.py
    title: cp_library/io/read_fn.py
  - icon: ':heavy_check_mark:'
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
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_B
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_B
  bundledCode: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_B\n\
    \ndef main():\n    N, M, root = read((0, ...))\n    E = read_edges(M, 0)\n   \
    \ MCA = edmonds_branching(E, N, root)\n    ans = sum(w for *_,w in MCA)\n    write(ans)\n\
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
    \ return cls(next(ts))\n        return parser\n\n@overload\ndef read() -> list[int]:\
    \ ...\n@overload\ndef read(spec: Type[_T], char=False) -> _T: ...\n@overload\n\
    def read(spec: _U, char=False) -> _U: ...\n@overload\ndef read(*specs: Type[_T],\
    \ char=False) -> tuple[_T, ...]: ...\n@overload\ndef read(*specs: _U, char=False)\
    \ -> tuple[_U, ...]: ...\ndef read(*specs: Union[Type[_T],_U], char=False):\n\
    \    if not char and not specs: return [int(s) for s in TokenStream.default.line()]\n\
    \    parser: _T = Parser.compile(specs)\n    ret = parser(CharStream.default if\
    \ char else TokenStream.default)\n    return ret[0] if len(specs) == 1 else ret\n\
    \ndef write(*args, **kwargs):\n    '''Prints the values to a stream, or to stdout_fast\
    \ by default.'''\n    sep, file = kwargs.pop(\"sep\", \" \"), kwargs.pop(\"file\"\
    , IOWrapper.stdout)\n    at_start = True\n    for x in args:\n        if not at_start:\n\
    \            file.write(sep)\n        file.write(str(x))\n        at_start = False\n\
    \    file.write(kwargs.pop(\"end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n\
    \        file.flush()\n\n\n\n\nclass Edge(tuple, Parsable):\n    @classmethod\n\
    \    def compile(cls, I=-1):\n        def parse(ts: TokenStream):\n          \
    \  u,v = ts.line()\n            return cls((int(u)+I,int(v)+I))\n        return\
    \ parse\n\nE = TypeVar('E', bound=Edge)\nM = TypeVar('M', bound=int)\n\nclass\
    \ EdgeCollection(Parsable):\n    @classmethod\n    def compile(cls, M: M, E: E\
    \ = Edge[-1]):\n        if isinstance(I := E, int):\n            E = Edge[I]\n\
    \        edge = Parser.compile(E)\n        def parse(ts: TokenStream):\n     \
    \       return cls(edge(ts) for _ in range(M))\n        return parse\n\nclass\
    \ EdgeList(EdgeCollection, list[E]):\n    pass\n\nclass EdgeSet(EdgeCollection,\
    \ set[E]):\n    pass\n\n\nfrom functools import total_ordering \n\n@total_ordering\n\
    class EdgeWeighted(Edge):\n    def __lt__(self, other: tuple) -> bool:\n     \
    \   a = self[2],self[0],self[1]\n        b = other[2],other[0],other[1]\n    \
    \    return a < b\n    \n    @classmethod\n    def compile(cls, I=-1):\n     \
    \   def parse(ts: TokenStream):\n            u,v,w = ts.line()\n            return\
    \ cls((int(u)+I, int(v)+I, int(w)))\n        return parse\n\nM = TypeVar('M',\
    \ bound=int)\nEw = TypeVar('Ew', bound=EdgeWeighted)\nclass EdgeCollectionWeighted(EdgeCollection):\n\
    \    @classmethod\n    def compile(cls, M: M, Ew: Ew = EdgeWeighted[-1]):\n  \
    \      if isinstance(I := Ew, int):\n            Ew = EdgeWeighted[I]\n      \
    \  return super().compile(M, Ew)\n\nclass EdgeListWeighted(EdgeCollectionWeighted,\
    \ list[Ew]):\n    pass\n\nclass EdgeSetWeighted(EdgeCollectionWeighted, set[Ew]):\n\
    \    pass\n\ndef read_edges(M, I=-1):\n    return read(EdgeListWeighted[M,I])\n\
    from functools import reduce\n\n\n\ndef heappush(heap: list, item):\n    heap.append(item)\n\
    \    heapsiftdown(heap, 0, len(heap)-1)\n\ndef heappop(heap: list):\n    item\
    \ = heap.pop()\n    if heap: item, heap[0] = heap[0], item; heapsiftup(heap, 0)\n\
    \    return item\n\ndef heapreplace(heap: list, item):\n    item, heap[0] = heap[0],\
    \ item; heapsiftup(heap, 0)\n    return item\n\ndef heappushpop(heap: list, item):\n\
    \    if heap and heap[0] < item: item, heap[0] = heap[0], item; heapsiftup(heap,\
    \ 0)\n    return item\n\ndef heapify(x: list):\n    for i in reversed(range(len(x)//2)):\
    \ heapsiftup(x, i)\n\ndef heapsiftdown(heap: list, root: int, pos: int):\n   \
    \ item = heap[pos]\n    while root < pos and item < heap[p := (pos-1)>>1]: heap[pos],\
    \ pos = heap[p], p\n    heap[pos] = item\n\ndef heapsiftup(heap: list, pos: int):\n\
    \    n, item, c = len(heap)-1, heap[pos], pos<<1|1\n    while c < n and heap[c\
    \ := c+(heap[c+1]<heap[c])] < item: heap[pos], pos, c = heap[c], c, c<<1|1\n \
    \   if c == n and heap[c] < item: heap[pos], pos = heap[c], c\n    heap[pos] =\
    \ item\n\ndef heappop_max(heap: list):\n    item = heap.pop()\n    if heap: item,\
    \ heap[0] = heap[0], item; heapsiftup_max(heap, 0)\n    return item\n\ndef heapreplace_max(heap:\
    \ list, item):\n    item, heap[0] = heap[0], item; heapsiftup_max(heap, 0)\n \
    \   return item\n\ndef heapify_max(x: list):\n    for i in reversed(range(len(x)//2)):\
    \ heapsiftup_max(x, i)\n\ndef heappush_max(heap: list, item):\n    heap.append(item);\
    \ heapsiftdown_max(heap, 0, len(heap)-1)\n\ndef heapreplace_max(heap: list, item):\n\
    \    item, heap[0] = heap[0], item; heapsiftup_max(heap, 0)\n    return item\n\
    \ndef heappushpop_max(heap: list, item):\n    if heap and heap[0] > item: item,\
    \ heap[0] = heap[0], item; heapsiftup_max(heap, 0)\n    return item\n\ndef heapsiftdown_max(heap:\
    \ list, root: int, pos: int):\n    item = heap[pos]\n    while root < pos and\
    \ heap[p := (pos-1)>>1] < item: heap[pos], pos = heap[p], p\n    heap[pos] = item\n\
    \ndef heapsiftup_max(heap: list, pos: int):\n    n, item, c = len(heap)-1, heap[pos],\
    \ pos<<1|1\n    while c < n and item < heap[c := c+(heap[c]<heap[c+1])]: heap[pos],\
    \ pos, c = heap[c], c, c<<1|1\n    if c == n and item < heap[c]: heap[pos], pos\
    \ = heap[c], c\n    heap[pos] = item\n\n# def heapsiftdown(heap: list, root: int,\
    \ pos: int):\n#     item = heap[pos]\n#     while root < pos and item < heap[p\
    \ := (pos-1)>>1]: heap[pos], pos = heap[p], p\n#     heap[pos] = item\n\n# def\
    \ heapsiftup(heap: list, pos: int):\n#     n, item, c = len(heap)-1, heap[pos],\
    \ pos<<1|1\n#     while c < n and heap[c := c+(heap[c+1]<heap[c])] < item: heap[pos],\
    \ pos, c = heap[c], c, c<<1|1\n#     if c == n and heap[c] < item: heap[pos],\
    \ pos = heap[c], c\n#     heap[pos] = item\n\n\nsys.setrecursionlimit(10**6)\n\
    import pypyjit\npypyjit.set_param(\"max_unroll_recursion=-1\")\nfrom typing import\
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
    \        return dsu\n        return parse_fn\n\ndef floyds_cycle(F, root):\n \
    \   slow = fast = root\n    while F[fast] != -1 and F[F[fast]] != -1:\n      \
    \  slow, fast = F[slow], F[F[fast]]\n        if slow == fast:\n            cyc\
    \ = [slow]\n            while F[slow] != cyc[0]:\n                slow = F[slow]\n\
    \                cyc.append(slow)\n            return cyc\n    return None\n\n\
    def edmonds_branching(E, N, root) -> list[tuple[int,int,any]]:\n    # obtain incoming\
    \ edges\n    Gin = [[] for _ in range(N)]\n    for id,(u,v,w) in enumerate(E):\n\
    \        if v != root:\n            Gin[v].append([w,u,id])\n    \n\n    # heapify\
    \ for fast access to optimal edges\n    for v in range(N):\n        heapify(Gin[v])\n\
    \n    groups = DSU(N)\n    active = set(range(N))\n    active.discard(root)\n\n\
    \    def find_cycle(min_in):\n        for v in active:\n            cyc = floyds_cycle(min_in,\
    \ v)\n            if cyc: return cyc\n        return None\n    \n    def contract(cyc):\n\
    \        kickout = [-1]*len(E)\n        active.difference_update(cyc)\n      \
    \  nv = reduce(groups.merge, cyc)\n        active.add(nv)\n        new_edges =\
    \ []\n        \n        # Update Gin to reflect the contracted cycle\n       \
    \ for v in cyc:\n            cw, _, cid = Gin[v][0]\n            for edge in Gin[v]:\n\
    \                _, u, id = edge\n                if groups.leader(u) != nv:\n\
    \                    edge[0] -= cw # update weight\n                    kickout[id]\
    \ = cid\n                    new_edges.append(edge)\n                    if new_edges[-1][0]\
    \ < new_edges[0][0]:\n                        new_edges[0], new_edges[-1] = new_edges[-1],\
    \ new_edges[0]\n            Gin[v].clear()\n        Gin[nv] = new_edges\n    \
    \    return kickout\n\n\n    def rec(Gin):\n        min_in = [groups.leader(Gin[v][0][1])\
    \ if Gin[v] else -1 for v in range(N)]\n        cyc = find_cycle(min_in)\n   \
    \     if cyc:\n            C = { Gin[v][0][2] for v in cyc }\n            kickout\
    \ = contract(cyc)\n            MCA = rec(Gin)\n            for id in MCA:\n  \
    \              C.discard(kickout[id])\n            MCA.extend(C)\n           \
    \ return MCA\n        else:\n            return [edges[0][2] for edges in Gin\
    \ if edges]\n\n    return [E[id] for id in rec(Gin)]\n\nif __name__ == '__main__':\n\
    \    main()\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_B\n\
    \ndef main():\n    N, M, root = read((0, ...))\n    E = read_edges(M, 0)\n   \
    \ MCA = edmonds_branching(E, N, root)\n    ans = sum(w for *_,w in MCA)\n    write(ans)\n\
    \nfrom cp_library.io.read_fn import read\nfrom cp_library.io.write_fn import write\n\
    from cp_library.io.read_edges_weighted_fn import read_edges\nfrom cp_library.alg.graph.edmonds_fn\
    \ import edmonds_branching\n\nif __name__ == '__main__':\n    main()"
  dependsOn:
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/io/read_edges_weighted_fn.py
  - cp_library/alg/graph/edmonds_fn.py
  - cp_library/io/fast_io_cls.py
  - cp_library/alg/graph/edge_list_weighted_cls.py
  - cp_library/ds/heap/fast_heapq.py
  - cp_library/misc/setrecursionlimit.py
  - cp_library/ds/dsu_cls.py
  - cp_library/alg/graph/floyds_cycle_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/alg/graph/edge_list_cls.py
  - cp_library/alg/graph/edge_weighted_cls.py
  - cp_library/ds/csr/csr_incremental_cls.py
  - cp_library/alg/graph/edge_cls.py
  isVerificationFile: true
  path: test/aoj/grl/grl_2_b_edmonds_branching.test.py
  requiredBy: []
  timestamp: '2025-05-19 05:52:10+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl/grl_2_b_edmonds_branching.test.py
layout: document
redirect_from:
- /verify/test/aoj/grl/grl_2_b_edmonds_branching.test.py
- /verify/test/aoj/grl/grl_2_b_edmonds_branching.test.py.html
title: test/aoj/grl/grl_2_b_edmonds_branching.test.py
---
