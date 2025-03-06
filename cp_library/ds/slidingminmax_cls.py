import cp_library.ds.__header__
from cp_library.misc.typing import _T
from cp_library.ds.list.deque_cls import Deque
from typing import Iterable

class SlidingMinMax(Deque[_T]):
    def __init__(self, *, maxlen):
        super().__init__(maxlen=maxlen)
        self.minq = Deque(maxlen=maxlen)
        self.maxq = Deque(maxlen=maxlen)

    def append(self, x: _T) -> None:
        while self.minq and x < self.minq.tail(): self.minq.pop()
        self.minq.append(x)
        while self.maxq and self.maxq.tail() < x: self.maxq.pop()
        self.maxq.append(x)
        super().append(x)
    
    def appendleft(self, x: _T) -> None:
        raise NotImplemented
    
    def extend(self, iterable: Iterable) -> None:
        for x in iterable: self.append(x)

    def extendleft(self, iterable: Iterable) -> None:
        raise NotImplemented

    def popleft(self) -> _T:
        x = super().popleft()
        if x == self.minq.head(): self.minq.popleft()
        if x == self.maxq.head(): self.maxq.popleft()
        return x
    
    def pop(self) -> _T: raise NotImplemented

    @property
    def min(self) -> _T: return self.minq.head()

    @property
    def max(self) -> _T: return self.maxq.head()
