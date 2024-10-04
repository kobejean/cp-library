---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge_cls.py
    title: cp_library/alg/graph/edge_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/graph_cls.py
    title: cp_library/alg/graph/graph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/heavy_light_decomposition_cls.py
    title: cp_library/alg/tree/heavy_light_decomposition_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_cls.py
    title: cp_library/alg/tree/tree_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/bit_cls.py
    title: cp_library/ds/bit_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_specs_fn.py
    title: cp_library/io/read_specs_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/abc337/tasks/abc337_g
    links:
    - https://atcoder.jp/contests/abc337/tasks/abc337_g
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc337/tasks/abc337_g\n\
    \nfrom itertools import accumulate\n\ndef main():\n    N = read(int)\n    T =\
    \ read(Tree[N])\n\n    hld = HLD(T)\n    bit = BinaryIndexTree(N)\n    ans = [0]*(N+1)\n\
    \n    def range_add(l,r,x):\n        ans[l] += x\n        ans[r] -= x\n\n    for\
    \ v in range(N):\n        for c in T[v]:\n            if c == hld.par[v]:\n  \
    \              l,r = hld.start[v], hld.end[v]\n                cnt = v-bit.range_sum(l,r)\n\
    \                range_add(l,r,cnt)\n            else:\n                l,r =\
    \ hld.start[c], hld.end[c]\n                cnt = bit.range_sum(l,r)\n       \
    \         range_add(0,l,cnt)\n                range_add(r,N,cnt)\n        bit.set(hld[v],1)\n\
    \    ans = list(accumulate(ans))\n    ans = [ans[i] for i in hld.start]\n    print(*ans)\n\
    \n\n\nclass HLD:\n    def __init__(self, T, r=0):\n        N = len(T)\n      \
    \  # build\n        size = [1]*N\n        start = [0]*N\n        end = [0]*N\n\
    \        par = [-1]*N\n        heavy = [-1]*N\n        head = [-1]*N\n       \
    \ depth = [0]*N\n        order = [0]*N\n        time = 0\n\n        stack = [(2,r,r),\
    \ (0,r,-1)]\n        while stack:\n            match stack.pop():\n          \
    \      case 0, v, p: # dfs down\n                    par[v] = p\n            \
    \        stack.append((1, v, p))\n                    for c in T[v]:\n       \
    \                 if c != p:\n                            depth[c] = depth[v]\
    \ + 1 \n                            stack.append((0, c, v))\n\n              \
    \  case 1, v, p: # dfs up\n                    l = -1\n                    for\
    \ c in T[v]:\n                        if c != p:\n                           \
    \ size[v] += size[c]\n                            if l == -1 or size[c] > size[l]:\n\
    \                                l = c\n                    heavy[v] = l\n\n \
    \               case 2, v, h: # decompose down\n                    head[v] =\
    \ h\n                    start[v] = time\n                    order[time] = v\n\
    \                    p = par[v]\n                    time += 1\n             \
    \       l = heavy[v]\n                    stack.append((3, v, h))\n          \
    \          \n                    for c in T[v]:\n                        if c\
    \ != p and c != l:\n                            stack.append((2, c, c))\n\n  \
    \                  if l != -1:\n                        stack.append((2, l, h))\n\
    \                case 3, v, h: # decompose up\n                    end[v] = time\n\
    \        self.N = N\n        self.T = T\n        self.size = size\n        self.start\
    \ = start\n        self.end = end\n        self.par = par\n        self.heavy\
    \ = heavy\n        self.head = head\n        self.depth = depth\n        self.order\
    \ = order\n\n    def __getitem__(self, key):\n        return self.start[key]\n\
    \n    def path(self, u, v, edge=False):\n        head, depth, par, start = self.head,\
    \ self.depth, self.par, self.start\n        while head[u] != head[v]:\n      \
    \      if depth[head[u]] < depth[head[v]]:\n                u,v = v,u\n      \
    \      yield start[head[u]], start[u]+1\n            u = par[head[u]]\n\n    \
    \    if depth[u] < depth[v]:\n            u,v = v,u\n\n        yield start[v]+edge,\
    \ start[u]+1\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2578\n             https://kobejean.github.io/cp-library             \
    \  \n'''\nfrom typing import TypeVar\n\n\nimport sys\nimport typing\nfrom collections\
    \ import deque\nfrom numbers import Number\nfrom typing import Callable, Collection,\
    \ Iterator, TypeAlias, TypeVar\n\nclass TokenStream(Iterator):\n    def __init__(self,\
    \ stream = sys.stdin):\n        self.stream = stream\n        self.queue = deque()\n\
    \n    def __next__(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        return self.queue.popleft()\n    \n    def wait(self):\n        if not\
    \ self.queue: self.queue.extend(self.line())\n        while self.queue: yield\n\
    \        \n    def line(self):\n        assert not self.queue\n        return\
    \ next(self.stream).rstrip().split()\n\nclass CharStream(Iterator):\n    def line(self):\n\
    \        assert not self.queue\n        return next(self.stream).rstrip()\n  \
    \      \nT = TypeVar('T')\nParseFn: TypeAlias = Callable[[TokenStream],T]\nclass\
    \ Parser:\n    def __init__(self, spec: type[T]|T):\n        self.parse = Parser.compile(spec)\n\
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
    \    def compile(spec: type[T]|T=int) -> ParseFn[T]:\n        if isinstance(spec,\
    \ type):\n            cls = typing.get_origin(spec) or spec\n            args\
    \ = typing.get_args(spec) or tuple()\n            return Parser.compile_type(cls,\
    \ args)\n        elif isinstance(offset := spec, Number): \n            cls =\
    \ type(spec)  \n            def parse(ts: TokenStream):\n                return\
    \ cls(next(ts)) + offset\n            return parse\n        elif isinstance(args\
    \ := spec, tuple):      \n            return Parser.compile_tuple(type(spec),\
    \ args)\n        elif isinstance(args := spec, Collection):  \n            return\
    \ Parser.compile_collection(type(spec), args)\n        else:\n            raise\
    \ NotImplementedError()\n    \n    @staticmethod\n    def compile_line(cls: T,\
    \ spec=int) -> ParseFn[T]:\n        fn = Parser.compile(spec)\n        def parse(ts:\
    \ TokenStream):\n            return cls(fn(ts) for _ in ts.wait())\n        return\
    \ parse\n\n    @staticmethod\n    def compile_repeat(cls: T, spec, N) -> ParseFn[T]:\n\
    \        fn = Parser.compile(spec)\n        def parse(ts: TokenStream):\n    \
    \        return cls(fn(ts) for _ in range(N))\n        return parse\n\n    @staticmethod\n\
    \    def compile_children(cls: T, specs) -> ParseFn[T]:\n        fns = tuple(Parser.compile(spec)\
    \ for spec in specs)\n        def parse(ts: TokenStream):\n            return\
    \ cls(fn(ts) for fn in fns)  \n        return parse\n\n    @staticmethod\n   \
    \ def compile_tuple(cls: type[T], specs) -> ParseFn[T]:\n        match specs:\n\
    \            case [spec, end] if end is ...:\n                return Parser.compile_line(cls,\
    \ spec)\n            case specs:   \n                return Parser.compile_children(cls,\
    \ specs)\n    \n    @staticmethod\n    def compile_collection(cls, specs):\n \
    \       match specs:\n            case [ ] | [_] | set():\n                return\
    \ Parser.compile_line(cls, *specs)\n            case [spec, int() as n]:\n   \
    \             return Parser.compile_repeat(cls, spec, n)\n            case _:\n\
    \                raise NotImplementedError()\n\n        \nclass Parsable:\n  \
    \  @classmethod\n    def compile(cls):\n        def parser(ts: TokenStream):\n\
    \            return cls(next(ts))\n        return parser\n\nH = TypeVar('H')\n\
    class Edge(tuple, Parsable):\n    @property\n    def u(self) -> int: return self[0]\n\
    \    @property\n    def v(self) -> int: return self[1]\n    @property\n    def\
    \ forw(self) -> H: return self[1]\n    @property\n    def back(self) -> H: return\
    \ self[0]\n    @classmethod\n    def compile(cls, I=1):\n        def parse(ts:\
    \ TokenStream):\n            return cls((int(s)+I for s in ts.line()))\n     \
    \   return parse\n\n\nclass Graph(list[H], Parsable):\n    def __init__(G, N:\
    \ int, edges=[]):\n        super().__init__([] for _ in range(N))\n        G.E\
    \ = list(edges)\n        for edge in G.E:\n            G[edge.u].append(edge.forw)\n\
    \            G[edge.v].append(edge.back)\n\n    @classmethod\n    def compile(cls,\
    \ N: int, M: int, E = Edge[-1]):\n        if isinstance(E, int): E = Edge[E]\n\
    \        edge = Parser.compile(E)\n        def parse(ts: TokenStream):\n     \
    \       return cls(N, (edge(ts) for _ in range(M)))\n        return parse\n\n\
    class Tree(Graph):\n    @classmethod\n    def compile(cls, N: int, E: type[Edge]|int\
    \ = Edge[-1]):\n        return super().compile(N, N-1, E)\n\n\nclass BinaryIndexTree:\n\
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
    \        return self.pref_sum(r) - self.pref_sum(l)\n\nfrom typing import Type,\
    \ TypeVar, overload\n\nT = TypeVar('T')\n@overload\ndef read(spec: int|None) ->\
    \ list[int]: ...\n@overload\ndef read(spec: Type[T]|T) -> T: ...\ndef read(spec:\
    \ Type[T]|T=None, char=False):\n    match spec, char:\n        case None, False:\n\
    \            return list(map(int, input().split()))\n        case int(offset),\
    \ False:\n            return [int(s)+offset for s in input().split()]\n      \
    \  case _, _:\n            if char:\n                stream = CharStream(sys.stdin)\n\
    \            else:\n                stream = TokenStream(sys.stdin)\n        \
    \    parser: T = Parser.compile(spec)\n            return parser(stream)\n\nif\
    \ __name__ == \"__main__\":\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc337/tasks/abc337_g\n\
    \nfrom itertools import accumulate\n\ndef main():\n    N = read(int)\n    T =\
    \ read(Tree[N])\n\n    hld = HLD(T)\n    bit = BinaryIndexTree(N)\n    ans = [0]*(N+1)\n\
    \n    def range_add(l,r,x):\n        ans[l] += x\n        ans[r] -= x\n\n    for\
    \ v in range(N):\n        for c in T[v]:\n            if c == hld.par[v]:\n  \
    \              l,r = hld.start[v], hld.end[v]\n                cnt = v-bit.range_sum(l,r)\n\
    \                range_add(l,r,cnt)\n            else:\n                l,r =\
    \ hld.start[c], hld.end[c]\n                cnt = bit.range_sum(l,r)\n       \
    \         range_add(0,l,cnt)\n                range_add(r,N,cnt)\n        bit.set(hld[v],1)\n\
    \    ans = list(accumulate(ans))\n    ans = [ans[i] for i in hld.start]\n    print(*ans)\n\
    \nfrom cp_library.alg.tree.heavy_light_decomposition_cls import HLD\nfrom cp_library.alg.tree.tree_cls\
    \ import Tree\nfrom cp_library.ds.bit_cls import BinaryIndexTree\nfrom cp_library.io.read_specs_fn\
    \ import read\n\nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - cp_library/alg/tree/heavy_light_decomposition_cls.py
  - cp_library/alg/tree/tree_cls.py
  - cp_library/ds/bit_cls.py
  - cp_library/io/read_specs_fn.py
  - cp_library/alg/graph/edge_cls.py
  - cp_library/alg/graph/graph_cls.py
  - cp_library/io/parser_cls.py
  isVerificationFile: true
  path: test/abc337_g_tree_inversion_heavy_light_decomposition.test.py
  requiredBy: []
  timestamp: '2024-10-04 19:59:43+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/abc337_g_tree_inversion_heavy_light_decomposition.test.py
layout: document
redirect_from:
- /verify/test/abc337_g_tree_inversion_heavy_light_decomposition.test.py
- /verify/test/abc337_g_tree_inversion_heavy_light_decomposition.test.py.html
title: test/abc337_g_tree_inversion_heavy_light_decomposition.test.py
---
