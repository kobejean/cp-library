# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/1/GRL/all/GRL_1_B
from math import inf
from cp_library.io.rint_fn import rint
from cp_library.io.read_graph_weighted_directed_fn import read_graph
from cp_library.alg.graph.bellman_ford_neg_cyc_check_fn import bellman_ford

N, M, r = rint()
G = read_graph(N, M, 0)

neg_cycle, D = bellman_ford(G, N, r)

if neg_cycle:
    print("NEGATIVE CYCLE")
else:
    print(*('INF' if d == inf else d for d in D), sep='\n')