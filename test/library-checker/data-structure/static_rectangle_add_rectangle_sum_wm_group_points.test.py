# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_rectangle_add_rectangle_sum

def main():
    mod, s, m = 998244353, 31, (1 << 31)-1
    N, Q = read(tuple[int, ...])
    N4 = N<<2
    X, Y, W = [0]*N4,[0]*N4,[(0,0)]*N4
    mod2 = mod<<s|mod
    def polynomial(x, y, w):
        # coefficients
        return (-x*w%mod)<<s|(-y*w%mod),((w%mod)<<s)|(x*y%mod*w%mod)
    for i in range(N):
        l, d, r, u, w = read()
        X[i:=i<<2], Y[i], W[i] = l, d, polynomial(l, d, w)
        X[i:=i +1], Y[i], W[i] = l, u, polynomial(l, u, -w)
        X[i:=i +1], Y[i], W[i] = r, d, polynomial(r, d, -w)
        X[i:=i +1], Y[i], W[i] = r, u, polynomial(r, u, w)
    
    def op(a, b):
        av, aw = a; bv, bw = b; v, w = av+bv,aw+bw
        return ((v>>s)%mod)<<s|((v&m)%mod),((w>>s)%mod)<<s|((w&m)%mod)
    def diff(a, b):
        av, aw = a; bv, bw = b; v, w = av+mod2-bv,aw+mod2-bw
        return ((v>>s)%mod)<<s|((v&m)%mod),((w>>s)%mod)<<s|((w&m)%mod)
    e = 0,0
    wm = WMGroupPoints(op, e, diff, X, Y, W)
    
    def poly_eval(x,y,poly):
        v, w = poly; v1, v2 = v>>s, v&m; w1, w2 = w>>s, w&m
        return (w2+y*v1+x*v2+x*y%mod*w1)%mod
    for _ in range(Q):
        l, d, r, u = read()
        ld = poly_eval(l,d,wm.prod_corner(l,d))
        lu = poly_eval(l,u,wm.prod_corner(l,u))
        rd = poly_eval(r,d,wm.prod_corner(r,d))
        ru = poly_eval(r,u,wm.prod_corner(r,u))
        ans = (ru+ld-lu-rd)%mod
        write(ans)

from cp_library.ds.wavelet.wm_group_points_cls import WMGroupPoints
from cp_library.io.write_fn import write
from cp_library.io.read_fn import read

if __name__ == "__main__":
    main()