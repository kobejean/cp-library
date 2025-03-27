import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.tree.__header__
import cp_library.alg.tree.fast.__header__
from cp_library.alg.tree.fast.hld_cls import HLD
from cp_library.alg.tree.fast.tree_weighted_base_cls import TreeWeightedBase

class HLDWeighted(HLD):
    def __init__(hld, T: TreeWeightedBase, r=0):
        N, time, Va, Wa = T.N, 0, T.Va, T.Wa
        tin, tout, size = [0]*N, [0]*N, [1]*N+[0]
        back, par, heavy, head = [-1]*N, [-1]*N, [-1]*N, [r]*N
        depth, order, vis = [0]*N, [0]*N, [0]*N
        weights = [0]*N
        st = elist(N)
        st.append(r)
        while st:
            if (s := vis[v := st.pop()]) == 0: # dfs down
                vis[v] = 1
                j = T.twin[back[v]] if back[v] >= 0 else -1
                st.append(v)
                for i in T.range(v):
                    if i != j:
                        c = Va[i]
                        depth[c], par[c], weights[c] = depth[v]+1, v, Wa[i]
                        back[c] = i
                        st.append(c)

            elif s == 1: # dfs up
                l = -1
                j = T.twin[back[v]] if back[v] >= 0 else -1
                for i in T.range(v):
                    if i != j:
                        size[v] += size[c := Va[i]]
                        if size[c] > size[l]:
                            l = c
                heavy[v] = l
                if j == -1:
                    vis[v] = 2
                    st.append(v)

            elif s == 2: # decompose down
                h, l = head[v], heavy[v]
                j = T.twin[back[v]] if back[v] >= 0 else -1
                tin[v], order[time], vis[v] = time, v, 3
                time += 1
                st.append(v)
                
                for i in T.range(v):
                    if i != j and (c := Va[i]) != l:
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
        hld.weights = weights
        hld.back = back

from cp_library.ds.elist_fn import elist