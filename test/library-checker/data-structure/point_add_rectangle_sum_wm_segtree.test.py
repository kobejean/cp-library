# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_rectangle_sum

from operator import add

def main():
    N, Q = map(int, input().split())
    Xn, Yn, Wn, Xq, Yq, Wq = [0]*N, [0]*N, [0]*N, elist(Q), elist(Q), elist(Q)
    T, L, D, R, U = elist(Q), elist(Q), elist(Q), elist(Q), elist(Q)
    # read input
    for i in range(N): Xn[i], Yn[i], Wn[i] = map(int, input().split())
    for i in range(Q):
        t, *q = map(int, input().split())
        if t == 0: x, y, w = q; Xq.append(x); Yq.append(y); Wq.append(w)
        else: l, d, r, u = q; L.append(l); D.append(d); R.append(r); U.append(u)
        T.append(t)
    L, R, Xn, Xq = icoord_compress_with_queries(L, R, Xn, Xq, distinct=True)
    D, U, Yn, Yq = icoord_compress_with_queries(D, U, Yn, Yq)
    # sort by X value
    Y, W = [0]*(N+len(Yq)), [0]*(N+len(Wq))
    for i,j in enumerate(Xn): Y[j], W[j] = Yn[i], Wn[i]
    for i,j in enumerate(Xq): Y[j], W[j] = Yq[i], 0

    wm = WMSegTree(add, 0, Y, W)
    t0 = t1 = 0
    for t in T:
        if t == 0: wm.set(Xq[t0], wm.get(Xq[t0])+Wq[t0]); t0 += 1
        else: append(str(wm.prod_rect(L[t1], D[t1], R[t1], U[t1]))); append('\n'); t1 += 1
    os.write(1, sb.build().encode())

from cp_library.ds.wavelet.wm_segtree_cls import WMSegTree
from cp_library.bit.pack.pack_sm_fn import pack_sm
from cp_library.alg.dp.max2_fn import max2
from cp_library.ds.list.elist_fn import elist

def icoord_compress_with_queries(*A: list[int], distinct=False):
    N = mx = 0
    for Ai in A: N += len(Ai); mx = max2(mx, len(Ai))
    si, mi = pack_sm(mx-1); sj, mj = pack_sm((len(A)-1)<<si)
    S, k = [0]*N, 0
    for i,Ai in enumerate(A):
        for j,a in enumerate(Ai): S[k]=a << sj | i << si | j; k += 1
    S.sort()
    r = p = -1
    for aji in S:
        a, i, j = aji >> sj, (aji&mj) >> si , aji & mi
        if 2<=i and (distinct or a != p): r = r+1; p = a
        A[i][j] = r+(i<2)
    return A
import sys,os
from __pypy__ import builders # type: ignore
sb = builders.StringBuilder()
append = sb.append
def input(): return sys.stdin.buffer.readline().strip()

if __name__ == "__main__":
    main()
    