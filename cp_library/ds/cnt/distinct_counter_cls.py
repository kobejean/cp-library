import cp_library.__header__
from collections import Counter
import cp_library.ds.__header__
import cp_library.ds.cnt.__header__

class DistinctCounter:
    def __init__(dc, Amax: int):
        dc.cnt = 0
        dc.freq = [0]*(Amax+1) if Amax < 5_000_000 else Counter()

    def add(dc, a):
        dc.cnt += dc.freq[a] == 0
        dc.freq[a] += 1

    def remove(dc, a):
        dc.freq[a] -= 1
        dc.cnt -= dc.freq[a] == 0
    
    def count(dc): return dc.cnt
