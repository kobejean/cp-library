---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/list/list_find_fn.py
    title: cp_library/ds/list/list_find_fn.py
  _extendedRequiredBy:
  - icon: ':warning:'
    path: cp_library/ds/slidingmax_cls.py
    title: cp_library/ds/slidingmax_cls.py
  - icon: ':warning:'
    path: cp_library/ds/slidingmin_cls.py
    title: cp_library/ds/slidingmin_cls.py
  - icon: ':heavy_check_mark:'
    path: cp_library/ds/slidingminmax_cls.py
    title: cp_library/ds/slidingminmax_cls.py
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: test/atcoder/agc/agc038_b_sliding_min_max.test.py
    title: test/atcoder/agc/agc038_b_sliding_min_max.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \nimport sys\n\ndef list_find(lst: list, value, start = 0, stop = sys.maxsize):\n\
    \    try:\n        return lst.index(value, start, stop)\n    except:\n       \
    \ return -1\nfrom typing import TypeVar\n_T = TypeVar('T')\nfrom typing import\
    \ MutableSequence, SupportsIndex\n\nclass Deque(MutableSequence[_T]):\n    def\
    \ __init__(que, A = tuple(), *, maxlen=-1):\n        super().__init__()\n    \
    \    data = [0]*maxlen\n        que._sz = que._t = len(A)\n        for i,a in\
    \ enumerate(A): data[i] = a\n        que._h, que.maxlen, que.data = 0, maxlen,\
    \ data\n\n    def __len__(que):\n        return que._sz \n    \n    def __contains__(que,\
    \ x):\n        if que._h >= que._t:\n            return (list_find(que.data, x,\
    \ 0, que._t) != -1\n                or list_find(que.data, x, que._h, que.maxlen)\
    \ != -1)\n        else:\n            return list_find(que.data, x, que._h, que._t)\
    \ != -1\n        \n    def __getitem__(que, i: SupportsIndex) -> _T:\n       \
    \ assert -que._sz <= i < que._sz\n        if i >= 0: return que.data[(que._h+i)%que.maxlen]\n\
    \        else: return que.data[(que._t+i)%que.maxlen]\n        \n    def __setitem__(que,\
    \ i: SupportsIndex, x):\n        assert -que._sz <= i < que._sz\n        if i\
    \ >= 0: que.data[(que._h+i)%que.maxlen] = x\n        else: que.data[(que._t+i)%que.maxlen]\
    \ = x\n    \n    def head(que) -> _T: return que.data[que._h]\n\n    def tail(que)\
    \ -> _T: return que.data[(que._t-1)%que.maxlen]\n\n    def __delitem__(que, i:\
    \ SupportsIndex):\n        raise NotImplemented\n    \n    def insert(que, i:\
    \ SupportsIndex, x):\n        raise NotImplemented\n    \n    def append(que,\
    \ x):\n        que.data[t := que._t] = x\n        que._t = (t+1)%que.maxlen\n\
    \        if que._sz == que.maxlen: que._h = que._t\n        else: que._sz += 1\n\
    \n    def appendleft(que, x):\n        que._h = (que._h-1)%que.maxlen\n      \
    \  que.data[que._h] = x\n        if que._sz == que.maxlen: que._t = que._h\n \
    \       else: que._sz += 1\n\n    def pop(que) -> _T:\n        assert que._sz,\
    \ \"Deque is empty\"\n        que._t = (que._t-1)%que.maxlen\n        que._sz\
    \ -= 1\n        return que.data[que._t]\n    \n    def popleft(que) -> _T:\n \
    \       assert que._sz, \"Deque is empty\"\n        x = que.data[h := que._h]\n\
    \        que._h = (h+1)%que.maxlen\n        que._sz -= 1\n        return x\n"
  code: "import cp_library.ds.__header__\nfrom cp_library.ds.list.list_find_fn import\
    \ list_find\nfrom cp_library.misc.typing import _T\nfrom typing import MutableSequence,\
    \ SupportsIndex\n\nclass Deque(MutableSequence[_T]):\n    def __init__(que, A\
    \ = tuple(), *, maxlen=-1):\n        super().__init__()\n        data = [0]*maxlen\n\
    \        que._sz = que._t = len(A)\n        for i,a in enumerate(A): data[i] =\
    \ a\n        que._h, que.maxlen, que.data = 0, maxlen, data\n\n    def __len__(que):\n\
    \        return que._sz \n    \n    def __contains__(que, x):\n        if que._h\
    \ >= que._t:\n            return (list_find(que.data, x, 0, que._t) != -1\n  \
    \              or list_find(que.data, x, que._h, que.maxlen) != -1)\n        else:\n\
    \            return list_find(que.data, x, que._h, que._t) != -1\n        \n \
    \   def __getitem__(que, i: SupportsIndex) -> _T:\n        assert -que._sz <=\
    \ i < que._sz\n        if i >= 0: return que.data[(que._h+i)%que.maxlen]\n   \
    \     else: return que.data[(que._t+i)%que.maxlen]\n        \n    def __setitem__(que,\
    \ i: SupportsIndex, x):\n        assert -que._sz <= i < que._sz\n        if i\
    \ >= 0: que.data[(que._h+i)%que.maxlen] = x\n        else: que.data[(que._t+i)%que.maxlen]\
    \ = x\n    \n    def head(que) -> _T: return que.data[que._h]\n\n    def tail(que)\
    \ -> _T: return que.data[(que._t-1)%que.maxlen]\n\n    def __delitem__(que, i:\
    \ SupportsIndex):\n        raise NotImplemented\n    \n    def insert(que, i:\
    \ SupportsIndex, x):\n        raise NotImplemented\n    \n    def append(que,\
    \ x):\n        que.data[t := que._t] = x\n        que._t = (t+1)%que.maxlen\n\
    \        if que._sz == que.maxlen: que._h = que._t\n        else: que._sz += 1\n\
    \n    def appendleft(que, x):\n        que._h = (que._h-1)%que.maxlen\n      \
    \  que.data[que._h] = x\n        if que._sz == que.maxlen: que._t = que._h\n \
    \       else: que._sz += 1\n\n    def pop(que) -> _T:\n        assert que._sz,\
    \ \"Deque is empty\"\n        que._t = (que._t-1)%que.maxlen\n        que._sz\
    \ -= 1\n        return que.data[que._t]\n    \n    def popleft(que) -> _T:\n \
    \       assert que._sz, \"Deque is empty\"\n        x = que.data[h := que._h]\n\
    \        que._h = (h+1)%que.maxlen\n        que._sz -= 1\n        return x"
  dependsOn:
  - cp_library/ds/list/list_find_fn.py
  isVerificationFile: false
  path: cp_library/ds/list/deque_cls.py
  requiredBy:
  - cp_library/ds/slidingmin_cls.py
  - cp_library/ds/slidingmax_cls.py
  - cp_library/ds/slidingminmax_cls.py
  timestamp: '2025-03-30 20:17:47+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - test/atcoder/agc/agc038_b_sliding_min_max.test.py
documentation_of: cp_library/ds/list/deque_cls.py
layout: document
redirect_from:
- /library/cp_library/ds/list/deque_cls.py
- /library/cp_library/ds/list/deque_cls.py.html
title: cp_library/ds/list/deque_cls.py
---
