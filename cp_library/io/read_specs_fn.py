import cp_library.io.__header__

from typing import Type, TypeVar, overload
from cp_library.io.parser_cls import Parser, TokenStream, CharStream

T = TypeVar('T')
@overload
def read() -> list[int]: ...
@overload
def read(spec: int|None) -> list[int]: ...
@overload
def read(spec: Type[T]|T, char=False) -> T: ...
def read(spec: Type[T]|T=None, char=False):
    match spec, char:
        case None, False:
            return list(map(int, input().split()))
        case int(offset), False:
            return [int(s)+offset for s in input().split()]
        case _, _:
            if char:
                stream = CharStream()
            else:
                stream = TokenStream()
            parser: T = Parser.compile(spec)
            return parser(stream)
