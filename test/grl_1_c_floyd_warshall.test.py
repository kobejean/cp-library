# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/1/GRL_1_C
from math import inf
from cp_library.io.rint_fn import rint
from cp_library.io.read_graph_weighted_directed_fn import read_graph
from cp_library.alg.graph.floyd_warshall_check_neg_cycle_fn import floyd_warshall

N, M = rint()
G = read_graph(N, M, 0)
neg_cycle, D = floyd_warshall(G, N)

if neg_cycle:
    print("NEGATIVE CYCLE")
else:
    for row in D:
        print(*('INF' if d == inf else d for d in row))