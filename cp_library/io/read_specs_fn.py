import cp_library.io.__init__

import sys
from typing import Iterator, Type, TypeVar, overload
from cp_library.io.parser_cls import Parser, TokenStream

T = TypeVar('T')
@overload
def read(spec: int|None) -> Iterator[int]: ...
@overload
def read(spec: Type[T]|T) -> T: ...
def read(spec: Type[T]|T=None):
    match spec:
        case None:
            return map(int, input().split())
        case int(i0):
            return (int(s)-i0 for s in input().split())
        case _:
            stream = TokenStream(sys.stdin)
            parser = Parser(spec)
            return parser(stream)
