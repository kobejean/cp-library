import cp_library.alg.dp.__init__
import cp_library.misc.setrecursionlimit
import typing
from cp_library.ds.bidirectional_array_cls import BidirectionalArray

class ReRootingDP():
    """ A class implementation of the Re-rooting Dynamic Programming technique. """
    S = typing.TypeVar('S')
    MergeOp = typing.Callable[[S, S], S]
    AddNodeOp = typing.Callable[[int, S], S]
    AddEdgeOp = typing.Callable[[int, int, S], S]

    def __init__(self, T: list[list[int]], e: S,
                 merge: MergeOp, 
                 add_node: AddNodeOp = lambda u,s:s, 
                 add_edge: AddEdgeOp = lambda u,v,s:s):
        """
        T: list[list[int]] - Adjacency list representation of the tree.
        e: S - Identity element for the merge operation.
        merge: (S,S) -> S - Function to merge two states.
        add_node: (int,S) -> S - Function to incorporate a node into the state.
        add_edge: (int,int,S) -> S - Function to incorporate an edge into the state.
        """
        self.T = T
        self.e = e
        self.merge = merge
        self.add_node = add_node
        self.add_edge = add_edge
    
    def solve(self) -> list[S]:
        dp = [[self.e]*len(adj) for adj in self.T]
        ans = [None for _ in range(len(self.T))]

        def dfs_up(u, p=None):
            res = self.e
            for i,v in enumerate(self.T[u]):
                if v != p:
                    dp[u][i] = self.add_edge(u, v, dfs_up(v, u))
                    res = self.merge(res, dp[u][i])
            return self.add_node(u, res)

        def dfs_down(u, p=None):
            ba = BidirectionalArray(self.e, self.merge, dp[u])
            for i,v in enumerate(self.T[u]):
                if v != p:
                    dp[v][self.T[v].index(u)] = self.add_edge(v, u, self.add_node(u, ba.out(i)))
                    dfs_down(v, u)
            ans[u] = ba.all()

        dfs_up(0)
        dfs_down(0)
        return ans