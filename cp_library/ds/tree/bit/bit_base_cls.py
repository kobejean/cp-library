import cp_library.__header__
from cp_library.misc.typing import _T
from typing import Generic, Union, Callable, Optional
import cp_library.ds.__header__
import cp_library.ds.tree.__header__
import cp_library.ds.tree.bit.__header__

class BITBase(Generic[_T]):
    _lst = list
    K: int = 1
    
    def __init__(bit, v: Union[int, list[_T]], e: _T = None) -> None:
        if isinstance(v, int):
            bit._n = v
            if bit._lst is list:
                bit._d = [e]*v if e is not None else [0]*v
            elif e is not None:
                bit._d = bit._lst(*([e_]*v for e_ in e))
            else:
                bit._d = bit._lst(*([0]*v for _ in range(bit.K)))
        else:
            bit.build(v)
        bit.e = e if e is not None else (0 if bit._lst is list else tuple(0 for _ in range(bit.K)))
        bit._lb = 1 << bit._n.bit_length()

    def build(bit, data: list[_T]):
        bit._n = len(data)
        if bit._lst is list:
            bit._d = bit._lst(data)
        else:
            bit._d = bit._lst(*([data[i][j] for i in range(len(data))] for j in range(len(data[0]))))
        for i in range(bit._n):
            if (r := i | i + 1) < bit._n:
                bit._add(r, bit._d[i])

    def _add(bit, i: int, x: _T) -> None:
        bit._d[i] = bit._op(bit._d[i], x)
    
    def _op(bit, a: _T, b: _T) -> _T:
        return a + b
    
    def _sub(bit, a: _T, b: _T) -> _T:
        return a - b

    def add(bit, i: int, x: _T) -> None:
        while i < bit._n: bit._add(i, x); i |= i + 1

    def sum(bit, n: int) -> _T:
        s = bit.e
        while n: s, n = bit._op(s, bit._d[n - 1]), n & n - 1
        return s

    def sum_range(bit, l: int, r: int) -> _T:
        s = bit.e
        while r: s, r = bit._op(s, bit._d[r - 1]), r & r - 1
        while l: s, l = bit._sub(s, bit._d[l - 1]), l & l - 1
        return s

    def __len__(bit) -> int: return bit._n

    def __getitem__(bit, i: int) -> _T:
        s, l = bit._d[i], i & (i + 1)
        while l != i: s, i = bit._sub(s, bit._d[i - 1]), i - (i & -i)
        return s

    get = __getitem__

    def __setitem__(bit, i: int, x: _T) -> None:
        bit.add(i, bit._sub(x, bit[i]))

    set = __setitem__

    def prelist(bit) -> list[_T]:
        pre = [bit.e] + bit._d[:] if bit._lst is list else bit._lst(*([e_] * (bit._n + 1) for e_ in bit.e))
        for i in range(bit._n): pre[i+1] = bit._d[i]
        for i in range(bit._n + 1):
            if i & i - 1 < bit._n + 1:
                pre[i] = bit._op(pre[i], pre[i & i - 1])
        return pre

    def bisect_left(bit, v, key: Optional[Callable] = None) -> int:
        i = 0
        s = bit.e
        if v <= s: return -1
        m = bit._lb
        
        if key:
            while m := m >> 1:
                if (ni := m | i) <= bit._n and key(ns := bit._op(s, bit._d[ni - 1])) < v:
                    s, i = ns, ni
        else:
            while m := m >> 1:
                if (ni := m | i) <= bit._n and (ns := bit._op(s, bit._d[ni - 1])) < v:
                    s, i = ns, ni
        return i

    def bisect_right(bit, v, key: Optional[Callable] = None) -> int:
        i = 0
        s = bit.e
        m = bit._lb
        
        if key:
            while m := m >> 1:
                if (ni := m | i) <= bit._n and key(ns := bit._op(s, bit._d[ni - 1])) <= v:
                    s, i = ns, ni
        else:
            while m := m >> 1:
                if (ni := m | i) <= bit._n and (ns := bit._op(s, bit._d[ni - 1])) <= v:
                    s, i = ns, ni
        return i