# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_rectangle_sum


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
    wm = WMBITPoints(Xq+Xn, Yq+Yn,[0]*len(Xq)+Wn)
    t0 = t1 = 0
    for t in T:
        if t == 0: wm.add(t0, Wq[t0]); t0 += 1
        else: append(str(wm.sum_rect(L[t1], D[t1], R[t1], U[t1]))); append('\n'); t1 += 1
    os.write(1, sb.build().encode())

from cp_library.ds.wavelet.wm_bit_points_cls import WMBITPoints
from cp_library.ds.elist_fn import elist

import sys,os
from __pypy__ import builders # type: ignore
sb = builders.StringBuilder()
append = sb.append
def input(): return sys.stdin.buffer.readline().strip()

if __name__ == "__main__":
    main()
    