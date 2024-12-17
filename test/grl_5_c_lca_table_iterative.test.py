# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_5_C

from cp_library.alg.tree.tree_cls import Tree


def main():
    N, = read()
    T = Tree(N, [])
    for u in range(N):
        k, *adj = read()
        T[u].extend(adj)
    lca = LCATable(T, 0)
    Q, = read()
    for _ in range(Q):
        u, v = read()
        write(lca.query(u,v)[0])

from cp_library.alg.tree.lca_table_iterative_cls import LCATable
from cp_library.io.read_int_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()