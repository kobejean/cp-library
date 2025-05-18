# verification-helper: PROBLEM https://judge.yosupo.jp/problem/predecessor_problem

def main():
    N, Q = map(int, sys.stdin.readline().split())
    T = sys.stdin.readline()

    def construct(T):
        B = u32f((M := (len(T)+31)>>5))
        for i,c in enumerate(T):
            if c == '1': B[i>>5] |= 1 << (i&31)
        return M, B
    
    M, B = construct(T)
    bit = BIT([popcnt32(b) for b in B])

    def count(b, r):
        return bit.sum(b)+popcnt32(B[b] & ((1<<r)-1))
    
    def get(b, r):
        return B[b]>>r&1
    
    def set(b, r, x):
        if get(b, r)^x:
            if x:
                B[b] |= 1 << r
                bit.add(b, 1)
            else:
                B[b] &= ~(1 << r)
                bit.add(b, -1)

    def ge(b, r):
        nb = bit.bisect_right(count(b, r))
        if nb < M:
            m = B[nb] if b < nb else (B[nb] >> r) << r
            return nb<<5|(m & -m).bit_length()-1
        else:
            return -1
        
    def le(b, r):
        nb = bit.bisect_left(count(b, r+1))
        if 0 <= nb:
            m = B[nb] if nb < b else (B[nb] & ((1<<(r+1))-1))
            return nb<<5|m.bit_length()-1
        else:
            return -1

    for _ in range(Q):
        c, k = sys.stdin.readline().split()
        k = int(k)
        b, r = k>>5, k&31
        if c == '0': set(b, r, 1)
        elif c == '1': set(b, r, 0)
        elif c == '2':
            append(str(get(b, r)))
            append('\n')
        elif c == '3':
            append(str(ge(b, r)))
            append('\n')
        elif c == '4':
            append(str(le(b, r)))
            append('\n')
    os.write(1, sb.build().encode())

from cp_library.bit.popcnt32_fn import popcnt32
from cp_library.ds.array.u32f_fn import u32f
from cp_library.ds.tree.bit.bit_cls import BIT

import os
from __pypy__ import builders
sb = builders.StringBuilder()
append = sb.append
import sys

if __name__ == "__main__":
    main()