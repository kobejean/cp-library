---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer_cls.py
    title: cp_library/bit/pack/packer_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/list_find_fn.py
    title: cp_library/ds/list/list_find_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/view/view_cls.py
    title: cp_library/ds/view/view_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/io_base_cls.py
    title: cp_library/io/io_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parsable_cls.py
    title: cp_library/io/parsable_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  _extendedRequiredBy:
  - icon: ':warning:'
    path: perf/grid.py
    title: perf/grid.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/unittests/ds/grid/grid_cls_test.py
    title: test/unittests/ds/grid/grid_cls_test.py
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
    from typing import Generic, Union\nfrom typing import TypeVar\n_S = TypeVar('S');\
    \ _T = TypeVar('T'); _U = TypeVar('U'); _T1 = TypeVar('T1'); _T2 = TypeVar('T2');\
    \ _T3 = TypeVar('T3'); _T4 = TypeVar('T4'); _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\
    from types import GenericAlias\n\n\nclass Parsable:\n    @classmethod\n    def\
    \ compile(cls):\n        def parser(io: 'IOBase'): return cls(next(io))\n    \
    \    return parser\n    @classmethod\n    def __class_getitem__(cls, item): return\
    \ GenericAlias(cls, item)\n\n\n\nclass Packer:\n    __slots__ = 's', 'm'\n   \
    \ def __init__(P, mx: int): P.s = mx.bit_length(); P.m = (1 << P.s) - 1\n    def\
    \ enc(P, a: int, b: int): return a << P.s | b\n    def dec(P, x: int) -> tuple[int,\
    \ int]: return x >> P.s, x & P.m\n    def enumerate(P, A, reverse=False): P.ienumerate(A:=list(A),\
    \ reverse); return A\n    def ienumerate(P, A, reverse=False):\n        if reverse:\n\
    \            for i,a in enumerate(A): A[i] = P.enc(-a, i)\n        else:\n   \
    \         for i,a in enumerate(A): A[i] = P.enc(a, i)\n    def indices(P, A: list[int]):\
    \ P.iindices(A:=list(A)); return A\n    def iindices(P, A):\n        for i,a in\
    \ enumerate(A): A[i] = P.m&a\n\n\n\n\nimport sys\n\ndef list_find(lst: list, value,\
    \ start = 0, stop = sys.maxsize):\n    try:\n        return lst.index(value, start,\
    \ stop)\n    except:\n        return -1\n\n\nclass view(Generic[_T]):\n    __slots__\
    \ = 'A', 'l', 'r'\n    def __init__(V, A: list[_T], l: int = 0, r: int = 0): V.A,\
    \ V.l, V.r = A, l, r\n    def __len__(V): return V.r - V.l\n    def __getitem__(V,\
    \ i: int): \n        if 0 <= i < V.r - V.l: return V.A[V.l+i]\n        else: raise\
    \ IndexError\n    def __setitem__(V, i: int, v: _T): V.A[V.l+i] = v\n    def __contains__(V,\
    \ v: _T): return list_find(V.A, v, V.l, V.r) != -1\n    def set_range(V, l: int,\
    \ r: int): V.l, V.r = l, r\n    def index(V, v: _T): return V.A.index(v, V.l,\
    \ V.r) - V.l\n    def reverse(V):\n        l, r = V.l, V.r-1\n        while l\
    \ < r: V.A[l], V.A[r] = V.A[r], V.A[l]; l += 1; r -= 1\n    def sort(V, /, *args,\
    \ **kwargs):\n        A = V.A[V.l:V.r]; A.sort(*args, **kwargs)\n        for i,a\
    \ in enumerate(A,V.l): V.A[i] = a\n    def pop(V): V.r -= 1; return V.A[V.r]\n\
    \    def append(V, v: _T): V.A[V.r] = v; V.r += 1\n    def popleft(V): V.l +=\
    \ 1; return V.A[V.l-1]\n    def appendleft(V, v: _T): V.l -= 1; V.A[V.l] = v;\
    \ \n    def validate(V): return 0 <= V.l <= V.r <= len(V.A)\n\nclass Grid(Generic[_T],\
    \ Parsable):\n    __slots__ = 'pkr', 'size', 'H', 'W', 'A'\n    def __init__(G,\
    \ H: int, W: int, A: Union[_T, list[_T], list[list[_T]]], pkr = None):\n     \
    \   G.pkr = pkr or Packer(W-1); G.size = H << G.pkr.s; G.H, G.W = H, W\n     \
    \   if isinstance(A, list):\n            if isinstance(A[0], list):\n        \
    \        G.A = [A[0][0]]*G.size\n                for i in range(H):\n        \
    \            ii = i << G.pkr.s\n                    for j in range(W): G.A[ii|j]\
    \ = A[i][j]\n            elif len(A) < G.size:\n                G.A = [A[0]]*G.size\n\
    \                for i in range(H):\n                    ii = i << G.pkr.s\n \
    \                   for j in range(W): G.A[ii|j] = A[i*W+j]\n            else:\n\
    \                G.A = A\n        else:\n            G.A = [A] * G.size\n    def\
    \ __len__(G): return G.H\n    def __getitem__(G, i: int): \n        if 0 <= i\
    \ < G.H: return view(G.A, i<<G.pkr.s, (i+1)<<G.pkr.s)\n        else: raise IndexError\n\
    \    def __call__(G, i: int, j: int): return G.A[G.pkr.enc(i,j)]\n    def set(G,\
    \ i: int, j: int, v: _T): G.A[G.pkr.enc(i,j)] = v\n\n    @classmethod\n    def\
    \ compile(cls, H: int, W: int, T: type = int):\n        pkr = Packer(W-1); size\
    \ = H << pkr.s\n        if T is int:\n            def parse(io: IOBase):\n   \
    \             A = [0]*size\n                for i in range(H):\n             \
    \       for j, a in enumerate(io.readints()): A[pkr.enc(i,j)] = a\n          \
    \      return cls(H, W, A, pkr)\n        elif T is str:\n            def parse(io:\
    \ IOBase):\n                A = ['']*size\n                for i in range(H):\n\
    \                    for j, s in enumerate(io.line()): A[pkr.enc(i,j)] = s\n \
    \               return cls(H, W, A, pkr)\n        else:\n            elm = Parser.compile(T)\n\
    \            def parse(io: IOBase):\n                A = [None]*size\n       \
    \         for i in range(H):\n                    for j in range(W): A[pkr.enc(i,j)]\
    \ = elm(io)\n                return cls(H, W, A, pkr)\n        return parse\n\
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
  code: "import cp_library.__header__\nfrom typing import Generic, Union\nfrom cp_library.misc.typing\
    \ import _T\nfrom cp_library.io.parsable_cls import Parsable\nfrom cp_library.bit.pack.packer_cls\
    \ import Packer\nimport cp_library.ds.__header__\nimport cp_library.ds.grid.__header__\n\
    from cp_library.ds.view.view_cls import view\n\nclass Grid(Generic[_T], Parsable):\n\
    \    __slots__ = 'pkr', 'size', 'H', 'W', 'A'\n    def __init__(G, H: int, W:\
    \ int, A: Union[_T, list[_T], list[list[_T]]], pkr = None):\n        G.pkr = pkr\
    \ or Packer(W-1); G.size = H << G.pkr.s; G.H, G.W = H, W\n        if isinstance(A,\
    \ list):\n            if isinstance(A[0], list):\n                G.A = [A[0][0]]*G.size\n\
    \                for i in range(H):\n                    ii = i << G.pkr.s\n \
    \                   for j in range(W): G.A[ii|j] = A[i][j]\n            elif len(A)\
    \ < G.size:\n                G.A = [A[0]]*G.size\n                for i in range(H):\n\
    \                    ii = i << G.pkr.s\n                    for j in range(W):\
    \ G.A[ii|j] = A[i*W+j]\n            else:\n                G.A = A\n        else:\n\
    \            G.A = [A] * G.size\n    def __len__(G): return G.H\n    def __getitem__(G,\
    \ i: int): \n        if 0 <= i < G.H: return view(G.A, i<<G.pkr.s, (i+1)<<G.pkr.s)\n\
    \        else: raise IndexError\n    def __call__(G, i: int, j: int): return G.A[G.pkr.enc(i,j)]\n\
    \    def set(G, i: int, j: int, v: _T): G.A[G.pkr.enc(i,j)] = v\n\n    @classmethod\n\
    \    def compile(cls, H: int, W: int, T: type = int):\n        pkr = Packer(W-1);\
    \ size = H << pkr.s\n        if T is int:\n            def parse(io: IOBase):\n\
    \                A = [0]*size\n                for i in range(H):\n          \
    \          for j, a in enumerate(io.readints()): A[pkr.enc(i,j)] = a\n       \
    \         return cls(H, W, A, pkr)\n        elif T is str:\n            def parse(io:\
    \ IOBase):\n                A = ['']*size\n                for i in range(H):\n\
    \                    for j, s in enumerate(io.line()): A[pkr.enc(i,j)] = s\n \
    \               return cls(H, W, A, pkr)\n        else:\n            elm = Parser.compile(T)\n\
    \            def parse(io: IOBase):\n                A = [None]*size\n       \
    \         for i in range(H):\n                    for j in range(W): A[pkr.enc(i,j)]\
    \ = elm(io)\n                return cls(H, W, A, pkr)\n        return parse\n\
    from cp_library.io.parser_cls import Parser\nfrom cp_library.io.io_base_cls import\
    \ IOBase"
  dependsOn:
  - cp_library/io/parsable_cls.py
  - cp_library/bit/pack/packer_cls.py
  - cp_library/ds/view/view_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/io/io_base_cls.py
  - cp_library/ds/list/list_find_fn.py
  isVerificationFile: false
  path: cp_library/ds/grid/grid_cls.py
  requiredBy:
  - perf/grid.py
  timestamp: '2025-07-28 14:17:34+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/unittests/ds/grid/grid_cls_test.py
documentation_of: cp_library/ds/grid/grid_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/grid/grid_cls.py
- /library/cp_library/ds/grid/grid_cls.py.html
title: cp_library/ds/grid/grid_cls.py
---
