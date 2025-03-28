# verification-helper: PROBLEM https://judge.yosupo.jp/problem/tree_path_composite_sum

def main():
    mint.set_mod(mod := 998244353)
    N = read(int)
    A = read(list[int])
    T = read(TreeWeightedMeta[N,2,tuple[int,int,int,int]])
    shift, mask = pack_sm(N)
    smod = mod << shift

    def merge(a, b):
        return (a+b)%smod

    def edge(s, i, p, u):
        b, c = T.Wa[i], T.Xa[i]
        x, cnt = pack_dec(s, shift, mask)
        cnt += 1; x += A[u]
        return pack_enc((b*x+c*cnt)%mod, cnt, shift)
    
    dp = T.rerooting_dp(0, merge, edge)
    ans = [((d >> shift) + A[u])%mod for u,d in enumerate(dp)]
    write(*ans)

from cp_library.math.mod.mint_cls import mint
from cp_library.bit.pack_sm_fn import pack_dec, pack_enc, pack_sm
from cp_library.alg.tree.fast.tree_weighted_meta_cls import TreeWeightedMeta
from cp_library.io.read_fn import read
from cp_library.io.write_fn import write

if __name__ == '__main__':
    main()
