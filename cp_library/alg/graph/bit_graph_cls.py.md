---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge_cls.py
    title: cp_library/alg/graph/edge_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/ctz32_fn.py
    title: cp_library/bit/ctz32_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/popcnt32_fn.py
    title: cp_library/bit/popcnt32_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/library-checker/graph/chromatic_number.test.py
    title: test/library-checker/graph/chromatic_number.test.py
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
    from typing import Union\n\n\ndef popcnt32(x):\n    x = ((x >> 1)  & 0x55555555)\
    \ + (x & 0x55555555)\n    x = ((x >> 2)  & 0x33333333) + (x & 0x33333333)\n  \
    \  x = ((x >> 4)  & 0x0f0f0f0f) + (x & 0x0f0f0f0f)\n    x = ((x >> 8)  & 0x00ff00ff)\
    \ + (x & 0x00ff00ff)\n    x = ((x >> 16) & 0x0000ffff) + (x & 0x0000ffff)\n  \
    \  return x\n\ndef ctz32(x): return popcnt32(~x & (x - 1))\n\nimport typing\n\
    from collections import deque\nfrom numbers import Number\nfrom types import GenericAlias\
    \ \nfrom typing import Callable, Collection, Iterator, TypeVar, Union\nimport\
    \ os\nimport sys\nfrom io import BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n\
    \    BUFSIZE = 8192\n    newlines = 0\n\n    def __init__(self, file):\n     \
    \   self._fd = file.fileno()\n        self.buffer = BytesIO()\n        self.writable\
    \ = \"x\" in file.mode or \"r\" not in file.mode\n        self.write = self.buffer.write\
    \ if self.writable else None\n\n    def read(self):\n        BUFSIZE = self.BUFSIZE\n\
    \        while True:\n            b = os.read(self._fd, max(os.fstat(self._fd).st_size,\
    \ BUFSIZE))\n            if not b:\n                break\n            ptr = self.buffer.tell()\n\
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
    \ Parser.compile_collection(type(spec), args)\n        elif isinstance(fn := spec,\
    \ Callable): \n            def parse(ts: TokenStream):\n                return\
    \ fn(next(ts))\n            return parse\n        else:\n            raise NotImplementedError()\n\
    \n    @staticmethod\n    def compile_line(cls: T, spec=int) -> ParseFn[T]:\n \
    \       if spec is int:\n            fn = Parser.compile(spec)\n            def\
    \ parse(ts: TokenStream):\n                return cls((int(token) for token in\
    \ ts.line()))\n            return parse\n        else:\n            fn = Parser.compile(spec)\n\
    \            def parse(ts: TokenStream):\n                return cls((fn(ts) for\
    \ _ in ts.wait()))\n            return parse\n\n    @staticmethod\n    def compile_repeat(cls:\
    \ T, spec, N) -> ParseFn[T]:\n        fn = Parser.compile(spec)\n        def parse(ts:\
    \ TokenStream):\n            return cls((fn(ts) for _ in range(N)))\n        return\
    \ parse\n\n    @staticmethod\n    def compile_children(cls: T, specs) -> ParseFn[T]:\n\
    \        fns = tuple((Parser.compile(spec) for spec in specs))\n        def parse(ts:\
    \ TokenStream):\n            return cls((fn(ts) for fn in fns))  \n        return\
    \ parse\n            \n    @staticmethod\n    def compile_tuple(cls: type[T],\
    \ specs) -> ParseFn[T]:\n        if isinstance(specs, (tuple,list)) and len(specs)\
    \ == 2 and specs[1] is ...:\n            return Parser.compile_line(cls, specs[0])\n\
    \        else:\n            return Parser.compile_children(cls, specs)\n\n   \
    \ @staticmethod\n    def compile_collection(cls, specs):\n        if not specs\
    \ or len(specs) == 1 or isinstance(specs, set):\n            return Parser.compile_line(cls,\
    \ *specs)\n        elif (isinstance(specs, (tuple,list)) and len(specs) == 2 \n\
    \            and isinstance(specs[1], int)):\n            return Parser.compile_repeat(cls,\
    \ specs[0], specs[1])\n        else:\n            raise NotImplementedError()\n\
    \nclass Parsable:\n    @classmethod\n    def compile(cls):\n        def parser(ts:\
    \ TokenStream):\n            return cls(next(ts))\n        return parser\n\nclass\
    \ Edge(tuple, Parsable):\n    @classmethod\n    def compile(cls, I=-1):\n    \
    \    def parse(ts: TokenStream):\n            u,v = ts.line()\n            return\
    \ cls((int(u)+I,int(v)+I))\n        return parse\n\nclass BitGraph(list, Parsable):\n\
    \    def __init__(G, N: int, E: list[Edge]=[]):\n        super().__init__([0]*N)\n\
    \        G.E, G.N, G.M = E, N, len(E)\n        for u,v in E:\n            G[u]\
    \ |= 1 << v\n            G[v] |= 1 << u\n\n    def to_complement(G):\n       \
    \ full = (1 << G.N) - 1\n        for u in range(G.N):\n            G[u] = full\
    \ ^ G[u]\n\n    def chromatic_number(G):\n        Z = 1 << (N := len(G))\n   \
    \     I, coef = [0]*Z, [1]*Z\n        I[0] = 1\n        for S in range(1, Z):\n\
    \            T = 1 << (v := ctz32(S)) ^ S\n            I[S] = I[T] + I[T & ~G[v]]\n\
    \            coef[S] = -1 if popcnt32(S) & 1 else 1\n        for k in range(1,\
    \ N):\n            Pk = 0\n            for S in range(Z):\n                coef[S]\
    \ *= I[S]\n                Pk += coef[S]\n            if Pk != 0: return k\n \
    \       return N\n\n    @classmethod\n    def compile(cls, N: int, M: int, E:\
    \ Union[type,int] = Edge[-1]):\n        if isinstance(E, int): E = Edge[E]\n \
    \       edge = Parser.compile(E)\n        def parse(ts: TokenStream):\n      \
    \      return cls(N, [edge(ts) for _ in range(M)])\n        return parse\n\n \
    \   \n"
  code: "import cp_library.alg.graph.__header__\nfrom typing import Union\nfrom cp_library.bit.popcnt32_fn\
    \ import popcnt32\nfrom cp_library.bit.ctz32_fn import ctz32\nfrom cp_library.alg.graph.edge_cls\
    \ import Edge\nfrom cp_library.io.parser_cls import Parsable, Parser, TokenStream\n\
    \nclass BitGraph(list, Parsable):\n    def __init__(G, N: int, E: list[Edge]=[]):\n\
    \        super().__init__([0]*N)\n        G.E, G.N, G.M = E, N, len(E)\n     \
    \   for u,v in E:\n            G[u] |= 1 << v\n            G[v] |= 1 << u\n\n\
    \    def to_complement(G):\n        full = (1 << G.N) - 1\n        for u in range(G.N):\n\
    \            G[u] = full ^ G[u]\n\n    def chromatic_number(G):\n        Z = 1\
    \ << (N := len(G))\n        I, coef = [0]*Z, [1]*Z\n        I[0] = 1\n       \
    \ for S in range(1, Z):\n            T = 1 << (v := ctz32(S)) ^ S\n          \
    \  I[S] = I[T] + I[T & ~G[v]]\n            coef[S] = -1 if popcnt32(S) & 1 else\
    \ 1\n        for k in range(1, N):\n            Pk = 0\n            for S in range(Z):\n\
    \                coef[S] *= I[S]\n                Pk += coef[S]\n            if\
    \ Pk != 0: return k\n        return N\n\n    @classmethod\n    def compile(cls,\
    \ N: int, M: int, E: Union[type,int] = Edge[-1]):\n        if isinstance(E, int):\
    \ E = Edge[E]\n        edge = Parser.compile(E)\n        def parse(ts: TokenStream):\n\
    \            return cls(N, [edge(ts) for _ in range(M)])\n        return parse\n\
    \n    "
  dependsOn:
  - cp_library/bit/popcnt32_fn.py
  - cp_library/bit/ctz32_fn.py
  - cp_library/alg/graph/edge_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: false
  path: cp_library/alg/graph/bit_graph_cls.py
  requiredBy: []
  timestamp: '2025-01-03 12:10:04+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/graph/chromatic_number.test.py
documentation_of: cp_library/alg/graph/bit_graph_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/bit_graph_cls.py
- /library/cp_library/alg/graph/bit_graph_cls.py.html
title: cp_library/alg/graph/bit_graph_cls.py
---