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
    path: cp_library/alg/graph/graph_cls.py
    title: cp_library/alg/graph/graph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/graph_weighted_cls.py
    title: cp_library/alg/graph/graph_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
    title: cp_library/alg/tree/lca_table_weighted_iterative_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/bit_cls.py
    title: cp_library/ds/bit_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/sparse_table_cls.py
    title: cp_library/ds/sparse_table_cls.py
  - icon: ':question:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':question:'
    path: cp_library/io/read_specs_fn.py
    title: cp_library/io/read_specs_fn.py
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
    \ndef main():\n    N = read(int)\n    E = read(EdgeListWeighted[N-1])\n    T =\
    \ GraphWeighted(N, E)\n    lca = LCATableWeighted(T)\n    bit = BinaryIndexTree(lca.weights)\n\
    \n    Q = read(int)\n    for query in read(list[tuple[int,int,int], Q]):\n   \
    \     match query:\n            case 1, i, w:\n                i -= 1\n      \
    \          u,v,_ = E[i]\n                p, _ = lca.query(u,v)\n             \
    \   c = u if p == v else v\n                l,r = lca.start[c], lca.end[c]\n \
    \               bit.set(l,w)\n                bit.set(r,-w)\n\n            case\
    \ 2, u, v:\n                u,v=u-1,v-1\n                a,_ = lca.query(u,v)\n\
    \                ans = bit.pref_sum(lca.end[u]) + \\\n                    bit.pref_sum(lca.end[v])\
    \ - \\\n                    2*bit.pref_sum(lca.end[a])\n                print(ans)\n\
    \        \n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2578\n             https://kobejean.github.io/cp-library             \
    \  \n'''\n\nfrom typing import TypeVar\n\n\n\nimport sys\nimport typing\nfrom\
    \ collections import deque\nfrom numbers import Number\nfrom typing import Callable,\
    \ Collection, Iterator, TypeAlias, TypeVar\n\nclass TokenStream(Iterator):\n \
    \   def __init__(self, stream = sys.stdin):\n        self.stream = stream\n  \
    \      self.queue = deque()\n\n    def __next__(self):\n        if not self.queue:\
    \ self.queue.extend(self.line())\n        return self.queue.popleft()\n    \n\
    \    def wait(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        while self.queue: yield\n        \n    def line(self):\n        assert\
    \ not self.queue\n        return next(self.stream).rstrip().split()\n\nclass CharStream(Iterator):\n\
    \    def line(self):\n        assert not self.queue\n        return next(self.stream).rstrip()\n\
    \        \nT = TypeVar('T')\nParseFn: TypeAlias = Callable[[TokenStream],T]\n\
    class Parser:\n    def __init__(self, spec: type[T]|T):\n        self.parse =\
    \ Parser.compile(spec)\n\n    def __call__(self, ts: TokenStream) -> T:\n    \
    \    return self.parse(ts)\n    \n    @staticmethod\n    def compile_type(cls:\
    \ type[T], args = ()) -> T:\n        if issubclass(cls, Parsable):\n         \
    \   return cls.compile(*args)\n        elif issubclass(cls, (Number, str)):\n\
    \            def parse(ts: TokenStream):\n                return cls(next(ts))\
    \              \n            return parse\n        elif issubclass(cls, tuple):\n\
    \            return Parser.compile_tuple(cls, args)\n        elif issubclass(cls,\
    \ Collection):\n            return Parser.compile_collection(cls, args)\n    \
    \    elif callable(cls):\n            def parse(ts: TokenStream):\n          \
    \      return cls(next(ts))              \n            return parse\n        else:\n\
    \            raise NotImplementedError()\n    \n    @staticmethod\n    def compile(spec:\
    \ type[T]|T=int) -> ParseFn[T]:\n        if isinstance(spec, type):\n        \
    \    cls = typing.get_origin(spec) or spec\n            args = typing.get_args(spec)\
    \ or tuple()\n            return Parser.compile_type(cls, args)\n        elif\
    \ isinstance(offset := spec, Number): \n            cls = type(spec)  \n     \
    \       def parse(ts: TokenStream):\n                return cls(next(ts)) + offset\n\
    \            return parse\n        elif isinstance(args := spec, tuple):     \
    \ \n            return Parser.compile_tuple(type(spec), args)\n        elif isinstance(args\
    \ := spec, Collection):  \n            return Parser.compile_collection(type(spec),\
    \ args)\n        else:\n            raise NotImplementedError()\n    \n    @staticmethod\n\
    \    def compile_line(cls: T, spec=int) -> ParseFn[T]:\n        fn = Parser.compile(spec)\n\
    \        def parse(ts: TokenStream):\n            return cls(fn(ts) for _ in ts.wait())\n\
    \        return parse\n\n    @staticmethod\n    def compile_repeat(cls: T, spec,\
    \ N) -> ParseFn[T]:\n        fn = Parser.compile(spec)\n        def parse(ts:\
    \ TokenStream):\n            return cls(fn(ts) for _ in range(N))\n        return\
    \ parse\n\n    @staticmethod\n    def compile_children(cls: T, specs) -> ParseFn[T]:\n\
    \        fns = tuple(Parser.compile(spec) for spec in specs)\n        def parse(ts:\
    \ TokenStream):\n            return cls(fn(ts) for fn in fns)  \n        return\
    \ parse\n\n    @staticmethod\n    def compile_tuple(cls: type[T], specs) -> ParseFn[T]:\n\
    \        match specs:\n            case [spec, end] if end is ...:\n         \
    \       return Parser.compile_line(cls, spec)\n            case specs:   \n  \
    \              return Parser.compile_children(cls, specs)\n    \n    @staticmethod\n\
    \    def compile_collection(cls, specs):\n        match specs:\n            case\
    \ [ ] | [_] | set():\n                return Parser.compile_line(cls, *specs)\n\
    \            case [spec, int() as n]:\n                return Parser.compile_repeat(cls,\
    \ spec, n)\n            case _:\n                raise NotImplementedError()\n\
    \n        \nclass Parsable:\n    @classmethod\n    def compile(cls):\n       \
    \ def parser(ts: TokenStream):\n            return cls(next(ts))\n        return\
    \ parser\n\nH = TypeVar('H')\nclass Edge(tuple, Parsable):\n    @property\n  \
    \  def u(self) -> int: return self[0]\n    @property\n    def v(self) -> int:\
    \ return self[1]\n    @property\n    def forw(self) -> H: return self[1]\n   \
    \ @property\n    def back(self) -> H: return self[0]\n    @classmethod\n    def\
    \ compile(cls, I=1):\n        def parse(ts: TokenStream):\n            return\
    \ cls((int(s)+I for s in ts.line()))\n        return parse\n\nE = TypeVar('E',\
    \ bound=Edge)\nM = TypeVar('M', bound=int)\n\nclass EdgeCollection(Parsable):\n\
    \    @classmethod\n    def compile(cls, M: M, E: E = Edge[-1]):\n        if isinstance(I\
    \ := E, int):\n            E = Edge[I]\n        edge = Parser.compile(E)\n   \
    \     def parse(ts: TokenStream):\n            return cls(edge(ts) for _ in range(M))\n\
    \        return parse\n\nclass EdgeList(EdgeCollection, list[E]):\n    pass\n\n\
    class EdgeSet(EdgeCollection, set[E]):\n    pass\n\n\nclass EdgeWeighted(Edge,\
    \ Parsable):\n    H: TypeAlias = tuple[int,int]\n    @property\n    def u(self):\
    \ return self[0]\n    @property\n    def v(self): return self[1]\n    @property\n\
    \    def w(self): return self[2]\n    @property\n    def forw(self) -> H: return\
    \ self[1], self[2]\n    @property\n    def back(self) -> H: return self[0], self[2]\n\
    \n    def __lt__(self, other: tuple) -> bool:\n        a = self[2],self[0],self[1]\n\
    \        b = other[2],other[0],other[1]\n        return a < b\n    \n    @classmethod\n\
    \    def compile(cls, I=-1):\n        def parse(ts: TokenStream):\n          \
    \  u,v,w = ts.line()\n            return cls((int(u)+I, int(v)+I, int(w)))\n \
    \       return parse\n\nM = TypeVar('M', bound=int)\nEw = TypeVar('Ew', bound=EdgeWeighted)\n\
    class EdgeCollectionWeighted(EdgeCollection):\n    @classmethod\n    def compile(cls,\
    \ M: M, Ew: Ew = EdgeWeighted[-1]):\n        if isinstance(I := Ew, int):\n  \
    \          Ew = EdgeWeighted[I]\n        return super().compile(M, Ew)\n\nclass\
    \ EdgeListWeighted(EdgeCollectionWeighted, list[Ew]):\n    pass\n\nclass EdgeSetWeighted(EdgeCollectionWeighted,\
    \ set[Ew]):\n    pass\n\n\n\nclass Graph(list[H], Parsable):\n    def __init__(G,\
    \ N: int, edges=[]):\n        super().__init__([] for _ in range(N))\n       \
    \ G.E = list(edges)\n        for edge in G.E:\n            G[edge.u].append(edge.forw)\n\
    \            G[edge.v].append(edge.back)\n\n    @classmethod\n    def compile(cls,\
    \ N: int, M: int, E = Edge[-1]):\n        if isinstance(E, int): E = Edge[E]\n\
    \        edge = Parser.compile(E)\n        def parse(ts: TokenStream):\n     \
    \       return cls(N, (edge(ts) for _ in range(M)))\n        return parse\n\n\
    class GraphWeighted(Graph):\n    @classmethod\n    def compile(cls, N: int, M:\
    \ int, E: EdgeWeighted|int = EdgeWeighted[-1]):\n        if isinstance(E, int):\
    \ E = EdgeWeighted[E]\n        return super().compile(N, M, E)\n\n\n\nfrom typing\
    \ import Any, Callable, List\n\nclass SparseTable:\n    def __init__(self, op:\
    \ Callable[[Any, Any], Any], arr: List[Any]):\n        self.n = len(arr)\n   \
    \     self.log = self.n.bit_length()\n        self.op = op\n        self.st =\
    \ [[None] * (self.n-(1<<i)+1) for i in range(self.log)]\n        self.st[0] =\
    \ arr[:]\n        \n        for i in range(self.log-1):\n            row, d =\
    \ self.st[i], 1<<i\n            for j in range(len(self.st[i+1])):\n         \
    \       self.st[i+1][j] = op(row[j], row[j+d])\n\n    def query(self, l: int,\
    \ r: int) -> Any:\n        k = (r-l).bit_length()-1\n        return self.op(self.st[k][l],\
    \ self.st[k][r-(1<<k)])\n    \n    def __repr__(self) -> str:\n        return\
    \ '\\n'.join(f'{i:<2d} {row}' for i,row in enumerate(self.st))\n\nclass LCATableWeighted(SparseTable):\n\
    \    def __init__(self, T, root = 0):\n        self.start = [-1] * len(T)\n  \
    \      self.end = [-1] * len(T)\n        self.euler = []\n        self.depth =\
    \ []\n        self.weights = []\n        \n        # Iterative DFS\n        stack\
    \ = [(root, -1, 0, 0)]\n        while stack:\n            u, p, d, w = stack.pop()\n\
    \            \n            if self.start[u] == -1:\n                self.start[u]\
    \ = len(self.euler)\n                for v, nw in reversed(T[u]):\n          \
    \          if v != p:\n                        stack.append((u, p, d, -nw))\n\
    \                        stack.append((v, u, d+1, nw))\n\n            self.euler.append(u)\n\
    \            self.depth.append(d)\n            self.weights.append(w)\n      \
    \      self.end[u] = len(self.euler)\n        super().__init__(min, list(zip(self.depth,\
    \ self.euler)))\n\n    def query(self, u, v) -> tuple[int,int]:\n        l, r\
    \ = min(self.start[u], self.start[v]), max(self.start[u], self.start[v])+1\n \
    \       d, a = super().query(l, r)\n        return a, d\n\nclass BinaryIndexTree:\n\
    \    def __init__(self, v: int|list):\n        if isinstance(v, int):\n      \
    \      self.data, self.size = [0]*v, v\n        else:\n            self.build(v)\n\
    \n    def build(self, data):\n        self.data, self.size = data, len(data)\n\
    \        for i in range(self.size):\n            if (r := i|(i+1)) < self.size:\
    \ \n                self.data[r] += self.data[i]\n\n    def get(self, i: int):\n\
    \        assert 0 <= i < self.size\n        s = self.data[i]\n        z = i&(i+1)\n\
    \        for _ in range((i^z).bit_count()):\n            s, i = s-self.data[i-1],\
    \ i-(i&-i)\n        return s\n    \n    def set(self, i: int, x: int):\n     \
    \   self.add(i, x-self.get(i))\n        \n    def add(self, i: int, x: object)\
    \ -> None:\n        assert 0 <= i <= self.size\n        i += 1\n        while\
    \ i <= self.size:\n            self.data[i-1], i = self.data[i-1] + x, i+(i&-i)\n\
    \n    def pref_sum(self, i: int):\n        assert 0 <= i <= self.size\n      \
    \  s = 0\n        for _ in range(i.bit_count()):\n            s, i = s+self.data[i-1],\
    \ i-(i&-i)\n        return s\n    \n    def range_sum(self, l: int, r: int):\n\
    \        return self.pref_sum(r) - self.pref_sum(l)\n\nfrom typing import Iterator,\
    \ Type, TypeVar, overload\n\nT = TypeVar('T')\n@overload\ndef read(spec: int|None)\
    \ -> Iterator[int]: ...\n@overload\ndef read(spec: Type[T]|T) -> T: ...\ndef read(spec:\
    \ Type[T]|T=None, char=False):\n    match spec, char:\n        case None, False:\n\
    \            return map(int, input().split())\n        case int(offset), False:\n\
    \            return (int(s)+offset for s in input().split())\n        case _,\
    \ _:\n            if char:\n                stream = CharStream(sys.stdin)\n \
    \           else:\n                stream = TokenStream(sys.stdin)\n         \
    \   parser: T = Parser.compile(spec)\n            return parser(stream)\n\nif\
    \ __name__ == \"__main__\":\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc294/tasks/abc294_g\n\
    \ndef main():\n    N = read(int)\n    E = read(EdgeListWeighted[N-1])\n    T =\
    \ GraphWeighted(N, E)\n    lca = LCATableWeighted(T)\n    bit = BinaryIndexTree(lca.weights)\n\
    \n    Q = read(int)\n    for query in read(list[tuple[int,int,int], Q]):\n   \
    \     match query:\n            case 1, i, w:\n                i -= 1\n      \
    \          u,v,_ = E[i]\n                p, _ = lca.query(u,v)\n             \
    \   c = u if p == v else v\n                l,r = lca.start[c], lca.end[c]\n \
    \               bit.set(l,w)\n                bit.set(r,-w)\n\n            case\
    \ 2, u, v:\n                u,v=u-1,v-1\n                a,_ = lca.query(u,v)\n\
    \                ans = bit.pref_sum(lca.end[u]) + \\\n                    bit.pref_sum(lca.end[v])\
    \ - \\\n                    2*bit.pref_sum(lca.end[a])\n                print(ans)\n\
    \        \n\nfrom cp_library.alg.graph.edge_list_weighted_cls import EdgeListWeighted\n\
    from cp_library.alg.graph.graph_weighted_cls import GraphWeighted\nfrom cp_library.alg.tree.lca_table_weighted_iterative_cls\
    \ import LCATableWeighted\nfrom cp_library.ds.bit_cls import BinaryIndexTree\n\
    from cp_library.io.read_specs_fn import read\n\nif __name__ == \"__main__\":\n\
    \    main()"
  dependsOn:
  - cp_library/alg/graph/edge_list_weighted_cls.py
  - cp_library/alg/graph/graph_weighted_cls.py
  - cp_library/alg/tree/lca_table_weighted_iterative_cls.py
  - cp_library/ds/bit_cls.py
  - cp_library/io/read_specs_fn.py
  - cp_library/alg/graph/edge_list_cls.py
  - cp_library/alg/graph/edge_weighted_cls.py
  - cp_library/alg/graph/graph_cls.py
  - cp_library/ds/sparse_table_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/alg/graph/edge_cls.py
  isVerificationFile: true
  path: test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
  requiredBy: []
  timestamp: '2024-09-28 03:27:29+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
layout: document
redirect_from:
- /verify/test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
- /verify/test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py.html
title: test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
---
