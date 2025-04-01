---
data:
  _extendedDependsOn:
  - icon: ':question:'
    path: cp_library/alg/iter/argsort_fn.py
    title: cp_library/alg/iter/argsort_fn.py
  - icon: ':question:'
    path: cp_library/bit/pack_sm_fn.py
    title: cp_library/bit/pack_sm_fn.py
  - icon: ':question:'
    path: cp_library/ds/csr/csr_incremental_cls.py
    title: cp_library/ds/csr/csr_incremental_cls.py
  - icon: ':question:'
    path: cp_library/ds/dsu_cls.py
    title: cp_library/ds/dsu_cls.py
  - icon: ':question:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  - icon: ':question:'
    path: cp_library/io/fast/fast_io_fn.py
    title: cp_library/io/fast/fast_io_fn.py
  - icon: ':question:'
    path: cp_library/io/fast_io_cls.py
    title: cp_library/io/fast_io_cls.py
  - icon: ':question:'
    path: cp_library/io/parser_cls.py
    title: cp_library/io/parser_cls.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/incremental_scc
    links:
    - https://judge.yosupo.jp/problem/incremental_scc
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/incremental_scc\n\
    \ndef main():\n    N, M = rd(), rd()\n    X = rdl(N)\n    U, V = [0]*M, [0]*M\n\
    \    for e in range(M): U[e], V[e] = rd(), rd()\n    W = scc_incremental(N, M,\
    \ U, V)\n    dsu = DSU(N)\n    cur = t = 0\n    mod = 998244353\n    ans = [0]*M\n\
    \    for e in argsort(W):\n        nt = W[e]\n        if nt < 0: continue\n  \
    \      x, y = dsu.merge(U[e], V[e], True)\n        while t < nt-1: ans[t] = cur;\
    \ t += 1\n        if x != y:\n            cur = (cur+X[x]*X[y])%mod\n        \
    \    X[x] = (X[x]+X[y])%mod\n    while t < M: ans[t] = cur; t += 1\n    wtnl(ans)\n\
    \n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\
    \n             https://kobejean.github.io/cp-library               \n'''\n\n\n\
    def pack_sm(N: int):\n    s = N.bit_length()\n    return s, (1<<s)-1\n\ndef pack_enc(a:\
    \ int, b: int, s: int):\n    return a << s | b\n    \ndef pack_dec(ab: int, s:\
    \ int, m: int):\n    return ab >> s, ab & m\n\ndef pack_indices(A, s):\n    return\
    \ [a << s | i for i,a in enumerate(A)]\n\ndef argsort(A: list[int], reverse=False):\n\
    \    s, m = pack_sm(len(A))\n    if reverse:\n        I = [a<<s|i^m for i,a in\
    \ enumerate(A)]\n        I.sort(reverse=True)\n        for i,ai in enumerate(I):\
    \ I[i] = (ai^m)&m\n    else:\n        I = [a<<s|i for i,a in enumerate(A)]\n \
    \       I.sort()\n        for i,ai in enumerate(I): I[i] = ai&m\n    return I\n\
    from typing import Collection\n\nimport typing\nfrom collections import deque\n\
    from numbers import Number\nfrom types import GenericAlias \nfrom typing import\
    \ Callable, Collection, Iterator, Union\nimport os\nimport sys\nfrom io import\
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
    \ return cls(next(ts))\n        return parser\n\nfrom typing import Sequence\n\
    \n\nclass CSRIncremental(Sequence[list[_T]]):\n    def __init__(csr, sizes: list[int]):\n\
    \        csr.L, N = [0]*len(sizes), 0\n        for i,sz in enumerate(sizes):\n\
    \            csr.L[i] = N; N += sz\n        csr.R, csr.A = csr.L[:], [0]*N\n\n\
    \    def append(csr, i: int, x: _T):\n        csr.A[csr.R[i]] = x; csr.R[i] +=\
    \ 1\n    \n    def __iter__(csr):\n        for i,l in enumerate(csr.L):\n    \
    \        yield csr.A[l:csr.R[i]]\n    \n    def __getitem__(csr, i: int) -> _T:\n\
    \        return csr.A[i]\n    \n    def __len__(dsu):\n        return len(dsu.L)\n\
    \n    def range(csr, i: int) -> _T:\n        return range(csr.L[i], csr.R[i])\n\
    \nclass DSU(Parsable, Collection):\n    def __init__(dsu, N):\n        dsu.N,\
    \ dsu.cc, dsu.par = N, N, [-1]*N\n\n    def merge(dsu, u, v, src = False):\n \
    \       x, y = dsu.leader(u), dsu.leader(v)\n        if x == y: return (x,y) if\
    \ src else x\n        if dsu.par[x] > dsu.par[y]: x, y = y, x\n        dsu.par[x]\
    \ += dsu.par[y]; dsu.par[y] = x; dsu.cc -= 1\n        return (x,y) if src else\
    \ x\n\n    def same(dsu, u: int, v: int):\n        return dsu.leader(u) == dsu.leader(v)\n\
    \n    def leader(dsu, i) -> int:\n        p = (par := dsu.par)[i]\n        while\
    \ p >= 0:\n            if par[p] < 0: return p\n            par[i], i, p = par[p],\
    \ par[p], par[par[p]]\n        return i\n\n    def size(dsu, i) -> int:\n    \
    \    return -dsu.par[dsu.leader(i)]\n\n    def groups(dsu) -> CSRIncremental[int]:\n\
    \        sizes, row, p = [0]*dsu.cc, [-1]*dsu.N, 0\n        for i in range(dsu.cc):\n\
    \            while dsu.par[p] >= 0: p += 1\n            sizes[i], row[p] = -dsu.par[p],\
    \ i; p += 1\n        csr = CSRIncremental(sizes)\n        for i in range(dsu.N):\
    \ csr.append(row[dsu.leader(i)], i)\n        return csr\n    \n    __iter__ =\
    \ groups\n    \n    def __len__(dsu):\n        return dsu.cc\n    \n    def __contains__(dsu,\
    \ uv):\n        u, v = uv\n        return dsu.same(u, v)\n    \n    @classmethod\n\
    \    def compile(cls, N: int, M: int, shift = -1):\n        def parse_fn(ts: TokenStream):\n\
    \            dsu = cls(N)\n            for _ in range(M):\n                u,\
    \ v = ts._line()\n                dsu.merge(int(u)+shift, int(v)+shift)\n    \
    \        return dsu\n        return parse_fn\n\ndef elist(est_len: int) -> list:\
    \ ...\ntry:\n    from __pypy__ import newlist_hint\nexcept:\n    def newlist_hint(hint):\n\
    \        return []\nelist = newlist_hint\n    \nfrom __pypy__.builders import\
    \ StringBuilder\nfrom os import read as os_read, write as os_write\nfrom atexit\
    \ import register as atexist_register\n\nclass Fastio:\n    ibuf = bytes()\n \
    \   pil = pir = 0\n    sb = StringBuilder()\n    def load(self):\n        self.ibuf\
    \ = self.ibuf[self.pil:]\n        self.ibuf += os_read(0, 131072)\n        self.pil\
    \ = 0; self.pir = len(self.ibuf)\n    def flush_atexit(self): os_write(1, self.sb.build().encode())\n\
    \    def flush(self):\n        os_write(1, self.sb.build().encode())\n       \
    \ self.sb = StringBuilder()\n    def fastin(self):\n        if self.pir - self.pil\
    \ < 64: self.load()\n        minus = x = 0\n        while self.ibuf[self.pil]\
    \ < 45: self.pil += 1\n        if self.ibuf[self.pil] == 45: minus = 1; self.pil\
    \ += 1\n        while self.ibuf[self.pil] >= 48:\n            x = x * 10 + (self.ibuf[self.pil]\
    \ & 15)\n            self.pil += 1\n        if minus: return -x\n        return\
    \ x\n    def fastin_string(self):\n        if self.pir - self.pil < 64: self.load()\n\
    \        while self.ibuf[self.pil] <= 32: self.pil += 1\n        res = bytearray()\n\
    \        while self.ibuf[self.pil] > 32:\n            if self.pir - self.pil <\
    \ 64: self.load()\n            res.append(self.ibuf[self.pil])\n            self.pil\
    \ += 1\n        return res\n    def fastout(self, x): self.sb.append(str(x))\n\
    \    def fastoutln(self, x): self.sb.append(str(x)); self.sb.append('\\n')\nfastio\
    \ = Fastio()\nrd = fastio.fastin; rds = fastio.fastin_string; wt = fastio.fastout;\
    \ wtn = fastio.fastoutln; flush = fastio.flush\natexist_register(fastio.flush_atexit)\n\
    sys.stdin = None; sys.stdout = None\ndef rdl(n): return [rd() for _ in range(n)]\n\
    def wtnl(l): wtn(' '.join(map(str, l)))\n\nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/incremental_scc\n\
    \ndef main():\n    N, M = rd(), rd()\n    X = rdl(N)\n    U, V = [0]*M, [0]*M\n\
    \    for e in range(M): U[e], V[e] = rd(), rd()\n    W = scc_incremental(N, M,\
    \ U, V)\n    dsu = DSU(N)\n    cur = t = 0\n    mod = 998244353\n    ans = [0]*M\n\
    \    for e in argsort(W):\n        nt = W[e]\n        if nt < 0: continue\n  \
    \      x, y = dsu.merge(U[e], V[e], True)\n        while t < nt-1: ans[t] = cur;\
    \ t += 1\n        if x != y:\n            cur = (cur+X[x]*X[y])%mod\n        \
    \    X[x] = (X[x]+X[y])%mod\n    while t < M: ans[t] = cur; t += 1\n    wtnl(ans)\n\
    \nfrom cp_library.alg.iter.argsort_fn import argsort\nfrom cp_library.ds.dsu_cls\
    \ import DSU\nfrom cp_library.ds.elist_fn import elist\nfrom cp_library.io.fast.fast_io_fn\
    \ import rd, rdl, wtnl\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - cp_library/alg/iter/argsort_fn.py
  - cp_library/ds/dsu_cls.py
  - cp_library/ds/elist_fn.py
  - cp_library/io/fast/fast_io_fn.py
  - cp_library/bit/pack_sm_fn.py
  - cp_library/io/parser_cls.py
  - cp_library/ds/csr/csr_incremental_cls.py
  - cp_library/io/fast_io_cls.py
  isVerificationFile: true
  path: test/library-checker/graph/incremental_scc.test.py
  requiredBy: []
  timestamp: '2025-04-02 01:29:15+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: test/library-checker/graph/incremental_scc.test.py
layout: document
redirect_from:
- /verify/test/library-checker/graph/incremental_scc.test.py
- /verify/test/library-checker/graph/incremental_scc.test.py.html
title: test/library-checker/graph/incremental_scc.test.py
---
