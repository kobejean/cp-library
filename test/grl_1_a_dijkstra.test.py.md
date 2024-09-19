---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/dijkstra_fn.py
    title: cp_library/alg/graph/dijkstra_fn.py
  - icon: ':question:'
    path: cp_library/io/parsable_cls.py
    title: cp_library/io/parsable_cls.py
  - icon: ':question:'
    path: cp_library/io/parse_stream_fn.py
    title: cp_library/io/parse_stream_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_graph_weighted_directed_fn.py
    title: cp_library/io/read_graph_weighted_directed_fn.py
  - icon: ':question:'
    path: cp_library/io/read_specs_fn.py
    title: cp_library/io/read_specs_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/1/GRL/all/GRL_1_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/1/GRL/all/GRL_1_A
  bundledCode: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/1/GRL/all/GRL_1_A\n\
    from math import inf\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2578\n             https://kobejean.github.io/cp-library       \
    \        \n'''\n\nimport sys\nfrom typing import Type, TypeVar\n\nT = TypeVar('T')\n\
    def read(spec: Type[T]|T=[int]) -> T:\n    return parse_stream(sys.stdin, spec)\n\
    \n\nimport typing\nfrom collections import deque\nfrom numbers import Number\n\
    from typing import Collection, Iterator, Type, TypeVar\n\n\nclass Parsable:\n\
    \    @classmethod\n    def parse(cls, parse_spec):\n        return parse_spec(lambda\
    \ s: cls(s))\n\nT = TypeVar('T')\ndef parse_stream(stream: Iterator[str], spec:\
    \ Type[T]|T) -> T:\n\n    def parse_tuple(cls, specs):\n        match specs:\n\
    \            case [spec, end] if end is ...: \n                return cls(parse_line(spec))\n\
    \            case specs:                     \n                return cls(parse_spec(spec)\
    \ for spec in specs)\n\n    def parse_collection(cls, specs) -> list:\n      \
    \  match specs:\n            case [ ] | [_] | set():          \n             \
    \   return cls(parse_line(*specs))\n            case [spec, int() as n]: \n  \
    \              return cls(parse_spec(spec) for _ in range(n))\n            case\
    \ _:\n                raise NotImplementedError()\n\n    def parse_spec(spec):\n\
    \        if args := match_spec(spec, Parsable):\n            cls, args = args\n\
    \            return cls.parse(parse_spec, *args)\n        elif args := match_spec(spec,\
    \ tuple):      \n            return parse_tuple(*args)\n        elif args := match_spec(spec,\
    \ Collection): \n            return parse_collection(*args)\n        elif issubclass(cls\
    \ := type(offset := spec), Number):         \n            return cls(next_token())\
    \ + offset\n        elif callable(cls := spec):                  \n          \
    \  return cls(next_token())\n        else:\n            raise NotImplementedError()\n\
    \n    def next_token():\n        if not queue: queue.extend(next_line())\n   \
    \     return queue.popleft()\n    \n    def parse_line(spec=int):\n        if\
    \ not queue: queue.extend(next_line())\n        while queue: yield parse_spec(spec)\n\
    \        \n    def next_line():\n        return next(stream).rstrip().split()\n\
    \    \n    def match_spec(spec, types):\n        if issubclass(cls := type(specs\
    \ := spec), types):\n            return cls, specs\n        elif (isinstance(spec,\
    \ type) and \n             issubclass(cls := typing.get_origin(spec) or spec,\
    \ types)):\n            return cls, (typing.get_args(spec) or tuple())\n     \
    \   \n    queue = deque() \n    return parse_spec(spec)\n\n\ndef read_graph(n:\
    \ int, m: int, i0=1):\n    G = [[] for _ in range(n)]\n    for _ in range(m):\n\
    \        u,v,w = read(tuple[-i0,-i0,int])\n        G[u].append((w,v))\n    return\
    \ G\n    \n\nimport heapq\n\ndef dijkstra(G, N, root) -> list[int]:\n    D = [inf\
    \ for _ in range(N)]\n    D[root] = 0\n    q = [(0, root)]\n    while q:\n   \
    \     d, v = heapq.heappop(q)\n        if d > D[v]: continue\n\n        for w,\
    \ u in G[v]:\n            nd = d + w\n            if nd < D[u]:\n            \
    \    D[u] = nd\n                heapq.heappush(q, (nd, u))\n    return D\n\nN,\
    \ M, r = read()\nG = read_graph(N, M, 0)\nD = dijkstra(G, N, r)\nprint(*('INF'\
    \ if d == inf else d for d in D), sep='\\n')\n"
  code: '# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/1/GRL/all/GRL_1_A

    from math import inf

    from cp_library.io.read_graph_weighted_directed_fn import read_graph

    from cp_library.io.read_specs_fn import read

    from cp_library.alg.graph.dijkstra_fn import dijkstra


    N, M, r = read()

    G = read_graph(N, M, 0)

    D = dijkstra(G, N, r)

    print(*(''INF'' if d == inf else d for d in D), sep=''\n'')'
  dependsOn:
  - cp_library/io/read_graph_weighted_directed_fn.py
  - cp_library/io/read_specs_fn.py
  - cp_library/alg/graph/dijkstra_fn.py
  - cp_library/io/parse_stream_fn.py
  - cp_library/io/parsable_cls.py
  isVerificationFile: true
  path: test/grl_1_a_dijkstra.test.py
  requiredBy: []
  timestamp: '2024-09-20 02:31:14+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/grl_1_a_dijkstra.test.py
layout: document
redirect_from:
- /verify/test/grl_1_a_dijkstra.test.py
- /verify/test/grl_1_a_dijkstra.test.py.html
title: test/grl_1_a_dijkstra.test.py
---
