# verification-helper: PROBLEM https://atcoder.jp/contests/abc246/tasks/abc246_e

def solve():
    N = read(int)
    Ax, Ay = read(tuple[-1, ...])
    Bx, By = read(tuple[-1, ...])
    G = read(BishopBoard[N,N])
    
    if (Ax+Ay)&1 != (Bx+By)&1:
        return -1 
    s,g = G.vertex((Ax, Ay)), G.vertex((Bx, By))
    ans = G.distance(s, g)
    return -1 if ans == inf else ans


def main():
    print(solve())

    

from collections import deque
from math import inf
from typing import Iterable
from cp_library.alg.graph.grid_direction_graph_cls import GridDirectionGraph
from cp_library.io.read_specs_fn import read

class BishopBoard(GridDirectionGraph):
    def __init__(G, H, W, S=...):
        super().__init__(H, W, S)
        G.dirs = [(1,1),(1,-1),(-1,1),(-1,-1)]
    
    def free_move(G, v: int, dir: int) -> Iterable[int]:
        if dir < 0: return v
        H, W = G.H, G.W
        i,j = divmod(v, W)
        di,dj = G.dirs[dir]
        ni,nj = i+di,j+dj
        if G.is_valid(ni, nj, u := ni*W+nj):
            return u
        return v
    
    def bfs(G, s = 0, g = None):
        D = [[inf]*4 for _ in range(G.N)]
        D[s] = [0]*4
        q = deque([(s,-1)])
        while q:
            u, dir = q.popleft()
            if u == g: return D[u][dir]
            
            nd = D[u][dir]
            if nd < D[v := G.free_move(u,dir)][dir]:
                D[v][dir] = nd
                q.appendleft((v,dir))
            nd += 1
            for v, ndir in G[u]:
                if nd < D[v][ndir]:
                    D[v][ndir] = nd
                    q.append((v,ndir))

        return D if g is None else inf    

if __name__ == "__main__":
    main()