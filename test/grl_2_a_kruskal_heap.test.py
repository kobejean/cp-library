# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_A
from cp_library.io.rint_fn import rint
from cp_library.io.read_edges_weighted_fn import read_edges
from cp_library.alg.graph.kruskal_heap_fn import kruskal

N, M = rint()
E = read_edges(M, 0)
MST = kruskal(E, N)
ans = sum(w for w,u,v in MST)
print(ans)