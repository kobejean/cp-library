import cp_library.__header__
from cp_library.io.parsable_cls import Parsable
import cp_library.ds.__header__

class DSU(Parsable):
    def __init__(dsu, N): dsu.N, dsu.cc, dsu.par = N, N, [-1]*N
    def merge(dsu, u, v):
        x, y = dsu.root(u), dsu.root(v)
        if x == y: return x,y
        if dsu.par[x] > dsu.par[y]: x, y = y, x
        dsu.par[x] += dsu.par[y]; dsu.par[y] = x; dsu.cc -= 1
        return x, y
    def root(dsu, i) -> int:
        p = (par := dsu.par)[i]
        while p >= 0:
            if par[p] < 0: return p
            par[i], i, p = par[p], par[p], par[par[p]]
        return i
    def groups(dsu) -> 'CSRIncremental[int]':
        sizes, row, p = [0]*dsu.cc, [-1]*dsu.N, 0
        for i in range(dsu.cc):
            while dsu.par[p] >= 0: p += 1
            sizes[i], row[p] = -dsu.par[p], i; p += 1
        csr = CSRIncremental(sizes)
        for i in range(dsu.N): csr.append(row[dsu.root(i)], i)
        return csr
    __iter__ = groups
    def merge_dest(dsu, u, v): return dsu.merge(u, v)[0]
    def same(dsu, u: int, v: int):  return dsu.root(u) == dsu.root(v)
    def size(dsu, i) -> int: return -dsu.par[dsu.root(i)]
    def __len__(dsu): return dsu.cc
    def __contains__(dsu, uv): u, v = uv; return dsu.same(u, v)
    @classmethod
    def compile(cls, N: int, M: int, shift = -1):
        def parse_fn(io: IOBase):
            dsu = cls(N)
            for _ in range(M): u, v = io.readints(); dsu.merge(u+shift, v+shift)
            return dsu
        return parse_fn
from cp_library.ds.csr.csr_incremental_cls import CSRIncremental
from cp_library.io.io_base_cls import IOBase