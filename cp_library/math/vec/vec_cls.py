import cp_library.math.__header__

from cp_library.io.parser_cls import Parsable, Parser, TokenStream
from cp_library.math.vec.elm_wise_mixin import ElmWiseMixin
from typing import Iterable 

class Vec(ElmWiseMixin, tuple, Parsable):
    def __new__(cls, *args):
        if len(args) == 1 and isinstance(args[0], Iterable):
            return super().__new__(cls, args[0])
        return super().__new__(cls, args)

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
  