from cp_library.ds.list.elist_fn import elist
import cp_library.alg.graph.__header__

from cp_library.alg.graph.func.func_graph_cls import FuncGraph

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

    def mark_finite(F):
        vis, finite = [0]*F.N, [1]*F.N
        for s in range(F.N):
            if vis[s]: continue
            slow = fast = s
            while F[fast]>=0 and (fast:=F[F[fast]])>=0 and not vis[fast]:
                if (slow:=F[slow]) == fast:
                    finite[fast] = 0; break
            fin = finite[fast] if fast >= 0 else 1
            slow = s
            while slow >= 0 and not vis[slow]:
                vis[slow], finite[slow] = 1, fin
                slow = F[slow]
        return finite

from cp_library.alg.iter.crf_list_cls import CRFList