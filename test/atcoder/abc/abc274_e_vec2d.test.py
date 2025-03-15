# verification-helper: PROBLEM https://atcoder.jp/contests/abc274/tasks/abc274_e
# verification-helper: ERROR 1e-6
from math import inf

def main():
    N, M = read(tuple[int, ...])
    XY = read(list[Vec2D, N])
    PQ = read(list[Vec2D, M])
    pts = PQ+XY
    o = Vec2D(0,0)
    Tmask = (1 << M) -1
    Y = N+M
    Z = 1 << Y
    O = [o.distance(v) for v in pts]
    F = [1/(1 << mask.bit_count()) for mask in range(1 << M)]
    
    dp = [[inf]*Y for _ in range(Z)]
    for y in range(Y):
        mask = 1 << y
        dp[mask][y] = O[y]
        
    for mask in range(1,Z):
        factor = F[mask&Tmask]
        for y in range(Y):
            nmask = mask | 1 << y
            if mask == nmask: continue
            nc = dp[nmask][y]
            for l in range(Y):
                nc = min(nc, dp[mask][l] + pts[l].distance(pts[y]) * factor)
            dp[nmask][y] = nc
            
    full = Z-1
    ans = inf
    for tmask in range(1<<M):
        mask = full ^ tmask
        factor = F[mask&Tmask]
        for l in range(Y):
            nc = dp[mask][l] + O[l] * factor
            ans = min(ans, nc)
    write(f'{ans:0.10f}')

from cp_library.math.linalg.vec.vec2d_cls import Vec2D
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == "__main__":
    main()