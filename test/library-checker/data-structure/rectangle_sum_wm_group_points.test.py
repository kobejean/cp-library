# verification-helper: PROBLEM https://judge.yosupo.jp/problem/rectangle_sum

from operator import add, sub

def main():
    N, Q = map(int, input().split())
    X, Y, W = [0]*N, [0]*N, [0]*N
    for i in range(N): X[i], Y[i], W[i] = map(int, input().split())
    wm = WMGroupPoints(add, 0, sub, X, Y, W)
    for i in range(Q): append(str(wm.prod_rect(*map(int, input().split())))); append('\n')
    os.write(1, sb.build().encode())

from cp_library.ds.wavelet.wm_group_points_cls import WMGroupPoints
import sys,os
from __pypy__ import builders # type: ignore
sb = builders.StringBuilder()
append = sb.append
def input(): return sys.stdin.buffer.readline().strip()

if __name__ == "__main__":
    main()
    