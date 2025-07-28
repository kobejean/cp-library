import cp_library.__header__
from types import GenericAlias
import cp_library.io.__header__

class Parsable:
    @classmethod
    def compile(cls):
        def parser(io: 'IOBase'): return cls(next(io))
        return parser
    @classmethod
    def __class_getitem__(cls, item): return GenericAlias(cls, item)