# verification-helper: PROBLEM https://atcoder.jp/contests/abc361/tasks/abc361_e

def main():
    N = read(int)
    T = read(TreeWeighted[N])
    diam, s, g = T.diameter(True)
    assert diam == T.distance(s, g)
    ans = 2*sum(T.W) - diam
    write(ans)

from cp_library.io.read_fn import read
from cp_library.io.write_fn import write
from cp_library.alg.tree.csr.tree_weighted_cls import TreeWeighted

if __name__ == '__main__':
    main()
