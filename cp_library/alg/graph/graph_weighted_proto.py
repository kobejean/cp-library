import cp_library.alg.graph.__header__

from typing import overload
from heapq import heapify, heappop, heappush
import operator
from math import inf

from cp_library.alg.graph.graph_proto import GraphProtocol

class GraphWeightedProtocol(GraphProtocol):

    def neighbors(G, v: int):
        return map(operator.itemgetter(0), G[v])
    
    @overload
    def distance(G) -> list[list[int]]: ...
    @overload
    def distance(G, s: int = 0) -> list[int]: ...
    @overload
    def distance(G, s: int, g: int) -> int: ...
    def distance(G, s = None, g = None):
        match s, g:
            case None, None:
                return G.floyd_warshall()
            case s, None:
                return G.dijkstra(s)
            case s, g:
                return G.dijkstra(s, g)
    
    def dijkstra(G, s = 0, g = None):
        D = [inf for _ in range(G.N)]
        D[s] = 0
        q = [(0, s)]
        while q:
            d, v = heappop(q)
            if d > D[v]: continue
            if v == g: return d
            for u, w, *_ in G[v]:
                if (nd := d + w) < D[u]:
                    D[u] = nd
                    heappush(q, (nd, u))
        return D if g is None else inf
    
    def kruskal(G):
        E, N = G.E, G.N
        heapify(E)
        dsu = DSU(N)
        MST = []
        need = N-1
        while E and need:
            edge = heappop(E)
            u,v,*_ = edge
            u,v = dsu.merge(u,v)
            if u != v:
                MST.append(edge)
                need -= 1
        cls = type(G)
        return cls(N, MST)
    
    def bellman_ford(G, s = 0) -> list[int]:
        D = [inf]*G.N
        D[s] = 0
        for _ in range(G.N-1):
            for u, edges in enumerate(G):
                for v,w,*_ in edges:
                    D[v] = min(D[v], D[u] + w)
        return D
    
    def floyd_warshall(G) -> list[list[int]]:
        D = [[inf]*G.N for _ in range(G.N)]

        for u, edges in enumerate(G):
            D[u][u] = 0
            for v,w in edges:
                D[u][v] = min(D[u][v], w)
        
        for k, Dk in enumerate(D):
            for Di in D:
                for j in range(G.N):
                    Di[j] = min(Di[j], Di[k]+Dk[j])
        return D

from cp_library.ds.dsu_cls import DSU