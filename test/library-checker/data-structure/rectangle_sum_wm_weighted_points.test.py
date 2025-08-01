# verification-helper: PROBLEM https://judge.yosupo.jp/problem/rectangle_sum

def main():
    N, Q = map(int, input().split())
    X, Y, W = [0]*N, [0]*N, [0]*N
    for i in range(N): X[i], Y[i], W[i] = map(int, input().split())
    wm = WMWeightedPoints(X, Y, W)
    for i in range(Q):
        append(str(wm.sum_rect(*map(int, input().split())))); append('\n')
    os.write(1, sb.build().encode())

from cp_library.ds.wavelet.wm_weighted_points_cls import WMWeightedPoints
import sys,os
from __pypy__ import builders # type: ignore
sb = builders.StringBuilder()
append = sb.append
def input(): return sys.stdin.buffer.readline().strip()

if __name__ == "__main__":
    main()
    