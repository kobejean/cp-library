import cp_library.math.__header__

from cp_library.math.elm_wise_mixin import ElmWiseMixin
from typing import Iterable

class Vec(tuple, ElmWiseMixin):
    def __new__(cls, *args):
        if len(args) == 1 and isinstance(args[0], Iterable):
            return super().__new__(cls, args[0])
        return super().__new__(cls, args)
