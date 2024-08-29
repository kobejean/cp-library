import cp_library.misc.setrecursionlimit
from typing import Any, Callable, List, TypeVar, Generic
from cp_library.ds.bidirectional_array_cls import BidirectionalArray

T = TypeVar('T')

class ReRootingDP(Generic[T]):
    def __init__(self, T: List[List[int]], e: T, merge: Callable[[T, T], T], add_node: Callable[[int, T], T]) -> None:
        self.T = T
        self.e = e
        self.merge = merge
        self.add_node = add_node

    def solve(self) -> List[T]:
        dp = [[self.e]*len(adj) for adj in self.T]
        ans = [None for _ in range(len(self.T))]
        
        def dfs_up(u, p=None):
            res = self.e
            for i,v in enumerate(self.T[u]):
                if v != p:
                    dp[u][i] = dfs_up(v,u)
                    res = self.merge(res, dp[u][i])
            return self.add_node(u, res)
        
        def dfs_down(u, p=None):
            ba = BidirectionalArray(self.e, self.merge, dp[u])
            for i,v in enumerate(self.T[u]):
                if v != p:
                    dp[v][self.T[v].index(u)] = self.add_node(u, ba.out(i))
                    dfs_down(v,u)
            ans[u] = ba.all()
        
        dfs_up(0)
        dfs_down(0)
        return ans
