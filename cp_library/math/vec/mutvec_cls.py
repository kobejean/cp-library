import cp_library.math.__header__
from typing import Iterable
from cp_library.io.parser_cls import Parsable, Parser, TokenStream
from cp_library.math.vec.elm_wise_in_place_mixin import ElmWiseInPlaceMixin

class MutVec(list, ElmWiseInPlaceMixin, Parsable):
    def __init__(self, *args):
        super().__init__(args[0] if len(args) == 1 and isinstance(args[0], Iterable) else args)
    
    @classmethod
    def compile(cls, T: type = int, N = None):
        elm = Parser.compile(T)
        if N is None:
            def parse(ts: TokenStream): return cls(elm(ts) for _ in ts.wait())
        else:
            def parse(ts: TokenStream):  return cls(elm(ts) for _ in range(N))
        return parse