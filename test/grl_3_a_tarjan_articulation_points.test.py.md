---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/graph_cls.py
    title: cp_library/alg/graph/graph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/tarjan_articulation_points_fn.py
    title: cp_library/alg/graph/tarjan_articulation_points_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parsable_cls.py
    title: cp_library/io/parsable_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parse_stream_fn.py
    title: cp_library/io/parse_stream_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_graph_fn.py
    title: cp_library/io/read_graph_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_specs_fn.py
    title: cp_library/io/read_specs_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/misc/setrecursionlimit.py
    title: cp_library/misc/setrecursionlimit.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_A
  bundledCode: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_A\n\
    \ndef main():\n    N, M = read()\n    G = read_graph(N, M, 0)\n    ans = sorted(tarjan_articulation_points(G,\
    \ N))\n    if ans:\n        print(*ans, sep='\\n')\n\n'''\n\u257A\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\nimport sys\nsys.setrecursionlimit(10**6)\nimport pypyjit\n\
    pypyjit.set_param(\"max_unroll_recursion=-1\")\n\ndef tarjan_articulation_points(G,\
    \ N):\n    order = [None] * N\n    low = [None] * N\n    parent = [-1] * N\n \
    \   ap = set()\n    time = 0\n\n    def dfs(u):\n        nonlocal time\n     \
    \   children = 0\n        order[u] = low[u] = time\n        time += 1\n\n    \
    \    for v in G[u]:\n            if order[v] is None:\n                children\
    \ += 1\n                parent[v] = u\n                dfs(v)\n              \
    \  low[u] = min(low[u], low[v])\n                if parent[u] != -1 and low[v]\
    \ >= order[u]:\n                    ap.add(u)\n            elif v != parent[u]:\n\
    \                low[u] = min(low[u], order[v])\n\n        if parent[u] == -1\
    \ and children > 1:\n            ap.add(u)\n\n    for i in range(N):\n       \
    \ if order[i] is None:\n            dfs(i)\n\n    return ap\n\n\nfrom typing import\
    \ Type, TypeVar\n\nT = TypeVar('T')\ndef read(spec: Type[T]|T=[int]) -> T:\n \
    \   return parse_stream(sys.stdin, spec)\n\n\nimport typing\nfrom collections\
    \ import deque\nfrom numbers import Number\nfrom typing import Collection, Iterator,\
    \ Type, TypeVar\n\n\nclass Parsable:\n    @classmethod\n    def parse(cls, parse_spec):\n\
    \        return parse_spec(lambda s: cls(s))\n\nT = TypeVar('T')\ndef parse_stream(stream:\
    \ Iterator[str], spec: Type[T]|T) -> T:\n\n    def parse_tuple(cls, specs):\n\
    \        match specs:\n            case [spec, end] if end is ...: \n        \
    \        return cls(parse_line(spec))\n            case specs:               \
    \      \n                return cls(parse_spec(spec) for spec in specs)\n\n  \
    \  def parse_collection(cls, specs) -> list:\n        match specs:\n         \
    \   case [ ] | [_] | set():          \n                return cls(parse_line(*specs))\n\
    \            case [spec, int() as n]: \n                return cls(parse_spec(spec)\
    \ for _ in range(n))\n            case _:\n                raise NotImplementedError()\n\
    \n    def parse_spec(spec):\n        if args := match_spec(spec, Parsable):\n\
    \            cls, args = args\n            return cls.parse(parse_spec, *args)\n\
    \        elif args := match_spec(spec, tuple):      \n            return parse_tuple(*args)\n\
    \        elif args := match_spec(spec, Collection): \n            return parse_collection(*args)\n\
    \        elif issubclass(cls := type(offset := spec), Number):         \n    \
    \        return cls(next_token()) + offset\n        elif callable(cls := spec):\
    \                  \n            return cls(next_token())\n        else:\n   \
    \         raise NotImplementedError()\n\n    def next_token():\n        if not\
    \ queue: queue.extend(next_line())\n        return queue.popleft()\n    \n   \
    \ def parse_line(spec=int):\n        if not queue: queue.extend(next_line())\n\
    \        while queue: yield parse_spec(spec)\n        \n    def next_line():\n\
    \        return next(stream).rstrip().split()\n    \n    def match_spec(spec,\
    \ types):\n        if issubclass(cls := type(specs := spec), types):\n       \
    \     return cls, specs\n        elif (isinstance(spec, type) and \n         \
    \    issubclass(cls := typing.get_origin(spec) or spec, types)):\n           \
    \ return cls, (typing.get_args(spec) or tuple())\n        \n    queue = deque()\
    \ \n    return parse_spec(spec)\n\n\n\nclass Graph(list, Parsable):\n    def __init__(self,\
    \ N, edges=[]):\n        super().__init__(([] for _ in range(N)))\n        for\
    \ u,v in edges:\n            self[u].append(v)\n            self[v].append(u)\n\
    \n    @classmethod\n    def parse(cls, parse_spec, N, M, I=-1):\n        return\
    \ cls(N, parse_spec(list[tuple[I,I], M]))\n\n\ndef read_graph(N: int, M: int,\
    \ i0=-1):\n    # G: Graph = [[] for _ in range(n)]\n    # for _ in range(m):\n\
    \    #     u,v = read(tuple[-i0,-i0])\n    #     G[u].append(v)\n    #     G[v].append(u)\n\
    \    return read(Graph[N, M, i0])\n\nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_A\n\
    \ndef main():\n    N, M = read()\n    G = read_graph(N, M, 0)\n    ans = sorted(tarjan_articulation_points(G,\
    \ N))\n    if ans:\n        print(*ans, sep='\\n')\n\nfrom cp_library.alg.graph.tarjan_articulation_points_fn\
    \ import tarjan_articulation_points\nfrom cp_library.io.read_graph_fn import read_graph\n\
    from cp_library.io.read_specs_fn import read\n\nif __name__ == '__main__':\n \
    \   main()"
  dependsOn:
  - cp_library/alg/graph/tarjan_articulation_points_fn.py
  - cp_library/io/read_graph_fn.py
  - cp_library/io/read_specs_fn.py
  - cp_library/misc/setrecursionlimit.py
  - cp_library/alg/graph/graph_cls.py
  - cp_library/io/parse_stream_fn.py
  - cp_library/io/parsable_cls.py
  isVerificationFile: true
  path: test/grl_3_a_tarjan_articulation_points.test.py
  requiredBy: []
  timestamp: '2024-09-20 03:21:05+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/grl_3_a_tarjan_articulation_points.test.py
layout: document
redirect_from:
- /verify/test/grl_3_a_tarjan_articulation_points.test.py
- /verify/test/grl_3_a_tarjan_articulation_points.test.py.html
title: test/grl_3_a_tarjan_articulation_points.test.py
---
