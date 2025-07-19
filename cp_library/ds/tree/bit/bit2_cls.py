import cp_library.__header__
import cp_library.ds.__header__
import cp_library.ds.tree.__header__
import cp_library.ds.tree.bit.__header__
from cp_library.ds.list.list2_cls import list2
from cp_library.ds.tree.bit.bit_base_cls import BITBase

class BIT2(BITBase[tuple[int,int]]):
    _lst = list2
    K = 2
    def _add(bit, i, x) -> None: bit._d.add(i, x)
    def _op(bit, a, b): return a[0] + b[0], a[1] + b[1]
    def _sub(bit, a, b): return a[0] - b[0], a[1] - b[1]