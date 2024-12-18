import cp_library.io.__header__

import sys
from typing import Type, TypeVar, Union

T = TypeVar('T')
def read(spec: Union[Type[T],T]=[int]) -> T:
    stream = TokenStream()
    parser = Parser.compile(spec)
    return parser(stream)

from cp_library.io.parser_cls import Parser, TokenStream