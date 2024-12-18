import cp_library.alg.graph.fast.__header__
from cp_library.io.parser_cls import Parser, TokenStream
from cp_library.alg.graph.fast.digraph_weighted_cls import DiGraphWeighted

class DiGraphWeightedMeta(DiGraphWeighted):
    def __init__(G, N: int, U: list[int], V: list[int], W: list[int],
                 X: list[int] = None, Y: list[int] = None, Z: list[int] = None):
        super().__init__(N, U, V, W)
        M = len(U)
        if X is not None:
            Xa = [0]*M
            for i,e in enumerate(G.Ea):
                Xa[i] = X[e%M]
            G.X = X
            """A parallel lists of edge meta data from the original edge list."""
            G.Xa = Xa
            """Xa[i] parallel lists of adjacent meta data to u for La[u] <= i < Ra[u]."""
        if Y is not None:
            Ya = [0]*M
            for i,e in enumerate(G.Ea):
                Ya[i] = Y[e%M]
            G.Y = Y
            """A parallel lists of edge meta data from the original edge list."""
            G.Ya = Ya
            """Ya[i] parallel lists of adjacent meta data to u for La[u] <= i < Ra[u]."""
        if Z is not None:
            Za = [0]*M
            for i,e in enumerate(G.Ea):
                Za[i] = Z[e%M]
            G.Z = Z
            """A parallel lists of edge meta data from the original edge list."""
            G.Za = Za
            """Za[i] parallel lists of adjacent meta data to u for La[u] <= i < Ra[u]."""

    @classmethod
    def compile(cls, N: int, M: int, T: list[type] = [-1,-1,int,int]):
        u, v, *w = map(Parser.compile, T)
        if len(w) == 2:
            if T == [-1,-1,int,int]:
                def parse(ts: TokenStream):
                    U, V, W, X = fill_u32(M), fill_u32(M), [0]*M, [0]*M
                    for i in range(M):
                        u,v,a,b = ts.line()
                        U[i], V[i], W[i], X[i] = int(u)-1, int(v)-1, int(a), int(b)
                    return cls(N, U, V, W, X)
            else:
                w, x = w
                def parse(ts: TokenStream):
                    U, V, W, X = fill_u32(M), fill_u32(M), [0]*M, [0]*M
                    for i in range(M):
                        U[i], V[i], W[i], X[i] = u(ts), v(ts), w(ts), x(ts)
                    return cls(N, U, V, W, X)
        elif len(w) == 3:
            w, x, y = w
            def parse(ts: TokenStream):
                U, V, W, X, Y = fill_u32(M), fill_u32(M), [0]*M, [0]*M, [0]*M
                for i in range(M):
                    U[i], V[i], W[i], X[i], Y[i] = u(ts), v(ts), w(ts), x(ts), y(ts)
                return cls(N, U, V, W, X, Y)
        else:
            w, x, y, z = w
            def parse(ts: TokenStream):
                U, V, W, X, Y, Z = fill_u32(M), fill_u32(M), [0]*M, [0]*M, [0]*M, [0]*M
                for i in range(M):
                    U[i], V[i], W[i], X[i], Y[i], Z[i] = u(ts), v(ts), w(ts), x(ts), y(ts), z(ts)
                return cls(N, U, V, W, X, Y, Z)
        return parse

from cp_library.ds.fill_fn import fill_u32