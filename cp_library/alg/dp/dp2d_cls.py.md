---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':question:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: test/abc185_e_dp2d.test.py
    title: test/abc185_e_dp2d.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    from typing import TypeVar, Generic, Container\n\nimport typing\nfrom collections\
    \ import deque\nfrom numbers import Number\nfrom types import GenericAlias \n\
    from typing import Callable, Collection, Iterator, TypeVar, Union\nimport os\n\
    import sys\nfrom io import BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n    BUFSIZE\
    \ = 8192\n    newlines = 0\n\n    def __init__(self, file):\n        self._fd\
    \ = file.fileno()\n        self.buffer = BytesIO()\n        self.writable = \"\
    x\" in file.mode or \"r\" not in file.mode\n        self.write = self.buffer.write\
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
    \ TokenStream):\n            return cls(next(ts))\n        return parser\nfrom\
    \ dataclasses import dataclass\nfrom math import inf\n\nT = TypeVar('T')\n\n@dataclass\n\
    class Transition2D(Generic[T]):\n    di: int\n    dj: int\n    \n    def __call__(self,\
    \ i: int, j: int, src: T, dest: T) -> T:\n        \"\"\"Override this to implement\
    \ transition logic\"\"\"\n        return src  # Default no-op\n    \n    @classmethod\n\
    \    def make(cls, func):\n        class Transition(cls):\n            def __call__(self,\
    \ i: int, j: int, src: T, dest: T) -> T:\n                return func(i,j,src,dest)\n\
    \        return Transition\n    \nT = TypeVar('T')\nclass DynamicProgramming2D(Generic[T],\
    \ Parsable, Container):\n    def __init__(self, rows: int, cols: int, default:\
    \ T = inf):\n        self.rows = rows\n        self.cols = cols\n        self.table\
    \ = default if isinstance(default, list) else [[default] * cols for _ in range(rows)]\n\
    \    \n    def __getitem__(self, pos: tuple[int, int]) -> T:\n        i, j = pos\n\
    \        return self.table[i][j]\n    \n    def __setitem__(self, pos: tuple[int,\
    \ int], value: T) -> None:\n        i, j = pos\n        self.table[i][j] = value\n\
    \n    def __contains__(self, x: object) -> bool:\n        return any(x in row\
    \ for row in self.table)\n    \n    \n    def solve(self, transitions: list[Transition2D[T]])\
    \ -> None:\n        for i in range(self.rows):\n            for j in range(self.cols):\n\
    \                curr_val = self.table[i][j]\n                for trans in transitions:\n\
    \                    ni, nj = i + trans.di, j + trans.dj\n                   \
    \ if 0 <= ni < self.rows and 0 <= nj < self.cols:\n                        self.table[ni][nj]\
    \ = trans(i, j, curr_val, self.table[ni][nj])\n    \n    @classmethod\n    def\
    \ compile(cls, N, M, T = int):\n        table = Parser.compile(list[list[T,M],N])\n\
    \        def parse(ts: TokenStream):\n            return cls(N, M, table(ts))\n\
    \        return parse\n"
  code: "import cp_library.alg.dp.__header__\nfrom typing import TypeVar, Generic,\
    \ Container\nfrom cp_library.io.parser_cls import Parsable, Parser, TokenStream\n\
    from dataclasses import dataclass\nfrom math import inf\n\nT = TypeVar('T')\n\n\
    @dataclass\nclass Transition2D(Generic[T]):\n    di: int\n    dj: int\n    \n\
    \    def __call__(self, i: int, j: int, src: T, dest: T) -> T:\n        \"\"\"\
    Override this to implement transition logic\"\"\"\n        return src  # Default\
    \ no-op\n    \n    @classmethod\n    def make(cls, func):\n        class Transition(cls):\n\
    \            def __call__(self, i: int, j: int, src: T, dest: T) -> T:\n     \
    \           return func(i,j,src,dest)\n        return Transition\n    \nT = TypeVar('T')\n\
    class DynamicProgramming2D(Generic[T], Parsable, Container):\n    def __init__(self,\
    \ rows: int, cols: int, default: T = inf):\n        self.rows = rows\n       \
    \ self.cols = cols\n        self.table = default if isinstance(default, list)\
    \ else [[default] * cols for _ in range(rows)]\n    \n    def __getitem__(self,\
    \ pos: tuple[int, int]) -> T:\n        i, j = pos\n        return self.table[i][j]\n\
    \    \n    def __setitem__(self, pos: tuple[int, int], value: T) -> None:\n  \
    \      i, j = pos\n        self.table[i][j] = value\n\n    def __contains__(self,\
    \ x: object) -> bool:\n        return any(x in row for row in self.table)\n  \
    \  \n    \n    def solve(self, transitions: list[Transition2D[T]]) -> None:\n\
    \        for i in range(self.rows):\n            for j in range(self.cols):\n\
    \                curr_val = self.table[i][j]\n                for trans in transitions:\n\
    \                    ni, nj = i + trans.di, j + trans.dj\n                   \
    \ if 0 <= ni < self.rows and 0 <= nj < self.cols:\n                        self.table[ni][nj]\
    \ = trans(i, j, curr_val, self.table[ni][nj])\n    \n    @classmethod\n    def\
    \ compile(cls, N, M, T = int):\n        table = Parser.compile(list[list[T,M],N])\n\
    \        def parse(ts: TokenStream):\n            return cls(N, M, table(ts))\n\
    \        return parse"
  dependsOn:
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: false
  path: cp_library/alg/dp/dp2d_cls.py
  requiredBy: []
  timestamp: '2024-12-17 07:25:33+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - test/abc185_e_dp2d.test.py
documentation_of: cp_library/alg/dp/dp2d_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/dp/dp2d_cls.py
- /library/cp_library/alg/dp/dp2d_cls.py.html
title: cp_library/alg/dp/dp2d_cls.py
---
