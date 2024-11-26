class FactorCounts(list[tuple[int,int]]):
    def __init__(self, N: int):
        pairs = []
        d = 2
        while d*d<=N:
            while N % d == 0:
                match pairs:
                    case [*_, (f,cnt)] if f == d:
                        pairs[-1] = (f,cnt+1)
                    case _:
                        pairs.append((d, 1))
                N //= d
            d += 1
        super().__init__(pairs)