---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/func/func_graph_cls.py
    title: cp_library/alg/graph/func/func_graph_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/crf_list_cls.py
    title: cp_library/alg/iter/crf_list_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/roll_fn.py
    title: cp_library/alg/iter/roll_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/array/u8f_fn.py
    title: cp_library/ds/array/u8f_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/elist_fn.py
    title: cp_library/ds/list/elist_fn.py
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
    path: test/atcoder/abc/abc175_d_permutation.test.py
    title: test/atcoder/abc/abc175_d_permutation.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/agc/agc038_b_sliding_min_max.test.py
    title: test/atcoder/agc/agc038_b_sliding_min_max.test.py
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
    \n\nfrom types import GenericAlias\n\n\nclass Parsable:\n    @classmethod\n  \
    \  def compile(cls):\n        def parser(io: 'IOBase'): return cls(next(io))\n\
    \        return parser\n    @classmethod\n    def __class_getitem__(cls, item):\
    \ return GenericAlias(cls, item)\n\nclass FuncGraph(list[int], Parsable):\n  \
    \  def __init__(F, successors):\n        super().__init__(successors)\n      \
    \  F.N = F.M = len(F)\n\n    def find_cycle(P, root: int) -> list[int]:\n    \
    \    slow = fast = root\n        while (slow := P[slow]) != (fast := P[P[fast]]):\
    \ pass\n        cyc = [slow]\n        while P[slow] != fast: cyc.append(slow :=\
    \ P[slow])\n        return cyc\n    \n    def cycles(P) -> 'CRFList[int]':\n \
    \       vis, cycs, S = u8f(N := P.N), elist(N), elist(N)\n        for v in range(P.N):\n\
    \            if vis[v]: continue\n            slow = fast = v\n            while\
    \ (slow := P[slow]) != (fast := P[P[fast]]) and not vis[fast]: pass\n        \
    \    if vis[fast]: continue\n            S.append(len(cycs))\n            cycs.append(slow)\n\
    \            vis[slow := P[slow]] = 1\n            while slow != fast:\n     \
    \           cycs.append(slow)\n                vis[slow := P[slow]] = 1\n    \
    \    return CRFList(cycs, S)\n    \n    def chain(P, root):\n        cyc = P.find_cycle(root)\n\
    \        slow, fast = root, cyc[0]\n        if slow == fast: return [], cyc\n\
    \        line = [slow]\n        while (slow := P[slow]) != (fast := P[fast]):\n\
    \            line.append(slow)\n        return line, roll(cyc, -cyc.index(slow))\n\
    \n    @classmethod\n    def compile(cls, N: int, shift = -1):\n        return\
    \ Parser.compile_repeat(cls, shift, N)\nfrom typing import Generic\nfrom typing\
    \ import TypeVar\n_S = TypeVar('S'); _T = TypeVar('T'); _U = TypeVar('U'); _T1\
    \ = TypeVar('T1'); _T2 = TypeVar('T2'); _T3 = TypeVar('T3'); _T4 = TypeVar('T4');\
    \ _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\n\nclass CRFList(Generic[_T]):\n\
    \    def __init__(crf, A: list[_T], S: list[int]):\n        crf.N, crf.A, crf.S\
    \ = len(S), A, S\n        S.append(len(A))\n\n    def __len__(crf) -> int: return\
    \ crf.N\n\n    def __getitem__(crf, i: int) -> list[_T]:\n        return crf.A[crf.S[i]:crf.S[i+1]]\n\
    \    \n    def get(crf, i: int, j: int) -> _T:\n        return crf.A[crf.S[i]+j]\n\
    \    \n    def len(crf, i: int) -> int:\n        return crf.S[i+1] - crf.S[i]\n\
    \ndef roll(A: list, t: int):\n    if t:=t%len(A): A[:t], A[t:] = A[-t:], A[:-t]\n\
    \    return A\n\n\nfrom array import array\ndef u8f(N: int, elm: int = 0):   \
    \   return array('B', (elm,))*N  # unsigned char\n\n\ndef elist(est_len: int)\
    \ -> list: ...\ntry:\n    from __pypy__ import newlist_hint\nexcept:\n    def\
    \ newlist_hint(hint):\n        return []\nelist = newlist_hint\n    \nimport typing\n\
    from numbers import Number\nfrom typing import Callable, Collection\n\nclass IOBase:\n\
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
    \        else:\n            raise NotImplementedError()\n\nclass PermGraph(FuncGraph):\n\
    \    def inv(P):\n        Pinv = [0]*P.N\n        for i,p in enumerate(P):\n \
    \           Pinv[p] = i\n        return type(P)(Pinv)\n"
  code: "import cp_library.__header__\nimport cp_library.alg.__header__\nimport cp_library.alg.graph.__header__\n\
    from cp_library.alg.graph.func.func_graph_cls import FuncGraph\n\nclass PermGraph(FuncGraph):\n\
    \    def inv(P):\n        Pinv = [0]*P.N\n        for i,p in enumerate(P):\n \
    \           Pinv[p] = i\n        return type(P)(Pinv)\n"
  dependsOn:
  - cp_library/alg/graph/func/func_graph_cls.py
  - cp_library/io/parsable_cls.py
  - cp_library/alg/iter/crf_list_cls.py
  - cp_library/alg/iter/roll_fn.py
  - cp_library/ds/array/u8f_fn.py
  - cp_library/ds/list/elist_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/io/io_base_cls.py
  isVerificationFile: false
  path: cp_library/alg/graph/func/perm_graph_cls.py
  requiredBy: []
  timestamp: '2025-07-28 19:59:52+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/agc/agc038_b_sliding_min_max.test.py
  - test/atcoder/abc/abc175_d_permutation.test.py
documentation_of: cp_library/alg/graph/func/perm_graph_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/func/perm_graph_cls.py
- /library/cp_library/alg/graph/func/perm_graph_cls.py.html
title: cp_library/alg/graph/func/perm_graph_cls.py
---
