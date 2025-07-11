import cp_library.__header__
import cp_library.bit.__header__
import cp_library.bit.pack.__header__

class Packer:
    __slots__ = 's', 'm'
    def __init__(P, mx: int): P.s = mx.bit_length(); P.m = (1 << P.s) - 1
    def enc(P, a: int, b: int): return a << P.s | b
    def dec(P, x: int) -> tuple[int, int]: return x >> P.s, x & P.m
    def enumerate(P, A, reverse=False): P.ienumerate(A:=list(A), reverse); return A
    def ienumerate(P, A, reverse=False):
        if reverse:
            for i,a in enumerate(A): A[i] = P.enc(-a, i)
        else:
            for i,a in enumerate(A): A[i] = P.enc(a, i)
    def indices(P, A: list[int]): P.iindices(A:=list(A)); return A
    def iindices(P, A):
        for i,a in enumerate(A): A[i] = P.m&a