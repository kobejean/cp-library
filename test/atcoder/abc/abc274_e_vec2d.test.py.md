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
    path: cp_library/io/io_cls.py
    title: cp_library/io/io_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parsable_cls.py
    title: cp_library/io/parsable_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_fn.py
    title: cp_library/io/read_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/write_fn.py
    title: cp_library/io/write_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/linalg/elm_wise_mixin.py
    title: cp_library/math/linalg/elm_wise_mixin.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/linalg/vec/vec2d_cls.py
    title: cp_library/math/linalg/vec/vec2d_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/linalg/vec/vec_cls.py
    title: cp_library/math/linalg/vec/vec_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    ERROR: 1e-6
    PROBLEM: https://atcoder.jp/contests/abc274/tasks/abc274_e
    links:
    - https://atcoder.jp/contests/abc274/tasks/abc274_e
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc274/tasks/abc274_e\n\
    # verification-helper: ERROR 1e-6\nfrom math import inf\n\ndef main():\n    N,\
    \ M = read(tuple[int, ...])\n    XY = read(list[Vec2D, N])\n    PQ = read(list[Vec2D,\
    \ M])\n    pts = PQ+XY\n    o = Vec2D(0,0)\n    Tmask = (1 << M) -1\n    Y = N+M\n\
    \    Z = 1 << Y\n    O = [o.distance(v) for v in pts]\n    F = [1/(1 << mask.bit_count())\
    \ for mask in range(1 << M)]\n    \n    dp = [[inf]*Y for _ in range(Z)]\n   \
    \ for y in range(Y):\n        mask = 1 << y\n        dp[mask][y] = O[y]\n    \
    \    \n    for mask in range(1,Z):\n        factor = F[mask&Tmask]\n        for\
    \ y in range(Y):\n            nmask = mask | 1 << y\n            if mask == nmask:\
    \ continue\n            nc = dp[nmask][y]\n            for l in range(Y):\n  \
    \              nc = min(nc, dp[mask][l] + pts[l].distance(pts[y]) * factor)\n\
    \            dp[nmask][y] = nc\n            \n    full = Z-1\n    ans = inf\n\
    \    for tmask in range(1<<M):\n        mask = full ^ tmask\n        factor =\
    \ F[mask&Tmask]\n        for l in range(Y):\n            nc = dp[mask][l] + O[l]\
    \ * factor\n            ans = min(ans, nc)\n    write(f'{ans:0.10f}')\n\n'''\n\
    \u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n   \
    \          https://kobejean.github.io/cp-library               \n'''\nfrom numbers\
    \ import Number\nfrom typing import Sequence\nfrom math import gcd, sqrt\n\n\n\
    from typing import Iterable \nfrom types import GenericAlias\n\n\nclass Parsable:\n\
    \    @classmethod\n    def compile(cls):\n        def parser(io: 'IOBase'): return\
    \ cls(next(io))\n        return parser\n    @classmethod\n    def __class_getitem__(cls,\
    \ item): return GenericAlias(cls, item)\nfrom math import hypot\nimport operator\n\
    \nclass ElmWiseMixin:\n    def elm_wise(self, other, op):\n        if isinstance(other,\
    \ Number):\n            return type(self)(op(x, other) for x in self)\n      \
    \  if isinstance(other, Sequence):\n            return type(self)(op(x, y) for\
    \ x, y in zip(self, other))\n        raise ValueError(\"Operand must be a number\
    \ or a tuple of the same length\")\n\n    def __add__(self, other): return self.elm_wise(other,\
    \ operator.add)\n    def __radd__(self, other): return self.elm_wise(other, operator.add)\n\
    \    def __sub__(self, other): return self.elm_wise(other, operator.sub)\n   \
    \ def __rsub__(self, other): return self.elm_wise(other, lambda x,y: operator.sub(y,x))\n\
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
    \        def parse(io: IOBase): return cls(elm(io), elm(io))\n        return parse\n\
    from typing import Type, Union, overload\nfrom typing import TypeVar\n_S = TypeVar('S');\
    \ _T = TypeVar('T'); _U = TypeVar('U'); _T1 = TypeVar('T1'); _T2 = TypeVar('T2');\
    \ _T3 = TypeVar('T3'); _T4 = TypeVar('T4'); _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\
    \n@overload\ndef read() -> list[int]: ...\n@overload\ndef read(spec: Type[_T],\
    \ char=False) -> _T: ...\n@overload\ndef read(spec: _U, char=False) -> _U: ...\n\
    @overload\ndef read(*specs: Type[_T], char=False) -> tuple[_T, ...]: ...\n@overload\n\
    def read(*specs: _U, char=False) -> tuple[_U, ...]: ...\ndef read(*specs: Union[Type[_T],_T],\
    \ char=False):\n    IO.stdin.char = char\n    if not specs: return IO.stdin.readnumsinto([])\n\
    \    parser: _T = Parser.compile(specs[0] if len(specs) == 1 else specs)\n   \
    \ return parser(IO.stdin)\nfrom os import read as os_read, write as os_write,\
    \ fstat as os_fstat\nimport sys\nfrom __pypy__.builders import StringBuilder\n\
    \n\ndef max2(a, b): return a if a > b else b\n\nclass IO(IOBase):\n    BUFSIZE\
    \ = 1 << 16; stdin: 'IO'; stdout: 'IO'\n    __slots__ = 'f', 'file', 'B', 'O',\
    \ 'V', 'S', 'l', 'p', 'char', 'sz', 'st', 'ist', 'writable', 'encoding', 'errors'\n\
    \    def __init__(io, file):\n        io.file = file\n        try: io.f = file.fileno();\
    \ io.sz, io.writable = max2(io.BUFSIZE, os_fstat(io.f).st_size), ('x' in file.mode\
    \ or 'r' not in file.mode)\n        except: io.f, io.sz, io.writable = -1, io.BUFSIZE,\
    \ False\n        io.B, io.O, io.S = bytearray(), [], StringBuilder(); io.V = memoryview(io.B);\
    \ io.l = io.p = 0\n        io.char, io.st, io.ist, io.encoding, io.errors = False,\
    \ [], [], 'ascii', 'ignore'\n    def _dec(io, l, r): return io.V[l:r].tobytes().decode(io.encoding,\
    \ io.errors)\n    def readbytes(io, sz): return os_read(io.f, sz)\n    def load(io):\n\
    \        while io.l >= len(io.O):\n            if not (b := io.readbytes(io.sz)):\n\
    \                if io.O[-1] < len(io.B): io.O.append(len(io.B))\n           \
    \     break\n            pos = len(io.B); io.B.extend(b)\n            while ~(pos\
    \ := io.B.find(b'\\n', pos)): io.O.append(pos := pos+1)\n    def __next__(io):\n\
    \        if io.char: return io.readchar()\n        else: return io.readtoken()\n\
    \    def readchar(io):\n        io.load(); r = io.O[io.l]\n        c = chr(io.B[io.p])\n\
    \        if io.p >= r-1: io.p = r; io.l += 1\n        else: io.p += 1\n      \
    \  return c\n    def write(io, s: str): io.S.append(s)\n    def readline(io):\
    \ io.load(); l, io.p = io.p, io.O[io.l]; io.l += 1; return io._dec(l, io.p)\n\
    \    def readtoken(io):\n        io.load(); r = io.O[io.l]\n        if ~(p :=\
    \ io.B.find(b' ', io.p, r)): s = io._dec(io.p, p); io.p = p+1\n        else: s\
    \ = io._dec(io.p, r-1); io.p = r; io.l += 1\n        return s\n    def readtokens(io):\
    \ io.st.clear(); return io.readtokensinto(io.st)\n    def readints(io): io.ist.clear();\
    \ return io.readintsinto(io.ist)\n    def readdigits(io): io.ist.clear(); return\
    \ io.readdigitsinto(io.ist)\n    def readnums(io): io.ist.clear(); return io.readnumsinto(io.ist)\n\
    \    def readchars(io): io.load(); l, io.p = io.p, io.O[io.l]; io.l += 1; return\
    \ io._dec(l, io.p-1)\n    def readinto(io, lst):\n        if io.char: return io.readcharsinto(lst)\n\
    \        else: return io.readtokensinto(lst)\n    def readcharsinto(io, lst):\
    \ lst.extend(io.readchars()); return lst\n    def readtokensinto(io, lst): \n\
    \        io.load(); r = io.O[io.l]\n        while ~(p := io.B.find(b' ', io.p,\
    \ r)): lst.append(io._dec(io.p, p)); io.p = p+1\n        lst.append(io._dec(io.p,\
    \ r-1)); io.p = r; io.l += 1; return lst\n    def readintsinto(io, lst):\n   \
    \     io.load(); r = io.O[io.l]\n        while io.p < r:\n            while io.p\
    \ < r and io.B[io.p] <= 32: io.p += 1\n            if io.p >= r: break\n     \
    \       minus = x = 0\n            if io.B[io.p] == 45: minus = 1; io.p += 1\n\
    \            while io.p < r and io.B[io.p] >= 48:\n                x = x * 10\
    \ + (io.B[io.p] & 15); io.p += 1\n            lst.append(-x if minus else x)\n\
    \            if io.p < r and io.B[io.p] == 32: io.p += 1\n        io.l += 1; return\
    \ lst\n    def readdigitsinto(io, lst):\n        io.load(); r = io.O[io.l]\n \
    \       while io.p < r and io.B[io.p] > 32:\n            if io.B[io.p] >= 48 and\
    \ io.B[io.p] <= 57:\n                lst.append(io.B[io.p] & 15)\n           \
    \ io.p += 1\n        if io.p < r and io.B[io.p] == 10: io.p = r; io.l += 1\n \
    \       return lst\n    def readnumsinto(io, lst):\n        if io.char: return\
    \ io.readdigitsinto(lst)\n        else: return io.readintsinto(lst)\n    def line(io):\
    \ io.st.clear(); return io.readinto(io.st)\n    def wait(io):\n        io.load();\
    \ r = io.O[io.l]\n        while io.p < r: yield\n    def flush(io):\n        if\
    \ io.writable: os_write(io.f, io.S.build().encode(io.encoding, io.errors)); io.S\
    \ = StringBuilder()\nsys.stdin = IO.stdin = IO(sys.stdin); sys.stdout = IO.stdout\
    \ = IO(sys.stdout)\n\ndef write(*args, **kwargs):\n    '''Prints the values to\
    \ a stream, or to stdout_fast by default.'''\n    sep, file = kwargs.pop(\"sep\"\
    , \" \"), kwargs.pop(\"file\", IO.stdout)\n    at_start = True\n    for x in args:\n\
    \        if not at_start:\n            file.write(sep)\n        file.write(str(x))\n\
    \        at_start = False\n    file.write(kwargs.pop(\"end\", \"\\n\"))\n    if\
    \ kwargs.pop(\"flush\", False):\n        file.flush()\n\nif __name__ == \"__main__\"\
    :\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc274/tasks/abc274_e\n\
    # verification-helper: ERROR 1e-6\nfrom math import inf\n\ndef main():\n    N,\
    \ M = read(tuple[int, ...])\n    XY = read(list[Vec2D, N])\n    PQ = read(list[Vec2D,\
    \ M])\n    pts = PQ+XY\n    o = Vec2D(0,0)\n    Tmask = (1 << M) -1\n    Y = N+M\n\
    \    Z = 1 << Y\n    O = [o.distance(v) for v in pts]\n    F = [1/(1 << mask.bit_count())\
    \ for mask in range(1 << M)]\n    \n    dp = [[inf]*Y for _ in range(Z)]\n   \
    \ for y in range(Y):\n        mask = 1 << y\n        dp[mask][y] = O[y]\n    \
    \    \n    for mask in range(1,Z):\n        factor = F[mask&Tmask]\n        for\
    \ y in range(Y):\n            nmask = mask | 1 << y\n            if mask == nmask:\
    \ continue\n            nc = dp[nmask][y]\n            for l in range(Y):\n  \
    \              nc = min(nc, dp[mask][l] + pts[l].distance(pts[y]) * factor)\n\
    \            dp[nmask][y] = nc\n            \n    full = Z-1\n    ans = inf\n\
    \    for tmask in range(1<<M):\n        mask = full ^ tmask\n        factor =\
    \ F[mask&Tmask]\n        for l in range(Y):\n            nc = dp[mask][l] + O[l]\
    \ * factor\n            ans = min(ans, nc)\n    write(f'{ans:0.10f}')\n\nfrom\
    \ cp_library.math.linalg.vec.vec2d_cls import Vec2D\nfrom cp_library.io.read_fn\
    \ import read\nfrom cp_library.io.write_fn import write\n\nif __name__ == \"__main__\"\
    :\n    main()"
  dependsOn:
  - cp_library/math/linalg/vec/vec2d_cls.py
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/math/linalg/vec/vec_cls.py
  - cp_library/io/io_base_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/io/io_cls.py
  - cp_library/io/parsable_cls.py
  - cp_library/math/linalg/elm_wise_mixin.py
  - cp_library/alg/dp/max2_fn.py
  isVerificationFile: true
  path: test/atcoder/abc/abc274_e_vec2d.test.py
  requiredBy: []
  timestamp: '2025-07-28 14:11:54+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/atcoder/abc/abc274_e_vec2d.test.py
layout: document
redirect_from:
- /verify/test/atcoder/abc/abc274_e_vec2d.test.py
- /verify/test/atcoder/abc/abc274_e_vec2d.test.py.html
title: test/atcoder/abc/abc274_e_vec2d.test.py
---
