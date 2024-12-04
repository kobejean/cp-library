import cp_library.ds.__header__

from collections import deque
from typing import Any, Iterable

class SlidingMax(deque):
    def __init__(self, *, maxlen = None):
        super().__init__(maxlen=maxlen+1)
        self.maxq = deque()

    @property
    def maxlen(self):
        return super().maxlen-1

    def append(self, x: Any) -> None:
        while self.maxq and self.maxq[-1] < x:
            self.maxq.pop()
        self.maxq.append(x)
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
        if x == self.maxq[0]:
            self.maxq.popleft()
        return x
    
    def pop(self) -> Any:
        raise NotImplementedError()

    @property
    def max(self) -> Any:
        return self.maxq[0]
