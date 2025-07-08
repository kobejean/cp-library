# verification-helper: PROBLEM https://atcoder.jp/contests/abc294/tasks/abc294_g

def main():
    N = read(int)
    T = read(TreeWeighted[N])
    U, V = T.U, T.V
    lca = LCATableWeighted(T)
    bit = BIT(lca.weights)

    def update(i,w):
        u,v = U[i], V[i]
        c = u if T.par[u] == v else v
        l,r = T.tin[c], T.tout[c]
        bit.set(l,w)
        bit.set(r,-w)
    
    def query(u,v):
        a,_ = lca.query(u,v)
        ans = bit.sum(T.tout[u]) + bit.sum(T.tout[v]) - 2*bit.sum(T.tout[a])
        write(ans)
    
    def answer():
        Q = read(int)
        for q in read(list[tuple[int,int,int], Q]):
            match q:
                case 1, i, w:
                    update(i-1,w)
                case 2, u, v:
                    query(u-1,v-1)
    answer()

from cp_library.alg.tree.csr.tree_weighted_cls import TreeWeighted
from cp_library.alg.tree.lca_table_weighted_iterative_cls import LCATableWeighted
from cp_library.ds.tree.bit.bit_cls import BIT
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == "__main__":
    main()