# verification-helper: PROBLEM https://atcoder.jp/contests/dp/tasks/dp_v


def main():
    N, M = read(tuple[int, ...])
    T = read(Tree[N])

    def merge(a,b):
        return a*b%M

    def add_node(p, c, i, res):
        return (res+1)%M
    
    e = 1

    ans = T.rerooting_dp(e, merge, add_node)

    write(*ans, sep='\n')

from array import array
from math import ceil, log10
import os

from cp_library.alg.graph.fast.tree_cls import Tree
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()