import cp_library.alg.graph.__header__

from cp_library.alg.graph.functional_graph_cls import FunctionalGraph

class PartialFunctionalGraph(FunctionalGraph):
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
        vis = [False]*F.N
        cycs = []
        for v in range(F.N):
            slow = fast = v
            while F[fast] != -1 and (fast := F[F[fast]]) != -1 and not vis[fast]:
                slow, fast = F[slow], F[F[fast]]
                if slow == fast:
                    cyc = [slow]
                    vis[slow] = True
                    while F[slow] != cyc[0]:
                        slow = F[slow]
                        cyc.append(slow)
                        vis[slow] = True
                    cycs.append(cyc)
                    break
        return cycs