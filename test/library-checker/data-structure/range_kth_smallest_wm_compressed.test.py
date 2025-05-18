# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_kth_smallest

def main():
    N, Q = map(int, sys.stdin.readline().split())
    A = [int(s) for s in sys.stdin.readline().split()]
    wm = WMCompressed(A)
    for _ in range(Q):
        l, r, k = sys.stdin.readline().split()
        append(str(wm.kth(int(k), int(l), int(r)))); append('\n')
    os.write(1, sb.build().encode())

from cp_library.ds.wavelet.wm_compressed_cls import WMCompressed
import os
import sys
from __pypy__ import builders
sb = builders.StringBuilder()
append = sb.append

if __name__ == "__main__":
    main()