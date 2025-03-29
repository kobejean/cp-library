# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_path_sum
from operator import add

def main():
    N, Q = read()
    A = read(list[int])
    T = read(Tree[N,0])
    hld = HLDBIT(T, A)

    for _ in range(Q):
        t, u, v = read()
        if t == 0:
            hld.add(u, v)
        else:
            write(hld.path_query(u, v))

from cp_library.alg.tree.fast.hld_bit_cls import HLDBIT
from cp_library.alg.tree.fast.tree_cls import Tree
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
