---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/deque_cls.py
    title: cp_library/ds/list/deque_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/list_find_fn.py
    title: cp_library/ds/list/list_find_fn.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    from typing import TypeVar\n_T = TypeVar('T')\n_U = TypeVar('U')\n\nimport sys\n\
    \ndef list_find(lst: list, value, start = 0, stop = sys.maxsize):\n    try:\n\
    \        return lst.index(value, start, stop)\n    except:\n        return -1\n\
    from typing import MutableSequence, SupportsIndex\n\nclass Deque(MutableSequence[_T]):\n\
    \    def __init__(que, A = tuple(), *, maxlen=-1):\n        super().__init__()\n\
    \        que.cap = 1 << (maxlen-1).bit_length()\n        data = [0]*que.cap\n\
    \        que._sz = que._t = len(A)\n        for i,a in enumerate(A): data[i] =\
    \ a\n        que._mask, que._h, que.maxlen, que.data = que.cap-1, 0, maxlen, data\n\
    \n    def __len__(que):\n        return que._sz \n    \n    def __contains__(que,\
    \ x):\n        if que._h >= que._t:\n            return (list_find(que.data, x,\
    \ 0, que._t) != -1\n                or list_find(que.data, x, que._h, que.cap)\
    \ != -1)\n        else:\n            return list_find(que.data, x, que._h, que._t)\
    \ != -1\n        \n    def __getitem__(que, i: SupportsIndex) -> _T:\n       \
    \ assert -que._sz <= i < que._sz\n        if i >= 0: return que.data[(que._h+i)&que._mask]\n\
    \        else: return que.data[(que._t+i)&que._mask]\n        \n    def __setitem__(que,\
    \ i: SupportsIndex, x):\n        assert -que._sz <= i < que._sz\n        if i\
    \ >= 0: que.data[(que._h+i)&que._mask] = x\n        else: que.data[(que._t+i)&que._mask]\
    \ = x\n    \n    def head(que) -> _T: return que.data[que._h]\n\n    def tail(que)\
    \ -> _T: return que.data[(que._t-1)&que._mask]\n\n    def __delitem__(que, i:\
    \ SupportsIndex):\n        raise NotImplemented\n    \n    def insert(que, i:\
    \ SupportsIndex, x):\n        raise NotImplemented\n    \n    def append(que,\
    \ x):\n        que.data[que._t] = x\n        que._t = (que._t+1)&que._mask\n \
    \       if que._sz == que.maxlen: que._h = (que._h+1)&que._mask\n        else:\
    \ que._sz += 1\n\n    def appendleft(que, x):\n        que._h = (que._h-1)&que._mask\n\
    \        que.data[que._h] = x\n        if que._sz == que.maxlen: que._t = que._h\n\
    \        else: que._sz += 1\n\n    def pop(que) -> _T:\n        assert que._sz,\
    \ \"Deque is empty\"\n        que._t = (que._t-1)&que._mask\n        que._sz -=\
    \ 1\n        return que.data[que._t]\n    \n    def popleft(que) -> _T:\n    \
    \    assert que._sz, \"Deque is empty\"\n        x = que.data[que._h]\n      \
    \  que._h = (que._h+1)&que._mask\n        que._sz -= 1\n        return x\nfrom\
    \ typing import Iterable\n\nclass SlidingMax(Deque[_T]):\n    def __init__(self,\
    \ *, maxlen = None):\n        super().__init__(maxlen=maxlen)\n        self.maxq\
    \ = Deque(maxlen=maxlen)\n\n    def append(self, x: _T) -> None:\n        while\
    \ self.maxq and self.maxq.tail() < x: self.maxq.pop()\n        self.maxq.append(x)\n\
    \        super().append(x)\n    \n    def appendleft(self, x: _T) -> None: raise\
    \ NotImplementedError()\n    \n    def extend(self, iterable: Iterable) -> None:\n\
    \        for x in iterable: self.append(x)\n\n    def extendleft(self, iterable:\
    \ Iterable) -> None: raise NotImplementedError()\n\n    def popleft(self) -> _T:\n\
    \        x = super().popleft()\n        if x == self.maxq.head(): self.maxq.popleft()\n\
    \        return x\n    \n    def pop(self) -> _T: raise NotImplementedError()\n\
    \n    @property\n    def max(self) -> _T: return self.maxq.head()\n"
  code: "import cp_library.ds.__header__\nfrom cp_library.misc.typing import _T\n\
    from cp_library.ds.list.deque_cls import Deque\nfrom typing import Iterable\n\n\
    class SlidingMax(Deque[_T]):\n    def __init__(self, *, maxlen = None):\n    \
    \    super().__init__(maxlen=maxlen)\n        self.maxq = Deque(maxlen=maxlen)\n\
    \n    def append(self, x: _T) -> None:\n        while self.maxq and self.maxq.tail()\
    \ < x: self.maxq.pop()\n        self.maxq.append(x)\n        super().append(x)\n\
    \    \n    def appendleft(self, x: _T) -> None: raise NotImplementedError()\n\
    \    \n    def extend(self, iterable: Iterable) -> None:\n        for x in iterable:\
    \ self.append(x)\n\n    def extendleft(self, iterable: Iterable) -> None: raise\
    \ NotImplementedError()\n\n    def popleft(self) -> _T:\n        x = super().popleft()\n\
    \        if x == self.maxq.head(): self.maxq.popleft()\n        return x\n   \
    \ \n    def pop(self) -> _T: raise NotImplementedError()\n\n    @property\n  \
    \  def max(self) -> _T: return self.maxq.head()\n"
  dependsOn:
  - cp_library/ds/list/deque_cls.py
  - cp_library/ds/list/list_find_fn.py
  isVerificationFile: false
  path: cp_library/ds/slidingmax_cls.py
  requiredBy: []
  timestamp: '2025-05-21 18:01:52+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/ds/slidingmax_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/slidingmax_cls.py
- /library/cp_library/ds/slidingmax_cls.py.html
title: cp_library/ds/slidingmax_cls.py
---
