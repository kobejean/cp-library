import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.cnt.__header__
from cp_library.ds.cnt.distinct_counter_cls import DistinctCounter

class RangeDistinctCounter(DistinctCounter):
    def __init__(rdc, A: list[int], Amax: int):
        super().__init__(Amax)
        rdc.A = A
        rdc.l = rdc.r = 0
    def add(rdc, i): super().add(rdc.A[i])
    def remove(rdc, i): super().remove(rdc.A[i])
    def move_query(rdc, l: int, r: int):
        while rdc.r < r: rdc.add(rdc.r); rdc.r += 1
        while l < rdc.l: rdc.l -= 1; rdc.add(rdc.l)
        while r < rdc.r: rdc.r -= 1; rdc.remove(rdc.r)
        while rdc.l < l: rdc.remove(rdc.l); rdc.l += 1
        return super().count()