from typing import List

from cp_library.ds.sparse_table_cls import SparseTable

class LCATable(SparseTable):
    def __init__(self, T: List[List[int]], root: int = 0):
        self.start = [-1] * len(T)
        euler_tour = []
        depths = []
        
        # Iterative DFS
        stack = [(root, -1, 0)]
        while stack:
            u, p, depth = stack.pop()
            
            if self.start[u] == -1:  # start visit to this node
                self.start[u] = len(euler_tour)
                euler_tour.append(u)
                depths.append(depth)
                
                # Add children to stack in reverse order
                for child in reversed(T[u]):
                    if child != p:
                        stack.append((u, p, depth))  # Re-add parent for backtracking
                        stack.append((child, u, depth + 1))
            else:  # Revisiting node (backtracking)
                euler_tour.append(u)
                depths.append(depth)
        super().__init__(min, list(zip(depths, euler_tour)))

    def query(self, u: int, v: int) -> int:
        l, r = min(self.start[u], self.start[v]), max(self.start[u], self.start[v])+1
        _, a = super().query(l, r)
        return a
