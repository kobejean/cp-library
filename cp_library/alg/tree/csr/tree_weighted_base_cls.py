import cp_library.alg.tree.csr.__header__
from typing import Optional
from cp_library.alg.graph.csr.graph_weighted_base_cls import GraphWeightedBase
from cp_library.alg.tree.csr.tree_base_cls import TreeBase

class TreeWeightedBase(TreeBase, GraphWeightedBase):

    def dfs_distance(T, s: int, g: Optional[int] = None):
        st, Wa, Va = elist(N := T.N), T.Wa, T.Va
        T.D, T.back = D, back = [inf]*N, i32f(N, -1)
        D[s] = 0; st.append(s)
        while st:
            d = D[u := st.pop()]
            if u == g: return d
            for i in T.range(u):
                if (nd := d+Wa[i]) < D[v := Va[i]]:
                    D[v], back[v] = nd, i; st.append(v)
        return D if g is None else inf 
    
    def euler_tour(T, s = 0):
        N, Va, Wa = len(T), T.Va, T.Wa
        tin, tout, par = [-1]*N,[-1]*N,[-1]*N
        order, delta, Wdelta = elist(2*N), elist(2*N), elist(2*N)
        st, Wst = elist(N), elist(N)
        st.append(s); Wst.append(0)
        while st:
            p, wd = par[u := st.pop()], Wst.pop()
            if tin[u] == -1:
                tin[u] = len(order)
                for i in T.range(u):
                    if (v := Va[i]) != p:
                        w, par[v] = Wa[i], u
                        st.append(u); st.append(v); Wst.append(-w); Wst.append(w)
                delta.append(1)
            else:
                delta.append(-1)
            Wdelta.append(wd); order.append(u)
            tout[u] = len(order)
        delta[0] = delta[-1] = 0
        T.tin, T.tout, T.par = tin, tout, par
        T.order, T.delta, T.Wdelta = order, delta, Wdelta

    @classmethod
    def compile(cls, N: int, shift: int = -1):
        return GraphWeightedBase.compile.__func__(cls, N, N-1, shift)
    
from cp_library.ds.list.elist_fn import elist
from cp_library.ds.array.i32f_fn import i32f
from math import inf