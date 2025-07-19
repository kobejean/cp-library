# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_set_range_composite

from cp_library.ds.tree.seg.segtree_cls import SegTree


def main():
    mod = 998244353
    shift, mask = 30, (1<<30)-1
    N, Q = read()
    S = [0]*N
    for i in range(N):
        c, d = read()
        S[i] = pack_enc(c, d, shift)
    
    def op(a,b):
        ac, ad = pack_dec(a, shift, mask)
        bc, bd = pack_dec(b, shift, mask)
        return pack_enc(ac*bc%mod, (ad*bc+bd)%mod, shift)
    
    seg = SegTree(op, 1 << shift, S)
    for _ in range(Q):
        t, *q = read()
        if t == 0:
            p, c, d = q
            seg.set(p, pack_enc(c, d, shift))
        else:
            l, r, x = q
            a, b = pack_dec(seg.prod(l, r), shift, mask)
            write((a*x+b)%mod)

from cp_library.bit.pack.pack_enc_fn import pack_enc
from cp_library.bit.pack.pack_dec_fn import pack_dec
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
