---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_edges_weighted_fn.py
    title: cp_library/io/read_edges_weighted_fn.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/abc175_d_permutation.test.py
    title: test/abc175_d_permutation.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc184_e_grid_graph.test.py
    title: test/abc184_e_grid_graph.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc184_e_grid_graph_bfs_fn.test.py
    title: test/abc184_e_grid_graph_bfs_fn.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc184_f_subset_sum_fn.test.py
    title: test/abc184_f_subset_sum_fn.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc185_e_dp2d.test.py
    title: test/abc185_e_dp2d.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc186_e_gcd_ex.test.py
    title: test/abc186_e_gcd_ex.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc189_e_vec2d.test.py
    title: test/abc189_e_vec2d.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc245_f_digraph.test.py
    title: test/abc245_f_digraph.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc246_e_grid_direction_graph.test.py
    title: test/abc246_e_grid_direction_graph.test.py
  - icon: ':x:'
    path: test/abc261_g_mo.test.py
    title: test/abc261_g_mo.test.py
  - icon: ':x:'
    path: test/abc261_g_queries_mo.test.py
    title: test/abc261_g_queries_mo.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc274_e_vec2d.test.py
    title: test/abc274_e_vec2d.test.py
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
    path: test/abc361_e_tree_diameter.test.py
    title: test/abc361_e_tree_diameter.test.py
  - icon: ':heavy_check_mark:'
    path: test/abc375_g_find_bridges.test.py
    title: test/abc375_g_find_bridges.test.py
  - icon: ':heavy_check_mark:'
    path: test/agc038_b_sliding_min_max.test.py
    title: test/agc038_b_sliding_min_max.test.py
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
    path: test/grl_2_a_kruskal_sort.test.py
    title: test/grl_2_a_kruskal_sort.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_2_b_edmonds_branching.test.py
    title: test/grl_2_b_edmonds_branching.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_3_a_articulation_points_fn.test.py
    title: test/grl_3_a_articulation_points_fn.test.py
  - icon: ':heavy_check_mark:'
    path: test/grl_3_a_graph_articulation_points.test.py
    title: test/grl_3_a_graph_articulation_points.test.py
  - icon: ':heavy_check_mark:'
    path: test/subset_convolution.test.py
    title: test/subset_convolution.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':question:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \nimport sys\nfrom typing import Type, TypeVar, overload\nfrom io import TextIOBase\n\
    \nimport typing\nfrom collections import deque\nfrom numbers import Number\nfrom\
    \ types import GenericAlias \nfrom typing import Callable, Collection, Iterator,\
    \ TypeAlias, TypeVar\n\nclass TokenStream(Iterator):\n    def __init__(self, stream:\
    \ TextIOBase = sys.stdin):\n        self.queue = deque()\n        self.stream\
    \ = stream\n\n    def __next__(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        return self.queue.popleft()\n    \n    def wait(self):\n        if not\
    \ self.queue: self.queue.extend(self.line())\n        while self.queue: yield\n\
    \        \n    def line(self):\n        assert not self.queue\n        return\
    \ sys.stdin.readline().split()\n\n    def n_uints(self, n: int, shift = 0, max_digits:\
    \ int = 20):\n        # sync buffers\n        tokens: list[str] = []\n       \
    \ while (lim := sys.stdin.buffer.tell() - sys.stdin.tell()) and len(tokens) <\
    \ n:\n            residual_str: str = sys.stdin.readline(lim)\n            tokens.extend(residual_str.split())\n\
    \        \n        result = [0] * n\n        pos = 0\n        \n        # Process\
    \ residual string and check for partial token\n        partial = None\n      \
    \  if tokens:\n            if not residual_str[-1].isspace():\n              \
    \  partial = tokens.pop()\n            for pos, token in enumerate(tokens):\n\
    \                result[pos] = int(token)+shift\n            pos += 1\n      \
    \  # Process remaining data token by token\n        stdin_buffer = sys.stdin.buffer\n\
    \        num = int(partial) if partial else 0\n        have_digit = partial is\
    \ not None\n\n        original_chunk_size = sys.stdin._CHUNK_SIZE\n        sys.stdin._CHUNK_SIZE\
    \ = max(original_chunk_size, max_digits * (n - pos))\n        \n        while\
    \ pos < n:\n            byte = stdin_buffer.read(1)\n\n            match byte[0]:\n\
    \                case 10 | 32:\n                    if have_digit:\n         \
    \               result[pos] = num+shift\n                        pos += 1\n  \
    \                      num = 0\n                        have_digit = False\n \
    \               case char:  # digit\n                    num = (num * 10) + (char\
    \ - 48)\n                    have_digit = True\n\n        if have_digit:\n   \
    \         result[pos] = num+shift\n            pos += 1\n\n        sys.stdin._CHUNK_SIZE\
    \ = original_chunk_size \n        if pos < n:\n            raise EOFError(f\"\
    Only found {pos} numbers, expected {n}\")\n            \n        return result\n\
    \    \n    def n_ints(self, n: int, shift = 0, max_digits: int = 20):\n      \
    \  # sync buffers\n        tokens: list[str] = []\n        while (lim := sys.stdin.buffer.tell()\
    \ - sys.stdin.tell()) and len(tokens) < n:\n            residual_str: str = sys.stdin.readline(lim)\n\
    \            tokens.extend(residual_str.split())\n        \n        result = [0]\
    \ * n\n        pos = 0\n        \n        # Process residual string and check\
    \ for partial token\n        partial = None\n        if tokens:\n            if\
    \ not residual_str[-1].isspace():\n                partial = tokens.pop()\n  \
    \          for pos, token in enumerate(tokens):\n                result[pos] =\
    \ int(token)+shift\n            pos += 1\n        # Process remaining data token\
    \ by token\n        stdin_buffer = sys.stdin.buffer\n        num = abs(int(partial))\
    \ if partial else 0\n        is_negative = partial and partial.startswith('-')\n\
    \        have_digit = partial is not None\n\n        original_chunk_size = sys.stdin._CHUNK_SIZE\n\
    \        sys.stdin._CHUNK_SIZE = max(original_chunk_size, max_digits * (n - pos))\n\
    \        \n        while pos < n:\n            byte = stdin_buffer.read(1)\n\n\
    \            match byte[0]:\n                case 10 | 32:\n                 \
    \   if have_digit:\n                        result[pos] = -num+shift if is_negative\
    \ else num+shift\n                        pos += 1\n                        num\
    \ = 0\n                        is_negative = False\n                        have_digit\
    \ = False\n                case 45:  # minus sign\n                    is_negative\
    \ = True\n                case char:  # digit\n                    num = (num\
    \ * 10) + (char - 48)\n                    have_digit = True\n\n        if have_digit:\n\
    \            result[pos] = -num+shift if is_negative else num+shift\n        \
    \    pos += 1\n\n        sys.stdin._CHUNK_SIZE = original_chunk_size \n      \
    \  if pos < n:\n            raise EOFError(f\"Only found {pos} numbers, expected\
    \ {n}\")\n            \n        return result\n\nclass CharStream(TokenStream):\n\
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
    \ type[T]|T=int) -> ParseFn[T]:\n        if isinstance(spec, (type, GenericAlias)):\n\
    \            cls = typing.get_origin(spec) or spec\n            args = typing.get_args(spec)\
    \ or tuple()\n            return Parser.compile_type(cls, args)\n        elif\
    \ isinstance(offset := spec, Number): \n            cls = type(spec)  \n     \
    \       def parse(ts: TokenStream):\n                return cls(next(ts)) + offset\n\
    \            return parse\n        elif isinstance(args := spec, tuple):     \
    \ \n            return Parser.compile_tuple(type(spec), args)\n        elif isinstance(args\
    \ := spec, Collection):  \n            return Parser.compile_collection(type(spec),\
    \ args)\n        else:\n            raise NotImplementedError()\n    \n    @staticmethod\n\
    \    def compile_line(cls: T, spec=int) -> ParseFn[T]:\n        fn = Parser.compile(spec)\n\
    \        def parse(ts: TokenStream):\n            return cls(fn(ts) for _ in ts.wait())\n\
    \        return parse\n    \n    @staticmethod\n    def compile_n_ints(cls: T,\
    \ N, shift = int) -> ParseFn[T]:\n        shift = shift if isinstance(shift, int)\
    \ else 0\n        def parse(ts: TokenStream):\n            return cls(ts.n_ints(N,\
    \ shift))\n        return parse\n\n    @staticmethod\n    def compile_repeat(cls:\
    \ T, spec, N) -> ParseFn[T]:\n        fn = Parser.compile(spec)\n        def parse(ts:\
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
    \            case [spec, int() as N]:\n                if issubclass(spec, int)\
    \ or isinstance(spec, int):\n                    return Parser.compile_n_ints(cls,\
    \ N, spec)\n                return Parser.compile_repeat(cls, spec, N)\n     \
    \       case _:\n                raise NotImplementedError()\n\n        \nclass\
    \ Parsable:\n    @classmethod\n    def compile(cls):\n        def parser(ts: TokenStream):\n\
    \            return cls(next(ts))\n        return parser\n\nT = TypeVar('T')\n\
    @overload\ndef read(spec: int|None) -> list[int]: ...\n@overload\ndef read(spec:\
    \ Type[T]|T, char=False) -> T: ...\ndef read(spec: Type[T]|T=None, char=False):\n\
    \    match spec, char:\n        case None, False:\n            return list(map(int,\
    \ input().split()))\n        case int(offset), False:\n            return [int(s)+offset\
    \ for s in input().split()]\n        case _, _:\n            if char:\n      \
    \          stream = CharStream()\n            else:\n                stream =\
    \ TokenStream()\n            parser: T = Parser.compile(spec)\n            return\
    \ parser(stream)\n"
  code: "import cp_library.io.__header__\n\nimport sys\nfrom typing import Type, TypeVar,\
    \ overload\nfrom cp_library.io.parser_cls import Parser, TokenStream, CharStream\n\
    \nT = TypeVar('T')\n@overload\ndef read(spec: int|None) -> list[int]: ...\n@overload\n\
    def read(spec: Type[T]|T, char=False) -> T: ...\ndef read(spec: Type[T]|T=None,\
    \ char=False):\n    match spec, char:\n        case None, False:\n           \
    \ return list(map(int, input().split()))\n        case int(offset), False:\n \
    \           return [int(s)+offset for s in input().split()]\n        case _, _:\n\
    \            if char:\n                stream = CharStream()\n            else:\n\
    \                stream = TokenStream()\n            parser: T = Parser.compile(spec)\n\
    \            return parser(stream)\n"
  dependsOn:
  - cp_library/io/parser_cls.py
  isVerificationFile: false
  path: cp_library/io/read_specs_fn.py
  requiredBy:
  - cp_library/io/read_edges_weighted_fn.py
  timestamp: '2024-11-15 01:34:01+09:00'
  verificationStatus: LIBRARY_SOME_WA
  verifiedWith:
  - test/abc261_g_mo.test.py
  - test/abc184_f_subset_sum_fn.test.py
  - test/abc375_g_find_bridges.test.py
  - test/grl_1_b_bellman_ford.test.py
  - test/abc184_e_grid_graph.test.py
  - test/agc038_b_sliding_min_max.test.py
  - test/abc261_g_queries_mo.test.py
  - test/grl_2_a_kruskal_sort.test.py
  - test/grl_2_b_edmonds_branching.test.py
  - test/abc175_d_permutation.test.py
  - test/abc337_g_tree_inversion_heavy_light_decomposition.test.py
  - test/abc186_e_gcd_ex.test.py
  - test/abc184_e_grid_graph_bfs_fn.test.py
  - test/abc361_e_tree_diameter.test.py
  - test/abc246_e_grid_direction_graph.test.py
  - test/grl_3_a_articulation_points_fn.test.py
  - test/abc189_e_vec2d.test.py
  - test/abc245_f_digraph.test.py
  - test/abc274_e_vec2d.test.py
  - test/grl_3_a_graph_articulation_points.test.py
  - test/abc185_e_dp2d.test.py
  - test/abc294_g_dist_queries_on_a_tree_lca_table_weighted_bit.test.py
  - test/abc294_g_dist_queries_on_a_tree_heavy_light_decomposition.test.py
  - test/subset_convolution.test.py
  - test/dp_z_cht_monotone_add_min.test.py
  - test/grl_1_a_dijkstra.test.py
  - test/dp_v_subtree_rerooting_recursive.test.py
  - test/dp_v_subtree_rerooting_iterative.test.py
documentation_of: cp_library/io/read_specs_fn.py
layout: document
redirect_from:
- /library/cp_library/io/read_specs_fn.py
- /library/cp_library/io/read_specs_fn.py.html
title: cp_library/io/read_specs_fn.py
---
