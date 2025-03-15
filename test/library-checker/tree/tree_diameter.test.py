# verification-helper: PROBLEM https://judge.yosupo.jp/problem/tree_diameter

def main():
    N = read(int)
    T = read(TreeWeighted[N,0])
    X, s, t = T.diameter(True)
    U = T.recover_path(s, t)
    Y = len(U)
    write(X, Y)
    write(*U)

from cp_library.alg.tree.fast.tree_weighted_cls import TreeWeighted
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
