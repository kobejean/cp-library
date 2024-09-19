import cp_library.ds.__init__

from typing import Any, Callable, List

class SparseTable:
    def __init__(self, op: Callable[[Any, Any], Any], arr: List[Any]):
        self.n = len(arr)
        self.log = self.n.bit_length()
        self.op = op
        self.st = [[None] * (self.n-(1<<i)+1) for i in range(self.log)]
        self.st[0] = arr[:]
        
        for i in range(self.log-1):
            row, d = self.st[i], 1<<i
            for j in range(len(self.st[i+1])):
                self.st[i+1][j] = op(row[j], row[j+d])

    def query(self, l: int, r: int) -> Any:
        k = (r-l).bit_length()-1
        return self.op(self.st[k][l], self.st[k][r-(1<<k)])
    
    def __repr__(self) -> str:
        return '\n'.join(f'{i:<2d} {row}' for i,row in enumerate(self.st))
