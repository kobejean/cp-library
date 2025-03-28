import cp_library.ds.__header__
from typing import Any, List

class MinSparseTable:
    def __init__(self, arr: List[Any]):
        self.N = N = len(arr)
        self.log = N.bit_length()
        
        self.offsets = offsets = [0]
        for i in range(1, self.log):
            offsets.append(offsets[-1] + N - (1 << (i-1)) + 1)
            
        self.st = st = [0] * (offsets[-1] + N - (1 << (self.log-1)) + 1)
        st[:N] = arr 
        
        for i in range(self.log-1):
            start, nxt, d = offsets[i], offsets[ni:=i+1], 1 << i
            for j in range(N - (1 << ni) + 1):
                st[nxt+j] = min(st[k := start+j], st[k + d])

    def query(self, l: int, r: int) -> Any:
        k = (r-l).bit_length() - 1
        start, st = self.offsets[k], self.st
        return min(st[start + l], st[start + r - (1 << k)])
    
    def __repr__(self) -> str:
        rows, offsets, log, st = [], self.offsets, self.log, self.st
        for i in range(log):
            start = offsets[i]
            end = offsets[i+1] if i+1 < log else len(st)
            rows.append(f"{i:<2d} {st[start:end]}")
        return '\n'.join(rows)