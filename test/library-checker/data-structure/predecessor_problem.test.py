# verification-helper: PROBLEM https://judge.yosupo.jp/problem/predecessor_problem

def main():
    N, Q = map(int, sys.stdin.readline().split())
    T = sys.stdin.readline()
    B = BitsetTree(T)
    for _ in range(Q):
        c, k = sys.stdin.readline().split()
        k = int(k)
        if c == '0':
            B[k] = 1
        elif c == '1':
            B[k] = 0
        elif c == '2':
            append(str(B[k]))
            append('\n')
        elif c == '3':
            append(str(B.ge(k)))
            append('\n')
        elif c == '4':
            append(str(B.le(k)))
            append('\n')
    os.write(1, sb.build().encode())

from cp_library.ds.tree.bitset_tree_cls import BitsetTree
import os
from __pypy__ import builders
sb = builders.StringBuilder()
append = sb.append
import sys

if __name__ == "__main__":
    main()