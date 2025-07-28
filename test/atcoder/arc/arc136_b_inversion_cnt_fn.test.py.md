---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/max2_fn.py
    title: cp_library/alg/dp/max2_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer_cls.py
    title: cp_library/bit/pack/packer_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/bit/bit_cls.py
    title: cp_library/ds/tree/bit/bit_cls.py
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
    path: cp_library/math/invcnt_fn.py
    title: cp_library/math/invcnt_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/arc136/tasks/arc136_b
    links:
    - https://atcoder.jp/contests/arc136/tasks/arc136_b
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/arc136/tasks/arc136_b\n\
    \n\ndef main():\n    N = read(int)\n    A = read(list[-1])\n    B = read(list[-1])\n\
    \    Aic = invcnt(A)\n    Bic = invcnt(B)\n    if sorted(A) != sorted(B):\n  \
    \      return False\n    has_dup = len(set(A)) < N\n    return has_dup or (Aic&1\
    \ == Bic&1)\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2578\n             https://kobejean.github.io/cp-library             \
    \  \n'''\n\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2578\n            \u250F\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2513            \n            \u2503               \
    \                     7 \u2503            \n            \u2517\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u252F\u2501\u251B            \n   \
    \         \u250F\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2513                 \u2502      \
    \        \n            \u2503                3 \u2503\u25C4\u2500\u2500\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2524\
    \              \n            \u2517\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u252F\u2501\u251B           \
    \      \u2502              \n            \u250F\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2513       \u2502  \u250F\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2513       \u2502              \n            \u2503      1 \u2503\u25C4\
    \u2500\u2500\u2500\u2500\u2500\u2500\u2524  \u2503      5 \u2503\u25C4\u2500\u2500\
    \u2500\u2500\u2500\u2500\u2524              \n            \u2517\u2501\u2501\u2501\
    \u2501\u2501\u2501\u252F\u2501\u251B       \u2502  \u2517\u2501\u2501\u2501\u2501\
    \u2501\u2501\u252F\u2501\u251B       \u2502              \n            \u250F\u2501\
    \u2501\u2501\u2513  \u2502  \u250F\u2501\u2501\u2501\u2513  \u2502  \u250F\u2501\
    \u2501\u2501\u2513  \u2502  \u250F\u2501\u2501\u2501\u2513  \u2502           \
    \   \n            \u2503 0 \u2503\u25C4\u2500\u2524  \u2503 2 \u2503\u25C4\u2500\
    \u2524  \u2503 4 \u2503\u25C4\u2500\u2524  \u2503 6 \u2503\u25C4\u2500\u2524 \
    \             \n            \u2517\u2501\u252F\u2501\u251B  \u2502  \u2517\u2501\
    \u252F\u2501\u251B  \u2502  \u2517\u2501\u252F\u2501\u251B  \u2502  \u2517\u2501\
    \u252F\u2501\u251B  \u2502              \n              \u2502    \u2502    \u2502\
    \    \u2502    \u2502    \u2502    \u2502    \u2502              \n          \
    \    \u25BC    \u25BC    \u25BC    \u25BC    \u25BC    \u25BC    \u25BC    \u25BC\
    \              \n            \u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\
    \u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\
    \u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\u250F\u2501\u2501\u2501\u2513\
    \u250F\u2501\u2501\u2501\u2513            \n            \u2503 0 \u2503\u2503\
    \ 1 \u2503\u2503 2 \u2503\u2503 3 \u2503\u2503 4 \u2503\u2503 5 \u2503\u2503 6\
    \ \u2503\u2503 7 \u2503            \n            \u2517\u2501\u2501\u2501\u251B\
    \u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\
    \u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B\u2517\
    \u2501\u2501\u2501\u251B\u2517\u2501\u2501\u2501\u251B            \n\u257A\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n           Data\
    \ Structure - Tree - Binary Index Tree            \n'''\n\nclass BIT:\n    def\
    \ __init__(bit, v):\n        if isinstance(v, int): bit._d, bit._n = [0]*v, v\n\
    \        else: bit.build(v)\n        bit._lb = 1<<bit._n.bit_length()\n\n    def\
    \ build(bit, data):\n        bit._d, bit._n = data, len(data)\n        for i in\
    \ range(bit._n):\n            if (r := i|i+1) < bit._n: bit._d[r] += bit._d[i]\n\
    \n    def add(bit, i, x):\n        while i < bit._n: bit._d[i] += x; i |= i+1\n\
    \n    def sum(bit, n: int) -> int:\n        s = 0\n        while n: s, n = s+bit._d[n-1],\
    \ n&n-1\n        return s\n\n    def sum_range(bit, l, r):\n        s = 0\n  \
    \      while r: s, r = s+bit._d[r-1], r&r-1\n        while l: s, l = s-bit._d[l-1],\
    \ l&l-1\n        return s\n\n    def __len__(bit) -> int:\n        return bit._n\n\
    \    \n    def __getitem__(bit, i: int) -> int:\n        s, l = bit._d[i], i&(i+1)\n\
    \        while l != i: s, i = s-bit._d[i-1], i-(i&-i)\n        return s\n    get\
    \ = __getitem__\n    \n    def __setitem__(bit, i: int, x: int) -> None: bit.add(i,\
    \ x-bit[i])\n    set = __setitem__\n\n    def prelist(bit) -> list[int]:\n   \
    \     pre = [0]+bit._d\n        for i in range(bit._n+1): pre[i] += pre[i&i-1]\n\
    \        return pre\n\n    def bisect_left(bit, v) -> int:\n        return bit.bisect_right(v-1)\
    \ if v>0 else -1\n    \n    def bisect_right(bit, v, key=None) -> int:\n     \
    \   i = s = 0; m = bit._lb\n        if key:\n            while m := m>>1:\n  \
    \              if (ni := m|i) <= bit._n and key(ns:=s+bit._d[ni-1]) <= v: s, i\
    \ = ns, ni\n        else:\n            while m := m>>1:\n                if (ni\
    \ := m|i) <= bit._n and (ns:=s+bit._d[ni-1]) <= v: s, i = ns, ni\n        return\
    \ i\n\ndef invcnt(A: list[int]):\n    P = Packer(N := len(A))\n    bit, cnt, I\
    \ = BIT(N), 0, P.enumerate(A); I.sort(reverse=True)\n    for i in I: cnt += bit.sum(i&P.m);\
    \ bit.add(i&P.m, 1)\n    return cnt\n\n\n\nclass Packer:\n    __slots__ = 's',\
    \ 'm'\n    def __init__(P, mx: int): P.s = mx.bit_length(); P.m = (1 << P.s) -\
    \ 1\n    def enc(P, a: int, b: int): return a << P.s | b\n    def dec(P, x: int)\
    \ -> tuple[int, int]: return x >> P.s, x & P.m\n    def enumerate(P, A, reverse=False):\
    \ P.ienumerate(A:=list(A), reverse); return A\n    def ienumerate(P, A, reverse=False):\n\
    \        if reverse:\n            for i,a in enumerate(A): A[i] = P.enc(-a, i)\n\
    \        else:\n            for i,a in enumerate(A): A[i] = P.enc(a, i)\n    def\
    \ indices(P, A: list[int]): P.iindices(A:=list(A)); return A\n    def iindices(P,\
    \ A):\n        for i,a in enumerate(A): A[i] = P.m&a\nfrom typing import Type,\
    \ Union, overload\nfrom typing import TypeVar\n_S = TypeVar('S'); _T = TypeVar('T');\
    \ _U = TypeVar('U'); _T1 = TypeVar('T1'); _T2 = TypeVar('T2'); _T3 = TypeVar('T3');\
    \ _T4 = TypeVar('T4'); _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\n\n@overload\n\
    def read() -> list[int]: ...\n@overload\ndef read(spec: Type[_T], char=False)\
    \ -> _T: ...\n@overload\ndef read(spec: _U, char=False) -> _U: ...\n@overload\n\
    def read(*specs: Type[_T], char=False) -> tuple[_T, ...]: ...\n@overload\ndef\
    \ read(*specs: _U, char=False) -> tuple[_U, ...]: ...\ndef read(*specs: Union[Type[_T],_T],\
    \ char=False):\n    IO.stdin.char = char\n    if not specs: return IO.stdin.readnumsinto([])\n\
    \    parser: _T = Parser.compile(specs[0] if len(specs) == 1 else specs)\n   \
    \ return parser(IO.stdin)\nfrom os import read as os_read, write as os_write,\
    \ fstat as os_fstat\nimport sys\nfrom __pypy__.builders import StringBuilder\n\
    \n\ndef max2(a, b): return a if a > b else b\n\nclass IOBase:\n    @property\n\
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
    \ ...\n\nclass IO(IOBase):\n    BUFSIZE = 1 << 16; stdin: 'IO'; stdout: 'IO'\n\
    \    __slots__ = 'f', 'file', 'B', 'O', 'V', 'S', 'l', 'p', 'char', 'sz', 'st',\
    \ 'ist', 'writable', 'encoding', 'errors'\n    def __init__(io, file):\n     \
    \   io.file = file\n        try: io.f = file.fileno(); io.sz, io.writable = max2(io.BUFSIZE,\
    \ os_fstat(io.f).st_size), ('x' in file.mode or 'r' not in file.mode)\n      \
    \  except: io.f, io.sz, io.writable = -1, io.BUFSIZE, False\n        io.B, io.O,\
    \ io.S = bytearray(), [], StringBuilder(); io.V = memoryview(io.B); io.l = io.p\
    \ = 0\n        io.char, io.st, io.ist, io.encoding, io.errors = False, [], [],\
    \ 'ascii', 'ignore'\n    def _dec(io, l, r): return io.V[l:r].tobytes().decode(io.encoding,\
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
    \ = IO(sys.stdout)\nimport typing\nfrom numbers import Number\nfrom types import\
    \ GenericAlias \nfrom typing import Callable, Collection\n\nclass Parsable:\n\
    \    @classmethod\n    def compile(cls):\n        def parser(io: 'IOBase'): return\
    \ cls(next(io))\n        return parser\n    @classmethod\n    def __class_getitem__(cls,\
    \ item): return GenericAlias(cls, item)\n\nclass Parser:\n    def __init__(self,\
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
    \        else:\n            raise NotImplementedError()\n\ndef write(*args, **kwargs):\n\
    \    '''Prints the values to a stream, or to stdout_fast by default.'''\n    sep,\
    \ file = kwargs.pop(\"sep\", \" \"), kwargs.pop(\"file\", IO.stdout)\n    at_start\
    \ = True\n    for x in args:\n        if not at_start:\n            file.write(sep)\n\
    \        file.write(str(x))\n        at_start = False\n    file.write(kwargs.pop(\"\
    end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n        file.flush()\n\
    \nif __name__ == \"__main__\":\n    ans = main()\n    write(\"Yes\" if ans else\
    \ \"No\")\n    \n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/arc136/tasks/arc136_b\n\
    \n\ndef main():\n    N = read(int)\n    A = read(list[-1])\n    B = read(list[-1])\n\
    \    Aic = invcnt(A)\n    Bic = invcnt(B)\n    if sorted(A) != sorted(B):\n  \
    \      return False\n    has_dup = len(set(A)) < N\n    return has_dup or (Aic&1\
    \ == Bic&1)\n\nfrom cp_library.math.invcnt_fn import invcnt\nfrom cp_library.io.read_fn\
    \ import read\nfrom cp_library.io.write_fn import write\n\nif __name__ == \"__main__\"\
    :\n    ans = main()\n    write(\"Yes\" if ans else \"No\")\n    "
  dependsOn:
  - cp_library/math/invcnt_fn.py
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/ds/tree/bit/bit_cls.py
  - cp_library/bit/pack/packer_cls.py
  - cp_library/io/io_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/io/io_base_cls.py
  - cp_library/io/parsable_cls.py
  - cp_library/alg/dp/max2_fn.py
  isVerificationFile: true
  path: test/atcoder/arc/arc136_b_inversion_cnt_fn.test.py
  requiredBy: []
  timestamp: '2025-07-28 14:17:34+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/atcoder/arc/arc136_b_inversion_cnt_fn.test.py
layout: document
redirect_from:
- /verify/test/atcoder/arc/arc136_b_inversion_cnt_fn.test.py
- /verify/test/atcoder/arc/arc136_b_inversion_cnt_fn.test.py.html
title: test/atcoder/arc/arc136_b_inversion_cnt_fn.test.py
---
