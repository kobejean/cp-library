import cp_library.__header__
from cp_library.io.parsable_cls import Parsable
from cp_library.io.io_base_cls import IOBase
import cp_library.alg.__header__
import cp_library.alg.graph.__header__

class EdgeList(Parsable):
    def __init__(E, N, U, V): E.N, E.M, E.U, E.V = N, len(U), U, V
    def __len__(E): return E.M
    def __getitem__(E, e): return E.U[e], E.V[e]
    @classmethod
    def compile(cls, N: int, M: int, I: int = -1):
        def parse(io: IOBase):
            U, V = [0]*M, [0]*M
            for e in range(M): u, v = io.readints(); U[e], V[e] = u+I, v+I
            return cls(N, U, V)
        return parse
    def sub(E, I: list[int]):
        U, V = elist(E.N-1), elist(E.N-1)
        for e in I: U.append(E.U[e]); V.append(E.V[e])
        return E.__class__(E.N, U, V)
from cp_library.ds.list.elist_fn import elist