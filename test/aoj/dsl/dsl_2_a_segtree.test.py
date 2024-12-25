# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_A

def main():
    N, Q = read()

    seg = SegTree(min, 2147483647, N)

    for _ in range(Q):
        com, x, y = read()
        if com:
            print(seg.prod(x,y+1))
        else:
            seg.set(x,y)

from cp_library.ds.segtree_cls import SegTree
from cp_library.io.read_int_fn import read

if __name__ == '__main__':
    main()