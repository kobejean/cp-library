# verification-helper: PROBLEM https://atcoder.jp/contests/abc184/tasks/abc184_e
from cp_library.math.inft_cnst import inft
from typing import Iterable

def main():
    H, W = read(tuple[int, ...])
    G = read(TeleportGraph[H,W])
    s = g = None
    for v,c in enumerate(G.S):
        match c:
            case 'S': s = v
            case 'G': g = v

    ans = G.bfs(s, g)
    print(ans if ans != inft else -1)
    
from cp_library.alg.graph.lazy_grid_graph_cls import LazyGridGraph

class TeleportGraph(LazyGridGraph):
    def __init__(G, H, W, S=[]):
        super().__init__(H, W, S)
        G.group = group = [set() for _ in range(26)]
        for u,c in enumerate(S):
            match c:
                case '.'|'#'|'S'|'G': ...
                case c: group[ord(c)-ord('a')].add(u)

    def neighbors(G, v: int) -> Iterable[int]:
        match G.S[v]:
            case '.'|'S'|'G': return super().neighbors(v)
            case c if adj := G.group[i := ord(c)-ord('a')]:
                G.group[i] = None
                adj.update(super().neighbors(v))
                return adj
            case _: return super().neighbors(v)
    

from cp_library.io.read_specs_fn import read

if __name__ == "__main__":
    main()