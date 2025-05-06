# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_frequency


def main():
    N, Q = map(int, input().split())
    A = [int(s) for s in input().split()]
    R, V = coord_compress(A)
    R.sort(); V.append(1 << 63)

    def find(A, x):
        l, r = 0, len(A)
        while l < r:
            if A[m := (l+r) >> 1] < x: l = m + 1
            else: r = m
        return l

    for _ in range(Q):
        l, r, x = input().split()
        x = int(x)
        if x == V[x:=find(V, x)]:
            x <<= 19
            append(str(find(R, x|int(r))-find(R, x|int(l)))); append('\n')
        else:
            append('0\n')
    os.write(1, sb.build().encode())

from cp_library.bit.pack_sm_fn import pack_dec, pack_sm


def coord_compress(A: list[int]):
    s, m = pack_sm((N := len(A))-1)
    R, V = [0]*N, [0]*N
    for i,a in enumerate(A): A[i] = a<<s|i
    A.sort()
    r = p = -1
    for ai in A:
        a, i = pack_dec(ai, s, m)
        if a != p: V[r:=r+1] = p = a
        R[i] = r<<19|i
    del V[r+1:]
    return R, V

import sys,os
from __pypy__ import builders
sb = builders.StringBuilder()
append = sb.append
def input(): return sys.stdin.buffer.readline().strip()

if __name__ == "__main__":
    main()