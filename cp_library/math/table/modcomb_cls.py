import cp_library.math.table.__header__
from cp_library.math.mod.mint_cls import mint
from cp_library.math.nt.mod_inv_fn import mod_inv
from itertools import accumulate

class modcomb():
    fact: list[int]
    fact_inv: list[int]
    inv: list[int] = [0,1]

    @staticmethod
    def precomp(N):
        mod = mint.mod
        def mod_mul(a,b): return a*b%mod
        fact = list(accumulate(range(1,N+1), mod_mul, initial=1))
        fact_inv = list(accumulate(range(N,0,-1), mod_mul, initial=mod_inv(fact[N], mod)))
        fact_inv.reverse()
        modcomb.fact, modcomb.fact_inv = fact, fact_inv
    
    @staticmethod
    def extend_inv(N):
        N, inv, mod = N+1, modcomb.inv, mint.mod
        while len(inv) < N:
            j, k = divmod(mod, len(inv))
            inv.append(-inv[k] * j % mod)

    @staticmethod
    def factorial(n: int, /) -> mint:
        return mint(modcomb.fact[n])

    @staticmethod
    def comb(n: int, k: int, /) -> mint:
        inv, mod = modcomb.fact_inv, mint.mod
        if n < k or k < 0: return mint.zero
        return mint(inv[k] * inv[n-k] % mod * modcomb.fact[n])
    nCk = binom = comb
    
    @staticmethod
    def comb_with_replacement(n: int, k: int, /) -> mint:
        if n <= 0: return mint.zero
        return modcomb.nCk(n + k - 1, k)
    nHk = comb_with_replacement
    
    @staticmethod
    def multinom(n: int, *K: int) -> mint:
        nCk, res = modcomb.nCk, mint.one
        for k in K: res, n = res*nCk(n,k), n-k
        return res

    @staticmethod
    def perm(n: int, k: int, /) -> mint:
        '''Returns P(n,k) mod p'''
        if n < k: return mint.zero
        return mint(modcomb.fact[n] * modcomb.fact_inv[n-k])
    nPk = perm
    
    @staticmethod
    def catalan(n: int, /) -> mint:
        return mint(modcomb.nCk(2*n,n) * modcomb.fact_inv[n+1])
