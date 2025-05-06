# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_frequency

def main():
    N, Q = map(int, input().split())
    A = [int(s) for s in input().split()]
    W = WaveletMatrix(A)
    for _ in range(Q):
        l, r, x = input().split()
        append(str(W.range_freq(int(l), int(r), int(x)))); append('\n')
    os.write(1, sb.build().encode())

from cp_library.ds.wavelet_matrix_cls import WaveletMatrix
import sys,os
from __pypy__ import builders
sb = builders.StringBuilder()
append = sb.append
def input(): return sys.stdin.buffer.readline().strip()

if __name__ == "__main__":
    main()