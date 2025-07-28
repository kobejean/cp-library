---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/io/io_base_cls.py
    title: cp_library/io/io_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parsable_cls.py
    title: cp_library/io/parsable_cls.py
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
    from types import GenericAlias\n\n\nclass Parsable:\n    @classmethod\n    def\
    \ compile(cls):\n        def parser(io: 'IOBase'): return cls(next(io))\n    \
    \    return parser\n    @classmethod\n    def __class_getitem__(cls, item): return\
    \ GenericAlias(cls, item)\n\nclass ParallelRange(tuple, Parsable):\n    def __new__(cls,\
    \ N): return super().__new__(cls, ([0]*N, [0]*N))\n    @classmethod\n    def compile(cls,\
    \ N: int):\n        def parse(io: IOBase):\n            L, R = P = cls(N)\n  \
    \          for i in range(N): l, r = io.readints(); L[i], R[i] = l-1, r\n    \
    \        return P\n        return parse\n\nclass IOBase:\n    @property\n    def\
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
    \ ...\n"
  code: "import cp_library.ds.__header__\nfrom cp_library.io.parsable_cls import Parsable\n\
    \nclass ParallelRange(tuple, Parsable):\n    def __new__(cls, N): return super().__new__(cls,\
    \ ([0]*N, [0]*N))\n    @classmethod\n    def compile(cls, N: int):\n        def\
    \ parse(io: IOBase):\n            L, R = P = cls(N)\n            for i in range(N):\
    \ l, r = io.readints(); L[i], R[i] = l-1, r\n            return P\n        return\
    \ parse\nfrom cp_library.io.io_base_cls import IOBase"
  dependsOn:
  - cp_library/io/parsable_cls.py
  - cp_library/io/io_base_cls.py
  isVerificationFile: false
  path: cp_library/ds/parallel_range_cls.py
  requiredBy: []
  timestamp: '2025-07-28 14:17:34+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/parallel_range_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/parallel_range_cls.py
- /library/cp_library/ds/parallel_range_cls.py.html
title: cp_library/ds/parallel_range_cls.py
---
