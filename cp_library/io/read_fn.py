import cp_library.io.__header__

from typing import Iterable, Type, Union, overload
from cp_library.io.parser_cls import Parser, TokenStream, CharStream
from cp_library.misc.typing import _T

@overload
def read() -> Iterable[int]: ...
@overload
def read(spec: int) -> list[int]: ...
@overload
def read(spec: Union[Type[_T],_T], char=False) -> _T: ...
def read(spec: Union[Type[_T],_T] = None, char=False):
    if not char and spec is None:
        return map(int, TokenStream.default.line())
    parser: _T = Parser.compile(spec)
    return parser(CharStream.default if char else TokenStream.default)
