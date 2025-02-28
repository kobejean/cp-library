import cp_library.math.table.__header__
import operator
from typing import Callable
from cp_library.ds.reserve_fn import reserve

class Primes(list[int]):
    def __init__(P, N: int):
        super().__init__()
        spf = [0] * (N + 1)
        spf[0], spf[1] = 0, 1
        reserve(P, N)

        for i in range(2, N + 1):
            if spf[i] == 0:
                spf[i] = i
                P.append(i)
            for p in P:
                if p > spf[i] or i*p > N: break
                spf[i*p] = p
        P.spf = spf

    def divisor_zeta(P, A: list[int], op: Callable[[int,int], int] = operator.add) -> list[int]:
        N = len(A)-1
        for p in P:
            for i in range(1, N//p+1): A[i*p] = op(A[i*p], A[i])
        return A
    
    def divisor_mobius(P, A: list[int], diff: Callable[[int,int], int] = operator.sub) -> list[int]:
        N = len(A)-1
        for p in P:
            for i in range(N//p, 0, -1): A[i*p] = diff(A[i*p], A[i])
        return A
    
    def multiple_zeta(P, A: list[int], op: Callable[[int,int], int] = operator.add) -> list[int]:
        N = len(A)-1
        for p in P:
            for i in range(N//p, 0, -1): A[i] = op(A[i], A[i*p])
        return A
    
    def multiple_mobius(P, A: list[int], diff: Callable[[int,int], int] = operator.sub) -> list[int]:
        N = len(A)-1
        for p in P:
            for i in range(1, N//p+1): A[i] = diff(A[i], A[i*p])
        return A
    
    def gcd_conv(P, A: list[int], B: list[int], add = operator.add, sub = operator.sub, mul = operator.mul):
        A, B = P.multiple_zeta(A, add), P.multiple_zeta(B, add)
        for i, b in enumerate(B): A[i] = mul(A[i], b)
        return P.multiple_mobius(A, sub)
    
    def lcm_conv(P, A: list[int], B: list[int], add = operator.add, sub = operator.sub, mul = operator.mul):
        A, B = P.divisor_zeta(A, add), P.divisor_zeta(B, add)
        for i, b in enumerate(B): A[i] = mul(A[i], b)
        return P.divisor_mobius(A, sub)
