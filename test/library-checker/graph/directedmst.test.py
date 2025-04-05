# verification-helper: PROBLEM https://judge.yosupo.jp/problem/directedmst
import os,sys,io
input=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline


class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.n = n

    def root(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def merge(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        return True

    def same(self, x, y):
        return self.root(x) == self.root(y)

from cp_library.ds.heap.skew_heap_forest_cls import SkewHeapForest

def directed_mst(n, edges, root):
    OFFSET = 1 << 31
    from_ = [0] * n
    from_cost = [0] * n
    from_heap = SkewHeapForest(n, len(edges))

    uf = UnionFind(n)
    par_e = [-1] * m
    stem = [-1] * n
    used = [0] * n
    used[root] = 2
    idxs = []

    for idx, (fr, to, cost) in enumerate(edges):
        from_heap.push(to, cost << 31 | idx)

    res = 0
    for v in range(n):
        if used[v] != 0:
            continue
        processing = []
        chi_e = []
        cycle = 0
        while used[v] != 2:
            used[v] = 1
            processing.append(v)
            if from_heap.empty(v):
               return -1, par
            from_cost[v], idx = divmod(from_heap.pop(v), OFFSET)
            from_[v] = uf.root(edges[idx][0])
            if stem[v] == -1:
                stem[v] = idx
            if from_[v] == v:
                continue
            res += from_cost[v]
            idxs.append(idx)
            while cycle:
                par_e[chi_e.pop()] = idx
                cycle -= 1
            chi_e.append(idx)
            if used[from_[v]] == 1:
                p = v
                while True:
                    if not from_heap.empty(p):
                        from_heap.add(p, -from_cost[p] << 31)
                    if p != v:
                        uf.merge(v, p)
                        from_heap.roots[v] = from_heap.merge(from_heap.roots[v], from_heap.roots[p])
                    p = uf.root(from_[p])
                    cycle += 1
                    if p == v:
                        break
            else:
                v = from_[v]
        for v in processing:
            used[v] = 2

    used_e = [0] * m
    tree = [-1] * n
    for idx in reversed(idxs):
        if used_e[idx]:
            continue
        fr, to, cost = edges[idx]
        tree[to] = fr
        x = stem[to]
        while x != idx:
            used_e[x] = 1
            x = par_e[x]
    return res, tree


n, m, root = map(int, input().split())
edges = [[int(s) for s in input().split()] for i in range(m)]


res, par = directed_mst(n, edges, root)
if res == -1:
    print(res)
else:
    print(res)
    print(*[p if p != -1 else i for i, p in enumerate(par)])