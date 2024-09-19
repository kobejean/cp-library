---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/alg/graph/edge_list_type.py
    title: cp_library/alg/graph/edge_list_type.py
  - icon: ':question:'
    path: cp_library/alg/graph/graph_cls.py
    title: cp_library/alg/graph/graph_cls.py
  - icon: ':x:'
    path: cp_library/alg/tree/find_centroid_recursive_fn.py
    title: cp_library/alg/tree/find_centroid_recursive_fn.py
  - icon: ':question:'
    path: cp_library/io/parsable_cls.py
    title: cp_library/io/parsable_cls.py
  - icon: ':question:'
    path: cp_library/io/parse_stream_fn.py
    title: cp_library/io/parse_stream_fn.py
  - icon: ':question:'
    path: cp_library/io/read_specs_fn.py
    title: cp_library/io/read_specs_fn.py
  - icon: ':question:'
    path: cp_library/io/read_tree_fn.py
    title: cp_library/io/read_tree_fn.py
  - icon: ':question:'
    path: cp_library/misc/setrecursionlimit.py
    title: cp_library/misc/setrecursionlimit.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    IGNORE: PROBLEM https://atcoder.jp/contests/arc183/tasks/arc183_d
    links:
    - https://atcoder.jp/contests/arc183/tasks/arc183_d
  bundledCode: "# verification-helper: IGNORE PROBLEM https://atcoder.jp/contests/arc183/tasks/arc183_d\n\
    import heapq\n\ndef solve():\n    N, = read()\n    T = read_tree(N)\n    size\
    \ = [0] * N\n    centroid = find_centroid(T)\n    dfs_order = [[] for _ in range(N)]\n\
    \    matched = (0, -1)\n    heap = []\n\n    def dfs(u, p):\n        r = u\n \
    \       stack = [(u, p, False)]\n        while stack:\n            u, p, done\
    \ = stack.pop()\n            if not done:\n                size[u] = 1\n     \
    \           dfs_order[r].append(u)\n                m = u ^ 1\n              \
    \  stack.append((u, p, True))\n                \n                if m != p and\
    \ m in T[u]:\n                    stack.append((m, u, False))\n\n            \
    \    for v in T[u]:\n                    if v == p or m == v:\n              \
    \          continue\n                    stack.append((v, u, False))\n       \
    \     else:\n                for v in T[u]:\n                    if v != p:\n\
    \                        size[u] += size[v]\n        \n\n    for v in T[centroid]:\n\
    \        dfs(v, centroid)\n        if centroid ^ 1 == v:\n            matched\
    \ = (-size[v], v)\n        else:\n            heapq.heappush(heap, (-size[v],\
    \ v))\n\n    ops = []\n    while heap:\n        s, v = heapq.heappop(heap)\n \
    \       if dfs_order[v] and dfs_order[matched[1]]:\n            leaf1 = dfs_order[v].pop()\n\
    \            leaf2 = dfs_order[matched[1]].pop()\n            ops.append((leaf1,\
    \ leaf2))\n        else:\n            continue\n        if -matched[0] > 1:\n\
    \            heapq.heappush(heap, (matched[0] + 1, matched[1]))\n        matched\
    \ = (s + 1, v)\n\n    if matched[1] != -1:\n        ops.append((centroid, matched[1]))\n\
    \n    return ops\n\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2578\n             https://kobejean.github.io/cp-library       \
    \        \n'''\n\nimport sys\nsys.setrecursionlimit(10**6)\nimport pypyjit\npypyjit.set_param(\"\
    max_unroll_recursion=-1\")\n\ndef find_centroid(T):\n    N = len(T)\n    size\
    \ = [1] * N\n    half = N // 2\n\n    def dfs(u=0, p=None):\n        is_cent =\
    \ True\n        for v in T[u]:\n            if v == p: continue\n            cent\
    \ = dfs(v, u)\n            if cent != -1: return cent\n            if size[v]\
    \ > half: is_cent = False\n            size[u] += size[v]\n        if N - size[u]\
    \ > half:\n            is_cent = False\n        return u if is_cent else -1\n\n\
    \    return dfs()\n\n\nfrom typing import Type, TypeVar\n\nT = TypeVar('T')\n\
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
    \   \n    queue = deque() \n    return parse_spec(spec)\n\n\n\nfrom typing import\
    \ TypeAlias, TypeVar\n\nM = TypeVar('M', int, None)\nI = TypeVar('I', int, None)\n\
    EdgeList: TypeAlias = list[tuple[I,I], M]\n\nclass Graph(list, Parsable):\n  \
    \  def __init__(self, N, edges: EdgeList=[]):\n        super().__init__(([] for\
    \ _ in range(N)))\n        for u,v in edges:\n            self[u].append(v)\n\
    \            self[v].append(u)\n\n    @classmethod\n    def parse(cls, parse_spec,\
    \ N, M, I=-1):\n        return cls(N, parse_spec(EdgeList[I,M]))\n\n\ndef read_tree(N,\
    \ i0=1):\n    T: Graph = [[] for _ in range(N)]\n    for _ in range(N-1):\n  \
    \      u,v = read(tuple[-i0,-i0])\n        T[u].append(v)\n        T[v].append(u)\n\
    \    return T\n\n\n# from cp_library.io.read_specs_fn import read\n# from cp_library.alg.graph.graph_cls\
    \ import Graph\n\nfor op in solve():\n    print(op[0] + 1, op[1] + 1)\n"
  code: "# verification-helper: IGNORE PROBLEM https://atcoder.jp/contests/arc183/tasks/arc183_d\n\
    import heapq\n\ndef solve():\n    N, = read()\n    T = read_tree(N)\n    size\
    \ = [0] * N\n    centroid = find_centroid(T)\n    dfs_order = [[] for _ in range(N)]\n\
    \    matched = (0, -1)\n    heap = []\n\n    def dfs(u, p):\n        r = u\n \
    \       stack = [(u, p, False)]\n        while stack:\n            u, p, done\
    \ = stack.pop()\n            if not done:\n                size[u] = 1\n     \
    \           dfs_order[r].append(u)\n                m = u ^ 1\n              \
    \  stack.append((u, p, True))\n                \n                if m != p and\
    \ m in T[u]:\n                    stack.append((m, u, False))\n\n            \
    \    for v in T[u]:\n                    if v == p or m == v:\n              \
    \          continue\n                    stack.append((v, u, False))\n       \
    \     else:\n                for v in T[u]:\n                    if v != p:\n\
    \                        size[u] += size[v]\n        \n\n    for v in T[centroid]:\n\
    \        dfs(v, centroid)\n        if centroid ^ 1 == v:\n            matched\
    \ = (-size[v], v)\n        else:\n            heapq.heappush(heap, (-size[v],\
    \ v))\n\n    ops = []\n    while heap:\n        s, v = heapq.heappop(heap)\n \
    \       if dfs_order[v] and dfs_order[matched[1]]:\n            leaf1 = dfs_order[v].pop()\n\
    \            leaf2 = dfs_order[matched[1]].pop()\n            ops.append((leaf1,\
    \ leaf2))\n        else:\n            continue\n        if -matched[0] > 1:\n\
    \            heapq.heappush(heap, (matched[0] + 1, matched[1]))\n        matched\
    \ = (s + 1, v)\n\n    if matched[1] != -1:\n        ops.append((centroid, matched[1]))\n\
    \n    return ops\n\nfrom cp_library.alg.tree.find_centroid_recursive_fn import\
    \ find_centroid\nfrom cp_library.io.read_tree_fn import read_tree\nfrom cp_library.io.read_specs_fn\
    \ import read\n\nfor op in solve():\n    print(op[0] + 1, op[1] + 1)\n"
  dependsOn:
  - cp_library/alg/tree/find_centroid_recursive_fn.py
  - cp_library/io/read_tree_fn.py
  - cp_library/io/read_specs_fn.py
  - cp_library/misc/setrecursionlimit.py
  - cp_library/alg/graph/graph_cls.py
  - cp_library/io/parse_stream_fn.py
  - cp_library/alg/graph/edge_list_type.py
  - cp_library/io/parsable_cls.py
  isVerificationFile: true
  path: test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py
  requiredBy: []
  timestamp: '2024-09-20 02:31:14+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py
layout: document
redirect_from:
- /verify/test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py
- /verify/test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py.html
title: test/arc183_d_keep_perfectly_matched_centroid_recursive.test.py
---
