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
    path: test/atcoder/abc/abc203_e_queries_grouped.test.py
    title: test/atcoder/abc/abc203_e_queries_grouped.test.py
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
    from types import GenericAlias\n\n\nclass Parsable:\n    @classmethod\n    def\
    \ compile(cls):\n        def parser(io: 'IOBase'): return cls(next(io))\n    \
    \    return parser\n    @classmethod\n    def __class_getitem__(cls, item): return\
    \ GenericAlias(cls, item)\nfrom itertools import groupby\nfrom typing import Iterable\n\
    \n\nclass Queries(list, Parsable):\n    def __init__(self, data: Iterable = []):\
    \ super().__init__((i,*query) for i,query in enumerate(data))\n    def append(self,\
    \ query) -> None: return super().append((len(self), *query))\n    @classmethod\n\
    \    def compile(cls, N: int, T: type = tuple[int, int]):\n        query = Parser.compile(T)\n\
    \        def parse(io: IOBase): return cls(query(io) for _ in range(N))\n    \
    \    return parse\n\nclass QueriesGrouped(Queries):\n    '''QueriesGrouped[Q:\
    \ int, key = 0, T: type = tuple[int, ...]]'''\n    def __init__(self, queries,\
    \ key = 0):\n        if isinstance(key, int):\n            group_idx = key+1\n\
    \            def wrap_key(row): return row[group_idx]\n        else:\n       \
    \     def wrap_key(row): _, *query = row; return key(query)\n        rows = sorted(((i,*query)\
    \ for i,query in enumerate(queries)), key = wrap_key)\n        groups = [(k, list(g))\
    \ for k, g in groupby(rows, key = wrap_key)]\n        groups.sort()\n        self.key\
    \ = key\n        list.__init__(self, groups)\n    @classmethod\n    def compile(cls,\
    \ Q: int, key = 0, T: type = tuple[int, ...]):\n        query = Parser.compile(T)\n\
    \        def parse(io: IOBase): return cls((query(io) for _ in range(Q)), key)\n\
    \        return parse\n\nclass QueriesRange(Queries):\n    '''QueriesRange[Q:\
    \ int, N: int, key = 0, T: type = tuple[-1, int]]'''\n    def __init__(self, queries,\
    \ N: int, key = 0):\n        if isinstance(key, int):\n            group_idx =\
    \ key+1\n            def wrap_key(row): return row[group_idx]\n        else:\n\
    \            def wrap_key(row): _, *query = row; return key(query)\n        rows\
    \ = list((i,*query) for i,query in enumerate(queries))\n        groups = [(k,[])\
    \ for k in range(N)]\n        for k, group in groupby(rows, key = wrap_key): groups[k][1].extend(group)\n\
    \        self.key = key\n        list.__init__(self, groups)\n    @classmethod\n\
    \    def compile(cls, Q: int, N: int, key = 0, T: type = tuple[-1, int]):\n  \
    \      query = Parser.compile(T)\n        def parse(io: IOBase):\n           \
    \ return cls((query(io) for _ in range(Q)), N, key)\n        return parse\n\n\
    class IOBase:\n    @property\n    def char(io) -> bool: ...\n    @property\n \
    \   def writable(io) -> bool: ...\n    def __next__(io) -> str: ...\n    def write(io,\
    \ s: str) -> None: ...\n    def readline(io) -> str: ...\n    def readtoken(io)\
    \ -> str: ...\n    def readtokens(io) -> list[str]: ...\n    def readints(io)\
    \ -> list[int]: ...\n    def readdigits(io) -> list[int]: ...\n    def readnums(io)\
    \ -> list[int]: ...\n    def readchar(io) -> str: ...\n    def readchars(io) ->\
    \ str: ...\n    def readinto(io, lst: list[str]) -> list[str]: ...\n    def readcharsinto(io,\
    \ lst: list[str]) -> list[str]: ...\n    def readtokensinto(io, lst: list[str])\
    \ -> list[str]: ...\n    def readintsinto(io, lst: list[int]) -> list[int]: ...\n\
    \    def readdigitsinto(io, lst: list[int]) -> list[int]: ...\n    def readnumsinto(io,\
    \ lst: list[int]) -> list[int]: ...\n    def wait(io): ...\n    def flush(io)\
    \ -> None: ...\n    def line(io) -> list[str]: ...\nimport typing\nfrom numbers\
    \ import Number\nfrom typing import Callable, Collection\n\nclass Parser:\n  \
    \  def __init__(self, spec):  self.parse = Parser.compile(spec)\n    def __call__(self,\
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
  code: "import cp_library.__header__\nfrom cp_library.io.parsable_cls import Parsable\n\
    from itertools import groupby\nfrom typing import Iterable\nimport cp_library.ds.__header__\n\
    \nclass Queries(list, Parsable):\n    def __init__(self, data: Iterable = []):\
    \ super().__init__((i,*query) for i,query in enumerate(data))\n    def append(self,\
    \ query) -> None: return super().append((len(self), *query))\n    @classmethod\n\
    \    def compile(cls, N: int, T: type = tuple[int, int]):\n        query = Parser.compile(T)\n\
    \        def parse(io: IOBase): return cls(query(io) for _ in range(N))\n    \
    \    return parse\n\nclass QueriesGrouped(Queries):\n    '''QueriesGrouped[Q:\
    \ int, key = 0, T: type = tuple[int, ...]]'''\n    def __init__(self, queries,\
    \ key = 0):\n        if isinstance(key, int):\n            group_idx = key+1\n\
    \            def wrap_key(row): return row[group_idx]\n        else:\n       \
    \     def wrap_key(row): _, *query = row; return key(query)\n        rows = sorted(((i,*query)\
    \ for i,query in enumerate(queries)), key = wrap_key)\n        groups = [(k, list(g))\
    \ for k, g in groupby(rows, key = wrap_key)]\n        groups.sort()\n        self.key\
    \ = key\n        list.__init__(self, groups)\n    @classmethod\n    def compile(cls,\
    \ Q: int, key = 0, T: type = tuple[int, ...]):\n        query = Parser.compile(T)\n\
    \        def parse(io: IOBase): return cls((query(io) for _ in range(Q)), key)\n\
    \        return parse\n\nclass QueriesRange(Queries):\n    '''QueriesRange[Q:\
    \ int, N: int, key = 0, T: type = tuple[-1, int]]'''\n    def __init__(self, queries,\
    \ N: int, key = 0):\n        if isinstance(key, int):\n            group_idx =\
    \ key+1\n            def wrap_key(row): return row[group_idx]\n        else:\n\
    \            def wrap_key(row): _, *query = row; return key(query)\n        rows\
    \ = list((i,*query) for i,query in enumerate(queries))\n        groups = [(k,[])\
    \ for k in range(N)]\n        for k, group in groupby(rows, key = wrap_key): groups[k][1].extend(group)\n\
    \        self.key = key\n        list.__init__(self, groups)\n    @classmethod\n\
    \    def compile(cls, Q: int, N: int, key = 0, T: type = tuple[-1, int]):\n  \
    \      query = Parser.compile(T)\n        def parse(io: IOBase):\n           \
    \ return cls((query(io) for _ in range(Q)), N, key)\n        return parse\nfrom\
    \ cp_library.io.io_base_cls import IOBase\nfrom cp_library.io.parser_cls import\
    \ Parser"
  dependsOn:
  - cp_library/io/parsable_cls.py
  - cp_library/io/io_base_cls.py
  - cp_library/io/parser_cls.py
  isVerificationFile: false
  path: cp_library/ds/queries_cls.py
  requiredBy: []
  timestamp: '2025-07-28 14:17:34+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/abc/abc203_e_queries_grouped.test.py
documentation_of: cp_library/ds/queries_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/queries_cls.py
- /library/cp_library/ds/queries_cls.py.html
title: cp_library/ds/queries_cls.py
---
