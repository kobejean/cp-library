# verification-helper: PROBLEM https://atcoder.jp/contests/abc294/tasks/abc294_g

def main():
    N = read(int)
    E = read(EdgeListWeighted[N-1])
    T = GraphWeighted(N, E)
    lca = LCATableWeighted(T)
    bit = BinaryIndexTree(lca.weights)

    Q = read(int)
    for query in read(list[tuple[int,int,int], Q]):
        match query:
            case 1, i, w:
                i -= 1
                u,v,_ = E[i]
                p, _ = lca.query(u,v)
                c = u if p == v else v
                l,r = lca.start[c], lca.end[c]
                bit.set(l,w)
                bit.set(r,-w)

            case 2, u, v:
                u,v=u-1,v-1
                a,_ = lca.query(u,v)
                ans = bit.pref_sum(lca.end[u]) + \
                    bit.pref_sum(lca.end[v]) - \
                    2*bit.pref_sum(lca.end[a])
                print(ans)
        

from cp_library.alg.graph.edge_list_weighted_cls import EdgeListWeighted
from cp_library.alg.graph.graph_weighted_cls import GraphWeighted
from cp_library.alg.tree.lca_table_weighted_iterative_cls import LCATableWeighted
from cp_library.ds.bit_cls import BinaryIndexTree
from cp_library.io.read_specs_fn import read

if __name__ == "__main__":
    main()