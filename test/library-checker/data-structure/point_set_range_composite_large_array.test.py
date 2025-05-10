# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_set_range_composite_large_array


def main():
    mod = 998244353
    shift, mask = 30, (1<<30)-1
    N, Q = read()
    
    def op(a,b):
        ac, ad = pack_dec(a, shift, mask)
        bc, bd = pack_dec(b, shift, mask)
        return pack_enc(ac*bc%mod, (ad*bc+bd)%mod, shift)
    P, L, R, Qs = elist(Q), elist(Q), elist(Q), [None]*Q
    for i in range(Q):
        t, *q = read()
        Qs[i] = t, q
        if t == 0:
            p, c, d = q
            P.append(p)
        else:
            l, r, x = q
            L.append(l); R.append(r)
    P, L, R, V = icoord_compress_multi(P, L, R)
    P.reverse(), L.reverse(), R.reverse()
    seg = SegTree(op, 1 << shift, len(V))
    for t, q in Qs:
        if t == 0:
            _, c, d = q
            seg.set(P.pop(), pack_enc(c, d, shift))
        else:
            _, _, x = q
            a, b = pack_dec(seg.prod(L.pop(), R.pop()), shift, mask)
            write((a*x+b)%mod)

from cp_library.alg.iter.cmpr.icoord_compress_multi_fn import icoord_compress_multi
from cp_library.ds.tree.segtree_cls import SegTree
from cp_library.ds.elist_fn import elist
from cp_library.bit.pack_sm_fn import pack_dec, pack_enc
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
