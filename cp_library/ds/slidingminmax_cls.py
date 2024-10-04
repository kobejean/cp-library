import cp_library.ds.__header__

from collections import deque
from typing import Any, Iterable

class SlidingMinMax(deque):
    def __init__(self, *, maxlen = None):
        super().__init__(maxlen=maxlen)
        self.minq = deque(maxlen=maxlen)
        self.maxq = deque(maxlen=maxlen)

    def append(self, x: Any) -> None:
        super().append(x)
        while self.minq and x < self.minq[-1]:
            self.minq.pop()
        self.minq.append(x)
        while self.maxq and self.maxq[-1] < x:
            self.maxq.pop()
        self.maxq.append(x)
    
    def appendleft(self, x: Any) -> None:
        raise NotImplementedError()
    
    def extend(self, iterable: Iterable) -> None:
        super().extend(iterable)
        for x in iterable:
            while self.minq and x < self.minq[-1]:
                self.minq.pop()
            self.minq.append(x)
            while self.maxq and self.maxq[-1] < x:
                self.maxq.pop()
            self.maxq.append(x)

    def extendleft(self, iterable: Iterable) -> None:
        raise NotImplementedError()

    def popleft(self) -> Any:
        x = super().popleft()
        if x == self.minq[0]:
            self.minq.popleft()
        if x == self.maxq[0]:
            self.maxq.popleft()
        return x
    
    def pop(self) -> Any:
        raise NotImplementedError()

    @property
    def min(self) -> Any:
        return self.minq[0]

    @property
    def max(self) -> Any:
        return self.maxq[0]
