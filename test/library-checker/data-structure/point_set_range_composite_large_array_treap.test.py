# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_set_range_composite_large_array

def main():
    mod = 998244353
    P = Packer((1<<30)-1)
    N, Q = read()
    TreapMonoid.reserve(1+2*Q)
    
    def op(a,b):
        ac, ad = P.dec(a)
        bc, bd = P.dec(b)
        return P.enc(ac*bc%mod, (ad*bc+bd)%mod)
    T = TreapMonoid(op, 1<<P.s)
    D = {}
    for _ in range(Q):
        t, *q = read()
        if t == 0:
            p, c, d = q
            # T[p] = P.enc(c, d)
            T[p] = D[p] = P.enc(c, d)
        else:
            l, r, x = q
            # a, b = P.dec(T.prod(l,r))
            a, b = P.dec(T[l:r])
            write((a*x+b)%mod)

    # test if the following can be run in reasonable time
    for key in D:
        assert T[key] == D[key]
    for i, key in enumerate(D):
        assert key in T
        del T[key]
        assert key not in T
        if i%10000 == 0: T._v()
    # addition of duplicate keys/values
    for p in range(Q): T.insert(0, 0)

from cp_library.ds.tree.bst.treap_monoid_cls import TreapMonoid
from cp_library.bit.pack.packer_cls import Packer
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
