import cp_library.__header__
from cp_library.misc.typing import _T
import cp_library.ds.__header__
import cp_library.ds.tree.__header__
import cp_library.ds.tree.bit.__header__
from cp_library.ds.list.list3_cls import list3
from cp_library.ds.tree.bit.bit_base_cls import BITBase

class BIT3(BITBase[_T]):
    _lst = list3
    K = 3
    def _add(bit, i: int, x: _T) -> None: bit._d.add(i, x)
    def _op(bit, a, b): return a[0] + b[0], a[1] + b[1], a[2] + b[2]
    def _sub(bit, a, b): return a[0] - b[0], a[1] - b[1], a[2] - b[2]