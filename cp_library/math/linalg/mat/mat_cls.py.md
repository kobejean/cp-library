---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':warning:'
    path: cp_library/math/linalg/elm_wise_in_place_mixin.py
    title: cp_library/math/linalg/elm_wise_in_place_mixin.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/linalg/elm_wise_mixin.py
    title: cp_library/math/linalg/elm_wise_mixin.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/mint_cls.py
    title: cp_library/math/mod/mint_cls.py
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
    from typing import Container, Sequence\nfrom numbers import Number\n\nimport typing\n\
    from collections import deque\nfrom types import GenericAlias \nfrom typing import\
    \ Callable, Collection, Iterator, Union\nimport os\nimport sys\nfrom io import\
    \ BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n    BUFSIZE = 8192\n    newlines\
    \ = 0\n\n    def __init__(self, file):\n        self._fd = file.fileno()\n   \
    \     self.buffer = BytesIO()\n        self.writable = \"x\" in file.mode or \"\
    r\" not in file.mode\n        self.write = self.buffer.write if self.writable\
    \ else None\n\n    def read(self):\n        BUFSIZE = self.BUFSIZE\n        while\
    \ True:\n            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))\n\
    \            if not b: break\n            ptr = self.buffer.tell()\n         \
    \   self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)\n    \
    \    self.newlines = 0\n        return self.buffer.read()\n\n    def readline(self):\n\
    \        BUFSIZE = self.BUFSIZE\n        while self.newlines == 0:\n         \
    \   b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))\n        \
    \    self.newlines = b.count(b\"\\n\") + (not b)\n            ptr = self.buffer.tell()\n\
    \            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)\n\
    \        self.newlines -= 1\n        return self.buffer.readline()\n\n    def\
    \ flush(self):\n        if self.writable:\n            os.write(self._fd, self.buffer.getvalue())\n\
    \            self.buffer.truncate(0), self.buffer.seek(0)\n\n\nclass IOWrapper(IOBase):\n\
    \    stdin: 'IOWrapper' = None\n    stdout: 'IOWrapper' = None\n    \n    def\
    \ __init__(self, file):\n        self.buffer = FastIO(file)\n        self.flush\
    \ = self.buffer.flush\n        self.writable = self.buffer.writable\n\n    def\
    \ write(self, s):\n        return self.buffer.write(s.encode(\"ascii\"))\n   \
    \ \n    def read(self):\n        return self.buffer.read().decode(\"ascii\")\n\
    \    \n    def readline(self):\n        return self.buffer.readline().decode(\"\
    ascii\")\ntry:\n    sys.stdin = IOWrapper.stdin = IOWrapper(sys.stdin)\n    sys.stdout\
    \ = IOWrapper.stdout = IOWrapper(sys.stdout)\nexcept:\n    pass\nfrom typing import\
    \ TypeVar\n_S = TypeVar('S')\n_T = TypeVar('T')\n_U = TypeVar('U')\n_T1 = TypeVar('T1')\n\
    _T2 = TypeVar('T2')\n_T3 = TypeVar('T3')\n_T4 = TypeVar('T4')\n_T5 = TypeVar('T5')\n\
    _T6 = TypeVar('T6')\n\nclass TokenStream(Iterator):\n    stream = IOWrapper.stdin\n\
    \n    def __init__(self):\n        self.queue = deque()\n\n    def __next__(self):\n\
    \        if not self.queue: self.queue.extend(self._line())\n        return self.queue.popleft()\n\
    \    \n    def wait(self):\n        if not self.queue: self.queue.extend(self._line())\n\
    \        while self.queue: yield\n \n    def _line(self):\n        return TokenStream.stream.readline().split()\n\
    \n    def line(self):\n        if self.queue:\n            A = list(self.queue)\n\
    \            self.queue.clear()\n            return A\n        return self._line()\n\
    TokenStream.default = TokenStream()\n\nclass CharStream(TokenStream):\n    def\
    \ _line(self):\n        return TokenStream.stream.readline().rstrip()\nCharStream.default\
    \ = CharStream()\n\nParseFn = Callable[[TokenStream],_T]\nclass Parser:\n    def\
    \ __init__(self, spec: Union[type[_T],_T]):\n        self.parse = Parser.compile(spec)\n\
    \n    def __call__(self, ts: TokenStream) -> _T:\n        return self.parse(ts)\n\
    \    \n    @staticmethod\n    def compile_type(cls: type[_T], args = ()) -> _T:\n\
    \        if issubclass(cls, Parsable):\n            return cls.compile(*args)\n\
    \        elif issubclass(cls, (Number, str)):\n            def parse(ts: TokenStream):\
    \ return cls(next(ts))              \n            return parse\n        elif issubclass(cls,\
    \ tuple):\n            return Parser.compile_tuple(cls, args)\n        elif issubclass(cls,\
    \ Collection):\n            return Parser.compile_collection(cls, args)\n    \
    \    elif callable(cls):\n            def parse(ts: TokenStream):\n          \
    \      return cls(next(ts))              \n            return parse\n        else:\n\
    \            raise NotImplementedError()\n    \n    @staticmethod\n    def compile(spec:\
    \ Union[type[_T],_T]=int) -> ParseFn[_T]:\n        if isinstance(spec, (type,\
    \ GenericAlias)):\n            cls = typing.get_origin(spec) or spec\n       \
    \     args = typing.get_args(spec) or tuple()\n            return Parser.compile_type(cls,\
    \ args)\n        elif isinstance(offset := spec, Number): \n            cls =\
    \ type(spec)  \n            def parse(ts: TokenStream): return cls(next(ts)) +\
    \ offset\n            return parse\n        elif isinstance(args := spec, tuple):\
    \      \n            return Parser.compile_tuple(type(spec), args)\n        elif\
    \ isinstance(args := spec, Collection):\n            return Parser.compile_collection(type(spec),\
    \ args)\n        elif isinstance(fn := spec, Callable): \n            def parse(ts:\
    \ TokenStream): return fn(next(ts))\n            return parse\n        else:\n\
    \            raise NotImplementedError()\n\n    @staticmethod\n    def compile_line(cls:\
    \ _T, spec=int) -> ParseFn[_T]:\n        if spec is int:\n            fn = Parser.compile(spec)\n\
    \            def parse(ts: TokenStream): return cls([int(token) for token in ts.line()])\n\
    \            return parse\n        else:\n            fn = Parser.compile(spec)\n\
    \            def parse(ts: TokenStream): return cls([fn(ts) for _ in ts.wait()])\n\
    \            return parse\n\n    @staticmethod\n    def compile_repeat(cls: _T,\
    \ spec, N) -> ParseFn[_T]:\n        fn = Parser.compile(spec)\n        def parse(ts:\
    \ TokenStream): return cls([fn(ts) for _ in range(N)])\n        return parse\n\
    \n    @staticmethod\n    def compile_children(cls: _T, specs) -> ParseFn[_T]:\n\
    \        fns = tuple((Parser.compile(spec) for spec in specs))\n        def parse(ts:\
    \ TokenStream): return cls([fn(ts) for fn in fns])  \n        return parse\n \
    \           \n    @staticmethod\n    def compile_tuple(cls: type[_T], specs) ->\
    \ ParseFn[_T]:\n        if isinstance(specs, (tuple,list)) and len(specs) == 2\
    \ and specs[1] is ...:\n            return Parser.compile_line(cls, specs[0])\n\
    \        else:\n            return Parser.compile_children(cls, specs)\n\n   \
    \ @staticmethod\n    def compile_collection(cls, specs):\n        if not specs\
    \ or len(specs) == 1 or isinstance(specs, set):\n            return Parser.compile_line(cls,\
    \ *specs)\n        elif (isinstance(specs, (tuple,list)) and len(specs) == 2 and\
    \ isinstance(specs[1], int)):\n            return Parser.compile_repeat(cls, specs[0],\
    \ specs[1])\n        else:\n            raise NotImplementedError()\n\nclass Parsable:\n\
    \    @classmethod\n    def compile(cls):\n        def parser(ts: TokenStream):\
    \ return cls(next(ts))\n        return parser\n    \n    @classmethod\n    def\
    \ __class_getitem__(cls, item):\n        return GenericAlias(cls, item)\n\n\n\n\
    import operator\nfrom math import hypot\n\n\nclass ElmWiseMixin:\n    def elm_wise(self,\
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
    \ ElmWiseInPlaceMixin):\n\n    def __init__(self, flat, N, M):\n        self.data,\
    \ self.N, self.M = flat, N, M\n\n    def elm_wise(self, other, op):\n        cls\
    \ = type(self)\n        if isinstance(other, Number):\n            return cls([op(elm,\
    \ other) for elm in self.data])\n        if isinstance(other, Sequence):\n   \
    \         return cls([op(self.data[i], elm) for i, elm in enumerate(other)])\n\
    \        raise ValueError(\"Operand must be a number or a tuple of the same length\"\
    )\n    \n    def ielm_wise(self, other, op):\n        data = self.data\n     \
    \   if isinstance(other, Number):\n            for i in range(len(data)):\n  \
    \              data[i] = op(data[i], other)\n        elif isinstance(other, Sequence)\
    \ and len(data) == len(other):\n            for i, elm in enumerate(other):\n\
    \                data[i] = op(data[i], elm)\n        else:\n            raise\
    \ ValueError(\"Operand must be a number or a list of the same length\")\n    \
    \    return self\n\n    def __len__(self):\n        return self.N\n\n    def __getitem__(self,\
    \ ij: tuple[int, int]):\n        i, j = ij\n        return self.data[i*self.M+j]\n\
    \    \n    def __setitem__(self, ij: tuple[int, int], val: int):\n        i, j\
    \ = ij\n        self.data[i*self.M+j] = val\n    \n    def __contains__(self,\
    \ x: int) -> bool:\n        return x in self.data\n\n    def __matmul__(A,B):\n\
    \        assert A.M == B.N, f\"Dimension mismatch {A.M = } {B.N = }\"\n      \
    \  N,M = A.N, B.M\n        cls = type(A)\n        R = cls([0]*(M*N))\n       \
    \ for irow in range(0,N*M,M):\n            for k in range(A.M):\n            \
    \    krow, a = k*M, A.data[irow+k]\n                for j in range(M):\n     \
    \               R.data[irow+j] = B.data[krow+j]*a + R.data[irow+j]\n        return\
    \ R\n    \n    def __pow__(A,K):\n        R = A[:] if K & 1 else type(A).identity(A.N)\n\
    \        for i in range(1,K.bit_length()):\n            A = A @ A\n          \
    \  if K >> i & 1:\n                R = R @ A\n        return R \n\n    @classmethod\n\
    \    def identity(cls, N):\n        data = [0]*(N*N)\n        for i in range(0,N*N,N+1):\
    \ data[i] = 1\n        return cls(data)\n    \n    def copy(self):\n        cls\
    \ = type(self)\n        obj = cls.__new__(cls)\n        obj.N, obj.M, obj.data\
    \ = self.N, self.M, self.data\n        return obj\n    \n    @classmethod\n  \
    \  def compile(cls, N: int, M: int, T: type = int):\n        elm, size = Parser.compile(T),\
    \ N*M\n        def parse(ts: TokenStream):\n            return cls([elm(ts) for\
    \ _ in range(size)])\n        return parse\n    \n    def __repr__(self) -> str:\n\
    \        return '\\n'.join(' '.join(str(elm) for elm in row) for row in self)\n\
    \n\n    \nclass mint(int):\n    mod: int\n    zero: 'mint'\n    one: 'mint'\n\
    \    two: 'mint'\n    cache: list['mint']\n\n    def __new__(cls, *args, **kwargs):\n\
    \        if 0 <= (x := int(*args, **kwargs)) < 64:\n            return cls.cache[x]\n\
    \        else:\n            return cls.fix(x)\n\n    @classmethod\n    def set_mod(cls,\
    \ mod: int):\n        mint.mod = cls.mod = mod\n        mint.zero = cls.zero =\
    \ cls.cast(0)\n        mint.one = cls.one = cls.fix(1)\n        mint.two = cls.two\
    \ = cls.fix(2)\n        mint.cache = cls.cache = [cls.zero, cls.one, cls.two]\n\
    \        for x in range(3,64): mint.cache.append(cls.fix(x))\n\n    @classmethod\n\
    \    def fix(cls, x): return cls.cast(x%cls.mod)\n\n    @classmethod\n    def\
    \ cast(cls, x): return super().__new__(cls,x)\n\n    @classmethod\n    def mod_inv(cls,\
    \ x):\n        a,b,s,t = int(x), cls.mod, 1, 0\n        while b: a,b,s,t = b,a%b,t,s-a//b*t\n\
    \        if a == 1: return cls.fix(s)\n        raise ValueError(f\"{x} is not\
    \ invertible in mod {cls.mod}\")\n    \n    @property\n    def inv(self): return\
    \ mint.mod_inv(self)\n\n    def __add__(self, x): return mint.fix(super().__add__(x))\n\
    \    def __radd__(self, x): return mint.fix(super().__radd__(x))\n    def __sub__(self,\
    \ x): return mint.fix(super().__sub__(x))\n    def __rsub__(self, x): return mint.fix(super().__rsub__(x))\n\
    \    def __mul__(self, x): return mint.fix(super().__mul__(x))\n    def __rmul__(self,\
    \ x): return mint.fix(super().__rmul__(x))\n    def __floordiv__(self, x): return\
    \ self * mint.mod_inv(x)\n    def __rfloordiv__(self, x): return self.inv * x\n\
    \    def __truediv__(self, x): return self * mint.mod_inv(x)\n    def __rtruediv__(self,\
    \ x): return self.inv * x\n    def __pow__(self, x): \n        return self.cast(super().__pow__(x,\
    \ self.mod))\n    def __neg__(self): return mint.mod-self\n    def __pos__(self):\
    \ return self\n    def __abs__(self): return self\n    def __class_getitem__(self,\
    \ x: int): return self.cache[x]\n"
  code: "import cp_library.__header__\nfrom typing import Container, Sequence\nfrom\
    \ numbers import Number\nfrom cp_library.io.parser_cls import Parsable, Parser,\
    \ TokenStream\nimport cp_library.math.__header__\nimport cp_library.math.linalg.__header__\n\
    from cp_library.math.linalg.elm_wise_in_place_mixin import ElmWiseInPlaceMixin\n\
    import cp_library.math.linalg.mat.__header__\n\nclass Mat(Parsable, Container,\
    \ ElmWiseInPlaceMixin):\n\n    def __init__(self, flat, N, M):\n        self.data,\
    \ self.N, self.M = flat, N, M\n\n    def elm_wise(self, other, op):\n        cls\
    \ = type(self)\n        if isinstance(other, Number):\n            return cls([op(elm,\
    \ other) for elm in self.data])\n        if isinstance(other, Sequence):\n   \
    \         return cls([op(self.data[i], elm) for i, elm in enumerate(other)])\n\
    \        raise ValueError(\"Operand must be a number or a tuple of the same length\"\
    )\n    \n    def ielm_wise(self, other, op):\n        data = self.data\n     \
    \   if isinstance(other, Number):\n            for i in range(len(data)):\n  \
    \              data[i] = op(data[i], other)\n        elif isinstance(other, Sequence)\
    \ and len(data) == len(other):\n            for i, elm in enumerate(other):\n\
    \                data[i] = op(data[i], elm)\n        else:\n            raise\
    \ ValueError(\"Operand must be a number or a list of the same length\")\n    \
    \    return self\n\n    def __len__(self):\n        return self.N\n\n    def __getitem__(self,\
    \ ij: tuple[int, int]):\n        i, j = ij\n        return self.data[i*self.M+j]\n\
    \    \n    def __setitem__(self, ij: tuple[int, int], val: int):\n        i, j\
    \ = ij\n        self.data[i*self.M+j] = val\n    \n    def __contains__(self,\
    \ x: int) -> bool:\n        return x in self.data\n\n    def __matmul__(A,B):\n\
    \        assert A.M == B.N, f\"Dimension mismatch {A.M = } {B.N = }\"\n      \
    \  N,M = A.N, B.M\n        cls = type(A)\n        R = cls([0]*(M*N))\n       \
    \ for irow in range(0,N*M,M):\n            for k in range(A.M):\n            \
    \    krow, a = k*M, A.data[irow+k]\n                for j in range(M):\n     \
    \               R.data[irow+j] = B.data[krow+j]*a + R.data[irow+j]\n        return\
    \ R\n    \n    def __pow__(A,K):\n        R = A[:] if K & 1 else type(A).identity(A.N)\n\
    \        for i in range(1,K.bit_length()):\n            A = A @ A\n          \
    \  if K >> i & 1:\n                R = R @ A\n        return R \n\n    @classmethod\n\
    \    def identity(cls, N):\n        data = [0]*(N*N)\n        for i in range(0,N*N,N+1):\
    \ data[i] = 1\n        return cls(data)\n    \n    def copy(self):\n        cls\
    \ = type(self)\n        obj = cls.__new__(cls)\n        obj.N, obj.M, obj.data\
    \ = self.N, self.M, self.data\n        return obj\n    \n    @classmethod\n  \
    \  def compile(cls, N: int, M: int, T: type = int):\n        elm, size = Parser.compile(T),\
    \ N*M\n        def parse(ts: TokenStream):\n            return cls([elm(ts) for\
    \ _ in range(size)])\n        return parse\n    \n    def __repr__(self) -> str:\n\
    \        return '\\n'.join(' '.join(str(elm) for elm in row) for row in self)\n\
    \nfrom cp_library.math.mod.mint_cls import mint"
  dependsOn:
  - cp_library/io/parser_cls.py
  - cp_library/math/linalg/elm_wise_in_place_mixin.py
  - cp_library/math/mod/mint_cls.py
  - cp_library/io/fast_io_cls.py
  - cp_library/math/linalg/elm_wise_mixin.py
  isVerificationFile: false
  path: cp_library/math/linalg/mat/mat_cls.py
  requiredBy: []
  timestamp: '2025-07-20 06:26:01+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/math/linalg/mat/mat_cls.py
layout: document
redirect_from:
- /library/cp_library/math/linalg/mat/mat_cls.py
- /library/cp_library/math/linalg/mat/mat_cls.py.html
title: cp_library/math/linalg/mat/mat_cls.py
---
