import cp_library.misc.setrecursionlimit
from cp_library.ds.bidirectional_array import BidirectionalArray

class ReRootingDP:
    def __init__(self, G, e, merge, add_node) -> None:
        self.G = G
        self.e = e
        self.merge = merge
        self.add_node = add_node
        self.dp = None
        self.state = None
        self.ans = None

    def dfs_up(self,u):
        self.state[u] = 1
        res = self.e
        for i,v in enumerate(self.G[u]):
            if self.state[v] == 0:
                self.dp[u][i] = self.dfs_up(v)
                res = self.merge(res, self.dp[u][i])
        return self.add_node(u, res)
    
    def dfs_down(self,u):
        self.state[u] = 2
        ba = BidirectionalArray(self.e, self.merge, self.dp[u])
        for i,v in enumerate(self.G[u]):
            if self.state[v] == 1:
                self.dp[v][self.G[v].index(u)] = self.add_node(u, ba.out(i))
                self.dfs_down(v)
        self.ans[u] = ba.all()

    def solve(self):
        self.dp = [[self.e]*len(adj) for adj in self.G]
        self.state = [0 for _ in range(len(self.G))]
        self.ans = [self.e for _ in range(len(self.G))]
        self.dfs_up(0)
        self.dfs_down(0)
        return self.ans