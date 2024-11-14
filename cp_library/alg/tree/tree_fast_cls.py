from typing import Iterable
from cp_library.alg.graph.edge_cls import Edge
import cp_library.alg.tree.__header__

from cp_library.alg.graph.graph_cls import Graph
from cp_library.alg.tree.tree_proto import TreeProtocol
from cp_library.io.parser_cls import TokenStream
from cp_library.ds.elist_fn import elist


class Tree(Graph, TreeProtocol):

    def edge(T, v, i):
        return T.adj[T.start[v]+i]

    def neighbors(T, v: int) -> list[int]:
        return T.adj[T.start[v]:T.end[v]]
    
    def dfs_topdown(T, s: int|list[int]|None = None, connect_roots = False):
        '''Returns list of (u,v) representing u->v edges in order of top down discovery'''
        stack: list[int] = elist(T.N)
        vis = [False]*T.N
        edges: list[tuple[int,int]] = elist(T.N)
        adj = T.adj

        for s in T.starts(s):
            if vis[s]: continue
            if connect_roots:
                edges.append((-1,s))
            vis[s] = True
            stack.append(s)
            while stack:
                u = stack.pop()
                start = T.start[u] 
                for idx in range(start, T.end[u]):
                    v = adj[idx]
                    if vis[v]:
                        adj[idx], adj[start] = adj[start], adj[idx]
                        continue
                    vis[v] = True
                    edges.append((u,v))
                    stack.append(v)
        return edges
    
    __getitem__ = neighbors
    
    @classmethod
    def compile(cls, N: int):

        def parse(ts: TokenStream):
            T = cls.__new__(cls)
            object.__init__(T)

            M2 = 2*(N-1)
            V = ts.n_uints(M2, -1)

            # Calculate degrees
            deg = [0] * N
            for i in range(0,M2,2):
                u, v = V[i], V[i+1]
                deg[u] += 1
                deg[v] += 1
            
            # Calculate start positions
            start = [0] * N
            curr_pos = 0
            for i in range(N):
                start[i] = curr_pos
                curr_pos += deg[i]
            
            # Initialize end as copy of start
            end = start.copy()
            
            # Create graph array
            adj = [0] * M2
            
            # Add edges, incrementing end positions
            for i in range(0,M2,2):
                u, v = V[i], V[i+1]
                adj[end[u]] = v
                adj[end[v]] = u
                end[u] += 1
                end[v] += 1
            T.deg = deg
            T.adj = adj
            T.start = start
            T.end = end
            T.N = N
            T.M = N-1
            return T

        return parse
