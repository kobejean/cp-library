---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/alg/graph/digraph_cls.py
    title: cp_library/alg/graph/digraph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/digraph_weighted_cls.py
    title: cp_library/alg/graph/digraph_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/graph_cls.py
    title: cp_library/alg/graph/graph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/graph_weighted_cls.py
    title: cp_library/alg/graph/graph_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/graph_weighted_proto.py
    title: cp_library/alg/graph/graph_weighted_proto.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_cls.py
    title: cp_library/alg/tree/tree_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/tree/tree_weighted_cls.py
    title: cp_library/alg/tree/tree_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_tree_fn.py
    title: cp_library/io/read_tree_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
    title: test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
    title: test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc337_g_tree_inversion_heavy_light_decomposition.test.py
    title: test/abc337_g_tree_inversion_heavy_light_decomposition.test.py
  - icon: ':heavy_check_mark:'
    path: test/dp_v_subtree_rerooting_iterative.test.py
    title: test/dp_v_subtree_rerooting_iterative.test.py
  - icon: ':heavy_check_mark:'
    path: test/dp_v_subtree_rerooting_recursive.test.py
    title: test/dp_v_subtree_rerooting_recursive.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_1_a_dijkstra.test.py
    title: test/grl_1_a_dijkstra.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_1_b_bellman_ford.test.py
    title: test/grl_1_b_bellman_ford.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_1_c_floyd_warshall.test.py
    title: test/grl_1_c_floyd_warshall.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_3_a_find_articulation_points.test.py
    title: test/grl_3_a_find_articulation_points.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_3_a_tarjan_articulation_points.test.py
    title: test/grl_3_a_tarjan_articulation_points.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \n\nimport sys\nimport typing\nfrom collections import deque\nfrom numbers import\
    \ Number\nfrom typing import Callable, Collection, Iterator, TypeAlias, TypeVar\n\
    \nclass TokenStream(Iterator):\n    def __init__(self, stream = sys.stdin):\n\
    \        self.stream = stream\n        self.queue = deque()\n\n    def __next__(self):\n\
    \        if not self.queue: self.queue.extend(self.line())\n        return self.queue.popleft()\n\
    \    \n    def wait(self):\n        if not self.queue: self.queue.extend(self.line())\n\
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
    \ parser\n\nfrom typing import Iterable\nfrom math import inf\n\nclass GraphProtocol(list,\
    \ Parsable):\n\n    def neighbors(G, v: int) -> Iterable[int]:\n        return\
    \ G[v]\n    \n    def edge_ids(G) -> list[list[int]]: ...\n    \n    def bfs(G,\
    \ s = 0) -> list[int]:\n        D = [inf for _ in range(G.N)]\n        D[s] =\
    \ 0\n        q = deque([s])\n        while q:\n            nd = D[u := q.popleft()]+1\n\
    \            for v in G.neighbors(u):\n                if nd < D[v]:\n       \
    \             D[v] = nd\n                    q.append(v)\n        return D\n \
    \   \n    def find_cycle(G, s = 0, vis = None, par = None):\n        N = G.N\n\
    \        vis = vis or [0] * N\n        par = par or [-1] * N\n        if vis[s]:\
    \ return None\n        vis[s] = 1\n        stack = [(True, s)]\n        while\
    \ stack:\n            forw, v = stack.pop()\n            if forw:\n          \
    \      stack.append((False, v))\n                vis[v] = 1\n                for\
    \ u in G.neighbors(v):\n                    if vis[u] == 1 and u != par[v]:\n\
    \                        # Cycle detected\n                        cyc = [u]\n\
    \                        vis[u] = 2\n                        while v != u:\n \
    \                           cyc.append(v)\n                            vis[v]\
    \ = 2\n                            v = par[v]\n                        return\
    \ cyc\n                    elif vis[u] == 0:\n                        par[u] =\
    \ v\n                        stack.append((True, u))\n            else:\n    \
    \            vis[v] = 2\n        return None\n    \n    def bridges(G):\n    \
    \    tin = [-1] * G.N\n        low = [-1] * G.N\n        par = [-1] * G.N\n  \
    \      vis = [0] * G.N\n        in_edge = [-1] * G.N\n\n        Eid = G.edge_ids()\n\
    \        time = 0\n        bridges = []\n        stack = list(range(G.N))\n  \
    \      while stack:\n            v = stack.pop()\n            p = par[v]\n   \
    \         match vis[v]:\n                case 0:\n                    vis[v] =\
    \ 1\n                    tin[v] = low[v] = time\n                    time += 1\n\
    \                    stack.append(v)\n                    for i, child in enumerate(G.neighbors(v)):\n\
    \                        if child == p:\n                            continue\n\
    \                        match vis[child]:\n                            case 0:\n\
    \                                # Tree edge - recurse\n                     \
    \           par[child] = v\n                                in_edge[child] = Eid[v][i]\n\
    \                                stack.append(child)\n                       \
    \     case 1:\n                                # Back edge - update low-link value\n\
    \                                low[v] = min(low[v], tin[child])\n          \
    \      case 1:\n                    vis[v] = 2\n                    if p != -1:\n\
    \                        low[p] = min(low[p], low[v])\n                      \
    \  if low[v] > tin[p]:\n                            bridges.append(in_edge[v])\n\
    \                \n        return bridges\n\n    def articulation_points(G):\n\
    \        N = G.N\n        order = [-1] * N\n        low = [-1] * N\n        par\
    \ = [-1] * N\n        vis = [0] * G.N\n        children = [0] * G.N\n        ap\
    \ = [False] * N\n        time = 0\n        stack = list(range(N))\n\n        while\
    \ stack:\n            v = stack.pop()\n            p = par[v]\n            if\
    \ vis[v] == 0:\n                vis[v] = 1\n                order[v] = low[v]\
    \ = time\n                time += 1\n            \n                stack.append(v)\n\
    \                for child in G[v]:\n                    if order[child] == -1:\n\
    \                        par[child] = v\n                        stack.append(child)\n\
    \                    elif child != p:\n                        low[v] = min(low[v],\
    \ order[child])\n                if p != -1:\n                    children[p]\
    \ += 1\n            elif vis[v] == 1:\n                vis[v] = 2\n          \
    \      ap[v] |= p == -1 and children[v] > 1\n                if p != -1:\n   \
    \                 low[p] = min(low[p], low[v])\n                    ap[p] |= par[p]\
    \ != -1 and low[v] >= order[p]\n\n        return ap\n\n    @classmethod\n    def\
    \ compile(cls, N: int, M: int, E):\n        edge = Parser.compile(E)\n       \
    \ def parse(ts: TokenStream):\n            return cls(N, (edge(ts) for _ in range(M)))\n\
    \        return parse\n    \n"
  code: "import cp_library.alg.graph.__header__\nfrom cp_library.io.parser_cls import\
    \ Parsable, Parser, TokenStream\n\nfrom typing import Iterable\nfrom collections\
    \ import deque\nfrom math import inf\n\nclass GraphProtocol(list, Parsable):\n\
    \n    def neighbors(G, v: int) -> Iterable[int]:\n        return G[v]\n    \n\
    \    def edge_ids(G) -> list[list[int]]: ...\n    \n    def bfs(G, s = 0) -> list[int]:\n\
    \        D = [inf for _ in range(G.N)]\n        D[s] = 0\n        q = deque([s])\n\
    \        while q:\n            nd = D[u := q.popleft()]+1\n            for v in\
    \ G.neighbors(u):\n                if nd < D[v]:\n                    D[v] = nd\n\
    \                    q.append(v)\n        return D\n    \n    def find_cycle(G,\
    \ s = 0, vis = None, par = None):\n        N = G.N\n        vis = vis or [0] *\
    \ N\n        par = par or [-1] * N\n        if vis[s]: return None\n        vis[s]\
    \ = 1\n        stack = [(True, s)]\n        while stack:\n            forw, v\
    \ = stack.pop()\n            if forw:\n                stack.append((False, v))\n\
    \                vis[v] = 1\n                for u in G.neighbors(v):\n      \
    \              if vis[u] == 1 and u != par[v]:\n                        # Cycle\
    \ detected\n                        cyc = [u]\n                        vis[u]\
    \ = 2\n                        while v != u:\n                            cyc.append(v)\n\
    \                            vis[v] = 2\n                            v = par[v]\n\
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
    \        return parse\n    "
  dependsOn:
  - cp_library/io/parser_cls.py
  isVerificationFile: false
  path: cp_library/alg/graph/graph_proto.py
  requiredBy:
  - cp_library/io/read_tree_fn.py
  - cp_library/alg/graph/graph_weighted_proto.py
  - cp_library/alg/graph/graph_cls.py
  - cp_library/alg/graph/digraph_cls.py
  - cp_library/alg/graph/graph_weighted_cls.py
  - cp_library/alg/graph/digraph_weighted_cls.py
  - cp_library/alg/tree/tree_cls.py
  - cp_library/alg/tree/tree_weighted_cls.py
  timestamp: '2024-10-23 00:17:22+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/grl_1_b_bellman_ford.test.py
  - test/grl_3_a_tarjan_articulation_points.test.py
  - test/abc337_g_tree_inversion_heavy_light_decomposition.test.py
  - test/grl_1_c_floyd_warshall.test.py
  - test/grl_3_a_find_articulation_points.test.py
  - test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
  - test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
  - test/grl_1_a_dijkstra.test.py
  - test/dp_v_subtree_rerooting_recursive.test.py
  - test/dp_v_subtree_rerooting_iterative.test.py
documentation_of: cp_library/alg/graph/graph_proto.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/graph_proto.py
- /library/cp_library/alg/graph/graph_proto.py.html
title: cp_library/alg/graph/graph_proto.py
---
