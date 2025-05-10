# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_count_distinct

from cp_library.bit.pack_sm_fn import pack_dec, pack_sm

def main():
    N, Q = map(int, input().split())
    A = [int(s) for s in input().split()]
    W = WaveletMatrix(jumps(A), N)
    for _ in range(Q):
        l, r = input().split()
        l, r = int(l), int(r)
        append(str(W.count_below(l+1, l, r))); append('\n')
    os.write(1, sb.build().encode())

def jumps(A: list[int]):
    s, m = pack_sm((N := len(A))-1)
    R, V = [0]*N, [0]*N
    for i,a in enumerate(A): A[i] = a<<s|i
    A.sort()
    r = p = -1
    for ai in A:
        a, i = pack_dec(ai, s, m)
        if a != p: r += 1; p = a
        R[i], V[r] = V[r], i+1
    return R

from cp_library.ds.tree.wavelet.wavelet_matrix_cls import WaveletMatrix
import sys,os
from __pypy__ import builders # type: ignore
sb = builders.StringBuilder()
append = sb.append
def input(): return sys.stdin.buffer.readline().strip()

if __name__ == "__main__":
    main()