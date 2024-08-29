# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_C
from cp_library.ds.kdtree_cls import KDTree

def rint(shift=0, base=10):
    return [int(x, base) + shift for x in input().split()]

N, = rint()
pts = [rint() for _ in range(N)]

kdtree = KDTree(pts)

Q, = rint()
for _ in range(Q):
    sx,tx,sy,ty = rint()
    tx += 1
    ty += 1
    ans = sorted(kdtree[sx:tx,sy:ty]) + ['']
    print(*ans, sep='\n')
