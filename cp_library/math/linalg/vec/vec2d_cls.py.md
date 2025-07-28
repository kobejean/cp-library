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
  - icon: ':heavy_check_mark:'
    path: cp_library/math/linalg/elm_wise_mixin.py
    title: cp_library/math/linalg/elm_wise_mixin.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/linalg/vec/vec_cls.py
    title: cp_library/math/linalg/vec/vec_cls.py
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/math/linalg/vec/slope_cls.py
    title: cp_library/math/linalg/vec/slope_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc151_f_fbisect_left.test.py
    title: test/atcoder/abc/abc151_f_fbisect_left.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc189_e_vec2d.test.py
    title: test/atcoder/abc/abc189_e_vec2d.test.py
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc274_e_vec2d.test.py
    title: test/atcoder/abc/abc274_e_vec2d.test.py
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
    from numbers import Number\nfrom typing import Sequence\nfrom math import gcd,\
    \ sqrt\n\n\nfrom typing import Iterable \nfrom types import GenericAlias\n\n\n\
    class Parsable:\n    @classmethod\n    def compile(cls):\n        def parser(io:\
    \ 'IOBase'): return cls(next(io))\n        return parser\n    @classmethod\n \
    \   def __class_getitem__(cls, item): return GenericAlias(cls, item)\nfrom math\
    \ import hypot\nimport operator\n\nclass ElmWiseMixin:\n    def elm_wise(self,\
    \ other, op):\n        if isinstance(other, Number):\n            return type(self)(op(x,\
    \ other) for x in self)\n        if isinstance(other, Sequence):\n           \
    \ return type(self)(op(x, y) for x, y in zip(self, other))\n        raise ValueError(\"\
    Operand must be a number or a tuple of the same length\")\n\n    def __add__(self,\
    \ other): return self.elm_wise(other, operator.add)\n    def __radd__(self, other):\
    \ return self.elm_wise(other, operator.add)\n    def __sub__(self, other): return\
    \ self.elm_wise(other, operator.sub)\n    def __rsub__(self, other): return self.elm_wise(other,\
    \ lambda x,y: operator.sub(y,x))\n    def __mul__(self, other): return self.elm_wise(other,\
    \ operator.mul)\n    def __rmul__(self, other): return self.elm_wise(other, operator.mul)\n\
    \    def __truediv__(self, other): return self.elm_wise(other, operator.truediv)\n\
    \    def __rtruediv__(self, other): return self.elm_wise(other, lambda x,y: operator.truediv(y,x))\n\
    \    def __floordiv__(self, other): return self.elm_wise(other, operator.floordiv)\n\
    \    def __rfloordiv__(self, other): return self.elm_wise(other, lambda x,y: operator.floordiv(y,x))\n\
    \    def __mod__(self, other): return self.elm_wise(other, operator.mod)\n\n \
    \   def distance(self: 'ElmWiseMixin', other: 'ElmWiseMixin'):\n        diff =\
    \ other-self\n        return hypot(*diff)\n    \n    def magnitude(vec: 'ElmWiseMixin'):\n\
    \        return hypot(*vec)\n    \n    def norm(vec: 'ElmWiseMixin'):\n      \
    \  return vec / vec.magnitude()\n\nclass Vec(ElmWiseMixin, tuple, Parsable):\n\
    \    def __new__(cls, *args):\n        return super().__new__(cls, args[0] if\
    \ len(args) == 1 and isinstance(args[0], Iterable) else args)\n    @classmethod\n\
    \    def compile(cls, T: type = int, N = None):\n        elm = Parser.compile(T)\n\
    \        if N is None:\n            def parse(io: IOBase): return cls(elm(io)\
    \ for _ in io.wait())\n        else:\n            def parse(io: IOBase): return\
    \ cls(elm(io) for _ in range(N))\n        return parse\n\nclass IOBase:\n    @property\n\
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
    \ ...\nimport typing\nfrom typing import Callable, Collection\n\nclass Parser:\n\
    \    def __init__(self, spec):  self.parse = Parser.compile(spec)\n    def __call__(self,\
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
    \        else:\n            raise NotImplementedError()\n\nclass Vec2D(Vec):\n\
    \    def __new__(cls, *args):\n        if len(args) == 0: return super().__new__(cls,\
    \ (0,0))\n        return super().__new__(cls, *args)\n    def elm_wise(self, other,\
    \ op):\n        if isinstance(other, Number): return Vec2D(op(self[0], other),\
    \ op(self[1], other))\n        if isinstance(other, Sequence): return Vec2D(op(self[0],\
    \ other[0]), op(self[1], other[1]))\n        raise ValueError(\"Operand must be\
    \ a number or a tuple of the same length\")\n    def manhat(v1: 'Vec', v2: 'Vec'):\
    \ return abs(v2[0]-v1[0]) + abs(v2[1]-v1[1])\n    def distance(v1: 'Vec', v2:\
    \ 'Vec'): dx, dy = v2[0]-v1[0], v2[1]-v1[1]; return sqrt(dx*dx+dy*dy)\n    def\
    \ distance2(v1: 'Vec', v2: 'Vec'): dx, dy = v2[0]-v1[0], v2[1]-v1[1]; return dx*dx+dy*dy\n\
    \    def magnitude(vec: 'Vec'): x, y = vec; return sqrt(x*x+y*y)\n    def magnitude2(vec:\
    \ 'Vec'): x, y = vec; return x*x+y*y\n    def rot90(vec): x,y = vec; return Vec2D(-y,x)\n\
    \    def rot180(vec): x,y = vec; return Vec2D(-x,-y)\n    def rot270(vec): x,y\
    \ = vec; return Vec2D(y,-x)\n    def flip_x(vec): x,y = vec; return Vec2D(-x,y)\n\
    \    def flip_y(vec): x,y = vec; return Vec2D(x,-y)\n    def cross(vec, other):\
    \ return vec[0]*other[1] - vec[1]*other[0]\n    def slope_norm(vec):\n       \
    \ x,y = vec\n        if x == 0 and y == 0: return vec\n        if x == 0: return\
    \ Vec2D((0,1)) if y > 0 else Vec2D((0,-1))\n        if y == 0: return Vec2D((1,0))\
    \ if x > 0 else Vec2D((-1,0))\n        g = gcd(x,y)\n        return Vec2D((x//g,y//g))\n\
    \    @classmethod\n    def compile(cls, T: type = int):\n        elm = Parser.compile(T)\n\
    \        def parse(io: IOBase): return cls(elm(io), elm(io))\n        return parse\n"
  code: "import cp_library.math.__header__\nfrom numbers import Number\nfrom typing\
    \ import Sequence\nfrom math import gcd, sqrt\nimport cp_library.math.__header__\n\
    import cp_library.math.linalg.__header__\nimport cp_library.math.linalg.vec.__header__\n\
    from cp_library.math.linalg.vec.vec_cls import Vec\n\nclass Vec2D(Vec):\n    def\
    \ __new__(cls, *args):\n        if len(args) == 0: return super().__new__(cls,\
    \ (0,0))\n        return super().__new__(cls, *args)\n    def elm_wise(self, other,\
    \ op):\n        if isinstance(other, Number): return Vec2D(op(self[0], other),\
    \ op(self[1], other))\n        if isinstance(other, Sequence): return Vec2D(op(self[0],\
    \ other[0]), op(self[1], other[1]))\n        raise ValueError(\"Operand must be\
    \ a number or a tuple of the same length\")\n    def manhat(v1: 'Vec', v2: 'Vec'):\
    \ return abs(v2[0]-v1[0]) + abs(v2[1]-v1[1])\n    def distance(v1: 'Vec', v2:\
    \ 'Vec'): dx, dy = v2[0]-v1[0], v2[1]-v1[1]; return sqrt(dx*dx+dy*dy)\n    def\
    \ distance2(v1: 'Vec', v2: 'Vec'): dx, dy = v2[0]-v1[0], v2[1]-v1[1]; return dx*dx+dy*dy\n\
    \    def magnitude(vec: 'Vec'): x, y = vec; return sqrt(x*x+y*y)\n    def magnitude2(vec:\
    \ 'Vec'): x, y = vec; return x*x+y*y\n    def rot90(vec): x,y = vec; return Vec2D(-y,x)\n\
    \    def rot180(vec): x,y = vec; return Vec2D(-x,-y)\n    def rot270(vec): x,y\
    \ = vec; return Vec2D(y,-x)\n    def flip_x(vec): x,y = vec; return Vec2D(-x,y)\n\
    \    def flip_y(vec): x,y = vec; return Vec2D(x,-y)\n    def cross(vec, other):\
    \ return vec[0]*other[1] - vec[1]*other[0]\n    def slope_norm(vec):\n       \
    \ x,y = vec\n        if x == 0 and y == 0: return vec\n        if x == 0: return\
    \ Vec2D((0,1)) if y > 0 else Vec2D((0,-1))\n        if y == 0: return Vec2D((1,0))\
    \ if x > 0 else Vec2D((-1,0))\n        g = gcd(x,y)\n        return Vec2D((x//g,y//g))\n\
    \    @classmethod\n    def compile(cls, T: type = int):\n        elm = Parser.compile(T)\n\
    \        def parse(io: IOBase): return cls(elm(io), elm(io))\n        return parse\n\
    from cp_library.io.io_base_cls import IOBase\nfrom cp_library.io.parser_cls import\
    \ Parser"
  dependsOn:
  - cp_library/math/linalg/vec/vec_cls.py
  - cp_library/io/io_base_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/io/parsable_cls.py
  - cp_library/math/linalg/elm_wise_mixin.py
  isVerificationFile: false
  path: cp_library/math/linalg/vec/vec2d_cls.py
  requiredBy:
  - cp_library/math/linalg/vec/slope_cls.py
  timestamp: '2025-07-28 14:11:54+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/abc/abc274_e_vec2d.test.py
  - test/atcoder/abc/abc151_f_fbisect_left.test.py
  - test/atcoder/abc/abc189_e_vec2d.test.py
documentation_of: cp_library/math/linalg/vec/vec2d_cls.py
layout: document
redirect_from:
- /library/cp_library/math/linalg/vec/vec2d_cls.py
- /library/cp_library/math/linalg/vec/vec2d_cls.py.html
title: cp_library/math/linalg/vec/vec2d_cls.py
---
