import cp_library.math.__header__

from cp_library.io.parser_cls import Parsable, Parser, TokenStream
from cp_library.math.elm_wise_mixin import ElmWiseMixin
from typing import Iterable 
from math import hypot

class Vec(tuple, ElmWiseMixin, Parsable):
    def __new__(cls, *args):
        if len(args) == 1 and isinstance(args[0], Iterable):
            return super().__new__(cls, args[0])
        return super().__new__(cls, args)

    def dist(v1: 'Vec', v2: 'Vec'):
        diff = v2-v1
        return hypot(*diff)

    @classmethod
    def compile(cls, T: type = int, N = None):
        elm = Parser.compile(T)
        if N is None:
            def parse(ts: TokenStream):
                return cls(elm(ts) for _ in ts.wait())
        else:
            def parse(ts: TokenStream):
                return cls(elm(ts) for _ in range(N))
        return parse
  