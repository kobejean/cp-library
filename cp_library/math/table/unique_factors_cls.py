import cp_library.math.table.__header__

class UniqueFactors(list[int]):
    def __init__(P, N: int):
        super().__init__()
        P.N = N
        d = 2
        while N > 1:
            if N % d == 0:
                P.append(d)
                N //= d
                while N % d == 0:
                    N //= d
            d += 1
            if d * d > N:
                if N > 1: P.append(N)
                break
    
    def mobius_inv(P, F, inclusive=True):
        D = P.N
        # codivisors of square free divisors
        C = [D]*(1<<len(P))
        f = F(D) if inclusive else 0
        for i,p in enumerate(P):
            for mask in range(bit := 1<<i, bit<<1):
                C[mask] = C[mask^bit] // p
                Fn = F(C[mask])
                f = f-Fn if mask.bit_count()&1 else f+Fn
        return f if inclusive else -f