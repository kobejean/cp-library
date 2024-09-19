# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/1/GRL/all/GRL_1_A
from math import inf
from cp_library.io.read_specs_fn import read
from cp_library.alg.graph.dijkstra_fn import dijkstra
from cp_library.alg.graph.digraph_weighted_cls import DiGraphWeighted

N, M, r = read()
G = read(DiGraphWeighted[N, M, 0])
D = dijkstra(G, N, r)
print(*('INF' if d == inf else d for d in D), sep='\n')