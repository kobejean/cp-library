import cp_library.__header__
import cp_library.alg.__header__
import cp_library.alg.graph.__header__
from cp_library.io.parser_cls import Parsable, Parser

class FuncGraph(list[int], Parsable):
    def __init__(F, successors):
        super().__init__(successors)
        F.N = F.M = len(F)

    def find_cycle(P, root: int) -> list[int]:
        slow = fast = root
        while (slow := P[slow]) != (fast := P[P[fast]]): pass
        cyc = [slow]
        while P[slow] != fast: cyc.append(slow := P[slow])
        return cyc
    
    def cycles(P) -> 'CRFList[int]':
        vis, cycs, S = u8f(N := P.N), elist(N), elist(N)
        for v in range(P.N):
            if vis[v]: continue
            slow = fast = v
            while (slow := P[slow]) != (fast := P[P[fast]]) and not vis[fast]: pass
            if vis[fast]: continue
            S.append(len(cycs))
            cycs.append(slow)
            vis[slow := P[slow]] = 1
            while slow != fast:
                cycs.append(slow)
                vis[slow := P[slow]] = 1
        return CRFList(cycs, S)
    
    def chain(P, root):
        cyc = P.find_cycle(root)
        slow, fast = root, cyc[0]
        if slow == fast: return [], cyc
        line = [slow]
        while (slow := P[slow]) != (fast := P[fast]):
            line.append(slow)
        return line, roll(cyc, -cyc.index(slow))

    @classmethod
    def compile(cls, N: int, shift = -1):
        return Parser.compile_repeat(cls, shift, N)

from cp_library.alg.iter.crf_list_cls import CRFList
from cp_library.alg.iter.roll_fn import roll
from cp_library.ds.array.u8f_fn import u8f
from cp_library.ds.elist_fn import elist