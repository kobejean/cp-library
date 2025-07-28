---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/alg/dp/max2_fn.py
    title: cp_library/alg/dp/max2_fn.py
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
    path: cp_library/bit/pack/packer_cls.py
    title: cp_library/bit/pack/packer_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/csr/csr_incremental_cls.py
    title: cp_library/ds/csr/csr_incremental_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/dsu_cls.py
    title: cp_library/ds/dsu_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/heap/skew_heap_forrest_cls.py
    title: cp_library/ds/heap/skew_heap_forrest_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/elist_fn.py
    title: cp_library/ds/list/elist_fn.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/io_base_cls.py
    title: cp_library/io/io_base_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/io_cls.py
    title: cp_library/io/io_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/io/parsable_cls.py
    title: cp_library/io/parsable_cls.py
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
    PROBLEM: https://judge.yosupo.jp/problem/directedmst
    links:
    - https://judge.yosupo.jp/problem/directedmst
  bundledCode: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/directedmst\n\
    \ndef main():\n    N, M, S = read()\n    E = read(EdgeListWeighted[N, M, 0])\n\
    \    I = E.edmond(S)\n    if I is None:\n        write(-1)\n    else:\n      \
    \  X = 0; P = [0]*N; P[S] = S\n        for e in I: X += E.W[e]; P[E.V[e]] = E.U[e]\n\
    \        write(X, *P)\n\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2578\n             https://kobejean.github.io/cp-library \
    \              \n'''\nfrom types import GenericAlias\n\n\nclass Parsable:\n  \
    \  @classmethod\n    def compile(cls):\n        def parser(io: 'IOBase'): return\
    \ cls(next(io))\n        return parser\n    @classmethod\n    def __class_getitem__(cls,\
    \ item): return GenericAlias(cls, item)\n\n\n\n\ndef argsort(A: list[int], reverse=False):\n\
    \    P = Packer(len(I := list(A))-1); P.ienumerate(I, reverse); I.sort(); P.iindices(I)\n\
    \    return I\n\n\n\nclass Packer:\n    __slots__ = 's', 'm'\n    def __init__(P,\
    \ mx: int): P.s = mx.bit_length(); P.m = (1 << P.s) - 1\n    def enc(P, a: int,\
    \ b: int): return a << P.s | b\n    def dec(P, x: int) -> tuple[int, int]: return\
    \ x >> P.s, x & P.m\n    def enumerate(P, A, reverse=False): P.ienumerate(A:=list(A),\
    \ reverse); return A\n    def ienumerate(P, A, reverse=False):\n        if reverse:\n\
    \            for i,a in enumerate(A): A[i] = P.enc(-a, i)\n        else:\n   \
    \         for i,a in enumerate(A): A[i] = P.enc(a, i)\n    def indices(P, A: list[int]):\
    \ P.iindices(A:=list(A)); return A\n    def iindices(P, A):\n        for i,a in\
    \ enumerate(A): A[i] = P.m&a\n\n\ndef isort_parallel(*L: list, reverse=False):\n\
    \    inv, order = [0]*len(L[0]), argsort(L[0], reverse=reverse)\n    for i, j\
    \ in enumerate(order): inv[j] = i\n    for i, j in enumerate(order):\n       \
    \ for A in L: A[i], A[j] = A[j], A[i]\n        order[inv[i]], inv[j] = j, inv[i]\n\
    \    return L\n\n\nclass EdgeListWeighted(Parsable):\n    def __init__(E, N: int,\
    \ U: list[int], V: list[int], W: list[int]): E.N, E.M, E.U, E.V, E.W = N, len(U),\
    \ U, V, W\n    def __len__(E): return E.M\n    def __getitem__(E, e): return E.U[e],\
    \ E.V[e], E.W[e]\n    @classmethod\n    def compile(cls, N: int, M: int, I: int\
    \ = -1):\n        def parse(io: IOBase):\n            U, V, W = [0]*M, [0]*M,\
    \ [0]*M\n            for e in range(M): u, v, w = io.readints(); U[e], V[e], W[e]\
    \ = u+I, v+I, w\n            return cls(N, U, V, W)\n        return parse\n  \
    \  def kruskal(E):\n        dsu, I = DSU(E.N), elist(E.N-1)\n        for e in\
    \ argsort(E.W):\n            x, y = dsu.merge(E.U[e], E.V[e])\n            if\
    \ x != y: I.append(e)\n        return I\n    def edmond(E, root):\n        U,\
    \ W, F, pkr, dsu = [0]*E.N, [0]*E.N, SkewHeapForrest(E.N, E.M), Packer(E.M), DSU(E.N)\n\
    \        Ein, stem, cyc, I, C = [-1]*E.M, [-1]*E.N, [], [], []; vis = [0]*E.N;\
    \ vis[root] = 2\n        for e in range(E.M): F.push(E.V[e], pkr.enc(E.W[e], e))\n\
    \        for v in range(E.N):\n            if vis[v := dsu.root(v)]: continue\n\
    \            cycle = 0; C.clear()\n            while vis[v] != 2:\n          \
    \      if F.empty(v): return None\n                vis[v] = 1; cyc.append(v);\
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
    \      return E.__class__(E.N, U, V, W)\n\n\nclass DSU(Parsable):\n    def __init__(dsu,\
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
    \ shift = -1):\n        def parse_fn(io: IOBase):\n            dsu = cls(N)\n\
    \            for _ in range(M): u, v = io.readints(); dsu.merge(u+shift, v+shift)\n\
    \            return dsu\n        return parse_fn\nfrom typing import Sequence\n\
    from typing import TypeVar\n_S = TypeVar('S'); _T = TypeVar('T'); _U = TypeVar('U');\
    \ _T1 = TypeVar('T1'); _T2 = TypeVar('T2'); _T3 = TypeVar('T3'); _T4 = TypeVar('T4');\
    \ _T5 = TypeVar('T5'); _T6 = TypeVar('T6')\n\n\nclass CSRIncremental(Sequence[list[_T]]):\n\
    \    def __init__(csr, sizes: list[int]):\n        csr.L, N = [0]*len(sizes),\
    \ 0\n        for i,sz in enumerate(sizes):\n            csr.L[i] = N; N += sz\n\
    \        csr.R, csr.A = csr.L[:], [0]*N\n\n    def append(csr, i: int, x: _T):\n\
    \        csr.A[csr.R[i]] = x; csr.R[i] += 1\n    \n    def __iter__(csr):\n  \
    \      for i,l in enumerate(csr.L):\n            yield csr.A[l:csr.R[i]]\n   \
    \ \n    def __getitem__(csr, i: int) -> _T:\n        return csr.A[i]\n    \n \
    \   def __len__(dsu):\n        return len(dsu.L)\n\n    def range(csr, i: int)\
    \ -> _T:\n        return range(csr.L[i], csr.R[i])\n\nclass IOBase:\n    @property\n\
    \    def char(io) -> bool: ...\n    @property\n    def writable(io) -> bool: ...\n\
    \    def __next__(io) -> str: ...\n    def write(io, s: str) -> None: ...\n  \
    \  def readline(io) -> str: ...\n    def readtoken(io) -> str: ...\n    def readtokens(io)\
    \ -> list[str]: ...\n    def readints(io) -> list[int]: ...\n    def readdigits(io)\
    \ -> list[int]: ...\n    def readnums(io) -> list[int]: ...\n    def readchar(io)\
    \ -> str: ...\n    def readchars(io) -> str: ...\n    def readinto(io, lst: list[str])\
    \ -> list[str]: ...\n    def readcharsinto(io, lst: list[str]) -> list[str]: ...\n\
    \    def readtokensinto(io, lst: list[str]) -> list[str]: ...\n    def readintsinto(io,\
    \ lst: list[int]) -> list[int]: ...\n    def readdigitsinto(io, lst: list[int])\
    \ -> list[int]: ...\n    def readnumsinto(io, lst: list[int]) -> list[int]: ...\n\
    \    def wait(io): ...\n    def flush(io) -> None: ...\n    def line(io) -> list[str]:\
    \ ...\n\n\ndef elist(est_len: int) -> list: ...\ntry:\n    from __pypy__ import\
    \ newlist_hint\nexcept:\n    def newlist_hint(hint):\n        return []\nelist\
    \ = newlist_hint\n    \nimport operator\nfrom typing import Generic\n\n\nclass\
    \ SkewHeapForrest(Generic[_T]):\n    def __init__(shf, N, M, e: _T = 0, op = operator.add):\n\
    \        shf.V, shf.A, shf.L, shf.R, shf.roots = [e]*M, [e]*M, [-1]*M, [-1]*M,\
    \ [-1]*N\n        shf.id, shf.st, shf.e, shf.op = 0, elist(M), e, op\n    \n \
    \   def propagate(shf, u: int):\n        if (a := shf.A[u]) != shf.e:\n      \
    \      if ~(l := shf.L[u]): shf.A[l] = shf.op(shf.A[l], a)\n            if ~(r\
    \ := shf.R[u]): shf.A[r] = shf.op(shf.A[r], a)\n            shf.V[u] = shf.op(shf.V[u],\
    \ a); shf.A[u] = shf.e\n\n    def merge(shf, u: int, v: int):\n        while ~u\
    \ and ~v:\n            shf.propagate(u); shf.propagate(v)\n            if shf.V[v]\
    \ < shf.V[u]: u, v = v, u\n            shf.st.append(u); shf.R[u], u = shf.L[u],\
    \ shf.R[u]\n        u = u if ~u else v\n        while shf.st: shf.L[u := shf.st.pop()]\
    \ = u\n        return u\n    \n    def min(shf, i: int):\n        assert ~(root\
    \ := shf.roots[i])\n        shf.propagate(root)\n        return shf.V[root]\n\n\
    \    def push(shf, i: int, x: _T):\n        shf.V[shf.id] = x\n        shf.roots[i]\
    \ = shf.merge(shf.roots[i], shf.id)\n        shf.id += 1\n\n    def pop(shf, i:\
    \ int) -> _T:\n        assert ~(root := shf.roots[i])\n        shf.propagate(root)\n\
    \        val, shf.roots[i] = shf.V[root], shf.merge(shf.L[root], shf.R[root])\n\
    \        return val\n    \n    def add(shf, i: int, val: _T): shf.A[shf.roots[i]]\
    \ = shf.op(shf.A[shf.roots[i]], val)\n    def empty(shf, i: int): return shf.roots[i]\
    \ == -1\n    \nfrom typing import Type, Union, overload\n\n@overload\ndef read()\
    \ -> list[int]: ...\n@overload\ndef read(spec: Type[_T], char=False) -> _T: ...\n\
    @overload\ndef read(spec: _U, char=False) -> _U: ...\n@overload\ndef read(*specs:\
    \ Type[_T], char=False) -> tuple[_T, ...]: ...\n@overload\ndef read(*specs: _U,\
    \ char=False) -> tuple[_U, ...]: ...\ndef read(*specs: Union[Type[_T],_T], char=False):\n\
    \    IO.stdin.char = char\n    if not specs: return IO.stdin.readnumsinto([])\n\
    \    parser: _T = Parser.compile(specs[0] if len(specs) == 1 else specs)\n   \
    \ return parser(IO.stdin)\nfrom os import read as os_read, write as os_write,\
    \ fstat as os_fstat\nimport sys\nfrom __pypy__.builders import StringBuilder\n\
    \n\ndef max2(a, b): return a if a > b else b\n\nclass IO(IOBase):\n    BUFSIZE\
    \ = 1 << 16; stdin: 'IO'; stdout: 'IO'\n    __slots__ = 'f', 'file', 'B', 'O',\
    \ 'V', 'S', 'l', 'p', 'char', 'sz', 'st', 'ist', 'writable', 'encoding', 'errors'\n\
    \    def __init__(io, file):\n        io.file = file\n        try: io.f = file.fileno();\
    \ io.sz, io.writable = max2(io.BUFSIZE, os_fstat(io.f).st_size), ('x' in file.mode\
    \ or 'r' not in file.mode)\n        except: io.f, io.sz, io.writable = -1, io.BUFSIZE,\
    \ False\n        io.B, io.O, io.S = bytearray(), [], StringBuilder(); io.V = memoryview(io.B);\
    \ io.l = io.p = 0\n        io.char, io.st, io.ist, io.encoding, io.errors = False,\
    \ [], [], 'ascii', 'ignore'\n    def _dec(io, l, r): return io.V[l:r].tobytes().decode(io.encoding,\
    \ io.errors)\n    def readbytes(io, sz): return os_read(io.f, sz)\n    def load(io):\n\
    \        while io.l >= len(io.O):\n            if not (b := io.readbytes(io.sz)):\n\
    \                if io.O[-1] < len(io.B): io.O.append(len(io.B))\n           \
    \     break\n            pos = len(io.B); io.B.extend(b)\n            while ~(pos\
    \ := io.B.find(b'\\n', pos)): io.O.append(pos := pos+1)\n    def __next__(io):\n\
    \        if io.char: return io.readchar()\n        else: return io.readtoken()\n\
    \    def readchar(io):\n        io.load(); r = io.O[io.l]\n        c = chr(io.B[io.p])\n\
    \        if io.p >= r-1: io.p = r; io.l += 1\n        else: io.p += 1\n      \
    \  return c\n    def write(io, s: str): io.S.append(s)\n    def readline(io):\
    \ io.load(); l, io.p = io.p, io.O[io.l]; io.l += 1; return io._dec(l, io.p)\n\
    \    def readtoken(io):\n        io.load(); r = io.O[io.l]\n        if ~(p :=\
    \ io.B.find(b' ', io.p, r)): s = io._dec(io.p, p); io.p = p+1\n        else: s\
    \ = io._dec(io.p, r-1); io.p = r; io.l += 1\n        return s\n    def readtokens(io):\
    \ io.st.clear(); return io.readtokensinto(io.st)\n    def readints(io): io.ist.clear();\
    \ return io.readintsinto(io.ist)\n    def readdigits(io): io.ist.clear(); return\
    \ io.readdigitsinto(io.ist)\n    def readnums(io): io.ist.clear(); return io.readnumsinto(io.ist)\n\
    \    def readchars(io): io.load(); l, io.p = io.p, io.O[io.l]; io.l += 1; return\
    \ io._dec(l, io.p-1)\n    def readinto(io, lst):\n        if io.char: return io.readcharsinto(lst)\n\
    \        else: return io.readtokensinto(lst)\n    def readcharsinto(io, lst):\
    \ lst.extend(io.readchars()); return lst\n    def readtokensinto(io, lst): \n\
    \        io.load(); r = io.O[io.l]\n        while ~(p := io.B.find(b' ', io.p,\
    \ r)): lst.append(io._dec(io.p, p)); io.p = p+1\n        lst.append(io._dec(io.p,\
    \ r-1)); io.p = r; io.l += 1; return lst\n    def _readint(io, r):\n        while\
    \ io.p < r and io.B[io.p] <= 32: io.p += 1\n        if io.p >= r: return None\n\
    \        minus = x = 0\n        if io.B[io.p] == 45: minus = 1; io.p += 1\n  \
    \      while io.p < r and io.B[io.p] >= 48: x = x * 10 + (io.B[io.p] & 15); io.p\
    \ += 1\n        io.p += 1\n        return -x if minus else x\n    def readintsinto(io,\
    \ lst):\n        io.load(); r = io.O[io.l]\n        while io.p < r and (x := io._readint(r))\
    \ is not None: lst.append(x)\n        io.l += 1; return lst\n    def _readdigit(io):\
    \ d = io.B[io.p] & 15; io.p += 1; return d\n    def readdigitsinto(io, lst):\n\
    \        io.load(); r = io.O[io.l]\n        while io.p < r and io.B[io.p] > 32:\
    \ lst.append(io._readdigit())\n        if io.B[io.p] == 10: io.l += 1\n      \
    \  io.p += 1\n        return lst\n    def readnumsinto(io, lst):\n        if io.char:\
    \ return io.readdigitsinto(lst)\n        else: return io.readintsinto(lst)\n \
    \   def line(io): io.st.clear(); return io.readinto(io.st)\n    def wait(io):\n\
    \        io.load(); r = io.O[io.l]\n        while io.p < r: yield\n    def flush(io):\n\
    \        if io.writable: os_write(io.f, io.S.build().encode(io.encoding, io.errors));\
    \ io.S = StringBuilder()\nsys.stdin = IO.stdin = IO(sys.stdin); sys.stdout = IO.stdout\
    \ = IO(sys.stdout)\nimport typing\nfrom numbers import Number\nfrom typing import\
    \ Callable, Collection\n\nclass Parser:\n    def __init__(self, spec):  self.parse\
    \ = Parser.compile(spec)\n    def __call__(self, io: IOBase): return self.parse(io)\n\
    \    @staticmethod\n    def compile_type(cls, args = ()):\n        if issubclass(cls,\
    \ Parsable): return cls.compile(*args)\n        elif issubclass(cls, (Number,\
    \ str)):\n            def parse(io: IOBase): return cls(next(io))            \
    \  \n            return parse\n        elif issubclass(cls, tuple): return Parser.compile_tuple(cls,\
    \ args)\n        elif issubclass(cls, Collection): return Parser.compile_collection(cls,\
    \ args)\n        elif callable(cls):\n            def parse(io: IOBase): return\
    \ cls(next(io))              \n            return parse\n        else: raise NotImplementedError()\n\
    \    @staticmethod\n    def compile(spec=int):\n        if isinstance(spec, (type,\
    \ GenericAlias)):\n            cls, args = typing.get_origin(spec) or spec, typing.get_args(spec)\
    \ or tuple()\n            return Parser.compile_type(cls, args)\n        elif\
    \ isinstance(offset := spec, Number): \n            cls = type(spec)  \n     \
    \       def parse(io: IOBase): return cls(next(io)) + offset\n            return\
    \ parse\n        elif isinstance(args := spec, tuple): return Parser.compile_tuple(type(spec),\
    \ args)\n        elif isinstance(args := spec, Collection): return Parser.compile_collection(type(spec),\
    \ args)\n        elif isinstance(fn := spec, Callable): \n            def parse(io:\
    \ IOBase): return fn(next(io))\n            return parse\n        else: raise\
    \ NotImplementedError()\n    @staticmethod\n    def compile_line(cls, spec=int):\n\
    \        if spec is int:\n            def parse(io: IOBase): return cls(io.readnums())\n\
    \        elif spec is str:\n            def parse(io: IOBase): return cls(io.line())\n\
    \        else:\n            fn = Parser.compile(spec)\n            def parse(io:\
    \ IOBase): return cls((fn(io) for _ in io.wait()))\n        return parse\n   \
    \ @staticmethod\n    def compile_repeat(cls, spec, N):\n        fn = Parser.compile(spec)\n\
    \        def parse(io: IOBase): return cls([fn(io) for _ in range(N)])\n     \
    \   return parse\n    @staticmethod\n    def compile_children(cls, specs):\n \
    \       fns = tuple((Parser.compile(spec) for spec in specs))\n        def parse(io:\
    \ IOBase): return cls([fn(io) for fn in fns])  \n        return parse\n    @staticmethod\n\
    \    def compile_tuple(cls, specs):\n        if isinstance(specs, (tuple,list))\
    \ and len(specs) == 2 and specs[1] is ...: return Parser.compile_line(cls, specs[0])\n\
    \        else: return Parser.compile_children(cls, specs)\n    @staticmethod\n\
    \    def compile_collection(cls, specs):\n        if not specs or len(specs) ==\
    \ 1 or isinstance(specs, set):\n            return Parser.compile_line(cls, *specs)\n\
    \        elif (isinstance(specs, (tuple,list)) and len(specs) == 2 and isinstance(specs[1],\
    \ int)):\n            return Parser.compile_repeat(cls, specs[0], specs[1])\n\
    \        else:\n            raise NotImplementedError()\n\ndef write(*args, **kwargs):\n\
    \    '''Prints the values to a stream, or to stdout_fast by default.'''\n    sep,\
    \ file = kwargs.pop(\"sep\", \" \"), kwargs.pop(\"file\", IO.stdout)\n    at_start\
    \ = True\n    for x in args:\n        if not at_start:\n            file.write(sep)\n\
    \        file.write(str(x))\n        at_start = False\n    file.write(kwargs.pop(\"\
    end\", \"\\n\"))\n    if kwargs.pop(\"flush\", False):\n        file.flush()\n\
    if __name__ == '__main__':\n    main()\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/directedmst\n\
    \ndef main():\n    N, M, S = read()\n    E = read(EdgeListWeighted[N, M, 0])\n\
    \    I = E.edmond(S)\n    if I is None:\n        write(-1)\n    else:\n      \
    \  X = 0; P = [0]*N; P[S] = S\n        for e in I: X += E.W[e]; P[E.V[e]] = E.U[e]\n\
    \        write(X, *P)\n\nfrom cp_library.alg.graph.edge.edge_list_weighted_cls\
    \ import EdgeListWeighted\nfrom cp_library.io.read_fn import read\nfrom cp_library.io.write_fn\
    \ import write\nif __name__ == '__main__':\n    main()"
  dependsOn:
  - cp_library/alg/graph/edge/edge_list_weighted_cls.py
  - cp_library/io/read_fn.py
  - cp_library/io/write_fn.py
  - cp_library/io/parsable_cls.py
  - cp_library/alg/iter/sort/isort_parallel_fn.py
  - cp_library/alg/iter/arg/argsort_fn.py
  - cp_library/bit/pack/packer_cls.py
  - cp_library/ds/dsu_cls.py
  - cp_library/ds/list/elist_fn.py
  - cp_library/ds/heap/skew_heap_forrest_cls.py
  - cp_library/io/io_base_cls.py
  - cp_library/io/io_cls.py
  - cp_library/io/parser_cls.py
  - cp_library/ds/csr/csr_incremental_cls.py
  - cp_library/alg/dp/max2_fn.py
  isVerificationFile: true
  path: test/library-checker/graph/directedmst_edge_list.test.py
  requiredBy: []
  timestamp: '2025-07-28 19:59:52+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: test/library-checker/graph/directedmst_edge_list.test.py
layout: document
redirect_from:
- /verify/test/library-checker/graph/directedmst_edge_list.test.py
- /verify/test/library-checker/graph/directedmst_edge_list.test.py.html
title: test/library-checker/graph/directedmst_edge_list.test.py
---
