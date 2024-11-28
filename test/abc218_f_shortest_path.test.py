# verification-helper: PROBLEM https://atcoder.jp/contests/abc218/tasks/abc218_f

from cp_library.math.inft_cnst import inft

def main():
    N, M = read(tuple[int, ...])
    G = read(DiGraph[N,M])
    path = G.shortest_path(0,N-1)
    if path is None:
        shortest = -1
    else:
        path = set(path)
        shortest = len(path)
    for e in range(M):
        if path is not None and e in path:
            G2 = DiGraph(N, G.E[:e]+G.E[e+1:])
            ans = G2.distance(0,N-1)
        else:
            ans = shortest
        write(ans if ans != inft else -1)

from cp_library.alg.graph.digraph_cls import DiGraph
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == "__main__":
    main()