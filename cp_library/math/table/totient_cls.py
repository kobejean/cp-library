import cp_library.math.table.__header__
from cp_library.math.table.primes_cls import Primes

class Totient(list[int]):
    def __init__(phi, N):
        super().__init__([0] * (N + 1))
        phi[0], phi[1] = 0, 1
        primes = Primes.__new__(Primes)

        for x in range(2, N + 1):
            if phi[x] == 0:
                phi[x] = x-1
                primes.append(x)
            for p in primes:
                if (y := x * p) > N: break
                if x % p == 0:
                    phi[y] = phi[x] * p
                    break
                phi[y] = phi[x] * (p-1)
        phi.primes = phi
