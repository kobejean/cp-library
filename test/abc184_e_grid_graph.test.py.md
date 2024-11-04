---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/graph_proto.py
    title: cp_library/alg/graph/graph_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/grid_graph_cls.py
    title: cp_library/alg/graph/grid_graph_cls.py
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
    PROBLEM: https://atcoder.jp/contests/abc184/tasks/abc184_e
    links:
    - https://atcoder.jp/contests/abc184/tasks/abc184_e
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc184/tasks/abc184_e\n\
    from math import inf\nfrom typing import Iterable\n\ndef main():\n    H, W = read(tuple[int,\
    \ ...])\n    G = read(TeleportGraph[H,W])\n    s = g = None\n    for v,c in enumerate(G.S):\n\
    \        match c:\n            case 'S': s = v\n            case 'G': g = v\n\n\
    \    ans = G.bfs(s, g)\n    print(ans if ans != inf else -1)\n    \nfrom collections.abc\
    \ import Iterator\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2578\n             https://kobejean.github.io/cp-library       \
    \        \n'''\n\nimport sys\nimport typing\nfrom collections import deque\nfrom\
    \ numbers import Number\nfrom typing import Callable, Collection, Iterator, TypeAlias,\
    \ TypeVar\n\nclass TokenStream(Iterator):\n    def __init__(self, stream = sys.stdin):\n\
    \        self.stream = stream\n        self.queue = deque()\n\n    def __next__(self):\n\
    \        if not self.queue: self.queue.extend(self.line())\n        return self.queue.popleft()\n\
    \    \n    def wait(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        while self.queue: yield\n        \n    def line(self):\n        assert\
    \ not self.queue\n        return next(self.stream).rstrip().split()\n\nclass CharStream(TokenStream):\n\
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
    \ parser\n\n\nfrom typing import Iterable, overload\n\nclass GraphProtocol(list,\
    \ Parsable):\n\n    def neighbors(G, v: int) -> Iterable[int]:\n        return\
    \ G[v]\n    \n    def edge_ids(G) -> list[list[int]]: ...\n\n    @overload\n \
    \   def distance(G) -> list[list[int]]: ...\n    @overload\n    def distance(G,\
    \ s: int = 0) -> list[int]: ...\n    @overload\n    def distance(G, s: int, g:\
    \ int) -> int: ...\n    def distance(G, s = None, g = None):\n        match s,\
    \ g:\n            case None, None:\n                return G.floyd_warshall()\n\
    \            case s, None:\n                return G.bfs(s)\n            case\
    \ s, g:\n                return G.bfs(s, g)\n\n    @overload\n    def bfs(G, s:\
    \ int = 0) -> list[int]: ...\n    @overload\n    def bfs(G, s: int, g: int) ->\
    \ int: ...\n    def bfs(G, s = 0, g = None):\n        D = [inf for _ in range(G.N)]\n\
    \        D[s] = 0\n        q = deque([s])\n        while q:\n            nd =\
    \ D[u := q.popleft()]+1\n            if u == g: return D[u]\n            for v\
    \ in G.neighbors(u):\n                if nd < D[v]:\n                    D[v]\
    \ = nd\n                    q.append(v)\n        return D if g is None else inf\
    \    \n    \n    \n    def floyd_warshall(G) -> list[list[int]]:\n        D =\
    \ [[inf]*G.N for _ in range(G.N)]\n\n        for u in G:\n            D[u][u]\
    \ = 0\n            for v in G.neighbors(u):\n                D[u][v] = 1\n   \
    \     \n        for k, Dk in enumerate(D):\n            for Di in D:\n       \
    \         for j in range(G.N):\n                    Di[j] = min(Di[j], Di[k]+Dk[j])\n\
    \        return D\n    \n    \n    def find_cycle(G, s = 0, vis = None, par =\
    \ None):\n        N = G.N\n        vis = vis or [0] * N\n        par = par or\
    \ [-1] * N\n        if vis[s]: return None\n        vis[s] = 1\n        stack\
    \ = [(True, s)]\n        while stack:\n            forw, v = stack.pop()\n   \
    \         if forw:\n                stack.append((False, v))\n               \
    \ vis[v] = 1\n                for u in G.neighbors(v):\n                    if\
    \ vis[u] == 1 and u != par[v]:\n                        # Cycle detected\n   \
    \                     cyc = [u]\n                        vis[u] = 2\n        \
    \                while v != u:\n                            cyc.append(v)\n  \
    \                          vis[v] = 2\n                            v = par[v]\n\
    \                        return cyc\n                    elif vis[u] == 0:\n \
    \                       par[u] = v\n                        stack.append((True,\
    \ u))\n            else:\n                vis[v] = 2\n        return None\n  \
    \  \n    def bridges(G):\n        tin = [-1] * G.N\n        low = [-1] * G.N\n\
    \        par = [-1] * G.N\n        vis = [0] * G.N\n        in_edge = [-1] * G.N\n\
    \n        Eid = G.edge_ids()\n        time = 0\n        bridges = []\n       \
    \ stack = list(range(G.N))\n        while stack:\n            v = stack.pop()\n\
    \            p = par[v]\n            match vis[v]:\n                case 0:\n\
    \                    vis[v] = 1\n                    tin[v] = low[v] = time\n\
    \                    time += 1\n                    stack.append(v)\n        \
    \            for i, child in enumerate(G.neighbors(v)):\n                    \
    \    if child == p:\n                            continue\n                  \
    \      match vis[child]:\n                            case 0:\n              \
    \                  # Tree edge - recurse\n                                par[child]\
    \ = v\n                                in_edge[child] = Eid[v][i]\n          \
    \                      stack.append(child)\n                            case 1:\n\
    \                                # Back edge - update low-link value\n       \
    \                         low[v] = min(low[v], tin[child])\n                case\
    \ 1:\n                    vis[v] = 2\n                    if p != -1:\n      \
    \                  low[p] = min(low[p], low[v])\n                        if low[v]\
    \ > tin[p]:\n                            bridges.append(in_edge[v])\n        \
    \        \n        return bridges\n\n    def articulation_points(G):\n       \
    \ N = G.N\n        order = [-1] * N\n        low = [-1] * N\n        par = [-1]\
    \ * N\n        vis = [0] * G.N\n        children = [0] * G.N\n        ap = [False]\
    \ * N\n        time = 0\n        stack = list(range(N))\n\n        while stack:\n\
    \            v = stack.pop()\n            p = par[v]\n            if vis[v] ==\
    \ 0:\n                vis[v] = 1\n                order[v] = low[v] = time\n \
    \               time += 1\n            \n                stack.append(v)\n   \
    \             for child in G[v]:\n                    if order[child] == -1:\n\
    \                        par[child] = v\n                        stack.append(child)\n\
    \                    elif child != p:\n                        low[v] = min(low[v],\
    \ order[child])\n                if p != -1:\n                    children[p]\
    \ += 1\n            elif vis[v] == 1:\n                vis[v] = 2\n          \
    \      ap[v] |= p == -1 and children[v] > 1\n                if p != -1:\n   \
    \                 low[p] = min(low[p], low[v])\n                    ap[p] |= par[p]\
    \ != -1 and low[v] >= order[p]\n\n        return ap\n\n    @classmethod\n    def\
    \ compile(cls, N: int, M: int, E):\n        edge = Parser.compile(E)\n       \
    \ def parse(ts: TokenStream):\n            return cls(N, (edge(ts) for _ in range(M)))\n\
    \        return parse\n    \n\nclass GridGraph(GraphProtocol):\n    def __init__(G,\
    \ H, W, S=[]):\n        G.N = W*H\n        G.W = W\n        G.H = H\n        G.S\
    \ = S\n        G.dirs = [(-1,0),(0,1),(1,0),(0,-1)]\n        G.wall = '#'\n  \
    \  \n    def neighbors(G, v: int) -> Iterable[int]:\n        H, W = G.H, G.W\n\
    \        i,j = divmod(v, W)\n        adj = []\n        for di,dj in G.dirs:\n\
    \            ni,nj = i+di,j+dj\n            u = ni*W+nj\n            if 0 <= ni\
    \ < H and 0 <= nj < W and G.S[u] != G.wall:\n                adj.append(u)\n \
    \       return adj\n    \n    def __len__(G) -> int:\n        return G.N\n   \
    \ \n    def __getitem__(G, v):\n        return G.neighbors(v)\n    \n    def __iter__(G)\
    \ -> Iterator:\n        return (G.neighbors(v) for v in range(G.N))\n    \n  \
    \  @classmethod\n    def compile(cls, H: int, W: int):\n        def parse(ts:\
    \ TokenStream):\n            S = ''.join(next(ts.stream).rstrip() for _ in range(H))\n\
    \            return cls(H, W, S)\n        return parse\n\nclass TeleportGraph(GridGraph):\n\
    \    def __init__(G, H, W, S=[]):\n        super().__init__(H, W, S)\n       \
    \ G.group = group = [set() for _ in range(26)]\n        for u,c in enumerate(S):\n\
    \            match c:\n                case '.'|'#'|'S'|'G': ...\n           \
    \     case c: group[ord(c)-ord('a')].add(u)\n\n    def neighbors(G, v: int) ->\
    \ Iterable[int]:\n        match G.S[v]:\n            case '.'|'S'|'G': return\
    \ super().neighbors(v)\n            case c if adj := G.group[i := ord(c)-ord('a')]:\n\
    \                G.group[i] = None\n                adj.update(super().neighbors(v))\n\
    \                return adj\n            case _: return super().neighbors(v)\n\
    \    \n\n\nfrom typing import Type, TypeVar, overload\n\nT = TypeVar('T')\n@overload\n\
    def read(spec: int|None) -> list[int]: ...\n@overload\ndef read(spec: Type[T]|T,\
    \ char=False) -> T: ...\ndef read(spec: Type[T]|T=None, char=False):\n    match\
    \ spec, char:\n        case None, False:\n            return list(map(int, input().split()))\n\
    \        case int(offset), False:\n            return [int(s)+offset for s in\
    \ input().split()]\n        case _, _:\n            if char:\n               \
    \ stream = CharStream(sys.stdin)\n            else:\n                stream =\
    \ TokenStream(sys.stdin)\n            parser: T = Parser.compile(spec)\n     \
    \       return parser(stream)\n\nif __name__ == \"__main__\":\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc184/tasks/abc184_e\n\
    from math import inf\nfrom typing import Iterable\n\ndef main():\n    H, W = read(tuple[int,\
    \ ...])\n    G = read(TeleportGraph[H,W])\n    s = g = None\n    for v,c in enumerate(G.S):\n\
    \        match c:\n            case 'S': s = v\n            case 'G': g = v\n\n\
    \    ans = G.bfs(s, g)\n    print(ans if ans != inf else -1)\n    \nfrom cp_library.alg.graph.grid_graph_cls\
    \ import GridGraph\n\nclass TeleportGraph(GridGraph):\n    def __init__(G, H,\
    \ W, S=[]):\n        super().__init__(H, W, S)\n        G.group = group = [set()\
    \ for _ in range(26)]\n        for u,c in enumerate(S):\n            match c:\n\
    \                case '.'|'#'|'S'|'G': ...\n                case c: group[ord(c)-ord('a')].add(u)\n\
    \n    def neighbors(G, v: int) -> Iterable[int]:\n        match G.S[v]:\n    \
    \        case '.'|'S'|'G': return super().neighbors(v)\n            case c if\
    \ adj := G.group[i := ord(c)-ord('a')]:\n                G.group[i] = None\n \
    \               adj.update(super().neighbors(v))\n                return adj\n\
    \            case _: return super().neighbors(v)\n    \n\nfrom cp_library.io.read_specs_fn\
    \ import read\n\nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - cp_library/alg/graph/grid_graph_cls.py
  - cp_library/io/read_specs_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/alg/graph/graph_proto.py
  isVerificationFile: true
  path: test/abc184_e_grid_graph.test.py
  requiredBy: []
  timestamp: '2024-11-04 17:54:46+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/abc184_e_grid_graph.test.py
layout: document
redirect_from:
- /verify/test/abc184_e_grid_graph.test.py
- /verify/test/abc184_e_grid_graph.test.py.html
title: test/abc184_e_grid_graph.test.py
---
