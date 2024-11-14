import cp_library.alg.graph.__header__

from cp_library.io.parser_cls import Parsable, Parser, TokenStream

class FunctionalGraph(list[int], Parsable):
    def __init__(F, successors):
        super().__init__(successors)
        F.N = F.M = len(F)

    def find_cycle(P, root):
        slow = fast = root
        while (slow := P[slow]) != (fast := P[P[fast]]):
            pass
        
        cyc = [slow]
        while P[slow] != cyc[0]:
            slow = P[slow]
            cyc.append(slow)
        return cyc
    
    def cycles(P):
        vis = [False]*P.N
        cycs = []
        for v in range(P.N):
            slow = fast = v
            while (slow := P[slow]) != (fast := P[P[fast]]) and not vis[fast]:
                pass
            if vis[fast]: continue
            
            cyc = [slow]
            vis[slow] = True
            while P[slow] != cyc[0]:
                slow = P[slow]
                cyc.append(slow)
                vis[slow] = True
            cycs.append(cyc)
        return cycs

    @classmethod
    def compile(cls, N: int, shift = -1):
        return Parser.compile_n_ints(cls, N, shift)