import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.tree.__header__
import cp_library.alg.tree.csr.__header__
from cp_library.alg.tree.csr.tree_base_cls import TreeBase

class HLDBase:
    def __init__(hld, T: TreeBase, r=0):
        hld.N, hld.T = len(T), T
        N, time, Va = T.N, 0, T.Va
        tin, tout, size = [0]*N, [0]*N, [1]*N+[0]
        back, heavy, head = [-1]*N, [-1]*N, [r]*N
        depth, order, vis = [0]*N, [0]*N, [0]*N
        st = elist(N); st.append(r)
        while st:
            if (s := vis[v := st.pop()]) == 0: # dfs down
                vis[v], j = 1, back[v]; st.append(v)
                for i in T.range(v):
                    if i != j:
                        depth[c := Va[i]], back[c] = depth[v]+1, T.twin[i]; st.append(c)
            elif s == 1: # dfs up
                l, j = -1, back[v]
                for i in T.range(v):
                    if i != j:
                        size[v] += size[c := Va[i]]
                        if size[c] > size[l]: l = c
                heavy[v] = l
                if j == -1: vis[v] = 2; st.append(v)

            elif s == 2: # decompose down
                h, l, j = head[v], heavy[v], back[v]
                tin[v], order[time], vis[v] = time, v, 3
                time += 1; st.append(v)
                for i in T.range(v):
                    if i != j and (c := Va[i]) != l:
                        head[c], vis[c] = c, 2; st.append(c)
                if l != -1: head[l], vis[l] = h, 2; st.append(l)

            elif s == 3: # decompose up
                tout[v] = time
        hld.up = [-1]*N
        for u,h in enumerate(head):
            if (j := back[h]) != -1:
                hld.up[u] = T.Va[j]

        hld.size, hld.depth = size, depth
        hld.order, hld.tin, hld.tout = order, tin, tout
        hld.heavy, hld.head, hld.back = heavy, head, back

    def subtree_range(hld, v):
        return hld.tin[v], hld.tout[v]

from cp_library.ds.list.elist_fn import elist