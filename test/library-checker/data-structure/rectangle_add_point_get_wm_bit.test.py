# verification-helper: PROBLEM https://judge.yosupo.jp/problem/rectangle_add_point_get

def main():
    Y, W, T, Xq, Wq, Xp, Yp = read_compressed_problem()
    wm = WMBIT(Y, W, len(Y)-1)
    p = q = -1
    for t in T:
        if t == 0:
            wm.add(Xq[q:=q+1], Wq[q]); wm.add(Xq[q:=q+1], Wq[q]); wm.add(Xq[q:=q+1], Wq[q]); wm.add(Xq[q:=q+1], Wq[q])
        else:
            append(str(wm.sum_corner(Xp[p:=p+1], Yp[p]))); append('\n')
    os.write(1, sb.build().encode())

from cp_library.ds.wavelet.wm_bit_cls import WMBIT
from cp_library.alg.dp.max2_fn import max2
from cp_library.bit.pack.pack_sm_fn import pack_sm
from cp_library.ds.elist_fn import elist

def read_compressed_problem():
    N, Q = map(int, input().split())
    N4 = N<<2
    Xn, Yn, Wn = [0]*N4, [0]*N4, [0]*N4
    for i in range(N):
        l, d, r, u, w = map(int, input().split())
        Xn[i:=i<<2], Yn[i], Wn[i] = l, d, w
        Xn[i:=i+1], Yn[i], Wn[i] = l, u, -w
        Xn[i:=i+1], Yn[i], Wn[i] = r, d, -w
        Xn[i:=i+1], Yn[i], Wn[i] = r, u, w
    Xq, Yq, Wq, T = elist(Q<<2), elist(Q<<2), elist(Q<<2), [0]*Q
    Xp, Yp = elist(Q), elist(Q)
    for i in range(Q):
        T[i], *q = map(int, input().split())
        if T[i] == 0:
            l, d, r, u, w = q
            Xq.append(l); Yq.append(d); Wq.append(w)
            Xq.append(l); Yq.append(u); Wq.append(-w)
            Xq.append(r); Yq.append(d); Wq.append(-w)
            Xq.append(r); Yq.append(u); Wq.append(w)
        else:
            x, y = q
            Xp.append(x+1); Yp.append(y+1)
    icoord_compress_multi(Xp, Xq, Xn, x=1, distinct=True); icoord_compress_multi(Yp, Yq, Yn, x=1)
    Y, W = [0]*((N<<2)+len(Yq)), [0]*((N<<2)+len(Yq))
    for i,j in enumerate(Xn): Y[j], W[j] = Yn[i], Wn[i]
    for i,j in enumerate(Xq): Y[j] = Yq[i]
    return Y, W, T, Xq, Wq, Xp, Yp

def icoord_compress_multi(*A: list[int], x=0, distinct=False):
    N = mx = 0
    for Ai in A: N += len(Ai); mx = max2(mx, len(Ai))
    si, mi = pack_sm(mx-1); sj, mj = pack_sm((len(A)-1)<<si)
    S, k = [0]*N, 0
    for i,Ai in enumerate(A):
        for j,a in enumerate(Ai): S[k]=a << sj | i << si | j; k += 1
    S.sort(); r = p = -1
    for aji in S:
        a, i, j = aji >> sj, (aji&mj) >> si , aji & mi
        if x<=i and (distinct or a != p): r = r+1; p = a
        A[i][j] = r+(i==0)
    return A

import sys,os
from __pypy__ import builders # type: ignore
sb = builders.StringBuilder()
append = sb.append
def input(): return sys.stdin.buffer.readline().strip()

if __name__ == "__main__":
    main()