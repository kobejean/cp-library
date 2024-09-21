from typing import List

import cp_library.misc.setrecursionlimit
from cp_library.ds.sparse_table_cls import SparseTable

class LCATable(SparseTable):
    def __init__(self, T, root):
        self.start = [-1] * len(T)
        euler_tour = []
        depths = []
        
        def dfs(u: int, p: int, depth: int):
            self.start[u] = len(euler_tour)
            euler_tour.append(u)
            depths.append(depth)
            
            for child in T[u]:
                if child != p:
                    dfs(child, u, depth + 1)
                    euler_tour.append(u)
                    depths.append(depth)
        
        dfs(root, -1, 0)
        super().__header__(min, list(zip(depths, euler_tour)))

    def query(self, u, v) -> tuple[int,int]:
        l, r = min(self.start[u], self.start[v]), max(self.start[u], self.start[v])+1
        d, a = super().query(l, r)
        return a, d
