---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/io_base_cls.py
    title: cp_library/io/io_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    import typing\nfrom numbers import Number\nfrom types import GenericAlias \nfrom\
    \ typing import Callable, Collection\n\n\nclass IOBase:\n    @property\n    def\
    \ char(io) -> bool: ...\n    @property\n    def writable(io) -> bool: ...\n  \
    \  def __next__(io) -> str: ...\n    def write(io, s: str) -> None: ...\n    def\
    \ readline(io) -> str: ...\n    def readtoken(io) -> str: ...\n    def readtokens(io)\
    \ -> list[str]: ...\n    def readints(io) -> list[int]: ...\n    def readdigits(io)\
    \ -> list[int]: ...\n    def readnums(io) -> list[int]: ...\n    def readchar(io)\
    \ -> str: ...\n    def readchars(io) -> str: ...\n    def readinto(io, lst: list[str])\
    \ -> list[str]: ...\n    def readcharsinto(io, lst: list[str]) -> list[str]: ...\n\
    \    def readtokensinto(io, lst: list[str]) -> list[str]: ...\n    def readintsinto(io,\
    \ lst: list[int]) -> list[int]: ...\n    def readdigitsinto(io, lst: list[int])\
    \ -> list[int]: ...\n    def readnumsinto(io, lst: list[int]) -> list[int]: ...\n\
    \    def wait(io): ...\n    def flush(io) -> None: ...\n    def line(io) -> list[str]:\
    \ ...\n\nclass Parser:\n    def __init__(self, spec):  self.parse = Parser.compile(spec)\n\
    \    def __call__(self, io: IOBase): return self.parse(io)\n    @staticmethod\n\
    \    def compile_type(cls, args = ()):\n        if issubclass(cls, Parsable):\
    \ return cls.compile(*args)\n        elif issubclass(cls, (Number, str)):\n  \
    \          def parse(io: IOBase): return cls(next(io))              \n       \
    \     return parse\n        elif issubclass(cls, tuple): return Parser.compile_tuple(cls,\
    \ args)\n        elif issubclass(cls, Collection): return Parser.compile_collection(cls,\
    \ args)\n        elif callable(cls):\n            def parse(io: IOBase): return\
    \ cls(next(io))              \n            return parse\n        else: raise NotImplementedError()\n\
    \    @staticmethod\n    def compile(spec=int):\n        if isinstance(spec, (type,\
    \ GenericAlias)):\n            cls, args = typing.get_origin(spec) or spec, typing.get_args(spec)\
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
    \        else:\n            raise NotImplementedError()\nclass Parsable:\n   \
    \ @classmethod\n    def compile(cls):\n        def parser(io: IOBase): return\
    \ cls(next(io))\n        return parser\n    @classmethod\n    def __class_getitem__(cls,\
    \ item): return GenericAlias(cls, item)\n\n\n\nclass EdgeList(Parsable):\n   \
    \ def __init__(E, N, U, V): E.N, E.M, E.U, E.V = N, len(U), U, V\n    def __len__(E):\
    \ return E.M\n    def __getitem__(E, e): return E.U[e], E.V[e]\n    @classmethod\n\
    \    def compile(cls, N: int, M: int, I: int = -1):\n        def parse(io: IOBase):\n\
    \            U, V = [0]*M, [0]*M\n            for e in range(M): u, v = io.readints();\
    \ U[e], V[e] = u+I, v+I\n            return cls(N, U, V)\n        return parse\n\
    \    def sub(E, I: list[int]):\n        U, V = elist(E.N-1), elist(E.N-1)\n  \
    \      for e in I: U.append(E.U[e]); V.append(E.V[e])\n        return E.__class__(E.N,\
    \ U, V)\n\n\ndef elist(est_len: int) -> list: ...\ntry:\n    from __pypy__ import\
    \ newlist_hint\nexcept:\n    def newlist_hint(hint):\n        return []\nelist\
    \ = newlist_hint\n    \n"
  code: "import cp_library.__header__\nfrom cp_library.io.parser_cls import Parsable,\
    \ IOBase\nimport cp_library.alg.__header__\nimport cp_library.alg.graph.__header__\n\
    \nclass EdgeList(Parsable):\n    def __init__(E, N, U, V): E.N, E.M, E.U, E.V\
    \ = N, len(U), U, V\n    def __len__(E): return E.M\n    def __getitem__(E, e):\
    \ return E.U[e], E.V[e]\n    @classmethod\n    def compile(cls, N: int, M: int,\
    \ I: int = -1):\n        def parse(io: IOBase):\n            U, V = [0]*M, [0]*M\n\
    \            for e in range(M): u, v = io.readints(); U[e], V[e] = u+I, v+I\n\
    \            return cls(N, U, V)\n        return parse\n    def sub(E, I: list[int]):\n\
    \        U, V = elist(E.N-1), elist(E.N-1)\n        for e in I: U.append(E.U[e]);\
    \ V.append(E.V[e])\n        return E.__class__(E.N, U, V)\nfrom cp_library.ds.elist_fn\
    \ import elist"
  dependsOn:
  - cp_library/io/parser_cls.py
  - cp_library/ds/elist_fn.py
  - cp_library/io/io_base_cls.py
  isVerificationFile: false
  path: cp_library/alg/graph/edge/edge_list_cls.py
  requiredBy: []
  timestamp: '2025-07-28 10:42:29+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/graph/edge/edge_list_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/edge/edge_list_cls.py
- /library/cp_library/alg/graph/edge/edge_list_cls.py.html
title: cp_library/alg/graph/edge/edge_list_cls.py
---
