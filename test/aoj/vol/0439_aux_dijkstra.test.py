# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/problems/0439

from cp_library.alg.tree.csr.aux_tree_cls import AuxTree
def main():
    inf = 1 << 61
    N = read(int)
    C = read(list[-1, N])
    T = read(AuxTree[N])
    que = PriorityQueue(N)
    clean = elist(N)
    ans = [inf]*N
    D = [inf]*N

    def dist(s, c):
        que.push(0, s); clean.append(s); D[s] = 0
        while que:
            d, u = que.pop()
            if d > D[u]: continue
            if u != s and C[u] == c:
                while clean: D[clean.pop()] = inf
                que.clear()
                return d
            for i in T.range(u):
                v, nd = T.Va[i], T.Wa[i]+d
                if chmin(D, v, nd):
                    que.push(nd, v); clean.append(v)


    for c, V, post in T.trees(C):
        for u in V:
            if C[u] == c:
                ans[u] = dist(u, c)

    write(*ans, sep='\n')

from cp_library.ds.heap.priority_queue_cls import PriorityQueue
from cp_library.alg.dp.chmin_fn import chmin
from cp_library.ds.elist_fn import elist
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write


if __name__ == '__main__':
    main()