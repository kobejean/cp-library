import cp_library.ds.__header__

from collections import deque
from typing import Any, Iterable

class SlidingMin(deque):
    def __init__(self, *, maxlen = None):
        super().__init__(maxlen=maxlen+1)
        self.minq = deque()

    @property
    def maxlen(self):
        return super().maxlen-1

    def append(self, x: Any) -> None:
        while self.minq and x < self.minq[-1]:
            self.minq.pop()
        self.minq.append(x)
        super().append(x)
        if len(self) > self.maxlen:
            self.popleft()
    
    def appendleft(self, x: Any) -> None:
        raise NotImplementedError()
    
    def extend(self, iterable: Iterable) -> None:
        for x in iterable:
            self.append(x)

    def extendleft(self, iterable: Iterable) -> None:
        raise NotImplementedError()

    def popleft(self) -> Any:
        x = super().popleft()
        if x == self.minq[0]:
            self.minq.popleft()
        return x
    
    def pop(self) -> Any:
        raise NotImplementedError()

    @property
    def min(self) -> Any:
        return self.minq[0]
