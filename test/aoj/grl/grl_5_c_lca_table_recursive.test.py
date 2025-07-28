# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_5_C

def main():
    N, = read()
    T = []
    for _ in range(N):
        k, *adj = read()
        T.append(adj)
    lca = LCATable(T, 0)
    Q, = read()
    for _ in range(Q):
        u, v = read()
        write(lca.query(u,v)[0])

from cp_library.alg.tree.lca_table_recursive_cls import LCATable
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()