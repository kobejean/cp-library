import cp_library.ds.__header__
from cp_library.ds.list.list_find_fn import list_find
from cp_library.misc.typing import _T
from typing import MutableSequence, SupportsIndex

class Deque(MutableSequence[_T]):
    def __init__(que, A = tuple(), *, maxlen=-1):
        super().__init__()
        que.cap = 1 << (maxlen-1).bit_length()
        data = [0]*que.cap
        que._sz = que._t = len(A)
        for i,a in enumerate(A): data[i] = a
        que._mask, que._h, que.maxlen, que.data = que.cap-1, 0, maxlen, data

    def __len__(que):
        return que._sz 
    
    def __contains__(que, x):
        if que._h >= que._t:
            return (list_find(que.data, x, 0, que._t) != -1
                or list_find(que.data, x, que._h, que.cap) != -1)
        else:
            return list_find(que.data, x, que._h, que._t) != -1
        
    def __getitem__(que, i: SupportsIndex) -> _T:
        assert -que._sz <= i < que._sz
        if i >= 0: return que.data[(que._h+i)&que._mask]
        else: return que.data[(que._t+i)&que._mask]
        
    def __setitem__(que, i: SupportsIndex, x):
        assert -que._sz <= i < que._sz
        if i >= 0: que.data[(que._h+i)&que._mask] = x
        else: que.data[(que._t+i)&que._mask] = x
    
    def head(que) -> _T: return que.data[que._h]

    def tail(que) -> _T: return que.data[(que._t-1)&que._mask]

    def __delitem__(que, i: SupportsIndex):
        raise NotImplemented
    
    def insert(que, i: SupportsIndex, x):
        raise NotImplemented
    
    def append(que, x):
        que.data[que._t] = x
        que._t = (que._t+1)&que._mask
        if que._sz == que.maxlen: que._h = (que._h+1)&que._mask
        else: que._sz += 1

    def appendleft(que, x):
        que._h = (que._h-1)&que._mask
        que.data[que._h] = x
        if que._sz == que.maxlen: que._t = que._h
        else: que._sz += 1

    def pop(que) -> _T:
        assert que._sz, "Deque is empty"
        que._t = (que._t-1)&que._mask
        que._sz -= 1
        return que.data[que._t]
    
    def popleft(que) -> _T:
        assert que._sz, "Deque is empty"
        x = que.data[que._h]
        que._h = (que._h+1)&que._mask
        que._sz -= 1
        return x