---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "import operator\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library \
    \              \n'''\nimport typing\nfrom collections import deque\nfrom numbers\
    \ import Number\nfrom types import GenericAlias \nfrom typing import Callable,\
    \ Collection, Iterator, Union\nimport os\nimport sys\nfrom io import BytesIO,\
    \ IOBase\n\n\nclass FastIO(IOBase):\n    BUFSIZE = 8192\n    newlines = 0\n\n\
    \    def __init__(self, file):\n        self._fd = file.fileno()\n        self.buffer\
    \ = BytesIO()\n        self.writable = \"x\" in file.mode or \"r\" not in file.mode\n\
    \        self.write = self.buffer.write if self.writable else None\n\n    def\
    \ read(self):\n        BUFSIZE = self.BUFSIZE\n        while True:\n         \
    \   b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))\n        \
    \    if not b:\n                break\n            ptr = self.buffer.tell()\n\
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
    \ return cls(next(ts))\n        return parser\n\n\nclass PDSU(Parsable):\n   \
    \ \"\"\"PDSU[N: int, M: int, op=operator.sub, inv=operator.neg, e=0, shift=-1]\"\
    \"\"\n\n    def __init__(self, op, inv, e, v) -> None:\n        n = v if isinstance(v,\
    \ int) else len(v)\n        self.n = n\n        self.par = [-1] * n\n        self.op\
    \ = op\n        self.inv = inv\n        self.e = e\n        self.pot = [e] * n\
    \ if isinstance(v, int) else v\n        self.valid = [True] * n\n\n    def leader(self,\
    \ x: int) -> int:\n        assert 0 <= x < self.n\n        path = []\n       \
    \ while self.par[x] >= 0:\n            path.append(x)\n            x = self.par[x]\n\
    \        for y in reversed(path):\n            self.pot[y] = self.op(self.pot[y],\
    \ self.pot[self.par[y]])\n            self.par[y] = x\n        return x\n    \n\
    \    def consistent(self, x: int, y: int, w) -> bool:\n        rx = self.leader(x)\n\
    \        ry = self.leader(y)\n        if rx == ry:\n            return self.op(self.pot[x],\
    \ self.inv(self.pot[y])) == w\n        return True\n\n    def merge(self, x: int,\
    \ y: int, w) -> tuple[int, int]:\n        assert 0 <= x < self.n\n        assert\
    \ 0 <= y < self.n\n        rx = self.leader(x)\n        ry = self.leader(y)\n\
    \        if rx != ry:\n            par = self.par\n            if par[rx] < par[ry]:\n\
    \                x,y,w,rx,ry = y,x,self.inv(w),ry,rx\n                \n     \
    \       par[ry] += par[rx]\n            par[rx] = ry\n            self.pot[rx]\
    \ = self.op(\n                self.op(self.inv(self.pot[x]), w), self.pot[y]\n\
    \            )\n        else:\n            self.valid[rx] &= self.consistent(x,\
    \ y, w)\n        return ry, rx\n\n    def same(self, x: int, y: int) -> bool:\n\
    \        assert 0 <= x < self.n\n        assert 0 <= y < self.n\n        return\
    \ self.leader(x) == self.leader(y)\n    \n    def size(self, x: int) -> int:\n\
    \        assert 0 <= x < self.n\n        return -self.par[self.leader(x)]\n  \
    \  \n    def groups(self):\n        leader_buf = [self.leader(i) for i in range(self.n)]\n\
    \n        result = [[] for _ in range(self.n)]\n        for i in range(self.n):\n\
    \            result[leader_buf[i]].append(i)\n\n        return list(filter(lambda\
    \ r: r, result))\n\n    def diff(self, x: int, y: int):\n        assert self.same(x,\
    \ y)\n        return self.op(self.pot[x], self.inv(self.pot[y]))\n\n    @classmethod\n\
    \    def compile(cls, N: int, M: int, op=operator.sub, inv=operator.neg, e=0,\
    \ shift=-1):\n        def parse(ts: TokenStream):\n            pdsu = cls(op,\
    \ inv, e, N)\n            for _ in range(M):\n                u, v, w = ts._line()\n\
    \                u, v = int(u)+shift, int(v)+shift, int(w)\n                pdsu.merge(u,\
    \ v, w)\n            return pdsu\n        return parse\n"
  code: "import operator\nfrom cp_library.io.parser_cls import Parsable, TokenStream\n\
    import cp_library.ds.__header__\n\nclass PDSU(Parsable):\n    \"\"\"PDSU[N: int,\
    \ M: int, op=operator.sub, inv=operator.neg, e=0, shift=-1]\"\"\"\n\n    def __init__(self,\
    \ op, inv, e, v) -> None:\n        n = v if isinstance(v, int) else len(v)\n \
    \       self.n = n\n        self.par = [-1] * n\n        self.op = op\n      \
    \  self.inv = inv\n        self.e = e\n        self.pot = [e] * n if isinstance(v,\
    \ int) else v\n        self.valid = [True] * n\n\n    def leader(self, x: int)\
    \ -> int:\n        assert 0 <= x < self.n\n        path = []\n        while self.par[x]\
    \ >= 0:\n            path.append(x)\n            x = self.par[x]\n        for\
    \ y in reversed(path):\n            self.pot[y] = self.op(self.pot[y], self.pot[self.par[y]])\n\
    \            self.par[y] = x\n        return x\n    \n    def consistent(self,\
    \ x: int, y: int, w) -> bool:\n        rx = self.leader(x)\n        ry = self.leader(y)\n\
    \        if rx == ry:\n            return self.op(self.pot[x], self.inv(self.pot[y]))\
    \ == w\n        return True\n\n    def merge(self, x: int, y: int, w) -> tuple[int,\
    \ int]:\n        assert 0 <= x < self.n\n        assert 0 <= y < self.n\n    \
    \    rx = self.leader(x)\n        ry = self.leader(y)\n        if rx != ry:\n\
    \            par = self.par\n            if par[rx] < par[ry]:\n             \
    \   x,y,w,rx,ry = y,x,self.inv(w),ry,rx\n                \n            par[ry]\
    \ += par[rx]\n            par[rx] = ry\n            self.pot[rx] = self.op(\n\
    \                self.op(self.inv(self.pot[x]), w), self.pot[y]\n            )\n\
    \        else:\n            self.valid[rx] &= self.consistent(x, y, w)\n     \
    \   return ry, rx\n\n    def same(self, x: int, y: int) -> bool:\n        assert\
    \ 0 <= x < self.n\n        assert 0 <= y < self.n\n        return self.leader(x)\
    \ == self.leader(y)\n    \n    def size(self, x: int) -> int:\n        assert\
    \ 0 <= x < self.n\n        return -self.par[self.leader(x)]\n    \n    def groups(self):\n\
    \        leader_buf = [self.leader(i) for i in range(self.n)]\n\n        result\
    \ = [[] for _ in range(self.n)]\n        for i in range(self.n):\n           \
    \ result[leader_buf[i]].append(i)\n\n        return list(filter(lambda r: r, result))\n\
    \n    def diff(self, x: int, y: int):\n        assert self.same(x, y)\n      \
    \  return self.op(self.pot[x], self.inv(self.pot[y]))\n\n    @classmethod\n  \
    \  def compile(cls, N: int, M: int, op=operator.sub, inv=operator.neg, e=0, shift=-1):\n\
    \        def parse(ts: TokenStream):\n            pdsu = cls(op, inv, e, N)\n\
    \            for _ in range(M):\n                u, v, w = ts._line()\n      \
    \          u, v = int(u)+shift, int(v)+shift, int(w)\n                pdsu.merge(u,\
    \ v, w)\n            return pdsu\n        return parse"
  dependsOn:
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: false
  path: cp_library/ds/tree/pdsu_cls.py
  requiredBy: []
  timestamp: '2025-03-09 20:40:43+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/tree/pdsu_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/tree/pdsu_cls.py
- /library/cp_library/ds/tree/pdsu_cls.py.html
title: cp_library/ds/tree/pdsu_cls.py
---
