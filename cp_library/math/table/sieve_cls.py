import cp_library.math.table.__header__
from functools import cached_property
from cp_library.math.table.sieve_proto import SieveProtocol
from cp_library.math.table.primes_cls import Primes

class Sieve(list[int], SieveProtocol):
    def __init__(spf, N):
        super().__init__(i for i in range(N+1))
        spf[0] = 1
        for x in range(2, N+1):
            x2 = x*x
            if x2 > N: break
            if spf[x] == x:
                for j in range(x2, N+1, x):
                    if spf[j] == j:
                        spf[j] = x
    @cached_property
    def primes(spf) -> Primes:
        gen = (x for x,f in enumerate(spf) if f == x)
        primes = Primes.__new__(Primes)
        super(Primes, primes).__init__(gen)
        return primes

    def factor_cnts(spf, N):
        assert N < len(spf)
        pairs = []
        while N > 1:
            match pairs:
                case [*_, (f,cnt)] if f == spf[N]:
                    pairs[-1] = (f,cnt+1)
                case _:
                    pairs.append((spf[N], 1))
            N //= spf[N]
        return pairs

    def factors(spf, N):
        assert N < len(spf)
        factors = []
        while N > 1:
            factors.append(spf[N])
            N //= spf[N]
        return factors
    
    def unique_factors(spf, N):
        assert N < len(spf)
        factors = []
        while N > 1:
            if factors and factors[-1] != spf[N]: 
                factors.append(spf[N])
            N //= spf[N]
        return factors
