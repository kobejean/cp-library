---
data:
  _extendedDependsOn:
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
    path: cp_library/io/parsable_cls.py
    title: cp_library/io/parsable_cls.py
  _extendedRequiredBy:
  - icon: ':warning:'
    path: perf/edge_list.py
    title: perf/edge_list.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_2_a_edge_list_kruskal.test.py
    title: test/aoj/grl/grl_2_a_edge_list_kruskal.test.py
  - icon: ':heavy_check_mark:'
    path: test/aoj/grl/grl_2_b_edge_list_edmond.test.py
    title: test/aoj/grl/grl_2_b_edge_list_edmond.test.py
  - icon: ':heavy_check_mark:'
    path: test/library-checker/graph/directedmst_edge_list.test.py
    title: test/library-checker/graph/directedmst_edge_list.test.py
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
    from types import GenericAlias\n\n\nclass Parsable:\n    @classmethod\n    def\
    \ compile(cls):\n        def parser(io: 'IOBase'): return cls(next(io))\n    \
    \    return parser\n    @classmethod\n    def __class_getitem__(cls, item): return\
    \ GenericAlias(cls, item)\n\n\n\n\ndef argsort(A: list[int], reverse=False):\n\
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
    \ == -1\n    \n"
  code: "import cp_library.__header__\nfrom cp_library.io.parsable_cls import Parsable\n\
    import cp_library.alg.__header__\nfrom cp_library.alg.iter.sort.isort_parallel_fn\
    \ import isort_parallel\nfrom cp_library.alg.iter.arg.argsort_fn import argsort\n\
    import cp_library.alg.graph.__header__\n\nclass EdgeListWeighted(Parsable):\n\
    \    def __init__(E, N: int, U: list[int], V: list[int], W: list[int]): E.N, E.M,\
    \ E.U, E.V, E.W = N, len(U), U, V, W\n    def __len__(E): return E.M\n    def\
    \ __getitem__(E, e): return E.U[e], E.V[e], E.W[e]\n    @classmethod\n    def\
    \ compile(cls, N: int, M: int, I: int = -1):\n        def parse(io: IOBase):\n\
    \            U, V, W = [0]*M, [0]*M, [0]*M\n            for e in range(M): u,\
    \ v, w = io.readints(); U[e], V[e], W[e] = u+I, v+I, w\n            return cls(N,\
    \ U, V, W)\n        return parse\n    def kruskal(E):\n        dsu, I = DSU(E.N),\
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
    \      return E.__class__(E.N, U, V, W)\nfrom cp_library.bit.pack.packer_cls import\
    \ Packer\nfrom cp_library.ds.dsu_cls import DSU\nfrom cp_library.ds.list.elist_fn\
    \ import elist\nfrom cp_library.ds.heap.skew_heap_forrest_cls import SkewHeapForrest\n\
    from cp_library.io.io_base_cls import IOBase"
  dependsOn:
  - cp_library/io/parsable_cls.py
  - cp_library/alg/iter/sort/isort_parallel_fn.py
  - cp_library/alg/iter/arg/argsort_fn.py
  - cp_library/bit/pack/packer_cls.py
  - cp_library/ds/dsu_cls.py
  - cp_library/ds/list/elist_fn.py
  - cp_library/ds/heap/skew_heap_forrest_cls.py
  - cp_library/io/io_base_cls.py
  - cp_library/ds/csr/csr_incremental_cls.py
  isVerificationFile: false
  path: cp_library/alg/graph/edge/edge_list_weighted_cls.py
  requiredBy:
  - perf/edge_list.py
  timestamp: '2025-07-28 14:17:34+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/library-checker/graph/directedmst_edge_list.test.py
  - test/aoj/grl/grl_2_b_edge_list_edmond.test.py
  - test/aoj/grl/grl_2_a_edge_list_kruskal.test.py
documentation_of: cp_library/alg/graph/edge/edge_list_weighted_cls.py
layout: document
redirect_from:
- /library/cp_library/alg/graph/edge/edge_list_weighted_cls.py
- /library/cp_library/alg/graph/edge/edge_list_weighted_cls.py.html
title: cp_library/alg/graph/edge/edge_list_weighted_cls.py
---
