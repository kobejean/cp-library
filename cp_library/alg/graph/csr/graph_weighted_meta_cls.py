import cp_library.__header__
import typing
import cp_library.alg.__header__
import cp_library.alg.graph.__header__
import cp_library.alg.graph.csr.__header__
from cp_library.alg.graph.csr.graph_weighted_cls import GraphWeighted

class GraphWeightedMeta(GraphWeighted):
    def __init__(G, N: int, U: list[int], V: list[int], W: list[int],
                 X: list[int] = None, Y: list[int] = None, Z: list[int] = None):
        super().__init__(N, U, V, W)
        M2 = len(G.Ea)
        if X is not None:
            Xa = [0]*M2
            for i,e in enumerate(G.Ea):
                Xa[i] = X[e]
            G.X = X
            '''A parallel lists of edge meta data from the original edge list.'''
            G.Xa = Xa
            '''Xa[i] parallel lists of adjacent meta data to u for La[u] <= i < Ra[u].'''
        if Y is not None:
            Ya = [0]*M2
            for i,e in enumerate(G.Ea):
                Ya[i] = Y[e]
            G.Y = Y
            '''A parallel lists of edge meta data from the original edge list.'''
            G.Ya = Ya
            '''Ya[i] parallel lists of adjacent meta data to u for La[u] <= i < Ra[u].'''
        if Z is not None:
            Za = [0]*M2
            for i,e in enumerate(G.Ea):
                Za[i] = Z[e]
            G.Z = Z
            '''A parallel lists of edge meta data from the original edge list.'''
            G.Za = Za
            '''Za[i] parallel lists of adjacent meta data to u for La[u] <= i < Ra[u].'''


    @classmethod
    def compile(cls, N: int, M: int, T: list[type] = [-1,-1,int,int]):
        u, v, *w = map(Parser.compile, typing.get_args(T) or T)
        if len(w) == 2:
            if T == [-1,-1,int,int]:
                def parse(io: IOBase):
                    U, V, W, X = u32f(M), u32f(M), [0]*M, [0]*M
                    for i in range(M): u, v, a, b = io.readints(); U[i], V[i], W[i], X[i] = u-1, v-1, a, b
                    return cls(N, U, V, W, X)
            else:
                w, x = w
                def parse(io: IOBase):
                    U, V, W, X = u32f(M), u32f(M), [0]*M, [0]*M
                    for i in range(M): U[i], V[i], W[i], X[i] = u(io), v(io), w(io), x(io)
                    return cls(N, U, V, W, X)
        elif len(w) == 3:
            w, x, y = w
            def parse(io: IOBase):
                U, V, W, X, Y = u32f(M), u32f(M), [0]*M, [0]*M, [0]*M
                for i in range(M): U[i], V[i], W[i], X[i], Y[i] = u(io), v(io), w(io), x(io), y(io)
                return cls(N, U, V, W, X, Y)
        else:
            w, x, y, z = w
            def parse(io: IOBase):
                U, V, W, X, Y, Z = u32f(M), u32f(M), [0]*M, [0]*M, [0]*M, [0]*M
                for i in range(M): U[i], V[i], W[i], X[i], Y[i], Z[i] = u(io), v(io), w(io), x(io), y(io), z(io)
                return cls(N, U, V, W, X, Y, Z)
        return parse
from cp_library.ds.array.u32f_fn import u32f
from cp_library.io.parser_cls import Parser
from cp_library.io.io_base_cls import IOBase
