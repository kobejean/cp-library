---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge/edge_cls.py
    title: cp_library/alg/graph/edge/edge_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/ctz32_fn.py
    title: cp_library/bit/ctz32_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/popcnt32_fn.py
    title: cp_library/bit/popcnt32_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/io_base_cls.py
    title: cp_library/io/io_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parsable_cls.py
    title: cp_library/io/parsable_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/graph/chromatic_number.test.py
    title: test/library-checker/graph/chromatic_number.test.py
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
    from typing import Union\nfrom types import GenericAlias\n\n\nclass Parsable:\n\
    \    @classmethod\n    def compile(cls):\n        def parser(io: 'IOBase'): return\
    \ cls(next(io))\n        return parser\n    @classmethod\n    def __class_getitem__(cls,\
    \ item): return GenericAlias(cls, item)\n\n\n\n\nclass Edge(tuple, Parsable):\n\
    \    @classmethod\n    def compile(cls, I=-1):\n        def parse(io: IOBase):\
    \ u, v = io.readints(); return cls((u+I,v+I))\n        return parse\n\nclass IOBase:\n\
    \    @property\n    def char(io) -> bool: ...\n    @property\n    def writable(io)\
    \ -> bool: ...\n    def __next__(io) -> str: ...\n    def write(io, s: str) ->\
    \ None: ...\n    def readline(io) -> str: ...\n    def readtoken(io) -> str: ...\n\
    \    def readtokens(io) -> list[str]: ...\n    def readints(io) -> list[int]:\
    \ ...\n    def readdigits(io) -> list[int]: ...\n    def readnums(io) -> list[int]:\
    \ ...\n    def readchar(io) -> str: ...\n    def readchars(io) -> str: ...\n \
    \   def readinto(io, lst: list[str]) -> list[str]: ...\n    def readcharsinto(io,\
    \ lst: list[str]) -> list[str]: ...\n    def readtokensinto(io, lst: list[str])\
    \ -> list[str]: ...\n    def readintsinto(io, lst: list[int]) -> list[int]: ...\n\
    \    def readdigitsinto(io, lst: list[int]) -> list[int]: ...\n    def readnumsinto(io,\
    \ lst: list[int]) -> list[int]: ...\n    def wait(io): ...\n    def flush(io)\
    \ -> None: ...\n    def line(io) -> list[str]: ...\n\nclass BitGraph(list, Parsable):\n\
    \    def __init__(G, N: int, E: list['Edge']=[]):\n        super().__init__([0]*N)\n\
    \        G.E, G.N, G.M = E, N, len(E)\n        for u, v in E: G[u] |= 1 << v;\
    \ G[v] |= 1 << u\n\n    def to_complement(G):\n        full = (1 << G.N) - 1\n\
    \        for u in range(G.N): G[u] = full ^ G[u]\n\n    def chromatic_number(G):\n\
    \        Z = 1 << (N := len(G))\n        I, coef = [0]*Z, [1]*Z; I[0] = 1\n  \
    \      for S in range(1, Z):\n            T = 1 << (v := ctz32(S)) ^ S\n     \
    \       I[S] = I[T] + I[T & ~G[v]]\n            coef[S] = -1 if popcnt32(S) &\
    \ 1 else 1\n        for k in range(1, N):\n            Pk = 0\n            for\
    \ S in range(Z): coef[S] *= I[S]; Pk += coef[S]\n            if Pk != 0: return\
    \ k\n        return N\n\n    @classmethod\n    def compile(cls, N: int, M: int,\
    \ E: Union[type,int] = Edge[-1]):\n        if isinstance(E, int): E = Edge[E]\n\
    \        edge = Parser.compile(E)\n        def parse(io: IOBase): return cls(N,\
    \ [edge(io) for _ in range(M)])\n        return parse\n\n\ndef popcnt32(x):\n\
    \    x = ((x >> 1)  & 0x55555555) + (x & 0x55555555)\n    x = ((x >> 2)  & 0x33333333)\
    \ + (x & 0x33333333)\n    x = ((x >> 4)  & 0x0f0f0f0f) + (x & 0x0f0f0f0f)\n  \
    \  x = ((x >> 8)  & 0x00ff00ff) + (x & 0x00ff00ff)\n    x = ((x >> 16) & 0x0000ffff)\
    \ + (x & 0x0000ffff)\n    return x\nif hasattr(int, 'bit_count'):\n    popcnt32\
    \ = int.bit_count\n\ndef ctz32(x): return popcnt32(~x&(x-1))\nimport typing\n\
    from numbers import Number\nfrom typing import Callable, Collection\n\nclass Parser:\n\
    \    def __init__(self, spec):  self.parse = Parser.compile(spec)\n    def __call__(self,\
    \ io: IOBase): return self.parse(io)\n    @staticmethod\n    def compile_type(cls,\
    \ args = ()):\n        if issubclass(cls, Parsable): return cls.compile(*args)\n\
    \        elif issubclass(cls, (Number, str)):\n            def parse(io: IOBase):\
    \ return cls(next(io))              \n            return parse\n        elif issubclass(cls,\
    \ tuple): return Parser.compile_tuple(cls, args)\n        elif issubclass(cls,\
    \ Collection): return Parser.compile_collection(cls, args)\n        elif callable(cls):\n\
    \            def parse(io: IOBase): return cls(next(io))              \n     \
    \       return parse\n        else: raise NotImplementedError()\n    @staticmethod\n\
    \    def compile(spec=int):\n        if isinstance(spec, (type, GenericAlias)):\n\
    \            cls, args = typing.get_origin(spec) or spec, typing.get_args(spec)\
    \ or tuple()\n            return Parser.compile_type(cls, args)\n        elif\
    \ isinstance(offset := spec, Number): \n            cls = type(spec)  \n     \
    \       def parse(io: IOBase): return cls(next(io)) + offset\n            return\
    \ parse\n        elif isinstance(args := spec, tuple): return Parser.compile_tuple(type(spec),\
    \ args)\n        elif isinstance(args := spec, Collection): return Parser.compile_collection(type(spec),\
    \ args)\n        elif isinstance(fn := spec, Callable): \n            def parse(io:\
    \ IOBase): return fn(next(io))\n            return parse\n        else: raise\
    \ NotImplementedError()\n    @staticmethod\n    def compile_line(cls, spec=int):\n\
    \        if spec is int:\n            def parse(io: IOBase): return cls(io.readnums())\n\
    \        else:\n            fn = Parser.compile(spec)\n            def parse(io:\
    \ IOBase): return cls([fn(io) for _ in io.wait()])\n        return parse\n   \
    \ @staticmethod\n    def compile_repeat(cls, spec, N):\n        fn = Parser.compile(spec)\n\
    \        def parse(io: IOBase): return cls([fn(io) for _ in range(N)])\n     \
    \   return parse\n    @staticmethod\n    def compile_children(cls, specs):\n \
    \       fns = tuple((Parser.compile(spec) for spec in specs))\n        def parse(io:\
    \ IOBase): return cls([fn(io) for fn in fns])  \n        return parse\n    @staticmethod\n\
    \    def compile_tuple(cls, specs):\n        if isinstance(specs, (tuple,list))\
    \ and len(specs) == 2 and specs[1] is ...: return Parser.compile_line(cls, specs[0])\n\
    \        else: return Parser.compile_children(cls, specs)\n    @staticmethod\n\
    \    def compile_collection(cls, specs):\n        if not specs or len(specs) ==\
    \ 1 or isinstance(specs, set):\n            return Parser.compile_line(cls, *specs)\n\
    \        elif (isinstance(specs, (tuple,list)) and len(specs) == 2 and isinstance(specs[1],\
    \ int)):\n            return Parser.compile_repeat(cls, specs[0], specs[1])\n\
    \        else:\n            raise NotImplementedError()\n"
  code: "import cp_library.__header__\nfrom typing import Union\nfrom cp_library.io.parsable_cls\
    \ import Parsable\nimport cp_library.alg.__header__\nimport cp_library.alg.graph.__header__\n\
    import cp_library.alg.graph.bit.__header__\nfrom cp_library.alg.graph.edge.edge_cls\
    \ import Edge\n\nclass BitGraph(list, Parsable):\n    def __init__(G, N: int,\
    \ E: list['Edge']=[]):\n        super().__init__([0]*N)\n        G.E, G.N, G.M\
    \ = E, N, len(E)\n        for u, v in E: G[u] |= 1 << v; G[v] |= 1 << u\n\n  \
    \  def to_complement(G):\n        full = (1 << G.N) - 1\n        for u in range(G.N):\
    \ G[u] = full ^ G[u]\n\n    def chromatic_number(G):\n        Z = 1 << (N := len(G))\n\
    \        I, coef = [0]*Z, [1]*Z; I[0] = 1\n        for S in range(1, Z):\n   \
    \         T = 1 << (v := ctz32(S)) ^ S\n            I[S] = I[T] + I[T & ~G[v]]\n\
    \            coef[S] = -1 if popcnt32(S) & 1 else 1\n        for k in range(1,\
    \ N):\n            Pk = 0\n            for S in range(Z): coef[S] *= I[S]; Pk\
    \ += coef[S]\n            if Pk != 0: return k\n        return N\n\n    @classmethod\n\
    \    def compile(cls, N: int, M: int, E: Union[type,int] = Edge[-1]):\n      \
    \  if isinstance(E, int): E = Edge[E]\n        edge = Parser.compile(E)\n    \
    \    def parse(io: IOBase): return cls(N, [edge(io) for _ in range(M)])\n    \
    \    return parse\nfrom cp_library.bit.popcnt32_fn import popcnt32\nfrom cp_library.bit.ctz32_fn\
    \ import ctz32\nfrom cp_library.io.io_base_cls import IOBase\nfrom cp_library.io.parser_cls\
    \ import Parser"
  dependsOn:
  - cp_library/io/parsable_cls.py
  - cp_library/alg/graph/edge/edge_cls.py
  - cp_library/bit/popcnt32_fn.py
  - cp_library/bit/ctz32_fn.py
  - cp_library/io/io_base_cls.py
  - cp_library/io/parser_cls.py
  isVerificationFile: false
  path: cp_library/alg/graph/bit/bit_graph_cls.py
  requiredBy: []
  timestamp: '2025-07-28 14:11:54+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/graph/chromatic_number.test.py
documentation_of: cp_library/alg/graph/bit/bit_graph_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/bit/bit_graph_cls.py
- /library/cp_library/alg/graph/bit/bit_graph_cls.py.html
title: cp_library/alg/graph/bit/bit_graph_cls.py
---
