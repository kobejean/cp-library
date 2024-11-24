import cp_library.alg.tree.__header__
from cp_library.alg.iter.presum_fn import presum
from cp_library.ds.sparse_table_cls import SparseTable

class LCATableWeighted(SparseTable):
    def __init__(self, T, root = 0):
        self.start = [-1] * len(T)
        self.end = [-1] * len(T)
        self.euler = []
        self.depth = []
        self.weights = []
        self.weighted_depth = None
        
        # Iterative DFS
        stack = [(root, -1, 0, 0)]
        while stack:
            u, p, d, w = stack.pop()
            
            if self.start[u] == -1:
                self.start[u] = len(self.euler)
                for v, nw in reversed(T[u]):
                    if v != p:
                        stack.append((u, p, d, -nw))
                        stack.append((v, u, d+1, nw))

            self.euler.append(u)
            self.depth.append(d)
            self.weights.append(w)
            self.end[u] = len(self.euler)
        super().__init__(min, list(zip(self.depth, self.euler)))

    def query(self, u, v) -> tuple[int,int]:
        l, r = min(self.start[u], self.start[v]), max(self.start[u], self.start[v])+1
        d, a = super().query(l, r)
        return a, d

    def distance(self, u, v) -> int:
        if self.weighted_depth is None:
            self.weighted_depth = presum(self.weights)
        l, r = min(self.start[u], self.start[v]), max(self.start[u], self.start[v])+1
        _, a = super().query(l, r)
        m = self.start[a]
        return self.weighted_depth[l] + self.weighted_depth[r] - 2*self.weighted_depth[m]