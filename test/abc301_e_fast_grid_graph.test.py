# verification-helper: PROBLEM https://atcoder.jp/contests/abc301/tasks/abc301_e

from math import inf


def solve():
    H, W, T = read(tuple[int, ...])
    G = read(GridGraph[H, W])
    s = G.S.find('S')
    g = G.S.find('G')
    O = [o for o in range(H*W) if G.S[o] == 'o']
    
    if G.distance(s,g) > T:
        return -1
    stops = [s] + O + [g]
    Y = len(stops)
    Z = 1 << Y
    D = []
    for u in stops:
        dist = G.distance(u)
        D.append([dist[v] for v in stops])
    
    dp = [[inf]*Y for _ in range(Z)]
    dp[1][0] = 0
    ans = [0]
    for mask in range(1,Z,2):
        for i, Di in enumerate(D):
            val = dp[mask][i]
            if mask >> i & 1 and val < inf:
                for j in range(1,Y):
                    nmask = mask | 1 << j
                    if nmask == mask: continue
                    chmin(dp[nmask], j, val+Di[j])
        if dp[mask][-1] <= T:
            chmax(ans, 0, mask.bit_count()-2)
    return ans[0]

from cp_library.alg.graph.fast.grid_graph_cls import GridGraph
from cp_library.alg.dp.chmin_fn import chmin
from cp_library.alg.dp.chmax_fn import chmax
from cp_library.io.read_fn import read

if __name__ == "__main__":
    print(solve())