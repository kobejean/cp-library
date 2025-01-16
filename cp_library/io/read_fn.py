import cp_library.io.__header__

from typing import Type, Union, overload
from cp_library.io.parser_cls import Parser, TokenStream, CharStream
from cp_library.misc.typing import _T

@overload
def read() -> list[int]: ...
@overload
def read(spec: int) -> list[int]: ...
@overload
def read(spec: Union[Type[_T],_T], char=False) -> _T: ...
def read(spec: Union[Type[_T],_T] = None, char=False):
    if not char:
        if spec is None:
            return map(int, TokenStream.stream.readline().split())
        elif isinstance(offset := spec, int):
            return [int(s)+offset for s in TokenStream.stream.readline().split()]
        elif spec is int:
            return int(TokenStream.stream.readline())
        else:
            stream = TokenStream()
    else:
        stream = CharStream()
    parser: _T = Parser.compile(spec)
    return parser(stream)
