# verification-helper: PROBLEM https://atcoder.jp/contests/dp/tasks/dp_v

def main():
    N, M = read(tuple[int, ...])
    T = read(Tree[N])
    def merge(a,b): return a*b%M
    def add_node(s, i, p, u): return (s+1)%M
    ans = T.rerooting_dp(1, merge, add_node)
    write(*ans, sep='\n')

from cp_library.alg.tree.csr.tree_cls import Tree
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()