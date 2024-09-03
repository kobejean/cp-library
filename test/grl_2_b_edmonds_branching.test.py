# verification-helper: PROBLEM https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/2/GRL_2_B
from cp_library.io.rint_fn import rint
from cp_library.io.read_edges_weighted_fn import read_edges
from cp_library.alg.graph.edmonds_fn import edmonds_branching

N, M, root = rint()
E = read_edges(M, 0)
MCA = edmonds_branching(E, N, root)
# print(MCA)
ans = sum(w for w,u,v in MCA)
print(ans)