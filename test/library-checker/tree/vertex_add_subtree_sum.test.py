# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_subtree_sum

def main():
    N, Q = read()
    A = read(list[int])
    P = read(list[int])
    T = Tree(N, range(1,N), P)
    T.euler_tour()
    S = [0]*(2*N)
    for u in range(N):
        S[T.tin[u]] = A[u]
    bit = BIT(S)
    for _ in range(Q):
        t, *q = read()
        if t == 0:
            u, x = q
            bit.add(T.tin[u], x)
        else:
            u, = q
            write(bit.sum_range(T.tin[u], T.tout[u]))

from cp_library.alg.tree.csr.tree_cls import Tree
from cp_library.ds.tree.bit.bit_cls import BIT
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
