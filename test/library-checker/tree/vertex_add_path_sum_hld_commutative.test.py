# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_path_sum
from operator import add

def main():
    N, Q = read()
    A = read(list[int])
    T = read(Tree[N,0])
    hld = HLDCommutative(T, add, 0, A)

    for _ in range(Q):
        t, u, v = read()
        if t == 0:
            hld.set(u, v+hld.get(u))
        else:
            write(hld.path_query(u, v))

from cp_library.alg.tree.csr.hld_commutative_cls import HLDCommutative
from cp_library.alg.tree.csr.tree_cls import Tree
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
