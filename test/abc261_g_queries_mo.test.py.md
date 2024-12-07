---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/queries_cls.py
    title: cp_library/ds/queries_cls.py
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
    \n\ndef main():\n    N, Q = read()\n    A = read(list[int])\n    queries = read(QueriesMoOps[Q,\
    \ N])\n    \n    # State for counting triples\n    cnt = [0]*200001        \n\
    \    triples = 0           \n    ans = [0]*Q\n    \n    for op in queries:\n \
    \       match op:\n            case (MoOp.ADD_RIGHT | MoOp.ADD_LEFT, start, stop,\
    \ step):\n                for i in range(start, stop, step):\n               \
    \     v = A[i]\n                    c = cnt[v] \n                    triples +=\
    \ c*(c-1)  \n                    cnt[v] += 1   \n            case (MoOp.REMOVE_RIGHT\
    \ | MoOp.REMOVE_LEFT, start, stop, step):\n                for i in range(start,\
    \ stop, step):\n                    v = A[i]\n                    cnt[v] -= 1\
    \       \n                    c = cnt[v]      \n                    triples -=\
    \ c*(c-1)    \n            case (MoOp.ANSWER, i, _, _):\n                ans[i]\
    \ = triples >> 1\n    \n    write(*ans, sep='\\n')\n\nfrom enum import IntEnum,\
    \ auto\nfrom itertools import chain, groupby\n'''\n\u257A\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library\
    \               \n'''\nimport sys\n\n\nimport typing\nfrom collections import\
    \ deque\nfrom numbers import Number\nfrom types import GenericAlias \nfrom typing\
    \ import Callable, Collection, Iterator, TypeVar, Union\nimport os\nfrom io import\
    \ BytesIO, IOBase\n\n\nclass FastIO(IOBase):\n    BUFSIZE = 8192\n    newlines\
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
    \ typing import Iterable, Sequence\n\nclass Queries(list, Parsable):\n    def\
    \ __init__(self, data: Iterable = []):\n        super().__init__((i,*query) for\
    \ i,query in enumerate(data))\n\n    def append(self, query) -> None:\n      \
    \  return super().append((len(self), *query))\n\n    @classmethod\n    def compile(cls,\
    \ N: int, T: type = tuple[int, int]):\n        query = Parser.compile(T)\n   \
    \     def parse(ts: TokenStream):\n            return cls(query(ts) for _ in range(N))\n\
    \        return parse\n\nclass QueriesGrouped(Queries):\n    '''QueriesGrouped[Q:\
    \ int, key = 0, T: type = tuple[int, ...]]'''\n    def __init__(self, queries,\
    \ key = 0):\n        if isinstance(key, int):\n            group_idx = key+1\n\
    \            def wrap_key(row):\n                return row[group_idx]\n     \
    \   else:\n            def wrap_key(row):\n                _, *query = row\n \
    \               return key(query)\n        rows = sorted(((i,*query) for i,query\
    \ in enumerate(queries)), key = wrap_key)\n        groups = [(k, list(g)) for\
    \ k, g in groupby(rows, key = wrap_key)]\n        groups.sort()\n        self.key\
    \ = key\n        \n        list.__init__(self, groups)\n            \n\n    @classmethod\n\
    \    def compile(cls, Q: int, key = 0, T: type = tuple[int, ...]):\n        query\
    \ = Parser.compile(T)\n        def parse(ts: TokenStream):\n            return\
    \ cls((query(ts) for _ in range(Q)), key)\n        return parse\n\nclass QueriesRange(Queries):\n\
    \    '''QueriesRange[Q: int, N: int, key = 0, T: type = tuple[-1, int]]'''\n \
    \   def __init__(self, queries, N: int, key = 0):\n        if isinstance(key,\
    \ int):\n            group_idx = key+1\n            def wrap_key(row):\n     \
    \           return row[group_idx]\n        else:\n            def wrap_key(row):\n\
    \                _, *query = row\n                return key(query)\n        rows\
    \ = list((i,*query) for i,query in enumerate(queries))\n        \n        groups\
    \ = [(k,[]) for k in range(N)]\n        for k, group in groupby(rows, key = wrap_key):\n\
    \            groups[k][1].extend(group)\n        self.key = key\n        \n  \
    \      list.__init__(self, groups)\n\n    @classmethod\n    def compile(cls, Q:\
    \ int, N: int, key = 0, T: type = tuple[-1, int]):\n        query = Parser.compile(T)\n\
    \        def parse(ts: TokenStream):\n            return cls((query(ts) for _\
    \ in range(Q)), N, key)\n        return parse\n\n\nclass MoOp(IntEnum):\n    ADD_LEFT\
    \ = auto()\n    ADD_RIGHT = auto()\n    REMOVE_LEFT = auto()\n    REMOVE_RIGHT\
    \ = auto()\n    ANSWER = auto()\n    \nfrom math import isqrt\n\n\n\ndef elist(est_len:\
    \ int) -> list: ...\ntry:\n    from __pypy__ import newlist_hint\nexcept:\n  \
    \  def newlist_hint(hint):\n        return []\nelist = newlist_hint\n    \n\n\
    class QueriesMoOps(list[tuple],Parsable):\n    \"\"\"\n    QueriesMoOps[Q: int,\
    \ N: int, T: type = tuple[int, int]]\n    Orders queries using Mo's algorithm\
    \ and generates a sequence of operations to process them efficiently.\n    Each\
    \ operation is either moving pointers or answering a query.\n    \n    Uses half-interval\
    \ convention: [left, right)\n    Block size is automatically set to sqrt(N) for\
    \ optimal complexity.\n    \"\"\"\n    \n    def encode(self, i, l, r):\n    \
    \    return (((r << self.nbits) + l) << self.qbits) + i\n    \n    def decode(self,\
    \ bits):\n        r = bits >> self.qbits >> self.nbits\n        l = bits >> self.qbits\
    \ & self.nmask\n        i = bits & self.qmask\n        return i, l, r\n\n    def\
    \ __init__(self, queries: list[tuple[int, int]], N: int):\n        Q = len(queries)\n\
    \        self.qbits = Q.bit_length()\n        self.nbits = N.bit_length()\n  \
    \      self.qmask = (1 << self.qbits)-1\n        self.nmask = (1 << self.nbits)-1\n\
    \n        # Initialize with original queries and their indices\n        B = isqrt(N)\n\
    \        K = (N+B-1)//B\n        buckets = [elist(64) for _ in range(K)]\n   \
    \     for i, (l, r) in enumerate(queries):\n            buckets[l//B].append(self.encode(i,\
    \ l, r))\n        for i, bucket in enumerate(buckets):\n            bucket.sort(reverse=i&1)\n\
    \        \n        \n        # Generate sequence of operations\n        ops =\
    \ elist(3*Q)\n\n        nl = nr = 0\n        \n        for bucket in buckets:\n\
    \            for code in bucket:\n                i, l, r = self.decode(code)\n\
    \                if l < nl:\n                    ops.append((MoOp.ADD_LEFT, nl-1,\
    \ l-1, -1))\n                elif l > nl:\n                    ops.append((MoOp.REMOVE_LEFT,\
    \ nl, l, 1))\n\n                if r > nr:\n                    ops.append((MoOp.ADD_RIGHT,\
    \ nr, r, 1))\n                elif r < nr:\n                    ops.append((MoOp.REMOVE_RIGHT,\
    \ nr-1, r-1, -1))\n                \n                ops.append((MoOp.ANSWER,\
    \ i, l, r))\n                \n                nl, nr = l, r\n        super().__init__(ops)\n\
    \        self.queries = queries\n\n\n    @classmethod\n    def compile(cls, Q:\
    \ int, N: int, T: type = tuple[-1, int]):\n        query = Parser.compile(T)\n\
    \        def parse(ts: TokenStream):\n            return cls([query(ts) for _\
    \ in range(Q)], N)\n        return parse\n\nfrom typing import Type, TypeVar,\
    \ Union, overload\n\nT = TypeVar('T')\n@overload\ndef read() -> list[int]: ...\n\
    @overload\ndef read(spec: int) -> list[int]: ...\n@overload\ndef read(spec: Union[Type[T],T],\
    \ char=False) -> T: ...\ndef read(spec: Union[Type[T],T] = None, char=False):\n\
    \    if not char:\n        if spec is None:\n            return map(int, TokenStream.stream.readline().split())\n\
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
    \        file.flush()\n\nif __name__ == \"__main__\":\n    main()\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc293/tasks/abc293_g\n\
    \n\ndef main():\n    N, Q = read()\n    A = read(list[int])\n    queries = read(QueriesMoOps[Q,\
    \ N])\n    \n    # State for counting triples\n    cnt = [0]*200001        \n\
    \    triples = 0           \n    ans = [0]*Q\n    \n    for op in queries:\n \
    \       match op:\n            case (MoOp.ADD_RIGHT | MoOp.ADD_LEFT, start, stop,\
    \ step):\n                for i in range(start, stop, step):\n               \
    \     v = A[i]\n                    c = cnt[v] \n                    triples +=\
    \ c*(c-1)  \n                    cnt[v] += 1   \n            case (MoOp.REMOVE_RIGHT\
    \ | MoOp.REMOVE_LEFT, start, stop, step):\n                for i in range(start,\
    \ stop, step):\n                    v = A[i]\n                    cnt[v] -= 1\
    \       \n                    c = cnt[v]      \n                    triples -=\
    \ c*(c-1)    \n            case (MoOp.ANSWER, i, _, _):\n                ans[i]\
    \ = triples >> 1\n    \n    write(*ans, sep='\\n')\n\nfrom cp_library.ds.queries_cls\
    \ import QueriesMoOps, MoOp\nfrom cp_library.io.read_fn import read\nfrom cp_library.io.write_fn\
    \ import write\n\nif __name__ == \"__main__\":\n    main()"
  dependsOn:
  - cp_library/ds/queries_cls.py
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/ds/elist_fn.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: true
  path: test/abc261_g_queries_mo.test.py
  requiredBy: []
  timestamp: '2024-12-08 02:40:51+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/abc261_g_queries_mo.test.py
layout: document
redirect_from:
- /verify/test/abc261_g_queries_mo.test.py
- /verify/test/abc261_g_queries_mo.test.py.html
title: test/abc261_g_queries_mo.test.py
---
