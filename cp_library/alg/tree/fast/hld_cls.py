import cp_library.__header__
from typing import Sequence
import cp_library.alg.__header__
import cp_library.alg.tree.__header__
import cp_library.alg.tree.fast.__header__
from cp_library.alg.tree.fast.tree_base_cls import TreeBase

class HLD(Sequence[int]):
    def __init__(hld, T: TreeBase, r=0):
        hld.N, hld.T = len(T), T
        N, time, Va = T.N, 0, T.Va
        tin, tout, size = [0]*N, [0]*N, [1]*N+[0]
        par, heavy, head = [-1]*N, [-1]*N, [r]*N
        depth, order, vis = [0]*N, [0]*N, [0]*N
        st = elist(N)
        st.append(r)
        while st:
            if (s := vis[v := st.pop()]) == 0: # dfs down
                p, vis[v] = par[v], 1; st.append(v)
                for i in T.range(v):
                    if (c := Va[i]) != p:
                        depth[c], par[c] = depth[v]+1, v; st.append(c)
            elif s == 1: # dfs up
                p, l = par[v], -1
                for i in T.range(v):
                    if (c := Va[i]) != p:
                        size[v] += size[c]
                        if size[c] > size[l]:
                            l = c
                heavy[v] = l
                if p == -1:
                    vis[v] = 2
                    st.append(v)

            elif s == 2: # decompose down
                p, h, l = par[v], head[v], heavy[v]
                tin[v], order[time], vis[v] = time, v, 3
                time += 1
                st.append(v)
                
                for i in T.range(v):
                    if (c := Va[i]) != p and c != l:
                        head[c], vis[c] = c, 2
                        st.append(c)

                if l != -1:
                    head[l], vis[l] = h, 2
                    st.append(l)

            elif s == 3: # decompose up
                tout[v] = time
        hld.size, hld.depth = size, depth
        hld.order, hld.tin, hld.tout = order, tin, tout
        hld.par, hld.heavy, hld.head = par, heavy, head

    def __getitem__(hld, key):
        return hld.tin[key]
    
    def __len__(hld):
        return len(hld.tin)
    
    def __contains__(hld, value):
        return hld.tin.__contains__(value)
    
    def subtree_range(hld, v):
        return hld.tin[v], hld.tout[v]

    def path(hld, u, v, query_fn, edge=False):
        head, depth, par, tin = hld.head, hld.depth, hld.par, hld.tin
        while head[u] != head[v]:
            if depth[head[u]] < depth[head[v]]:
                u,v = v,u
            query_fn(tin[head[u]], tin[u]+1)
            u = par[head[u]]

        if depth[u] < depth[v]:
            u,v = v,u
        query_fn(tin[v]+edge, tin[u]+1)

from cp_library.ds.elist_fn import elist