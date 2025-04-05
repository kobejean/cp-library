---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/mo_cls.py
    title: cp_library/alg/dp/mo_cls.py
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
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/abc293/tasks/abc293_g
    links:
    - https://atcoder.jp/contests/abc293/tasks/abc293_g
  bundledCode: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc293/tasks/abc293_g\n\
    \n\ndef main():\n    N, Q = read(tuple[int, ...])\n    A = read(list[int])\n \
    \   mo = read(TripletQueries[Q, N])\n    \n    write(*mo.solve(A), sep='\\n')\n\
    \n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\
    \n             https://kobejean.github.io/cp-library               \n'''\nfrom\
    \ math import isqrt\n\nimport typing\nfrom collections import deque\nfrom numbers\
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
    \   '''Mo[Q: int, N: int, T: type = tuple[int, int]]'''\n    def __init__(self,\
    \ L: list[int], R: list[int], N: int):\n        self.Q = len(L)\n        self.qbits\
    \ = self.Q.bit_length()\n        self.nbits = N.bit_length()\n        self.qmask\
    \ = (1 << self.qbits) - 1\n        self.nmask = (1 << self.nbits) - 1\n      \
    \  \n        self.B = isqrt(N)\n        self.order = [self.packet(i, L[i], R[i])\
    \ for i in range(self.Q)]\n        self.order.sort()\n        self.L = [0]*self.Q\n\
    \        self.R = [0]*self.Q\n        for i,j in enumerate(self.order):\n    \
    \        j &= self.qmask\n            self.order[i] = j\n            self.L[i]\
    \ = L[j]\n            self.R[i] = R[j]\n\n    def packet(self, i: int, l: int,\
    \ r: int) -> int:\n        '''Pack query information into a single integer.'''\n\
    \        b = l//self.B\n        if b & 1:\n            return (((b << self.nbits)\
    \ + self.nmask - r) << self.qbits) + i\n        else:\n            return (((b\
    \ << self.nbits) + r) << self.qbits) + i\n\n    def add(self, i: int):\n     \
    \   '''Add element at index i to current range.'''\n        pass\n\n    def remove(self,\
    \ i: int):\n        '''Remove element at index i from current range.'''\n    \
    \    pass\n\n    def answer(self, i: int, l: int, r: int) -> int:\n        '''Compute\
    \ answer for current range.'''\n        pass\n    \n    def solve(self) -> list[int]:\n\
    \        curr_l = curr_r = 0\n        ans = [0] * self.Q\n        order, L, R\
    \ = self.order, self.L, self.R\n        \n        for i in range(self.Q):\n  \
    \          qid, l, r = order[i], L[i], R[i]\n            \n            if r >\
    \ curr_r:\n                for i in range(curr_r, r):\n                    self.add(i)\n\
    \n            if l < curr_l:\n                for i in range(curr_l-1, l-1, -1):\n\
    \                    self.add(i)\n\n            if l > curr_l:\n             \
    \   for i in range(curr_l, l):\n                    self.remove(i)\n\n       \
    \     if r < curr_r:\n                for i in range(curr_r-1, r-1, -1):\n   \
    \                 self.remove(i)\n                    \n            ans[qid] =\
    \ self.answer(qid, l, r)\n            curr_l, curr_r = l, r\n            \n  \
    \      return ans\n\n    @classmethod\n    def compile(cls, Q: int, N: int, T:\
    \ type = tuple[-1, int]):\n        query = Parser.compile(T)\n        def parse(ts:\
    \ TokenStream):\n            L, R = [0]*Q, [0]*Q\n            for i in range(Q):\n\
    \                L[i], R[i] = query(ts) \n            return cls(L, R, N)\n  \
    \      return parse\n\nfrom typing import Iterable, Type, Union, overload\n\n\
    @overload\ndef read() -> Iterable[int]: ...\n@overload\ndef read(spec: int) ->\
    \ list[int]: ...\n@overload\ndef read(spec: Union[Type[_T],_T], char=False) ->\
    \ _T: ...\ndef read(spec: Union[Type[_T],_T] = None, char=False):\n    if not\
    \ char and spec is None: return map(int, TokenStream.default.line())\n    parser:\
    \ _T = Parser.compile(spec)\n    return parser(CharStream.default if char else\
    \ TokenStream.default)\n\ndef write(*args, **kwargs):\n    '''Prints the values\
    \ to a stream, or to stdout_fast by default.'''\n    sep, file = kwargs.pop(\"\
    sep\", \" \"), kwargs.pop(\"file\", IOWrapper.stdout)\n    at_start = True\n \
    \   for x in args:\n        if not at_start:\n            file.write(sep)\n  \
    \      file.write(str(x))\n        at_start = False\n    file.write(kwargs.pop(\"\
    end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n        file.flush()\n\
    \nclass TripletQueries(Mo):\n    cnt = [0]*200001      \n    pairs = [0]*200001\
    \    \n    triples = 0\n    A: list[int] = None\n\n    def add(self, i):\n   \
    \     v = self.A[i]\n        self.triples += self.pairs[v]    \n        self.pairs[v]\
    \ += self.cnt[v]     \n        self.cnt[v] += 1 \n    \n    def remove(self, i):\n\
    \        v = self.A[i]\n        self.cnt[v] -= 1 \n        self.pairs[v] -= self.cnt[v]\
    \     \n        self.triples -= self.pairs[v]   \n\n    def answer(self, i, l,\
    \ r):\n        return self.triples \n    \n    def solve(self, A):\n        self.A\
    \ = A\n        return super().solve()\n\nif __name__ == \"__main__\":\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc293/tasks/abc293_g\n\
    \n\ndef main():\n    N, Q = read(tuple[int, ...])\n    A = read(list[int])\n \
    \   mo = read(TripletQueries[Q, N])\n    \n    write(*mo.solve(A), sep='\\n')\n\
    \nfrom cp_library.alg.dp.mo_cls import Mo\nfrom cp_library.io.read_fn import read\n\
    from cp_library.io.write_fn import write\n\nclass TripletQueries(Mo):\n    cnt\
    \ = [0]*200001      \n    pairs = [0]*200001    \n    triples = 0\n    A: list[int]\
    \ = None\n\n    def add(self, i):\n        v = self.A[i]\n        self.triples\
    \ += self.pairs[v]    \n        self.pairs[v] += self.cnt[v]     \n        self.cnt[v]\
    \ += 1 \n    \n    def remove(self, i):\n        v = self.A[i]\n        self.cnt[v]\
    \ -= 1 \n        self.pairs[v] -= self.cnt[v]     \n        self.triples -= self.pairs[v]\
    \   \n\n    def answer(self, i, l, r):\n        return self.triples \n    \n \
    \   def solve(self, A):\n        self.A = A\n        return super().solve()\n\n\
    if __name__ == \"__main__\":\n    main()"
  dependsOn:
  - cp_library/alg/dp/mo_cls.py
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: true
  path: test/atcoder/abc/abc261_g_mo.test.py
  requiredBy: []
  timestamp: '2025-04-06 08:06:21+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/atcoder/abc/abc261_g_mo.test.py
layout: document
redirect_from:
- /verify/test/atcoder/abc/abc261_g_mo.test.py
- /verify/test/atcoder/abc/abc261_g_mo.test.py.html
title: test/atcoder/abc/abc261_g_mo.test.py
---
