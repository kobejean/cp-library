# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_5_A

def main():
    N = read(int)
    T = read(TreeWeighted[N, 0])
    write(T.diameter())

from cp_library.io.read_fn import read
from cp_library.io.write_fn import write
from cp_library.alg.tree.csr.tree_weighted_cls import TreeWeighted

if __name__ == '__main__':
    main()