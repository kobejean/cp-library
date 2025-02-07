import cp_library.math.__header__
from typing import Union
from cp_library.ds.bit_cls import BinaryIndexTree

def inversion_cnt(Z, N: Union[int,None] = None):
    if N is None:
        Zcomp = { v: i for i, v in enumerate(sorted(set(Z))) }
        Z, N = [Zcomp[z] for z in Z],  len(Z)

    bit = BinaryIndexTree(N)
    cnt = 0
    for z in reversed(Z):
        cnt += bit.presum(z)
        bit.add(z, 1)
    return cnt