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
    I = [0]*N
    for i in hld.back:
        if i == -1: continue
        I[T.Ea[i]] = hld[T.Va[i]]

    Q = read(int)
    for q in read(list[tuple[int, int, int], Q]):
        match q:
            case 1, i, w:
                bit[I[i-1]] = w
            case 2, u, v:
                ans = 0
                hld.path(u-1, v-1, query, True)
                write(ans)

from cp_library.ds.tree.bit.bit_cls import BIT
from cp_library.alg.tree.fast.tree_weighted_cls import TreeWeighted
from cp_library.alg.tree.fast.hld_weighted_cls import HLDWeighted
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == "__main__":
    main()