import cp_library.io.__header__
from typing import Type, Union
from cp_library.misc.typing import _T

def read(spec: Union[Type[_T],_T]=[int]) -> _T:
    stream = TokenStream()
    parser = Parser.compile(spec)
    return parser(stream)

from cp_library.io.parser_cls import Parser, TokenStream