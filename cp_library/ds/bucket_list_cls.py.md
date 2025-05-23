---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://github.com/tatyam-prime/SortedSet/blob/main/BucketList.py
  bundledCode: "\n'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2578\n             https://kobejean.github.io/cp-library             \
    \  \n'''\nfrom math import ceil, sqrt\nfrom typing import Iterable, Iterator,\
    \ MutableSequence\nfrom typing import TypeVar\n_T = TypeVar('T')\n_U = TypeVar('U')\n\
    \n# https://github.com/tatyam-prime/SortedSet/blob/main/BucketList.py\nclass BucketList(MutableSequence[_T]):\n\
    \    BUCKET_RATIO = 16\n    SPLIT_RATIO = 24\n    \n    def __init__(self, a:\
    \ Iterable[_T] = []) -> None:\n        a = list(a)\n        n = self.size = len(a)\n\
    \        num_bucket = int(ceil(sqrt(n / self.BUCKET_RATIO)))\n        self.a =\
    \ [a[n * i // num_bucket : n * (i + 1) // num_bucket] for i in range(num_bucket)]\n\
    \n    def __iter__(self) -> Iterator[_T]:\n        for i in self.a:\n        \
    \    for j in i: yield j\n\n    def __reversed__(self) -> Iterator[_T]:\n    \
    \    for i in reversed(self.a):\n            for j in reversed(i): yield j\n \
    \   \n    def __eq__(self, other):\n        if len(self) != len(other): return\
    \ False\n        for x, y in zip(self, other):\n            if x != y: return\
    \ False\n        return True\n    \n    def __len__(self) -> int:\n        return\
    \ self.size\n    \n    def __repr__(self):\n        return \"BucketList\" + str(self.a)\n\
    \    \n    def __str__(self):\n        return str(list(self))\n\n    def __contains__(self,\
    \ x: _T):\n        for y in self:\n            if x == y: return True\n      \
    \  return False\n    \n    def _insert(self, a: list[_T], b: int, i: int, x: _T):\n\
    \        a.insert(i, x)\n        self.size += 1\n        if len(a) > len(self.a)\
    \ * self.SPLIT_RATIO:\n            mid = len(a) >> 1\n            self.a[b:b+1]\
    \ = [a[:mid], a[mid:]]\n\n    def insert(self, i: int, x: _T):\n        if self.size\
    \ == 0:\n            if i != 0 and i != -1: raise IndexError\n            self.a\
    \ = [[x]]\n            self.size = 1\n            return\n        if i < 0:\n\
    \            for b, a in enumerate(reversed(self.a)):\n                i += len(a)\n\
    \                if i >= 0: return self._insert(a, len(self.a) + ~b, i, x)\n \
    \       else:\n            for b, a in enumerate(self.a):\n                if\
    \ i <= len(a): return self._insert(a, b, i, x)\n                i -= len(a)\n\n\
    \    def append(self, x: _T):\n        a = self.a[-1]\n        return self._insert(a,\
    \ len(self.a) - 1, len(a), x)\n    \n    def extend(self, a: Iterable[_T]):\n\
    \        for x in a: self.append(x)\n    \n    def __getitem__(self, i: int):\n\
    \        if i < 0:\n            for a in reversed(self.a):\n                i\
    \ += len(a)\n                if i >= 0: return a[i]\n        else:\n         \
    \   for a in self.a:\n                if i < len(a): return a[i]\n           \
    \     i -= len(a)\n        raise IndexError\n    \n    def __setitem__(self, i:\
    \ int, x: _T):\n        if i < 0:\n            for a in reversed(self.a):\n  \
    \              i += len(a)\n                if i >= 0: a[i] = x\n        else:\n\
    \            for a in self.a:\n                if i < len(a): a[i] = x\n     \
    \           i -= len(a)\n        raise IndexError\n    \n    def _pop(self, a:\
    \ list[_T], b: int, i: int):\n        ans = a.pop(i)\n        self.size -= 1\n\
    \        if not a: del self.a[b]\n        return ans\n    \n    def pop(self,\
    \ i: int = -1):\n        if i < 0:\n            for b, a in enumerate(reversed(self.a)):\n\
    \                i += len(a)\n                if i >= 0: return self._pop(a, ~b,\
    \ i)\n        else:\n            for b, a in enumerate(self.a):\n            \
    \    if i < len(a): return self._pop(a, b, i)\n                i -= len(a)\n \
    \       raise IndexError\n    __delitem__ = pop\n\n    def count(self, x: _T):\n\
    \        return sum(x == y for y in self)\n\n    def index(self, x: _T):\n   \
    \     for i, y in enumerate(self):\n            if x == y: return i\n        raise\
    \ ValueError\n    \n    def remove(self, x: _T):\n        self.pop(self.index(x))\n\
    \n    def clear(self):\n        self.a = []\n        self.size = 0\n\n    def\
    \ reverse(self):\n        self.a.reverse()\n        for a in self.a: a.reverse()\n\
    \n    def copy(self):\n        return BucketList(self)\n"
  code: "\nimport cp_library.ds.__header__\nfrom math import ceil, sqrt\nfrom typing\
    \ import Iterable, Iterator, MutableSequence\nfrom cp_library.misc.typing import\
    \ _T\n\n# https://github.com/tatyam-prime/SortedSet/blob/main/BucketList.py\n\
    class BucketList(MutableSequence[_T]):\n    BUCKET_RATIO = 16\n    SPLIT_RATIO\
    \ = 24\n    \n    def __init__(self, a: Iterable[_T] = []) -> None:\n        a\
    \ = list(a)\n        n = self.size = len(a)\n        num_bucket = int(ceil(sqrt(n\
    \ / self.BUCKET_RATIO)))\n        self.a = [a[n * i // num_bucket : n * (i + 1)\
    \ // num_bucket] for i in range(num_bucket)]\n\n    def __iter__(self) -> Iterator[_T]:\n\
    \        for i in self.a:\n            for j in i: yield j\n\n    def __reversed__(self)\
    \ -> Iterator[_T]:\n        for i in reversed(self.a):\n            for j in reversed(i):\
    \ yield j\n    \n    def __eq__(self, other):\n        if len(self) != len(other):\
    \ return False\n        for x, y in zip(self, other):\n            if x != y:\
    \ return False\n        return True\n    \n    def __len__(self) -> int:\n   \
    \     return self.size\n    \n    def __repr__(self):\n        return \"BucketList\"\
    \ + str(self.a)\n    \n    def __str__(self):\n        return str(list(self))\n\
    \n    def __contains__(self, x: _T):\n        for y in self:\n            if x\
    \ == y: return True\n        return False\n    \n    def _insert(self, a: list[_T],\
    \ b: int, i: int, x: _T):\n        a.insert(i, x)\n        self.size += 1\n  \
    \      if len(a) > len(self.a) * self.SPLIT_RATIO:\n            mid = len(a) >>\
    \ 1\n            self.a[b:b+1] = [a[:mid], a[mid:]]\n\n    def insert(self, i:\
    \ int, x: _T):\n        if self.size == 0:\n            if i != 0 and i != -1:\
    \ raise IndexError\n            self.a = [[x]]\n            self.size = 1\n  \
    \          return\n        if i < 0:\n            for b, a in enumerate(reversed(self.a)):\n\
    \                i += len(a)\n                if i >= 0: return self._insert(a,\
    \ len(self.a) + ~b, i, x)\n        else:\n            for b, a in enumerate(self.a):\n\
    \                if i <= len(a): return self._insert(a, b, i, x)\n           \
    \     i -= len(a)\n\n    def append(self, x: _T):\n        a = self.a[-1]\n  \
    \      return self._insert(a, len(self.a) - 1, len(a), x)\n    \n    def extend(self,\
    \ a: Iterable[_T]):\n        for x in a: self.append(x)\n    \n    def __getitem__(self,\
    \ i: int):\n        if i < 0:\n            for a in reversed(self.a):\n      \
    \          i += len(a)\n                if i >= 0: return a[i]\n        else:\n\
    \            for a in self.a:\n                if i < len(a): return a[i]\n  \
    \              i -= len(a)\n        raise IndexError\n    \n    def __setitem__(self,\
    \ i: int, x: _T):\n        if i < 0:\n            for a in reversed(self.a):\n\
    \                i += len(a)\n                if i >= 0: a[i] = x\n        else:\n\
    \            for a in self.a:\n                if i < len(a): a[i] = x\n     \
    \           i -= len(a)\n        raise IndexError\n    \n    def _pop(self, a:\
    \ list[_T], b: int, i: int):\n        ans = a.pop(i)\n        self.size -= 1\n\
    \        if not a: del self.a[b]\n        return ans\n    \n    def pop(self,\
    \ i: int = -1):\n        if i < 0:\n            for b, a in enumerate(reversed(self.a)):\n\
    \                i += len(a)\n                if i >= 0: return self._pop(a, ~b,\
    \ i)\n        else:\n            for b, a in enumerate(self.a):\n            \
    \    if i < len(a): return self._pop(a, b, i)\n                i -= len(a)\n \
    \       raise IndexError\n    __delitem__ = pop\n\n    def count(self, x: _T):\n\
    \        return sum(x == y for y in self)\n\n    def index(self, x: _T):\n   \
    \     for i, y in enumerate(self):\n            if x == y: return i\n        raise\
    \ ValueError\n    \n    def remove(self, x: _T):\n        self.pop(self.index(x))\n\
    \n    def clear(self):\n        self.a = []\n        self.size = 0\n\n    def\
    \ reverse(self):\n        self.a.reverse()\n        for a in self.a: a.reverse()\n\
    \n    def copy(self):\n        return BucketList(self)\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/ds/bucket_list_cls.py
  requiredBy: []
  timestamp: '2025-05-23 18:57:17+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/bucket_list_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/bucket_list_cls.py
- /library/cp_library/ds/bucket_list_cls.py.html
title: cp_library/ds/bucket_list_cls.py
---
