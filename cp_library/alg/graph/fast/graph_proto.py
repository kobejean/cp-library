import cp_library.alg.graph.__header__
from cp_library.io.parser_cls import Parsable, Parser, TokenStream
from cp_library.alg.graph.dfs_options_cls import DFSFlags, DFSEvent
from cp_library.ds.elist_fn import elist
from typing import Iterable, Sequence, overload
from collections import deque
from cp_library.math.inft_cnst import inft

class GraphProtocol(Sequence, Parsable):

    # @overload
    # def distance(G) -> list[list[int]]: ...
    # @overload
    # def distance(G, s: int = 0) -> list[int]: ...
    # @overload
    # def distance(G, s: int, g: int) -> int: ...
    # def distance(G, s = None, g = None):
    #     match s, g:
    #         case None, None:
    #             return G.floyd_warshall()
    #         case s, None:
    #             return G.bfs(s)
    #         case s, g:
    #             return G.bfs(s, g)

    # @overload
    # def bfs(G, s: int|list = 0) -> list[int]: ...
    # @overload
    # def bfs(G, s: int|list, g: int) -> int: ...
    # def bfs(G, s = 0, g = None):
    #     D = [inft for _ in range(G.N)]
    #     q = deque([s] if isinstance(s, int) else s)
    #     for u in q: D[u] = 0
    #     while q:
    #         nd = D[u := q.popleft()]+1
    #         if u == g: return D[u]
    #         for v in G.neighbors(u):
    #             if nd < D[v]:
    #                 D[v] = nd
    #                 q.append(v)
    #     return D if g is None else inft 


    def starts(G, v: int|list[int]|None) -> Iterable:
        match v:
            case int(v): return (v,)
            case None: return range(G.N)
            case V: return V
