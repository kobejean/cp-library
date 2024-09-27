import cp_library.alg.tree.__header__
from itertools import pairwise
from cp_library.alg.tree.lca_table_iterative_cls import LCATable

class AuxiliaryTree(LCATable):

    def build_auxiliary_tree(self, V):
        V = sorted(V, key=lambda x: self.start[x])
        stack = [V[0]]
        for u, v in pairwise(V):
            lca, _ = self.query(u, v)
            while len(stack) > 1 and self.start[stack[-1]] > self.start[lca]:
                stack.pop()
            if stack[-1] != lca:
                stack.append(lca)
            stack.append(v)

        aux_tree = { v: [] for v in stack }
        for p, c in pairwise(stack):
            aux_tree[p].append(c)
        return aux_tree

    def get_path(self, u, v):
        lca, _ = self.query(u, v)
        path = []
        
        # Path from u to LCA
        current = u
        while current != lca:
            path.append(current)
            for parent in self.T[current]:
                if self.start[parent] < self.start[current]:
                    current = parent
                    break
        
        # Add LCA
        path.append(lca)
        
        # Path from LCA to v (in reverse order)
        current = v
        reverse_path = []
        while current != lca:
            reverse_path.append(current)
            for parent in self.T[current]:
                if self.start[parent] < self.start[current]:
                    current = parent
                    break
        # Combine paths
        path.extend(reversed(reverse_path))
        return path