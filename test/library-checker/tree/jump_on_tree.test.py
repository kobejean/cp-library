# verification-helper: PROBLEM https://judge.yosupo.jp/problem/jump_on_tree

def main():
    N, Q = read()
    T = read(Tree[N,0])
    lca = LCATable(T)
    P = [T.par[:]]
    P[0].append(-1)
    for _ in range(18):
        par = P[-1]
        P.append([par[p] for p in par])

    def kth(v: int, k: int):
        for d in range(k.bit_length()):
            if k >> d & 1:
                v = P[d][v]
        return v
    
    for _ in range(Q):
        s, t, i = read()
        _, d = lca.query(s, t)
        ln = lca.depth[lca.tin[s]] - d
        rn = ln + lca.depth[lca.tin[t]] - d
        if i < ln:
            write(kth(s, i))
        elif i <= rn:
            write(kth(t, rn-i))
        else:
            write(-1)


from cp_library.alg.tree.lca_table_iterative_cls import LCATable
from cp_library.alg.tree.fast.tree_cls import Tree
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
