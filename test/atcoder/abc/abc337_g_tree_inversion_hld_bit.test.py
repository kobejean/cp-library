# verification-helper: PROBLEM https://atcoder.jp/contests/abc337/tasks/abc337_g

def main():
    N = read(int)
    T = read(Tree[N])
    hld, ans = HLDBIT(T, [0]*N), [0]*(N+1)

    def range_add(l,r,x):
        ans[l] += x
        ans[r] -= x

    for u in range(N):
        l,r = hld.subtree_range(u)
        range_add(l,r,u-hld.subtree_query(u))
        for i in T.range(u):
            if i != hld.back[u]:
                l,r = hld.subtree_range(T.Va[i])
                cnt = hld.subtree_query(T.Va[i])
                range_add(0,l,cnt)
                range_add(r,N,cnt)
        hld.add(u,1)
    ans = presum(ans)
    ans = [ans[i] for i in hld.tin]
    write(*ans)

from cp_library.alg.tree.csr.hld_bit_cls import HLDBIT
from cp_library.alg.tree.csr.tree_cls import Tree
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write
from cp_library.alg.iter.presum_fn import presum

if __name__ == "__main__":
    main()