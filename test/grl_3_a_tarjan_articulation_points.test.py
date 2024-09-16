# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/3/GRL_3_A
from cp_library.io.read_graph_fn import read_graph
from cp_library.io.read_int_fn import read
from cp_library.alg.graph.tarjan_articulation_points_fn import tarjan_articulation_points

N, M = read()
G = read_graph(N, M, 0)
ans = sorted(tarjan_articulation_points(G, N))
if ans:
    print(*ans, sep='\n')