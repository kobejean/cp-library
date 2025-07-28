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
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc261_g_queries_mo_ops.test.py
    title: test/atcoder/abc/abc261_g_queries_mo_ops.test.py
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
    from enum import IntFlag, auto\nfrom math import isqrt\nfrom types import GenericAlias\n\
    \n\nclass Parsable:\n    @classmethod\n    def compile(cls):\n        def parser(io:\
    \ 'IOBase'): return cls(next(io))\n        return parser\n    @classmethod\n \
    \   def __class_getitem__(cls, item): return GenericAlias(cls, item)\n\n\n\ndef\
    \ elist(est_len: int) -> list: ...\ntry:\n    from __pypy__ import newlist_hint\n\
    except:\n    def newlist_hint(hint):\n        return []\nelist = newlist_hint\n\
    \    \n\nclass MoOp(IntFlag):\n    ADD_LEFT = auto()\n    ADD_RIGHT = auto()\n\
    \    REMOVE_LEFT = auto()\n    REMOVE_RIGHT = auto()\n    ANSWER = auto()\n  \
    \  \n    ADD = ADD_LEFT | ADD_RIGHT\n    REMOVE = REMOVE_LEFT | REMOVE_RIGHT\n\
    \n# def hilbert(x: int, y: int, n: int) -> int:\n#     '''Convert (x,y) to Hilbert\
    \ curve distance for given n (power of 2).'''\n#     d = 0\n#     for s in range(n.bit_length()\
    \ - 1, -1, -1):\n#         rx = (x >> s) & 1\n#         ry = (y >> s) & 1\n# \
    \        d += n * n * ((3 * rx) ^ ry) >> 2\n#         if ry == 0:\n#         \
    \    if rx == 1:\n#                 x = n-1 - x\n#                 y = n-1 - y\n\
    #             x, y = y, x\n#     return d\n\nclass QueriesMoOps(tuple[list[int],\
    \ ...],Parsable):\n    '''\n    QueriesMoOps[Q: int, N: int, T: type = tuple[int,\
    \ int]]\n    Orders queries using Mo's algorithm and generates a sequence of operations\
    \ to process them efficiently.\n    Each operation is either moving pointers or\
    \ answering a query.\n    \n    Uses half-interval convention: [left, right)\n\
    \    '''\n    def __new__(cls, L: list[int], R: list[int], N: int, B: int = None):\n\
    \        Q = len(L)\n        qbits = Q.bit_length()\n        nbits = (N+1).bit_length()\n\
    \        qmask = qmask = (1 << qbits)-1\n        nmask = (1 << nbits)-1\n    \
    \    B = max(1,N//isqrt(max(1,Q)) )if B is None else B\n        order = [0]*Q\n\
    \        for i in range(Q):\n            l, r = L[i], R[i]\n            b = l//B\n\
    \            r = nmask - r if b & 1 else r\n            order[i] = (((b << nbits)\
    \ + r) << qbits) + i\n        # n = 1 << nbits\n        # for i in range(Q):\n\
    \        #     l, r = L[i], R[i]\n        #     # Use Hilbert curve mapping for\
    \ the 2D point (l,r)\n        #     h = hilbert(l, r, n)\n        #     order[i]\
    \ = (h << qbits) + i\n        order.sort()\n        ops = elist(3*Q); A1 = elist(3*Q);\
    \ A2 = elist(3*Q); A3 = elist(3*Q)\n        nl = nr = 0\n        for i in order:\n\
    \            i &= qmask\n            l, r = L[i], R[i]\n            if l < nl:\
    \ ops.append(MoOp.ADD_LEFT); A1.append(nl-1); A2.append(l-1); A3.append(-1)\n\
    \            elif l > nl: ops.append(MoOp.REMOVE_LEFT); A1.append(nl); A2.append(l);\
    \ A3.append(1)\n            if r > nr: ops.append(MoOp.ADD_RIGHT); A1.append(nr);\
    \ A2.append(r); A3.append(1)\n            elif r < nr: ops.append(MoOp.REMOVE_RIGHT);\
    \ A1.append(nr-1); A2.append(r-1); A3.append(-1)\n            ops.append(MoOp.ANSWER);\
    \ A1.append(i); A2.append(l); A3.append(r)\n            nl, nr = l, r\n      \
    \  return super().__new__(cls, (ops, A1, A2, A3))\n\n    @classmethod\n    def\
    \ compile(cls, Q: int, N: int, T: type = tuple[-1, int], B: int = None):\n   \
    \     if T == tuple[-1, int]:\n            query = Parser.compile(T)\n       \
    \     def parse(io: IOBase):\n                L, R = [0]*Q, [0]*Q\n          \
    \      for i in range(Q): L[i], R[i] = io.readints(); L[i] -= 1\n            \
    \    return cls(L, R, N, B)\n            return parse\n        else:\n       \
    \     query = Parser.compile(T)\n            def parse(io: IOBase):\n        \
    \        L, R = [0]*Q, [0]*Q\n                for i in range(Q): L[i], R[i] =\
    \ query(io)\n                return cls(L, R, N, B)\n            return parse\n\
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
  code: "import cp_library.__header__\nfrom enum import IntFlag, auto\nfrom math import\
    \ isqrt\nfrom cp_library.io.parsable_cls import Parsable\nimport cp_library.ds.__header__\n\
    from cp_library.ds.list.elist_fn import elist\n\nclass MoOp(IntFlag):\n    ADD_LEFT\
    \ = auto()\n    ADD_RIGHT = auto()\n    REMOVE_LEFT = auto()\n    REMOVE_RIGHT\
    \ = auto()\n    ANSWER = auto()\n    \n    ADD = ADD_LEFT | ADD_RIGHT\n    REMOVE\
    \ = REMOVE_LEFT | REMOVE_RIGHT\n\n# def hilbert(x: int, y: int, n: int) -> int:\n\
    #     '''Convert (x,y) to Hilbert curve distance for given n (power of 2).'''\n\
    #     d = 0\n#     for s in range(n.bit_length() - 1, -1, -1):\n#         rx =\
    \ (x >> s) & 1\n#         ry = (y >> s) & 1\n#         d += n * n * ((3 * rx)\
    \ ^ ry) >> 2\n#         if ry == 0:\n#             if rx == 1:\n#            \
    \     x = n-1 - x\n#                 y = n-1 - y\n#             x, y = y, x\n\
    #     return d\n\nclass QueriesMoOps(tuple[list[int], ...],Parsable):\n    '''\n\
    \    QueriesMoOps[Q: int, N: int, T: type = tuple[int, int]]\n    Orders queries\
    \ using Mo's algorithm and generates a sequence of operations to process them\
    \ efficiently.\n    Each operation is either moving pointers or answering a query.\n\
    \    \n    Uses half-interval convention: [left, right)\n    '''\n    def __new__(cls,\
    \ L: list[int], R: list[int], N: int, B: int = None):\n        Q = len(L)\n  \
    \      qbits = Q.bit_length()\n        nbits = (N+1).bit_length()\n        qmask\
    \ = qmask = (1 << qbits)-1\n        nmask = (1 << nbits)-1\n        B = max(1,N//isqrt(max(1,Q))\
    \ )if B is None else B\n        order = [0]*Q\n        for i in range(Q):\n  \
    \          l, r = L[i], R[i]\n            b = l//B\n            r = nmask - r\
    \ if b & 1 else r\n            order[i] = (((b << nbits) + r) << qbits) + i\n\
    \        # n = 1 << nbits\n        # for i in range(Q):\n        #     l, r =\
    \ L[i], R[i]\n        #     # Use Hilbert curve mapping for the 2D point (l,r)\n\
    \        #     h = hilbert(l, r, n)\n        #     order[i] = (h << qbits) + i\n\
    \        order.sort()\n        ops = elist(3*Q); A1 = elist(3*Q); A2 = elist(3*Q);\
    \ A3 = elist(3*Q)\n        nl = nr = 0\n        for i in order:\n            i\
    \ &= qmask\n            l, r = L[i], R[i]\n            if l < nl: ops.append(MoOp.ADD_LEFT);\
    \ A1.append(nl-1); A2.append(l-1); A3.append(-1)\n            elif l > nl: ops.append(MoOp.REMOVE_LEFT);\
    \ A1.append(nl); A2.append(l); A3.append(1)\n            if r > nr: ops.append(MoOp.ADD_RIGHT);\
    \ A1.append(nr); A2.append(r); A3.append(1)\n            elif r < nr: ops.append(MoOp.REMOVE_RIGHT);\
    \ A1.append(nr-1); A2.append(r-1); A3.append(-1)\n            ops.append(MoOp.ANSWER);\
    \ A1.append(i); A2.append(l); A3.append(r)\n            nl, nr = l, r\n      \
    \  return super().__new__(cls, (ops, A1, A2, A3))\n\n    @classmethod\n    def\
    \ compile(cls, Q: int, N: int, T: type = tuple[-1, int], B: int = None):\n   \
    \     if T == tuple[-1, int]:\n            query = Parser.compile(T)\n       \
    \     def parse(io: IOBase):\n                L, R = [0]*Q, [0]*Q\n          \
    \      for i in range(Q): L[i], R[i] = io.readints(); L[i] -= 1\n            \
    \    return cls(L, R, N, B)\n            return parse\n        else:\n       \
    \     query = Parser.compile(T)\n            def parse(io: IOBase):\n        \
    \        L, R = [0]*Q, [0]*Q\n                for i in range(Q): L[i], R[i] =\
    \ query(io)\n                return cls(L, R, N, B)\n            return parse\n\
    from cp_library.io.parser_cls import Parser\nfrom cp_library.io.io_base_cls import\
    \ IOBase"
  dependsOn:
  - cp_library/io/parsable_cls.py
  - cp_library/ds/list/elist_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/io/io_base_cls.py
  isVerificationFile: false
  path: cp_library/ds/queries_mo_ops_cls.py
  requiredBy: []
  timestamp: '2025-07-28 19:59:52+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/abc/abc261_g_queries_mo_ops.test.py
documentation_of: cp_library/ds/queries_mo_ops_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/queries_mo_ops_cls.py
- /library/cp_library/ds/queries_mo_ops_cls.py.html
title: cp_library/ds/queries_mo_ops_cls.py
---
