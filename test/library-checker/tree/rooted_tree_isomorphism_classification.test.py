# verification-helper: PROBLEM https://judge.yosupo.jp/problem/rooted_tree_isomorphism_classification

def main():
    N = rd()
    P = rdl(N-1)
    if all(i == p for i,p in enumerate(P)):
        wtn(N)
        P.append(N-1)
        wtnl(P)
        return

    H = gen(N+1)
    sz = [1]*N
    ans = [1]*N
    for i, p in rev_enumerate(P, 1):
        ans[p] = mul(ans[p], ans[i] + H[sz[i]])
        sz[p] += sz[i]
    ids = { a: i for i, a in enumerate(set(ans)) }
    for i,a in enumerate(ans):
        ans[i] = ids[a]
    wtn(len(ids))
    wtnl(ans)

def mul(a: int, b: int) -> int:
    au, ad = a >> 31, a & 0x7fffffff
    bu, bd = b >> 31, b & 0x7fffffff
    m = ad * bu + au * bd
    mu, md = m >> 30, m & 0x3fffffff
    x = (au*bu<<1) + mu + (md << 31) + ad * bd
    xu, xd = x >> 61, x & 0x1fffffffffffffff
    res = xu + xd
    return res if res < 0x1fffffffffffffff else res - 0x1fffffffffffffff

from random import randint

def gen(N: int):
    seed = randint(0, 0xffffffff)
    H = [0]*N
    for i in range(N):
        seed ^= seed<<13&0xFFFFFFFF
        seed ^= seed>>17&0xFFFFFFFF
        seed ^= seed<<5&0xFFFFFFFF
        H[i] = seed &0xFFFFFFFF
    return H

from cp_library.alg.iter.rev_enumerate_fn import rev_enumerate
from cp_library.io.fast.fast_io_fn import rd, rdl, wtn, wtnl

if __name__ == '__main__':
    main()
