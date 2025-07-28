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
  - icon: ':warning:'
    path: cp_library/math/linalg/elm_wise_in_place_mixin.py
    title: cp_library/math/linalg/elm_wise_in_place_mixin.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/linalg/elm_wise_mixin.py
    title: cp_library/math/linalg/elm_wise_mixin.py
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
    from typing import Container, Sequence\nfrom numbers import Number\nfrom types\
    \ import GenericAlias\n\n\nclass Parsable:\n    @classmethod\n    def compile(cls):\n\
    \        def parser(io: 'IOBase'): return cls(next(io))\n        return parser\n\
    \    @classmethod\n    def __class_getitem__(cls, item): return GenericAlias(cls,\
    \ item)\n\n\nimport operator\nfrom math import hypot\n\nclass ElmWiseMixin:\n\
    \    def elm_wise(self, other, op):\n        if isinstance(other, Number):\n \
    \           return type(self)(op(x, other) for x in self)\n        if isinstance(other,\
    \ Sequence):\n            return type(self)(op(x, y) for x, y in zip(self, other))\n\
    \        raise ValueError(\"Operand must be a number or a tuple of the same length\"\
    )\n\n    def __add__(self, other): return self.elm_wise(other, operator.add)\n\
    \    def __radd__(self, other): return self.elm_wise(other, operator.add)\n  \
    \  def __sub__(self, other): return self.elm_wise(other, operator.sub)\n    def\
    \ __rsub__(self, other): return self.elm_wise(other, lambda x,y: operator.sub(y,x))\n\
    \    def __mul__(self, other): return self.elm_wise(other, operator.mul)\n   \
    \ def __rmul__(self, other): return self.elm_wise(other, operator.mul)\n    def\
    \ __truediv__(self, other): return self.elm_wise(other, operator.truediv)\n  \
    \  def __rtruediv__(self, other): return self.elm_wise(other, lambda x,y: operator.truediv(y,x))\n\
    \    def __floordiv__(self, other): return self.elm_wise(other, operator.floordiv)\n\
    \    def __rfloordiv__(self, other): return self.elm_wise(other, lambda x,y: operator.floordiv(y,x))\n\
    \    def __mod__(self, other): return self.elm_wise(other, operator.mod)\n\n \
    \   def distance(self: 'ElmWiseMixin', other: 'ElmWiseMixin'):\n        diff =\
    \ other-self\n        return hypot(*diff)\n    \n    def magnitude(vec: 'ElmWiseMixin'):\n\
    \        return hypot(*vec)\n    \n    def norm(vec: 'ElmWiseMixin'):\n      \
    \  return vec / vec.magnitude()\n\nclass ElmWiseInPlaceMixin(ElmWiseMixin):\n\
    \    def ielm_wise(self, other, op):\n        if isinstance(other, Number):\n\
    \            for i in range(len(self)):\n                self[i] = op(self[i],\
    \ other)\n        elif isinstance(other, Sequence) and len(self) == len(other):\n\
    \            for i in range(len(self)):\n                self[i] = op(self[i],\
    \ other[i])\n        else:\n            raise ValueError(\"Operand must be a number\
    \ or a list of the same length\")\n        return self\n    \n    def __iadd__(self,\
    \ other): return self.ielm_wise(other, operator.add)\n    def __isub__(self, other):\
    \ return self.ielm_wise(other, operator.sub)\n    def __imul__(self, other): return\
    \ self.ielm_wise(other, operator.mul)\n    def __itruediv__(self, other): return\
    \ self.ielm_wise(other, operator.truediv)\n    def __ifloordiv__(self, other):\
    \ return self.ielm_wise(other, operator.floordiv)\n    def __imod__(self, other):\
    \ return self.ielm_wise(other, operator.mod)\n\n\nclass Mat(Parsable, Container,\
    \ ElmWiseInPlaceMixin):\n    def __init__(self, flat, N, M): self.data, self.N,\
    \ self.M = flat, N, M\n    def elm_wise(self, other, op):\n        cls = type(self)\n\
    \        if isinstance(other, Number): return cls([op(elm, other) for elm in self.data])\n\
    \        if isinstance(other, Sequence): return cls([op(self.data[i], elm) for\
    \ i, elm in enumerate(other)])\n        raise ValueError(\"Operand must be a number\
    \ or a tuple of the same length\")\n    def ielm_wise(self, other, op):\n    \
    \    data = self.data\n        if isinstance(other, Number):\n            for\
    \ i in range(len(data)): data[i] = op(data[i], other)\n        elif isinstance(other,\
    \ Sequence) and len(data) == len(other):\n            for i, elm in enumerate(other):\
    \ data[i] = op(data[i], elm)\n        else: raise ValueError(\"Operand must be\
    \ a number or a list of the same length\")\n        return self\n    def __len__(self):\
    \ return self.N\n    def __getitem__(self, ij: tuple[int, int]): i, j = ij; return\
    \ self.data[i*self.M+j]\n    def __setitem__(self, ij: tuple[int, int], val: int):\
    \ i, j = ij; self.data[i*self.M+j] = val\n    def __contains__(self, x: int) ->\
    \ bool: return x in self.data\n    def __matmul__(A,B):\n        assert A.M ==\
    \ B.N, f\"Dimension mismatch {A.M = } {B.N = }\"\n        N,M = A.N, B.M\n   \
    \     cls = type(A)\n        R = cls([0]*(M*N))\n        for irow in range(0,N*M,M):\n\
    \            for k in range(A.M):\n                krow, a = k*M, A.data[irow+k]\n\
    \                for j in range(M):\n                    R.data[irow+j] = B.data[krow+j]*a\
    \ + R.data[irow+j]\n        return R\n    def __pow__(A,K):\n        R = A[:]\
    \ if K & 1 else type(A).identity(A.N)\n        for i in range(1,K.bit_length()):\n\
    \            A = A @ A\n            if K >> i & 1: R = R @ A\n        return R\
    \ \n    @classmethod\n    def identity(cls, N):\n        data = [0]*(N*N)\n  \
    \      for i in range(0,N*N,N+1): data[i] = 1\n        return cls(data)\n    def\
    \ copy(self):\n        cls = type(self)\n        obj = cls.__new__(cls)\n    \
    \    obj.N, obj.M, obj.data = self.N, self.M, self.data\n        return obj\n\
    \    @classmethod\n    def compile(cls, N: int, M: int, T: type = int):\n    \
    \    elm, size = Parser.compile(T), N*M\n        def parse(io: IOBase): return\
    \ cls([elm(io) for _ in range(size)])\n        return parse\n    def __repr__(self)\
    \ -> str: return '\\n'.join(' '.join(str(elm) for elm in row) for row in self)\n\
    import typing\nfrom typing import Callable, Collection\n\nclass IOBase:\n    @property\n\
    \    def char(io) -> bool: ...\n    @property\n    def writable(io) -> bool: ...\n\
    \    def __next__(io) -> str: ...\n    def write(io, s: str) -> None: ...\n  \
    \  def readline(io) -> str: ...\n    def readtoken(io) -> str: ...\n    def readtokens(io)\
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
    \        else:\n            raise NotImplementedError()\n"
  code: "import cp_library.__header__\nfrom typing import Container, Sequence\nfrom\
    \ numbers import Number\nfrom cp_library.io.parsable_cls import Parsable\nimport\
    \ cp_library.math.__header__\nimport cp_library.math.linalg.__header__\nfrom cp_library.math.linalg.elm_wise_in_place_mixin\
    \ import ElmWiseInPlaceMixin\nimport cp_library.math.linalg.mat.__header__\n\n\
    class Mat(Parsable, Container, ElmWiseInPlaceMixin):\n    def __init__(self, flat,\
    \ N, M): self.data, self.N, self.M = flat, N, M\n    def elm_wise(self, other,\
    \ op):\n        cls = type(self)\n        if isinstance(other, Number): return\
    \ cls([op(elm, other) for elm in self.data])\n        if isinstance(other, Sequence):\
    \ return cls([op(self.data[i], elm) for i, elm in enumerate(other)])\n       \
    \ raise ValueError(\"Operand must be a number or a tuple of the same length\"\
    )\n    def ielm_wise(self, other, op):\n        data = self.data\n        if isinstance(other,\
    \ Number):\n            for i in range(len(data)): data[i] = op(data[i], other)\n\
    \        elif isinstance(other, Sequence) and len(data) == len(other):\n     \
    \       for i, elm in enumerate(other): data[i] = op(data[i], elm)\n        else:\
    \ raise ValueError(\"Operand must be a number or a list of the same length\")\n\
    \        return self\n    def __len__(self): return self.N\n    def __getitem__(self,\
    \ ij: tuple[int, int]): i, j = ij; return self.data[i*self.M+j]\n    def __setitem__(self,\
    \ ij: tuple[int, int], val: int): i, j = ij; self.data[i*self.M+j] = val\n   \
    \ def __contains__(self, x: int) -> bool: return x in self.data\n    def __matmul__(A,B):\n\
    \        assert A.M == B.N, f\"Dimension mismatch {A.M = } {B.N = }\"\n      \
    \  N,M = A.N, B.M\n        cls = type(A)\n        R = cls([0]*(M*N))\n       \
    \ for irow in range(0,N*M,M):\n            for k in range(A.M):\n            \
    \    krow, a = k*M, A.data[irow+k]\n                for j in range(M):\n     \
    \               R.data[irow+j] = B.data[krow+j]*a + R.data[irow+j]\n        return\
    \ R\n    def __pow__(A,K):\n        R = A[:] if K & 1 else type(A).identity(A.N)\n\
    \        for i in range(1,K.bit_length()):\n            A = A @ A\n          \
    \  if K >> i & 1: R = R @ A\n        return R \n    @classmethod\n    def identity(cls,\
    \ N):\n        data = [0]*(N*N)\n        for i in range(0,N*N,N+1): data[i] =\
    \ 1\n        return cls(data)\n    def copy(self):\n        cls = type(self)\n\
    \        obj = cls.__new__(cls)\n        obj.N, obj.M, obj.data = self.N, self.M,\
    \ self.data\n        return obj\n    @classmethod\n    def compile(cls, N: int,\
    \ M: int, T: type = int):\n        elm, size = Parser.compile(T), N*M\n      \
    \  def parse(io: IOBase): return cls([elm(io) for _ in range(size)])\n       \
    \ return parse\n    def __repr__(self) -> str: return '\\n'.join(' '.join(str(elm)\
    \ for elm in row) for row in self)\nfrom cp_library.io.parser_cls import Parser\n\
    from cp_library.io.io_base_cls import IOBase"
  dependsOn:
  - cp_library/io/parsable_cls.py
  - cp_library/math/linalg/elm_wise_in_place_mixin.py
  - cp_library/io/parser_cls.py
  - cp_library/io/io_base_cls.py
  - cp_library/math/linalg/elm_wise_mixin.py
  isVerificationFile: false
  path: cp_library/math/linalg/mat/mat_cls.py
  requiredBy: []
  timestamp: '2025-07-28 14:11:54+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/linalg/mat/mat_cls.py
layout: document
redirect_from:
- /library/cp_library/math/linalg/mat/mat_cls.py
- /library/cp_library/math/linalg/mat/mat_cls.py.html
title: cp_library/math/linalg/mat/mat_cls.py
---
