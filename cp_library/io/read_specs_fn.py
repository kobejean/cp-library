import cp_library.io.__header__

import sys
from typing import Iterator, Type, TypeVar, overload
from cp_library.io.parser_cls import Parser, TokenStream, CharStream

T = TypeVar('T')
@overload
def read(spec: int|None) -> Iterator[int]: ...
@overload
def read(spec: Type[T]|T) -> T: ...
def read(spec: Type[T]|T=None, char=False):
    match spec, char:
        case None, False:
            return map(int, input().split())
        case int(offset), False:
            return (int(s)+offset for s in input().split())
        case _, _:
            if char:
                stream = CharStream(sys.stdin)
            else:
                stream = TokenStream(sys.stdin)
            parser: T = Parser.compile(spec)
            return parser(stream)
