import cp_library.alg.tree.__header__

class CentroidDecomposition():
    def __init__(self, tree):
        n = len(tree)
        self.n = n
        self.tree = tree
        self.par = [-1] * n
        self.dep = [-1] * n
        self.size = [1] * n
        self.used = [0] * n
        self.root = None

    def set_root(self, r):
        self.root = r
        self.par[r] = -1
        self.dep[r] = 0
        self.size[r] = 1
        self.ord = [r]
        stack = [r]
        while stack:
            v = stack.pop()
            for a in self.tree[v]:
                if self.par[v] == a or self.used[a]: continue
                self.size[a] = 1
                self.par[a] = v
                self.dep[a] = self.dep[v] + 1
                self.ord.append(a)
                stack.append(a)
        for v in reversed(self.ord):
            for a in self.tree[v]:
                if self.par[v] == a or self.used[a]: continue
                self.size[v] += self.size[a]

    def centroid(self, r):
        v = r
        while True:
            for a in self.tree[v]:
                if self.par[v] == a or self.used[a]: continue
                if self.size[a] > self.size[r] // 2:
                    v = a
                    break
            else:
                return v

    def centroid_decomposition(self, vis_centroid, vis_subtree):
        self.set_root(0)
        stack = [self.centroid(0)]
        while stack:
            v = stack.pop()
            self.used[v] = True
            self.set_root(v)
            vis_centroid(self, v)
            for a in self.tree[v]:
                if self.used[a]: continue
                self.set_root(a)
                vis_subtree(self, a)
                stack.append(self.centroid(a))