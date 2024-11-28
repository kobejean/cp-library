import cp_library.alg.graph.fast.__header__

from typing import Sequence
from cp_library.io.parser_cls import Parsable, TokenStream
from cp_library.ds.fill_fn import fill_i32, fill_u32, fill_u64
from cp_library.alg.graph.fast.graph_weighted_proto import GraphWeightedProtocol

class DiGraphWeighted(GraphWeightedProtocol):
    def __init__(G, N: int, U: list, V: list, W: list):
        M = len(U)
        deg, Ea, Ua, Va, Wa = fill_u32(N), fill_u32(M), fill_u32(M), fill_u32(M), [0]*M

        for u in U:
            deg[u] += 1
            
        La, idx = fill_u32(N), 0
        for u in range(N): 
            La[u], idx = idx, idx + deg[u]
        Ra = La[:]

        # place edge data using R to track
        for e in range(M):
            i = Ra[u := U[e]]
            Ua[i], Va[i], Wa[i], Ea[i] = U[e], V[e], W[e], e
            Ra[u] += 1

        G.N, G.M, G.U, G.V, G.W = N, M, U, V, W
        G.La, G.Ra, G.Ua, G.Va, G.Wa, G.Ea = La, Ra, Ua, Va, Wa, Ea

    @classmethod
    def compile(cls, N: int, M: int, shift: int = -1):
        def parse(ts: TokenStream):
            U, V, W = fill_u32(M), fill_u32(M), [0]*M
            stream = ts.stream
            for i in range(M):
                u, v, W[i] = map(int, stream.readline().split())
                U[i], V[i] = u-shift, v-shift
            return cls(N, U, V, W)
        return parse
    
from cp_library.ds.elist_fn import elist
from cp_library.ds.priority_queue_cls import PriorityQueue
from cp_library.math.inft_cnst import inft