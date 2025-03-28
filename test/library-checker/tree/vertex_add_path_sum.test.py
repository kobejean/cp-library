# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_path_sum
def main():
    N, Q = read()
    A = read(list[int])
    T = read(Tree[N,0])
    hld = HLD(T)
    B = [0]*N
    for u in range(N):
        B[hld.tin[u]] = A[u]
    bit = BIT(B)
    ans = 0
    def query(l, r):
        nonlocal ans
        ans += bit.range_sum(l,r)
    for _ in range(Q):
        t, u, v = read()
        if t == 0:
            bit.add(hld.tin[u], v)
        else:
            hld.path(u, v, query)
            write(ans)
            ans = 0

from cp_library.alg.tree.fast.hld_cls import HLD
from cp_library.alg.tree.fast.tree_cls import Tree
from cp_library.ds.tree.bit.bit_cls import BIT
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
