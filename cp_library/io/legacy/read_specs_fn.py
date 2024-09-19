import cp_library.io.__init__

import sys
from typing import Type, TypeVar

T = TypeVar('T')
def read(spec: Type[T]|T=[int]) -> T:
    return parse_stream(sys.stdin, spec)

from cp_library.io.old.parse_stream_fn import parse_stream