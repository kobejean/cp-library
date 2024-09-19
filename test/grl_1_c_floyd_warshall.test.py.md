---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/floyd_warshall_check_neg_cycle_fn.py
    title: cp_library/alg/graph/floyd_warshall_check_neg_cycle_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/floyd_warshall_directed_fn.py
    title: cp_library/alg/graph/floyd_warshall_directed_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/floyd_warshall_fn.py
    title: cp_library/alg/graph/floyd_warshall_fn.py
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
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_C
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_C
  bundledCode: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_C\n\
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
    \ G\n    \n\ndef floyd_warshall(G, N, directed=True) -> tuple[bool, list[int]]:\n\
    \    if directed:\n        \n        def floyd_warshall(G, N) -> list[int]:\n\
    \            D = [[inf]*N for _ in range(N)]\n        \n            for u, edges\
    \ in enumerate(G):\n                D[u][u] = 0\n                for w,v in edges:\n\
    \                    D[u][v] = min(D[u][v], w)\n            \n            for\
    \ k, Dk in enumerate(D):\n                for Di in D:\n                    for\
    \ j in range(N):\n                        Di[j] = min(Di[j], Di[k]+Dk[j])\n  \
    \          return D\n    else:\n        \n        def floyd_warshall(G, N) ->\
    \ list[int]:\n            D = [[inf]*N for _ in range(N)]\n        \n        \
    \    for u, edges in enumerate(G):\n                D[u][u] = 0\n            \
    \    for w,v in edges:\n                    D[u][v] = min(D[u][v], w)\n      \
    \      \n            for k, Dk in enumerate(D):\n                for i, Di in\
    \ enumerate(D):\n                    for j in range(i):\n                    \
    \    Di[j] = D[j][i] = min(Di[j], Di[k]+Dk[j])\n            return D\n    D =\
    \ floyd_warshall(G, N)\n    return any(D[i][i] < 0 for i in range(N)), D\n\nN,\
    \ M = read()\nG = read_graph(N, M, 0)\nneg_cycle, D = floyd_warshall(G, N)\n\n\
    if neg_cycle:\n    print(\"NEGATIVE CYCLE\")\nelse:\n    for row in D:\n     \
    \   print(*('INF' if d == inf else d for d in row))\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_C\n\
    from math import inf\nfrom cp_library.io.read_graph_weighted_directed_fn import\
    \ read_graph\nfrom cp_library.io.read_specs_fn import read\nfrom cp_library.alg.graph.floyd_warshall_check_neg_cycle_fn\
    \ import floyd_warshall\n\nN, M = read()\nG = read_graph(N, M, 0)\nneg_cycle,\
    \ D = floyd_warshall(G, N)\n\nif neg_cycle:\n    print(\"NEGATIVE CYCLE\")\nelse:\n\
    \    for row in D:\n        print(*('INF' if d == inf else d for d in row))"
  dependsOn:
  - cp_library/io/read_graph_weighted_directed_fn.py
  - cp_library/io/read_specs_fn.py
  - cp_library/alg/graph/floyd_warshall_check_neg_cycle_fn.py
  - cp_library/alg/graph/floyd_warshall_directed_fn.py
  - cp_library/alg/graph/floyd_warshall_fn.py
  - cp_library/io/parse_stream_fn.py
  - cp_library/io/parsable_cls.py
  isVerificationFile: true
  path: test/grl_1_c_floyd_warshall.test.py
  requiredBy: []
  timestamp: '2024-09-20 02:31:14+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/grl_1_c_floyd_warshall.test.py
layout: document
redirect_from:
- /verify/test/grl_1_c_floyd_warshall.test.py
- /verify/test/grl_1_c_floyd_warshall.test.py.html
title: test/grl_1_c_floyd_warshall.test.py
---
