
import cp_library.ds.__header__
from math import ceil, sqrt
from typing import Iterable, Iterator, MutableSequence
from cp_library.misc.typing import _T

# https://github.com/tatyam-prime/SortedSet/blob/main/BucketList.py
class BucketList(MutableSequence[_T]):
    BUCKET_RATIO = 16
    SPLIT_RATIO = 24
    
    def __init__(self, a: Iterable[_T] = []) -> None:
        a = list(a)
        n = self.size = len(a)
        num_bucket = int(ceil(sqrt(n / self.BUCKET_RATIO)))
        self.a = [a[n * i // num_bucket : n * (i + 1) // num_bucket] for i in range(num_bucket)]

    def __iter__(self) -> Iterator[_T]:
        for i in self.a:
            for j in i: yield j

    def __reversed__(self) -> Iterator[_T]:
        for i in reversed(self.a):
            for j in reversed(i): yield j
    
    def __eq__(self, other):
        if len(self) != len(other): return False
        for x, y in zip(self, other):
            if x != y: return False
        return True
    
    def __len__(self) -> int:
        return self.size
    
    def __repr__(self):
        return "BucketList" + str(self.a)
    
    def __str__(self):
        return str(list(self))

    def __contains__(self, x: _T):
        for y in self:
            if x == y: return True
        return False
    
    def _insert(self, a: list[_T], b: int, i: int, x: _T):
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.SPLIT_RATIO:
            mid = len(a) >> 1
            self.a[b:b+1] = [a[:mid], a[mid:]]

    def insert(self, i: int, x: _T):
        if self.size == 0:
            if i != 0 and i != -1: raise IndexError
            self.a = [[x]]
            self.size = 1
            return
        if i < 0:
            for b, a in enumerate(reversed(self.a)):
                i += len(a)
                if i >= 0: return self._insert(a, len(self.a) + ~b, i, x)
        else:
            for b, a in enumerate(self.a):
                if i <= len(a): return self._insert(a, b, i, x)
                i -= len(a)

    def append(self, x: _T):
        a = self.a[-1]
        return self._insert(a, len(self.a) - 1, len(a), x)
    
    def extend(self, a: Iterable[_T]):
        for x in a: self.append(x)
    
    def __getitem__(self, i: int):
        if i < 0:
            for a in reversed(self.a):
                i += len(a)
                if i >= 0: return a[i]
        else:
            for a in self.a:
                if i < len(a): return a[i]
                i -= len(a)
        raise IndexError
    
    def __setitem__(self, i: int, x: _T):
        if i < 0:
            for a in reversed(self.a):
                i += len(a)
                if i >= 0: a[i] = x
        else:
            for a in self.a:
                if i < len(a): a[i] = x
                i -= len(a)
        raise IndexError
    
    def _pop(self, a: list[_T], b: int, i: int):
        ans = a.pop(i)
        self.size -= 1
        if not a: del self.a[b]
        return ans
    
    def pop(self, i: int = -1):
        if i < 0:
            for b, a in enumerate(reversed(self.a)):
                i += len(a)
                if i >= 0: return self._pop(a, ~b, i)
        else:
            for b, a in enumerate(self.a):
                if i < len(a): return self._pop(a, b, i)
                i -= len(a)
        raise IndexError
    __delitem__ = pop

    def count(self, x: _T):
        return sum(x == y for y in self)

    def index(self, x: _T):
        for i, y in enumerate(self):
            if x == y: return i
        raise ValueError
    
    def remove(self, x: _T):
        self.pop(self.index(x))

    def clear(self):
        self.a = []
        self.size = 0

    def reverse(self):
        self.a.reverse()
        for a in self.a: a.reverse()

    def copy(self):
        return BucketList(self)
