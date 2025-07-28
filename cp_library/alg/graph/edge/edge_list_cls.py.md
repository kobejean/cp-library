---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/elist_fn.py
    title: cp_library/ds/list/elist_fn.py
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
    \ GenericAlias(cls, item)\n\nclass IOBase:\n    @property\n    def char(io) ->\
    \ bool: ...\n    @property\n    def writable(io) -> bool: ...\n    def __next__(io)\
    \ -> str: ...\n    def write(io, s: str) -> None: ...\n    def readline(io) ->\
    \ str: ...\n    def readtoken(io) -> str: ...\n    def readtokens(io) -> list[str]:\
    \ ...\n    def readints(io) -> list[int]: ...\n    def readdigits(io) -> list[int]:\
    \ ...\n    def readnums(io) -> list[int]: ...\n    def readchar(io) -> str: ...\n\
    \    def readchars(io) -> str: ...\n    def readinto(io, lst: list[str]) -> list[str]:\
    \ ...\n    def readcharsinto(io, lst: list[str]) -> list[str]: ...\n    def readtokensinto(io,\
    \ lst: list[str]) -> list[str]: ...\n    def readintsinto(io, lst: list[int])\
    \ -> list[int]: ...\n    def readdigitsinto(io, lst: list[int]) -> list[int]:\
    \ ...\n    def readnumsinto(io, lst: list[int]) -> list[int]: ...\n    def wait(io):\
    \ ...\n    def flush(io) -> None: ...\n    def line(io) -> list[str]: ...\n\n\n\
    \nclass EdgeList(Parsable):\n    def __init__(E, N, U, V): E.N, E.M, E.U, E.V\
    \ = N, len(U), U, V\n    def __len__(E): return E.M\n    def __getitem__(E, e):\
    \ return E.U[e], E.V[e]\n    @classmethod\n    def compile(cls, N: int, M: int,\
    \ I: int = -1):\n        def parse(io: IOBase):\n            U, V = [0]*M, [0]*M\n\
    \            for e in range(M): u, v = io.readints(); U[e], V[e] = u+I, v+I\n\
    \            return cls(N, U, V)\n        return parse\n    def sub(E, I: list[int]):\n\
    \        U, V = elist(E.N-1), elist(E.N-1)\n        for e in I: U.append(E.U[e]);\
    \ V.append(E.V[e])\n        return E.__class__(E.N, U, V)\n\n\ndef elist(est_len:\
    \ int) -> list: ...\ntry:\n    from __pypy__ import newlist_hint\nexcept:\n  \
    \  def newlist_hint(hint):\n        return []\nelist = newlist_hint\n    \n"
  code: "import cp_library.__header__\nfrom cp_library.io.parsable_cls import Parsable\n\
    from cp_library.io.io_base_cls import IOBase\nimport cp_library.alg.__header__\n\
    import cp_library.alg.graph.__header__\n\nclass EdgeList(Parsable):\n    def __init__(E,\
    \ N, U, V): E.N, E.M, E.U, E.V = N, len(U), U, V\n    def __len__(E): return E.M\n\
    \    def __getitem__(E, e): return E.U[e], E.V[e]\n    @classmethod\n    def compile(cls,\
    \ N: int, M: int, I: int = -1):\n        def parse(io: IOBase):\n            U,\
    \ V = [0]*M, [0]*M\n            for e in range(M): u, v = io.readints(); U[e],\
    \ V[e] = u+I, v+I\n            return cls(N, U, V)\n        return parse\n   \
    \ def sub(E, I: list[int]):\n        U, V = elist(E.N-1), elist(E.N-1)\n     \
    \   for e in I: U.append(E.U[e]); V.append(E.V[e])\n        return E.__class__(E.N,\
    \ U, V)\nfrom cp_library.ds.list.elist_fn import elist"
  dependsOn:
  - cp_library/io/parsable_cls.py
  - cp_library/io/io_base_cls.py
  - cp_library/ds/list/elist_fn.py
  isVerificationFile: false
  path: cp_library/alg/graph/edge/edge_list_cls.py
  requiredBy: []
  timestamp: '2025-07-28 19:59:52+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/alg/graph/edge/edge_list_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/edge/edge_list_cls.py
- /library/cp_library/alg/graph/edge/edge_list_cls.py.html
title: cp_library/alg/graph/edge/edge_list_cls.py
---
