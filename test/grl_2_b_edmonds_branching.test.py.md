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
    path: cp_library/ds/dsu_cls.py
    title: cp_library/ds/dsu_cls.py
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
    \ typing import Type, TypeVar, Union, overload\nimport sys\n\nimport typing\n\
    from collections import deque\nfrom numbers import Number\nfrom types import GenericAlias\
    \ \nfrom typing import Callable, Collection, Iterator, TypeVar, Union\nimport\
    \ os\nfrom io import BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n    BUFSIZE =\
    \ 8192\n    newlines = 0\n\n    def __init__(self, file):\n        self._fd =\
    \ file.fileno()\n        self.buffer = BytesIO()\n        self.writable = \"x\"\
    \ in file.mode or \"r\" not in file.mode\n        self.write = self.buffer.write\
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
    from functools import reduce\nfrom heapq import heapify\n\n\nsys.setrecursionlimit(10**6)\n\
    import pypyjit\npypyjit.set_param(\"max_unroll_recursion=-1\")\n\n\nclass DSU:\n\
    \    def __init__(self, N):\n        self.N = N\n        self.par = [-1] * N\n\
    \n    def merge(self, u, v, src = False):\n        assert 0 <= u < self.N\n  \
    \      assert 0 <= v < self.N\n\n        x, y = self.leader(u), self.leader(v)\n\
    \        if x == y: return (x,y) if src else x\n\n        if self.par[x] > self.par[y]:\n\
    \            x, y = y, x\n\n        self.par[x] += self.par[y]\n        self.par[y]\
    \ = x\n\n        return (x,y) if src else x\n\n    def same(self, u: int, v: int):\n\
    \        assert 0 <= u < self.N\n        assert 0 <= v < self.N\n        return\
    \ self.leader(u) == self.leader(v)\n\n    def leader(self, i) -> int:\n      \
    \  assert 0 <= i < self.N\n        par = self.par\n        p = par[i]\n      \
    \  while p >= 0:\n            if par[p] < 0:\n                return p\n     \
    \       par[i], i, p = par[p], par[p], par[par[p]]\n\n        return i\n\n   \
    \ def size(self, i) -> int:\n        assert 0 <= i < self.N\n        \n      \
    \  return -self.par[self.leader(i)]\n\n    def groups(self) -> list[list[int]]:\n\
    \        leader_buf = [self.leader(i) for i in range(self.N)]\n\n        result\
    \ = [[] for _ in range(self.N)]\n        for i in range(self.N):\n           \
    \ result[leader_buf[i]].append(i)\n\n        return [r for r in result if r]\n\
    \ndef floyds_cycle(F, root):\n    slow = fast = root\n    while F[fast] != -1\
    \ and F[F[fast]] != -1:\n        slow, fast = F[slow], F[F[fast]]\n        if\
    \ slow == fast:\n            cyc = [slow]\n            while F[slow] != cyc[0]:\n\
    \                slow = F[slow]\n                cyc.append(slow)\n          \
    \  return cyc\n    return None\n\ndef edmonds_branching(E, N, root) -> list[tuple[int,int,any]]:\n\
    \    # obtain incoming edges\n    Gin = [[] for _ in range(N)]\n    for id,(u,v,w)\
    \ in enumerate(E):\n        if v != root:\n            Gin[v].append([w,u,id])\n\
    \    \n\n    # heapify for fast access to optimal edges\n    for v in range(N):\n\
    \        heapify(Gin[v])\n\n    groups = DSU(N)\n    active = set(range(N))\n\
    \    active.discard(root)\n\n    def find_cycle(min_in):\n        for v in active:\n\
    \            cyc = floyds_cycle(min_in, v)\n            if cyc: return cyc\n \
    \       return None\n    \n    def contract(cyc):\n        kickout = [-1]*len(E)\n\
    \        active.difference_update(cyc)\n        nv = reduce(groups.merge, cyc)\n\
    \        active.add(nv)\n        new_edges = []\n        \n        # Update Gin\
    \ to reflect the contracted cycle\n        for v in cyc:\n            cw, _, cid\
    \ = Gin[v][0]\n            for edge in Gin[v]:\n                _, u, id = edge\n\
    \                if groups.leader(u) != nv:\n                    edge[0] -= cw\
    \ # update weight\n                    kickout[id] = cid\n                   \
    \ new_edges.append(edge)\n                    if new_edges[-1][0] < new_edges[0][0]:\n\
    \                        new_edges[0], new_edges[-1] = new_edges[-1], new_edges[0]\n\
    \            Gin[v].clear()\n        Gin[nv] = new_edges\n        return kickout\n\
    \n\n    def rec(Gin):\n        min_in = [groups.leader(Gin[v][0][1]) if Gin[v]\
    \ else -1 for v in range(N)]\n        cyc = find_cycle(min_in)\n        if cyc:\n\
    \            C = { Gin[v][0][2] for v in cyc }\n            kickout = contract(cyc)\n\
    \            MCA = rec(Gin)\n            for id in MCA:\n                C.discard(kickout[id])\n\
    \            MCA.extend(C)\n            return MCA\n        else:\n          \
    \  return [edges[0][2] for edges in Gin if edges]\n\n    return [E[id] for id\
    \ in rec(Gin)]\n\nif __name__ == '__main__':\n    main()\n"
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
  - cp_library/misc/setrecursionlimit.py
  - cp_library/ds/dsu_cls.py
  - cp_library/alg/graph/floyds_cycle_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/alg/graph/edge_list_cls.py
  - cp_library/alg/graph/edge_weighted_cls.py
  - cp_library/alg/graph/edge_cls.py
  isVerificationFile: true
  path: test/grl_2_b_edmonds_branching.test.py
  requiredBy: []
  timestamp: '2024-12-08 02:40:51+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/grl_2_b_edmonds_branching.test.py
layout: document
redirect_from:
- /verify/test/grl_2_b_edmonds_branching.test.py
- /verify/test/grl_2_b_edmonds_branching.test.py.html
title: test/grl_2_b_edmonds_branching.test.py
---