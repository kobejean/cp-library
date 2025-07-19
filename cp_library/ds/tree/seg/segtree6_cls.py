import cp_library.__header__
from cp_library.misc.typing import _T
import cp_library.ds.__header__
from cp_library.ds.list.list6_cls import list6
import cp_library.ds.tree.__header__
import cp_library.ds.tree.seg.__header__
from cp_library.ds.tree.seg.segtree_cls import SegTree

class SegTree6(SegTree[_T]):
    _lst = list6
