---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack_sm_fn.py
    title: cp_library/bit/pack_sm_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/tree/segtree_cls.py
    title: cp_library/ds/tree/segtree_cls.py
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
    PROBLEM: https://judge.yosupo.jp/problem/point_set_range_composite
    links:
    - https://judge.yosupo.jp/problem/point_set_range_composite
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_set_range_composite\n\
    \n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\
    \n             https://kobejean.github.io/cp-library               \n'''\nfrom\
    \ typing import Callable, Generic, Union\nfrom typing import TypeVar\n_T = TypeVar('T')\n\
    \n\n\nclass SegTree(Generic[_T]):\n    def __init__(seg, op: Callable[[_T, _T],\
    \ _T], e: _T, v: Union[int, list[_T]]) -> None:\n        if isinstance(v, int):\
    \ v = [e] * v\n        seg.op, seg.e, seg.n = op, e, (n := len(v))\n        seg.log,\
    \ seg.sz, seg.d = (log := (n-1).bit_length()+1), (sz := 1 << log), [e] * (sz <<\
    \ 1)\n        for i in range(n): seg.d[sz + i] = v[i]\n        for i in range(sz-1,0,-1):\
    \ seg.d[i] = op(seg.d[i<<1], seg.d[i<<1|1])\n\n    def set(seg, p: int, x: _T)\
    \ -> None:\n        seg.d[p := p + seg.sz], op = x, seg.op\n        for _ in range(seg.log):\
    \ seg.d[p:=p>>1] = op(seg.d[p:=p^(p&1)], seg.d[p|1])\n    __setitem__ = set\n\n\
    \    def get(seg, p: int) -> _T:\n        return seg.d[p + seg.sz]\n    __getitem__\
    \ = get\n\n    def prod(seg, l: int, r: int) -> _T:\n        sml = smr = seg.e\n\
    \        l, r = l+seg.sz, r+seg.sz\n        while l < r:\n            if l&1:\
    \ sml, l = seg.op(sml, seg.d[l]), l+1\n            if r&1: smr = seg.op(seg.d[r:=r-1],\
    \ smr)\n            l, r = l >> 1, r >> 1\n        return seg.op(sml, smr)\n\n\
    \    def all_prod(seg) -> _T:\n        return seg.d[1]\n\n    def max_right(seg,\
    \ l: int, f: Callable[[_T], bool]) -> int:\n        assert 0 <= l <= seg.n\n \
    \       assert f(seg.e)\n        if l == seg.n: return seg.n\n        l, op, d,\
    \ sm = l+(sz := seg.sz), seg.op, seg.d, seg.e\n        while True:\n         \
    \   while l&1 == 0: l >>= 1\n            if not f(op(sm, d[l])):\n           \
    \     while l < sz:\n                    if f(op(sm, d[l:=l<<1])): sm, l = op(sm,\
    \ d[l]), l+1\n                return l - sz\n            sm, l = op(sm, d[l]),\
    \ l+1\n            if l&-l == l: return seg.n\n\n    def min_left(seg, r: int,\
    \ f: Callable[[_T], bool]) -> int:\n        assert 0 <= r <= seg.n\n        assert\
    \ f(seg.e)\n        if r == 0: return 0\n        r, op, d, sm = r+(sz := seg.sz),\
    \ seg.op, seg.d, seg.e\n        while True:\n            r -= 1\n            while\
    \ r > 1 and r & 1: r >>= 1\n            if not f(op(d[r], sm)):\n            \
    \    while r < sz:\n                    if f(op(d[r:=r<<1|1], sm)): sm, r = op(d[r],\
    \ sm), r-1\n                return r + 1 - sz\n            sm = op(d[r], sm)\n\
    \            if (r & -r) == r: return 0\n\n\ndef main():\n    mod = 998244353\n\
    \    shift, mask = 30, (1<<30)-1\n    N, Q = read()\n    S = [0]*N\n    for i\
    \ in range(N):\n        c, d = read()\n        S[i] = pack_enc(c, d, shift)\n\
    \    \n    def op(a,b):\n        ac, ad = pack_dec(a, shift, mask)\n        bc,\
    \ bd = pack_dec(b, shift, mask)\n        return pack_enc(ac*bc%mod, (ad*bc+bd)%mod,\
    \ shift)\n    \n    seg = SegTree(op, 1 << shift, S)\n    for _ in range(Q):\n\
    \        t, *q = read()\n        if t == 0:\n            p, c, d = q\n       \
    \     seg.set(p, pack_enc(c, d, shift))\n        else:\n            l, r, x =\
    \ q\n            a, b = pack_dec(seg.prod(l, r), shift, mask)\n            write((a*x+b)%mod)\n\
    \n\n\ndef pack_sm(N: int):\n    s = N.bit_length()\n    return s, (1<<s)-1\n\n\
    def pack_enc(a: int, b: int, s: int):\n    return a << s | b\n    \ndef pack_dec(ab:\
    \ int, s: int, m: int):\n    return ab >> s, ab & m\n\ndef pack_indices(A, s):\n\
    \    return [a << s | i for i,a in enumerate(A)]\n\n\nfrom typing import Iterable,\
    \ Type, Union, overload\nimport typing\nfrom collections import deque\nfrom numbers\
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
    \ = IOWrapper(sys.stdout)\n\nclass TokenStream(Iterator):\n    stream = IOWrapper.stdin\n\
    \n    def __init__(self):\n        self.queue = deque()\n\n    def __next__(self):\n\
    \        if not self.queue: self.queue.extend(self._line())\n        return self.queue.popleft()\n\
    \    \n    def wait(self):\n        if not self.queue: self.queue.extend(self._line())\n\
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
    \ char else TokenStream.default)\n\ndef write(*args, **kwargs):\n    '''Prints\
    \ the values to a stream, or to stdout_fast by default.'''\n    sep, file = kwargs.pop(\"\
    sep\", \" \"), kwargs.pop(\"file\", IOWrapper.stdout)\n    at_start = True\n \
    \   for x in args:\n        if not at_start:\n            file.write(sep)\n  \
    \      file.write(str(x))\n        at_start = False\n    file.write(kwargs.pop(\"\
    end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n        file.flush()\n\
    \nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_set_range_composite\n\
    \nfrom cp_library.ds.tree.segtree_cls import SegTree\n\n\ndef main():\n    mod\
    \ = 998244353\n    shift, mask = 30, (1<<30)-1\n    N, Q = read()\n    S = [0]*N\n\
    \    for i in range(N):\n        c, d = read()\n        S[i] = pack_enc(c, d,\
    \ shift)\n    \n    def op(a,b):\n        ac, ad = pack_dec(a, shift, mask)\n\
    \        bc, bd = pack_dec(b, shift, mask)\n        return pack_enc(ac*bc%mod,\
    \ (ad*bc+bd)%mod, shift)\n    \n    seg = SegTree(op, 1 << shift, S)\n    for\
    \ _ in range(Q):\n        t, *q = read()\n        if t == 0:\n            p, c,\
    \ d = q\n            seg.set(p, pack_enc(c, d, shift))\n        else:\n      \
    \      l, r, x = q\n            a, b = pack_dec(seg.prod(l, r), shift, mask)\n\
    \            write((a*x+b)%mod)\n\nfrom cp_library.bit.pack_sm_fn import pack_dec,\
    \ pack_enc\nfrom cp_library.io.read_fn import read\nfrom cp_library.io.write_fn\
    \ import write\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - cp_library/ds/tree/segtree_cls.py
  - cp_library/bit/pack_sm_fn.py
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: true
  path: test/library-checker/data-structure/point_set_range_composite.test.py
  requiredBy: []
  timestamp: '2025-03-29 18:58:28+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/data-structure/point_set_range_composite.test.py
layout: document
redirect_from:
- /verify/test/library-checker/data-structure/point_set_range_composite.test.py
- /verify/test/library-checker/data-structure/point_set_range_composite.test.py.html
title: test/library-checker/data-structure/point_set_range_composite.test.py
---
