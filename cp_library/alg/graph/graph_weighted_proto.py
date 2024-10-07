import cp_library.alg.graph.__header__
from cp_library.alg.graph.graph_proto import GraphProtocol
import heapq
from math import inf

class GraphWeightedProtocol(GraphProtocol):

    def dijkstra(G, s):
        dists = [inf for _ in range(G.N)]
        dists[s] = 0
        queue = [(0, s)]

        while queue:
            d, v = heapq.heappop(queue)
            if d > dists[v]: continue

            for u, w in G[v]:
                nd = d + w
                if nd < dists[u]:
                    dists[u] = nd
                    heapq.heappush(queue, (nd, u))

        return dists
