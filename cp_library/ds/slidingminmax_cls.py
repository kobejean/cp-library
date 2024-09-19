import cp_library.ds.__init__

from collections import deque
from typing import Any

class SlidingMinMax(deque):
    def __init__(self):
        super().__init__()
        self.minq = deque()
        self.maxq = deque()

    def append(self, x: Any) -> None:
        super().append(x)
        while self.minq and x < self.minq[-1]:
            self.minq.pop()
        self.minq.append(x)
        while self.maxq and self.maxq[-1] < x:
            self.maxq.pop()
        self.maxq.append(x)

    def popleft(self) -> Any:
        x = super().popleft()
        if x == self.minq[0]:
            self.minq.popleft()
        if x == self.maxq[0]:
            self.maxq.popleft()
        return x

    @property
    def min(self) -> Any:
        return self.minq[0]

    @property
    def max(self) -> Any:
        return self.maxq[0]
