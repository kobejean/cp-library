import cp_library.ds.__header__
from typing import Any, Callable, List

class SparseTable:
    def __init__(self, op: Callable[[Any, Any], Any], arr: List[Any]):
        self.N = N = len(arr)
        self.log = N.bit_length()
        self.op = op
        
        self.offsets = offsets = [0]
        for i in range(1, self.log):
            offsets.append(offsets[-1] + N - (1 << (i-1)) + 1)
            
        self.st = st = [0] * (offsets[-1] + N - (1 << (self.log-1)) + 1)
        st[:N] = arr 
        
        for i in range(self.log - 1):
            d = 1 << i
            start = offsets[i]
            next_start = offsets[i + 1]
            for j in range(N - (1 << (i+1)) + 1):
                st[next_start + j] = op(st[k := start+j], st[k + d])

    def query(self, l: int, r: int) -> Any:
        k = (r-l).bit_length() - 1
        start, st = self.offsets[k], self.st
        return self.op(st[start + l], st[start + r - (1 << k)])
    
    def __repr__(self) -> str:
        rows = []
        for i in range(self.log):
            start = self.offsets[i]
            end = self.offsets[i+1] if i+1 < self.log else len(self.st)
            rows.append(f"{i:<2d} {self.st[start:end]}")
        return '\n'.join(rows)