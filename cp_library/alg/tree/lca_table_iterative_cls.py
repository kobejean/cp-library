import cp_library.alg.tree.__header__
from cp_library.ds.sparse_table_cls import SparseTable

class LCATable(SparseTable):
    def __init__(self, T, root = 0):
        self.start = [-1] * len(T)
        self.end = [-1] * len(T)
        self.euler = []
        self.depth = []
        
        # Iterative DFS
        stack = [(root, -1, 0)]
        while stack:
            u, p, d = stack.pop()
            
            if self.start[u] == -1:
                self.start[u] = len(self.euler)
                
                for v in reversed(T[u]):
                    if v != p:
                        stack.append((u, p, d))
                        stack.append((v, u, d+1))
                        
            self.euler.append(u)
            self.depth.append(d)
            self.end[u] = len(self.euler)
        super().__init__(min, list(zip(self.depth, self.euler)))

    def query(self, u, v) -> tuple[int,int]:
        l, r = min(self.start[u], self.start[v]), max(self.start[u], self.start[v])+1
        d, a = super().query(l, r)
        return a, d
