import operator
from typing import Callable
import cp_library.math.table.__header__
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

    def divisor_zeta(P, A: list[int], op: Callable[[int,int], int] = operator.add):
        N = len(A)
        for p in P:
            for i in range(1, N//p+1):
                A[i*p] = op(A[i], A[i*p])
        return A
    
    def divisor_mobius(P, A: list[int], diff: Callable[[int,int], int] = operator.sub):
        N = len(A)
        for p in P:
            for i in range(N//p, 0, -1):
                A[i*p] = diff(A[i*p], A[i])
        return A
    
    def multiple_zeta(P, A: list[int], op: Callable[[int,int], int] = operator.add):
        N = len(A)
        for p in P:
            for i in range(N//p, 0, -1):
                A[i] = op(A[i*p], A[i])
        return A
    
    def multiple_mobius(P, A: list[int], diff: Callable[[int,int], int] = operator.sub):
        N = len(A)
        for p in P:
            for i in range(1, N//p+1):
                A[i] = diff(A[i], A[i*p])
        return A

