---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/max2_fn.py
    title: cp_library/alg/dp/max2_fn.py
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
    path: test/atcoder/abc/abc261_g_mo.test.py
    title: test/atcoder/abc/abc261_g_mo.test.py
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
    from math import isqrt\nfrom types import GenericAlias\n\n\nclass Parsable:\n\
    \    @classmethod\n    def compile(cls):\n        def parser(io: 'IOBase'): return\
    \ cls(next(io))\n        return parser\n    @classmethod\n    def __class_getitem__(cls,\
    \ item): return GenericAlias(cls, item)\n\n\n\ndef max2(a, b): return a if a >\
    \ b else b\n\nclass Mo(Parsable):\n    '''Mo[Q: int, N: int, T: type = tuple[int,\
    \ int]]'''\n    def __init__(mo, L: list[int], R: list[int], N: int):\n      \
    \  mo.Q = len(L)\n        mo.qbits = mo.Q.bit_length()\n        mo.nbits = N.bit_length()\n\
    \        mo.qmask = (1 << mo.qbits) - 1\n        mo.nmask = (1 << mo.nbits) -\
    \ 1\n        mo.B = max2(1,N//isqrt(max2(1,mo.Q)))\n        mo.order = [mo.packet(i,\
    \ L[i], R[i]) for i in range(mo.Q)]\n        mo.order.sort()\n        mo.L = [0]*mo.Q\n\
    \        mo.R = [0]*mo.Q\n        for i,j in enumerate(mo.order):\n          \
    \  j &= mo.qmask\n            mo.order[i], mo.L[i], mo.R[i] = j, L[j], R[j]\n\n\
    \    def packet(mo, i: int, l: int, r: int) -> int:\n        b = l//mo.B\n   \
    \     if b & 1: r = mo.nmask - r\n        return (b << mo.nbits | r) << mo.qbits\
    \ | i\n\n    def add(mo, i: int):\n        '''Add element at index i to current\
    \ range.'''\n        pass\n\n    def remove(mo, i: int):\n        '''Remove element\
    \ at index i from current range.'''\n        pass\n\n    def answer(mo, i: int,\
    \ l: int, r: int) -> int:\n        '''Compute answer for current range.'''\n \
    \       pass\n    \n    def solve(mo) -> list[int]:\n        ans = [0]*mo.Q; l\
    \ = r = 0\n        for i in range(mo.Q):\n            qid, nl, nr = mo.order[i],\
    \ mo.L[i], mo.R[i]\n            while r < nr: mo.add(r); r += 1\n            while\
    \ nl < l: mo.add(l:=l-1)\n            while l < nl: mo.remove(l); l += 1\n   \
    \         while nr < r: mo.remove(r:=r-1)\n            ans[qid] = mo.answer(qid,\
    \ l, r)\n        return ans\n\n    @classmethod\n    def compile(cls, Q: int,\
    \ N: int, T: type = tuple[-1, int]):\n        query = Parser.compile(T)\n    \
    \    def parse(io: IOBase):\n            L, R = [0]*Q, [0]*Q\n            for\
    \ i in range(Q): L[i], R[i] = query(io) \n            return cls(L, R, N)\n  \
    \      return parse\n\nclass IOBase:\n    @property\n    def char(io) -> bool:\
    \ ...\n    @property\n    def writable(io) -> bool: ...\n    def __next__(io)\
    \ -> str: ...\n    def write(io, s: str) -> None: ...\n    def readline(io) ->\
    \ str: ...\n    def readtoken(io) -> str: ...\n    def readtokens(io) -> list[str]:\
    \ ...\n    def readints(io) -> list[int]: ...\n    def readdigits(io) -> list[int]:\
    \ ...\n    def readnums(io) -> list[int]: ...\n    def readchar(io) -> str: ...\n\
    \    def readchars(io) -> str: ...\n    def readinto(io, lst: list[str]) -> list[str]:\
    \ ...\n    def readcharsinto(io, lst: list[str]) -> list[str]: ...\n    def readtokensinto(io,\
    \ lst: list[str]) -> list[str]: ...\n    def readintsinto(io, lst: list[int])\
    \ -> list[int]: ...\n    def readdigitsinto(io, lst: list[int]) -> list[int]:\
    \ ...\n    def readnumsinto(io, lst: list[int]) -> list[int]: ...\n    def wait(io):\
    \ ...\n    def flush(io) -> None: ...\n    def line(io) -> list[str]: ...\nimport\
    \ typing\nfrom numbers import Number\nfrom typing import Callable, Collection\n\
    \nclass Parser:\n    def __init__(self, spec):  self.parse = Parser.compile(spec)\n\
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
    \        else:\n            raise NotImplementedError()\n"
  code: "import cp_library.__header__\nfrom math import isqrt\nfrom cp_library.io.parsable_cls\
    \ import Parsable\nimport cp_library.alg.__header__\nimport cp_library.alg.dp.__header__\n\
    from cp_library.alg.dp.max2_fn import max2\n\nclass Mo(Parsable):\n    '''Mo[Q:\
    \ int, N: int, T: type = tuple[int, int]]'''\n    def __init__(mo, L: list[int],\
    \ R: list[int], N: int):\n        mo.Q = len(L)\n        mo.qbits = mo.Q.bit_length()\n\
    \        mo.nbits = N.bit_length()\n        mo.qmask = (1 << mo.qbits) - 1\n \
    \       mo.nmask = (1 << mo.nbits) - 1\n        mo.B = max2(1,N//isqrt(max2(1,mo.Q)))\n\
    \        mo.order = [mo.packet(i, L[i], R[i]) for i in range(mo.Q)]\n        mo.order.sort()\n\
    \        mo.L = [0]*mo.Q\n        mo.R = [0]*mo.Q\n        for i,j in enumerate(mo.order):\n\
    \            j &= mo.qmask\n            mo.order[i], mo.L[i], mo.R[i] = j, L[j],\
    \ R[j]\n\n    def packet(mo, i: int, l: int, r: int) -> int:\n        b = l//mo.B\n\
    \        if b & 1: r = mo.nmask - r\n        return (b << mo.nbits | r) << mo.qbits\
    \ | i\n\n    def add(mo, i: int):\n        '''Add element at index i to current\
    \ range.'''\n        pass\n\n    def remove(mo, i: int):\n        '''Remove element\
    \ at index i from current range.'''\n        pass\n\n    def answer(mo, i: int,\
    \ l: int, r: int) -> int:\n        '''Compute answer for current range.'''\n \
    \       pass\n    \n    def solve(mo) -> list[int]:\n        ans = [0]*mo.Q; l\
    \ = r = 0\n        for i in range(mo.Q):\n            qid, nl, nr = mo.order[i],\
    \ mo.L[i], mo.R[i]\n            while r < nr: mo.add(r); r += 1\n            while\
    \ nl < l: mo.add(l:=l-1)\n            while l < nl: mo.remove(l); l += 1\n   \
    \         while nr < r: mo.remove(r:=r-1)\n            ans[qid] = mo.answer(qid,\
    \ l, r)\n        return ans\n\n    @classmethod\n    def compile(cls, Q: int,\
    \ N: int, T: type = tuple[-1, int]):\n        query = Parser.compile(T)\n    \
    \    def parse(io: IOBase):\n            L, R = [0]*Q, [0]*Q\n            for\
    \ i in range(Q): L[i], R[i] = query(io) \n            return cls(L, R, N)\n  \
    \      return parse\nfrom cp_library.io.io_base_cls import IOBase\nfrom cp_library.io.parser_cls\
    \ import Parser"
  dependsOn:
  - cp_library/io/parsable_cls.py
  - cp_library/alg/dp/max2_fn.py
  - cp_library/io/io_base_cls.py
  - cp_library/io/parser_cls.py
  isVerificationFile: false
  path: cp_library/alg/dp/mo_cls.py
  requiredBy: []
  timestamp: '2025-07-28 14:17:34+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/abc/abc261_g_mo.test.py
documentation_of: cp_library/alg/dp/mo_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/dp/mo_cls.py
- /library/cp_library/alg/dp/mo_cls.py.html
title: cp_library/alg/dp/mo_cls.py
---
