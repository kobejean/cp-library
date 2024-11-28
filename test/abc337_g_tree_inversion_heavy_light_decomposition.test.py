# verification-helper: PROBLEM https://atcoder.jp/contests/abc337/tasks/abc337_g

from itertools import accumulate

def main():
    N = read(int)
    T = read(Tree[N])

    hld = HLD(T)
    bit = BinaryIndexTree(N)
    ans = [0]*(N+1)

    def range_add(l,r,x):
        ans[l] += x
        ans[r] -= x

    for v in range(N):
        for c in T[v]:
            if c == hld.par[v]:
                l,r = hld.start[v], hld.end[v]
                cnt = v-bit.range_sum(l,r)
                range_add(l,r,cnt)
            else:
                l,r = hld.start[c], hld.end[c]
                cnt = bit.range_sum(l,r)
                range_add(0,l,cnt)
                range_add(r,N,cnt)
        bit.set(hld[v],1)
    ans = presum(ans)
    ans = [ans[i] for i in hld.start]
    write(*ans)

from cp_library.alg.tree.heavy_light_decomposition_cls import HLD
from cp_library.alg.tree.tree_cls import Tree
from cp_library.ds.bit_cls import BinaryIndexTree
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write
from cp_library.alg.iter.presum_fn import presum

if __name__ == "__main__":
    main()