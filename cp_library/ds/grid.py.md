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
    from math import prod\nfrom typing import Container, Iterable\nfrom types import\
    \ GenericAlias\n\n\nclass Parsable:\n    @classmethod\n    def compile(cls):\n\
    \        def parser(io: 'IOBase'): return cls(next(io))\n        return parser\n\
    \    @classmethod\n    def __class_getitem__(cls, item): return GenericAlias(cls,\
    \ item)\n\nclass grid2d(Parsable, Container):\n\n    def __init__(self, shape:\
    \ tuple[int, int], data = 0):\n        self.shape = shape\n        self.size =\
    \ prod(shape)\n        if isinstance(data, Iterable) and not isinstance(data,\
    \ str):\n            self.data = list(elm for row in data for elm in row)\n  \
    \      else:\n            self.data = [data] * (self.size)\n    \n    @classmethod\n\
    \    def compile(cls, shape: tuple[int, int], T: type = int):\n        elm = Parser.compile(T)\n\
    \        def parse(io: IOBase):\n            obj = cls.__new__(cls)\n        \
    \    obj.shape = shape\n            obj.size = prod(shape)\n            obj.data\
    \ = list(elm(io) for _ in range(obj.size))\n            return obj\n        return\
    \ parse\n    \n    def __contains__(self, x: object) -> bool:\n        return\
    \ x in self.data\n    \n    def __getitem__(self, key: tuple[int, int]):\n   \
    \     i, j = key\n        return self.data[i * self.shape[1] + j]\n    \n    def\
    \ __setitem__(self, key: tuple[int, int], value):\n        i, j = key\n      \
    \  self.data[i * self.shape[1] + j] = value\n    \n    def __repr__(self) -> str:\n\
    \        (N, M), data = self.shape, self.data\n        return '\\n'.join(' '.join(str(data[j])\
    \ for j in range(i,i+M)) for i in range(0,N*M,M))\nimport typing\nfrom numbers\
    \ import Number\nfrom typing import Callable, Collection\n\nclass IOBase:\n  \
    \  @property\n    def char(io) -> bool: ...\n    @property\n    def writable(io)\
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
  code: "import cp_library.ds.__header__\nfrom math import prod\nfrom typing import\
    \ Container, Iterable\nfrom cp_library.io.parsable_cls import Parsable\n\nclass\
    \ grid2d(Parsable, Container):\n\n    def __init__(self, shape: tuple[int, int],\
    \ data = 0):\n        self.shape = shape\n        self.size = prod(shape)\n  \
    \      if isinstance(data, Iterable) and not isinstance(data, str):\n        \
    \    self.data = list(elm for row in data for elm in row)\n        else:\n   \
    \         self.data = [data] * (self.size)\n    \n    @classmethod\n    def compile(cls,\
    \ shape: tuple[int, int], T: type = int):\n        elm = Parser.compile(T)\n \
    \       def parse(io: IOBase):\n            obj = cls.__new__(cls)\n         \
    \   obj.shape = shape\n            obj.size = prod(shape)\n            obj.data\
    \ = list(elm(io) for _ in range(obj.size))\n            return obj\n        return\
    \ parse\n    \n    def __contains__(self, x: object) -> bool:\n        return\
    \ x in self.data\n    \n    def __getitem__(self, key: tuple[int, int]):\n   \
    \     i, j = key\n        return self.data[i * self.shape[1] + j]\n    \n    def\
    \ __setitem__(self, key: tuple[int, int], value):\n        i, j = key\n      \
    \  self.data[i * self.shape[1] + j] = value\n    \n    def __repr__(self) -> str:\n\
    \        (N, M), data = self.shape, self.data\n        return '\\n'.join(' '.join(str(data[j])\
    \ for j in range(i,i+M)) for i in range(0,N*M,M))\nfrom cp_library.io.parser_cls\
    \ import Parser\nfrom cp_library.io.io_base_cls import IOBase"
  dependsOn:
  - cp_library/io/parsable_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/io/io_base_cls.py
  isVerificationFile: false
  path: cp_library/ds/grid.py
  requiredBy: []
  timestamp: '2025-07-28 19:59:52+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/grid.py
layout: document
redirect_from:
- /library/cp_library/ds/grid.py
- /library/cp_library/ds/grid.py.html
title: cp_library/ds/grid.py
---
