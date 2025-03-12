# verification-helper: PROBLEM https://atcoder.jp/contests/abc294/tasks/abc294_g

def main():
    N = read(int)
    T = read(TreeWeighted[N])

    hld = HLDWeighted(T)
    W = [hld.weights[i] for i in hld.order]
    bit = BIT(W)
    ans = 0

    def query(l, r):
        nonlocal ans
        ans += bit.range_sum(l,r) 

    Q = read(int)
    for q in read(list[tuple[int, int, int], Q]):
        match q:
            case 1, i, w:
                i -= 1  # Convert to 0-based index
                u, v = T.U[i], T.V[i]
                idx = hld[u if hld.par[u] == v else v]
                bit.set(idx, w)
            case 2, u, v:
                u, v = u - 1, v - 1
                ans = 0
                hld.path(u,v, query, True)
                write(ans)

from cp_library.ds.tree.bit.bit_cls import BIT
from cp_library.alg.tree.fast.tree_weighted_cls import TreeWeighted
from cp_library.alg.tree.heavy_light_decomposition_weighted_cls import HLDWeighted
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == "__main__":
    main()