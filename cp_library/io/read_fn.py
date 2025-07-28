import cp_library.__header__
from typing import Type, Union, overload
from cp_library.misc.typing import _T, _U
import cp_library.io.__header__

@overload
def read() -> list[int]: ...
@overload
def read(spec: Type[_T], char=False) -> _T: ...
@overload
def read(spec: _U, char=False) -> _U: ...
@overload
def read(*specs: Type[_T], char=False) -> tuple[_T, ...]: ...
@overload
def read(*specs: _U, char=False) -> tuple[_U, ...]: ...
def read(*specs: Union[Type[_T],_T], char=False):
    IO.stdin.char = char
    if not specs: return IO.stdin.readnumsinto([])
    parser: _T = Parser.compile(specs[0] if len(specs) == 1 else specs)
    return parser(IO.stdin)
from cp_library.io.io_cls import IO
from cp_library.io.parser_cls import Parser