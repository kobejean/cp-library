---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
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
    path: cp_library/math/mobius_transform_fn.py
    title: cp_library/math/mobius_transform_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/mint_cls.py
    title: cp_library/math/mod/mint_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/mobius_transform_fn.py
    title: cp_library/math/mod/mobius_transform_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/subset_convolution_fn.py
    title: cp_library/math/mod/subset_convolution_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/mod/zeta_transform_fn.py
    title: cp_library/math/mod/zeta_transform_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/subset_convolution_fn.py
    title: cp_library/math/subset_convolution_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/math/zeta_transform_fn.py
    title: cp_library/math/zeta_transform_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
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
    \ import Type, TypeVar, Union, overload\nimport typing\nfrom collections import\
    \ deque\nfrom numbers import Number\nfrom types import GenericAlias \nfrom typing\
    \ import Callable, Collection, Iterator, TypeVar, Union\nimport os\nimport sys\n\
    from io import BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n    BUFSIZE = 8192\n\
    \    newlines = 0\n\n    def __init__(self, file):\n        self._fd = file.fileno()\n\
    \        self.buffer = BytesIO()\n        self.writable = \"x\" in file.mode or\
    \ \"r\" not in file.mode\n        self.write = self.buffer.write if self.writable\
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
    \ = IOWrapper(sys.stdout)\n\n\nclass TokenStream(Iterator):\n    stream = IOWrapper.stdin\n\
    \n    def __init__(self):\n        self.queue = deque()\n\n    def __next__(self):\n\
    \        if not self.queue: self.queue.extend(self.line())\n        return self.queue.popleft()\n\
    \    \n    def wait(self):\n        if not self.queue: self.queue.extend(self.line())\n\
    \        while self.queue: yield\n        \n    def line(self):\n        return\
    \ TokenStream.stream.readline().split()\n\nclass CharStream(TokenStream):\n  \
    \  def line(self):\n        assert not self.queue\n        return next(TokenStream.stream).rstrip()\n\
    \        \nT = TypeVar('T')\nParseFn = Callable[[TokenStream],T]\nclass Parser:\n\
    \    def __init__(self, spec: Union[type[T],T]):\n        self.parse = Parser.compile(spec)\n\
    \n    def __call__(self, ts: TokenStream) -> T:\n        return self.parse(ts)\n\
    \    \n    @staticmethod\n    def compile_type(cls: type[T], args = ()) -> T:\n\
    \        if issubclass(cls, Parsable):\n            return cls.compile(*args)\n\
    \        elif issubclass(cls, (Number, str)):\n            def parse(ts: TokenStream):\n\
    \                return cls(next(ts))              \n            return parse\n\
    \        elif issubclass(cls, tuple):\n            return Parser.compile_tuple(cls,\
    \ args)\n        elif issubclass(cls, Collection):\n            return Parser.compile_collection(cls,\
    \ args)\n        elif callable(cls):\n            def parse(ts: TokenStream):\n\
    \                return cls(next(ts))              \n            return parse\n\
    \        else:\n            raise NotImplementedError()\n    \n    @staticmethod\n\
    \    def compile(spec: Union[type[T],T]=int) -> ParseFn[T]:\n        if isinstance(spec,\
    \ (type, GenericAlias)):\n            cls = typing.get_origin(spec) or spec\n\
    \            args = typing.get_args(spec) or tuple()\n            return Parser.compile_type(cls,\
    \ args)\n        elif isinstance(offset := spec, Number): \n            cls =\
    \ type(spec)  \n            def parse(ts: TokenStream):\n                return\
    \ cls(next(ts)) + offset\n            return parse\n        elif isinstance(args\
    \ := spec, tuple):      \n            return Parser.compile_tuple(type(spec),\
    \ args)\n        elif isinstance(args := spec, Collection):  \n            return\
    \ Parser.compile_collection(type(spec), args)\n        else:\n            raise\
    \ NotImplementedError()\n    \n    @staticmethod\n    def compile_line(cls: T,\
    \ spec=int) -> ParseFn[T]:\n        if spec is int:\n            fn = Parser.compile(spec)\n\
    \            def parse(ts: TokenStream):\n                return cls((int(token)\
    \ for token in ts.line()))\n            return parse\n        else:\n        \
    \    fn = Parser.compile(spec)\n            def parse(ts: TokenStream):\n    \
    \            return cls((fn(ts) for _ in ts.wait()))\n            return parse\n\
    \n    @staticmethod\n    def compile_repeat(cls: T, spec, N) -> ParseFn[T]:\n\
    \        fn = Parser.compile(spec)\n        def parse(ts: TokenStream):\n    \
    \        return cls((fn(ts) for _ in range(N)))\n        return parse\n\n    @staticmethod\n\
    \    def compile_children(cls: T, specs) -> ParseFn[T]:\n        fns = tuple((Parser.compile(spec)\
    \ for spec in specs))\n        def parse(ts: TokenStream):\n            return\
    \ cls((fn(ts) for fn in fns))  \n        return parse\n            \n    @staticmethod\n\
    \    def compile_tuple(cls: type[T], specs) -> ParseFn[T]:\n        if isinstance(specs,\
    \ (tuple,list)) and len(specs) == 2 and specs[1] is ...:\n            return Parser.compile_line(cls,\
    \ specs[0])\n        else:\n            return Parser.compile_children(cls, specs)\n\
    \n    @staticmethod\n    def compile_collection(cls, specs):\n        if not specs\
    \ or len(specs) == 1 or isinstance(specs, set):\n            return Parser.compile_line(cls,\
    \ *specs)\n        elif (isinstance(specs, (tuple,list)) and len(specs) == 2 \n\
    \            and isinstance(specs[1], int)):\n            return Parser.compile_repeat(cls,\
    \ specs[0], specs[1])\n        else:\n            raise NotImplementedError()\n\
    \nclass Parsable:\n    @classmethod\n    def compile(cls):\n        def parser(ts:\
    \ TokenStream):\n            return cls(next(ts))\n        return parser\n\nT\
    \ = TypeVar('T')\n@overload\ndef read() -> list[int]: ...\n@overload\ndef read(spec:\
    \ int) -> list[int]: ...\n@overload\ndef read(spec: Union[Type[T],T], char=False)\
    \ -> T: ...\ndef read(spec: Union[Type[T],T] = None, char=False):\n    if not\
    \ char:\n        if spec is None:\n            return map(int, TokenStream.stream.readline().split())\n\
    \        elif isinstance(offset := spec, int):\n            return [int(s)+offset\
    \ for s in TokenStream.stream.readline().split()]\n        elif spec is int:\n\
    \            return int(TokenStream.stream.readline())\n        else:\n      \
    \      stream = TokenStream()\n    else:\n        stream = CharStream()\n    parser:\
    \ T = Parser.compile(spec)\n    return parser(stream)\n\ndef write(*args, **kwargs):\n\
    \    \"\"\"Prints the values to a stream, or to stdout_fast by default.\"\"\"\n\
    \    sep, file = kwargs.pop(\"sep\", \" \"), kwargs.pop(\"file\", IOWrapper.stdout)\n\
    \    at_start = True\n    for x in args:\n        if not at_start:\n         \
    \   file.write(sep)\n        file.write(str(x))\n        at_start = False\n  \
    \  file.write(kwargs.pop(\"end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n\
    \        file.flush()\nmod = 998244353\n\nN, = read()\nif N < 10:\n    \n    \n\
    \    def subset_convolution(A, B, N):\n        Z = 1 << N\n    \n        # Prepare\
    \ arrays for rank (popcount) decomposition\n        Arank = [[0]*Z for _ in range(N+1)]\n\
    \        Brank = [[0]*Z for _ in range(N+1)]\n    \n        # Initialize rank\
    \ arrays\n        for mask in range(Z):\n            rank = mask.bit_count()\n\
    \            Arank[rank][mask] = A[mask]\n            Brank[rank][mask] = B[mask]\n\
    \    \n        # Zeta transform for each rank\n        for Ar in Arank: zeta_transform(Ar,\
    \ N)\n        for Br in Brank: zeta_transform(Br, N)\n    \n        # Convolution\n\
    \        Crank = [[0 for _ in range(Z)] for _ in range(N+1)]\n        for mask\
    \ in range(Z):\n            L = mask.bit_count()+1\n            for i in range(L):\n\
    \                for j in range(min(L, N+1-i)):\n                    k = i+j\n\
    \                    Crank[k][mask] = Crank[k][mask] + Arank[i][mask] * Brank[j][mask]\n\
    \    \n        # M\xF6bius transform (inverse of Zeta transform)\n        for\
    \ Cr in Crank: mobius_transform(Cr, N)\n            \n        # Combine results\n\
    \        C = [0] * Z\n        for mask in range(Z):\n            rank = mask.bit_count()\n\
    \            C[mask] = Crank[rank][mask]\n    \n        return C\n    \n    \n\
    \    \n    def zeta_transform(A, N, block=5):\n        for i in range(min(block,N)):\n\
    \            for mask in range(bit := 1<<i, 1<<N):\n                if mask &\
    \ bit:\n                    A[mask] += A[mask ^ bit]\n        for i in range(block,N):\n\
    \            for base in range(bit := 1<<i, 1<<N, bit << 1):\n               \
    \ for mask in range(base, base+bit):\n                    A[mask] += A[mask ^\
    \ bit]\n        return A\n    \n    \n    def mobius_transform(A, N, block=5):\n\
    \        for i in range(min(block,N)):\n            for mask in range(bit := 1<<i,\
    \ 1<<N):\n                if mask & bit:\n                    A[mask] -= A[mask\
    \ ^ bit]\n        for i in range(block,N):\n            for base in range(bit\
    \ := 1<<i, 1<<N, bit << 1):\n                for mask in range(base, base+bit):\n\
    \                    A[mask] -= A[mask ^ bit]\n        return A\n    \n    \n\
    \    class mint(int):\n        mod: int\n        zero: 'mint'\n        one: 'mint'\n\
    \        two: 'mint'\n        cache: list['mint']\n    \n        def __new__(cls,\
    \ *args, **kwargs):\n            if (x := int(*args, **kwargs)) <= 2:\n      \
    \          return cls.cache[x]\n            else:\n                return cls.fix(x)\n\
    \    \n        @classmethod\n        def set_mod(cls, mod):\n            cls.mod\
    \ = mod\n            cls.zero = cls.cast(0)\n            cls.one = cls.fix(1)\n\
    \            cls.two = cls.fix(2)\n            cls.cache = [cls.zero, cls.one,\
    \ cls.two]\n    \n        @classmethod\n        def fix(cls, x): return cls.cast(x%cls.mod)\n\
    \    \n        @classmethod\n        def cast(cls, x): return super().__new__(cls,x)\n\
    \    \n        @classmethod\n        def mod_inv(cls, x):\n            a,b,s,t\
    \ = int(x), cls.mod, 1, 0\n            while b: a,b,s,t = b,a%b,t,s-a//b*t\n \
    \           if a == 1: return cls.fix(s)\n            raise ValueError(f\"{x}\
    \ is not invertible in mod {cls.mod}\")\n        \n        @property\n       \
    \ def inv(self): return mint.mod_inv(self)\n    \n        def __add__(self, x):\
    \ return mint.fix(super().__add__(x))\n        def __radd__(self, x): return mint.fix(super().__radd__(x))\n\
    \        def __sub__(self, x): return mint.fix(super().__sub__(x))\n        def\
    \ __rsub__(self, x): return mint.fix(super().__rsub__(x))\n        def __mul__(self,\
    \ x): return mint.fix(super().__mul__(x))\n        def __rmul__(self, x): return\
    \ mint.fix(super().__rmul__(x))\n        def __floordiv__(self, x): return self\
    \ * mint.mod_inv(x)\n        def __rfloordiv__(self, x): return self.inv * x\n\
    \        def __truediv__(self, x): return self * mint.mod_inv(x)\n        def\
    \ __rtruediv__(self, x): return self.inv * x\n        def __pow__(self, x): \n\
    \            return self.cast(super().__pow__(x, self.mod))\n        def __neg__(self):\
    \ return mint.mod-self\n        def __pos__(self): return self\n        def __abs__(self):\
    \ return self\n    \n    mint.set_mod(mod)\n    F = read(list[mint])\n    G =\
    \ read(list[mint])\n    write(*subset_convolution(F, G, N))\nelse:\n    \n   \
    \ \n    def subset_convolution(A, B, N, mod):\n        Z = 1 << N\n    \n    \
    \    # Prepare arrays for rank (popcount) decomposition\n        Arank = [[0]*Z\
    \ for _ in range(N+1)]\n        Brank = [[0]*Z for _ in range(N+1)]\n    \n  \
    \      # Initialize rank arrays\n        for mask in range(Z):\n            rank\
    \ = mask.bit_count()\n            Arank[rank][mask] = A[mask]\n            Brank[rank][mask]\
    \ = B[mask]\n    \n        # Zeta transform for each rank\n        for Ar in Arank:\
    \ zeta_transform(Ar, N, mod)\n        for Br in Brank: zeta_transform(Br, N, mod)\n\
    \    \n        # Convolution\n        Crank = [[0]*Z for _ in range(N+1)]\n  \
    \      for mask in range(Z):\n            L = mask.bit_count()+1\n           \
    \ for i in range(L):\n                for j in range(min(L, N+1-i)):\n       \
    \             k = i+j\n                    Crank[k][mask] = (Crank[k][mask] +\
    \ Arank[i][mask] * Brank[j][mask]) % mod\n    \n        # M\xF6bius transform\
    \ (inverse of Zeta transform)\n        for Cr in Crank: mobius_transform(Cr, N,\
    \ mod)\n            \n        # Combine results\n        C = [0] * Z\n       \
    \ for mask in range(Z):\n            rank = mask.bit_count()\n            C[mask]\
    \ = Crank[rank][mask]\n    \n        return C\n    \n    \n    \n    def zeta_transform(A,\
    \ N, mod, block=5):\n        for i in range(min(block,N)):\n            for mask\
    \ in range(bit := 1<<i, 1<<N):\n                if mask & bit:\n             \
    \       A[mask] = (A[mask] + A[mask ^ bit]) % mod\n        for i in range(block,N):\n\
    \            for base in range(bit := 1<<i, 1<<N, bit << 1):\n               \
    \ for mask in range(base, base+bit):\n                    A[mask] = (A[mask] +\
    \ A[mask ^ bit]) % mod\n        return A\n    \n    \n    def mobius_transform(A,\
    \ N, mod, block=5):\n        for i in range(min(block,N)):\n            for mask\
    \ in range(bit := 1<<i, 1<<N):\n                if mask & bit:\n             \
    \       A[mask] = (A[mask] - A[mask ^ bit]) % mod\n        for i in range(block,N):\n\
    \            for base in range(bit := 1<<i, 1<<N, bit << 1):\n               \
    \ for mask in range(base, base+bit):\n                    A[mask] = (A[mask] -\
    \ A[mask ^ bit]) % mod\n        return A\n    \n    F = read(list[int])\n    G\
    \ = read(list[int])\n    write(*subset_convolution(F, G, N, mod))\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/subset_convolution\n\
    from cp_library.io.read_fn import read\nfrom cp_library.io.write_fn import write\n\
    mod = 998244353\n\nN, = read()\nif N < 10:\n    from cp_library.math.subset_convolution_fn\
    \ import subset_convolution\n    from cp_library.math.mod.mint_cls import mint\n\
    \    mint.set_mod(mod)\n    F = read(list[mint])\n    G = read(list[mint])\n \
    \   write(*subset_convolution(F, G, N))\nelse:\n    from cp_library.math.mod.subset_convolution_fn\
    \ import subset_convolution\n    \n    F = read(list[int])\n    G = read(list[int])\n\
    \    write(*subset_convolution(F, G, N, mod))"
  dependsOn:
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/math/subset_convolution_fn.py
  - cp_library/math/mod/mint_cls.py
  - cp_library/math/mod/subset_convolution_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  - cp_library/math/zeta_transform_fn.py
  - cp_library/math/mobius_transform_fn.py
  - cp_library/math/mod/zeta_transform_fn.py
  - cp_library/math/mod/mobius_transform_fn.py
  isVerificationFile: true
  path: test/subset_convolution.test.py
  requiredBy: []
  timestamp: '2024-12-17 20:59:28+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/subset_convolution.test.py
layout: document
redirect_from:
- /verify/test/subset_convolution.test.py
- /verify/test/subset_convolution.test.py.html
title: test/subset_convolution.test.py
---
