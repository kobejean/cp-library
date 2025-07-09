---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/graph/edge/edge_list_weighted_cls.py
    title: cp_library/alg/graph/edge/edge_list_weighted_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/arg/argsort_fn.py
    title: argsort
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/sort/isort_parallel_fn.py
    title: cp_library/alg/iter/sort/isort_parallel_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/iter/sort/sort_parallel_fn.py
    title: cp_library/alg/iter/sort/sort_parallel_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/bit/pack/packer_cls.py
    title: cp_library/bit/pack/packer_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/csr/csr_incremental_cls.py
    title: cp_library/ds/csr/csr_incremental_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/dsu_cls.py
    title: cp_library/ds/dsu_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/elist_fn.py
    title: cp_library/ds/elist_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/skew_heap_forrest_cls.py
    title: cp_library/ds/heap/skew_heap_forrest_cls.py
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
    PROBLEM: https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A
    links:
    - https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A
  bundledCode: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A\n\
    \ndef main():\n    N, M = read((int,int))\n    E = read(EdgeListWeighted[N,M,0])\n\
    \    MST = E.sub(E.kruskal())\n    ans = sum(MST.W)\n    write(ans)\n\n'''\n\u257A\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2578\n         \
    \    https://kobejean.github.io/cp-library               \n'''\n\nfrom typing\
    \ import Type, Union, overload\nimport typing\nfrom collections import deque\n\
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
    ascii\")\ntry:\n    sys.stdin = IOWrapper.stdin = IOWrapper(sys.stdin)\n    sys.stdout\
    \ = IOWrapper.stdout = IOWrapper(sys.stdout)\nexcept:\n    pass\nfrom typing import\
    \ TypeVar\n_T = TypeVar('T')\n_U = TypeVar('U')\n\nclass TokenStream(Iterator):\n\
    \    stream = IOWrapper.stdin\n\n    def __init__(self):\n        self.queue =\
    \ deque()\n\n    def __next__(self):\n        if not self.queue: self.queue.extend(self._line())\n\
    \        return self.queue.popleft()\n    \n    def wait(self):\n        if not\
    \ self.queue: self.queue.extend(self._line())\n        while self.queue: yield\n\
    \ \n    def _line(self):\n        return TokenStream.stream.readline().split()\n\
    \n    def line(self):\n        if self.queue:\n            A = list(self.queue)\n\
    \            self.queue.clear()\n            return A\n        return self._line()\n\
    TokenStream.default = TokenStream()\n\nclass CharStream(TokenStream):\n    def\
    \ _line(self):\n        return TokenStream.stream.readline().rstrip()\nCharStream.default\
    \ = CharStream()\n\nParseFn = Callable[[TokenStream],_T]\nclass Parser:\n    def\
    \ __init__(self, spec: Union[type[_T],_T]):\n        self.parse = Parser.compile(spec)\n\
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
    \ isinstance(args := spec, Collection):\n            return Parser.compile_collection(type(spec),\
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
    \ return cls(next(ts))\n        return parser\n    \n    @classmethod\n    def\
    \ __class_getitem__(cls, item):\n        return GenericAlias(cls, item)\n\n@overload\n\
    def read() -> list[int]: ...\n@overload\ndef read(spec: Type[_T], char=False)\
    \ -> _T: ...\n@overload\ndef read(spec: _U, char=False) -> _U: ...\n@overload\n\
    def read(*specs: Type[_T], char=False) -> tuple[_T, ...]: ...\n@overload\ndef\
    \ read(*specs: _U, char=False) -> tuple[_U, ...]: ...\ndef read(*specs: Union[Type[_T],_U],\
    \ char=False):\n    if not char and not specs: return [int(s) for s in TokenStream.default.line()]\n\
    \    parser: _T = Parser.compile(specs[0] if len(specs) == 1 else specs)\n   \
    \ return parser(CharStream.default if char else TokenStream.default)\n\ndef write(*args,\
    \ **kwargs):\n    '''Prints the values to a stream, or to stdout_fast by default.'''\n\
    \    sep, file = kwargs.pop(\"sep\", \" \"), kwargs.pop(\"file\", IOWrapper.stdout)\n\
    \    at_start = True\n    for x in args:\n        if not at_start:\n         \
    \   file.write(sep)\n        file.write(str(x))\n        at_start = False\n  \
    \  file.write(kwargs.pop(\"end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n\
    \        file.flush()\n\n\n\n\ndef argsort(A: list[int], reverse=False):\n   \
    \ P = Packer(len(I := A.copy())-1); P.ienumerate(I, reverse); I.sort(); P.iindices(I)\n\
    \    return I\n\n\n\nclass Packer:\n    def __init__(P, mx: int):\n        P.s\
    \ = mx.bit_length()\n        P.m = (1 << P.s) - 1\n    def enc(P, a: int, b: int):\
    \ return a << P.s | b\n    def dec(P, x: int) -> tuple[int, int]: return x >>\
    \ P.s, x & P.m\n    def enumerate(P, A, reverse=False): P.ienumerate(A:=A.copy(),\
    \ reverse); return A\n    def ienumerate(P, A, reverse=False):\n        if reverse:\n\
    \            for i,a in enumerate(A): A[i] = P.enc(-a, i)\n        else:\n   \
    \         for i,a in enumerate(A): A[i] = P.enc(a, i)\n    def indices(P, A: list[int]):\
    \ P.iindices(A:=A.copy()); return A\n    def iindices(P, A):\n        for i,a\
    \ in enumerate(A): A[i] = P.m&a\n\n\ndef isort_parallel(*L: list, reverse=False):\n\
    \    inv, order = [0]*len(L[0]), argsort(L[0], reverse=reverse)\n    for i, j\
    \ in enumerate(order): inv[j] = i\n    for i, j in enumerate(order):\n       \
    \ for A in L: A[i], A[j] = A[j], A[i]\n        order[inv[i]], inv[j] = j, inv[i]\n\
    \    return L\n\ndef sort_parallel(*L: list, reverse=False):\n    N, K, order\
    \ = len(L[0]), len(L), argsort(L[0], reverse)\n    R = tuple([0]*N for _ in range(K))\n\
    \    for k, Lk in enumerate(L):\n        Rk = R[k]\n        for i, j in enumerate(order):\
    \ Rk[i] = Lk[j]\n    return R\n\n\nclass EdgeListWeighted(Parsable):\n    def\
    \ __init__(E, N: int, U: list[int], V: list[int], W: list[int]): E.N, E.M, E.U,\
    \ E.V, E.W = N, len(U), U, V, W\n    def __len__(E): return E.M\n    def __getitem__(E,\
    \ e): return E.U[e], E.V[e], E.W[e]\n    @classmethod\n    def compile(cls, N:\
    \ int, M: int, I: int = -1):\n        def parse(ts: TokenStream):\n          \
    \  U, V, W = [0]*M, [0]*M, [0]*M\n            for e in range(M): u, v, w = ts.line();\
    \ U[e], V[e], W[e] = int(u)+I, int(v)+I, int(w)\n            return cls(N, U,\
    \ V, W)\n        return parse\n    def kruskal(E):\n        dsu, I = DSU(E.N),\
    \ elist(E.N-1)\n        for e in argsort(E.W):\n            x, y = dsu.merge(E.U[e],\
    \ E.V[e])\n            if x != y: I.append(e)\n        return I\n    def edmond(E,\
    \ root):\n        U, W, F, pkr, dsu = [0]*E.N, [0]*E.N, SkewHeapForrest(E.N, E.M),\
    \ Packer(E.M), DSU(E.N)\n        Ein, stem, cyc, I, C = [-1]*E.M, [-1]*E.N, [],\
    \ [], []; vis = [0]*E.N; vis[root] = 2\n        for e in range(E.M): F.push(E.V[e],\
    \ pkr.enc(E.W[e], e))\n        for v in range(E.N):\n            if vis[v := dsu.root(v)]:\
    \ continue\n            cycle = 0; C.clear()\n            while vis[v] != 2:\n\
    \                if F.empty(v): return None\n                vis[v] = 1; cyc.append(v);\
    \ W[v], e = pkr.dec(F.pop(v)); U[v] = dsu.root(E.U[e])\n                if stem[v]\
    \ == -1: stem[v] = e\n                if U[v] == v: continue\n               \
    \ while cycle: Ein[C.pop()] = e; cycle -= 1\n                I.append(e); C.append(e)\n\
    \                if vis[U[v]] == 1:\n                    if not F.empty(v): F.add(v,\
    \ -W[v]<<pkr.s)\n                    U[v] = p = dsu.root(U[v]); cycle += 1\n \
    \                   while p != v:\n                        if not F.empty(p):\
    \ F.add(p, -W[p]<<pkr.s)\n                        F.roots[v := dsu.merge_dest(v,\
    \ p)] = F.merge(F.roots[v], F.roots[p])\n                        U[p] = p = dsu.root(U[p]);\
    \ cycle += 1\n                else:\n                    v = U[v]\n          \
    \  while cyc: vis[cyc.pop()] = 2\n\n        vis, T = [0]*E.M, []\n        for\
    \ e in reversed(I):\n            if vis[e]: continue\n            f = stem[E.V[e]];\
    \ T.append(e)\n            while f != e: vis[f] = 1; f = Ein[f]\n        return\
    \ T\n    \n    def sort(E):\n        isort_parallel(E.W, E.U, E.V)\n\n    def\
    \ sub(E, I: list[int]):\n        U, V, W = elist(E.N-1), elist(E.N-1), elist(E.N-1)\n\
    \        for e in I: U.append(E.U[e]); V.append(E.V[e]); W.append(E.W[e])\n  \
    \      return E.__class__(E.N, U, V, W)\n\n\n\nclass DSU(Parsable):\n    def __init__(dsu,\
    \ N): dsu.N, dsu.cc, dsu.par = N, N, [-1]*N\n    def merge(dsu, u, v):\n     \
    \   x, y = dsu.root(u), dsu.root(v)\n        if x == y: return x,y\n        if\
    \ dsu.par[x] > dsu.par[y]: x, y = y, x\n        dsu.par[x] += dsu.par[y]; dsu.par[y]\
    \ = x; dsu.cc -= 1\n        return x, y\n    def root(dsu, i) -> int:\n      \
    \  p = (par := dsu.par)[i]\n        while p >= 0:\n            if par[p] < 0:\
    \ return p\n            par[i], i, p = par[p], par[p], par[par[p]]\n        return\
    \ i\n    def groups(dsu) -> 'CSRIncremental[int]':\n        sizes, row, p = [0]*dsu.cc,\
    \ [-1]*dsu.N, 0\n        for i in range(dsu.cc):\n            while dsu.par[p]\
    \ >= 0: p += 1\n            sizes[i], row[p] = -dsu.par[p], i; p += 1\n      \
    \  csr = CSRIncremental(sizes)\n        for i in range(dsu.N): csr.append(row[dsu.root(i)],\
    \ i)\n        return csr\n    __iter__ = groups\n    def merge_dest(dsu, u, v):\
    \ return dsu.merge(u, v)[0]\n    def same(dsu, u: int, v: int):  return dsu.root(u)\
    \ == dsu.root(v)\n    def size(dsu, i) -> int: return -dsu.par[dsu.root(i)]\n\
    \    def __len__(dsu): return dsu.cc\n    def __contains__(dsu, uv): u, v = uv;\
    \ return dsu.same(u, v)\n    @classmethod\n    def compile(cls, N: int, M: int,\
    \ shift = -1):\n        def parse_fn(ts: TokenStream):\n            dsu = cls(N)\n\
    \            for _ in range(M): u, v = ts._line(); dsu.merge(int(u)+shift, int(v)+shift)\n\
    \            return dsu\n        return parse_fn\nfrom typing import Sequence\n\
    \n\nclass CSRIncremental(Sequence[list[_T]]):\n    def __init__(csr, sizes: list[int]):\n\
    \        csr.L, N = [0]*len(sizes), 0\n        for i,sz in enumerate(sizes):\n\
    \            csr.L[i] = N; N += sz\n        csr.R, csr.A = csr.L[:], [0]*N\n\n\
    \    def append(csr, i: int, x: _T):\n        csr.A[csr.R[i]] = x; csr.R[i] +=\
    \ 1\n    \n    def __iter__(csr):\n        for i,l in enumerate(csr.L):\n    \
    \        yield csr.A[l:csr.R[i]]\n    \n    def __getitem__(csr, i: int) -> _T:\n\
    \        return csr.A[i]\n    \n    def __len__(dsu):\n        return len(dsu.L)\n\
    \n    def range(csr, i: int) -> _T:\n        return range(csr.L[i], csr.R[i])\n\
    \ndef elist(est_len: int) -> list: ...\ntry:\n    from __pypy__ import newlist_hint\n\
    except:\n    def newlist_hint(hint):\n        return []\nelist = newlist_hint\n\
    \    \nimport operator\nfrom typing import Generic\n\n\nclass SkewHeapForrest(Generic[_T]):\n\
    \    def __init__(shf, N, M, e: _T = 0, op = operator.add):\n        shf.V, shf.A,\
    \ shf.L, shf.R, shf.roots = [e]*M, [e]*M, [-1]*M, [-1]*M, [-1]*N\n        shf.id,\
    \ shf.st, shf.e, shf.op = 0, elist(M), e, op\n    \n    def propagate(shf, u:\
    \ int):\n        if (a := shf.A[u]) != shf.e:\n            if ~(l := shf.L[u]):\
    \ shf.A[l] = shf.op(shf.A[l], a)\n            if ~(r := shf.R[u]): shf.A[r] =\
    \ shf.op(shf.A[r], a)\n            shf.V[u] = shf.op(shf.V[u], a); shf.A[u] =\
    \ shf.e\n\n    def merge(shf, u: int, v: int):\n        while ~u and ~v:\n   \
    \         shf.propagate(u); shf.propagate(v)\n            if shf.V[v] < shf.V[u]:\
    \ u, v = v, u\n            shf.st.append(u); shf.R[u], u = shf.L[u], shf.R[u]\n\
    \        u = u if ~u else v\n        while shf.st: shf.L[u := shf.st.pop()] =\
    \ u\n        return u\n    \n    def min(shf, i: int):\n        assert ~(root\
    \ := shf.roots[i])\n        shf.propagate(root)\n        return shf.V[root]\n\n\
    \    def push(shf, i: int, x: _T):\n        shf.V[shf.id] = x\n        shf.roots[i]\
    \ = shf.merge(shf.roots[i], shf.id)\n        shf.id += 1\n\n    def pop(shf, i:\
    \ int) -> _T:\n        assert ~(root := shf.roots[i])\n        shf.propagate(root)\n\
    \        val, shf.roots[i] = shf.V[root], shf.merge(shf.L[root], shf.R[root])\n\
    \        return val\n    \n    def add(shf, i: int, val: _T): shf.A[shf.roots[i]]\
    \ = shf.op(shf.A[shf.roots[i]], val)\n    def empty(shf, i: int): return shf.roots[i]\
    \ == -1\n    \n\nif __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A\n\
    \ndef main():\n    N, M = read((int,int))\n    E = read(EdgeListWeighted[N,M,0])\n\
    \    MST = E.sub(E.kruskal())\n    ans = sum(MST.W)\n    write(ans)\n\nfrom cp_library.io.read_fn\
    \ import read\nfrom cp_library.io.write_fn import write\nfrom cp_library.alg.graph.edge.edge_list_weighted_cls\
    \ import EdgeListWeighted\n\nif __name__ == '__main__':\n    main()"
  dependsOn:
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/alg/graph/edge/edge_list_weighted_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/io/fast_io_cls.py
  - cp_library/alg/iter/sort/isort_parallel_fn.py
  - cp_library/alg/iter/sort/sort_parallel_fn.py
  - cp_library/alg/iter/arg/argsort_fn.py
  - cp_library/bit/pack/packer_cls.py
  - cp_library/ds/dsu_cls.py
  - cp_library/ds/elist_fn.py
  - cp_library/ds/heap/skew_heap_forrest_cls.py
  - cp_library/ds/csr/csr_incremental_cls.py
  isVerificationFile: true
  path: test/aoj/grl/grl_2_a_edge_list_kruskal.test.py
  requiredBy: []
  timestamp: '2025-07-10 00:37:15+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/aoj/grl/grl_2_a_edge_list_kruskal.test.py
layout: document
redirect_from:
- /verify/test/aoj/grl/grl_2_a_edge_list_kruskal.test.py
- /verify/test/aoj/grl/grl_2_a_edge_list_kruskal.test.py.html
title: test/aoj/grl/grl_2_a_edge_list_kruskal.test.py
---
