---
data:
  _extendedDependsOn:
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
    path: test/atcoder/abc/abc185_e_dp2d.test.py
    title: test/atcoder/abc/abc185_e_dp2d.test.py
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
    \nfrom typing import Generic, Container\nfrom types import GenericAlias\n\n\n\
    class Parsable:\n    @classmethod\n    def compile(cls):\n        def parser(io:\
    \ 'IOBase'): return cls(next(io))\n        return parser\n    @classmethod\n \
    \   def __class_getitem__(cls, item): return GenericAlias(cls, item)\nfrom dataclasses\
    \ import dataclass\nfrom math import inf\n\nfrom typing import TypeVar\n_S = TypeVar('S');\
    \ _T = TypeVar('T'); _U = TypeVar('U'); _T1 = TypeVar('T1'); _T2 = TypeVar('T2');\
    \ _T3 = TypeVar('T3'); _T4 = TypeVar('T4'); _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\
    \n@dataclass\nclass Transition2D(Generic[_T]):\n    di: int; dj: int\n    \n \
    \   def __call__(self, i: int, j: int, src: _T, dest: _T) -> _T:\n        '''Override\
    \ this to implement transition logic'''\n        return src  # Default no-op\n\
    \    \n    @classmethod\n    def make(cls, func):\n        class Transition(cls):\n\
    \            def __call__(self, i: int, j: int, src: _T, dest: _T) -> _T:\n  \
    \              return func(i,j,src,dest)\n        return Transition\n\nclass DynamicProgramming2D(Generic[_T],\
    \ Parsable, Container):\n    def __init__(self, rows: int, cols: int, default:\
    \ _T = inf):\n        self.rows = rows\n        self.cols = cols\n        self.table\
    \ = default if isinstance(default, list) else [[default] * cols for _ in range(rows)]\n\
    \    \n    def __getitem__(self, pos: tuple[int, int]) -> _T:\n        i, j =\
    \ pos\n        return self.table[i][j]\n    \n    def __setitem__(self, pos: tuple[int,\
    \ int], value: _T) -> None:\n        i, j = pos\n        self.table[i][j] = value\n\
    \n    def __contains__(self, x: object) -> bool:\n        return any(x in row\
    \ for row in self.table)\n    \n    def solve(self, transitions: list[Transition2D[_T]])\
    \ -> None:\n        for i in range(self.rows):\n            for j in range(self.cols):\n\
    \                curr_val = self.table[i][j]\n                for trans in transitions:\n\
    \                    ni, nj = i + trans.di, j + trans.dj\n                   \
    \ if 0 <= ni < self.rows and 0 <= nj < self.cols:\n                        self.table[ni][nj]\
    \ = trans(i, j, curr_val, self.table[ni][nj])\n    \n    @classmethod\n    def\
    \ compile(cls, N, M, T = int):\n        table = Parser.compile(list[list[T,M],N])\n\
    \        def parse(io: IOBase): return cls(N, M, table(io))\n        return parse\n\
    import typing\nfrom numbers import Number\nfrom typing import Callable, Collection\n\
    \nclass IOBase:\n    @property\n    def char(io) -> bool: ...\n    @property\n\
    \    def writable(io) -> bool: ...\n    def __next__(io) -> str: ...\n    def\
    \ write(io, s: str) -> None: ...\n    def readline(io) -> str: ...\n    def readtoken(io)\
    \ -> str: ...\n    def readtokens(io) -> list[str]: ...\n    def readints(io)\
    \ -> list[int]: ...\n    def readdigits(io) -> list[int]: ...\n    def readnums(io)\
    \ -> list[int]: ...\n    def readchar(io) -> str: ...\n    def readchars(io) ->\
    \ str: ...\n    def readinto(io, lst: list[str]) -> list[str]: ...\n    def readcharsinto(io,\
    \ lst: list[str]) -> list[str]: ...\n    def readtokensinto(io, lst: list[str])\
    \ -> list[str]: ...\n    def readintsinto(io, lst: list[int]) -> list[int]: ...\n\
    \    def readdigitsinto(io, lst: list[int]) -> list[int]: ...\n    def readnumsinto(io,\
    \ lst: list[int]) -> list[int]: ...\n    def wait(io): ...\n    def flush(io)\
    \ -> None: ...\n    def line(io) -> list[str]: ...\n\nclass Parser:\n    def __init__(self,\
    \ spec):  self.parse = Parser.compile(spec)\n    def __call__(self, io: IOBase):\
    \ return self.parse(io)\n    @staticmethod\n    def compile_type(cls, args = ()):\n\
    \        if issubclass(cls, Parsable): return cls.compile(*args)\n        elif\
    \ issubclass(cls, (Number, str)):\n            def parse(io: IOBase): return cls(next(io))\
    \              \n            return parse\n        elif issubclass(cls, tuple):\
    \ return Parser.compile_tuple(cls, args)\n        elif issubclass(cls, Collection):\
    \ return Parser.compile_collection(cls, args)\n        elif callable(cls):\n \
    \           def parse(io: IOBase): return cls(next(io))              \n      \
    \      return parse\n        else: raise NotImplementedError()\n    @staticmethod\n\
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
    \        elif spec is str:\n            def parse(io: IOBase): return cls(io.line())\n\
    \        else:\n            fn = Parser.compile(spec)\n            def parse(io:\
    \ IOBase): return cls((fn(io) for _ in io.wait()))\n        return parse\n   \
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
  code: "import cp_library.__header__\nimport cp_library.alg.__header__\nfrom typing\
    \ import Generic, Container\nfrom cp_library.io.parsable_cls import Parsable\n\
    from dataclasses import dataclass\nfrom math import inf\nimport cp_library.alg.dp.__header__\n\
    from cp_library.misc.typing import _T\n\n@dataclass\nclass Transition2D(Generic[_T]):\n\
    \    di: int; dj: int\n    \n    def __call__(self, i: int, j: int, src: _T, dest:\
    \ _T) -> _T:\n        '''Override this to implement transition logic'''\n    \
    \    return src  # Default no-op\n    \n    @classmethod\n    def make(cls, func):\n\
    \        class Transition(cls):\n            def __call__(self, i: int, j: int,\
    \ src: _T, dest: _T) -> _T:\n                return func(i,j,src,dest)\n     \
    \   return Transition\n\nclass DynamicProgramming2D(Generic[_T], Parsable, Container):\n\
    \    def __init__(self, rows: int, cols: int, default: _T = inf):\n        self.rows\
    \ = rows\n        self.cols = cols\n        self.table = default if isinstance(default,\
    \ list) else [[default] * cols for _ in range(rows)]\n    \n    def __getitem__(self,\
    \ pos: tuple[int, int]) -> _T:\n        i, j = pos\n        return self.table[i][j]\n\
    \    \n    def __setitem__(self, pos: tuple[int, int], value: _T) -> None:\n \
    \       i, j = pos\n        self.table[i][j] = value\n\n    def __contains__(self,\
    \ x: object) -> bool:\n        return any(x in row for row in self.table)\n  \
    \  \n    def solve(self, transitions: list[Transition2D[_T]]) -> None:\n     \
    \   for i in range(self.rows):\n            for j in range(self.cols):\n     \
    \           curr_val = self.table[i][j]\n                for trans in transitions:\n\
    \                    ni, nj = i + trans.di, j + trans.dj\n                   \
    \ if 0 <= ni < self.rows and 0 <= nj < self.cols:\n                        self.table[ni][nj]\
    \ = trans(i, j, curr_val, self.table[ni][nj])\n    \n    @classmethod\n    def\
    \ compile(cls, N, M, T = int):\n        table = Parser.compile(list[list[T,M],N])\n\
    \        def parse(io: IOBase): return cls(N, M, table(io))\n        return parse\n\
    from cp_library.io.parser_cls import Parser\nfrom cp_library.io.io_base_cls import\
    \ IOBase"
  dependsOn:
  - cp_library/io/parsable_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/io/io_base_cls.py
  isVerificationFile: false
  path: cp_library/alg/dp/dp2d_cls.py
  requiredBy: []
  timestamp: '2025-07-28 19:59:52+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/abc/abc185_e_dp2d.test.py
documentation_of: cp_library/alg/dp/dp2d_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/dp/dp2d_cls.py
- /library/cp_library/alg/dp/dp2d_cls.py.html
title: cp_library/alg/dp/dp2d_cls.py
---
