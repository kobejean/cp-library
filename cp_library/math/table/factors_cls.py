import cp_library.__header__
import cp_library.math.__header__
import cp_library.math.table.__header__

class Factors(list[int]):
    def __init__(self, N: int):
        factors = []
        n = N
        i = 2
        while i * i <= n:
            while n % i == 0:
                factors.append(i)
                n //= i
            i += 1
        if n > 1:
            factors.append(n)
        super().__init__(factors)