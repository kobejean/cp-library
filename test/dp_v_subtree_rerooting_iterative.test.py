# verification-helper: PROBLEM https://atcoder.jp/contests/dp/tasks/dp_v

def main():
    N, M = read()
    T = read(Tree[N])

    def mul(a,b):
        return a*b%M

    def add_node(v,res):
        return (res+1)%M

    rr = ReRootingDP(T, 1, mul, add_node)

    print(*rr.solve(), sep='\n')

from cp_library.alg.dp.rerooting_iterative_cls import ReRootingDP
from cp_library.alg.tree.tree_cls import Tree
from cp_library.io.read_specs_fn import read

if __name__ == '__main__':
    main()