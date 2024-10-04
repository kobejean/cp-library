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
    
    def mobius_inv(P, F, full=True):
        C, f = [P.N]*(1<<len(P)), F(P.N) if full else 0
        for i,p in enumerate(P):
            l = 2*(b := 1<<i)-1
            for m in range(b, b << 1):
                C[m], f = (c := C[l^m]//p), F(c)-f
        return -f if full else f