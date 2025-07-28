import cp_library.__header__
from cp_library.io.parsable_cls import Parsable
import cp_library.alg.__header__
from cp_library.alg.iter.sort.isort_parallel_fn import isort_parallel
from cp_library.alg.iter.arg.argsort_fn import argsort
import cp_library.alg.graph.__header__

class EdgeListWeighted(Parsable):
    def __init__(E, N: int, U: list[int], V: list[int], W: list[int]): E.N, E.M, E.U, E.V, E.W = N, len(U), U, V, W
    def __len__(E): return E.M
    def __getitem__(E, e): return E.U[e], E.V[e], E.W[e]
    @classmethod
    def compile(cls, N: int, M: int, I: int = -1):
        def parse(io: IOBase):
            U, V, W = [0]*M, [0]*M, [0]*M
            for e in range(M): u, v, w = io.readints(); U[e], V[e], W[e] = u+I, v+I, w
            return cls(N, U, V, W)
        return parse
    def kruskal(E):
        dsu, I = DSU(E.N), elist(E.N-1)
        for e in argsort(E.W):
            x, y = dsu.merge(E.U[e], E.V[e])
            if x != y: I.append(e)
        return I
    def edmond(E, root):
        U, W, F, pkr, dsu = [0]*E.N, [0]*E.N, SkewHeapForrest(E.N, E.M), Packer(E.M), DSU(E.N)
        Ein, stem, cyc, I, C = [-1]*E.M, [-1]*E.N, [], [], []; vis = [0]*E.N; vis[root] = 2
        for e in range(E.M): F.push(E.V[e], pkr.enc(E.W[e], e))
        for v in range(E.N):
            if vis[v := dsu.root(v)]: continue
            cycle = 0; C.clear()
            while vis[v] != 2:
                if F.empty(v): return None
                vis[v] = 1; cyc.append(v); W[v], e = pkr.dec(F.pop(v)); U[v] = dsu.root(E.U[e])
                if stem[v] == -1: stem[v] = e
                if U[v] == v: continue
                while cycle: Ein[C.pop()] = e; cycle -= 1
                I.append(e); C.append(e)
                if vis[U[v]] == 1:
                    if not F.empty(v): F.add(v, -W[v]<<pkr.s)
                    U[v] = p = dsu.root(U[v]); cycle += 1
                    while p != v:
                        if not F.empty(p): F.add(p, -W[p]<<pkr.s)
                        F.roots[v := dsu.merge_dest(v, p)] = F.merge(F.roots[v], F.roots[p])
                        U[p] = p = dsu.root(U[p]); cycle += 1
                else:
                    v = U[v]
            while cyc: vis[cyc.pop()] = 2

        vis, T = [0]*E.M, []
        for e in reversed(I):
            if vis[e]: continue
            f = stem[E.V[e]]; T.append(e)
            while f != e: vis[f] = 1; f = Ein[f]
        return T
    
    def sort(E):
        isort_parallel(E.W, E.U, E.V)

    def sub(E, I: list[int]):
        U, V, W = elist(E.N-1), elist(E.N-1), elist(E.N-1)
        for e in I: U.append(E.U[e]); V.append(E.V[e]); W.append(E.W[e])
        return E.__class__(E.N, U, V, W)
from cp_library.bit.pack.packer_cls import Packer
from cp_library.ds.dsu_cls import DSU
from cp_library.ds.list.elist_fn import elist
from cp_library.ds.heap.skew_heap_forrest_cls import SkewHeapForrest
from cp_library.io.io_base_cls import IOBase