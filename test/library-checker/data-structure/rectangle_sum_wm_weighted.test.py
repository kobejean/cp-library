# verification-helper: PROBLEM https://judge.yosupo.jp/problem/rectangle_sum

def main():
    N, Q = map(int, input().split())
    Xn, Yn, Wn = [0]*N, [0]*N, [0]*N; L, D, R, U = [0]*Q, [0]*Q, [0]*Q, [0]*Q
    for i in range(N): Xn[i], Yn[i], Wn[i] = map(int, input().split())
    for i in range(Q): L[i], D[i], R[i], U[i] = map(int, input().split())
    icoord_compress_multi(L, R, Xn, distinct=True); icoord_compress_multi(D, U, Yn)
    Y, W = [0]*N, [0]*N
    for i,j in enumerate(Xn): Y[j], W[j] = Yn[i], Wn[i]
    wm = WMWeighted(Y, W)
    for i in range(Q): append(str(wm.sum_rect(L[i], D[i], R[i], U[i]))); append('\n')
    os.write(1, sb.build().encode())

from cp_library.ds.wavelet.wm_weighted_points_cls import WMWeightedPoints
from cp_library.ds.wavelet.wm_weighted_cls import WMWeighted
from cp_library.alg.dp.max2_fn import max2
from cp_library.bit.pack.pack_sm_fn import pack_sm

def icoord_compress_multi(*A: list[int], distinct=False):
    N = mx = 0
    for Ai in A: N += len(Ai); mx = max2(mx, len(Ai))
    si, mi = pack_sm(mx-1); sj, mj = pack_sm((len(A)-1)<<si)
    S, k = [0]*N, 0
    for i,Ai in enumerate(A):
        for j,a in enumerate(Ai): S[k]=a << sj | i << si | j; k += 1
    S.sort(); r = p = -1
    for aji in S:
        a, i, j = aji >> sj, (aji&mj) >> si , aji & mi
        if i == 2 and (distinct or a != p): r = r+1; p = a
        A[i][j] = r+(i!=2)
    return A

import sys,os
from __pypy__ import builders # type: ignore
sb = builders.StringBuilder()
append = sb.append
def input(): return sys.stdin.buffer.readline().strip()

if __name__ == "__main__":
    main()