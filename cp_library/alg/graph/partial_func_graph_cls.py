from cp_library.ds.elist_fn import elist
import cp_library.alg.graph.__header__

from cp_library.alg.graph.func_graph_cls import FuncGraph

class PartialFuncGraph(FuncGraph):
    def __init__(F, successors):
        super().__init__(successors)
        F.M = sum(f>=0 for f in F)

    def find_cycle(F, root):
        slow = fast = root
        while F[fast] != -1 and F[F[fast]] != -1:
            slow, fast = F[slow], F[F[fast]]
            if slow == fast:
                cyc = [slow]
                while F[slow] != cyc[0]:
                    slow = F[slow]
                    cyc.append(slow)
                return cyc
        return None
    
    def cycles(F):
        vis, cycs, S = [False]*F.N, elist(F.N), elist(F.N)
        for v in range(F.N):
            slow = fast = v
            while F[fast] != -1 and (fast := F[F[fast]]) != -1 and not vis[fast]:
                slow, fast = F[slow], F[F[fast]]
                if slow == fast:
                    S.append(len(cycs))
                    cycs.append(slow)
                    vis[slow] = True
                    while F[slow] != fast:
                        slow = F[slow]
                        cycs.append(slow)
                        vis[slow] = True
                    break
        return CRFList(cycs, S)

from cp_library.alg.iter.crf_list_cls import CRFList