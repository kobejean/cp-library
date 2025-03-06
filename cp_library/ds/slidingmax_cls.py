import cp_library.ds.__header__
from cp_library.misc.typing import _T
from cp_library.ds.list.deque_cls import Deque
from typing import Iterable

class SlidingMax(Deque[_T]):
    def __init__(self, *, maxlen = None):
        super().__init__(maxlen=maxlen)
        self.maxq = Deque(maxlen=maxlen)

    def append(self, x: _T) -> None:
        while self.maxq and self.maxq.tail() < x: self.maxq.pop()
        self.maxq.append(x)
        super().append(x)
    
    def appendleft(self, x: _T) -> None: raise NotImplementedError()
    
    def extend(self, iterable: Iterable) -> None:
        for x in iterable: self.append(x)

    def extendleft(self, iterable: Iterable) -> None: raise NotImplementedError()

    def popleft(self) -> _T:
        x = super().popleft()
        if x == self.maxq.head(): self.maxq.popleft()
        return x
    
    def pop(self) -> _T: raise NotImplementedError()

    @property
    def max(self) -> _T: return self.maxq.head()
