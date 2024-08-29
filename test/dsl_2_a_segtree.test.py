# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_A
from cp_library.ds.segtree_cls import SegTree

def rint(shift=0, base=10):
    return [int(x, base) + shift for x in input().split()]

N, Q = rint()

seg = SegTree(min, 2147483647, N)

for _ in range(Q):
    com, x, y = rint()
    if com:
        print(seg.prod(x,y+1))
    else:
        seg.set(x,y)
