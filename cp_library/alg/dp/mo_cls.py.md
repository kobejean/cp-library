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
  - icon: ':heavy_check_mark:'
    path: test/atcoder/abc/abc261_g_mo.test.py
    title: test/atcoder/abc/abc261_g_mo.test.py
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
    from math import isqrt\n\nimport typing\nfrom collections import deque\nfrom numbers\
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
    \ return cls(next(ts))\n        return parser\n\nclass Mo(list, Parsable):\n \
    \   \"\"\"Mo[Q: int, N: int, T: type = tuple[int, int]]\"\"\"\n    def __init__(self,\
    \ L: list[int], R: list[int], N: int):\n        self.Q = len(L)\n        self.qbits\
    \ = self.Q.bit_length()\n        self.nbits = N.bit_length()\n        self.qmask\
    \ = (1 << self.qbits) - 1\n        self.nmask = (1 << self.nbits) - 1\n      \
    \  \n        self.B = isqrt(N)\n        self.order = [self.packet(i, L[i], R[i])\
    \ for i in range(self.Q)]\n        self.order.sort()\n        self.L = [0]*self.Q\n\
    \        self.R = [0]*self.Q\n        for i,j in enumerate(self.order):\n    \
    \        j &= self.qmask\n            self.order[i] = j\n            self.L[i]\
    \ = L[j]\n            self.R[i] = R[j]\n\n    def packet(self, i: int, l: int,\
    \ r: int) -> int:\n        \"\"\"Pack query information into a single integer.\"\
    \"\"\n        b = l//self.B\n        if b & 1:\n            return (((b << self.nbits)\
    \ + self.nmask - r) << self.qbits) + i\n        else:\n            return (((b\
    \ << self.nbits) + r) << self.qbits) + i\n\n    def add(self, i: int):\n     \
    \   \"\"\"Add element at index i to current range.\"\"\"\n        pass\n\n   \
    \ def remove(self, i: int):\n        \"\"\"Remove element at index i from current\
    \ range.\"\"\"\n        pass\n\n    def answer(self, i: int, l: int, r: int) ->\
    \ int:\n        \"\"\"Compute answer for current range.\"\"\"\n        pass\n\
    \    \n    def solve(self) -> list[int]:\n        curr_l = curr_r = 0\n      \
    \  ans = [0] * self.Q\n        order, L, R = self.order, self.L, self.R\n    \
    \    \n        for i in range(self.Q):\n            qid, l, r = order[i], L[i],\
    \ R[i]\n            \n            if r > curr_r:\n                for i in range(curr_r,\
    \ r):\n                    self.add(i)\n\n            if l < curr_l:\n       \
    \         for i in range(curr_l-1, l-1, -1):\n                    self.add(i)\n\
    \n            if l > curr_l:\n                for i in range(curr_l, l):\n   \
    \                 self.remove(i)\n\n            if r < curr_r:\n             \
    \   for i in range(curr_r-1, r-1, -1):\n                    self.remove(i)\n \
    \                   \n            ans[qid] = self.answer(qid, l, r)\n        \
    \    curr_l, curr_r = l, r\n            \n        return ans\n\n    @classmethod\n\
    \    def compile(cls, Q: int, N: int, T: type = tuple[-1, int]):\n        query\
    \ = Parser.compile(T)\n        def parse(ts: TokenStream):\n            L, R =\
    \ [0]*Q, [0]*Q\n            for i in range(Q):\n                L[i], R[i] = query(ts)\
    \ \n            return cls(L, R, N)\n        return parse\n"
  code: "import cp_library.alg.dp.__header__\nfrom math import isqrt\nfrom cp_library.io.parser_cls\
    \ import Parsable, Parser, TokenStream\n\nclass Mo(list, Parsable):\n    \"\"\"\
    Mo[Q: int, N: int, T: type = tuple[int, int]]\"\"\"\n    def __init__(self, L:\
    \ list[int], R: list[int], N: int):\n        self.Q = len(L)\n        self.qbits\
    \ = self.Q.bit_length()\n        self.nbits = N.bit_length()\n        self.qmask\
    \ = (1 << self.qbits) - 1\n        self.nmask = (1 << self.nbits) - 1\n      \
    \  \n        self.B = isqrt(N)\n        self.order = [self.packet(i, L[i], R[i])\
    \ for i in range(self.Q)]\n        self.order.sort()\n        self.L = [0]*self.Q\n\
    \        self.R = [0]*self.Q\n        for i,j in enumerate(self.order):\n    \
    \        j &= self.qmask\n            self.order[i] = j\n            self.L[i]\
    \ = L[j]\n            self.R[i] = R[j]\n\n    def packet(self, i: int, l: int,\
    \ r: int) -> int:\n        \"\"\"Pack query information into a single integer.\"\
    \"\"\n        b = l//self.B\n        if b & 1:\n            return (((b << self.nbits)\
    \ + self.nmask - r) << self.qbits) + i\n        else:\n            return (((b\
    \ << self.nbits) + r) << self.qbits) + i\n\n    def add(self, i: int):\n     \
    \   \"\"\"Add element at index i to current range.\"\"\"\n        pass\n\n   \
    \ def remove(self, i: int):\n        \"\"\"Remove element at index i from current\
    \ range.\"\"\"\n        pass\n\n    def answer(self, i: int, l: int, r: int) ->\
    \ int:\n        \"\"\"Compute answer for current range.\"\"\"\n        pass\n\
    \    \n    def solve(self) -> list[int]:\n        curr_l = curr_r = 0\n      \
    \  ans = [0] * self.Q\n        order, L, R = self.order, self.L, self.R\n    \
    \    \n        for i in range(self.Q):\n            qid, l, r = order[i], L[i],\
    \ R[i]\n            \n            if r > curr_r:\n                for i in range(curr_r,\
    \ r):\n                    self.add(i)\n\n            if l < curr_l:\n       \
    \         for i in range(curr_l-1, l-1, -1):\n                    self.add(i)\n\
    \n            if l > curr_l:\n                for i in range(curr_l, l):\n   \
    \                 self.remove(i)\n\n            if r < curr_r:\n             \
    \   for i in range(curr_r-1, r-1, -1):\n                    self.remove(i)\n \
    \                   \n            ans[qid] = self.answer(qid, l, r)\n        \
    \    curr_l, curr_r = l, r\n            \n        return ans\n\n    @classmethod\n\
    \    def compile(cls, Q: int, N: int, T: type = tuple[-1, int]):\n        query\
    \ = Parser.compile(T)\n        def parse(ts: TokenStream):\n            L, R =\
    \ [0]*Q, [0]*Q\n            for i in range(Q):\n                L[i], R[i] = query(ts)\
    \ \n            return cls(L, R, N)\n        return parse"
  dependsOn:
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: false
  path: cp_library/alg/dp/mo_cls.py
  requiredBy: []
  timestamp: '2025-03-02 23:16:20+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/abc/abc261_g_mo.test.py
documentation_of: cp_library/alg/dp/mo_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/dp/mo_cls.py
- /library/cp_library/alg/dp/mo_cls.py.html
title: cp_library/alg/dp/mo_cls.py
---
