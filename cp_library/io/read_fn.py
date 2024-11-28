import cp_library.io.__header__

from typing import Type, TypeVar, Union, overload
from cp_library.io.parser_cls import Parser, TokenStream, CharStream

T = TypeVar('T')
@overload
def read() -> list[int]: ...
@overload
def read(spec: int) -> list[int]: ...
@overload
def read(spec: Union[Type[T],T], char=False) -> T: ...
def read(spec: Union[Type[T],T] = None, char=False):
    if not char:
        if spec is None:
            return list(map(int, TokenStream.stream.readline().split()))
        elif isinstance(offset := spec, int):
            return [int(s)+offset for s in TokenStream.stream.readline().split()]
        else:
            stream = TokenStream()
    else:
        stream = CharStream()
    parser: T = Parser.compile(spec)
    return parser(stream)
