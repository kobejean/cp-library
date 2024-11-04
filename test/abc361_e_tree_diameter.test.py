# verification-helper: PROBLEM https://atcoder.jp/contests/abc361/tasks/abc361_e

def main():
    N = read(int)
    T = read(TreeWeighted[N])
    diam, s, g = T.diameter(True)
    assert diam == T.distance(s, g)
    ans = sum(2*w for _, _, w in T.E) - diam
    print(ans)
    

from cp_library.io.read_specs_fn import read
from cp_library.alg.tree.tree_weighted_cls import TreeWeighted

if __name__ == '__main__':
    main()
