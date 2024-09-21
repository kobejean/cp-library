from cp_library.ds.sparse_table_cls import SparseTable

class LCATable(SparseTable):
    def __init__(self, T, root = 0):
        self.start = [-1] * len(T)
        self.euler = []
        self.depth = []
        
        # Iterative DFS
        stack = [(root, -1, 0)]
        while stack:
            u, p, d = stack.pop()
            
            if self.start[u] == -1:  # start visit to this node
                self.start[u] = len(self.euler)
                self.euler.append(u)
                self.depth.append(d)
                
                # Add children to stack in reverse order
                for child in reversed(T[u]):
                    if child != p:
                        stack.append((u, p, d))  # Re-add parent for backtracking
                        stack.append((child, u, d + 1))
            else:  # Revisiting node (backtracking)
                self.euler.append(u)
                self.depth.append(d)
        super().__header__(min, list(zip(self.depth, self.euler)))

    def query(self, u, v) -> tuple[int,int]:
        l, r = min(self.start[u], self.start[v]), max(self.start[u], self.start[v])+1
        d, a = super().query(l, r)
        return a, d
