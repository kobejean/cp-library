# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/1/GRL/all/GRL_1_A
from math import inf
from cp_library.io.read_graph_weighted_directed_fn import read_graph
from cp_library.io.read_int_fn import read
from cp_library.alg.graph.dijkstra_fn import dijkstra

N, M, r = read()
G = read_graph(N, M, 0)
D = dijkstra(G, N, r)
print(*('INF' if d == inf else d for d in D), sep='\n')