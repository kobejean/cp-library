import cp_library.math.table.__header__
from cp_library.math.table.sieve_proto import SieveProtocol
from cp_library.math.table.primes_cls import Primes

class LinearSieveCounts(list[int], SieveProtocol):

    def __init__(spf, N: int):
        super().__init__([0] * (N + 1))
        exp = [0] * (N + 1)
        nxt = [0] * (N + 1)
        primes = Primes.__new__(Primes)
        spf[0], spf[1] = 0, 1
        exp[1] = 1
        for x in range(2,N+1):
            if spf[x] == 0:
                spf[x],exp[x] = x,1
                primes.append(x)
            for p in primes:
                if (y := x*p) > N or p > spf[x]: break
                spf[y] = p
                if x%p:
                    nxt[y], exp[y] = x, 1
                else:
                    nxt[y], exp[y] = nxt[x], exp[x]+1
        spf.primes = primes
        spf.exp = exp
        spf.nxt = nxt
    
    def factor_cnts(spf, N: int):
        assert N < len(spf)
        exp,nxt = spf.exp, spf.nxt
        pairs = []
        while spf[N] != N:
            pairs.append((spf[N],exp[N]))
            N = nxt[N]
        if N:
            pairs.append((spf[N],exp[N]))
        return pairs

    def factors(spf, N):
        assert N < len(spf)
        exp,nxt = spf.exp, spf.nxt
        factors = []
        while N > 1:
            factors.extend(spf[N] for _ in range(exp[N]))
            N = nxt[N]
        return factors
