---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parsable_cls.py
    title: cp_library/io/parsable_cls.py
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/io/read_edges_fn.py
    title: cp_library/io/read_edges_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_edges_weighted_fn.py
    title: cp_library/io/read_edges_weighted_fn.py
  - icon: ':warning:'
    path: cp_library/io/read_graph_directed_fn.py
    title: cp_library/io/read_graph_directed_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_graph_fn.py
    title: cp_library/io/read_graph_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_graph_weighted_directed_fn.py
    title: cp_library/io/read_graph_weighted_directed_fn.py
  - icon: ':warning:'
    path: cp_library/io/read_graph_weighted_fn.py
    title: cp_library/io/read_graph_weighted_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_specs_fn.py
    title: cp_library/io/read_specs_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_tree_fn.py
    title: cp_library/io/read_tree_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/dp_v_subtree_rerooting_iterative.test.py
    title: test/dp_v_subtree_rerooting_iterative.test.py
  - icon: ':heavy_check_mark:'
    path: test/dp_v_subtree_rerooting_recursive.test.py
    title: test/dp_v_subtree_rerooting_recursive.test.py
  - icon: ':heavy_check_mark:'
    path: test/dp_z_cht_monotone_add_min.test.py
    title: test/dp_z_cht_monotone_add_min.test.py
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
    path: test/grl_2_a_kruskal_heap.test.py
    title: test/grl_2_a_kruskal_heap.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_2_a_kruskal_sort.test.py
    title: test/grl_2_a_kruskal_sort.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_2_b_edmonds_branching.test.py
    title: test/grl_2_b_edmonds_branching.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_3_a_tarjan_articulation_points.test.py
    title: test/grl_3_a_tarjan_articulation_points.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_5_c_lca_table_iterative.test.py
    title: test/grl_5_c_lca_table_iterative.test.py
  - icon: ':heavy_check_mark:'
    path: test/subset_convolution.test.py
    title: test/subset_convolution.test.py
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
    \nimport typing\nfrom collections import deque\nfrom numbers import Number\nfrom\
    \ typing import Collection, Iterator, Type, TypeVar\n\n\nclass Parsable:\n   \
    \ @classmethod\n    def parse(cls, parse_spec):\n        return parse_spec(lambda\
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
    \   \n    queue = deque() \n    return parse_spec(spec)\n"
  code: "import cp_library.io.__init__\n\nimport typing\nfrom collections import deque\n\
    from numbers import Number\nfrom typing import Collection, Iterator, Type, TypeVar\n\
    \nfrom cp_library.io.parsable_cls import Parsable\n\nT = TypeVar('T')\ndef parse_stream(stream:\
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
    \ \n    return parse_spec(spec)\n"
  dependsOn:
  - cp_library/io/parsable_cls.py
  isVerificationFile: false
  path: cp_library/io/parse_stream_fn.py
  requiredBy:
  - cp_library/io/read_graph_directed_fn.py
  - cp_library/io/read_tree_fn.py
  - cp_library/io/read_graph_weighted_directed_fn.py
  - cp_library/io/read_specs_fn.py
  - cp_library/io/read_graph_fn.py
  - cp_library/io/read_edges_weighted_fn.py
  - cp_library/io/read_edges_fn.py
  - cp_library/io/read_graph_weighted_fn.py
  timestamp: '2024-09-20 03:21:05+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/grl_2_a_kruskal_sort.test.py
  - test/subset_convolution.test.py
  - test/dp_v_subtree_rerooting_iterative.test.py
  - test/grl_5_c_lca_table_iterative.test.py
  - test/dp_v_subtree_rerooting_recursive.test.py
  - test/grl_2_b_edmonds_branching.test.py
  - test/dp_z_cht_monotone_add_min.test.py
  - test/grl_1_c_floyd_warshall.test.py
  - test/grl_3_a_tarjan_articulation_points.test.py
  - test/grl_1_a_dijkstra.test.py
  - test/grl_1_b_bellman_ford.test.py
  - test/grl_2_a_kruskal_heap.test.py
documentation_of: cp_library/io/parse_stream_fn.py
layout: document
redirect_from:
- /library/cp_library/io/parse_stream_fn.py
- /library/cp_library/io/parse_stream_fn.py.html
title: cp_library/io/parse_stream_fn.py
---
