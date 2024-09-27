import cp_library.alg.graph.__header__
from typing import TypeVar
from cp_library.io.parser_cls import Parsable, TokenStream

H = TypeVar('H')
class Edge(tuple, Parsable):
    @property
    def u(self) -> int: return self[0]
    @property
    def v(self) -> int: return self[1]
    @property
    def forw(self) -> H: return self[1]
    @property
    def back(self) -> H: return self[0]
    @classmethod
    def compile(cls, I=1):
        def parse(ts: TokenStream):
            return cls((int(s)+I for s in ts.line()))
        return parse