# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_C

def main():
    N, = read()
    pts = [read() for _ in range(N)]

    kdtree = KDTree(pts)

    Q, = read()
    for _ in range(Q):
        sx,tx,sy,ty = read()
        tx += 1
        ty += 1
        ans = sorted(kdtree[sx:tx,sy:ty]) + ['']
        print(*ans, sep='\n')

from cp_library.ds.kdtree_cls import KDTree
from cp_library.io.read_int_fn import read

if __name__ == '__main__':
    main()