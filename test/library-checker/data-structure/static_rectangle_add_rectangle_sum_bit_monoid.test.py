# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_rectangle_add_rectangle_sum

def main():
    mod, s, m = 998244353, 31, (1 << 31)-1
    N, Q = read()
    N4, Q4 = N<<2, Q<<2
    X, Y, V, W = [0]*N4,[0]*N4,[0]*N4,[0]*N4
    Xq, Yq = [0]*Q4,[0]*Q4
    for i in range(N):
        l, d, r, u, w = read()
        X[i:=i<<2], Y[i], V[i], W[i] = l, d, (-l*w%mod)<<s|(-d*w%mod),(( w%mod)<<s)|( l*d%mod*w%mod)
        X[i:=i +1], Y[i], V[i], W[i] = l, u, ( l*w%mod)<<s|( u*w%mod),((-w%mod)<<s)|(-l*u%mod*w%mod)
        X[i:=i +1], Y[i], V[i], W[i] = r, d, ( r*w%mod)<<s|( d*w%mod),((-w%mod)<<s)|(-r*d%mod*w%mod)
        X[i:=i +1], Y[i], V[i], W[i] = r, u, (-r*w%mod)<<s|(-u*w%mod),(( w%mod)<<s)|( r*u%mod*w%mod)
    for i in range(Q):
        l, d, r, u = read()
        Xq[i:=i<<2], Yq[i] = l, d
        Xq[i:=i +1], Yq[i] = l, u
        Xq[i:=i +1], Yq[i] = r, d
        Xq[i:=i +1], Yq[i] = r, u
    OYq = Yq[:]
    icoord_compress_with_queries(Yq,Y,x=1)
    def op(a, b):
        v = a+b
        return ((v>>s)%mod)<<s|(v&m)%mod
    Vseg, Wseg = BITMonoid(op, 0, N4+Q4), BITMonoid(op, 0, N4+Q4)

    def poly_eval(x,y,v,w):
        v1, v2 = v>>s, v&m; w1, w2 = w>>s, w&m
        return (w2+y*v1+x*v2+x*y%mod*w1)%mod

    qans = [0]*Q4
    for i in argsort_multi(X+Xq,Y+Yq):
        if i < N4:
            Vseg.add(Y[i],V[i]); Wseg.add(Y[i],W[i])
        else:
            i -= N4
            qans[i] = poly_eval(Xq[i],OYq[i],Vseg.sum(Yq[i]),Wseg.sum(Yq[i]))
    for i in range(Q):
        ans = (qans[i:=i<<2]-qans[i:=i+1]-qans[i:=i+1]+qans[i:=i+1])%mod
        write(ans)

from cp_library.ds.tree.bit.bit_monoid_cls import BITMonoid
from cp_library.alg.iter.arg.argsort_multi_fn import argsort_multi
from cp_library.alg.iter.cmpr.icoord_compress_with_queries_fn import icoord_compress_with_queries
from cp_library.io.write_fn import write
from cp_library.io.read_fn import read

if __name__ == "__main__":
    main()