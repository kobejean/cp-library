from cp_library.alg.tree.fast.tree_base_cls import TreeBase
from cp_library.alg.tree.lca_table_iterative_cls import LCATable
from cp_library.ds.elist_fn import elist
from cp_library.alg.iter.argsort_fn import argsort
from typing import Callable
from cp_library.misc.typing import _T

class AuxTreeBase(TreeBase):

    def __init__(T, lca: LCATable):
        T.lca = lca

    def add(T, u, v):
        w = T.lca.distance(u,v)
        i, j = T.Ra[u], T.Ra[v]
        T.Ua[i], T.Va[i], T.Wa[i], T.Ua[j], T.Va[j], T.Wa[j] = u, v, w, v, u, w
        T.twin[i], T.twin[j] = j, i
        T.Ra[u], T.Ra[v] = i+1, j+1
        return j

    def trees(T, C: list[int]):
        lca, N = T.lca, T.N
        T.Ra, cnt, order = T.La[:], [0]*N, argsort(T.tin)
        for c in C: cnt[c] += 1
        L = [0]*N
        for i in range(N-1): L[i+1] = L[i]+cnt[i]
        R, G = L[:], [0]*N
        
        for i in order: c = C[i]; G[R[c]] = i; R[c] += 1
        st, V, post = elist(N), elist(N), elist(N)
        La, Ra, tin = T.La, T.Ra, T.tin

        for c in range(N):
            l, r = L[c], R[c]
            if l == r: continue
            st.append(G[l])
            for j in range(l,r-1):
                u, v = G[j], G[j+1]
                a, _ = lca.query(u, v)
                if a != u:
                    l = st.pop()
                    while st and tin[t := st[-1]] > tin[a]:
                        V.append(l); post.append(T.add(l, l := st.pop()))
                    if not st or t != a: st.append(a)
                    V.append(l); post.append(T.add(l, a))
                st.append(v)
            l = st.pop()
            while st: V.append(l); post.append(T.add(l, l := st.pop()))
            V.append(l)
            yield c, V, post
            while V:
                Ra[u] = La[u := V.pop()]
                if T.vis: T.vis[u] = 0
            post.clear()

    def rerooting_dp(T, C: list[int], e: _T, 
                     merge: Callable[[_T,_T],_T], 
                     edge_op: Callable[[_T,int,int,int,int],_T] = lambda s,i,p,u,c:s):
        ans, dp, suf, I = [e]*T.N, [e]*T.N, [e]*len(T.Ua), T.La[:]

        for c, V, post in T.trees(C):
            r = V[-1]
            for v in V: I[v] = T.Ra[v]

            # up
            for i in post:
                u,v = T.Ua[i], T.Va[i]
                # subtree v finished up pass, store value to accumulate for u
                dp[v] = new = edge_op(dp[v], i, u, v, c)
                dp[u] = merge(dp[u], new)
                # suffix accumulation
                if (j:=I[u]-1) > T.La[u]: suf[j-1] = merge(suf[j], new)
                I[u] = j
            # down
            dp[r] = e # at this point dp stores values to be merged in parent
            for i in reversed(post):
                u,v = T.Ua[i], T.Va[i]
                dp[u] = merge(pre := dp[u], dp[v])
                dp[v] = edge_op(merge(suf[I[u]], pre), i, v, u, c)
                I[u] += 1
            
            # store ans and reset
            for v in V:
                if C[v] == c: ans[v] = dp[v]
                dp[v] = e
            for i in post:
                suf[i] = e
        return ans
