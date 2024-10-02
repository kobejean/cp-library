import cp_library.math.table.__header__
from cp_library.math.table.sieve_proto import SieveProtocol
from cp_library.math.table.primes_cls import Primes

class LinearSieve(list[int], SieveProtocol):
    def __init__(spf, N):
        super().__init__([0] * (N + 1))
        spf[0], spf[1] = 0, 1
        primes = Primes.__new__(Primes)

        for i in range(2, N + 1):
            if spf[i] == 0:
                spf[i] = i
                primes.append(i)
            for p in primes:
                if p > spf[i] or i * p > N:
                    break
                spf[i * p] = p
        spf.primes = spf

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
 