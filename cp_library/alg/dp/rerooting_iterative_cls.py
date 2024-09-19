import cp_library.alg.dp.__init__
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
        ans = [self.e for _ in range(len(self.T))]
        parent_idx = [None for _ in range(len(self.T))]
        child_idx = [None for _ in range(len(self.T))]
        stack = [(2,0,None),(0,0,None)]
        while stack:
            phase, u, p = stack.pop()
            match phase:
                case 0:  # Visit children
                    if p is not None:
                        stack.append((1,u,p))
                    for i,v in enumerate(self.T[u]):
                        if v != p:
                            stack.append((0,v,u))
                            child_idx[v] = i
                        else:
                            parent_idx[u] = i
                case 1:  # Upward updates
                    val = dp[p][child_idx[u]] = self.add_edge(p, u, self.add_node(u, ans[u]))
                    ans[p] = self.merge(ans[p], val)
                case 2:  # Downward updates
                    ba = BidirectionalArray(self.e, self.merge, dp[u])
                    for i,v in enumerate(self.T[u]):
                        if v != p:
                            dp[v][parent_idx[v]] = self.add_edge(v, u, self.add_node(u, ba.out(i)))
                            stack.append((2,v,u))
                    ans[u] = ba.all()
        return ans