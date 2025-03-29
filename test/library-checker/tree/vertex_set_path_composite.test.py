# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_set_path_composite

def set(hld, p, c, d, shift):
    hld.set(p, pack_enc(c, d, shift))

def query(hld, u, v, x, shift, mask, mod):
    a, b = pack_dec(hld.path_query(u, v), shift, mask)
    return (a*x+b)%mod

def ans(Q, hld, shift, mask, mod):
    for _ in range(Q):
        t, u, v, x = read()
        if t == 0:
            set(hld, u, v, x, shift)
        else:
            write(query(hld, u, v, x, shift, mask, mod))

def main():
    shift, mask = pack_sm(mod := 998244353)
    N, Q = read()
    S = [0]*N
    for i in range(N):
        a, b = read()
        S[i] = pack_enc(a, b, shift)
    T = read(Tree[N,0])

    def op(a, b):
        ac, ad = pack_dec(a, shift, mask)
        bc, bd = pack_dec(b, shift, mask)
        return pack_enc((ac*bc)%mod, (bc*ad+bd)%mod, shift)
    e = 1 << shift
    hld = HLDMonoid(T, op, e, S)
    ans(Q, hld, shift, mask, mod)


from cp_library.alg.tree.fast.hld_monoid_cls import HLDMonoid
from cp_library.alg.tree.fast.tree_cls import Tree
from cp_library.bit.pack_sm_fn import pack_dec, pack_enc, pack_sm
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
