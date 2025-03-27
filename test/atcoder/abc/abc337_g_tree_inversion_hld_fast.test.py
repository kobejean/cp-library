# verification-helper: PROBLEM https://atcoder.jp/contests/abc337/tasks/abc337_g

def main():
    N = read(int)
    T = read(Tree[N])
    hld = HLD(T)
    bit = BIT(N)
    ans = [0]*(N+1)

    def range_add(l,r,x):
        ans[l] += x
        ans[r] -= x

    for v in range(N):
        l,r = hld.subtree_range(v)
        range_add(l,r,v-bit.range_sum(l,r))
        for i in T.range(v):
            if (c := T.Va[i]) != hld.par[v]:
                l,r = hld.subtree_range(c)
                cnt = bit.range_sum(l,r)
                range_add(0,l,cnt)
                range_add(r,N,cnt)
        bit.add(hld[v],1)
    ans = presum(ans)
    ans = [ans[i] for i in hld]
    write(*ans)

from cp_library.alg.tree.fast.hld_cls import HLD
from cp_library.alg.tree.fast.tree_cls import Tree
from cp_library.ds.tree.bit.bit_cls import BIT
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write
from cp_library.alg.iter.presum_fn import presum

if __name__ == "__main__":
    main()