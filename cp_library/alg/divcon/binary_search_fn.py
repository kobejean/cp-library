import cp_library.__header__
from typing import Callable
import cp_library.alg.__header__
import cp_library.alg.divcon.__header__

def binary_search(ac: int, wa: int, judge: Callable[[int],bool]):
    if ac < wa:
        while 1<(wa-ac):
            if judge(wj := (ac+wa)>>1): ac = wj
            else: wa = wj
    else:
        while 1<(ac-wa):
            if judge(wj := (ac+wa)>>1): ac = wj
            else: wa = wj
    return ac