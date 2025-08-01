import cp_library.__header__
from typing import Iterable
from cp_library.io.parsable_cls import Parsable
import cp_library.math.__header__
import cp_library.math.linalg.__header__
import cp_library.math.linalg.mat.__header__
import cp_library.math.linalg.vec.__header__
from cp_library.math.linalg.elm_wise_in_place_mixin import ElmWiseInPlaceMixin

class MutVec(list, ElmWiseInPlaceMixin, Parsable):
    def __init__(self, *args):
        super().__init__(args[0] if len(args) == 1 and isinstance(args[0], Iterable) else args)
    @classmethod
    def compile(cls, T: type = int, N = None):
        elm = Parser.compile(T)
        if N is None:
            def parse(io: IOBase): return cls(elm(io) for _ in io.wait())
        else:
            def parse(io: IOBase):  return cls(elm(io) for _ in range(N))
        return parse
from cp_library.io.io_base_cls import IOBase
from cp_library.io.parser_cls import Parser