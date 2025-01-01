from array import array
from typing import Sequence, SupportsIndex

class Bounds:
    def __init__(self, endpoints: array):
        self.endpoints = endpoints
        view = memoryview(endpoints)
        self.L = view[:-1]
        self.R = view[1:]
    

    
    def range(self, key: SupportsIndex):
        return range(self.L[key], self.R[key])

# class Partition(Sequence[list[]])