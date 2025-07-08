# verification-helper: PROBLEM https://judge.yosupo.jp/problem/lca

def main():
    N, Q = read()
    U = range(1,N)
    P = read(list[int])
    T = Tree(N, P, U)
    lca = LCATable(T)
    for _ in range(Q):
        u, v = read()
        a, _ = lca.query(u, v)
        write(a)

from cp_library.alg.tree.lca_table_iterative_cls import LCATable
from cp_library.alg.tree.csr.tree_cls import Tree
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
