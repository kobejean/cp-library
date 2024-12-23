import cp_library.math.table.__header__
from cp_library.math.mod.mint_cls import mint
from itertools import accumulate

class modcomb(list[mint]):
    fact: list[mint]
    fact_inv: list[mint]

    @staticmethod
    def precomp(N):
        fact = list(accumulate(range(1,N+1), mint.__mul__, initial=mint.one))
        fact_inv = list(accumulate(range(N,0,-1), mint.__mul__, initial=fact[N].inv))
        fact_inv.reverse()
        # table.inv = inv = [0]*(N+1)
        # inv[N] = int(table[N].inv)
        # mod = mint.mod
        # for n in range(N,0,-1):
        #     inv[n-1] = n*inv[n]%mod
        modcomb.fact, modcomb.fact_inv = fact, fact_inv

    @staticmethod
    def comb(n: int, k: int, /) -> mint:
        inv = modcomb.fact_inv
        if n < k: return mint.zero
        return (inv[k] * inv[n-k]) * modcomb.fact[n]
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
        """Returns P(n,k) mod p"""
        if n < k: return mint.zero
        return modcomb.fact[n] * modcomb.fact_inv[n-k]
    nPk = perm
    
    @staticmethod
    def catalan(n: int, /) -> mint:
        return modcomb.nCk(2*n,n) * modcomb.fact_inv[n+1]
