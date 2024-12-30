import cp_library.alg.graph.__header__
from typing import Iterator
from cp_library.io.parser_cls import Parsable, Parser, TokenStream

class FunctionalGraph(list[int], Parsable):
    def __init__(F, successors):
        super().__init__(successors)
        F.N = F.M = len(F)

    def find_cycle(P, root):
        slow = fast = root
        while (slow := P[slow]) != (fast := P[P[fast]]): pass
        cyc = [slow]
        while P[slow] != fast: cyc.append(slow := P[slow])
        return cyc
    
    def cycles(P) -> Iterator[list[int]]:
        vis, cycs, L = u8f(N := P.N), elist(N), elist(N)
        for v in range(P.N):
            if vis[v]: continue
            slow = fast = v
            while (slow := P[slow]) != (fast := P[P[fast]]) and not vis[fast]: pass
            if vis[fast]: continue
            L.append(len(cycs))
            cycs.append(slow)
            vis[slow := P[slow]] = 1
            while slow != fast:
                cycs.append(slow)
                vis[slow := P[slow]] = 1
        return SliceIteratorReverse(cycs, L)

    @classmethod
    def compile(cls, N: int, shift = -1):
        return Parser.compile_repeat(cls, shift, N)

from cp_library.alg.iter.slice_iterator_reverse_cls import SliceIteratorReverse
from cp_library.ds.array_init_fn import u8f
from cp_library.ds.elist_fn import elist