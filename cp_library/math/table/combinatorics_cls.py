
from cp_library.math.mod.mint_cls import mint

from itertools import accumulate

class Combinatorics(list[mint]):
    def __init__(table, N: int):
        super().__init__(accumulate(range(1,N+1), mint.__mul__, initial=mint.one))
        table.inv = list(accumulate(
            range(N,0,-1), mint.__mul__, initial=table[N].inv
        ))[::-1]
        
        
    def combinations(table, n: int, k: int, /) -> mint:
        if n < k: return mint.zero
        return table[n] * table.inv[k] * table.inv[n - k]
    
    nCk = combinations
    
    def combinations_with_replacement(table, n: int, k: int, /) -> mint:
        if n <= 0: return mint.zero
        return table.nCk(n + k - 1, k)
    
    nHk = combinations_with_replacement
    
    def factorial(table, n: int, /) -> mint:
        return table[n]
    
    def multinomial(self, n: int, *K: int) -> mint:
        res = mint.one
        for k in K:
            res *= self.nCk(n, k)
            n -= k
        return res

    def perm(table, n: int, k: int, /) -> mint:
        """Returns P(n,k) mod p"""
        if n < k: return mint.zero
        return table[n] * table.inv[n - k]
    
    nPk = perm

    
    def catalan(table, n: int, /) -> mint:
        return table.nCk(2 * n, n) * table.inv[n + 1]
 
