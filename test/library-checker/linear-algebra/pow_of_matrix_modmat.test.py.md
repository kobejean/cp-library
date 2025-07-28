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
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/read_fn.py
    title: cp_library/io/read_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/write_fn.py
    title: cp_library/io/write_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/linalg/mat/mod/modmat_cls.py
    title: cp_library/math/linalg/mat/mod/modmat_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/mint_cls.py
    title: cp_library/math/mod/mint_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/pow_of_matrix
    links:
    - https://judge.yosupo.jp/problem/pow_of_matrix
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_matrix\n\
    \ndef main():\n    mint.set_mod(998244353)\n    N, K = read()\n    A = ModMat([read()\
    \ for _ in range(N)])\n    B = A**K\n    write(B)\n\n'''\n\u257A\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\n\n\n    \nclass mint(int):\n    mod: int\n    zero: 'mint'\n\
    \    one: 'mint'\n    two: 'mint'\n    cache: list['mint']\n    def __new__(cls,\
    \ *args, **kwargs):\n        if 0 <= (x := int(*args, **kwargs)) < 64: return\
    \ cls.cache[x]\n        else: return cls.fix(x)\n    @classmethod\n    def set_mod(cls,\
    \ mod: int):\n        mint.mod = cls.mod = mod\n        mint.zero = cls.zero =\
    \ cls.cast(0)\n        mint.one = cls.one = cls.fix(1)\n        mint.two = cls.two\
    \ = cls.fix(2)\n        mint.cache = cls.cache = [cls.zero, cls.one, cls.two]\n\
    \        for x in range(3,64): mint.cache.append(cls.fix(x))\n    @classmethod\n\
    \    def fix(cls, x): return cls.cast(x%cls.mod)\n    @classmethod\n    def cast(cls,\
    \ x): return super().__new__(cls,x)\n    @classmethod\n    def mod_inv(cls, x):\n\
    \        a,b,s,t = int(x), cls.mod, 1, 0\n        while b: a,b,s,t = b,a%b,t,s-a//b*t\n\
    \        if a == 1: return cls.fix(s)\n        raise ValueError(f\"{x} is not\
    \ invertible in mod {cls.mod}\")\n    @property\n    def inv(self): return mint.mod_inv(self)\n\
    \    def __add__(self, x): return mint.fix(super().__add__(x))\n    def __radd__(self,\
    \ x): return mint.fix(super().__radd__(x))\n    def __sub__(self, x): return mint.fix(super().__sub__(x))\n\
    \    def __rsub__(self, x): return mint.fix(super().__rsub__(x))\n    def __mul__(self,\
    \ x): return mint.fix(super().__mul__(x))\n    def __rmul__(self, x): return mint.fix(super().__rmul__(x))\n\
    \    def __floordiv__(self, x): return self * mint.mod_inv(x)\n    def __rfloordiv__(self,\
    \ x): return self.inv * x\n    def __truediv__(self, x): return self * mint.mod_inv(x)\n\
    \    def __rtruediv__(self, x): return self.inv * x\n    def __pow__(self, x):\
    \ return self.cast(super().__pow__(x, self.mod))\n    def __neg__(self): return\
    \ mint.mod-self\n    def __pos__(self): return self\n    def __abs__(self): return\
    \ self\n    def __class_getitem__(self, x: int): return self.cache[x]\nfrom typing\
    \ import Union, List, Tuple\n\n\n\n\nclass ModMat:\n    __slots__ = 'data', 'R',\
    \ 'C'\n\n    def __init__(self, data: List[Union[int,mint]]):\n        self.data,\
    \ self.R, self.C = data, len(data), len(data[0])\n    \n    @classmethod\n   \
    \ def identity(cls, N) -> 'ModMat': return ModMat([[int(i==j) for j in range(N)]\
    \ for i in range(N)])\n    \n    @classmethod\n    def zeros(cls, R, C) -> 'ModMat':\
    \ return ModMat([[0]*C for _ in range(R)])\n\n    def inv(self) -> 'ModMat':\n\
    \        assert self.R != self.C\n        \n        N = self.R\n        A = [row[:]\
    \ for row in self.data]\n        I = [[int(i==j) for j in range(N)] for i in range(N)]\n\
    \        \n        for i in range(N):\n            if A[i][i] == 0:\n        \
    \        for j in range(i+1, N):\n                    if A[j][i] != 0:\n     \
    \                   A[i], A[j] = A[j], A[i]\n                        I[i], I[j]\
    \ = I[j], I[i]\n                        break\n                else:\n       \
    \             raise ValueError(\"Matrix is not invertible\")\n            \n \
    \           inv = pow(A[i][i], -1, mint.mod)\n            for j in range(N):\n\
    \                A[i][j] = (A[i][j] * inv) % mint.mod\n                I[i][j]\
    \ = (I[i][j] * inv) % mint.mod\n            \n            for j in range(N):\n\
    \                if i != j:\n                    factor = A[j][i]\n          \
    \          for k in range(N):\n                        A[j][k] = (A[j][k] - factor\
    \ * A[i][k]) % mint.mod\n                        I[j][k] = (I[j][k] - factor *\
    \ I[i][k]) % mint.mod\n        \n        return ModMat(I)\n    \n    def T(self)\
    \ -> 'ModMat': return ModMat(list(map(list,zip(*self.data))))\n\n    def elem_wise(self,\
    \ func, other):\n        if isinstance(other, ModMat):\n            return ModMat([[func(a,b)\
    \ for a,b in zip(Ai,Bi)] for Ai,Bi in zip(self.data,other.data)])\n        elif\
    \ isinstance(other, int):\n            return ModMat([[func(a,other) for a in\
    \ Ai] for Ai in self.data])\n        else:\n            return NotImplemented\n\
    \        \n    def __str__(self): return '\\n'.join(' '.join(map(str,row)) for\
    \ row in self.data)\n    def __iter__(self): return self.data\n    def __copy__(self):\
    \ return ModMat([row[:] for row in self.data])\n    def copy(self): return ModMat([row[:]\
    \ for row in self.data])\n    def __add__(self, other): return self.elem_wise(lambda\
    \ a,b: (a+b) % mint.mod, other)\n    def __radd__(self, other): return self.__add__(other)\n\
    \    def __sub__(self, other): return self.elem_wise(lambda a,b: (a-b) % mint.mod,\
    \ other)\n    def __rsub__(self, other): return self.__sub__(other)\n    def __mul__(self,\
    \ other): return self.elem_wise(lambda a,b: (a*b) % mint.mod, other)\n    def\
    \ __rmul__(self, other): return self.__mul__(other)\n    def __truediv__(self,\
    \ other): return self.elem_wise(lambda a,b: a*pow(b,-1,mint.mod) % mint.mod, other)\n\
    \    def __rtruediv__(self, other): return self.elem_wise(lambda a,b: pow(a,-1,mint.mod)*b\
    \ % mint.mod, other)\n    \n    def __matmul__(self, other: 'ModMat'):\n     \
    \   assert self.C == other.R\n        R = [[0]*other.C for _ in range(self.R)]\n\
    \        for i,Ri in enumerate(R):\n            for k,Aik in enumerate(self.data[i]):\n\
    \                for j,Bkj in enumerate(other.data[k]):\n                    Ri[j]\
    \ = (Ri[j] + Aik*Bkj) % mint.mod\n        return ModMat(R)\n    \n    def __pow__(self,\
    \ K):\n        assert isinstance(K,int)\n        assert self.R == self.C\n   \
    \     A = self.copy()\n        R = A if K & 1 else ModMat.identity(self.R)\n \
    \       for i in range(1,K.bit_length()):\n            A @= A \n            if\
    \ K >> i & 1:\n                R @= A \n        return R\n    \n    def __getitem__(self,\
    \ key: Union[int, Tuple[int, int], slice, Tuple[slice, slice]]):\n        if isinstance(key,\
    \ int):\n            return self.data[key]\n        elif isinstance(key, tuple):\n\
    \            if len(key) == 2:\n                if all(isinstance(k, int) for\
    \ k in key):\n                    return mint(self.data[key[0]][key[1]])\n   \
    \             elif all(isinstance(k, slice) for k in key):\n                 \
    \   return ModMat([[self.data[i][j] for j in range(*key[1].indices(self.C))] \n\
    \                                   for i in range(*key[0].indices(self.R))])\n\
    \            raise IndexError(\"Invalid index\")\n        elif isinstance(key,\
    \ slice):\n            return ModMat([row[:] for row in self.data[key]])\n   \
    \     raise IndexError(\"Invalid index\")\n\n    def __setitem__(self, key: Union[Tuple[int,\
    \ int], slice, Tuple[slice, slice]], value):\n        if isinstance(key, tuple):\n\
    \            if len(key) == 2:\n                if all(isinstance(k, int) for\
    \ k in key):\n                    self.data[key[0]][key[1]] = value % mint.mod\n\
    \                elif all(isinstance(k, slice) for k in key):\n              \
    \      if isinstance(value, ModMat):\n                        for i, row in enumerate(range(*key[0].indices(self.R))):\n\
    \                            for j, col in enumerate(range(*key[1].indices(self.C))):\n\
    \                                self.data[row][col] = value.data[i][j] % mint.mod\n\
    \                    else:\n                        for row in range(*key[0].indices(self.R)):\n\
    \                            for col in range(*key[1].indices(self.C)):\n    \
    \                            self.data[row][col] = value % mint.mod\n        \
    \        else:\n                    raise IndexError(\"Invalid index\")\n    \
    \        else:\n                raise IndexError(\"Invalid index\")\n        elif\
    \ isinstance(key, slice):\n            if isinstance(value, ModMat):\n       \
    \         for i, row in enumerate(range(*key.indices(self.R))):\n            \
    \        self.data[row] = [v % mint.mod for v in value.data[i]]\n            else:\n\
    \                for row in range(*key.indices(self.R)):\n                   \
    \ self.data[row] = [value % mint.mod] * self.C\n        else:\n            raise\
    \ IndexError(\"Invalid index\")\n\n    def __delitem__(self, key: Union[int, slice]):\n\
    \        if isinstance(key, (int, slice)):\n            del self.data[key]\n \
    \           self.R = len(self.data)\n            if self.R == 0:\n           \
    \     self.C = 0\n        else:\n            raise IndexError(\"Invalid index\"\
    )\n\n    \nfrom typing import Type, Union, overload\nfrom typing import TypeVar\n\
    _S = TypeVar('S'); _T = TypeVar('T'); _U = TypeVar('U'); _T1 = TypeVar('T1');\
    \ _T2 = TypeVar('T2'); _T3 = TypeVar('T3'); _T4 = TypeVar('T4'); _T5 = TypeVar('T5');\
    \ _T6 = TypeVar('T6')\n\n\n@overload\ndef read() -> list[int]: ...\n@overload\n\
    def read(spec: Type[_T], char=False) -> _T: ...\n@overload\ndef read(spec: _U,\
    \ char=False) -> _U: ...\n@overload\ndef read(*specs: Type[_T], char=False) ->\
    \ tuple[_T, ...]: ...\n@overload\ndef read(*specs: _U, char=False) -> tuple[_U,\
    \ ...]: ...\ndef read(*specs: Union[Type[_T],_T], char=False):\n    IO.stdin.char\
    \ = char\n    if not specs: return IO.stdin.readnumsinto([])\n    parser: _T =\
    \ Parser.compile(specs[0] if len(specs) == 1 else specs)\n    return parser(IO.stdin)\n\
    from os import read as os_read, write as os_write, fstat as os_fstat\nimport sys\n\
    from __pypy__.builders import StringBuilder\n\n\ndef max2(a, b):\n    return a\
    \ if a > b else b\n\nclass IOBase:\n    @property\n    def char(io) -> bool: ...\n\
    \    @property\n    def writable(io) -> bool: ...\n    def __next__(io) -> str:\
    \ ...\n    def write(io, s: str) -> None: ...\n    def readline(io) -> str: ...\n\
    \    def readtoken(io) -> str: ...\n    def readtokens(io) -> list[str]: ...\n\
    \    def readints(io) -> list[int]: ...\n    def readdigits(io) -> list[int]:\
    \ ...\n    def readnums(io) -> list[int]: ...\n    def readchar(io) -> str: ...\n\
    \    def readchars(io) -> str: ...\n    def readinto(io, lst: list[str]) -> list[str]:\
    \ ...\n    def readcharsinto(io, lst: list[str]) -> list[str]: ...\n    def readtokensinto(io,\
    \ lst: list[str]) -> list[str]: ...\n    def readintsinto(io, lst: list[int])\
    \ -> list[int]: ...\n    def readdigitsinto(io, lst: list[int]) -> list[int]:\
    \ ...\n    def readnumsinto(io, lst: list[int]) -> list[int]: ...\n    def wait(io):\
    \ ...\n    def flush(io) -> None: ...\n    def line(io) -> list[str]: ...\n\n\
    class IO(IOBase):\n    BUFSIZE = 1 << 16; stdin: 'IO'; stdout: 'IO'\n    __slots__\
    \ = 'f', 'file', 'B', 'O', 'V', 'S', 'l', 'p', 'char', 'sz', 'st', 'ist', 'writable',\
    \ 'encoding', 'errors'\n    def __init__(io, file):\n        io.file = file\n\
    \        try: io.f = file.fileno(); io.sz, io.writable = max2(io.BUFSIZE, os_fstat(io.f).st_size),\
    \ ('x' in file.mode or 'r' not in file.mode)\n        except: io.f, io.sz, io.writable\
    \ = -1, io.BUFSIZE, False\n        io.B, io.O, io.S = bytearray(), [], StringBuilder();\
    \ io.V = memoryview(io.B); io.l = io.p = 0\n        io.char, io.st, io.ist, io.encoding,\
    \ io.errors = False, [], [], 'ascii', 'ignore'\n    def _dec(io, l, r): return\
    \ io.V[l:r].tobytes().decode(io.encoding, io.errors)\n    def readbytes(io, sz):\
    \ return os_read(io.f, sz)\n    def load(io):\n        while io.l >= len(io.O):\n\
    \            if not (b := io.readbytes(io.sz)):\n                if io.O[-1] <\
    \ len(io.B): io.O.append(len(io.B))\n                break\n            pos =\
    \ len(io.B); io.B.extend(b)\n            while ~(pos := io.B.find(b'\\n', pos)):\
    \ io.O.append(pos := pos+1)\n    def __next__(io):\n        if io.char: return\
    \ io.readchar()\n        else: return io.readtoken()\n    def readchar(io):\n\
    \        io.load(); r = io.O[io.l]\n        c = chr(io.B[io.p])\n        if io.p\
    \ >= r-1: io.p = r; io.l += 1\n        else: io.p += 1\n        return c\n   \
    \ def write(io, s: str): io.S.append(s)\n    def readline(io): io.load(); l, io.p\
    \ = io.p, io.O[io.l]; io.l += 1; return io._dec(l, io.p)\n    def readtoken(io):\n\
    \        io.load(); r = io.O[io.l]\n        if ~(p := io.B.find(b' ', io.p, r)):\
    \ s = io._dec(io.p, p); io.p = p+1\n        else: s = io._dec(io.p, r-1); io.p\
    \ = r; io.l += 1\n        return s\n    def readtokens(io): io.st.clear(); return\
    \ io.readtokensinto(io.st)\n    def readints(io): io.ist.clear(); return io.readintsinto(io.ist)\n\
    \    def readdigits(io): io.ist.clear(); return io.readdigitsinto(io.ist)\n  \
    \  def readnums(io): io.ist.clear(); return io.readnumsinto(io.ist)\n    def readchars(io):\
    \ io.load(); l, io.p = io.p, io.O[io.l]; io.l += 1; return io._dec(l, io.p-1)\n\
    \    def readinto(io, lst):\n        if io.char: return io.readcharsinto(lst)\n\
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
    \ GenericAlias \nfrom typing import Callable, Collection\n\nclass Parser:\n  \
    \  def __init__(self, spec):  self.parse = Parser.compile(spec)\n    def __call__(self,\
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
    \        else:\n            raise NotImplementedError()\nclass Parsable:\n   \
    \ @classmethod\n    def compile(cls):\n        def parser(io: IOBase): return\
    \ cls(next(io))\n        return parser\n    @classmethod\n    def __class_getitem__(cls,\
    \ item): return GenericAlias(cls, item)\n\ndef write(*args, **kwargs):\n    '''Prints\
    \ the values to a stream, or to stdout_fast by default.'''\n    sep, file = kwargs.pop(\"\
    sep\", \" \"), kwargs.pop(\"file\", IO.stdout)\n    at_start = True\n    for x\
    \ in args:\n        if not at_start:\n            file.write(sep)\n        file.write(str(x))\n\
    \        at_start = False\n    file.write(kwargs.pop(\"end\", \"\\n\"))\n    if\
    \ kwargs.pop(\"flush\", False):\n        file.flush()\n\nif __name__ == '__main__':\n\
    \    main()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/pow_of_matrix\n\
    \ndef main():\n    mint.set_mod(998244353)\n    N, K = read()\n    A = ModMat([read()\
    \ for _ in range(N)])\n    B = A**K\n    write(B)\n\nfrom cp_library.math.mod.mint_cls\
    \ import mint\nfrom cp_library.math.linalg.mat.mod.modmat_cls import ModMat\n\
    from cp_library.io.read_fn import read\nfrom cp_library.io.write_fn import write\n\
    \nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - cp_library/math/mod/mint_cls.py
  - cp_library/math/linalg/mat/mod/modmat_cls.py
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/io/io_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/io/io_base_cls.py
  - cp_library/alg/dp/max2_fn.py
  isVerificationFile: true
  path: test/library-checker/linear-algebra/pow_of_matrix_modmat.test.py
  requiredBy: []
  timestamp: '2025-07-28 10:42:29+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/linear-algebra/pow_of_matrix_modmat.test.py
layout: document
redirect_from:
- /verify/test/library-checker/linear-algebra/pow_of_matrix_modmat.test.py
- /verify/test/library-checker/linear-algebra/pow_of_matrix_modmat.test.py.html
title: test/library-checker/linear-algebra/pow_of_matrix_modmat.test.py
---
