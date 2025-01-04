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
    if not char and spec is None:
        line = TokenStream.default.queue or TokenStream.stream.readline().split()
        return map(int, line)
    parser: _T = Parser.compile(spec)
    return parser(CharStream.default if char else TokenStream.default)
