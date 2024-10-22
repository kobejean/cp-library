import cp_library.math.__header__

from cp_library.math.elm_wise_in_place_mixin import ElmWiseInPlaceMixin
from typing import Iterable

class MutVec(list, ElmWiseInPlaceMixin):

    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], Iterable):
            super().__init__(args[0])
        else:
            super().__init__(args)
    
