# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_set_range_composite_large_array

def main():
    mod = 998244353
    shift, mask = 30, (1<<30)-1
    N, Q = read()
    TreapMonoid.reserve(1+Q)
    
    def op(a,b):
        ac, ad = pack_dec(a, shift, mask)
        bc, bd = pack_dec(b, shift, mask)
        return pack_enc(ac*bc%mod, (ad*bc+bd)%mod, shift)
    T = TreapMonoid(op, e := 1 << shift)
    D = {}
    for _ in range(Q):
        t, *q = read()
        if t == 0:
            p, c, d = q
            T[p] = D[p] = pack_enc(c, d, shift)
        else:
            l, r, x = q
            a, b = pack_dec(T[l:r], shift, mask)
            write((a*x+b)%mod)

    # # test if the following can be run in reasonable time
    # for i, key in enumerate(D):
    #     assert T[key] == D.get(key, e)
    #     assert T[i] == D.get(i, e)
    # for i, key in enumerate(D):
    #     assert key in T
    #     del T[key]
    #     assert key not in T
    #     if i%10000 == 0: T._validate()
    # # addition of duplicate values
    # for p in range(Q): T.insert(0, 0)

from cp_library.ds.tree.treap_monoid_cls import TreapMonoid
from cp_library.bit.pack.pack_enc_fn import pack_enc
from cp_library.bit.pack.pack_dec_fn import pack_dec
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
