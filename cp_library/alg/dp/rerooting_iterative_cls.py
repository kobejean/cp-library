from typing import Any, Callable, List, TypeVar, Generic
from cp_library.ds.bidirectional_array_cls import BidirectionalArray

T = TypeVar('T')

class ReRootingDP(Generic[T]):
    def __init__(self, T: List[List[int]], e: T, merge: Callable[[T, T], T], add_node: Callable[[int, T], T]) -> None:
        self.T = T
        self.e = e
        self.merge = merge
        self.add_node = add_node

    def solve(self) -> List[Any]:
        dp = [[self.e]*len(adj) for adj in self.T]
        ans = [self.e for _ in range(len(self.T))]
        parent_idx = [None for _ in range(len(self.T))]
        child_idx = [None for _ in range(len(self.T))]
        stack = [(2,0,None),(0,0,None)]
        
        while stack:
            phase, u, p = stack.pop()
            match phase:
                case 0: # phase 0: Visit children
                    if p != None:
                        stack.append((1,u,p))
                    for i,v in enumerate(self.T[u]):
                        if v != p:
                            stack.append((0,v,u))
                            child_idx[v] = i
                        else:
                            parent_idx[u] = i
                case 1: # phase 1: Upward updates
                    val = dp[p][child_idx[u]] = self.add_node(u, ans[u])
                    ans[p] = self.merge(ans[p], val)
                case 2: # phase 2: Downward updates
                    ba = BidirectionalArray(self.e, self.merge, dp[u])
                    for i,v in enumerate(self.T[u]):
                        if v != p:
                            dp[v][parent_idx[v]] = self.add_node(u, ba.out(i))
                            stack.append((2,v,u))
                    ans[u] = ba.all()
        return ans
