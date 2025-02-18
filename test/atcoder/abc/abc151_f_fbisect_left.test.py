# verification-helper: PROBLEM https://atcoder.jp/contests/abc151/tasks/abc151_f
# verification-helper: ERROR 1e-6

from math import sqrt

def main():
    N = read(int)
    points = read(list[Vec2D[float], N])

    def candidates(r) -> list[Vec2D[float]]:
        r2 = 2*r
        intersections = []
        for i in range(N):
            for j in range(i):
                if i == j: continue
                diff = points[j] - points[i]
                if (d := diff.magnitude()) <= r2:
                    diff /= d
                    d /= 2.0
                    diff = diff.rot90() * sqrt(r*r - d*d)
                    mid = (points[i]+points[j])/2.0
                    intersections.append(mid-diff)
                    intersections.append(mid+diff)

        return intersections

    def f(r):
        for candidate in candidates(r):
            if all(candidate.distance(point) <= r+1e-9 for point in points):
                return True
        return False
    
    ans = fbisect_left(f, 2000.0)
    write(f'{ans:0.18f}')


from cp_library.alg.divcon.fbisect_fn import fbisect_left
from cp_library.math.vec.vec2d_cls import Vec2D
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == "__main__":
    main()