import cp_library.math.__header__
from cp_library.ds.tree.bit.bit_cls import BIT

def invcnt(A: list[int]):
    P = Packer(N := len(A))
    bit, cnt, I = BIT(N), 0, P.enumerate(A); I.sort(reverse=True)
    for i in I: cnt += bit.sum(i&P.m); bit.add(i&P.m, 1)
    return cnt
from cp_library.bit.pack.packer_cls import Packer