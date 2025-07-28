import cp_library.ds.list.__header__
from cp_library.io.parsable_cls import Parsable

class ordlist(list[int], Parsable):
    def __init__(lst, S: str, base = 'a'):
        base = ord(base); super().__init__([ord(c)-base for c in S])
    @classmethod
    def compile(cls, base = 'a'):
        def parse(io: IOBase): return cls(next(io), base)
        return parse
from cp_library.io.io_base_cls import IOBase