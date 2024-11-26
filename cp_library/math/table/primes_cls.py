import cp_library.math.table.__header__

class Primes(list[int]):
    def __init__(primes, N: int):
        super().__init__()
        spf = [0] * (N + 1)
        spf[0], spf[1] = 0, 1

        for i in range(2, N + 1):
            if spf[i] == 0:
                spf[i] = i
                primes.append(i)
            for p in primes:
                if p > spf[i] or i * p > N:
                    break
                spf[i * p] = p
        primes.spf = spf
