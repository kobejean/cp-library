---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':question:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  - icon: ':question:'
    path: cp_library/io/read_fn.py
    title: cp_library/io/read_fn.py
  - icon: ':question:'
    path: cp_library/io/write_fn.py
    title: cp_library/io/write_fn.py
  - icon: ':question:'
    path: cp_library/math/mod/mint_cls.py
    title: cp_library/math/mod/mint_cls.py
  - icon: ':x:'
    path: cp_library/math/mod/subset_conv_fn.py
    title: cp_library/math/mod/subset_conv_fn.py
  - icon: ':x:'
    path: cp_library/math/subset_conv_fn.py
    title: cp_library/math/subset_conv_fn.py
  - icon: ':x:'
    path: cp_library/math/subset_mobius_fn.py
    title: cp_library/math/subset_mobius_fn.py
  - icon: ':x:'
    path: cp_library/math/subset_zeta_fn.py
    title: cp_library/math/subset_zeta_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/subset_convolution
    links:
    - https://judge.yosupo.jp/problem/subset_convolution
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/subset_convolution\n\
    '''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n   \
    \          https://kobejean.github.io/cp-library               \n'''\n\nfrom typing\
    \ import Iterable, Type, Union, overload\nimport typing\nfrom collections import\
    \ deque\nfrom numbers import Number\nfrom types import GenericAlias \nfrom typing\
    \ import Callable, Collection, Iterator, Union\nimport os\nimport sys\nfrom io\
    \ import BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n    BUFSIZE = 8192\n    newlines\
    \ = 0\n\n    def __init__(self, file):\n        self._fd = file.fileno()\n   \
    \     self.buffer = BytesIO()\n        self.writable = \"x\" in file.mode or \"\
    r\" not in file.mode\n        self.write = self.buffer.write if self.writable\
    \ else None\n\n    def read(self):\n        BUFSIZE = self.BUFSIZE\n        while\
    \ True:\n            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))\n\
    \            if not b:\n                break\n            ptr = self.buffer.tell()\n\
    \            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)\n\
    \        self.newlines = 0\n        return self.buffer.read()\n\n    def readline(self):\n\
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
    ascii\")\n\nsys.stdin = IOWrapper.stdin = IOWrapper(sys.stdin)\nsys.stdout = IOWrapper.stdout\
    \ = IOWrapper(sys.stdout)\nfrom typing import TypeVar\n_T = TypeVar('T')\n\nclass\
    \ TokenStream(Iterator):\n    stream = IOWrapper.stdin\n\n    def __init__(self):\n\
    \        self.queue = deque()\n\n    def __next__(self):\n        if not self.queue:\
    \ self.queue.extend(self._line())\n        return self.queue.popleft()\n    \n\
    \    def wait(self):\n        if not self.queue: self.queue.extend(self._line())\n\
    \        while self.queue: yield\n \n    def _line(self):\n        return TokenStream.stream.readline().split()\n\
    \n    def line(self):\n        if self.queue:\n            A = list(self.queue)\n\
    \            self.queue.clear()\n            return A\n        return self._line()\n\
    TokenStream.default = TokenStream()\n\nclass CharStream(TokenStream):\n    def\
    \ _line(self):\n        return TokenStream.stream.readline().rstrip()\nCharStream.default\
    \ = CharStream()\n\n\nParseFn = Callable[[TokenStream],_T]\nclass Parser:\n  \
    \  def __init__(self, spec: Union[type[_T],_T]):\n        self.parse = Parser.compile(spec)\n\
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
    \ isinstance(args := spec, Collection):  \n            return Parser.compile_collection(type(spec),\
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
    \ return cls(next(ts))\n        return parser\n\n@overload\ndef read() -> Iterable[int]:\
    \ ...\n@overload\ndef read(spec: int) -> list[int]: ...\n@overload\ndef read(spec:\
    \ Union[Type[_T],_T], char=False) -> _T: ...\ndef read(spec: Union[Type[_T],_T]\
    \ = None, char=False):\n    if not char and spec is None: return map(int, TokenStream.default.line())\n\
    \    parser: _T = Parser.compile(spec)\n    return parser(CharStream.default if\
    \ char else TokenStream.default)\n\ndef write(*args, **kwargs):\n    \"\"\"Prints\
    \ the values to a stream, or to stdout_fast by default.\"\"\"\n    sep, file =\
    \ kwargs.pop(\"sep\", \" \"), kwargs.pop(\"file\", IOWrapper.stdout)\n    at_start\
    \ = True\n    for x in args:\n        if not at_start:\n            file.write(sep)\n\
    \        file.write(str(x))\n        at_start = False\n    file.write(kwargs.pop(\"\
    end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n        file.flush()\n\
    mod = 998244353\n\nN, = read()\nif N < 10:\n    \n    \n    def subset_conv(A,\
    \ B, N):\n        Z = 1 << N\n    \n        # Prepare arrays for rank (popcount)\
    \ decomposition\n        Arank = [[0]*Z for _ in range(N+1)]\n        Brank =\
    \ [[0]*Z for _ in range(N+1)]\n    \n        # Initialize rank arrays\n      \
    \  for mask in range(Z):\n            rank = mask.bit_count()\n            Arank[rank][mask]\
    \ = A[mask]\n            Brank[rank][mask] = B[mask]\n    \n        # Zeta transform\
    \ for each rank\n        for Ar in Arank: subset_zeta(Ar, N)\n        for Br in\
    \ Brank: subset_zeta(Br, N)\n    \n        # Convolution\n        Crank = [[0\
    \ for _ in range(Z)] for _ in range(N+1)]\n        for mask in range(Z):\n   \
    \         for i in range(L := mask.bit_count()+1):\n                for j in range(min(L,\
    \ N+1-i)):\n                    k = i+j\n                    Crank[k][mask] =\
    \ Crank[k][mask] + Arank[i][mask] * Brank[j][mask]\n    \n        # M\xF6bius\
    \ transform (inverse of Zeta transform)\n        for Cr in Crank: subset_mobius(Cr,\
    \ N)\n            \n        # Combine results\n        C = [0] * Z\n        for\
    \ mask in range(Z):\n            rank = mask.bit_count()\n            C[mask]\
    \ = Crank[rank][mask]\n    \n        return C\n    \n    \n    \n    def subset_zeta(A,\
    \ N, block=5):\n        for i in range(min(block,N)):\n            for mask in\
    \ range(bit := 1<<i, 1<<N):\n                if mask & bit:\n                \
    \    A[mask] += A[mask ^ bit]\n        for i in range(block,N):\n            for\
    \ base in range(bit := 1<<i, 1<<N, bit << 1):\n                for mask in range(base,\
    \ base+bit):\n                    A[mask] += A[mask ^ bit]\n        return A\n\
    \    \n    \n    def subset_mobius(A, N, block=5):\n        for i in range(min(block,N)):\n\
    \            for mask in range(bit := 1<<i, 1<<N):\n                if mask &\
    \ bit:\n                    A[mask] -= A[mask ^ bit]\n        for i in range(block,N):\n\
    \            for base in range(bit := 1<<i, 1<<N, bit << 1):\n               \
    \ for mask in range(base, base+bit):\n                    A[mask] -= A[mask ^\
    \ bit]\n        return A\n    \n        \n    class mint(int):\n        mod: int\n\
    \        zero: 'mint'\n        one: 'mint'\n        two: 'mint'\n        cache:\
    \ list['mint']\n    \n        def __new__(cls, *args, **kwargs):\n           \
    \ if 0<= (x := int(*args, **kwargs)) <= 2:\n                return cls.cache[x]\n\
    \            else:\n                return cls.fix(x)\n    \n        @classmethod\n\
    \        def set_mod(cls, mod: int):\n            mint.mod = cls.mod = mod\n \
    \           mint.zero = cls.zero = cls.cast(0)\n            mint.one = cls.one\
    \ = cls.fix(1)\n            mint.two = cls.two = cls.fix(2)\n            mint.cache\
    \ = cls.cache = [cls.zero, cls.one, cls.two]\n    \n        @classmethod\n   \
    \     def fix(cls, x): return cls.cast(x%cls.mod)\n    \n        @classmethod\n\
    \        def cast(cls, x): return super().__new__(cls,x)\n    \n        @classmethod\n\
    \        def mod_inv(cls, x):\n            a,b,s,t = int(x), cls.mod, 1, 0\n \
    \           while b: a,b,s,t = b,a%b,t,s-a//b*t\n            if a == 1: return\
    \ cls.fix(s)\n            raise ValueError(f\"{x} is not invertible in mod {cls.mod}\"\
    )\n        \n        @property\n        def inv(self): return mint.mod_inv(self)\n\
    \    \n        def __add__(self, x): return mint.fix(super().__add__(x))\n   \
    \     def __radd__(self, x): return mint.fix(super().__radd__(x))\n        def\
    \ __sub__(self, x): return mint.fix(super().__sub__(x))\n        def __rsub__(self,\
    \ x): return mint.fix(super().__rsub__(x))\n        def __mul__(self, x): return\
    \ mint.fix(super().__mul__(x))\n        def __rmul__(self, x): return mint.fix(super().__rmul__(x))\n\
    \        def __floordiv__(self, x): return self * mint.mod_inv(x)\n        def\
    \ __rfloordiv__(self, x): return self.inv * x\n        def __truediv__(self, x):\
    \ return self * mint.mod_inv(x)\n        def __rtruediv__(self, x): return self.inv\
    \ * x\n        def __pow__(self, x): \n            return self.cast(super().__pow__(x,\
    \ self.mod))\n        def __neg__(self): return mint.mod-self\n        def __pos__(self):\
    \ return self\n        def __abs__(self): return self\n    mint.set_mod(mod)\n\
    \    F = read(list[mint])\n    G = read(list[mint])\n    write(*subset_conv(F,\
    \ G, N))\nelse:\n    \n    \n    def subset_conv(A, B, N, mod):\n        Z = 1\
    \ << N\n    \n        # Prepare arrays for rank (popcount) decomposition\n   \
    \     Arank = [[0]*Z for _ in range(N+1)]\n        Brank = [[0]*Z for _ in range(N+1)]\n\
    \    \n        # Initialize rank arrays\n        for mask in range(Z):\n     \
    \       rank = mask.bit_count()\n            Arank[rank][mask] = A[mask]\n   \
    \         Brank[rank][mask] = B[mask]\n    \n        # Zeta transform for each\
    \ rank\n        for Ar in Arank: subset_zeta(Ar, N, mod)\n        for Br in Brank:\
    \ subset_zeta(Br, N, mod)\n    \n        # Convolution\n        Crank = [[0]*Z\
    \ for _ in range(N+1)]\n        for mask in range(Z):\n            L = mask.bit_count()+1\n\
    \            for i in range(L):\n                for j in range(min(L, N+1-i)):\n\
    \                    k = i+j\n                    Crank[k][mask] = (Crank[k][mask]\
    \ + Arank[i][mask] * Brank[j][mask]) % mod\n    \n        # M\xF6bius transform\
    \ (inverse of Zeta transform)\n        for Cr in Crank: subset_mobius(Cr, N, mod)\n\
    \            \n        # Combine results\n        C = [0] * Z\n        for mask\
    \ in range(Z):\n            rank = mask.bit_count()\n            C[mask] = Crank[rank][mask]\n\
    \    \n        return C\n    \n    from cp_library.math.mod.subset_zeta_fn import\
    \ subset_zeta\n    from cp_library.math.mod.subset_mobius_fn import subset_mobius\n\
    \    \n    F = read(list[int])\n    G = read(list[int])\n    write(*subset_conv(F,\
    \ G, N, mod))\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/subset_convolution\n\
    from cp_library.io.read_fn import read\nfrom cp_library.io.write_fn import write\n\
    mod = 998244353\n\nN, = read()\nif N < 10:\n    from cp_library.math.subset_conv_fn\
    \ import subset_conv\n    from cp_library.math.mod.mint_cls import mint\n    mint.set_mod(mod)\n\
    \    F = read(list[mint])\n    G = read(list[mint])\n    write(*subset_conv(F,\
    \ G, N))\nelse:\n    from cp_library.math.mod.subset_conv_fn import subset_conv\n\
    \    \n    F = read(list[int])\n    G = read(list[int])\n    write(*subset_conv(F,\
    \ G, N, mod))"
  dependsOn:
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/math/subset_conv_fn.py
  - cp_library/math/mod/mint_cls.py
  - cp_library/math/mod/subset_conv_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  - cp_library/math/subset_zeta_fn.py
  - cp_library/math/subset_mobius_fn.py
  isVerificationFile: true
  path: test/library-checker/set-power-series/subset_convolution.test.py
  requiredBy: []
  timestamp: '2025-02-18 02:22:25+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library-checker/set-power-series/subset_convolution.test.py
layout: document
redirect_from:
- /verify/test/library-checker/set-power-series/subset_convolution.test.py
- /verify/test/library-checker/set-power-series/subset_convolution.test.py.html
title: test/library-checker/set-power-series/subset_convolution.test.py
---
