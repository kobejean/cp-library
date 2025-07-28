import cp_library.math.table.__header__
from cp_library.bit.popcnt32_fn import popcnt32
from cp_library.ds.list.elist_fn import elist

class Submasks(list[list[int]]):
    def __init__(S,N):
        Z = 1 << N
        super().__init__([elist(popcnt32(m)) for m in range(Z)])
        for s in range(Z):
            sub = S[t := s]
            while t:
                sub.append(t)
                t = (t-1)&s
            sub.append(0)
            sub.reverse()
        