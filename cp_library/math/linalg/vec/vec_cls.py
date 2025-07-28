import cp_library.__header__
from typing import Iterable 
from cp_library.io.parsable_cls import Parsable
import cp_library.math.__header__
import cp_library.math.linalg.__header__
import cp_library.math.linalg.vec.__header__
from cp_library.math.linalg.elm_wise_mixin import ElmWiseMixin

class Vec(ElmWiseMixin, tuple, Parsable):
    def __new__(cls, *args):
        return super().__new__(cls, args[0] if len(args) == 1 and isinstance(args[0], Iterable) else args)
    @classmethod
    def compile(cls, T: type = int, N = None):
        elm = Parser.compile(T)
        if N is None:
            def parse(io: IOBase): return cls(elm(io) for _ in io.wait())
        else:
            def parse(io: IOBase): return cls(elm(io) for _ in range(N))
        return parse
from cp_library.io.io_base_cls import IOBase
from cp_library.io.parser_cls import Parser