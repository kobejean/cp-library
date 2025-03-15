# verification-helper: PROBLEM https://atcoder.jp/contests/abc189/tasks/abc189_e

def main():
    N = read(int)
    pts = read(list[Vec2D, N])
    
    dx,dy = Vec2D(1,0), Vec2D(0,1)
    origin = Vec2D(0,0)
    
    M = read(int)
    states = [(dx,dy,origin)]
    for op in read(list[tuple[int, ...], M]):
        match op:
            case 1,:
                dx = dx.rot270()
                dy = dy.rot270()
                origin = origin.rot270()
            case 2,:
                dx = dx.rot90()
                dy = dy.rot90()
                origin = origin.rot90()
            case 3, p:
                origin = origin.flip_x()
                origin += Vec2D(2*p,0)
                dx = dx.flip_x()
                dy = dy.flip_x()
            case 4, p:
                origin = origin.flip_y()
                origin += Vec2D(0,2*p)
                dx = dx.flip_y()
                dy = dy.flip_y()
        states.append((dx,dy,origin))
        
    Q = read(int)
    for _ in range(Q):
        A, B = read(tuple[int,-1])
        x,y = pts[B]
        dx,dy,origin = states[A]
        ans = x*dx+y*dy + origin
        write(*ans)

from cp_library.io.read_fn import read
from cp_library.io.write_fn import write
from cp_library.math.linalg.vec.vec2d_cls import Vec2D

if __name__ == "__main__":
    main()